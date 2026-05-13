---
type: process
title: Standup Skill (AIO daily standup workflow)
slug: standup
created: 2026-05-07
updated: 2026-05-13
departments: [ai-office]
sources: [jehad-vault-import-2026-05-13]
related: [jehad-altoutou, michael-bruck, ai-tool-evaluation, ai-tool-evaluation-framework, fireflies, monday-com, notion, linear, claude-code, standup-skill]
captured_by: jehad-altoutou
---

> _Jehad's personal-vault articulation of this topic, imported 2026-05-13. The canonical wiki page is at `processes/standup.md` — this file is preserved as a source for divergent framing / additional context._

# Standup Skill

Janus AI Office's end-to-end post-standup processing pipeline: **Fireflies → Monday → Linear AIP → Notion**. Owned by [[jehad-altoutou]]; currently at v3.13 (2026-05-06).

> Dedupe note: see also the canonical project stub [[standup-skill]]; this page is the process-level reference restored from PR backup.

> **For execution, use the skill.** Canonical implementation lives at `~/.claude/skills/standup/SKILL.md` and may have moved ahead of what's summarised here.

## What it does

For each AIO standup, the skill consumes the [[fireflies]] transcript and writes:
- A **Clean Meeting Summary** (5–7 bullets) plus time-bucketed next steps into the [[notion]] Operations Notebook (`## AIO DD Mon YYYY`).
- Atomic [[monday-com]] updates: status changes, source-bumps, sub-item creates, Description Updates — all on the AIO Automations board (`5095012818`).
- Linear AIP status reconciliation (read-only by default; updates only when the transcript or completed Monday execution authorises it).

## Architecture (3-phase: Analyse → Plan → Execute)

| Phase | Purpose |
|---|---|
| **Analyse** | Pull the Fireflies transcript; idempotency check against today's Notion entry; extract decisions, action items, vendor mentions, project/Monday references. |
| **Plan** | Match transcript items to Monday tasks and projects; flag conflicts; identify Subagent Dispatch candidates (`/ai-registry`, `/ai-tool-evaluation`); compute write surface and volume. |
| **Execute** | Atomic, idempotent writes to the Monday Automations board; gated subagent dispatches; Linear AIP reconciliation per Conflict Safety rules; Notion entry append. |

## Sub-skill orchestration

Acts as orchestrator for two child skills via isolated Task/Agent subagent dispatch:

- **`/ai-tool-evaluation`** — Gate 1/2/3 evaluations against tools. See [[ai-tool-evaluation]].
- **`/ai-registry`** — Linear AIR CRUD for the AI Tools Registry.

Per **chained evaluation (v3.10+)**: when `/ai-registry` creates a new AIR-N issue, `/standup` automatically dispatches `/ai-tool-evaluation` for Gate 1 against that same tool — no separate user confirmation needed.

The skill **never writes to Linear AIR or to the deprecated Monday AI Tools Registry board** — all tool-side work flows through gated subagent dispatch.

## Context Coverage Invariant (v3.13 headline)

Every Monday item the skill *touches* in any Phase 3 step is guaranteed to carry a `<h2>Description (from meeting notes)</h2>` block in its Updates timeline by the time Phase 3 completes. Three steps enforce this:

- **Step 3G** — mandatory Description Update on every newly created item.
- **Step 3H** — backfill Description Update on touched-but-undocumented items.
- **Step 3E.1** — group-move rationale Update whenever an item moves between groups.
- **Step 3I** — coverage check at end of Phase 3; any miss triggers immediate backfill via 3H.

## Version history (recent)

- **v3.13 (2026-05-06)** — Context Coverage Invariant extended to every touched item.
- **v3.12 (~2026-05-05)** — Description Update with prominent header; Monday API limitation documented.
- **v3.11** — Mandatory Context Update on creates (Step 3G).
- **v3.10** — Chained evaluation dispatch (`/ai-registry` → `/ai-tool-evaluation` for new tools).

## When to update this page

When the skill version drifts ahead and the high-level architecture changes (phase shape, coverage invariants, sub-skill contracts).
