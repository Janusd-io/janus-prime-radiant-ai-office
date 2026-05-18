---
type: vendor
title: Notion
slug: notion
created: 2026-05-06
updated: 2026-05-18
departments: [ai-office, it-ops, office-of-ceo]
status: deprecating
confidence: high
sources: [2026-05-13-aio-it-meeting, 2026-05-18-ai-native-ceo]
related: [michael-bruck, janus-prime-radiant-build, 2026-05-11-notion-restricted-to-aio-no-broad-rollout]
---

# Notion

Workspace, wiki, and docs platform. At Janus, primary use was the **Operations Notebook** — the forward-looking journal / reporting surface for AIO operations.

## Deprecation (as of 2026-05-13, reconfirmed 2026-05-18)

**Notion deprecation target: end of May 2026.** Confirmed in [[2026-05-13-aio-it-meeting]]. Reconfirmed by Bonaventure Wong in the [[2026-05-18-ai-native-ceo|18 May 2026 CEO meeting]] — "one fewer tool in the stack." The transition path is dual-write: the `/standup` skill (v3.15+) writes standup logs both to Notion (legacy) and to the Prime Radiant vault inbox via MCP connector (Step 5G). After end of May, Notion-side writes stop and Prime Radiant becomes the sole journal surface. This aligns with [[2026-05-11-notion-restricted-to-aio-no-broad-rollout|Bonaventure's no-broad-Notion-rollout decision]] and the [[janus-prime-radiant-build]] program direction.

## Scope at Janus (historical)

The Operations Notebook is where the `/standup` skill writes daily standup logs (`## AIO DD Mon YYYY` entries) consolidating decisions, next-step planning, and registry/evaluation outcomes from each day. Beyond the standup journal, Notion also hosts project documentation tied to active Monday projects and ad-hoc internal documentation.

## Relationship to this wiki

Notion was authoritative for the daily operations narrative — what was discussed, what was decided, what's queued next. This wiki ingests Notion pages selectively, focused on the standup-log entries which are the densest carrier of decisions and rationale. Per `CLAUDE.md` §5.1.

The wiki is the **synthesis layer over Notion**, not a replacement for it — until end of May 2026, when Prime Radiant absorbs the journal role and Notion exits the operational stack.
