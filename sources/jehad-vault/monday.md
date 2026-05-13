---
type: vendor
title: Monday
slug: monday
created: 2026-05-13
updated: 2026-05-13
departments: [ai-office, hr, marketing, it-ops]
status: active
confidence: high
sources: [jehad-vault-import-2026-05-13]
related: [linear, monday]
captured_by: jehad-altoutou
---

> _Jehad's personal-vault articulation of this topic, imported 2026-05-13. The canonical wiki page is at `entities/vendors/monday.md` — this file is preserved as a source for divergent framing / additional context._

# Monday

Work management platform (monday.com). Janus's primary execution surface for tasks, projects, and action tracking — first-class in the system-of-record map. Existing vault page `monday-com.md` is a thin stub under a less-canonical slug; flagged as dedup.

## Boards in active use

| Board | ID | Scope |
|---|---|---|
| **Automation Plans & Task Tracking** | `5095012818` | Primary execution surface for AIO; the `/standup` skill writes to this board. |
| **HR Dashboard — Recruitment & Leave Management** | `5095636727` | Dedicated board for SSFI / Assessify pipeline. |
| **AI Tools Registry** *(deprecated)* | `5095577150` | Historical reference only; no new writes. AI Tools Registry lives exclusively in Linear AIR. |

## Status (as of 2026-05-06)

In Sandbox in Linear AIR (auto-promoted from Evaluating by the standup skill v3.12 upon noticing active use). Production push targeted that week per 2026-05-06-monday-com-to-production-this-week — first concrete sandbox→production promotion in the new IT hand-off process.

## Janus conventions

- **Context Coverage Invariant** (from /standup skill v3.13): every Monday item the skill touches in any phase carries a `<h2>Description (from meeting notes)</h2>` block in its Updates timeline.
- **Board-segmentation principle:** workstreams large enough to warrant their own board get one, with a "bridge item" on the AIO Automations board pointing to the dedicated board.

## Relationship to this wiki

Monday is an ingest source for `sources/monday/` per CLAUDE.md §5.1. Filter: completed tasks with substantive Description Updates; standup-execution items where the Context Coverage Invariant block carries non-trivial rationale.

## Watch for

- Production promotion — first real test of the IT hand-off template.
- Whether the deprecated AI Tools Registry board ever gets fully archived or stays read-only.
