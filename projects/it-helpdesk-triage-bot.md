---
type: project
title: IT Helpdesk Triage Bot
slug: it-helpdesk-triage-bot
created: 2026-05-07
updated: 2026-05-07
departments: [it-ops, ai-office]
status: active
owner: jehad-altoutou
sources: [aio-2026-05-06, it-discussion-tracker, automations-2896117600]
related: [slack, jehad-altoutou, andrey-timokhov, euclid-wong, it-department-standup-pilot, 2026-05-06-slack-tool-intake-as-agentic-workflow-not-bot]
---

# IT Helpdesk Triage Bot

Hub for the [[slack]]→triage→Zendesk agentic workflow that replaces dumb passthrough on IT support requests. Mirrors the AI Internal Hub agentic-workflow pattern (per [[2026-05-06-slack-tool-intake-as-agentic-workflow-not-bot]]) but in a different problem space (user support, not tool requests).

## Scope

- **Slack ingest** — IT helpdesk channel posts captured.
- **Triage** — agent classifies issues (password reset / SSO / hardware / software access / escalation), suggests resolution path.
- **Zendesk handoff** — substantive issues open a Zendesk ticket with triage context pre-filled; trivial resolutions stay in Slack with logged outcomes.
- **SLA + status loop** per the agentic-workflow framing: requester sees acknowledgement, classification, progress, resolution.

## Why a separate project from [[it-department-standup-pilot]]

Same department coordination cadence; different problem space and architecture. Helpdesk triage is user-facing automation; the standup pilot is internal team-process automation. They share IT-team coordination but should not be tracked as one piece of work.

## Timeline

- **Spec by 2026-05-13.**
- **Build by 2026-05-22.**

## Architecture pattern

Mirrors the AI Internal Hub design (Slack-first agentic workflow with SLA + status loop), substituting the IT-support intent classifier for the tool-intake form. The relevance: the AI Internal Hub is currently blocked behind ISO compliance; this bot is a candidate first-mover that proves the pattern in a lower-policy-friction domain.

## Success criteria

- First-week deflection rate measurable (% of issues resolved in Slack vs. handed off to Zendesk).
- No degradation in time-to-resolution vs. baseline.
- Clear escalation path for issues the bot can't classify.

## Watch for

- Whether the triage classifier needs domain fine-tuning or if a general LLM with prompts is sufficient.
- Pattern viability for the AI Internal Hub once ISO unblocks it.
