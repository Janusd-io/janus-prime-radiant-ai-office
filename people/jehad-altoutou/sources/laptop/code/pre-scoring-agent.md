---
type: source
source_type: laptop
title: pre-scoring-agent
slug: pre-scoring-agent
created: 2026-05-06
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/lib/recruitment/pre-scoring-agent.ts
original_size: 21303
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# pre-scoring-agent

_Extracted from `[[assessify|assessify]]/src/lib/recruitment/pre-scoring-agent.ts` on 2026-05-14._

```typescript
// Pre-interview scoring agent (Phase 1.B v2).
//
// Triggered fire-and-forget from the recruitment intake form-submit handler.
// Produces a full HR-equivalent pre-screening report (3-part package matching
// the format Mariam authors manually): candidate snapshot, career arc
// narrative, weighted scorecard with role-specific dimensions, structural
// gaps, why-to-hire, risk register, recommended interview questions,
// decision framework, compensation structure, 90-day onboarding plan, final
// assessment.
//
// Errors are caught + slackAlert'd — never bubble to the form submission.
// On failure the Application stays at intake_received so HR can manually
// rescore via MCP later.

import Anthropic from "@anthropic-ai/sdk";
import { prisma } from "@/lib/db";
import { auditLog } from "@/lib/audit";
import { slackAlert, sendDM, getHrSlackId, recruitmentScoredMessage } from "@/lib/slack";
import {
  compositeToRecommendation,
  scoreToTier,
  type FullPreScreeningReport,
  type Recommendation,
  type RiskSeverity,
  type ScoreTier,
  RECOMMENDATIONS,
  RISK_SEVERITIES,
} from "@/lib/recruitment";

type Criterion = {
  key: string;
  label: string;
  weight: number;
  scoringPrompt: string;
  commentaryGuidance?: string;
  redFlagSignals?: string[];
};

const DEFAULT_MODEL = "claude-sonnet-4-6";

let _client: Anthropic | null = null;
function getClient(): Anthropic {
  if (_client) return _client;
  const apiKey = process.env.ANTHROPIC_API_KEY;
  if (!apiKey) throw new Error("ANTHROPIC_API_KEY env var not set");
  _client = new Anthropic({ apiKey });
  return _client;
}

export interface ScorePreInterviewInput {
  applicationId: string;
  cvBase64: string;
  cvFileName: string;
}

export async function scorePreInterview(input: ScorePreInterviewInput): Promise<void> {
  try {
    await scorePreInterviewInner(input);
  } catch (err) {
    console.error("[pre-scoring-agent] failed for application", input.applicationId, err);
    await slackAlert("Recruitment pre-scoring failed", err, {
      applicationId: input.applicationId,
      cvFileName: input.cvFileName,
    }).catch(() => {});
  }
}

async function scorePreInterviewInner(input: ScorePreInterviewInput): Promise<void> {
  const { applicationId, cvBase64, cvFileName } = input;

  const application = await prisma.application.findUnique({
    where: { id: applicationId },
    include: {
      candidate: true,
      jobRole: { include: { department: true } },
    },
  });
  if (!application) throw new Error(`Application not found: ${applicationId}`);

  const rubric = await findActiveRubric(application.jobRoleId);
  if (!rubric) {
    await slackAlert(
      "Recruitment pre-scoring skipped — no active rubric",
      `No active pre_interview rubric for jobRoleId=${application.jobRoleId} or global default.`,
      { applicationId },
    );
    return;
  }

  let criteria: Criterion[];
  try {
    criteria = parseCriteria(rubric.criteria);
  } catch {
    await slackAlert(
      "Recruitment pre-scoring rubric malformed",
      `Could not parse criteria JSON on rubric ${rubric.id}`,
      { applicationId, rubricId: rubric.id },
    );
    return;
  }
  if (criteria.length === 0) {
    await slackAlert("Recruitment pre-scoring rubric empty", `Rubric ${rubric.id} has no criteria.`, {
      applicationId,
    });
    return;
  }

  const prompt = buildPrompt({ application, criteria });

  const client = getClient();
  const model = process.env.PRE_SCORING_MODEL || DEFAULT_MODEL;
  const completion = await client.messages.create({
    model,
    // 16K output room — the full HR-format report (10-dim scorecard +
    // structural gaps + risk register + interview questions + comp +
    // 90-day onboarding) regularly runs past 8K. 16K gives comfortable
    // headroom on Sonnet 4.6 (which supports 64K output).
    max_tokens: 16000,
    messages: [
      {
        role: "user",
        content: [
          {
            type: "document",
            source: { type: "base64", media_type: "application/pdf", data: cvBase64 },
          },
          { type: "text", text: prompt },
        ],
      },
    ],
  });

  const rawText = completion.content
    .filter((c) => c.type === "text")
    .map((c) => (c as { type: "text"; text: string }).text)
    .join("\n")
    .trim();

  let report: FullPreScreeningReport;
  try {
    report = parseReport(rawText, criteria);
  } catch (err) {
    await slackAlert("Recruitment pre-scoring parse failed", err, {
      applicationId,
      rawExcerpt: rawText.slice(0, 500),
    });
    return;
  }

  // Recompute composite + recommendation from scorecard so we don't trust the
  // model's arithmetic. Tier comes from rubric thresholds.
  const composite = computeComposite(report.scorecard, criteria);
  report.scoreOutOf100 = composite;
  report.scoreOutOf10 = +(composite / 10).toFixed(1);
  report.recommendation = compositeToRecommendation(composite, {
    strong: rubric.thresholdStrong,
    match: rubric.thresholdMatch,
    consider: rubric.thresholdConsider,
  });

  const score01 = composite / 100;
  const tier: ScoreTier = scoreToTier(score01, {
    strong: rubric.thresholdStrong,
    match: rubric.thresholdMatch,
    consider: rubric.thresholdConsider,
  });

  await prisma.applicationScore.create({
    data: {
      applicationId,
      rubricId: rubric.id,
      kind: "pre_interview",
      score: score01,
      tier,
      breakdown: JSON.stringify(report),
      sourceRef: cvFileName,
      computedBy: "claude",
    },
  });
  await prisma.application.update({
    where: { id: applicationId },
    data: { preScore: score01, preScoreTier: tier, currentStage: "pre_scored" },
  });
  await prisma.applicationStage.create({
    data: {
      applicationId,
      stage: "pre_scored",
      notes: `Pre-screen scored by ${model}: ${composite.toFixed(0)}/100 (${report.recommendation})`,
    },
  });

  await auditLog({
    userId: "system:pre-scoring-agent",
    userEmail: "system@assessify",
    action: "recruitment.scored.pre_interview",
    targetType: "Application",
    targetId: applicationId,
    details: {
      score: score01,
      scoreOutOf100: composite,
      tier,
      recommendation: report.recommendation,
      model,
      rubricId: rubric.id,
      cvFileName,
    },
  });

  try {
    const hrSlackId = await getHrSlackId();
    if (hrSlackId) {
      const baseUrl = process.env.PUBLIC_BASE_URL ?? "https://assessify.janusd.io";
      const { text, blocks } = recruitmentScoredMessage({
        applicationId,
        candidateName: `${application.candidate.firstName} ${application.candidate.lastName}`,
        roleTitle: application.jobRole.title,
        department: application.jobRole.department.name,
        office: application.office,
        source: application.source,
        agencyName: application.agencyName,
        score: score01,
        tier,
        topCriteria: pickTopCriteria(report.scorecard),
        dashboardUrl: `${baseUrl}/admin/recruitment/${applicationId}`,
      });
      await sendDM(hrSlackId, text, blocks);
    }
  } catch (err) {
    console.error("[pre-scoring-agent] Slack DM failed", err);
  }
}

// ─── Pure helpers (testable) ────────────────────────────────────────

export function parseCriteria(raw: string): Criterion[] {
  const parsed = JSON.parse(raw);
  if (!Array.isArray(parsed)) throw new Error("criteria is not an array");
  return parsed.map((c: unknown, i: number) => {
    const obj = c as Partial<Criterion>;
    if (typeof obj.key !== "string" || typeof obj.label !== "string" || typeof obj.weight !== "number") {
      throw new Error(`criterion ${i} malformed: missing key/label/weight`);
    }
    return {
      key: obj.key,
      label: obj.label,
      weight: obj.weight,
      scoringPrompt: typeof obj.scoringPrompt === "string" ? obj.scoringPrompt : obj.label,
      commentaryGuidance: typeof obj.commentaryGuidance === "string" ? obj.commentaryGuidance : undefined,
      redFlagSignals: Array.isArray(obj.redFlagSignals) ? (obj.redFlagSignals as string[]) : undefined,
    };
  });
}

export function buildPrompt(args: {
  application: {
    candidate: {
      firstName: string;
      lastName: string;
      email: string;
      phoneNumber: string | null;
      nationality: string | null;
      noticePeriod: string | null;
      office: string | null;
      source: string | null;
      agencyName: string | null;
      linkedinUrl: string | null;
    };
    office: string | null;
    source: string | null;
    agencyName: string | null;
    jobRole: {
      title: string;
      department: { name: string };
      description: string | null;
      jdSummary: string | null;
      jdResponsibilities: string | null;
      jdRequirements: string | null;
      jdNiceToHaves: string | null;
      jdYearsExperience: string | null;
    };
  };
  criteria: Criterion[];
}): string {
  const { application: a, criteria } = args;
  const role = a.jobRole;
  const fmt = (label: string, v: string | null) => (v ? `${label}: ${v}\n` : "");
  const jdSection =
    fmt("Summary", role.jdSummary) +
    fmt("Years of experience expected", role.jdYearsExperience) +
    fmt("Responsibilities", role.jdResponsibilities) +
    fmt("Requirements (must-have)", role.jdRequirements) +
    fmt("Nice to have", role.jdNiceToHaves);
  const jd = jdSection.trim() || role.description || "(no structured JD on file — use the role title as your only anchor)";

  const criteriaSection = criteria
    .map((c, i) => {
      const guidance = c.commentaryGuidance ? `\n   Commentary guidance: ${c.commentaryGuidance}` : "";
      const flags =
        c.redFlagSignals && c.redFlagSignals.length > 0
          ? `\n   Red-flag signals to surface in riskRegister if present: ${c.redFlagSignals.join("; ")}`
          : "";
      return `${i + 1}. ${c.label} (key: \`${c.key}\`, weight: ${c.weight}): ${c.scoringPrompt}${guidance}${flags}`;
    })
    .join("\n");

  const recommendations = RECOMMENDATIONS.join('" | "');
  const severities = RISK_SEVERITIES.join('" | "');

  return `You are Janus Digital's HR pre-interview assessment analyst. Your tone, format, and depth match the institutional pre-screening packages Mariam (Head of HR) authors manually for senior hires — confidential, unsparing, and grounded in CV evidence. You are NOT a generic CV screener.

CANDIDATE
Name: ${a.candidate.firstName} ${a.candidate.lastName}
Email: ${a.candidate.email}
Phone: ${a.candidate.phoneNumber ?? "—"}
Nationality: ${a.candidate.nationality ?? "—"}
Notice period: ${a.candidate.noticePeriod ?? "—"}
Office: ${a.office ?? "—"}
Source: ${a.source ?? "—"}${a.agencyName ? ` (${a.agencyName})` : ""}
LinkedIn: ${a.candidate.linkedinUrl ?? "—"}

ROLE
Title: ${role.title}
Department: ${role.department.name}

JOB DESCRIPTION
${jd}

WEIGHTED SCORECARD CRITERIA (score each 0–10 with weight summing to 1.0):
${criteriaSection}

CV: attached as a PDF document above. Read it carefully — every claim in your report must be grounded in CV evidence (transactions named, employers named, education + certifications, dates, numbers).

OUTPUT FORMAT
Return ONE JSON object — no markdown fences, no commentary outside the JSON, no trailing text. Match this schema EXACTLY:

{
  "scoreOutOf100": <weighted average of (criterion.score * criterion.weight * 10), result in 0..100>,
  "scoreOutOf10": <scoreOutOf100 / 10, one decimal>,
  "recommendation": "${recommendations}",
  "candidateSnapshot": [
    {"label": "Candidate", "value": "<full name>"},
    {"label": "Applying For", "value": "<role title — include department>"},
    {"label": "Current Role", "value": "<most recent role from CV with employer + dates, or null>"},
    {"label": "Previous Role", "value": "<prior role with employer + dates, or null>"},
    {"label": "Location", "value": "<from CV / form, with relocation status if relevant>"},
    {"label": "Experience", "value": "<years summary, e.g. '4 years across X, Y, Z'>"},
    {"label": "Education", "value": "<degree + institution + honours/grade if listed>"},
    {"label": "Certifications", "value": "<CFA, CAIA, etc. — null if none>"},
    {"label": "Notice Period", "value": "<from form>"},
    {"label": "Current Compensation", "value": "<if disclosed in CV — else null or 'Not disclosed'>"},
    {"label": "Nationality / Status", "value": "<nationality + visa/relocation note if relevant>"},
    {"label": "Source", "value": "<agency name if agency, else 'Direct application'>"}
  ],
  "careerArc": {
    "phases": [
      {"title": "Phase 1 — <descriptive label> (<years>)", "narrative": "<2-4 sentences naming employers + transactions + competencies built, mapped to JD>"},
      ...one entry per distinct career phase the CV reveals, typically 2-4 phases
    ]
  },
  "scorecard": [
    {"key": "<criterion key from rubric>", "label": "<criterion label>", "weight": <0..1>, "score": <0..10>, "commentary": "<2-4 sentence assessment grounded in CV evidence — name specific transactions, dates, or gaps. Match the depth of HR's analyst commentary, not a generic summary.>"},
    ...one entry per rubric criterion in the same order, exactly ${criteria.length} entries
  ],
  "positioningSummary": "<2-3 paragraphs synthesising the candidacy. First paragraph: candidate's headline strengths. Second paragraph: but the candidacy has these structural gaps that must be weighed carefully. Third paragraph (optional): net positioning.>",
  "structuralGaps": [
    {"title": "Gap 1 — <concise gap name>", "detail": "<why this matters for the role, what's missing, severity assessment>"},
    {"title": "Gap 2 — <gap name>", "detail": "..."},
    {"title": "Gap 3 — <gap name>", "detail": "..."}
  ],
  "whyToHire": [
    "<bullet — make the case in one specific, evidence-backed sentence each. Reference the CV.>",
    ...4-6 bullets
  ],
  "riskRegister": [
    {"risk": "<concise risk name>", "severity": "${severities}", "detail": "<2-3 sentence explanation>", "mitigation": "<concrete mitigation: training plan, vesting, structured onboarding, etc.>"},
    ...3-6 entries
  ],
  "interviewQuestions": [
    {"theme": "<theme — e.g. 'Deal Ownership'>", "question": "<the question to ask, often a multi-part probe>", "listenFor": "<what a strong vs weak answer reveals>"},
    ...4-6 entries probing the highest-leverage uncertainties
  ],
  "decisionFramework": [
    {"outcome": "<post-interview outcome scenario>", "recommendation": "<what to do>"},
    ...3-4 scenarios spanning strong / mixed / weak interview signals
  ],
  "compensation": [
    {"component": "Base Salary", "proposed": "<range>", "rationale": "<why>"},
    {"component": "Signing Bonus", "proposed": "<amount or N/A>", "rationale": "..."},
    {"component": "Performance Bonus", "proposed": "<% of base>", "rationale": "..."},
    {"component": "Equity / Phantom Equity", "proposed": "<vesting>", "rationale": "..."}
  ],
  "onboardingPlan": [
    {"phase": "Days 1-14", "title": "<phase title>", "narrative": "<3-5 sentences of concrete onboarding objectives + measurable Day-N outcomes>"},
    {"phase": "Days 15-30", "title": "...", "narrative": "..."},
    {"phase": "Days 31-60", "title": "...", "narrative": "..."},
    {"phase": "Days 61-90", "title": "...", "narrative": "..."}
  ],
  "finalAssessment": "<one closing paragraph stating the score / recommendation, the decisive interview gate, and the 'develop into the role' or 'pass' thesis>"
}

RULES
- Be unsparing. If the CV is thin, score low. If a transaction is unnamed, treat it as unverified.
- Reference specific CV evidence — employers, deal names, education with honours/grades, certifications, dates, deal sizes — by name in the commentary.
- Structural gaps are role-specific; identify what is genuinely missing for THIS role, not generic gaps.
- Risk register severities are calibrated: HIGH = role-blocking absent mitigation; MEDIUM = manageable with structured intervention; LOW = noise.
- Use British/Singaporean English (programme, organisation, optimise) to match Janus's house style.
- Do not invent CV facts. If a field isn't on the CV, write null or "Not disclosed".
- The scoreOutOf100 you write will be IGNORED — the system recomputes it from the scorecard. But populate it anyway as a sanity check.

Return ONLY the JSON object.`;
}

export function parseReport(raw: string, criteria: Criterion[]): FullPreScreeningReport {
  let cleaned = raw.trim();
  if (cleaned.startsWith("```")) {
    cleaned = cleaned.replace(/^```(?:json)?\s*/i, "").replace(/```\s*$/i, "").trim();
  }
  const firstBrace = cleaned.indexOf("{");
  const lastBrace = cleaned.lastIndexOf("}");
  if (firstBrace >= 0 && lastBrace > firstBrace) {
    cleaned = cleaned.slice(firstBrace, lastBrace + 1);
  }
  const parsed = JSON.parse(cleaned) as Partial<FullPreScreeningReport>;
  if (typeof parsed !== "object" || parsed == null) throw new Error("response is not an object");

  // Required fields
  if (!Array.isArray(parsed.scorecard)) throw new Error("scorecard must be an array");
  if (parsed.scorecard.length !== criteria.length) {
    throw new Error(`scorecard length ${parsed.scorecard.length} does not match rubric criteria count ${criteria.length}`);
  }
  for (const entry of parsed.scorecard) {
    if (typeof entry?.key !== "string") throw new Error("scorecard entry missing key");
    if (typeof entry?.score !== "number") throw new Error(`scorecard entry ${entry.key} missing numeric score`);
    if (typeof entry?.commentary !== "string") entry.commentary = "";
    if (typeof entry?.weight !== "number") {
      const fromRubric = criteria.find((c) => c.key === entry.key)?.weight;
      entry.weight = typeof fromRubric === "number" ? fromRubric : 0;
    }
    if (typeof entry?.label !== "string") {
      entry.label = criteria.find((c) => c.key === entry.key)?.label ?? entry.key;
    }
  }

  if (!Array.isArray(parsed.candidateSnapshot)) parsed.candidateSnapshot = [];
  if (!parsed.careerArc || !Array.isArray(parsed.careerArc.phases)) parsed.careerArc = { phases: [] };
  if (!Array.isArray(parsed.structuralGaps)) parsed.structuralGaps = [];
  if (!Array.isArray(parsed.whyToHire)) parsed.whyToHire = [];
  if (!Array.isArray(parsed.riskRegister)) parsed.riskRegister = [];
  if (!Array.isArray(parsed.interviewQuestions)) parsed.interviewQuestions = [];
  if (!Array.isArray(parsed.decisionFramework)) parsed.decisionFramework = [];
  if (!Array.isArray(parsed.compensation)) parsed.compensation = [];
  if (!Array.isArray(parsed.onboardingPlan)) parsed.onboardingPlan = [];
  if (typeof parsed.positioningSummary !== "string") parsed.positioningSummary = "";
  if (typeof parsed.finalAssessment !== "string") parsed.finalAssessment = "";

  // Coerce risk severities to a known value (defensive — model may shorten "MEDIUM-HIGH" to "MEDIUM HIGH" or similar)
  for (const r of parsed.riskRegister) {
    const s = String(r.severity ?? "").toUpperCase().replace(/\s+/g, "-");
    r.severity = (RISK_SEVERITIES as readonly string[]).includes(s) ? (s as RiskSeverity) : "MEDIUM";
  }

  // Coerce recommendation to a known value (the system overrides this anyway, but normalise for the unprocessed report)
  if (typeof parsed.recommendation !== "string" || !(RECOMMENDATIONS as readonly string[]).includes(parsed.recommendation)) {
    parsed.recommendation = "consider";
  }

  if (typeof parsed.scoreOutOf100 !== "number") parsed.scoreOutOf100 = 0;
  if (typeof parsed.scoreOutOf10 !== "number") parsed.scoreOutOf10 = parsed.scoreOutOf100 / 10;

  return parsed as FullPreScreeningReport;
}

/** Re-compute composite from scorecard so the system, not the model, owns
 *  the arithmetic. Each criterion contributes (score/10) * weight to a
 *  weighted average, scaled to /100. */
export function computeComposite(
  scorecard: FullPreScreeningReport["scorecard"],
  criteria: Criterion[],
): number {
  const totalWeight = criteria.reduce((s, c) => s + c.weight, 0);
  if (totalWeight <= 0) return 0;
  let weighted = 0;
  for (const c of criteria) {
    const entry = scorecard.find((e) => e.key === c.key);
    if (!entry) continue;
    const clamped = Math.max(0, Math.min(10, entry.score));
    weighted += (clamped / 10) * c.weight;
  }
  return Math.max(0, Math.min(100, (weighted / totalWeight) * 100));
}

/** Top-3 highest-scoring scorecard entries — used in Slack DM. */
export function pickTopCriteria(
  scorecard: FullPreScreeningReport["scorecard"],
): Array<{ label: string; score: number; reasoning: string }> {
  return [...scorecard]
    .sort((a, b) => b.score - a.score)
    .slice(0, 3)
    .map((c) => ({
      label: c.label,
      score: c.score / 10,
      reasoning: c.commentary,
    }));
}

async function findActiveRubric(jobRoleId: string) {
  const roleSpecific = await prisma.recruitmentRubric.findFirst({
    where: { kind: "pre_interview", jobRoleId, isActive: true },
    orderBy: { version: "desc" },
  });
  if (roleSpecific) return roleSpecific;
  return prisma.recruitmentRubric.findFirst({
    where: { kind: "pre_interview", jobRoleId: null, isActive: true },
    orderBy: { version: "desc" },
  });
}

export type { Criterion, FullPreScreeningReport, Recommendation, ScoreTier };

```