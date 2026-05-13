---
type: source
slug: automations-2894742266
title: Singapore market-intelligence news bot
created: 2026-05-06
updated: 2026-05-06
monday_id: 2894742266
monday_url: https://janusd-company.monday.com/boards/5095012818/pulses/2894742266
board: 5095012818
status: In Definition
priority: Medium
source_type: monday-item
---

## Monday item summary

**Title:** Singapore market-intelligence news bot  
**Owner:** Jehad Altoutou  
**Status:** In Definition  
**Source:** AIO 6 May 2026  

## Context

Bonaventure asked Michael for a daily news bot tailored to Singapore market intelligence, triggered by the Singaporean PM's recent AI/energy speech. Janus's first commercial footprint is Singapore, so this bot becomes the always-on radar for relevant local news, regulation, and competitor moves.

## Definition of done

A scheduled bot (likely cron / Windmill / N8N) that:
- Ingests curated Singapore news sources (Straits Times, Asia Tech outlets, PM-office releases, RSS/XML)
- Runs site-tailored scrapers
- Summarises with a cheap LLM (DeepSeek-class)
- Groups by sub-theme
- Emails / Slacks a daily digest with global summary + sub-theme rollup + source links
- Output quality matches Eddie's reference Asia-Tech digest

## Key updates

**6 May 2026 (AIO standup):** Bonaventure triggered the request. Michael's clarification: "What kind of news is he looking for? How do we filter it? Is it keywords? Is it a thematic search?"

**Next steps (by next standup):**
- Schedule requirements meeting with Bonaventure + Andrew + Jehad (sub-item 2894728110)
- Outputs: news sources, keywords vs thematic filter, daily-digest format
- Build sub-items unblock once requirements land

## Notes

- Jehad has prior scraper experience; Beautiful Soup alone insufficient, expect bespoke per-source scrapers
- Content in Updates because Monday's set_item_description_content mutation is broken for newly created items

## Related wiki

- [[singapore|Singapore expansion]] (country-context)
- [[news-monitoring]] (automation type)
