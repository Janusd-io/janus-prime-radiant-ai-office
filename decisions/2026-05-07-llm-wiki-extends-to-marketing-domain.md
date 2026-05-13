---
type: decision
title: LLM Wiki prototype validated; pattern extends to marketing-domain knowledge tool
slug: 2026-05-07-llm-wiki-extends-to-marketing-domain
created: 2026-05-07
updated: 2026-05-07
departments: [ai-office, marketing]
status: resolved
owner: michael
sources: [aio-2026-05-07]
related: [llm-wiki, janus-prime-radiant-build, andrew-soane, singapore-news-monitoring, 2026-05-05-kb-direction-markdown-progressive-exposure-not-rag]
---

# LLM Wiki extends to marketing-domain knowledge tool

**Decision date:** 2026-05-07
**Decided by:** Michael Bruck, Jehad Altoutou
**Source:** [[aio-2026-05-07]]

## What

The [[janus-prime-radiant-build|Janus Prime Radiant prototype]] was demo'd in the 7 May standup — directory-structure + `CLAUDE.md` + Obsidian, pre-processing Notion + clipped X posts + transcripts into concepts / themes / decisions / lessons / briefs / articles. **Verdict: prototype validated.** The pattern will be extended to a **marketing-domain knowledge tool** that [[andrew-soane|Andrew]] needs (signals → rubric → daily briefs), feeding the [[singapore-news-monitoring]] pipeline.

## Why

- Validation: per [[aio-2026-05-07]] key findings, "LLM Wiki proves capture-everything is worth it — *'all this knowledge came out of these meetings.'*" The prototype demonstrably surfaces decisions, lessons, and concept density that previously evaporated into Notion or Slack.
- Marketing fit: Andrew's signal-to-content workflow needs the same primitives — durable narrative pages, decision archives, source provenance — but with marketing-specific entity types (campaigns, audience signals, brand themes).
- Architecture re-use: the same `CLAUDE.md` schema discipline that works for AIO knowledge can be parameterised per domain. Different folder taxonomy and entity types, same maintenance pattern.

## Scope of the extension

A marketing-domain LLM Wiki sibling to this one. Owned by Michael; consumed by Andrew. Likely structure:

- Domain entities: campaigns, audience segments, brand themes, narrative pillars (instead of vendors / concepts / projects).
- Sources: clipped articles, market signals (incl. [[singapore-news-monitoring]] output), competitor moves, customer transcripts.
- Outputs: daily / weekly briefs for Andrew; signal-rubric tracking; conversation starters for Bonaventure round-tables.

## Implications

- The Karpathy pattern is now multi-instance at Janus. The `CLAUDE.md`-driven discipline is what makes the pattern portable — schema is the parameter.
- Standup skill markdown-to-wiki integration is **deferred** (per same standup) so the AIO wiki matures further before the integration surface is locked.
- The Obsidian-clipper scraper integration for marketing data is queued (longer horizon).

## Related

- [[janus-prime-radiant-build]] — the AIO instance / first prototype.
- [[2026-05-05-kb-direction-markdown-progressive-exposure-not-rag]] — the originating direction.
- [[singapore-news-monitoring]] — first downstream consumer of the marketing wiki.
