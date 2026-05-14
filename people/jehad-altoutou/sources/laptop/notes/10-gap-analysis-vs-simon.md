---
type: source
source_type: laptop
title: 10-GAP-ANALYSIS-vs-SIMON
slug: 10-gap-analysis-vs-simon
created: 2026-05-08
captured_by: jehad-altoutou
audience: personal
original_path: /Users/jehad/Documents/janus-puls-onboarding/10-GAP-ANALYSIS-vs-SIMON.md
original_size: 17470
original_ext: .md
category: notes
extracted_with: text-copy
extracted_at: "2026-05-14T09:51:46Z"
sensitivity: dept
sensitivity_confidence: 0.90
sensitivity_reason: "Gap analysis vs Simon's formal template — work content for IMS alignment"
---

# 10-GAP-ANALYSIS-vs-SIMON

_Extracted from `Documents/janus-puls-onboarding/10-GAP-ANALYSIS-vs-SIMON.md` on 2026-05-14._

# Gap Analysis — Our Process Docs vs. Simon's IMS-PRC-AI-001

**Subject:** Comparison of Janus's existing AI tool / platform process docs ([07], [08], [09]) against Simon's *IMS-PRC-AI-001 Management of Internal AI Tools v0.4*. Plus a separate strategic ask raised by the HR Process Architecture image he shared.

> Quick verdict: substantial overlap, alignable gaps. Simon's doc is the formal IMS shape; ours is the operational reality. We need to map our reality to his shape, fill the missing lifecycle stage, and adopt his form-coded vocabulary.

| Field | Value |
|---|---|
| **Author** | Jehad — AI Operations Engineer |
| **Compared documents** | This repo: [07-MEETING-TO-TASK-WORKFLOW.md](./07-MEETING-TO-TASK-WORKFLOW.md) · [08-TOOL-EVALUATION-PROCEDURE.md](./08-TOOL-EVALUATION-PROCEDURE.md) · [09-PLATFORM-DEVELOPMENT-PROCESS.md](./09-PLATFORM-DEVELOPMENT-PROCESS.md) |
| **Simon's document** | `IMS-AI-Process_Elements_Table_ISO9001_Figure1_v0.4.docx` — IMS-PRC-AI-001 Management of Internal AI Tools |
| **Date** | 8 May 2026 |

---

## 1. Side-by-side stage mapping

Simon's doc has **9 numbered stages** with **8 forms (F1-F8)**. Mine has **5 stages** with no form codes. Here's the alignment:

| # | Simon's stage | Form | What our doc 08 covers it as | Match quality |
|---|---|---|---|---|
| 1 | **Request / Proposal** | F1 — AI Tool Request Form | Stage 1 — Intake (Path A meeting + Path B Slack) | 🟡 Partial — we cover the channel but not the formal request form |
| 2 | **Stage 1 — Intake and Triage** (Gate 1) | F2 | Stage 2 — Registry check & enrichment | 🟢 Good — `/ai-registry` does this; need form template |
| 3 | **Stage 2 — Technical Qualification** (Gate 2) | F3 | Folded into our Gates 1+2 (Initial fitness + Security/data) | 🟡 Partial — same activity, different gate-numbering scheme |
| 4 | **Stage 3 — Sandbox and Domain Expert Evaluation** (Gate 3) | F4 | Stage 4 — Sandbox deployment & requester validation | 🟡 Partial — we have requester, not a designated Domain Expert role |
| 5 | **Stage 4 — Approval Decision** | F5 | Implicit at end of our Stage 3 + Stage 4 sign-off | 🟡 Partial — no consolidated approval dossier |
| 6 | **IT Readiness / Deployment Preparation** | F6 | Stage 5 — IT handover & company-wide deployment | 🟢 Good — same activity; need form template |
| 7 | **AI Tools Register Listing** | F7 | Final [[linear|Linear]] AIR status → Active in Stage 5 | 🟢 Good — Linear AIR entry serves as F7 |
| 8 | **Production Use / Implementation** | (training record) | Implicit "all employees have access" final state | 🟡 Partial — no explicit user training/guidance record |
| 9 | **Ongoing Review, Re-evaluation, Suspension, De-listing** | F8 | **❌ Not covered** | 🔴 Missing entirely |

---

## 2. Concrete gaps and how to fill them

### Gap 1 — Formal forms (F1-F8) vs. our digital records

**Simon expects:** every stage produces a numbered form (F1-F8) as the official record.
**We have:** Linear AIR comments · Slack threads · Notion entries · Final Execution Reports.

**Fix:** Build a **form-mapping table** that says "F-code = digital record location." We don't need PDFs — we need a documented mapping the auditor can follow.

| Form | Janus implementation |
|---|---|
| F1 — AI Tool Request Form | Slack workflow form in `#ai-tool-requests` (Path B — needs building) OR transcript line item from standup (Path A) |
| F2 — Stage 1 Intake/Triage Record | Linear AIR-N issue creation comment (auto-populated by `/ai-registry`) |
| F3 — Stage 2 Technical Qualification Record | Linear AIR-N comment from `/ai-tool-evaluation` Gate 1+2 |
| F4 — Stage 3 Sandbox & Domain Expert Eval Form | Linear AIR-N comment with sandbox findings + Domain Expert sign-off |
| F5 — Stage 4 Approval Decision Record | Linear AIR-N comment with final decision · approved use cases · prohibited uses · data boundary · review date |
| F6 — IT Readiness Confirmation | Linear AIR-N comment from IT confirming readiness OR a Notion handover acceptance page linked from AIR |
| F7 — AI Tools Register Entry Template | Linear AIR-N issue itself (status → Active) |
| F8 — Re-evaluation/Suspension/De-listing Record | Linear AIR-N comment when status changes post-Active |

**Effort:** 1 dev-day to build Notion templates for each form + update doc 08 with the mapping table.

### Gap 2 — Gate numbering scheme mismatch

**Simon:** Gate 1 (Stage 1 intake), Gate 2 (Stage 2 technical), Gate 3 (Stage 3 sandbox) — **3 gates**, each tied to a stage.
**Ours:** Gate 1 (Initial fitness), Gate 2 (Security & data), Gate 3 (AI governance 42001), Gate 4 (Operational fit) — **4 gates**, all in one block.

**Fix:** Adopt Simon's 3-gate-3-stage structure. Re-distribute our 4 evaluation areas across his 3 stages:

| Simon's stage | Gate | Janus criteria (re-distributed) |
|---|---|---|
| Stage 1 (Gate 1 — Intake) | Triage | Vendor reputation · pricing reasonableness · request completeness · obvious red flags (blacklisted vendor, obvious TOS issues) |
| Stage 2 (Gate 2 — Technical) | Technical qualification | Security posture · data residency · encryption · audit logs · 42001 AI governance · operational fit (stack integration · SSO · API · SLA · exit) |
| Stage 3 (Gate 3 — Sandbox) | Practical validation | Use case satisfied · [[5-area-stress-test|5-area stress test]] pass · output quality · workflow integration without parallel processes |

**Effort:** Update doc 08 Section 2 + Section 3 controls table. Half a day.

### Gap 3 — Domain Expert role

**Simon's Stage 3** specifies a **Domain Expert** performs sandbox testing using approved test data and records practical feedback.
**Ours:** Requester runs use case OR AI Ops runs stress test.

**Fix:** Introduce Domain Expert as an explicit role. Two-tier:

- **Simple cases:** the **Requester** acts as Domain Expert (already validates use case in our flow).
- **Complex / cross-functional cases:** a **designated Domain Expert** is named in Stage 1 of intake (e.g., HR rep for HR-impacting tools, Finance for finance tools).

This satisfies Simon's separation of "user perspective" from "technical perspective" without creating a new bureaucratic role for every evaluation.

**Effort:** Update doc 08 Stage 4 description + add a column to the role table. Quarter-day.

### Gap 4 — Approval authority hierarchy

**Simon names specific roles:** Head of AI Native · Head of AI Office · Department Head · AI Department/Evaluator · IT/Security/Legal.
**Ours:** "Process Owner" and "AI Ops" generically.

**Fix:** Map our Linear/Janus roles to Simon's titles in a single table:

| Simon's role | Janus equivalent |
|---|---|
| AI Department / Evaluator | Jehad — AI Operations Engineer |
| Head of AI Native | TBD — confirm with Michael |
| Head of AI Office | [[michael-bruck|Michael Bruck]] (AI Projects lead) |
| Department Head | Per requesting department (HR head · Finance head · etc.) |
| IT / Security / Legal | TBD per Janus org chart |
| Approval authority for Stage 4 | TBD — likely Michael for routine, escalates to Top Management for high-risk |

**Effort:** Half-day conversation with Michael to lock the role mapping. Then update doc 08.

### Gap 5 — Missing Stage 9 (lifecycle ongoing review)

**Simon's Stage 9** covers scheduled review · vendor change response · incident-triggered review · new use case requests · de-listing · suspension. Outputs **F8 — Re-evaluation/Suspension/De-listing Record**.
**Ours:** Doc 08 ends at "Tool live → all employees have access." No lifecycle.

**Fix:** Add Stage 6 to doc 08:

```
Stage 6 — Ongoing review, suspension, or de-listing
  Triggers: scheduled review date · vendor change · security incident
            · obsolescence · new use case request · new data type request
  Outputs: F8 record (Linear AIR comment) · updated F7 (AIR status)
  Notification: affected users · Department Heads · Top Management if material
  Notes: Slack/email are notification channels only — F8 is the official record
```

**Effort:** Half-day to draft + add to doc 08. **This is the biggest functional gap.**

### Gap 6 — Process document reference codes (IMS-PRC-AI-XXX)

**Simon uses formal IDs:** IMS-PRC-AI-001 = Management of Internal AI Tools.
**Ours:** File numbers (07, 08, 09) — useful for the repo, not for the IMS.

**Fix:** Adopt Simon's naming for the IMS submission. Proposed:

| Repo file | IMS-PRC code (proposed) | Title |
|---|---|---|
| 07-MEETING-TO-TASK-WORKFLOW | IMS-PRC-AI-002 | Meeting Intelligence and Task Orchestration |
| 08-TOOL-EVALUATION-PROCEDURE | **IMS-PRC-AI-001** (matches Simon) | Management of Internal AI Tools |
| 09-PLATFORM-DEVELOPMENT-PROCESS | IMS-PRC-AI-003 | Internal Platform & Tool Development |

**Effort:** Cosmetic. Add the code to each doc's header. 15 minutes.

### Gap 7 — Appendix A (AI Tool Evaluation and Approval Methodology)

**Simon references "Appendix A"** as the source of detailed gate criteria — referenced in stages 2, 3, 4, 9.
**Ours:** `/ai-tool-evaluation` skill methodology lives only inside the skill file.

**Fix:** Publish the gate criteria as a formal **Appendix A** document — even if it's just an export of the skill's methodology section into Notion or a separate IMS doc. The auditor needs to read it; they can't run the skill.

**Effort:** Half-day to extract from `/ai-tool-evaluation` skill + format as a standalone document.

### Gap 8 — Personal accounts not permitted

**Simon explicitly states (Stage 6 monitoring):** "Personal accounts are not permitted. Access must be limited to approved users, departments and use cases."
**Ours:** Doc 08 doesn't mention this control.

**Fix:** Add to doc 08 Section 3 controls table:

| Control | Where it fires | Why |
|---|---|---|
| **Work-account-only access** | Stage 5 (IT handover) | No personal accounts; SSO + RBAC enforced; per Simon IMS-PRC-AI-001 |

**Effort:** 5 minutes.

### Gap 9 — Slack/email are not approval records

**Simon explicitly states (Stage 9 monitoring):** "Slack/email are only notification channels and not official approval records."
**Ours:** Doc 08 treats Slack notifications as part of the audit trail.

**Fix:** Clarify in doc 08 that Slack/email are **notifications only**. The official record is always the Linear AIR comment (F1-F8 equivalents). Update the outputs table to reflect this.

**Effort:** 10 minutes.

### Gap 10 — Stage 8 (Production use / implementation) — training/guidance record

**Simon's Stage 8** requires a "user guidance record" — confirmation that approved users have received training or guidance on permitted/prohibited use.
**Ours:** Implicit in "tool live · users have access."

**Fix:** Add an explicit micro-step at Stage 5 of doc 08:

```
5.7 — User guidance record
  - Send approved users a one-pager (Notion or Slack message) covering:
    - approved use cases · prohibited use cases · data boundary
    - escalation paths · review date
  - Receipt confirmed via Slack reaction or Notion checkbox
  - Recorded as comment on AIR-N (or in approved system)
```

**Effort:** Quarter-day to template the one-pager.

---

## 3. Total effort to align doc 08 with Simon's IMS-PRC-AI-001

| Gap | Effort |
|---|---|
| 1. Form mapping table | 1 day (templates + doc update) |
| 2. Re-distribute gates 4→3 | Half day |
| 3. Domain Expert role | Quarter day |
| 4. Approval authority hierarchy | Half day (Michael conversation + update) |
| 5. **Stage 9 lifecycle (biggest functional gap)** | **Half day** |
| 6. IMS-PRC code naming | 15 min |
| 7. Appendix A publication | Half day |
| 8. Personal accounts control | 5 min |
| 9. Slack/email notification-only clarification | 10 min |
| 10. User guidance record | Quarter day |

**Total: ~3 dev-days to fully align our docs to Simon's IMS-PRC-AI-001 v0.4 structure.**

This includes one half-day with Michael (Gap 4) and one optional dev-day for the Slack-webhook intake (Gap 1's Path B form, already noted as "to be built" in doc 08's implementation gap).

---

## 4. The HR Process Architecture image — a separate strategic question

Simon also shared an image with **two HR architecture options**:

| Aspect | Option 1: INTEGRATED | Option 2: DECENTRALIZED |
|---|---|---|
| Context | Startups / SMEs | Large enterprises / corps |
| Main process | People Operations & Employee Experience | 3 independent processes |
| Sub-processes | TA & Onboarding · People Admin & Payroll · L&D · Offboarding | Talent Acquisition · HR Compliance & Admin · Talent Mgmt & Org Dev |
| Key why? | Agility — holistic view, zero silos | Specialisation — high-risk compliance separated from "soft" HR |
| Ownership | One People Lead / Generalist | Multiple Process Owners (Heads) |

This is **not about doc 08**. It's about how Janus structures the **HR-related IMS process documents** in the deck's process map (slide 6). Simon is asking which model to adopt.

**My read of where Janus actually is right now:**

- **Today (10 entities):** sized like an SME → Option 1 (Integrated) fits the current reality
- **2027 target (20+ entities/year):** approaching enterprise → Option 2 (Decentralized) becomes necessary
- **[[assessify|Assessify]] is HR-domain** — already covered under "TA & Onboarding" in Option 1, or "Talent Acquisition" in Option 2

**Recommendation to Simon:**

Adopt **Option 1 (Integrated)** for the v1 IMS submission, with an **explicit migration trigger** to Option 2 written into the M1 (Strategic Leadership) process: when Janus reaches X entities or Y headcount, split into the 3 decentralized processes. This:

1. Matches current scale (won't look forced to the auditor)
2. Acknowledges the trajectory (auditor sees you've thought about it)
3. Doesn't require restructuring the deck's slide 6 process map yet (HR-related processes stay folded into existing Core processes — C3 Partner Enablement covers some, Assessify-built features cover hiring assessment)

The trigger thresholds need a separate conversation. Suggested defaults: split when **headcount > 250** OR **entities > 25** OR **regulatory requirement in any jurisdiction mandates separated HR compliance** — whichever comes first.

---

## 5. Recommended next moves

**Today:**

1. **Reply to Simon** acknowledging the doc and confirming alignment intent. Three sentences:
   > Read IMS-PRC-AI-001 v0.4. ~70% aligned to what we already operate (see [our doc 08]). Can put together a v0.5 that adopts your form codes (F1-F8), three-gate structure, and adds the Stage 9 lifecycle that we currently don't have documented. Half a week of work — happy to lead it. Want me to send a draft by 15 May?

2. **Send him the HR architecture recommendation** (Option 1 with migration trigger to Option 2). Separate Slack message — don't dilute the AI tool process reply.

**This week:**

3. **Half-day with Michael** to lock the approval-authority role mapping (Gap 4). Without this, Stage 4 has no defined sign-off chain.

4. **Update doc 08** with Gaps 5, 6, 8, 9, 10 (the cheap ones — total ~1.5 hours).

**Next week:**

5. **Restructure doc 08's gates** (Gap 2) to match Simon's 3-stage structure.
6. **Build form templates** in Notion for F1-F8 (Gap 1).
7. **Publish Appendix A** as a standalone document (Gap 7).

**Phase 2 (post-Path B):**

8. Build the Slack webhook intake (already in doc 08's implementation gap section).
9. Each form template gets a corresponding webhook payload schema.

---

## 6. Open questions for Simon

These are the things only Simon can answer — flag them in the reply:

1. **Form codes — physical or digital?** Are F1-F8 expected as PDF/Word forms, or is our digital mapping (Linear AIR comments, Notion templates, Slack workflow forms) acceptable as the F-record equivalent?
2. **Approval authority for Stage 4 (F5)** — does this always escalate to Top Management for AI tools, or does the AI Department / Head of AI Office have approval rights for routine cases?
3. **Re-evaluation cadence (Stage 9)** — what's the default review date when an AIR-N entry is created? 6 months? 12 months? Tool-class-dependent?
4. **HR architecture decision** — Option 1 (Integrated) for v1 with a documented migration trigger to Option 2, or do you want Option 2 adopted from day one?
5. **Appendix A naming** — should it be `IMS-APP-AI-001-A` or follow a different convention?

---

## 7. Relationship to the rest of the repo

| Doc | Status after this gap analysis |
|---|---|
| [04-FORMAL-RESPONSE.md](./04-FORMAL-RESPONSE.md) | No change — still the role-level Figure-1 schematic |
| [06-FIRST-VOICE-FINAL.md](./06-FIRST-VOICE-FINAL.md) | No change — already addressed to Simon |
| [07-MEETING-TO-TASK-WORKFLOW.md](./07-MEETING-TO-TASK-WORKFLOW.md) | Add IMS-PRC-AI-002 reference code; otherwise unchanged |
| **[08-TOOL-EVALUATION-PROCEDURE.md](./08-TOOL-EVALUATION-PROCEDURE.md)** | **Major rev pending — apply Gaps 1-10 to produce v2 aligned with IMS-PRC-AI-001 v0.4** |
| [09-PLATFORM-DEVELOPMENT-PROCESS.md](./09-PLATFORM-DEVELOPMENT-PROCESS.md) | Add IMS-PRC-AI-003 reference code; cross-link to revised 08 |
| **This doc (10)** | Living gap-analysis · close items as they're resolved · target: zero open gaps before sending updated 08 to Simon |

---

← Back to [README](./README.md) · See also: [08-TOOL-EVALUATION-PROCEDURE.md](./08-TOOL-EVALUATION-PROCEDURE.md) · [09-PLATFORM-DEVELOPMENT-PROCESS.md](./09-PLATFORM-DEVELOPMENT-PROCESS.md)
