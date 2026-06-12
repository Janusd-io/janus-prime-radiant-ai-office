---
type: source
source_type: meeting
title: Jehad + Theresa Wong — Assessify HR Platform Review 12 Jun 2026
slug: 2026-06-12-assessify-hr-meeting
created: 2026-06-12
captured_by: jehad-altoutou
fireflies_id: 01KTXFSB24C7MM60F08GBTN23Y
fireflies_url: https://app.fireflies.ai/view/01KTXFSB24C7MM60F08GBTN23Y
attendees: [Jehad Altoutou, Theresa Wong]
duration_min: 75
audience: department
departments: [ai-office, hr]
standup_skill_version: v3.24
parser_version: 3
related: [2881310536, 2990812837, 2891398195, 2991511246, 2991515327, 2991552538, 2991511267, 2991554791, 2991515496, 2991525989, 2991520017, 2991516040, 2991555314, AIR-168, AIR-9]
---

## Clean Meeting Summary

Jehad walked Theresa Wong (HR) through the full Assessify platform — all of her previously requested features are built and working, and she endorsed the recruitment module as exactly what HR needs right now. The session produced a detailed upgrade list: RAF renaming with UK English, HR CC notifications on every approval stage, a gated agency-recruiter login system, candidate-list filters with full CV visibility, an interviewer Slack pack, recruitment KPI reporting, a team-scoped leave calendar, and — the largest piece — a People Profile employee portal with self-service personal data, own-compensation history, and role-based access control. The strategic direction was agreed: Assessify grows into a full HRIS that progressively replaces Deel, with Deel retained only for multi-country payroll calculations until a payroll module exists. All upgrades are filed as ten implementation-ready Monday sub-items for the Claude Code run on Monday.

## 🎯 Next steps — by next standup

- _None — implementation begins Monday 15 Jun._

## 📅 Next steps — this week (Claude Code implementation run, Mon 15 Jun)

All owner Jehad, due 15 Jun, under [Assessify HR platform](https://janusd-company.monday.com/boards/5095012818/pulses/2881310536); each sub-item carries its full implementation spec:

- [Rename MRF → RAF, UK English + HR-friendly labels](https://janusd-company.monday.com/boards/5095012849/pulses/2991511246)
- [Requester field + HR CC Slack notifications on all RAF stages](https://janusd-company.monday.com/boards/5095012849/pulses/2991515327)
- [Agency recruiter login system with locked auto-filled fields](https://janusd-company.monday.com/boards/5095012849/pulses/2991552538)
- [Candidate score column, score/role filters, CV links](https://janusd-company.monday.com/boards/5095012849/pulses/2991511267)
- [Duplicate-applicant handling with re-applicant flagging](https://janusd-company.monday.com/boards/5095012849/pulses/2991554791)
- [Post-booking interviewer pack via Slack (PDF + CV)](https://janusd-company.monday.com/boards/5095012849/pulses/2991515496)
- [Recruitment KPI reports — time-to-hire, volume, difficulty](https://janusd-company.monday.com/boards/5095012849/pulses/2991525989)
- [Line-manager team leave calendar with team-scoped access](https://janusd-company.monday.com/boards/5095012849/pulses/2991520017)
- [Candidate + recruiter acknowledgement messaging](https://janusd-company.monday.com/boards/5095012849/pulses/2991555314)

## 🏔️ Next steps — longer horizon

- [People Profile employee portal — HRIS phase 1](https://janusd-company.monday.com/boards/5095012849/pulses/2991516040) — Owner: Jehad — start 15 Jun, largest build; visibility matrix config-driven pending Theresa's definitions
- [Ingest all historic CVs once delivered](https://janusd-company.monday.com/boards/5095012849/pulses/2891398195) — Owner: Jehad — blocked on Teresa/Mariam delivery
- Payroll module (multi-country tax/pension/social-insurance), performance assessment + training records — future phases completing the Deel replacement; scope decision with Theresa

## Decisions made

- Strategic: Assessify becomes the HRIS of record, progressively replacing Deel; Deel kept only for payroll calculations until an internal payroll module exists. Theresa: "If we can do all that, then I don't even need to use Deel."
- Form is RAF ("Recruitment Authorisation Form"), never MRF; UK English is the platform standard; dates DD/MM/YYYY.
- HR is informed (CC'd via private Slack channel), never an approver, at every RAF stage including rejections with reasons. Approval chain stays line manager → Bonaventure.
- Agency submissions gated behind HR-issued logins for contracted agencies only — blocks unsolicited CVs and fee claims.
- All candidate CVs remain visible regardless of score; AI never auto-eliminates — HR filters by threshold and role.
- Duplicate applicants: keep only the updated CV; flag re-applicants with prior role + score; disregard rapid re-tailored resubmissions.
- Interviewer receives assessment PDF + CV via Slack after booking — never attached to the calendar invite (candidate visibility).
- Leave visibility matrix: line managers see only their own team (incl. cross-country reports); employees see team leave dates only; rejection reasons stay HR-side.
- People Profile: compensation visible to self + HR only for now (line manager excluded; may open later); terminated profiles move to an HR-only archive with retention; country-level data isolation required.
- Onboarding personal-data form stays (needed pre-join for visas) and maps into the profile, which becomes the living record; Google Drive keeps original documents.
- Candidates get expectation-setting acknowledgement ("if shortlisted we'll contact you"); recruiters get an email confirmation; HR gets no per-submission notifications (portal-monitored).

## Findings / context

- Everything from the previous Teresa session is built and confirmed working: RAF form (from Mariam's Word doc), recruitment pipeline with pre-screening scoring rubrics, agency intake form, Google Meet/Calendar interview booking with prefilled invites and emails, leave management with conflict detection and rejection reasons, employee/team records with Slack handles, question bank, per-department dashboards, and the SSFI MCP connector (Claude can create/edit roles, JDs, and scoring rubrics conversationally; admin approval gates connector access).
- Post-interview scoring rubric remains a placeholder — HR will fill key criteria per role in-platform (fields left blank for HR); pre/post score matching designed but needs the rubric.
- Stage pipeline exists end-to-end (intake → hired/rejected/withdrawn) but offer/hire tracking needs verification — folded into the KPI reports task.
- Theresa demoed her previous employer's SAP-based HRIS as the reference pattern for People Profile (employee self-service, leave, compensation history, performance, training tabs) — her stated gap there ("I can't see my whole team's absences in one view") is exactly what our leave calendar task addresses.
- AI-mediated interview availability matching (auto-emailing both parties and matching slots) discussed; blocked on per-line-manager calendar API access — consciously deferred.
- "Question bank" explained: every assessment question created is reusable across assessments.
- CV storage scale: Google Drive handles volume; rows will link to Drive CVs once the backend linkage is built.

## Monday items touched

- [Assessify HR platform](https://janusd-company.monday.com/boards/5095012818/pulses/2881310536) — source bump, meeting-summary Update, next-step stub
- [Walk Teresa through updated Assessify platform](https://janusd-company.monday.com/boards/5095012849/pulses/2990812837) — marked **Done** (this meeting was the walkthrough)
- [Collect sample CVs, JDs and interview outputs from Teresa / Mariam](https://janusd-company.monday.com/boards/5095012849/pulses/2891398195) — scope expanded to all historic CVs + 3H backfill
- 10 new implementation sub-items created (listed above), each with a Step 3G implementation spec

Coverage: ✅ 13 items, ⚠️ 1 backfilled, ➡️ 0 move-rationales, ❌ 0 coverage failures

## External / Other-Department Follow-ups

- **Send personal-data visibility definitions (HR-only vs manager-visible fields)** — Owner: Theresa Wong (HR) — this week — Monday: excluded by AI Office Ownership Gate
- **Provide/decide post-interview scoring rubric criteria; HR fills key skills per role in-platform** — Owner: Theresa/HR — Monday: excluded by AI Office Ownership Gate
- **Deliver all historic CVs from prior recruitments** — Owner: Teresa → Mariam (HR) — Monday: excluded by AI Office Ownership Gate (ingest side tracked on 2891398195)
- **Written confirmation of leave-record deletion process** — Owner: HR — Monday: excluded by AI Office Ownership Gate
- **Provision dedicated Fireflies account for interview recordings** — Owner: IT department — Monday: excluded by AI Office Ownership Gate (integration mapping is in the AIO backlog once delivered)
- **Decide payroll/social-insurance module scope** — Owner: Theresa Wong — future phase — Monday: excluded by AI Office Ownership Gate

## Linear AIP reconciliation

No AIP status changes authorised — none applied. (Note: AIP-23, HR Recruitment Pipeline Automation, remains In Progress and is consistent with today's expansion; AIR-168 was cross-linked to AIP-15/AIP-23 by the registry subagent.)

## AI Registry / Tool Evaluation outcomes

- **Deel — NEW entry AIR-168** (was unregistered despite production use): status Production; description captures active HR use, the 12 Jun replacement strategy, payroll-only retention, and the May sandbox/middleware work; cross-linked to AIP-15/AIP-23; `vendors/deel.md` updated. Gate 1 skipped with rationale (retroactive registration of phase-out tool; governance follow-up = contract scope review + Production→Monitor transition planning).
- **AIR-9 Fireflies.ai** — enriched: dedicated interviews-only instance auto-attached to Assessify-booked interviews feeding post-interview scoring; pending IT provisioning; `vendors/fireflies.md` updated. Status unchanged (Production).
- Skipped (registered, no new info): Slack, Google Drive (AIR-107), Google Calendar/Meet (Workspace), Claude/MCP (AIR-10/11). Dropped (zero-context): SAP (Theresa's previous employer's system), LinkedIn (passing mention).
- Assessify itself: internal Janus product — not registered, per standing decision.

## Notes for the registry lint

- Linear AIR label vocabulary has no "HR" label — AIR-168 carries Finance only; HR scope lives in the description. Candidate addition to the locked vocabulary (needs Michael's approval).
- AIR-168 cost fields (contract scope, licence count, renewal date) are TBD — needs HR/Finance input.
