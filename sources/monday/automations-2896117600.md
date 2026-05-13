---
type: source
slug: automations-2896117600
title: AI agent for IT helpdesk (Slack triage to Zendesk)
created: 2026-05-06
updated: 2026-05-06
monday_id: 2896117600
monday_url: https://janusd-company.monday.com/boards/5095012818/pulses/2896117600
board: 5095012818
status: In Definition
priority: Medium
source_type: monday-item
---

## Monday item summary

**Title:** AI agent for IT helpdesk (Slack triage → Zendesk)  
**Owners:** Michael Bruck, Jehad Altoutou  
**Status:** In Definition  
**Source:** AI/IT Mtg 6 May 2026  

## Context

Today's Slack→Zendesk integration is "stupid integration" — text passthrough, no intelligence. Same agentic-feedback-loop pattern designed for the AI Internal Hub (tool requests) applies to IT helpdesk: user reports issue in Slack → triage bot asks clarifying questions → proposes solution → only escalate to Zendesk if unresolved. KB grows over time.

## Definition of done

- Slack-side triage bot live
- Replaces dumb passthrough integration
- Zendesk receives only escalated, pre-triaged tickets with conversation context
- First-week deflection rate measurable

## Key updates

**6 May 2026 (AI ↔ IT Meeting):** Michael described the pattern: "If we could have some bot on the Slack side or on Zendesk somewhere… that will just ask some questions… maybe it can propose some solution. So we don't even have to create a ticket or maybe it will create a ticket later." Architecture mirrors AI Internal Hub bot (item 2882214985). Two distinct scopes: AI Hub is tool requests; IT helpdesk is user support issues.

**Next steps (by 13 May):**
- Spec the Slack → triage → Zendesk user journey (2896120889)
- Build (replace passthrough) by 22 May (2896131018)
- Coordinate with AI Internal Hub Slack bot (2882214985) for shared infra

## Related wiki

- [[ai-internal-hub-slack-bot]] (mirror architecture)
- [[agentic-ai]] (design pattern)
