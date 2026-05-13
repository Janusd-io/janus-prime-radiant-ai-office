---
type: source
slug: automations-2891609456
title: Build categorisation taxonomy for AI tools
created: 2026-05-06
updated: 2026-05-06
monday_id: 2891609456
monday_url: https://janusd-company.monday.com/boards/5095012818/pulses/2891609456
board: 5095012818
status: In Definition
priority: Medium
source_type: monday-item
---

## Monday item summary

**Title:** Build categorisation taxonomy for AI tools (comparables search)  
**Owners:** Michael Bruck, Jehad Altoutou  
**Status:** In Definition  
**Source:** AI/IT Mtg 6 May 2026, Bonaventure/Michael/Jehad/Andrew 4 May 2026  

## Context

The Hercules / Lovable / Replit / Claude Design / Google Stitch comparison surfaced a structural gap: no good auto-categoriser for AI tools exists, breaking the AI Registry's related-tools check and the standup methodology's comparables search. This taxonomy will enable the /ai-registry skill to surface "tools similar to X" reliably.

## Definition of done

A taxonomy proposal covering:
- Top-level categories (e.g. dev tooling, CRM, data, voice, etc.)
- Sub-categories
- Attribute schema (capability, integration surface, deployment model, data classification)
- Mapping onto existing AIR Linear team structure
- Validation: re-categorise 10 existing AIR entries and run a comparables query

## Key updates (most recent first)

**6 May 2026 (AI ↔ IT Meeting):** Strong agreement that Monday.com, Notion, Deel, Xero, Airwallex are NOT AI tools and should not live in AI Registry. Euclid: "I'm so glad that Michael define[s] it's not [an] AI tool." The taxonomy parent already covers comparables-search; this meeting added scope question as parallel decision: keep with "general SaaS" classifier vs prune entirely. Sub-item added for scope-policy decision (2896109872).

**Next steps (by 13 May):**
- Decide AI-registry scope policy: prune Monday/Notion/Deel/Xero/Airwallex or add "general SaaS" classifier
- Communicate decision to /ai-registry skill maintainers

**4 May 2026 (Bonaventure/Michael/Jehad/Andrew meeting):** Why: structural gap in taxonomy powering comparables search. Powers /ai-registry related-tools check + standup-methodology comparables search.

## Related wiki

- [[ai-registry-v2]] (parent project)
- [[linear]] (AIR team mapping)
