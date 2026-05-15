---
type: project
title: Singapore News Monitoring Agent
slug: singapore-news-monitoring
created: 2026-05-07
updated: 2026-05-15
departments: [marketing, ai-office]
countries: [sg]
status: active
owner: michael-bruck
sources: [aio-2026-05-06, automations-2894742266, automations-2896179151, 2026-05-12-bonaventure-ai-native-call, 2026-05-15-singapore-marketing-launch-plan-v1, jehad-vault-singapore-news-monitoring]
related: [bonaventure-wong, andrew-soane, jehad-altoutou, slack, ai-native-janus-positioning, 2026-05-12-singapore-as-lead-market, 2026-05-12-vivian-balakrishnan-llm-wiki-government, ingest-2026-05-12-1730-vivian-balakrishnan-and-factset, marketing-prime-radiant, ingest-2026-05-15-joyce-woo]
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

First *named* market-intelligence project tied to a specific country footprint. Bonaventure asked for it directly; ties Janus's Singapore office (officially open 2026 W19) to operational signal capture rather than passive press monitoring. Doubles as a proof-of-concept for the per-country pattern as Janus expands (UK offices opening 2026 W20).

**Strategic promotion (12 May 2026):** Per [[2026-05-12-singapore-as-lead-market]], Singapore is now Janus's lead commercial market for AI Native products. This project moves from "sponsored signal-capture" to *commercial-gating intelligence layer* — the Singapore news monitoring feeds the [[ai-native-janus-positioning|three-pillar messaging]] pipeline and underpins Bonaventure's July luncheon with Singapore asset managers built on the back of the PM's AI-in-REITs white paper.

## Update — 2026-05-07

The 6 May Bonaventure / Andrew / Michael session captured by [[andrew-marketing-discussion-tracker]] adds substantial detail. Strategic intent: fuel **round-table breakfast events** Bonaventure wants to seed; output is **conversation starters and content seeds** delivered to Slack — explicitly **NOT** news summary. Quality bar 1–2 nuggets per week. Architecture confirmed two-pass: wide keyword/site collection first, then semantic theme matching. Andrew framing aligns with the find-and-react capability previously discussed for LinkedIn outreach, scoped today to Singapore. Twitter/X explicitly de-prioritised for Phase 1. Joyce's recommended outlets are the anchor source list; iterate as signal/noise emerges. Per the 7 May standup, a duplicate Monday item ("Singapore market signals" `2896179151`) was deprecated; merge into the parent Monday item is queued for 8 May.

## Architecture (as of 2026-05-06)

- **Per-source scrapers** — Jehad has prior scraper experience; build per-outlet scrapers for chosen Singapore sources (list TBD in requirements meeting).
- **Semantic ranking** — score each item against Janus theme prompts.
- **Slack delivery** — post curated items to a dedicated channel; format includes source, summary, why-it-matters reasoning.
- Possibly involves [[wispr-flow]] for voice-summary outputs (speculative; explore in Phase 2).

## Active dependencies

- **Requirements meeting** with Bonaventure + Andrew + Jehad — Michael to schedule (pending as of 2026-05-06).
- **Source list** lock-in — which Singapore outlets are in scope for Phase 1.
- **Janus theme prompts** — to give the semantic ranker its scoring vocabulary; Andrew owns this (curation framework).

## Owners

- **Strategic / executive:** [[michael-bruck]]
- **Curation framework + content review:** [[andrew-soane]]
- **Build:** [[jehad-altoutou]]
- **Sponsor:** [[bonaventure-wong]]

## Watch for

- Requirements meeting outcome (source list, theme prompts, success criteria).
- First Slack post (proof-of-life).
- Phase 1 → Phase 2 gate: signal-quality threshold required before automating commentary drafts.

## Update — 2026-05-12 AI Native CEO call

Several material updates from the 12 May call with Bonaventure ([[2026-05-12-bonaventure-ai-native-call]]):

- **Data source candidate: FactSet.** Bonaventure suggested it; Michael endorsed ("poor man's Bloomberg" but with built-in AI/MCP/API integration). Perplexity and City Finance use FactSet as their financial-data source. Already in Linear AIR per Michael — wiki vendor page proposed in [[ingest-2026-05-12-1730-vivian-balakrishnan-and-factset]]. Adjacent candidate: Alpha Sites (single-mention, defer). **Andrew pushback (12 May 3pm session, see [[2026-05-12-andrew-onboarding-review]]):** FactSet should NOT be called out as a primary anchor source; it belongs under a generic "news sources / information gathering" category. Andrew's primary intelligence channel is **LinkedIn** (plus Twitter); FactSet is one of many.
- **July luncheon target.** Bonaventure is preparing a Singapore asset-manager luncheon for July on the back of the PM's AI-in-REITs white paper. The news-monitoring agent should be operational with at least Phase 1 signals flowing by then.
- **Government advocate emerging.** Singapore Foreign Minister [[vivian-balakrishnan|Dr. Vivian Balakrishnan]] (Bonaventure knows him personally, was Ambassador to UAE) is keynoting AI Engineering Conference 16–17 May and runs his own LLM wiki on a Raspberry Pi. Bonaventure: "He could be our advocates inside of the government there." See [[2026-05-12-vivian-balakrishnan-llm-wiki-government]].
- **REIT-level data drill-through is the holy grail.** Bonaventure: "Imagine Janus affecting every single price, stock price, because of us, NOI are real time, then quarterly and such." Theme prompts should weight signal sources by REIT-level data utility.
- **Singapore PM white paper** to be shared by Bonaventure when he receives it. Worth ingesting as a primary source for the theme prompts when it lands.
- **External-network momentum** — Bonaventure had lunch on 12 May with Steve (going to Singapore to discuss real-time data with central banks); Bonaventure pitched Janus's REIT angle to him as a concrete entry point.
