---
type: source
source_type: laptop
title: post-scoring-agent
slug: post-scoring-agent
created: 2026-05-07
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/lib/recruitment/post-scoring-agent.ts
original_size: 17488
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---

# post-scoring-agent

_Extracted from `[[assessify|assessify]]/src/lib/recruitment/post-scoring-agent.ts` on 2026-05-14._

```typescript
// Post-interview scoring agent (Phase 1.C).
//
// Takes pasted interview transcripts or interviewer notes, scores them against
// the active post_interview rubric, and persists a structured report in the
// same ApplicationScore table used by pre-screening.

import Anthropic from "@anthropic-ai/sdk";
import { prisma } from "@/lib/db";
import { auditLog } from "@/lib/audit";
import { slackAlert } from "@/lib/slack";
import {
  compositeToRecommendation,
  scoreToTier,
  RECOMMENDATIONS,
  type FullPreScreeningReport,
  type PostInterviewReport,
  type ScoreTier,
} from "@/lib/recruitment";
import { computeComposite, parseCriteria, type Criterion } from "@/lib/recruitment/pre-scoring-agent";

const DEFAULT_MODEL = "claude-sonnet-4-6";

let _client: Anthropic | null = null;
function getClient(): Anthropic {
  if (_client) return _client;
  const apiKey = process.env.ANTHROPIC_API_KEY;
  if (!apiKey) throw new Error("ANTHROPIC_API_KEY env var not set");
  _client = new Anthropic({ apiKey });
  return _client;
}

export interface ScorePostInterviewInput {
  applicationId: string;
  transcript: string;
  sourceRef?: string | null;
  interviewDate?: string | null;
  interviewer?: string | null;
  interviewFormat?: string | null;
  durationMin?: number | null;
  actorId?: string | null;
  actorEmail?: string | null;
}

export async function scorePostInterview(input: ScorePostInterviewInput): Promise<PostInterviewReport | null> {
  try {
    return await scorePostInterviewInner(input);
  } catch (err) {
    console.error("[post-scoring-agent] failed for application", input.applicationId, err);
    await slackAlert("Recruitment post-interview scoring failed", err, {
      applicationId: input.applicationId,
      sourceRef: input.sourceRef,
    }).catch(() => {});
    return null;
  }
}

async function scorePostInterviewInner(input: ScorePostInterviewInput): Promise<PostInterviewReport | null> {
  const application = await prisma.application.findUnique({
    where: { id: input.applicationId },
    include: {
      candidate: true,
      jobRole: { include: { department: true } },
      scores: {
        where: { kind: "pre_interview" },
        orderBy: { computedAt: "desc" },
        take: 1,
        include: { rubric: true },
      },
    },
  });
  if (!application) throw new Error(`Application not found: ${input.applicationId}`);

  const rubric = await findActivePostRubric(application.jobRoleId);
  if (!rubric) {
    await slackAlert(
      "Recruitment post-scoring skipped - no active rubric",
      `No active post_interview rubric for jobRoleId=${application.jobRoleId} or global default.`,
      { applicationId: input.applicationId },
    );
    return null;
  }

  let criteria: Criterion[];
  try {
    criteria = parseCriteria(rubric.criteria);
  } catch {
    await slackAlert(
      "Recruitment post-scoring rubric malformed",
      `Could not parse criteria JSON on rubric ${rubric.id}`,
      { applicationId: input.applicationId, rubricId: rubric.id },
    );
    return null;
  }
  if (criteria.length === 0) {
    await slackAlert("Recruitment post-scoring rubric empty", `Rubric ${rubric.id} has no criteria.`, {
      applicationId: input.applicationId,
    });
    return null;
  }

  const latestPreReport = parseLatestPreReport(application.scores[0]?.breakdown);
  const prompt = buildPostInterviewPrompt({
    application,
    criteria,
    transcript: input.transcript,
    sourceRef: input.sourceRef,
    interviewDate: input.interviewDate,
    interviewer: input.interviewer,
    interviewFormat: input.interviewFormat,
    durationMin: input.durationMin,
    latestPreReport,
  });

  const client = getClient();
  const model = process.env.POST_SCORING_MODEL || process.env.PRE_SCORING_MODEL || DEFAULT_MODEL;
  const completion = await client.messages.create({
    model,
    max_tokens: 12000,
    messages: [{ role: "user", content: prompt }],
  });

  const rawText = completion.content
    .filter((c) => c.type === "text")
    .map((c) => (c as { type: "text"; text: string }).text)
    .join("\n")
    .trim();

  let report: PostInterviewReport;
  try {
    report = parsePostInterviewReport(rawText, criteria);
  } catch (err) {
    await slackAlert("Recruitment post-scoring parse failed", err, {
      applicationId: input.applicationId,
      rawExcerpt: rawText.slice(0, 500),
    });
    return null;
  }

  const scorecardForComposite = report.interviewScorecard.map((row) => ({
    key: row.key,
    label: row.label,
    weight: criteria.find((c) => c.key === row.key)?.weight ?? 0,
    score: row.score,
    commentary: row.evidence,
  }));
  const composite = computeComposite(scorecardForComposite, criteria);
  report.postScoreOutOf100 = composite;
  report.postScoreOutOf10 = +(composite / 10).toFixed(1);
  report.postRecommendation = compositeToRecommendation(composite, {
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

  await prisma.$transaction(async (tx) => {
    const alreadyCompleted = await tx.applicationStage.findFirst({
      where: { applicationId: input.applicationId, stage: "interview_completed" },
      select: { id: true },
    });
    if (!alreadyCompleted) {
      await tx.applicationStage.create({
        data: {
          applicationId: input.applicationId,
          stage: "interview_completed",
          actorId: input.actorId ?? undefined,
          notes: input.sourceRef ? `Interview transcript ingested from ${input.sourceRef}` : "Interview notes ingested",
        },
      });
    }

    await tx.applicationScore.create({
      data: {
        applicationId: input.applicationId,
        rubricId: rubric.id,
        kind: "post_interview",
        score: score01,
        tier,
        breakdown: JSON.stringify(report),
        sourceRef: input.sourceRef ?? "manual transcript",
        computedBy: "claude",
      },
    });
    await tx.application.update({
      where: { id: input.applicationId },
      data: { postScore: score01, postScoreTier: tier, currentStage: "post_scored" },
    });
    await tx.applicationStage.create({
      data: {
        applicationId: input.applicationId,
        stage: "post_scored",
        actorId: input.actorId ?? undefined,
        notes: `Post-interview scored by ${model}: ${composite.toFixed(0)}/100 (${report.postRecommendation})`,
      },
    });
  });

  await auditLog({
    userId: input.actorId ?? "system:post-scoring-agent",
    userEmail: input.actorEmail ?? "system@assessify",
    action: "recruitment.scored.post_interview",
    targetType: "Application",
    targetId: input.applicationId,
    details: {
      score: score01,
      scoreOutOf100: composite,
      tier,
      recommendation: report.postRecommendation,
      model,
      rubricId: rubric.id,
      sourceRef: input.sourceRef,
    },
  });

  return report;
}

export function buildPostInterviewPrompt(args: {
  application: {
    candidate: {
      firstName: string;
      lastName: string;
      email: string;
      noticePeriod: string | null;
      nationality: string | null;
    };
    office: string | null;
    source: string | null;
    agencyName: string | null;
    preScore: number | null;
    preScoreTier: string | null;
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
  transcript: string;
  sourceRef?: string | null;
  interviewDate?: string | null;
  interviewer?: string | null;
  interviewFormat?: string | null;
  durationMin?: number | null;
  latestPreReport?: FullPreScreeningReport | null;
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
  const jd = jdSection.trim() || role.description || "(no structured JD on file - use the role title as your anchor)";

  const criteriaSection = criteria
    .map((c, i) => {
      const guidance = c.commentaryGuidance ? `\n   Evidence guidance: ${c.commentaryGuidance}` : "";
      const flags =
        c.redFlagSignals && c.redFlagSignals.length > 0
          ? `\n   Red-flag signals to surface in criticalFindings if present: ${c.redFlagSignals.join("; ")}`
          : "";
      return `${i + 1}. ${c.label} (key: \`${c.key}\`, weight: ${c.weight}): ${c.scoringPrompt}${guidance}${flags}`;
    })
    .join("\n");

  const preScorecard =
    args.latestPreReport?.scorecard
      .map((s) => `- ${s.label} (${s.key}): ${s.score}/10 - ${s.commentary}`)
      .join("\n") ?? "(no full pre-screening scorecard available)";
  const recommendations = RECOMMENDATIONS.join('" | "');

  return `You are Janus Digital's post-interview hiring assessment analyst. Your job is to turn interview transcripts or interviewer notes into a structured, evidence-led post-interview report. You are evaluating what changed after the conversation, not re-screening the CV.

CANDIDATE
Name: ${a.candidate.firstName} ${a.candidate.lastName}
Email: ${a.candidate.email}
Nationality: ${a.candidate.nationality ?? "-"}
Notice period: ${a.candidate.noticePeriod ?? "-"}
Office: ${a.office ?? "-"}
Source: ${a.source ?? "-"}${a.agencyName ? ` (${a.agencyName})` : ""}

ROLE
Title: ${role.title}
Department: ${role.department.name}

JOB DESCRIPTION
${jd}

PRE-INTERVIEW BASELINE
Stored score: ${a.preScore != null ? `${(a.preScore * 100).toFixed(0)}/100` : "pending"}${a.preScoreTier ? ` (${a.preScoreTier})` : ""}
Scorecard:
${preScorecard}

POST-INTERVIEW RUBRIC CRITERIA (score each 0-10 with weight summing to 1.0):
${criteriaSection}

INTERVIEW METADATA
Date: ${args.interviewDate ?? "-"}
Format: ${args.interviewFormat ?? "Manual transcript / notes"}
Interviewer: ${args.interviewer ?? "-"}
Duration minutes: ${args.durationMin ?? "-"}
Source reference: ${args.sourceRef ?? "manual transcript"}

TRANSCRIPT / NOTES
${args.transcript}

OUTPUT FORMAT
Return ONE JSON object - no markdown fences, no commentary outside the JSON, no trailing text. Match this schema EXACTLY:

{
  "postScoreOutOf100": <weighted average of (criterion.score * criterion.weight * 10), result in 0..100>,
  "postScoreOutOf10": <postScoreOutOf100 / 10, one decimal>,
  "postRecommendation": "${recommendations}",
  "interviewSummary": {
    "date": "<date from metadata, or 'Not specified'>",
    "format": "<format/source>",
    "interviewer": "<interviewer name(s), or 'Not specified'>",
    "durationMin": <duration in minutes, or 0>,
    "location": "<if stated, otherwise omit>"
  },
  "interviewContext": "<2-3 paragraphs: what was covered, seniority/depth of conversation, and reliability of evidence>",
  "interviewScorecard": [
    {"key": "<criterion key from rubric>", "label": "<criterion label>", "score": <0..10>, "evidence": "<2-4 sentences grounded only in the transcript/notes>", "quotes": ["<short supporting quote or paraphrased answer>", "..."]},
    ...one entry per rubric criterion in the same order, exactly ${criteria.length} entries
  ],
  "criticalFindings": [
    {"index": 1, "title": "<finding>", "body": "<why it matters for the hire/no-hire decision>"},
    ...3-6 findings, including both positive and negative signals
  ],
  "preVsPostComparison": [
    {"dimension": "<rubric dimension or decision theme>", "preScore": <0..10 or null>, "postScore": <0..10>, "whatChanged": "<what the interview confirmed, improved, weakened, or left unresolved>"},
    ...one row per major decision dimension
  ],
  "mitigatingFactors": [
    "<specific factor that reduces risk or explains a weakness>",
    ...0-5 bullets
  ],
  "finalRecommendation": "<one decisive paragraph: hire/advance/hold/reject thesis, score, gating risks, and next action>"
}

RULES
- Use only interview transcript/notes for post-interview evidence. Use the CV/pre-screen only as baseline comparison.
- If the notes are thin or vague, say so and score conservatively.
- Quotes must be short. If exact wording is unavailable, write a concise paraphrase and do not use quotation marks.
- Do not invent answers, interviewer names, dates, deal examples, compensation numbers, or motivations.
- Be explicit about unresolved risks and what a hiring manager must verify before offer.
- Use British/Singaporean English.
- The score fields and recommendation will be recomputed by the system from interviewScorecard. Populate them anyway.

Return ONLY the JSON object.`;
}

export function parsePostInterviewReport(raw: string, criteria: Criterion[]): PostInterviewReport {
  let cleaned = raw.trim();
  if (cleaned.startsWith("```")) {
    cleaned = cleaned.replace(/^```(?:json)?\s*/i, "").replace(/```\s*$/i, "").trim();
  }
  const firstBrace = cleaned.indexOf("{");
  const lastBrace = cleaned.lastIndexOf("}");
  if (firstBrace >= 0 && lastBrace > firstBrace) {
    cleaned = cleaned.slice(firstBrace, lastBrace + 1);
  }
  const parsed = JSON.parse(cleaned) as Partial<PostInterviewReport>;
  if (typeof parsed !== "object" || parsed == null) throw new Error("response is not an object");
  if (!Array.isArray(parsed.interviewScorecard)) throw new Error("interviewScorecard must be an array");
  if (parsed.interviewScorecard.length !== criteria.length) {
    throw new Error(
      `interviewScorecard length ${parsed.interviewScorecard.length} does not match rubric criteria count ${criteria.length}`,
    );
  }

  for (const entry of parsed.interviewScorecard) {
    if (typeof entry?.key !== "string") throw new Error("interviewScorecard entry missing key");
    if (typeof entry?.score !== "number") throw new Error(`interviewScorecard entry ${entry.key} missing numeric score`);
    if (typeof entry?.label !== "string") entry.label = criteria.find((c) => c.key === entry.key)?.label ?? entry.key;
    if (typeof entry?.evidence !== "string") entry.evidence = "";
    if (!Array.isArray(entry.quotes)) entry.quotes = [];
    entry.quotes = entry.quotes.map((q) => String(q)).filter(Boolean).slice(0, 4);
  }

  if (!parsed.interviewSummary || typeof parsed.interviewSummary !== "object") {
    parsed.interviewSummary = { date: "Not specified", format: "Not specified", interviewer: "Not specified", durationMin: 0 };
  }
  if (typeof parsed.interviewSummary.date !== "string") parsed.interviewSummary.date = "Not specified";
  if (typeof parsed.interviewSummary.format !== "string") parsed.interviewSummary.format = "Not specified";
  if (typeof parsed.interviewSummary.interviewer !== "string") parsed.interviewSummary.interviewer = "Not specified";
  if (typeof parsed.interviewSummary.durationMin !== "number") parsed.interviewSummary.durationMin = 0;

  if (!Array.isArray(parsed.criticalFindings)) parsed.criticalFindings = [];
  parsed.criticalFindings = parsed.criticalFindings.map((f, i) => ({
    index: typeof f.index === "number" ? f.index : i + 1,
    title: typeof f.title === "string" ? f.title : `Finding ${i + 1}`,
    body: typeof f.body === "string" ? f.body : "",
  }));

  if (!Array.isArray(parsed.preVsPostComparison)) parsed.preVsPostComparison = [];
  parsed.preVsPostComparison = parsed.preVsPostComparison.map((row) => ({
    dimension: typeof row.dimension === "string" ? row.dimension : "",
    preScore: typeof row.preScore === "number" ? row.preScore : null,
    postScore: typeof row.postScore === "number" ? row.postScore : 0,
    whatChanged: typeof row.whatChanged === "string" ? row.whatChanged : "",
  }));

  if (!Array.isArray(parsed.mitigatingFactors)) parsed.mitigatingFactors = [];
  if (typeof parsed.interviewContext !== "string") parsed.interviewContext = "";
  if (typeof parsed.finalRecommendation !== "string") parsed.finalRecommendation = "";
  if (typeof parsed.postRecommendation !== "string" || !(RECOMMENDATIONS as readonly string[]).includes(parsed.postRecommendation)) {
    parsed.postRecommendation = "consider";
  }
  if (typeof parsed.postScoreOutOf100 !== "number") parsed.postScoreOutOf100 = 0;
  if (typeof parsed.postScoreOutOf10 !== "number") parsed.postScoreOutOf10 = parsed.postScoreOutOf100 / 10;

  return parsed as PostInterviewReport;
}

async function findActivePostRubric(jobRoleId: string) {
  const roleSpecific = await prisma.recruitmentRubric.findFirst({
    where: { kind: "post_interview", jobRoleId, isActive: true },
    orderBy: { version: "desc" },
  });
  if (roleSpecific) return roleSpecific;
  return prisma.recruitmentRubric.findFirst({
    where: { kind: "post_interview", jobRoleId: null, isActive: true },
    orderBy: { version: "desc" },
  });
}

function parseLatestPreReport(raw: string | undefined): FullPreScreeningReport | null {
  if (!raw) return null;
  try {
    const parsed = JSON.parse(raw) as Partial<FullPreScreeningReport>;
    return Array.isArray(parsed.scorecard) ? (parsed as FullPreScreeningReport) : null;
  } catch {
    return null;
  }
}

```