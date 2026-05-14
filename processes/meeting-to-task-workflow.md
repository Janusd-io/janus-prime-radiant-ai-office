---
type: process
title: Meeting → Task → Build workflow
slug: meeting-to-task-workflow
created: 2026-05-14
updated: 2026-05-14
captured_by: jehad-altoutou
audience: department
departments: [ai-office]
sources: [sub-process-meeting-to-task, diagram-prompt-meeting-to-task, parent-process]
related: [standup, ai-registry, ai-tool-evaluation, linear, monday-rollout, ims-process-document-shape, iso-9001-figure-1]
---

# Meeting → Task → Build workflow

How requirements become tracked tasks become deployed software at Janus Digital — AI Operations. This is the **sub-process implementation of Activity 1 ("Gather requirements")** through **Activity 6 ("Handover to IT")** in Jehad's AI Operations Engineer parent process. Process Owner: [[jehad-altoutou]]. Underlying technical skill: [[standup|/standup v3.11]].

The operational pattern is captured here for cross-reference; the authoritative running implementation is the `/standup` skill. Don't paraphrase phase logic from this page when running an actual standup — invoke the skill.

## Three-phase model (read-only → read-only → writes-only)

**Phase 1 — Analyse (read-only).** Retrieve Fireflies transcript · build Meeting Intelligence Digest · Notion idempotency check · parse Digest into typed items. *No writes occur until decision is made.* Fireflies auto-summary is treated as a weak hint, never canonical.

**Phase 2 — Plan (read-only).** Confidence-scored matching (high ≥85% / medium 60-84% / low <60%) against existing Monday tasks / Linear AIP / Notion entries · duplicate detection · parent project routing · Subagent Dispatch Gate · compile execution plan · Execution Control Mode check (>15 actions OR >3 subagent dispatches → requires literal "Approve execution" phrase).

**Phase 3 — Execute (writes only, strict priority order).** Monday Automations writes (Strict Write Safety) → No-orphan next-step pass → Mandatory Context Updates on creates (v3.11) → Subagent dispatch (`/ai-registry` + auto-chained `/ai-tool-evaluation` Gate 1) → Linear AIP reconciliation (Conflict Safety) → Notion journal entry (size hygiene) → Final Execution Report.

## Decision logic

- Confidence ≥85% → execute automatically (subject to Strict Write Safety).
- Confidence 60-84% → paused for approval in Phase 2.
- Confidence <60% → never auto-creates.

## Why this exists

Audit traceability runs end-to-end: every deployed feature traces back to **Monday task → Linear AIP → Notion entry → Fireflies transcript → original meeting**. That's the §7.5 evidence chain. Confidence bands, the Subagent Dispatch Gate, and Conflict Safety on AIP exist because uncontrolled writes from a meeting-derived plan were the failure mode before /standup v3.x.

## ISO clause coverage

- ISO 9001:2015 §8.1 Operational planning · §7.5 Documented information · §8.5.6 Control of changes
- ISO/IEC 27001:2022 A.5 Information security policies · A.8 Asset management (via [[ai-registry|Linear AIR]])
- ISO/IEC 42001:2023 §6.1 AI risk management (auto-chained Gate 1) · §8.2 AI System Impact Assessment (via [[ai-tool-evaluation]] sibling skill)

## Where this slots in

Feeds Activities 2-6 of the AI Operations Engineer parent process: Build in sandbox → Stress test → Fix & enrol → Document → Handover to IT. Becomes part of the **C1 / C2 / S2** IMS process documents once Process Owner assignments are confirmed by [[michael-bruck]].
