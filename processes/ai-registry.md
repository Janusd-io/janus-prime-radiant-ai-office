---
type: process
title: AI Registry (Linear AIR) management
slug: ai-registry
created: 2026-05-12
updated: 2026-05-12
departments: [ai-office]
related: [linear, ai-tool-evaluation, standup, claude, anthropic, janus-prime-radiant-build, aio-skills-sor-architecture-jehad, aio-playbooks-jehad]
---

# AI Registry (Linear AIR) management

Janus's reference convention for managing the AI Tools Registry in [[linear]] AIR. Owned by the AI Office. The canonical implementation is the **`/ai-registry` skill** — this wiki page is a short reference for cross-linking and high-level orientation, not a duplicate of the skill. Parallel in shape to [[ai-tool-evaluation]] (which references the `/ai-tool-evaluation` skill).

> **For execution, use the skill.** Do not paraphrase AIR conventions from this page when adding or updating registry entries; the skill is authoritative and may have moved ahead.

## What `/ai-registry` does

CRUD-and-narrative wrapper over [[linear]] AIR (the AI Registry team). The skill is the **only** sanctioned write path into AIR — the [[standup|/standup]] skill dispatches it as a subagent for tool-registry mutations, and the [[ai-tool-evaluation|/ai-tool-evaluation]] skill chains off it for Gate 1 evaluation immediately after a new AIR-N issue is created.

Responsibilities:

- Create AIR issues with the description-template schema (purpose, owner, source, integration sketch, cost class, departments touched, sandbox/production posture).
- Update existing issues as evaluation moves them through the pipeline (Backlog → Evaluating → Sandbox → Production → Monitor → Deprecated / Rejected / Duplicate).
- Apply the AIR label taxonomy (tool/infrastructure/workload classification, ISO-touch flags, departmental tags).
- Read AIR state for cross-references from the wiki and from other skills.

## Pipeline stages (canonical)

| Stage | Meaning |
|---|---|
| **Backlog** | Candidate noted; no evaluation yet started |
| **Evaluating** | Gate 1 triage in progress |
| **Sandbox** | Gate 2 passed; controlled testing underway (Gate 3 in progress) |
| **Production** | Full approval; IT handover complete |
| **Monitor** | In production; watch-list for renewal/replacement/deprecation |
| **Deprecated** | Retired from active use |
| **Rejected** | Failed evaluation; documented reason |
| **Duplicate** | Folded into another entry; pointer maintained |

Tools never return to Backlog once evaluation has begun — see [[2026-05-06-backlog-cleanup-no-return-to-backlog]].

## Tool / Infrastructure / Workload classification

Per [[ai-tool-evaluation]]: classify before evaluating. The skill enforces the trichotomy and applies the right Gate 1 criteria. Tool/Infrastructure/Workload framing affects which AIR labels apply and which gate criteria are scored.

## Relationship to other skills

- **[[standup|/standup]]** — orchestrator. Dispatches `/ai-registry` as a subagent when the standup transcript surfaces a new tool or a stage-change action. Per the v3.10+ chained-evaluation contract, every newly-created AIR-N entry immediately triggers a subsequent `/ai-tool-evaluation` Gate 1 dispatch.
- **[[ai-tool-evaluation|/ai-tool-evaluation]]** — sibling skill. Reads AIR state, posts gate comments, moves the issue between stages. Calls into `/ai-registry` for any write operation; never writes to AIR directly outside the skill's contract.
- **This wiki** — narrative layer. Vendor entity pages cross-reference their AIR issue (when one exists); decision and lesson pages may cite AIR comments. Closed AIR issues with substantive resolution narrative are an ingest source per `CLAUDE.md` §5.1.

## Linkage to systems of record

| Surface | Role | Skill access |
|---|---|---|
| [[linear]] AIR | Pipeline state (canonical) | `/ai-registry` writes; `/ai-tool-evaluation` reads + comments; `/standup` reads only |
| Monday Automations | Execution surface | Tool *adoption work* (sandbox tasks, IT handover items) lives here; not the registry itself |
| Notion Operations Notebook | Daily journal | Decisions about tools captured in standup logs; ingested back into the wiki |
| This wiki | Narrative + cross-cutting analysis | Vendor pages, decisions, lessons, briefs |

## Federated reference

Jehad's federated synthesis pages document the read-vs-write matrix and subagent-dispatch JSON contracts in operational detail — see [[aio-skills-sor-architecture-jehad]] and [[aio-playbooks-jehad]].

## When to update this page

When the `/ai-registry` skill version drifts and the pipeline stages, labels, or subagent-dispatch contract change. For minor internal refinements, the canonical skill file is sufficient — no need to update here.

## Convention note

This page exists so that the wikilink form `[[ai-registry|/ai-registry]]` (display-alias form for slash-command references) resolves cleanly across the wiki. Matches the existing `[[ai-tool-evaluation|/ai-tool-evaluation]]` and `[[standup|/standup]]` convention.
