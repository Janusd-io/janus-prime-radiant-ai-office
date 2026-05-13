---
type: source
slug: automations-2881310536
title: Assessify HR platform — Recruitment automation pipeline
created: 2026-05-06
updated: 2026-05-06
monday_id: 2881310536
monday_url: https://janusd-company.monday.com/boards/5095012818/pulses/2881310536
board: 5095012818
status: In Testing
priority: Medium
source_type: monday-item
---

## Monday item summary

**Title:** Assessify HR platform  
**Owner:** Jehad Altoutou  
**Status:** In Testing  
**Source:** AIO 5 May 2026, 4 May 2026  

## Context

Assessify is being integrated as a recruitment automation bridge, powering a full CV → pre-assessment → Slack notification → interview → post-assessment pipeline. Execution work is tracked on a dedicated HR Dashboard board (28 items, P0→P3 prioritised); this Monday item is the Automations-board bridge for status, ownership, and standup-driven decisions.

## Key updates (most recent first)

**5 May 2026 (AIO standup):** Direction confirmed — move from Bonaventure's project + thread approach to a reusable Claude skill (agentic flow). Inputs: CV, JD, interview transcript. Blockers: Marianne does not hold the formal QBIC scoring metrics; Teresa / Mariam to provide sample CVs, JDs, and interview outputs. Architecture: dedicated Fireflies invitee email auto-records interviews and triggers a post-assessment skill via webhook (design only this round).

**Next steps (by next standup):**
- Obtain QBIC recruitment scoring metrics
- Collect sample CVs / JDs / interview outputs from Teresa / Mariam
- Convert recruitment scoring project + thread into reusable Claude skill
- Design Fireflies webhook for auto post-interview assessment

**4 May 2026 (AIO standup):** Recruitment scope expanded into full pipeline. Tactical work lives on the HR Dashboard (CV intake form, leave balance timeline, line manager dashboard, agentic UI as Deel middleware). Awaiting 10 sample CVs + interview transcripts from Teresa (engaged 1 May). Centralised Fireflies setup planned for interview transcripts (webhook-driven). Stitch (Google) flagged as stronger alternative to Lovable — pending evaluation.

## Related wiki

- [[assessify]] (vendor page candidate)
- [[deel]] (line manager dashboard middleware)
- [[fireflies]] (interview transcript pull + webhook)
