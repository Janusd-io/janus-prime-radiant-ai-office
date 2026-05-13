---
type: question
slug: update-monday
title: Proposed update to entities/vendors/monday.md
created: 2026-05-11
updated: 2026-05-11
status: active
owner: jehad-altoutou
audience: [department]
departments: [ai-office]
captured_by: jehad-altoutou
target_page: entities/vendors/monday.md
---

# Proposed update to entities/vendors/monday.md

**Reason:** Personal monday.md notes the board IDs but omits the schema-level details (column IDs, status labels, group IDs, sub-item types) which are operationally load-bearing for any /standup or wiki-driven Monday API work.

**Patch block** (append to existing canonical page):

---


## Schema reference (Automations board `5095012818`)

Captured from AI Office Brain `Systems-of-Record/Monday-Automations.md` (4 May 2026). Source: [[aio-brain-sor-monday-automations]].

### Status labels (Automations)

Backlog (`5`), In Definition (`6`), In Development (`0`), In Testing (`2`), In Production (`1`), Postponed (`4`), Deprecated (`3`).

### Groups (departments)

| Group | ID |
|---|---|
| Planned Automations (default top group) | `topics` |
| Marketing Department | `group_mm2xfh38` |
| Operations Department | `group_mm2xtzbj` |
| ISO Department | `group_mm2xjkm2` |
| HR Department | `group_mm2m796p` |
| Done | `group_mm2mbjs3` |

### Sub-item columns

Name (`name`), Owner (`person`), Status (`status` — Working on it / Done / Stuck), Date (`date0`).

### Department routing for new parent items

HR forms/hiring/onboarding/training → HR Department. Marketing/CRM/brand/content/lead-gen → Marketing Department. ISO compliance/audit/policy → ISO Department. Operations/post-prod/infra-ops/vendor-mgmt/finance dashboards → Operations Department. Cross-cutting tech/AI policy/anything else → Planned Automations. Routing confidence <70% → `/standup` asks before creating.

## HR Dashboard board (`5095636727`)

Flat priority-grouped checklist (no Sub-items, no Source, no Owner column). Groups P0 → P3 by priority. **28 items** as of 4 May 2026. The "Assessify HR platform" item on Monday Automations (id `2881310536`) is the **bridge** to this board — `/standup` does not write to the HR Dashboard directly. See [[aio-brain-sor-monday-hr-dashboard]].

