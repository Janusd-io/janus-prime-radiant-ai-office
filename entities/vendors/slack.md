---
type: vendor
title: Slack
slug: slack
created: 2026-05-06
updated: 2026-05-06
departments: [ai-office, marketing, it-ops, hr]
status: active
confidence: high
sources: [aio-2026-05-04, aio-2026-05-06]
related: [2026-05-06-slack-tool-intake-as-agentic-workflow-not-bot]
---

# Slack

Real-time messaging platform. Janus's primary chat surface across departments. First-class in the `CLAUDE.md` system-of-record map.

## Use at Janus

- **AI Hub channel** — formal announcement surface for new tools moving to Production in Linear AIR (per the [[ai-tool-evaluation]] Stage 4 announcement step).
- **Recruitment notifications** — part of the SSFI/Assessify pipeline (CV parse → score → Slack notify → interview scheduling).
- **AI Internal Hub bot / agentic workflow** — in-development feature for tool-intake submissions; reframed per [[2026-05-06-slack-tool-intake-as-agentic-workflow-not-bot]] from "a bot" to "an agentic workflow with SLA + status loop." Build blocked on ISO compliance.

## Relationship to this wiki

Slack threads are an ingest source for `sources/slack/` per `CLAUDE.md` §5.1 — bookmarked threads only, treated as high-signal because Michael curated them. Pull whole-thread context, not just the bookmarked message.

## Watch for

- Build resumption of the AI Internal Hub agentic workflow once ISO unblocks.
- Slack Connect adoption (cross-org channels) if Janus engages in inter-company collaboration.
