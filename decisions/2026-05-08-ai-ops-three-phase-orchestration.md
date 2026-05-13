---
type: decision
title: "AI Ops task pipeline structured as three-phase orchestration (Analyze, Plan, Execute)"
slug: 2026-05-08-ai-ops-three-phase-orchestration
created: 2026-05-08
updated: 2026-05-13
departments: [ai-office]
status: resolved
owner: jehad-altoutou
decided_by: jehad-altoutou
sources: [2026-05-08-jehad-michael-roza-simon-euclid-bonaventure-meeting, jehad-vault-import-2026-05-13]
related: []
captured_by: jehad-altoutou
confidence: high
---

# AI Ops task pipeline structured as three-phase orchestration (Analyze, Plan, Execute)

## Decision

The AI Operations department's task-development sub-process will run as three orchestration phases: Analyze (read-only ingestion of Fireflies, Slack, Monday/Linear/Notion state), Plan, and Execute (write-only output to Monday tasks, Linear tool entries, and Notion logs).

## Why

Separating read and write phases enforces a deterministic boundary between ingestion and side effects, lets sub-agents handle specialised sub-skills (AI evaluation, AI registry) inside the Execute phase, and allows confidence-scored routing of new items as sub-items of existing tasks rather than creating orphans.

## Evidence

> Speaker 1: It's going to come through three phases. Orchestrations. The first one is analyze... Then it will go through the phase two, which is planning... And the phase three is execution, which is right only.

## When

2026-05-08 · meeting [[2026-05-08-jehad-michael-roza-simon-euclid-bonaventure-meeting]] · decided by [[jehad-altoutou]]

## Implications

- (to be populated by the owner)
