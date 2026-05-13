---
type: decision
title: Recruitment automation execution lives on the HR Dashboard Monday board
slug: 2026-05-04-recruitment-execution-on-hr-dashboard-board
created: 2026-05-06
updated: 2026-05-06
departments: [ai-office, hr]
status: resolved
owner: michael
sources: [aio-2026-05-04]
---

# Recruitment automation execution lives on the HR Dashboard Monday board

**Decision date:** 2026-05-04
**Decided by:** Michael Bruck, Jehad Altoutou
**Source:** [[aio-2026-05-04]]

## What

The expanded SSFI / Assessify recruitment automation pipeline is executed on the dedicated HR Dashboard — Recruitment & Leave Management Monday board (`5095636727`). The "Assessify HR platform" item on the AIO Automations board (`5095012818`) acts as the bridge — the bookkeeping reference that points at the real execution surface.

## Why

The recruitment pipeline grew large enough (28 items, P0–P3 prioritised) to warrant its own board rather than crowding the AIO Automations board. The bridge pattern keeps AIO standups aware of the work without duplicating tasks.

## Implications

- All recruitment-pipeline tasks (CV intake form, AI pre-assessment, Slack notifications, interview scheduling, Fireflies pull, post-assessment scoring) live on the HR Dashboard.
- Status reporting back to AIO standups goes via the Assessify bridge item.
- Future AI Office ↔ HR coordination follows the same bridge-item pattern when execution should be HR-owned.
