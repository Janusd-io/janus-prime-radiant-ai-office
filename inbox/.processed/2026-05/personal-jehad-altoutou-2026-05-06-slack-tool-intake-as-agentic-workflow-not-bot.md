---
type: decision
title: Slack tool-intake is an agentic workflow, not a bot
slug: 2026-05-06-slack-tool-intake-as-agentic-workflow-not-bot
created: 2026-05-06
updated: 2026-05-13
departments: [ai-office]
status: resolved
owner: michael-bruck
confidence: high
sources: [pr-backup-2026-05-11-decision-slack-tool-intake-agentic-workflow]
related: [ai-hub-tool-request-bot, slack, michael-bruck, jehad-altoutou]
audience: [department]
captured_by: jehad-altoutou
---

# Slack tool-intake is an agentic workflow, not a bot

**Decision date:** 2026-05-06. **Decided by:** [[michael-bruck]], [[jehad-altoutou]]. Source: AIO 2026-05-06 standup.

## What

The AI Internal Hub Slack tool-intake feature is reframed from "a Slack bot" to **"an agentic workflow with SLA + status loop."** The submitter sees acknowledgement, progress states, and resolution updates — but does not have to direct the work themselves.

## Why

- "Bot" framing implies command-style turn-taking, under-promises on what's being built, and over-promises on responsiveness.
- "Agentic workflow with SLA + status loop" frames it correctly: asynchronous process with clear handoff and feedback semantics. Submitter "feels involved without being involved."
- Framing also clarifies the build target — optimise status communication, SLA adherence; avoid chatbot-style conversational depth that nobody actually wants.

## Implications

- Build is blocked on ISO compliance per [[2026-05-01-iso-compliance-gate-before-automation]].
- When build resumes, design centres SLA + status loop, not natural-language command parsing.
- Internal communication about the feature should use "agentic workflow" framing consistently — avoid "bot."
