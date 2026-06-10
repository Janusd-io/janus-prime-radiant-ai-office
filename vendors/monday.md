---
type: vendor
title: Monday
slug: monday
created: 2026-05-06
updated: 2026-06-09
departments: [ai-office, hr, marketing, it-ops]
status: active
confidence: high
sources: [aio-2026-05-01, aio-2026-05-04, aio-2026-05-06, 2026-05-11-aio-standup-with-jehad, jehad-vault-monday]
related: [linear, 2026-05-01-ai-registry-source-of-truth-stays-in-linear-air, 2026-05-06-monday-com-to-production-this-week, 2026-05-04-recruitment-execution-on-hr-dashboard-board, aio-skills-sor-architecture-jehad]
migrated_from: entities/vendors/monday.md
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

---

## Operational notes — Monday AI Tools Registry

_Migrated from the personal-vault 'AI Office Brain' base, 2026-06-09._

# Monday — AI Tools Registry (DEPRECATED)

Board ID: `5095577150`
URL: https://janusd-company.monday.com/boards/5095577150

> ⚠️ **Deprecated as an active execution surface (since standup skill v3.7).**
> [[ai-registry]] is the sole source of truth for AI tool registry data.
> This board is retained for **historical reference only**.

## Why deprecated

Resolved during the AIO 1 May 2026 standup. Maintaining the registry in two places (Linear and Monday) caused duplication-sync drift. The Linear-side conventions (description schema, label taxonomy, gate-comment audit trail in [[ai-tool-evaluation]]) were too rich to mirror cleanly on Monday columns. Decision: collapse to Linear AIR as canonical, deprecate this board.

## Do NOT

- Update items on board `5095577150`
- Move items between status groups on board `5095577150`
- Sync Linear AIR back into board `5095577150`
- Reference board `5095577150` schema in any new automation work

## Existing items

74 items remain (one-time migration from Linear AIR done before deprecation). Each item has:
- Status, Category, Departments Using, Owner / Evaluator
- A `📋 Linear description (snapshot at migration)` Update with the Linear-side description as it existed at migration time

These snapshots are **frozen** — they don't update when Linear AIR changes.

## When to look here anyway

- Browsing historical "what was AIR-N's status on 30 Apr?"
- Reading the snapshot of an old description before it was edited
- Linking out to the Linear AIR issue from the snapshot Update (each carries the AIR-N URL)

For anything current, go to [[ai-registry]] directly.

## Related

- Replacement: [[ai-registry]]
- Skill that owns the live registry: [[ai-registry]]

---

## Operational notes — Monday Automations

_Migrated from the personal-vault 'AI Office Brain' base, 2026-06-09._

# Monday — Automation Plans & Task Tracking

Board ID: `5095012818`
URL: https://janusd-company.monday.com/boards/5095012818

The primary surface for tasks, projects, automations, action tracking, and sub-items in the AI Office. Source of truth for the operational layer. Written by [[standup]].

## Schema

### Columns

| Column | ID | Type | Notes |
|---|---|---|---|
| Name | `name` | name | |
| Task Owner | `multiple_person_mm2mxqy7` | people | |
| Status | `color_mm2mfrpd` | status | Lifecycle (see below) |
| Timeline | `timerange_mm2mbggm` | timeline | |
| Priority | `color_mm2mbt5n` | status | Critical / High / Medium / Low |
| Automation Type | `dropdown_mm2mkr0y` | dropdown | Data Integration / Notification / Reporting / Task Management |
| Source | `text_mm2x5d54` | text | "AIO DD Mon YYYY" — bumped on every standup touch |
| Labels | `dropdown_mm2xe0sn` | dropdown (multi) | Cross-cutting tags |
| Link | `link_mm2xexj3` | link | AIP-N URL when applicable — drives [[linear]] reconciliation |
| Subitems | `subtasks_mm2mszsh` | subtasks | Production stages AND action sub-items |

### Status labels

- Backlog (`5`)
- In Definition (`6`)
- In Development (`0`)
- In Testing (`2`)
- In Production (`1`)
- Postponed (`4`)
- Deprecated (`3`)

### Groups (departments)

| Group | ID |
|---|---|
| Planned Automations (default top group) | `topics` |
| Marketing Department | `group_mm2xfh38` |
| Operations Department | `group_mm2xtzbj` |
| ISO Department | `group_mm2xjkm2` |
| HR Department | `group_mm2m796p` |
| Done | `group_mm2mbjs3` |

### Labels (multi-select dropdown)

Office of CEO, AI Policy, Technology, Finance, Marketing, Commercial, Legal, Training, Country.

### Sub-item columns

- Name (`name`)
- Owner (`person`, people)
- Status (`status`) — Working on it, Done, Stuck
- Date (`date0`)

## Two sub-item types

[[standup]] uses two distinct sub-item types under any parent:

1. **Production Stage sub-items** — canonical names: Plan, Build, Test, Deploy, Monitor. Created only as stages are explicitly discussed; not pre-populated.
2. **Action sub-items** — concrete follow-ups attached to existing parents. Naming convention: **Verb + object + context**. ✅ "Send Lisandro the Monday API token" / ❌ "Follow up".

## Key items (snapshot, May 2026)

- **Assessify HR platform** (`2881310536`) — bridge to [[monday]] for recruitment work
- **#60 ISO officer process documentation** (`2882088503`) — In Development; recurring blocker on Simon's docs
- **#80 Notion Operations Notebook restructure** (`2882088507`) — In Development
- **Build ISO facilitation skill for Simon** (`2889155963`) — In Definition; depends on Simon's references arriving
- **Standup skill v3.x ISO alignment** (`2889202957`) — In Development
- **LinkedIn / GitHub / Kaggle candidate search bot** (`2889210775`) — In Definition; Bonaventure-driven

## Department routing (for new parent items)

| Transcript signal | Target group |
|---|---|
| HR forms, hiring, onboarding, training | HR Department |
| Marketing, CRM, brand, content, lead gen | Marketing Department |
| ISO compliance, audit, policy enforcement | ISO Department |
| Operations, post-prod support, infra-ops, vendor mgmt, finance dashboards | Operations Department |
| Cross-cutting tech, AI policy, anything not above | Planned Automations |

If routing confidence < 70%, [[standup]] asks before creating.

## What lives here vs. elsewhere

- Tasks, automations, projects, action items, sub-items → here
- AI Tools Registry (descriptions, costs, tier, evaluations) → [[ai-registry]] (NOT here)
- Recruitment pipeline tactical work → [[monday]] (Assessify item here is just a bridge)
- Standup logs / decisions / next-step plans → [[notion]]

## Related

- Skill that writes: [[standup]]
- Reconciliation target: [[linear]]
- Bridge to recruitment: [[monday]]

---

## Operational notes — Monday HR Dashboard

_Migrated from the personal-vault 'AI Office Brain' base, 2026-06-09._

# Monday — HR Dashboard (Recruitment & Leave Management)

Board ID: `5095636727`
URL: https://janusd-company.monday.com/boards/5095636727

Dedicated board for the HR recruitment pipeline + leave management work. Created 1 May 2026 from a separate HR meeting (Fireflies `01KQH403N18AFABK6Y5R5CCMV6`), distinct from the AIO standup transcripts.

## Scope

Covers Assessify gaps, recruitment tracker, AI/CV scoring, Fireflies post-interview analysis, Slack-based leave workflow, Deel.com sync, dashboard UX. **28 items** prioritised P0 → P3.

## Groups (priority-based)

| Group | ID | Purpose |
|---|---|---|
| P0 — Critical (Start This Week) | `group_mm2yndrs` | Top group |
| P1 — Recruitment Tracker & Dashboard | `group_mm2yhfsb` | |
| P1 — Assessify Gaps (Pre & Post Interview) | `group_mm2ywrz7` | |
| P2 — Leave Management Workflow | `group_mm2yj650` | |
| P2 — AI / Fireflies / Slack Integrations | `group_mm2y5crs` | |
| P3 — Future / Backlog | `group_mm2yzj7b` | |

## Schema

### Columns

| Column | ID | Type | Notes |
|---|---|---|---|
| Name | `name` | name | |
| Status | `color_mm2y1rqc` | status | Working on it / Done / Stuck |
| Priority | `color_mm31z70m` | status | Critical / High / Medium / Low |

Notably **no Sub-items, no Source, no Owner column** — this board is a flat priority-grouped checklist, not a project hierarchy.

## Bridge to [[monday]]

The "Assessify HR platform" item on [[monday]] (id `2881310536`) is the **bridge**: it carries the operational status (currently In Testing) and gets touched by [[standup]] each day Assessify or recruitment-pipeline work is discussed. The detailed task-level work lives here, not on Automations.

When a standup mentions HR/recruitment work that's already covered by an HR Dashboard item, [[standup]] **does not duplicate** — it posts a consolidated next-step Update on the Assessify Automations item instead, with deep links to the relevant HR Dashboard items.

## Key items (snapshot)

- **HR: Share 10 sample CVs + pre-interview assessment templates** (`2884092914`) — Working on it
- **Build CV-to-JD pre-interview scoring engine** (`2884093144`)
- **Build post-interview assessment module (Fireflies transcript scoring)** (`2884097641`)
- **Build Slack leave request form** (`2884097695`)
- **Sync leave balances with Deel.com (single source of truth)** (`2884091103`)
- **Fireflies webhook → shared inbox → auto-import transcripts** (`2884098351`)
- **Career page → direct candidate intake automation** (`2884089201`) — P3
- *(plus 21 more across recruitment, assessment, leave, integrations)*

## Not orchestrated by [[standup]]

[[standup]] does not write to this board directly. The HR team manages it. [[standup]] only references it (links from Assessify bridge item, mentions in Notion entries) when standup discussion touches recruitment work.

## Related

- Bridge item: [[monday]] → Assessify HR platform (`2881310536`)
- Skill at the platform level: [[assessify]]
- HR backend: Deel ([[linear]] AIP-15 capability assessment)
