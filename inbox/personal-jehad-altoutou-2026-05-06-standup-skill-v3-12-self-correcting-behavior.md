---
type: decision
title: Standup skill v3.12 demonstrates self-correcting behavior in Linear AIR
slug: 2026-05-06-standup-skill-v3-12-self-correcting-behavior
created: 2026-05-06
updated: 2026-05-13
departments: [ai-office]
status: resolved
owner: jehad-altoutou
confidence: high
sources: [pr-backup-2026-05-11-decision-standup-v3-12-self-correcting]
related: [standup-skill, ai-registry, linear, iso-compliance-programme]
audience: [department]
captured_by: jehad-altoutou
---

# Standup skill v3.12 demonstrates self-correcting behaviour in Linear AIR

**Decision date:** 6 May 2026. **Owner:** [[jehad-altoutou]]. Source: `automations-2889202957`.

## What

As of 6 May 2026, standup skill v3.12 has demonstrated **self-correcting behaviour in the AI Registry**: the skill auto-dispatched /ai-registry entries for tools discussed in standups AND self-corrected drift in [[linear]] AIR by moving [[monday]] and [[hostinger]] from Evaluation → Sandbox because the skill noticed these tools were in active use, not evaluation stage.

Status: **In Development, not yet In Testing.** Move to In Testing only after [[jehad-altoutou]] explicitly confirms a clean live run.

## What worked

- Sub-skill orchestration confirmed working.
- Mandatory Description Update on every create (Step 3G) producing per-task context blocks across Monday board.
- Auto-dispatch to /ai-registry for AI tools mentioned in standups.
- Drift-detection and self-correction in Linear AIR.

## Why it matters

First evidence that the standup skill's multi-tool orchestration (Monday → Linear AIR → Notion sync) is achieving its goal of keeping system-of-record data consistent. Self-correction is not a bug — it's the skill doing what it was designed to do.

## Caution

Jehad described the skill as "almost done" and "way better than before," but "almost done" is not authoritative completion evidence. Keeping status at In Development until Jehad validates a full clean live run.

## Confidence

High for capabilities demonstrated; medium for production-readiness (pending full validation).
