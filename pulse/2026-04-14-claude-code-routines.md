---
type: pulse
title: Claude Code introduces routines — scheduled, event-driven Claude Code automations
slug: 2026-04-14-claude-code-routines
created: 2026-05-06
updated: 2026-05-06
departments: [ai-office, engineering]
confidence: high
sources: [claude-code-routines]
related: [agentic-ai, agent-harness]
---

# Claude Code routines launch in research preview (2026-04-14)

[[anthropic|Anthropic]] introduced **routines** in [[claude|Claude]] Code: a Claude Code automation configured once (prompt + repo + connectors) and then triggered on a schedule, from an API call, or in response to an event. Routines run on Claude Code's web infrastructure rather than the user's laptop.

Use-cases pitched in the announcement: working through a backlog, reviewing PRs, responding to events.

## Why this matters

Pushes Claude Code from "synchronous coding assistant" toward "asynchronous, always-on agent." Compares directly with [[2026-04-08-claude-managed-agents-launch]] — same direction (cloud execution, no laptop dependency), different surface (Claude Code's coding-flavoured framing vs. Managed Agents' generic API).

For Janus: routines are interesting for any recurring AI Office workflow that's currently human-triggered (e.g., reviewing the AI Registry weekly, summarising recent industry pulse entries). Worth a Stage 1 viability look once it's out of research preview.

## Watch for

- Reliability and monitoring story (research preview = expect breakage).
- Pricing once it leaves preview.
- Overlap with Managed Agents — at what point is "routines in Claude Code" just "Managed Agents with a coding flavour"?
