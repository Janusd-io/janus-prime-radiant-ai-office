---
type: process
title: Standup Skill (AIO daily standup workflow)
slug: standup
created: 2026-05-07
updated: 2026-05-12
departments: [ai-office]
related: [jehad-altoutou, michael-bruck, ai-tool-evaluation, fireflies, monday, notion, linear, claude, aio-skills-sor-architecture-jehad, aio-playbooks-jehad, ingest-2026-05-11-standup-skill-dual-write-to-aio-inbox, 2026-05-06-standup-skill-v3-12-self-correcting-behavior, april-2026-aio-transcripts-recovery]
---

# Standup Skill

Janus AI Office's end-to-end post-standup processing pipeline: **Fireflies → Monday → Linear AIP → Notion**. Owned by [[jehad-altoutou]]; currently at v3.13 (2026-05-06).

> **For execution, use the skill.** This wiki page is a short reference for cross-linking and high-level orientation, not a duplicate of the skill. The canonical implementation lives at `~/.claude/skills/standup/SKILL.md` and may have moved ahead of what's summarised here.

## What it does

For each AIO standup, the skill consumes the [[fireflies]] transcript and writes:
- A **Clean Meeting Summary** (5–7 bullets) plus time-bucketed next steps (🎯 by next standup / 📅 this week / 🏔️ longer horizon) into the [[notion]] Operations Notebook (`## AIO DD Mon YYYY`).
- Atomic [[monday]] updates: status changes, source-bumps, sub-item creates, Description Updates — all on the AIO Automations board (`5095012818`).
- Linear AIP status reconciliation (read-only by default; updates only when the transcript or completed Monday execution authorises it).

## Architecture (3-phase: Analyse → Plan → Execute)

| Phase | Purpose |
|---|---|
| **Analyse** | Pull the Fireflies transcript; idempotency check against today's Notion entry; extract decisions, action items, vendor mentions, project/Monday references. |
| **Plan** | Match transcript items to Monday tasks and projects; flag conflicts; identify Subagent Dispatch candidates (`/ai-registry`, `/ai-tool-evaluation`); compute write surface and volume. |
| **Execute** | Atomic, idempotent writes to the Monday Automations board; gated subagent dispatches; Linear AIP reconciliation per Conflict Safety rules; Notion entry append. |

## Sub-skill orchestration

Acts as orchestrator for two child skills via isolated Task/Agent subagent dispatch:

- **[[ai-tool-evaluation|/ai-tool-evaluation]]** — Gate 1/2/3 evaluations against tools.
- **/ai-registry** — Linear AIR CRUD for the AI Tools Registry.

Per **chained evaluation (v3.10+)**: when `/ai-registry` creates a new AIR-N issue, `/standup` automatically dispatches `/ai-tool-evaluation` for Gate 1 against that same tool — no separate user confirmation needed.

The skill **never writes to Linear AIR or to the deprecated Monday AI Tools Registry board** — all tool-side work flows through gated subagent dispatch.

## Context Coverage Invariant (v3.13 headline)

Every Monday item the skill *touches* in any Phase 3 step (create, source bump, status change, group move, sub-item add) is guaranteed to carry a `<h2>Description (from meeting notes)</h2>` block in its Updates timeline by the time Phase 3 completes. Three steps enforce this:

- **Step 3G** — mandatory Description Update on every newly created item.
- **Step 3H** — backfill Description Update on touched-but-undocumented items (source bump, status change without prior context).
- **Step 3E.1** — group-move rationale Update whenever an item moves between groups.
- **Step 3I** — coverage check at end of Phase 3; any miss triggers immediate backfill via 3H.

Net effect: anyone opening a touched Monday item sees a Description Update with Source / Why / Definition of done / Cross-links.

## Version history (recent)

- **v3.13 (2026-05-06)** — Context Coverage Invariant extended to every touched item.
- **v3.12 (~2026-05-05)** — Description Update with prominent header; Monday API limitation documented (set_item_description_content returns HTTP 500 on freshly-created items); self-correcting sub-skill orchestration validated. See [[2026-05-06-standup-skill-v3-12-self-correcting-behavior]] for the decision record on the orchestration pattern.
- **v3.11** — Mandatory Context Update on creates (Step 3G).
- **v3.10** — Chained evaluation dispatch (`/ai-registry` → `/ai-tool-evaluation` for new tools).

## Linkage to other surfaces

- The wiki ingests the Notion entries this skill writes — see `CLAUDE.md` §5.1 Notion ingest rules. Standup logs are the highest-signal Notion ingest target.
- The [[monday]] vendor page documents the Automations board this skill operates against.
- The [[ai-tool-evaluation]] reference page documents the framework `/ai-tool-evaluation` implements.

## When to update this page

When the skill version drifts ahead and the high-level architecture changes (phase shape, coverage invariants, sub-skill contracts). For minor version bumps that just refine internals, the canonical skill file is sufficient — no need to update here.

## Reference schemas (snapshot 2026-05-04, AI Office Brain v3.9; cross-checked 2026-05-11)

From Jehad's federated view ([[aio-skills-sor-architecture-jehad]]).

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

## Durability — Fireflies-as-source-of-truth backstop

The transcripts this skill consumes are durable backstops, not ephemeral inputs. When Notion or Monday surfaces fail or lose data, the canonical record can be reconstructed from raw [[fireflies]] transcripts. The [[april-2026-aio-transcripts-recovery]] project is the live validation: ~22 April 2026 standup entries lost from Notion (Notion glitch) are being recovered by re-running raw transcripts through the synthesis pipeline. The Fireflies-as-backstop property is what makes the standup skill safe to evolve aggressively without risking institutional memory.

## Pending v3.14 — wiki inbox dual-write

Open escalation: [[ingest-2026-05-11-standup-skill-dual-write-to-aio-inbox]]. The 2026-05-11 standup surfaced a proposal to extend `/standup` so it writes a markdown version of every standup to the AIO Prime Radiant `inbox/` folder in addition to the Notion entry. Provisionally agreed; question page captures the routing / what-gets-written / order / failure-mode questions awaiting [[michael-bruck|Michael]]'s sign-off. A separate spec exists at `standup-skill-v3.14-wiki-inbox-mirror-spec.md` in the vault root.
