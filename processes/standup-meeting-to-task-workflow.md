---
type: process
title: Meeting-to-Task Workflow (standup skill orchestrator)
slug: standup-meeting-to-task-workflow
created: 2026-05-14
updated: 2026-05-14
departments: [ai-office]
status: active
captured_by: jehad-altoutou
owner: jehad-altoutou
audience: [department]
sources: [puls-meeting-to-task-workflow]
related: [jehad-altoutou, fireflies, monday, linear, notion, ai-registry, ai-tool-evaluation]
---

# Meeting-to-Task Workflow

[[jehad-altoutou]]'s end-to-end procedure for converting AI Office meetings into tracked tasks, logged work, and executed builds. Implements Activity 1 (Gather requirements) through Activity 6 (Handover to IT) of his AI Operations Engineer role.

## Three-phase model

- **Phase 1 — Analyse (read-only):** retrieve [[fireflies]] transcript, build Meeting Intelligence Digest, [[notion]] idempotency check, parse digest into typed items.
- **Phase 2 — Plan (read-only):** confidence-scored matching against existing [[monday]] / [[linear]] AIP / Notion state, duplicate detection, Subagent Dispatch Gate, generate execution plan, Execution Control Mode threshold check.
- **Phase 3 — Execute (writes only):** Monday writes → no-orphan owner pass → Context Updates → subagent dispatch ([[ai-registry]], [[ai-tool-evaluation]]) → Linear AIP reconciliation → Notion journal entry → Final Execution Report.

## Trigger

User says "Process today's standup" or "Log the standup from <date>" in Claude Desktop. The `/standup` skill (v3.11+) orchestrates everything described above.

## ISO clauses satisfied

9001 §8.1, §7.5, §8.5.6 · 27001 A.5, A.8 · 42001 §6.1, §8.2.
