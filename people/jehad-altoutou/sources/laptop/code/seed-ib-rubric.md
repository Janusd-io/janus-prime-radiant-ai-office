---
type: source
source_type: laptop
title: seed-ib-rubric
slug: seed-ib-rubric
created: 2026-05-06
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/scripts/seed-ib-rubric.ts
original_size: 9126
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---

# seed-ib-rubric

_Extracted from `[[assessify|assessify]]/scripts/seed-ib-rubric.ts` on 2026-05-14._

```typescript
// Idempotent seeder for the Associate Investment Banker (REIB) pre-interview
// rubric (Phase 1.B v2). Mirrors the 10-dimension weighted scorecard HR uses
// in her actual reports (e.g. Terence Yeo Pre-Interview Assessment Package).
//
// If a JobRole with slug `associate-investment-banker-reib` exists, the
// rubric is scoped to it. Otherwise it's seeded as global with kind=
// pre_interview but jobRoleId=null — and HR can re-attach via the rubric
// admin once the role is created.

import "dotenv/config";
import { PrismaClient } from "../src/generated/prisma/client.js";
import { PrismaLibSql } from "@prisma/adapter-libsql";

const dbUrl = process.env.DATABASE_URL ?? "file:./dev.db";
const adapter = new PrismaLibSql({ url: dbUrl });
const prisma = new PrismaClient({ adapter });

const IB_CRITERIA = [
  {
    key: "real_estate_ib_experience",
    label: "Real Estate Investment Banking Experience",
    weight: 0.15,
    scoringPrompt:
      "Years and depth of direct real estate IB / advisory experience. 10 = global REIB platform (JLL, CBRE, Cushman, Brookfield, Blackstone) with deal-lead role. 7 = boutique or regional with named transactions and structuring depth. 5 = adjacent (PE, infra, fund-of-funds) with one named real estate transaction. 2 = peripheral exposure only.",
    commentaryGuidance:
      "Name specific firms, transaction names, deal sizes (USD/AED/SGD), property types (residential, retail, office, hospitality, DC), and ARGUS proficiency. Call out any REIT advisory or REIT valuation experience explicitly.",
    redFlagSignals: ["No named real estate transactions", "No exposure to institutional REIB platforms"],
  },
  {
    key: "capital_raising",
    label: "Capital Raising & Investor Engagement",
    weight: 0.15,
    scoringPrompt:
      "Programmatic fund-level fundraising vs deal-specific origination. 10 = led $100M+ institutional capital raise from sovereigns/family offices. 7 = supported large raises and engaged Tier 1 investors. 5 = deal-by-deal origination with 20+ term sheet discussions. 2 = no investor-facing experience.",
    commentaryGuidance:
      "Reference named investors engaged (Oaktree, KKR, Brookfield, sovereign wealth funds), fundraise sizes, conversion rates, and whether origination was systematic or relationship-driven.",
    redFlagSignals: ["No investor-facing experience", "Origination volume <5 term sheets"],
  },
  {
    key: "financial_modelling",
    label: "Financial Modelling & Valuation",
    weight: 0.15,
    scoringPrompt:
      "Modelling depth across LBO, IRR/MOIC, JV waterfalls, convertible bond pricing, NAV/FFO/AFFO. 10 = ARGUS Enterprise + REIT-specific valuation + LBO + structured products. 7 = strong general modelling, gap on REIT-specific. 5 = solid LBO/DCF only. 2 = no demonstrated modelling.",
    commentaryGuidance:
      "Name actuarial / CFA / CAIA progress, education honours, and the kinds of models built. Flag if ARGUS, REIT NAV, or FFO/AFFO are missing.",
    redFlagSignals: ["No quantitative coursework or certifications", "No named modelling work on CV"],
  },
  {
    key: "property_management_knowledge",
    label: "Property Management Ecosystem Knowledge",
    weight: 0.1,
    scoringPrompt:
      "Hands-on experience with or deep knowledge of property management firms (JLL, CBRE, Savills, Knight Frank), their management contract structures, fee models, and operational reporting — foundational for modelling the Operating Profit Share delta. 10 = direct PM advisory experience. 5 = adjacent operational exposure. 2 = no exposure.",
    commentaryGuidance:
      "Name PM firms worked with or alongside; describe contract structures (base fee, performance incentives, ancillary fees) the candidate has modelled.",
    redFlagSignals: ["No exposure to property management contracts or operations"],
  },
  {
    key: "proptech_ai_understanding",
    label: "PropTech / AI Platform Commercial Understanding",
    weight: 0.1,
    scoringPrompt:
      "Ability to articulate how AI-driven operational improvements translate into measurable real estate valuation uplift (NOI uplift, cap rate compression, predictive maintenance capex reduction). 10 = direct PropTech experience or commercial work pitching outcome-based platforms. 5 = adjacent technology fluency. 2 = pure financial career, no tech exposure.",
    commentaryGuidance:
      "Reference any building management systems, IoT, energy efficiency, digital twin, or outcome-based commercial models the candidate has touched.",
    redFlagSignals: ["No technology / PropTech / BMS / digital twin exposure"],
  },
  {
    key: "deal_narrative_deliverables",
    label: "Deal Narrative & Marketing Deliverables",
    weight: 0.1,
    scoringPrompt:
      "Production of institutional-grade pitch books, CIMs, management presentations, and DDQs for Tier 1 investor audiences. 10 = led deliverables for billion-dollar transactions to sovereign / Tier 1 audiences. 7 = strong deliverables on mid-market deals. 5 = JV decks or transaction docs only. 2 = no deliverable production evidence.",
    commentaryGuidance:
      "Name specific deliverables (PPM, IM, CIM, DDQ responses), transaction sizes, and audiences.",
  },
  {
    key: "cross_border_experience",
    label: "Cross-Border Transaction Experience",
    weight: 0.05,
    scoringPrompt:
      "Multi-country deal execution (especially across Janus's expansion footprint: Singapore, Dubai, GCC, China, ASEAN). 10 = led deals in 4+ countries including Janus core markets. 7 = 2–3 countries. 4 = single-country with adjacent regional exposure. 2 = single-country only.",
    commentaryGuidance: "List the specific countries and the deal types in each.",
  },
  {
    key: "ceo_support_presence",
    label: "CEO Support & Executive Presence",
    weight: 0.05,
    scoringPrompt:
      "Track record serving as direct C-suite support — anticipating needs, preparing high-stakes meetings, operating as the CEO's front-line partner with institutional allocators. 10 = chief-of-staff or direct EA-level support to a named CEO. 7 = strong C-suite-adjacent work. 4 = individual contributor / deal executor. 2 = no senior-stakeholder exposure.",
    commentaryGuidance:
      "Reference specific examples of investor-facing CEO support, board-meeting prep, or senior-stakeholder handling.",
    redFlagSignals: ["Operated only as IC / deal executor"],
  },
  {
    key: "due_diligence_process",
    label: "Due Diligence & Process Management",
    weight: 0.05,
    scoringPrompt:
      "Multi-workstream DD and VDR management for institutional-grade processes. 10 = led complex multi-workstream DD on $500M+ transactions. 7 = strong DD support on mid-market. 5 = transactional DD experience. 2 = no DD management.",
    commentaryGuidance: "Name the DD processes, VDR platforms, and counterparty advisors involved.",
  },
  {
    key: "cultural_fit_availability",
    label: "Cultural Fit, Availability & Compensation",
    weight: 0.1,
    scoringPrompt:
      "Notice period, location/relocation, language fit (English-fluent expected), and compensation alignment with the role band. 10 = immediately available + already in-market + no visa delay + competitive comp. 7 = available within 30 days. 5 = available within 60 days. 2 = relocation + visa + comp gap.",
    commentaryGuidance:
      "State the candidate's notice period, current location vs role office, nationality / visa status, and stated comp expectations vs the role band.",
  },
];

async function main() {
  console.log("Seeding Associate Investment Banker (REIB) pre-interview rubric...");

  const totalWeight = IB_CRITERIA.reduce((s, c) => s + c.weight, 0);
  if (Math.abs(totalWeight - 1) > 0.001) {
    throw new Error(`IB rubric weights sum to ${totalWeight}, must equal 1.0`);
  }

  const role = await prisma.jobRole.findUnique({
    where: { slug: "associate-investment-banker-reib" },
  });
  if (role) {
    console.log(`  Found JobRole '${role.title}' (${role.id}) — scoping rubric to it.`);
  } else {
    console.log("  No JobRole with slug 'associate-investment-banker-reib' found — skipping role-scope.");
    console.log("  Create the role in /admin/departments/[slug] and re-run, OR re-attach the rubric via the rubric editor.");
  }

  const name = "Associate Investment Banker (REIB) — pre-interview";
  const existing = await prisma.recruitmentRubric.findFirst({
    where: { name, kind: "pre_interview" },
  });

  const data = {
    name,
    kind: "pre_interview" as const,
    jobRoleId: role?.id ?? null,
    isActive: true,
    criteria: JSON.stringify(IB_CRITERIA),
    thresholdStrong: 0.85,
    thresholdMatch: 0.7,
    thresholdConsider: 0.55,
  };

  if (existing) {
    const updated = await prisma.recruitmentRubric.update({
      where: { id: existing.id },
      data,
    });
    console.log(`  ✓ Updated existing rubric ${updated.id}`);
  } else {
    const created = await prisma.recruitmentRubric.create({ data });
    console.log(`  ✓ Created rubric ${created.id}`);
  }

  console.log("Done.");
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});

```