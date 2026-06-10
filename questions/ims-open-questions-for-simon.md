---
type: tracker
title: IMS — Open Questions for Simon
slug: ims-open-questions-for-simon
created: 2026-05-08
updated: 2026-06-09
departments: [ai-office]
captured_by: jehad-altoutou
audience: [department]
migrated_from: personal-obsidian-vault (07 ISO IMS PULS)
tags: [iso, ims, open-questions, simon]
status: live
---
# Open Questions for Simon

> Pending decisions that block specific work. Each question has the **decision needed**, **why it's blocking**, and **who answers**. Close items as Simon resolves them.

---

## Live items (last reviewed 11 May 2026 — all 11 items unchanged since 8 May)

### Q1 — Process Owner assignment for C1 / C2 / S2

- **What:** Am I the named Process Owner for C1 (AI System Design & Development), C2 (Software Development & Release), and S2 (IT Infrastructure & Data Governance), or is this splitting with Michael?
- **Why blocking:** Can't draft those process documents until ownership is confirmed.
- **Where asked:** [[janus-puls-onboarding|repo file 02]] (sent to Simon today)
- **Who answers:** Simon + Michael
- **Status:** ⏳ Awaiting reply

### Q2 — Form codes (F1-F8) — physical or digital?

- **What:** Simon's IMS-PRC-AI-001 v0.4 uses formal form codes (F1-F8). Are these expected as PDF/Word forms, or is our digital mapping (Linear AIR comments, Notion templates, Slack workflow forms) acceptable as the F-record equivalent?
- **Why blocking:** Determines effort to align our [[janus-puls-onboarding|repo file 08]] with his structure (1 dev-day digital mapping vs much more for actual forms).
- **Who answers:** Simon
- **Status:** ⏳ Pending — raise on next reply

### Q3 — Approval authority for Stage 4 (F5)

- **What:** Does Stage 4 final approval always escalate to Top Management for AI tools, or does the AI Department / Head of AI Office have approval rights for routine cases?
- **Why blocking:** Without this, the [[janus-puls-onboarding|repo file 08]] approval flow has no defined sign-off chain.
- **Who answers:** Simon + Michael (it's a delegation question)
- **Status:** ⏳ Pending

### Q4 — Re-evaluation cadence (Stage 9)

- **What:** What's the default review date when an AI tool is approved? 6 months? 12 months? Tool-class-dependent?
- **Why blocking:** [[janus-puls-onboarding|repo file 08]] Stage 9 (lifecycle review) needs concrete cadence to be implementable.
- **Who answers:** Simon
- **Status:** ⏳ Pending

### Q5 — HR architecture decision

- **What:** Adopt **Option 1 (Integrated)** for v1 IMS submission with a documented migration trigger to **Option 2 (Decentralized)**, or Option 2 from day one?
- **My recommendation:** Option 1 + migration trigger (headcount > 250 OR entities > 25 OR jurisdictional regulatory mandate — whichever first).
- **Why blocking:** Determines how HR-related processes are structured in the deck's slide 6 process map.
- **Who answers:** Simon + Top Management
- **Status:** ⏳ Pending

### Q6 — Appendix A naming convention

- **What:** Should the gate-criteria appendix be `IMS-APP-AI-001-A` or follow a different convention?
- **Why blocking:** Cosmetic — but needs answering before the appendix is published.
- **Who answers:** Simon
- **Status:** ⏳ Pending

### Q7 — Linear AIR vs separate AI Systems Register

- **What:** Does Linear AIR (with Gate 1 evaluation comments) satisfy the **AI Systems Register** requirement under ISO 42001 §6, or does Simon want a Notion-side mirror or a separate document?
- **Why blocking:** If we need a Notion mirror, that's additional work to build the sync.
- **Who answers:** Simon
- **Status:** ⏳ Pending

### Q8 — Obsidian-as-living-docs acceptable as §7.5 evidence?

- **What:** Is the Obsidian project-note-as-living-source-of-truth approach acceptable as ISO 9001 §7.5 documented information, or does the auditor expect Notion-as-only-surface for accessibility?
- **Why blocking:** Affects [[janus-puls-onboarding|repo file 09]] (Platform Development Process) — currently positions Obsidian as primary; would need restructuring if not.
- **Who answers:** Simon (with auditor preference once Certification Body is selected)
- **Status:** ⏳ Pending

### Q9 — Tool-evaluation Gates 1-4 criteria alignment

- **What:** Do my proposed Gate 1-4 criteria (Initial fitness · Security & data · AI governance · Operational fit) align with what `/ai-tool-evaluation` actually checks today, or does the skill need refinement to satisfy 42001 §8.2 explicitly?
- **Why blocking:** Determines whether the existing skill methodology becomes Appendix A as-is, or needs revision.
- **Who answers:** Simon + me (joint review of `/ai-tool-evaluation` skill)
- **Status:** ⏳ Pending — schedule a 30-min review

### Q10 — Tool sunset/decommission process

- **What:** Does a tool **status sunset** stage (when a tool is decommissioned) need its own documented procedure, or is it sufficient to handle as a status transition within Stage 9 lifecycle review?
- **Why blocking:** Minor scope question — affects whether [[janus-puls-onboarding|repo file 08]] needs a Stage 10 or whether Stage 9 covers it.
- **Who answers:** Simon
- **Status:** ⏳ Pending

### Q11 — Path B (Slack webhook intake) — pre or post certification?

- **What:** Should the Slack-webhook intake path for tool requests be built before certification, or treated as a Phase 2 enhancement?
- **My recommendation:** Pre-certification — it's ~3 dev-days of work and gives better evidence of "anyone can request, the system gates."
- **Why blocking:** Affects timeline planning.
- **Who answers:** Simon + Michael (budget question)
- **Status:** ⏳ Pending

---

## Resolved items

*(none yet — populate as Simon answers)*

---

## Resolution discipline

When Simon answers each question:

1. Move the item from **Live** to **Resolved**
2. Capture the answer in the relevant doc:
   - Process Owner answers → [[ims-process-owners-map]]
   - Form / structure answers → update [[janus-puls-onboarding|repo file 08]]
   - HR architecture → update [[ims-process-documents]] structure
   - Linear AIR / Obsidian acceptability → update [[janus-puls-onboarding|repo files 08 + 09]]
3. Re-link in [[iso-ims-puls]] status snapshot

---

## Related

- [[ims-process-owners-map]]
- [[janus-puls-onboarding|repo file 10]] — gap analysis (sections 5 + 6 list these questions)

← Back to [[iso-ims-puls]]
