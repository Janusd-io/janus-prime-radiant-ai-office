---
type: source
source_type: laptop
title: 2026-05-13-aio-pm-meeting
slug: 2026-05-13-aio-pm-meeting
created: 2026-05-14
captured_by: jehad-altoutou
audience: personal
original_path: /Users/jehad/Downloads/2026-05-13-aio-pm-meeting.md
original_size: 6875
original_ext: .md
category: notes
extracted_with: text-copy
extracted_at: "2026-05-14T09:51:47Z"
sensitivity: dept
sensitivity_confidence: 0.90
sensitivity_reason: "AIO project-management meeting with Michael, Euclid, Rosa — explicitly marked `privacy: public` in source frontmatter; covers GitHub-as-canonical-store decision and PM team Prime Radiant rollout"
---

# 2026-05-13-aio-pm-meeting

_Extracted from `Downloads/2026-05-13-aio-pm-meeting.md` on 2026-05-14._

---
title: "AIO, Project Management Meeting — 13 May 2026"
date: 2026-05-13
meeting_type: project_management
attendees:
  - [[jehad-altoutou|Jehad Altoutou]]
  - [[michael-bruck|Michael Bruck]]
  - Euclid (PM Lead)
  - [[rosa|Rosa]] (PM Team)
duration_minutes: 97
fireflies_id: 01KRGKF94R785XZNVKGKTB840J
fireflies_url: https://app.[[fireflies|fireflies]].ai/view/01KRGKF94R785XZNVKGKTB840J
standup_skill_version: v3.16
privacy: public
tags:
  - prime-radiant
  - vault-rollout
  - [[github|github]]
  - project-management
  - knowledge-graph
---

# AIO, Project Management Meeting — 13 May 2026

**Attendees:** Jehad Altoutou, Michael Bruck, Euclid (PM Lead), Rosa (PM Team)
**Duration:** ~97 minutes
**Source transcript:** [Fireflies](https://app.fireflies.ai/view/01KRGKF94R785XZNVKGKTB840J)
**Canonical vault entry** — v3.16 Step 5G. Notion overlap continues until end-May deprecation.

---

## Clean Meeting Summary

- **[[prime-radiant|Prime Radiant]] architecture demo** delivered to Euclid and Rosa — covered the full personal → department → company vault hierarchy, inbox-first ingestion workflow, and the CLAUDE.md meta-skill brain. First exposure for the PM team to the system they will be onboarding onto.
- **GitHub confirmed as canonical file store** for Prime Radiant across all departments, replacing the previously planned Google Shared Drive structure. The Shared Drive project has been formally deprecated. GitHub accounts are provisioned silently by the skill — users never need to touch GitHub directly.
- **Inbox-first ingestion workflow** demonstrated — documents placed in the inbox folder are parsed and routed to appropriate vault sections based on front-matter metadata. Requires product/project folder separation to be agreed before upload.
- **Product/project content separation** agreed as a prerequisite for PM team ingestion. Michael to facilitate with Euclid and Rosa so content lands in the correct vault sections and avoids misclassification.
- **PM team vault rollout kicked off** — Euclid confirmed as pilot #2 (following Andrew). Six action sub-items created under the Prime Radiant Monday parent covering the full onboarding sequence: speaker tagging, IT onboarding session, GitHub permissions, folder taxonomy, document upload, and dashboard design.
- **Dynamic dashboards and visualisation prompts** scoped as a longer-horizon deliverable (Rosa). Will surface Prime Radiant knowledge base data in actionable formats once the ingestion pipeline is stable and document volume is sufficient.
- **Fireflies speaker tags** remain as [[unknown-speaker-1|Speaker 1]]–4 post-recording. Only Jehad (recording owner) can tag retroactively. Confirmed mapping: Speaker 4 = Euclid, [[speaker-2-unidentified|Speaker 2]] = Rosa. Tagging queued as an immediate next step.

---

## Decisions Made

- [[2026-05-13-github-canonical-prime-radiant-substrate|GitHub is the canonical file store for Prime Radiant; Google Shared Drive structure project deprecated]].
- Inbox-first ingestion is the standard onboarding pattern for all departments.
- PM team is pilot #2 for vault rollout (after Andrew / Marketing).
- Product/project folder separation must be defined before document upload begins.
- Dynamic dashboards are a longer-horizon deliverable, not a blocker for initial rollout.
- Speaker tagging responsibility confirmed: recording owner only (Jehad).

---

## Next Steps

### 🎯 By next standup
- [ ] Tag speakers in AIO PM Meeting Fireflies transcript — Jehad — [Monday](https://janusd-company.monday.com/boards/5095012849/pulses/2915304498)
- [ ] Schedule IT/Operations follow-up session for Prime Radiant onboarding — Jehad — [Monday](https://janusd-company.monday.com/boards/5095012849/pulses/2915295881)

### 📅 This week
- [ ] Set up GitHub repo permissions and sync for Euclid + Rosa — Jehad — [Monday](https://janusd-company.monday.com/boards/5095012849/pulses/2915304582)
- [ ] Facilitate PM folder structure and product/project content separation — Michael — [Monday](https://janusd-company.monday.com/boards/5095012849/pulses/2915295883)
- [ ] Upload PM team documents to Prime Radiant inbox folder — Euclid (external) — [Monday](https://janusd-company.monday.com/boards/5095012849/pulses/2915304680)

### 🏔️ Longer horizon
- [ ] Build dynamic dashboards and visualisation prompts — Rosa (external) — [Monday](https://janusd-company.monday.com/boards/5095012849/pulses/2915304683)

---

## Monday Items Touched

| Item | Action | ID |
|---|---|---|
| Prime Radiant — company-wide [[knowledge-graph|knowledge graph]] | Source bumped + substantive Update + next-step stub | [2900825519](https://janusd-company.monday.com/boards/5095012818/pulses/2900825519) |
| Engage large-scale data architecture specialist | Source bumped + substantive Update + next-step stub | [2882208018](https://janusd-company.monday.com/boards/5095012818/pulses/2882208018) |
| Notion Operations Notebook restructure | Source bumped + Description backfill | [2882088507](https://janusd-company.monday.com/boards/5095012818/pulses/2882088507) |
| Implement company-wide Google Shared Drive structure | **Deprecated** — Status set to Deprecated + deprecation rationale + Description Update | [2898141770](https://janusd-company.monday.com/boards/5095012818/pulses/2898141770) |
| Tag speakers in AIO PM Meeting Fireflies transcript | ➕ New sub-item (Jehad) | [2915304498](https://janusd-company.monday.com/boards/5095012849/pulses/2915304498) |
| Schedule IT/Operations follow-up session | ➕ New sub-item (Jehad) | [2915295881](https://janusd-company.monday.com/boards/5095012849/pulses/2915295881) |
| Set up GitHub repo permissions for PM team | ➕ New sub-item (Jehad) | [2915304582](https://janusd-company.monday.com/boards/5095012849/pulses/2915304582) |
| Facilitate PM folder structure for Prime Radiant ingestion | ➕ New sub-item (Michael) | [2915295883](https://janusd-company.monday.com/boards/5095012849/pulses/2915295883) |
| Upload PM team documents to Prime Radiant inbox | ➕ New sub-item (Euclid — external) | [2915304680](https://janusd-company.monday.com/boards/5095012849/pulses/2915304680) |
| Build dynamic dashboards for Prime Radiant | ➕ New sub-item (Rosa — external) | [2915304683](https://janusd-company.monday.com/boards/5095012849/pulses/2915304683) |

**Updates posted:** 3A source bumps × 3 + 1 deprecation status + 3 substantive Updates (3C) + 6 Description Updates (3G) + 1 Description backfill (3H) + 2 next-step stubs (3.5) + 1 coverage backfill (3I)

---

## [[linear|Linear]] AIP Reconciliation

- No new AIP-N references in transcript. No new AIP issues required.
- **AIP-21 carry-forward (10th run):** Linear status = Done (completedAt 2026-04-24). Monday [[assessify|Assessify]] HR platform = In Testing (active expansion). AIP-23 is the live successor. **Manual resolution required — strongly escalated.**

---

## AI Registry / Tool Evaluation Outcomes

*None this round.* No actionable tool mentions in transcript. GitHub is already operational infrastructure; no new evaluation needed.
