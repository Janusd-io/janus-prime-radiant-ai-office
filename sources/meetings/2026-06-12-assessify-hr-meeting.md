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
related: [2881310536, 2990812837, 2891398195, 2991531764, 2991545790, 2991562985, 2991532135, 2991561461, 2991546268, 2991546933, 2884091280, 2884090820, 2884112593, 2884093357, 2884091103, 2987895946, 2910697070, AIR-168, AIR-9]
---

## Clean Meeting Summary

Jehad walked Theresa Wong (HR) through the full Assessify platform — all of her previously requested features are built and working, and she endorsed the recruitment module as exactly what HR needs right now. The session produced a detailed upgrade list: RAF renaming with UK English, HR CC notifications on every approval stage, a gated agency-recruiter login system, candidate-list filters with full CV visibility, an interviewer Slack pack, recruitment KPI reporting, a team-scoped leave calendar, and — the largest piece — a People Profile employee portal with self-service personal data, own-compensation history, and role-based access control. The strategic direction was agreed: Assessify grows into a full HRIS that progressively replaces Deel, with Deel retained only for multi-country payroll calculations until a payroll module exists. All upgrades are filed as ten implementation-ready Monday sub-items for the Claude Code run on Monday.

## 🎯 Next steps — by next standup

- _None — implementation begins Monday 15 Jun._

## 📅 Next steps — this week (Claude Code implementation run, Mon 15 Jun)

All owner Jehad, due/start 15 Jun, on the [HR Dashboard — Recruitment & Leave Management board](https://janusd-company.monday.com/boards/5095636727) (the dedicated Assessify execution board); each carries its full implementation spec:

- [Rename MRF → RAF, UK English + HR-friendly labels](https://janusd-company.monday.com/boards/5098349722/pulses/2991561461) — sub-item under the MRF/RAF item
- [Requester field + HR CC Slack notifications on all RAF stages](https://janusd-company.monday.com/boards/5098349722/pulses/2991546268) — sub-item under the MRF/RAF item
- [Agency recruiter login system with locked auto-filled fields](https://janusd-company.monday.com/boards/5095636727/pulses/2884091280) — existing "Recruitment agency portal" item, activated P3 → P1 with new spec
- [Candidate score column, score/role filters](https://janusd-company.monday.com/boards/5095636727/pulses/2884090820) + [CV links on dashboard records](https://janusd-company.monday.com/boards/5095636727/pulses/2884112593) — specs added to existing items
- [Duplicate-applicant handling with re-applicant flagging](https://janusd-company.monday.com/boards/5095636727/pulses/2991545790) — new, P1
- [Post-booking interviewer pack via Slack (PDF + CV)](https://janusd-company.monday.com/boards/5098349722/pulses/2991546933) — sub-item under interview scheduling
- [Recruitment KPI reports — time-to-hire, volume, difficulty](https://janusd-company.monday.com/boards/5095636727/pulses/2991562985) — new, P1
- [Team leave calendar — access matrix added](https://janusd-company.monday.com/boards/5095636727/pulses/2884093357) — existing item, spec expanded
- [Candidate + recruiter acknowledgement messaging](https://janusd-company.monday.com/boards/5095636727/pulses/2991532135) — new, P1

## 🏔️ Next steps — longer horizon

- [People Profile employee portal — HRIS phase 1](https://janusd-company.monday.com/boards/5095636727/pulses/2991531764) — Owner: Jehad — new, P0 Critical — start 15 Jun, largest build; visibility matrix config-driven pending Theresa's definitions
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

**Automations board (bridge only):**

- [Assessify HR platform](https://janusd-company.monday.com/boards/5095012818/pulses/2881310536) — source bump, meeting-summary Update, next-step stub, relocation-correction note
- [Walk Teresa through updated Assessify platform](https://janusd-company.monday.com/boards/5095012849/pulses/2990812837) — marked **Done** (this meeting was the walkthrough)
- [Collect sample CVs, JDs and interview outputs from Teresa / Mariam](https://janusd-company.monday.com/boards/5095012849/pulses/2891398195) — scope expanded to all historic CVs + 3H backfill

**HR Dashboard board (5095636727 — tactical execution, corrected location):**

- Created: People Profile portal (P0), duplicate-applicant handling, KPI reports, acknowledgement messaging (P1); RAF rename + HR CC notification sub-items under the MRF/RAF item; interviewer-pack sub-item under interview scheduling — each with a full implementation spec
- Updated: agency portal (activated P3 → P1 with move rationale), candidate view, CV auto-link, team leave calendar, Deel sync (strategy note)

*Correction note: the 10 implementation tasks were initially mis-filed as sub-items on the Automations board and were deleted after recreation on the HR Dashboard board — the Automations Assessify item is the bridge only; tactical work lives on the HR board per the standing convention.*

Coverage: ✅ all touched items covered (7 creates with specs, 1 backfill, move-rationale posted on the P3→P1 activation), ❌ 0 failures

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
