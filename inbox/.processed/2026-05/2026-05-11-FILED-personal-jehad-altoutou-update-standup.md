---
type: question
slug: update-standup
title: Proposed update to processes/standup.md
created: 2026-05-11
updated: 2026-05-11
status: active
owner: jehad-altoutou
audience: [department]
departments: [ai-office]
captured_by: jehad-altoutou
target_page: processes/standup.md
---

# Proposed update to processes/standup.md

**Reason:** AI Office Brain's standup + Linear-AIP + Monday-Automations references carry operational schema (status UUIDs, column IDs, sub-item types, Notion size thresholds) that the personal process page omits. Adding a 'Reference schemas' section anchors the right level of detail without duplicating the skill source.

**Patch block** (append to existing canonical page):

---


## Reference schemas (snapshot 2026-05-04, AI Office Brain v3.9)

From the local AI Office Brain (`sources/laptop/aio-brain-skill-standup`, `aio-brain-sor-linear-aip`, `aio-brain-sor-monday-automations`, `aio-brain-sor-notion-operations-notebook`):

### Monday Automations board (`5095012818`) — column IDs

- Source bump: `text_mm2x5d54` ("AIO DD Mon YYYY")
- Status: `color_mm2mfrpd`
- Link (drives AIP reconciliation): `link_mm2xexj3`
- Subitems: `subtasks_mm2mszsh`

### Linear AIP team (`2d1b5c04-94fd-4087-8e95-a5a7aa244a16`) — status UUIDs

| Status | UUID |
|---|---|
| Backlog | `57d6d704-7a3b-41f9-b936-a7d64252d00a` |
| Planned | `d5ccd469-37b4-4b5b-92d6-21be9f27dc90` |
| In Progress | `210b719c-eb51-4d5f-88fb-dcde85ae9939` |
| Done | `661dd6ca-5d5b-4378-8cb4-f1b0384975dc` |
| Cancelled | `ebfcf4e3-f40e-4599-a2b2-827656299627` |

### Notion size hygiene (v3.9 thresholds)

| Threshold | Behaviour |
|---|---|
| <60KB | Healthy |
| 60–80KB | Warn; queue archival |
| >80KB | Mandatory archival before append |
| >100KB | Block live append; fall back to outputs file |

Retention window: 14 days of full content on the master Operations Notebook page; older entries auto-archive to monthly `Standup Log Archive — <Month YYYY>` child pages.

### Sub-item naming convention

- **Production Stage sub-items** (canonical): Plan, Build, Test, Deploy, Monitor. Created only as stages are explicitly discussed; not pre-populated.
- **Action sub-items**: Verb + object + context. "Send Lisandro the Monday API token" ✅ / "Follow up" ❌.

