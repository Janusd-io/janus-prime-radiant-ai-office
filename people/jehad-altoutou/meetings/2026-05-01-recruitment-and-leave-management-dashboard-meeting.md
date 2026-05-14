---
type: source
source_type: meeting
title: Recruitment and Leave Management Dashboard Meeting
slug: 2026-05-01-recruitment-and-leave-management-dashboard-meeting
created: 2026-05-01
captured_by: jehad-altoutou
attendees: [jehad-altoutou, theresa-wong]
duration_min: 65
fireflies_id: 01KQH403N18AFABK6Y5R5CCMV6
audience: department
departments: [ai-office, hr]
dept_scope: [ai-office, hr]
sensitivity: dept
task_tracker: monday
parsed_at: "2026-05-14T09:51:32Z"
parser_version: 2
summary: "Jehad walked Theresa through a prototype HR / recruitment dashboard (referred to as the SSFI dashboard) covering departments, roles, assessments with scoring thresholds (strong-hire 85%, hire 70%, consider 55%, weak 40%), a question bank, candidate invites, and a leave-request workflow routed throug"
topics: [recruitment-dashboard, leave-management, assessments, ats, fireflies-webhook, deel-integration, slack-hub, hr-templates]
decisions: [2026-05-01-park-easter-egg-critical-thinking-assessment, 2026-05-01-recruitment-tracker-is-priority-build, 2026-05-01-slack-primary-leave-request-surface-deel-backend, 2026-05-01-remove-emergency-and-paid-leave-types, 2026-05-01-leave-balance-defaults-22-annual-14-sick]
action_items_count: 10
confidence_overall: high
---

# Recruitment and Leave Management Dashboard Meeting

**Date:** 2026-05-01
**Attendees:** [[jehad-altoutou]], [[theresa-wong]]
**Duration:** 65 min
**Fireflies:** [original meeting](https://app.fireflies.ai/view/01KQH403N18AFABK6Y5R5CCMV6)

---

## Summary

Jehad walked Theresa through a prototype HR / recruitment dashboard (referred to as the SSFI dashboard) covering departments, roles, assessments with scoring thresholds (strong-hire 85%, hire 70%, consider 55%, weak 40%), a question bank, candidate invites, and a leave-request workflow routed through the Noemi internal AI agent. Theresa pushed for a recruitment tracker as the priority: a one-line-per-candidate view with CVs stored centrally, pre-interview (CV-vs-JD) and post-interview (transcript-derived) scoring, source (direct vs recruitment agency), interview stages, and comments — replacing the current Excel-on-laptop + Slack-scattered setup. They agreed the candidate flow would be career-page apply -> automated ATS-style JD/CV match -> Slack notification -> optional pre-interview assessment -> interview (Fireflies-recorded, post-assessment via webhook) -> further rounds, and that JDs and assessments should attach to roles inside the dashboard rather than living in separate documents. On leave management, they agreed Slack would remain the primary employee surface (request hub) while Deel becomes the back-end record-keeper once live, with Slack approve/reject mirroring Deel and a team-calendar chart view added so line managers can spot leave clashes. The Easter-egg / critical-thinking assessment was explicitly parked pending Jehad's further design work, and Jehad will wait for Bonaventure's HR Claude template (already shared with Michael) before finalising the pre-interview scoring format so per-person formats don't diverge.

## Decisions

- [[2026-05-01-park-easter-egg-critical-thinking-assessment]] — Park the Easter-egg critical-thinking assessment for now
- [[2026-05-01-recruitment-tracker-is-priority-build]] — Recruitment tracker is the priority build over Easter-egg and other modules
- [[2026-05-01-slack-primary-leave-request-surface-deel-backend]] — Slack stays the leave-request surface; Deel is the back-end record
- [[2026-05-01-remove-emergency-and-paid-leave-types]] — Remove Emergency and Paid leave from leave-type list
- [[2026-05-01-leave-balance-defaults-22-annual-14-sick]] — Leave-balance defaults: 22 annual / 14 sick (Bonaventure 30 annual)

## Action items

- [ ] @theresa-wong Share a shared Google Drive folder with ~10 sample CVs so Jehad can use them to build and test the recruitment tracker. (raised by @jehad-altoutou) — Monday
- [ ] @theresa-wong Share the soft copy of the pre-interview assessment template / pack with Jehad. (raised by @jehad-altoutou) — Monday
- [ ] @theresa-wong Share Mariam's existing recruitment-tracker Excel sheet (or just its column headers) with Jehad so he can mirror the schema. (raised by @jehad-altoutou) — Monday
- [ ] @jehad-altoutou Create a /Recruitment Google Drive folder structured by branch (Dubai first, Singapore later) and then by department for CV intake. — Monday
- [ ] @jehad-altoutou Confirm with Michael whether Bonaventure's HR Claude template (JD, pre-interview, post-interview formats) has been handed over, and pull it as the canonical template before finalising the dashboard's scoring formats. — Monday
- [ ] @jehad-altoutou Investigate Fireflies webhooks (meeting transcribe / summarize events) to auto-pipe interview transcripts into the dashboard for post-interview scoring. — Monday
- [ ] @jehad-altoutou Investigate Deel's API / webhook / sandbox to mirror leave-balance logic and produce a team-calendar chart view for line managers. (raised by @theresa-wong) — Monday
- [ ] @jehad-altoutou Verify whether UAE public-holiday data is implemented in the leave calendar and wire in a daily auto-fetch so dates like Eid stay current. — Monday
- [ ] @jehad-altoutou Update leave-type defaults in the dashboard: 22 annual / 14 sick / Bonaventure 30; remove Emergency and Paid; keep Haj as unpaid. — Monday
- [ ] @jehad-altoutou Add a JD field to the role-creation form so JDs are stored against roles in the dashboard and reused for CV-vs-JD scoring. — Monday

## 🎯 This week

- @jehad-altoutou Begin building the recruitment-tracker module (one line per candidate, CV link, source dropdown, interview stages, pre/post scoring slots). (raised by @theresa-wong)
- @theresa-wong Pull together the sample CVs, pre-interview pack, and Mariam's tracker headers and send to Jehad as the input bundle for the build. (raised by @jehad-altoutou)

## 🏔️ Long horizon

- Build a careers page on the Janus website so external applicants (and recruitment agencies) submit CVs directly into the dashboard, eliminating manual email/Slack intake. (owner: @jehad-altoutou; horizon: weeks)
- Implement an internal ATS-style filter that automatically scores incoming CVs against the JD and only surfaces passing candidates to HR (with a Slack notification on each). (owner: @jehad-altoutou; horizon: weeks)
- Stand up a single company-wide Slack requests hub where each department exposes its forms (leave, HR, etc.) so employees have one channel rather than scattered tools. (horizon: quarter)
- Migrate leave-record source of truth to Deel once Deel is live, keeping Slack as the request/approve UI and dashboard as a viewing layer. (owner: @theresa-wong; horizon: weeks)
- Expand recruitment tracker scope per-country (Dubai first, Singapore next) so each office has its own tracker view. (owner: @jehad-altoutou; horizon: quarter)
- Design the Easter-egg / critical-thinking assessment as a role-aware scenario module (different scenarios and weights for HR vs IT vs leadership candidates). (owner: @jehad-altoutou)

## Findings

- Recruitment artefacts are currently fragmented across personal email inboxes, Slack channels, and an Excel sheet Mariam maintains — there is no single place to see CVs, interview status, and scoring together. (stated by @theresa-wong)
- Mariam, Theresa, and Bonaventure each generate HR/recruitment outputs via Claude in different formats, so Bonaventure is consolidating an HR-specific Claude template (JDs, pre-interview, post-interview) and has shared it with Michael to become the canonical format. (stated by @theresa-wong)
- Pre-interview vs post-interview scoring already produces actionable divergence on real candidates — one candidate dropped from 6.7 to 5.8 (CV-bluffing surfaced by transcript) while another rose 6.2 to 7.6 (CV undersold the candidate). (stated by @theresa-wong)
- Fireflies supports webhooks for meeting transcribe and meeting summarize events, which makes auto-piping interview transcripts into a post-interview scoring step feasible. (stated by @jehad-altoutou)
- Leave approvals will route line-manager-first then HR — except for CEO-level (Bonaventure), where the request bypasses line-manager approval and only notifies HR. (stated by @theresa-wong)
- Noemi is an internal Janus AI agent surfaced inside the dashboard for routing notifications (e.g. leave-approval prompts to line managers). (stated by @jehad-altoutou; confidence: medium)
- MCP (Model Context Protocol) is wired into the dashboard so users can talk to Claude to create/update content (e.g. generate an assessment description) instead of filling forms manually. (stated by @theresa-wong)

## Open questions

- How should Fireflies transcripts from in-person interviews (which won't be recorded on Google Meet) be ingested into the post-interview scoring flow? (raised by @theresa-wong)
- Can a single Fireflies organisation-level webhook capture interviews regardless of which Janus employee hosted the meeting, or do we need a dedicated interview email/account? (raised by @jehad-altoutou)
- Does Deel expose a line-manager team-view of upcoming leave (so clashes are visible without opening each report's record), or do we need to build that chart in the dashboard? (raised by @jehad-altoutou)
- Is the UAE public-holiday calendar already implemented in the leave system, and how is it auto-updated daily? (raised by @jehad-altoutou)
- If recruiters (not candidates) submit CVs, should they go through the same careers-page form, or via a recruiter-specific upload that prevents duplicate entries? (raised by @jehad-altoutou)

## Blockers

- Recruitment-tracker scoring formats cannot be finalised until Bonaventure's HR Claude template (shared with Michael) is retrieved, to avoid divergent per-person formats. (blocks: [[recruitment-tracker]]; owner: @jehad-altoutou)
- Deel integration design is blocked on access to a Deel sandbox / API documentation to understand the leave-balance logic. (blocks: [[deel-integration]]; owner: @jehad-altoutou)

## Tool mentions

- [[fireflies]] — interview transcripts to be auto-piped via webhook into post-interview scoring
- [[deel]] — back-end leave-record system once live; needs API/sandbox access to mirror logic in Slack
- [[slack]] — primary employee request hub for leave requests, approvals, and HR forms
- [[google-drive]] — shared storage for sample CVs and recruitment intake folder structured by branch and department
- [[claude]] — used today to generate JDs, pre-interview, and post-interview scoring packs; to be integrated into dashboard via MCP
- [[model-context-protocol]] — wired into the dashboard so users can chat with Claude to create/edit assessments and descriptions
- [[noemi]] — internal Janus AI agent that delivers leave-approval prompts and notifications inside the dashboard
- [[google-meet]] — interview meeting platform whose calendar invites would route transcripts into a shared interview inbox

## Topics

- recruitment-dashboard
- leave-management
- assessments
- ats
- fireflies-webhook
- deel-integration
- slack-hub
- hr-templates

## Related

- Project: [[recruitment-and-leave-dashboard]] — primary subject of the meeting — HR dashboard covering recruitment tracker, assessments, and leave workflow
- Project: [[janus-careers-page]] — future careers page on Janus website that feeds CVs into the dashboard
- Vendor: [[fireflies]] — interview transcript source; webhook integration discussed
- Vendor: [[deel]] — incoming HR system of record for leave balances; sandbox/API access needed
- Vendor: [[slack]] — primary employee request and approval surface
- Vendor: [[google-drive]] — CV storage substrate for the tracker
- Vendor: [[claude]] — used by Mariam, Theresa, and Bonaventure today for JD/CV scoring; to be embedded via MCP
- Concept: [[model-context-protocol]] — integrated into the dashboard to let users chat with Claude to create assessments
- Concept: [[applicant-tracking-system]] — the dashboard is described as an internal ATS-style CV-vs-JD filter
- Person: [[bonaventure-wong]] — owns the canonical HR Claude template (JD, pre-interview, post-interview); already shared with Michael
- Person: [[michael-bruck]] — holds Bonaventure's HR Claude template handover; line manager in example flows
- Person: [[euclid-wong]] — designed an existing technical test with Andrey; named as hiring manager example
- Person: [[andrey-timokhov]] — co-designed the existing technical test with Euclid
- Person: [[maryam]] — current HR ops owner of the recruitment Excel tracker and HR Claude prompts
- Concept: [[noemi]] — internal Janus AI agent used for routing dashboard notifications

---

## Transcript

See [[2026-05-01-recruitment-and-leave-management-dashboard-meeting.transcript|full transcript]]
