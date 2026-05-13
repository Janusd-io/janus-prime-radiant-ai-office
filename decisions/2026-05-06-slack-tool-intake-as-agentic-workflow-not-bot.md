---
type: decision
title: Slack tool-intake is an agentic workflow, not a bot
slug: 2026-05-06-slack-tool-intake-as-agentic-workflow-not-bot
created: 2026-05-06
updated: 2026-05-06
departments: [ai-office]
status: resolved
owner: michael
sources: [aio-2026-05-06]
---

# Slack tool-intake is an agentic workflow, not a bot

**Decision date:** 2026-05-06
**Decided by:** Michael Bruck, Jehad Altoutou
**Source:** [[aio-2026-05-06]]

## What

The AI Internal Hub Slack tool-intake feature is reframed from "a Slack bot" to "an agentic workflow with SLA + status loop." The submitter sees acknowledgement, progress states, and resolution updates — but does not have to direct the work themselves.

## Why

- "Bot" framing implies command-style turn-taking, which under-promises on what's actually being built and over-promises on responsiveness.
- "Agentic workflow with SLA + status loop" frames it correctly: an asynchronous process with clear handoff and feedback semantics. The submitter "feels involved without being involved."
- This framing also clarifies the build target — what to optimise (status communication, SLA adherence) vs what to avoid (chatbot-style conversational depth that nobody actually wants).

## Implications

- Build is blocked on ISO compliance per [[2026-05-01-iso-compliance-gate-before-automation]].
- When build resumes, design centres SLA + status loop, not natural-language command parsing.
- Internal communication about the feature should use "agentic workflow" framing consistently — avoid "bot."
