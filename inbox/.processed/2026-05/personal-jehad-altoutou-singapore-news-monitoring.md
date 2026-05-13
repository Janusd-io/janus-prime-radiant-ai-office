---
type: project
title: Singapore News Monitoring Agent
slug: singapore-news-monitoring
created: 2026-05-07
updated: 2026-05-13
departments: [marketing, ai-office]
countries: [sg]
status: active
owner: michael-bruck
sources: [pr-backup-2026-05-11-project-singapore-news-monitoring]
related: [bonaventure-wong, andrew-soane, jehad-altoutou, slack, singapore-launch-campaign]
audience: [department]
captured_by: jehad-altoutou
---

# Singapore News Monitoring Agent

Hub for the Bonaventure-driven market-intelligence agent: scheduled pipeline that crawls Singapore news sources, semantic-matches against Janus themes, and posts 1–2 high-signal items per week to [[slack]]. First commercial-footprint signal capture for Janus's Singapore office.

## Phased scope

| Phase | Focus | Out of scope |
|---|---|---|
| **Phase 1** — News curation | Scrape per-source Singapore outlets, deduplicate, semantic-rank against Janus themes, post top 1–2/week to Slack. | Twitter, mainstream financial press, auto-publishing. |
| **Phase 2** — Response-content generation | Auto-draft Janus response posts / commentary for Andrew's review. | Direct publishing (always human-in-the-loop). |
| **Phase 3** — Multi-country | Same architecture extended to other Janus markets as offices open. | — |

Timeline: Phase 1 build window 2026-05-06 → 2026-05-31 (~8 weeks).

## Why this matters

First *named* market-intelligence project tied to a specific country footprint. Bonaventure asked for it directly; ties Janus's Singapore office (officially open 2026 W19) to operational signal capture rather than passive press monitoring. Doubles as proof-of-concept for the per-country pattern as Janus expands.

## Strategic intent (2026-05-07)

Fuel **round-table breakfast events** Bonaventure wants to seed; output is **conversation starters and content seeds** delivered to Slack — explicitly **NOT** news summary. Quality bar 1–2 nuggets per week. Architecture confirmed two-pass: wide keyword/site collection first, then semantic theme matching. Twitter/X explicitly de-prioritised for Phase 1. [[joyce]]'s recommended outlets are the anchor source list; iterate as signal/noise emerges.

## Architecture (as of 2026-05-06)

- **Per-source scrapers** — Jehad has prior scraper experience; build per-outlet scrapers for chosen Singapore sources.
- **Semantic ranking** — score each item against Janus theme prompts.
- **Slack delivery** — post curated items to a dedicated channel; format includes source, summary, why-it-matters reasoning.
- Possibly involves [[whisperflow]] for voice-summary outputs (Phase 2, speculative).

## Active dependencies

- **Requirements meeting** with Bonaventure + Andrew + Jehad — Michael to schedule.
- **Source list** lock-in — which Singapore outlets are in scope for Phase 1.
- **Janus theme prompts** — Andrew owns this (curation framework).

## Owners

- **Strategic / executive:** [[michael-bruck]]
- **Curation framework + content review:** [[andrew-soane]]
- **Build:** [[jehad-altoutou]]
- **Sponsor:** [[bonaventure-wong]]

## Watch for

- Requirements meeting outcome (source list, theme prompts, success criteria).
- First Slack post (proof-of-life).
- Phase 1 → Phase 2 gate: signal-quality threshold required before automating commentary drafts.
