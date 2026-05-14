---
type: source
source_type: laptop
title: seed-ib-post-rubric
slug: seed-ib-post-rubric
created: 2026-05-07
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/scripts/seed-ib-post-rubric.ts
original_size: 7643
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# seed-ib-post-rubric

_Extracted from `assessify/scripts/seed-ib-post-rubric.ts` on 2026-05-14._

```typescript
// Idempotent seeder for the Associate Investment Banker (REIB)
// post-interview rubric (Phase 1.C).
//
// Mirrors the structure of the HR post-interview package in
// /Users/jehad/Desktop/HR/Alwyn_Thu_Naung_Zaw_Post_Interview.docx.
// If the REIB role exists, the rubric is role-scoped; otherwise it falls back
// to a global post_interview rubric so the scoring workflow remains usable.

import "dotenv/config";
import { PrismaClient } from "../src/generated/prisma/client.js";
import { PrismaLibSql } from "@prisma/adapter-libsql";

const dbUrl = process.env.DATABASE_URL ?? "file:./dev.db";
const adapter = new PrismaLibSql({ url: dbUrl });
const prisma = new PrismaClient({ adapter });

const POST_INTERVIEW_CRITERIA = [
  {
    key: "motivation_conviction",
    label: "Motivation & Conviction",
    weight: 0.2,
    scoringPrompt:
      "Score the candidate's genuine pull toward Janus, REIB, PropTech/AI, and the specific role. 10 = clear, prepared, mission-linked conviction with a personal thesis for why Janus now. 7 = credible interest with role-specific reasons. 5 = opportunistic but professionally curious. 2 = ambivalent, recruiter-led, or 'why not' motivation. 0 = actively misaligned or only compensation/title driven.",
    commentaryGuidance:
      "Quote or paraphrase the candidate's stated reason for taking the interview. Assess whether they can credibly pitch Janus to institutional investors with conviction.",
    redFlagSignals: [
      "No pull factor for Janus or PropTech",
      "Recruiter-led curiosity only",
      "Cannot explain why this role now",
    ],
  },
  {
    key: "re_domain_depth",
    label: "Real Estate Domain Depth",
    weight: 0.18,
    scoringPrompt:
      "Score interview-demonstrated real estate domain understanding, not CV claims. 10 = independently explains RE valuation, NOI, cap rates, asset classes, REIT/NAV concepts, and property operations. 7 = solid domain fluency with some prompted gaps. 5 = understands high-level mechanics but relies on interviewer framing. 3 = admits surface-level exposure. 0 = cannot discuss RE fundamentals.",
    commentaryGuidance:
      "Compare the candidate's own description of their RE knowledge to the pre-interview CV-based score. Flag self-downgrades or inability to substantiate named RE transactions.",
    redFlagSignals: [
      "Self-assesses RE knowledge as shallow",
      "Cannot explain own RE transactions",
      "Confuses property operations and investment concepts",
    ],
  },
  {
    key: "analytical_pitch_capability",
    label: "Analytical & Pitch Capability",
    weight: 0.18,
    scoringPrompt:
      "Score whether the candidate can absorb, extend, and communicate the Janus investment thesis. 10 = generates independent valuation/pitch insight and links operational improvement to investor outcomes. 7 = accurately explains NOI/cap-rate/valuation logic and asks useful commercial questions. 5 = follows interviewer explanation but adds little. 2 = cannot restate the model or pitch it. 0 = materially misunderstands the thesis.",
    commentaryGuidance:
      "Look for evidence of active reasoning rather than repeating the interviewer. Highlight whether the candidate can turn platform features into investor-grade value language.",
    redFlagSignals: [
      "Only repeats interviewer explanation",
      "No independent commercial insight",
      "Cannot translate product into investment value",
    ],
  },
  {
    key: "engagement_curiosity",
    label: "Engagement & Curiosity",
    weight: 0.15,
    scoringPrompt:
      "Score preparation, question quality, and active engagement. 10 = prepared, asks targeted questions about role, investors, market entry, economics, team, and first-90-day expectations. 7 = asks several relevant questions. 5 = polite engagement with limited probing. 3 = mostly passive, few questions. 0 = disengaged or unprepared.",
    commentaryGuidance:
      "Name the strongest and weakest questions asked. Note important topics the candidate should have probed but did not.",
    redFlagSignals: [
      "No prepared questions",
      "Does not ask about role expectations",
      "Passive in CEO-led conversation",
    ],
  },
  {
    key: "self_presentation_quality",
    label: "Self-Presentation Quality",
    weight: 0.14,
    scoringPrompt:
      "Score how well the candidate presents their most relevant experience for the role. 10 = concise, strategically framed, leads with the most relevant REIB/capital raising examples. 7 = coherent and mostly relevant. 5 = competent but undersells or overemphasises less relevant work. 3 = unfocused, surface-level, or misses key CV strengths. 0 = poor or contradictory self-presentation.",
    commentaryGuidance:
      "Assess whether the candidate mentioned the most relevant CV material without prompting. For REIB, watch for CapitaLand/LINK REIT/fundraise examples versus unrelated current work.",
    redFlagSignals: [
      "Best CV material left unspoken",
      "Frames experience as surface-level execution only",
      "Leads with least relevant experience",
    ],
  },
  {
    key: "ceo_support_readiness",
    label: "CEO Support & Executive Presence",
    weight: 0.15,
    scoringPrompt:
      "Score readiness to operate as the CEO's strategic right hand. 10 = proactively challenges, synthesises, asks CEO-level questions, and shows institutional presence. 7 = strong senior-stakeholder handling and thoughtful follow-ups. 5 = professional but reactive. 3 = passive listener requiring heavy direction. 0 = lacks executive presence or judgment for CEO-adjacent work.",
    commentaryGuidance:
      "Evaluate whether the candidate could support investor meetings, board-level materials, and CEO-led strategic work. Account for interview format but do not excuse passivity entirely.",
    redFlagSignals: [
      "Conversation is one-directional information transfer",
      "Does not probe strategic implications",
      "No evidence of CEO-adjacent operating style",
    ],
  },
];

async function main() {
  console.log("Seeding Associate Investment Banker (REIB) post-interview rubric...");

  const totalWeight = POST_INTERVIEW_CRITERIA.reduce((sum, criterion) => sum + criterion.weight, 0);
  if (Math.abs(totalWeight - 1) > 0.001) {
    throw new Error(`Post-interview rubric weights sum to ${totalWeight}, must equal 1.0`);
  }

  const role = await prisma.jobRole.findUnique({
    where: { slug: "associate-investment-banker-reib" },
  });
  if (role) {
    console.log(`  Found JobRole '${role.title}' (${role.id}) - scoping rubric to it.`);
  } else {
    console.log("  No REIB JobRole found - seeding as global post_interview fallback.");
  }

  const name = "Associate Investment Banker (REIB) - post-interview";
  const existing = await prisma.recruitmentRubric.findFirst({
    where: { name, kind: "post_interview" },
  });

  const data = {
    name,
    kind: "post_interview" as const,
    jobRoleId: role?.id ?? null,
    version: 1,
    isActive: true,
    criteria: JSON.stringify(POST_INTERVIEW_CRITERIA),
    thresholdStrong: 0.85,
    thresholdMatch: 0.7,
    thresholdConsider: 0.55,
  };

  if (existing) {
    const updated = await prisma.recruitmentRubric.update({
      where: { id: existing.id },
      data,
    });
    console.log(`  Updated existing rubric ${updated.id}`);
  } else {
    const created = await prisma.recruitmentRubric.create({ data });
    console.log(`  Created rubric ${created.id}`);
  }

  console.log("Done.");
}

main()
  .catch((error) => {
    console.error(error);
    process.exit(1);
  })
  .finally(async () => {
    await prisma.$disconnect();
  });

```