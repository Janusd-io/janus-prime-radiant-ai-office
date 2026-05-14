---
type: pulse
title: Gap analysis — Janus AI-Ops docs vs Simon's IMS-PRC-AI-001 v0.4
slug: 2026-05-08-ims-prc-ai-001-gap-analysis-3-dev-days-to-align
created: 2026-05-08
updated: 2026-05-14
captured_by: jehad-altoutou
audience: department
departments: [ai-office, iso]
confidence: high
sources: [10-gap-analysis-vs-simon, simon-ims-prc-ai-001-v0-4, 08-tool-evaluation-procedure, sub-process-tool-evaluation]
related: [iso-compliance-programme, iso-ims-puls, ims-enrolment, ai-tool-evaluation, ai-registry, simon-tarskih]
---

# Gap analysis — Janus AI-Ops docs vs Simon's IMS-PRC-AI-001 v0.4

On 2026-05-08 Jehad ran a side-by-side comparison of Janus's existing AI-Ops process documents (`07-MEETING-TO-TASK-WORKFLOW`, `08-TOOL-EVALUATION-PROCEDURE`, `09-PLATFORM-DEVELOPMENT-PROCESS`) against Simon's formal `IMS-PRC-AI-001 v0.4 — Management of Internal AI Tools`. Verdict: ~70% overlap. Simon's doc is the formal IMS shape; ours is the operational reality. **~3 dev-days of work** to fully align.

## The ten gaps

1. **Form codes F1-F8** — Simon expects a numbered form per stage; we have Linear AIR comments, Slack threads, Notion entries. Fix: build a form-mapping table (digital records ↔ F-codes). 1 day.
2. **Gate numbering mismatch** — Simon has 3 gates tied to 3 stages; ours has 4 gates in one block. Fix: re-distribute. Half day.
3. **Domain Expert role** — Simon names an explicit Domain Expert in Stage 3; we have Requester OR AI Ops. Fix: two-tier (Requester for simple cases, designated Domain Expert for cross-functional). Quarter day.
4. **Approval-authority hierarchy** — Simon names Head of AI Native / Head of AI Office / Department Head / IT/Security/Legal; ours says "Process Owner". Fix: lock the role mapping with [[michael-bruck]]. Half day.
5. **Stage 9 lifecycle review** — Simon covers ongoing review / suspension / de-listing (F8); **we don't cover it at all**. Fix: add as new stage to doc 08. Half day. **Biggest functional gap.**
6. **IMS-PRC reference codes** — Simon uses `IMS-PRC-AI-001`; ours uses repo file numbers. Fix: adopt Simon's naming. 15 min cosmetic.
7. **Appendix A publication** — Simon references "Appendix A" for detailed gate criteria; ours lives only inside the `/ai-tool-evaluation` skill. Fix: publish a standalone Appendix A doc the auditor can read. Half day.
8. **Personal accounts not permitted** — Simon explicitly states this; our doc 08 doesn't mention it. Fix: add the control. 5 min.
9. **Slack/email are not approval records** — Simon explicitly states this; we partly treat them as audit trail. Fix: clarify Linear AIR comment is always the official record. 10 min.
10. **Stage 8 user-guidance record** — Simon requires confirmation that approved users received training/guidance; we leave it implicit. Fix: add a one-pager template + receipt confirmation. Quarter day.

## Why this matters

The AI Tool Evaluation Procedure is one of the **first concrete IMS documents** Janus will submit. If the v0.5 lands aligned to Simon's vocabulary on the first pass, the auditor sees one IMS shape across the company (and across the queued Marketing / HR / Finance / IT-Ops instances), not ten dialects. The Stage 9 lifecycle gap is also the one that would surface during the certification audit — closing it pre-emptively is cheap.

## HR Process Architecture — separate strategic ask

Simon also shared an HR architecture image with two options:
- **Option 1: Integrated** People Operations & Employee Experience — one main process, four sub-processes — fits SMEs / current Janus scale.
- **Option 2: Decentralized** — three independent processes (Talent Acquisition · HR Compliance & Admin · Talent Mgmt & Org Dev) — fits large enterprises.

Jehad recommends adopting **Option 1 for the v1 IMS submission**, with an **explicit migration trigger to Option 2** written into the M1 (Strategic Leadership) process: split when headcount >250 OR entities >25 OR a jurisdiction mandates separated HR compliance — whichever comes first.

## Next moves

- Reply to Simon today: "~70% aligned, can put together a v0.5 by 15 May."
- Half-day with Michael to lock the approval-authority role mapping (Gap 4).
- Update doc 08 with the cheap gaps (5, 6, 8, 9, 10) — total ~1.5 hours.
- Next week: restructure gates (Gap 2), build F1-F8 form templates (Gap 1), publish Appendix A (Gap 7).
- Send the HR architecture recommendation as a separate Slack message — don't dilute the AI-tool-process reply.
