---
type: source
slug: automations-2889202957
title: Standup skill v3.x ISO alignment
created: 2026-05-06
updated: 2026-05-06
monday_id: 2889202957
monday_url: https://janusd-company.monday.com/boards/5095012818/pulses/2889202957
board: 5095012818
status: In Development
priority: Medium
source_type: monday-item
---

## Monday item summary

**Title:** Standup skill v3.x ISO alignment  
**Owner:** Jehad Altoutou  
**Status:** In Development  
**Source:** AIO 6 May 2026, 1 May 2026, 4 May 2026  

## Context

The standup skill v3.x is being hardened toward ISO alignment — restructuring the project schema on Monday to match ISO input/activities/output. Version 2.1 remains in production until v3 is ISO-aligned. As of 6 May, the skill reached v3.12 and is "almost done"; sub-skill orchestration is working, and the mandatory Description Update on every create is producing per-task context blocks across the board.

## Status updates

**6 May 2026 (AIO standup):** Standup skill reached v3.12; Jehad described it as "almost done" and "way better than before." Sub-skill orchestration is confirmed working — the skill auto-dispatched /ai-registry for tools discussed and even self-corrected drift in Linear AIR (moved Monday.com and Hostinger from Evaluation → Sandbox once it noticed they were in active use). Mandatory Description Update on every create (Step 3G) is producing per-task context blocks across the board. Kept In Development — "almost done" is not authoritative completion evidence. Move to In Testing only after Jehad explicitly confirms a clean live run.

**4 May 2026 (AIO standup):** Joint review of standup skill v3.x architecture planned for 5 May. Focus: token-cache flushing concerns, project schema alignment with ISO input/activities/output.

**1 May 2026 (AIO standup):** Continue iterating v3.x toward ISO alignment — restructure project schema on Monday to match ISO input/activities/output. v2.1 remains in production until v3 is ISO-aligned.

## Key capability achievements

- Sub-skill orchestration working: auto-dispatches /ai-registry for AI tools discussed
- Self-correcting: moved Monday.com and Hostinger from Evaluation → Sandbox (noticed they were in active use)
- Description Update blocker: mandatory Description Update Step 3G producing per-task context blocks

## Related wiki

- [[standup|standup skill]] (parent skill)
- [[ai-registry-v2]] (dispatched tasks)
- [[iso-officer-process-documentation]] (ISO schema alignment)
