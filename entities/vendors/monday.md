---
type: vendor
title: Monday
slug: monday
created: 2026-05-06
updated: 2026-05-13
departments: [ai-office, hr, marketing, it-ops]
status: active
confidence: high
sources: [aio-2026-05-01, aio-2026-05-04, aio-2026-05-06, 2026-05-11-aio-standup-with-jehad, jehad-vault-monday]
related: [linear, 2026-05-01-ai-registry-source-of-truth-stays-in-linear-air, 2026-05-06-monday-com-to-production-this-week, 2026-05-04-recruitment-execution-on-hr-dashboard-board, aio-skills-sor-architecture-jehad]
---

# Monday

Work management platform (monday.com). Janus's primary execution surface for tasks, projects, and action tracking — first-class in the `CLAUDE.md` system-of-record map.

## Boards in active use at Janus

| Board | ID | Scope |
|---|---|---|
| **Automation Plans & Task Tracking** | `5095012818` | Primary execution surface for AIO; the `/standup` skill writes to this board. |
| **HR Dashboard — Recruitment & Leave Management** | `5095636727` | Per [[2026-05-04-recruitment-execution-on-hr-dashboard-board]] — dedicated board for SSFI / Assessify pipeline. |
| **AI Tools Registry** *(deprecated)* | `5095577150` | Retained as historical reference only; no new writes. AI Tools Registry now lives exclusively in Linear AIR — see [[2026-05-01-ai-registry-source-of-truth-stays-in-linear-air]]. |

## Status (as of 2026-05-06)

In Sandbox in Linear AIR (auto-promoted from Evaluating to Sandbox by the standup skill v3.12 upon noticing active use). Production push targeted for this week per [[2026-05-06-monday-com-to-production-this-week]] — first concrete sandbox→production promotion in the new IT hand-off process.

## Janus conventions

- **Context Coverage Invariant** (from [[standup|/standup]] skill v3.13): every Monday item the skill touches in any phase carries a `<h2>Description (from meeting notes)</h2>` block in its Updates timeline. No exceptions, no orphans.
- **Board-segmentation principle:** workstreams large enough to warrant their own board (e.g., recruitment) get one, with a "bridge item" on the AIO Automations board pointing to the dedicated board. See [[2026-05-04-recruitment-execution-on-hr-dashboard-board]].

## Relationship to this wiki

Monday is an ingest source for `sources/monday/` per `CLAUDE.md` §5.1. Filter: completed tasks with substantive Description Updates; standup-execution items where the Context Coverage Invariant block carries non-trivial rationale.

## Watch for

- Production promotion this week — first real test of the IT hand-off template.
- Whether the deprecated AI Tools Registry board ever gets fully archived or stays as a read-only reference.

## Explicitly NOT the Janus CRM

Per the [[marketing-stack-technical-writeup|2026-05-19 marketing stack analysis]]: Monday has an official MCP server (390+ GitHub stars), but its **board-centric data model is not relationship-centric** in the way a CRM is. It works fine for the AI Registry, project tracking, and standup execution it already supports — but it is **not** being promoted to system-of-record for customer relationships. That role is going to [[agentic-lean-marketing-stack|Attio]] per AIR-76. Decision rationale: keep Monday for what it already does well; don't stretch it into a category where a purpose-built tool (Attio, with 3/3 on the [[stack-composition-framework]]) is the cleaner fit.

## Schema reference (Automations board `5095012818`)

From Jehad's federated view ([[aio-skills-sor-architecture-jehad]], 2026-05-11) — operationally load-bearing schema for any `/standup` or wiki-driven Monday API work.

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

### Column IDs

- Source bump: `text_mm2x5d54` ("AIO DD Mon YYYY")
- Status: `color_mm2mfrpd`
- Link (drives AIP reconciliation): `link_mm2xexj3`
- Subitems: `subtasks_mm2mszsh`

### Sub-item columns

Name (`name`), Owner (`person`), Status (`status` — Working on it / Done / Stuck), Date (`date0`).

### Department routing for new parent items

HR forms/hiring/onboarding/training → HR Department. Marketing/CRM/brand/content/lead-gen → Marketing Department. ISO compliance/audit/policy → ISO Department. Operations/post-prod/infra-ops/vendor-mgmt/finance dashboards → Operations Department. Cross-cutting tech/AI policy/anything else → Planned Automations. Routing confidence <70% → `/standup` asks before creating.

## HR Dashboard board (`5095636727`)

Flat priority-grouped checklist (no Sub-items, no Source, no Owner column). Groups P0 → P3 by priority. **28 items** as of 4 May 2026. The "Assessify HR platform" item on Monday Automations (id `2881310536`) is the **bridge** to this board — `/standup` does not write to the HR Dashboard directly.
