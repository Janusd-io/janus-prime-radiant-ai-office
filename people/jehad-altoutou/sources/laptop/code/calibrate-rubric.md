---
type: source
source_type: laptop
title: calibrate-rubric
slug: calibrate-rubric
created: 2026-05-06
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/scripts/calibrate-rubric.ts
original_size: 14039
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---

# calibrate-rubric

_Extracted from `[[assessify|assessify]]/scripts/calibrate-rubric.ts` on 2026-05-14._

```typescript
// Calibration runner for the Phase 1.B v2 pre-screening agent.
//
// Reads CV samples from ~/Desktop/HR, runs each through the same prompt the
// production agent builds, and dumps the JSON report to /tmp/calibration/.
// Prints a side-by-side summary so we can compare against HR's actual
// Terence Yeo report.
//
// Run: npx tsx scripts/calibrate-rubric.ts
//
// Reads ANTHROPIC_API_KEY from .env (must be set).

import "dotenv/config";
import { promises as fs } from "fs";
import path from "path";
import os from "os";
import Anthropic from "@anthropic-ai/sdk";
import {
  buildPrompt,
  parseReport,
  computeComposite,
} from "../src/lib/recruitment/pre-scoring-agent";
import {
  compositeToRecommendation,
  RECOMMENDATION_LABEL,
} from "../src/lib/recruitment";

// The Associate Investment Banker (REIB) rubric — same 10 dimensions HR
// uses, verbatim from scripts/seed-ib-rubric.ts.
const IB_CRITERIA = [
  { key: "real_estate_ib_experience", label: "Real Estate Investment Banking Experience", weight: 0.15, scoringPrompt: "Years and depth of direct real estate IB / advisory experience. 10 = global REIB platform (JLL, CBRE, Cushman, Brookfield, Blackstone) with deal-lead role. 7 = boutique or regional with named transactions and structuring depth. 5 = adjacent (PE, infra, fund-of-funds) with one named real estate transaction. 2 = peripheral exposure only." },
  { key: "capital_raising", label: "Capital Raising & Investor Engagement", weight: 0.15, scoringPrompt: "Programmatic fund-level fundraising vs deal-specific origination. 10 = led $100M+ institutional capital raise from sovereigns/family offices. 7 = supported large raises and engaged Tier 1 investors. 5 = deal-by-deal origination with 20+ term sheet discussions. 2 = no investor-facing experience." },
  { key: "financial_modelling", label: "Financial Modelling & Valuation", weight: 0.15, scoringPrompt: "Modelling depth across LBO, IRR/MOIC, JV waterfalls, convertible bond pricing, NAV/FFO/AFFO. 10 = ARGUS Enterprise + REIT-specific valuation + LBO + structured products. 7 = strong general modelling, gap on REIT-specific. 5 = solid LBO/DCF only. 2 = no demonstrated modelling." },
  { key: "property_management_knowledge", label: "Property Management Ecosystem Knowledge", weight: 0.10, scoringPrompt: "Hands-on experience with or deep knowledge of property management firms (JLL, CBRE, Savills, Knight Frank), their management contract structures, fee models, and operational reporting — foundational for modelling the Operating Profit Share delta. 10 = direct PM advisory experience. 5 = adjacent operational exposure. 2 = no exposure." },
  { key: "proptech_ai_understanding", label: "PropTech / AI Platform Commercial Understanding", weight: 0.10, scoringPrompt: "Ability to articulate how AI-driven operational improvements translate into measurable real estate valuation uplift (NOI uplift, cap rate compression, predictive maintenance capex reduction). 10 = direct PropTech experience or commercial work pitching outcome-based platforms. 5 = adjacent technology fluency. 2 = pure financial career, no tech exposure." },
  { key: "deal_narrative_deliverables", label: "Deal Narrative & Marketing Deliverables", weight: 0.10, scoringPrompt: "Production of institutional-grade pitch books, CIMs, management presentations, and DDQs for Tier 1 investor audiences. 10 = led deliverables for billion-dollar transactions to sovereign / Tier 1 audiences. 7 = strong deliverables on mid-market deals. 5 = JV decks or transaction docs only. 2 = no deliverable production evidence." },
  { key: "cross_border_experience", label: "Cross-Border Transaction Experience", weight: 0.05, scoringPrompt: "Multi-country deal execution (especially across Janus expansion footprint: Singapore, Dubai, GCC, China, ASEAN). 10 = led deals in 4+ countries including Janus core markets. 7 = 2-3 countries. 4 = single-country with adjacent regional exposure. 2 = single-country only." },
  { key: "ceo_support_presence", label: "CEO Support & Executive Presence", weight: 0.05, scoringPrompt: "Track record serving as direct C-suite support — anticipating needs, preparing high-stakes meetings, operating as the CEO front-line partner with institutional allocators. 10 = chief-of-staff or direct EA-level support to a named CEO. 7 = strong C-suite-adjacent work. 4 = individual contributor / deal executor. 2 = no senior-stakeholder exposure." },
  { key: "due_diligence_process", label: "Due Diligence & Process Management", weight: 0.05, scoringPrompt: "Multi-workstream DD and VDR management for institutional-grade processes. 10 = led complex multi-workstream DD on $500M+ transactions. 7 = strong DD support on mid-market. 5 = transactional DD experience. 2 = no DD management." },
  { key: "cultural_fit_availability", label: "Cultural Fit, Availability & Compensation", weight: 0.10, scoringPrompt: "Notice period, location/relocation, language fit (English-fluent expected), and compensation alignment with the role band. 10 = immediately available + already in-market + no visa delay + competitive comp. 7 = available within 30 days. 5 = available within 60 days. 2 = relocation + visa + comp gap." },
];

// Stub JD matching the role HR scored Terence against (Associate Investment
// Banker — REIB at Janus Digital). Hand-distilled from her Career-Arc and
// scorecard commentary so the agent has the same context HR did.
const IB_JD = {
  title: "Associate Investment Banker",
  department: { name: "Real Estate Investment Banking (REIB)" },
  description: "Front-line partner to the CEO on capital raising, deal structuring, and institutional investor engagement for Janus Digital's PropTech-driven real estate platform.",
  jdSummary: "Janus Digital pairs physics-based AI digital twins of buildings with a 30% Operating Profit Share commercial model — capturing demonstrated efficiency gains as the platform's revenue. The Associate IB partners directly with the CEO on capital raising, structuring real estate JVs and platform-level investments, and pitching the platform to sovereign wealth funds, family offices, infrastructure funds, and global property managers (JLL / CBRE / Cushman / Savills).",
  jdResponsibilities: "- Build and maintain financial models (LBO, IRR/MOIC, REIT NAV / FFO / AFFO, Operating Profit Share)\n- Produce institutional-grade pitch books, CIMs, management presentations, DDQ responses\n- Originate and qualify investor pipeline across HNWIs, family offices, infrastructure funds, sovereigns\n- Structure real estate JVs and platform investments with property managers\n- Partner with the CEO on Tier 1 investor meetings — pre-meeting briefs, post-meeting follow-ups, weekly pipeline reviews\n- Drive multi-workstream due diligence and VDR management",
  jdRequirements: "- 3-5 years in real estate investment banking, real estate private equity, or infrastructure funds\n- ARGUS Enterprise proficiency\n- REIT valuation: NAV, FFO/AFFO, dividend discount\n- Demonstrated capital raising or origination track record at institutional scale\n- Cross-border deal execution experience (Singapore / Dubai / GCC / ASEAN)\n- English-fluent; institutional executive presence",
  jdNiceToHaves: "- CFA / CAIA charter or progress\n- Direct experience pitching property managers (JLL, CBRE, Cushman, Savills, Knight Frank)\n- PropTech / digital twin / BMS / IoT exposure\n- Chief-of-staff or direct C-suite support track record",
  jdYearsExperience: "3-5 years",
};

type CVSample = {
  label: string;
  file: string;
  candidate: { firstName: string; lastName: string; nationality: string | null; noticePeriod: string | null; office: string | null };
  isPdf: boolean;
};

const SAMPLES: CVSample[] = [
  {
    label: "Terence Yeo (Weak — HR scored 5.5/10)",
    file: "Terence Yeo Qing Kai - Weak CV.docx",
    candidate: { firstName: "Terence", lastName: "Yeo Qing Kai", nationality: "Singaporean", noticePeriod: "Immediately Available", office: "Dubai" },
    isPdf: false,
  },
  {
    label: "Wayne Ang (Borderline — HR ground truth not shared)",
    file: "Wayne Ang Wei Xuan - borderline CV.docx",
    candidate: { firstName: "Wayne", lastName: "Ang Wei Xuan", nationality: "Singaporean", noticePeriod: "60 days neg.", office: "Singapore" },
    isPdf: false,
  },
  {
    label: "Samuel Charlton (Strong — HR ground truth not shared)",
    file: "Samuel Charlton (strong cv).pdf",
    candidate: { firstName: "Samuel", lastName: "Charlton", nationality: null, noticePeriod: null, office: null },
    isPdf: true,
  },
];

const HR_DIR = path.join(os.homedir(), "Desktop", "HR");
const OUT_DIR = "/tmp/calibration";

async function loadCv(sample: CVSample): Promise<{ pdfBase64?: string; text?: string }> {
  const fp = path.join(HR_DIR, sample.file);
  if (sample.isPdf) {
    const buf = await fs.readFile(fp);
    return { pdfBase64: buf.toString("base64") };
  }
  // For .docx, convert to plain text via macOS textutil and pass as text.
  const { exec } = await import("child_process");
  const { promisify } = await import("util");
  const execP = promisify(exec);
  const tmpTxt = `/tmp/cv-${Math.random().toString(36).slice(2)}.txt`;
  await execP(`textutil -convert txt -output "${tmpTxt}" "${fp}"`);
  const text = await fs.readFile(tmpTxt, "utf-8");
  await fs.unlink(tmpTxt).catch(() => {});
  return { text };
}

async function main() {
  await fs.mkdir(OUT_DIR, { recursive: true });

  const apiKey = process.env.ANTHROPIC_API_KEY;
  if (!apiKey) throw new Error("ANTHROPIC_API_KEY not set");
  const client = new Anthropic({ apiKey });
  const model = process.env.PRE_SCORING_MODEL || "claude-sonnet-4-6";

  console.log(`Calibrating ${SAMPLES.length} CVs against the Investment Banker (REIB) rubric using model=${model}\n`);

  const summary: Array<{
    label: string;
    composite: number;
    recommendation: string;
    topThree: Array<{ label: string; score: number }>;
    bottomThree: Array<{ label: string; score: number }>;
  }> = [];

  for (const sample of SAMPLES) {
    process.stdout.write(`  ${sample.label}... `);
    const cv = await loadCv(sample);

    const stubApplication = {
      candidate: {
        firstName: sample.candidate.firstName,
        lastName: sample.candidate.lastName,
        email: `${sample.candidate.firstName.toLowerCase()}@calibration`,
        phoneNumber: null,
        nationality: sample.candidate.nationality,
        noticePeriod: sample.candidate.noticePeriod,
        office: sample.candidate.office,
        source: "agency",
        agencyName: "Calibration",
        linkedinUrl: null,
      },
      office: sample.candidate.office,
      source: "agency",
      agencyName: "Calibration",
      jobRole: IB_JD,
    };

    const prompt = buildPrompt({ application: stubApplication, criteria: IB_CRITERIA });

    const cvBlock = cv.pdfBase64
      ? { type: "document" as const, source: { type: "base64" as const, media_type: "application/pdf" as const, data: cv.pdfBase64 } }
      : { type: "document" as const, source: { type: "text" as const, media_type: "text/plain" as const, data: cv.text! } };

    const completion = await client.messages.create({
      model,
      max_tokens: 16000,
      messages: [
        {
          role: "user",
          content: [cvBlock, { type: "text", text: prompt }],
        },
      ],
    });

    const rawText = completion.content
      .filter((c) => c.type === "text")
      .map((c) => (c as { type: "text"; text: string }).text)
      .join("\n")
      .trim();

    let report;
    try {
      report = parseReport(rawText, IB_CRITERIA);
    } catch (err) {
      console.log("✗ parse failed");
      const errFile = path.join(OUT_DIR, `${slugify(sample.label)}.error.txt`);
      await fs.writeFile(errFile, `${err instanceof Error ? err.message : String(err)}\n\n--- raw ---\n${rawText}`);
      console.log(`    raw saved to ${errFile}`);
      continue;
    }

    const composite = computeComposite(report.scorecard, IB_CRITERIA);
    report.scoreOutOf100 = composite;
    report.scoreOutOf10 = +(composite / 10).toFixed(1);
    report.recommendation = compositeToRecommendation(composite, { strong: 0.85, match: 0.7, consider: 0.55 });

    const outFile = path.join(OUT_DIR, `${slugify(sample.label)}.report.json`);
    await fs.writeFile(outFile, JSON.stringify(report, null, 2));
    console.log(`✓ ${composite.toFixed(1)}/100 (${RECOMMENDATION_LABEL[report.recommendation] ?? report.recommendation})`);
    console.log(`    saved → ${outFile}`);

    const sortedScorecard = [...report.scorecard].sort((a, b) => b.score - a.score);
    summary.push({
      label: sample.label,
      composite,
      recommendation: RECOMMENDATION_LABEL[report.recommendation] ?? report.recommendation,
      topThree: sortedScorecard.slice(0, 3).map((s) => ({ label: s.label, score: s.score })),
      bottomThree: sortedScorecard.slice(-3).map((s) => ({ label: s.label, score: s.score })),
    });
  }

  console.log("\n\n=== Calibration summary ===\n");
  for (const s of summary) {
    console.log(`▸ ${s.label}`);
    console.log(`  Composite: ${s.composite.toFixed(1)}/100   →   ${s.recommendation}`);
    console.log(`  Strongest dimensions:`);
    for (const t of s.topThree) console.log(`    + ${t.label} — ${t.score.toFixed(1)}/10`);
    console.log(`  Weakest dimensions:`);
    for (const t of s.bottomThree) console.log(`    - ${t.label} — ${t.score.toFixed(1)}/10`);
    console.log();
  }

  console.log(`\nFull JSON reports in ${OUT_DIR}/`);
  console.log("HR's Terence ground truth was 5.5/10 (54.5/100) — Conditional Advance.");
  console.log("Top dimensions HR scored highest:  Cultural Fit (9.0), Cross-Border (7.0), Financial Modelling (7.0)");
  console.log("Top dimensions HR scored lowest:   Property Management (2.0), PropTech (2.0), CEO Support (4.0)");
}

function slugify(s: string): string {
  return s.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "");
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});

```