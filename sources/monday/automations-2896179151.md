---
type: source
slug: automations-2896179151
title: Singapore market-signals news monitoring agent
created: 2026-05-06
updated: 2026-05-06
monday_id: 2896179151
monday_url: https://janusd-company.monday.com/boards/5095012818/pulses/2896179151
board: 5095012818
status: In Definition
priority: Medium
source_type: monday-item
---

## Monday item summary

**Title:** Singapore market-signals news monitoring agent  
**Owner:** Michael Bruck  
**Status:** In Definition  
**Timeline:** 2026-05-06 → 2026-05-31  
**Source:** Bonaventure / Andrew / Michael News Monitoring meeting — 6 May 2026  

## Context

Bonaventure asked Michael to build an AI-driven monitoring agent that surfaces Singapore market signals (news, government releases, niche analyst newsletters) to seed thought-leadership content, LinkedIn engagement, and conversation starters with prospects.

## Quality-over-quantity intelligence stream

Feeding Janus's marketing engagement ladder: surfaced signal → conversation starter → social engagement → round-table breakfast invite → face-to-face client conversation. Off-the-shelf monitoring tools previously evaluated were weak; build in-house.

## Definition of done (Phase 1)

Daily scheduled pipeline that:
1. Crawls a curated Singapore source list (Straits Times, Business Times, gov.sg ministries for energy, sustainability, urbanisation, labour; niche REIT/asset-manager newsletters)
2. Keyword-filters first pass
3. Semantic-matches against Janus theme profile
4. Posts 1–2 high-signal items/week to Slack as conversation starters (not a news digest, not salesy)
5. Source list and keywords are easy to add/remove as signal/noise emerges

## Out of scope (Phase 1)

- Twitter/X
- Mainstream non-Asian financial press
- Auto-publishing of content
- Multi-country generalisation
- LinkedIn scraping (deferred to Phase 1.5)

## Future phases

**Phase 2:** Response-content generation skill (LinkedIn post / blog / white-paper draft) with explicit thought-leadership-vs-commercial angle rubric. Andrew to define rubric. Requires Bonaventure's Janus knowledge repository as Claude skill.

**Phase 3:** Multi-country generalisation — same framework, swap source list + accounts + ministry list per country.

## Open questions

1. Source list — awaiting Joyce's recommendations
2. Filter sequencing — collect-everything-then-filter (Bonaventure) vs filter-at-source (Michael, cost-driven). Resolve once Phase 1 volume observable
3. Trigger threshold — Andrew's lean: multi-theme intersection ⇒ priority 1
4. Slack channel — new dedicated channel vs 3-person Andrew/Jehad/Michael channel (created 5 May)
5. LinkedIn approach — direct API vs Google-indexed LinkedIn-post search

## Cross-links

- Andrew / Marketing tracker on Notion (6 May entry)
- Related Monday: LinkedIn / GitHub / Kaggle candidate search bot (shared find-and-react primitive, item 2889210775)
- No Linear AIP reference
- No third-party tool eval triggered (in-house build)

## Narrative ownership

Michael: executive owner (agenda-setter, architecture direction, filter sequencing)
Andrew: narrative ownership of rubric and source-list curation (no Monday account; attribution narrative-only)

## Related wiki

- [[singapore|Singapore expansion]]
- [[news-monitoring]]
- [[agentic-ai]]
