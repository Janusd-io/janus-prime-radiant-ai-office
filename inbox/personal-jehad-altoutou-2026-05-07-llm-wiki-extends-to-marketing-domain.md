---
type: decision
title: LLM Wiki prototype validated; pattern extends to marketing-domain knowledge tool
slug: 2026-05-07-llm-wiki-extends-to-marketing-domain
created: 2026-05-07
updated: 2026-05-13
departments: [ai-office, marketing]
status: resolved
owner: michael-bruck
confidence: high
sources: [pr-backup-2026-05-11-decision-llm-wiki-extends-marketing]
related: [llm-wiki, janus-prime-radiant, andrew-soane, singapore-launch-campaign, 2026-05-05-kb-direction-markdown-progressive-exposure-not-rag]
audience: [department]
captured_by: jehad-altoutou
---

# LLM Wiki extends to marketing-domain knowledge tool

**Decision date:** 2026-05-07. **Decided by:** [[michael-bruck]], [[jehad-altoutou]]. Source: AIO 2026-05-07 standup.

## What

The [[janus-prime-radiant|Janus Prime Radiant prototype]] was demo'd in the 7 May standup — directory-structure + `CLAUDE.md` + Obsidian, pre-processing Notion + clipped X posts + transcripts into concepts/themes/decisions/lessons/briefs/articles. **Verdict: prototype validated.** The pattern will extend to a **marketing-domain knowledge tool** that [[andrew-soane]] needs (signals → rubric → daily briefs), feeding the Singapore news-monitoring pipeline.

## Why

- Validation: "LLM Wiki proves capture-everything is worth it — *'all this knowledge came out of these meetings.'*" Prototype demonstrably surfaces decisions, lessons, and concept density that previously evaporated into Notion or Slack.
- Marketing fit: Andrew's signal-to-content workflow needs the same primitives — durable narrative pages, decision archives, source provenance — but with marketing-specific entity types (campaigns, audience signals, brand themes).
- Architecture re-use: the same `CLAUDE.md` schema discipline that works for AIO knowledge can be parameterised per domain. Different folder taxonomy and entity types, same maintenance pattern.

## Scope of the extension

A marketing-domain LLM Wiki sibling to this one. Owned by Michael; consumed by Andrew. Likely structure:

- Domain entities: campaigns, audience segments, brand themes, narrative pillars (instead of vendors / concepts / projects).
- Sources: clipped articles, market signals (incl. Singapore news monitoring output), competitor moves, customer transcripts.
- Outputs: daily / weekly briefs for Andrew; signal-rubric tracking; conversation starters for Bonaventure round-tables.

## Implications

- The Karpathy pattern is now multi-instance at Janus. The `CLAUDE.md`-driven discipline is what makes the pattern portable — schema is the parameter.
- Standup skill markdown-to-wiki integration is **deferred** (per same standup) so the AIO wiki matures further before the integration surface is locked.
- The Obsidian-clipper scraper integration for marketing data is queued (longer horizon).
