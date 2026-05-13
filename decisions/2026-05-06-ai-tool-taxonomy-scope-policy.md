---
type: decision
slug: 2026-05-06-ai-tool-taxonomy-scope-policy
title: AI-registry scope policy — exclude non-AI SaaS tools (Monday, Notion, Deel, Xero, Airwallex)
created: 2026-05-06
updated: 2026-05-07
departments: [ai-office]
status: resolved
owner: michael-bruck
decided_by: michael-bruck
sources: [automations-2891609456]
related: [ai-registry-v2, linear, ai-tool-evaluation]
---

## Decision

As of 6 May 2026 (AI ↔ IT meeting), strong agreement that **Monday.com, Notion, Deel, Xero, Airwallex are NOT AI tools** and should not live in the AI Registry.

**Scope-policy sub-decision (due 13 May, item 2896109872):** Prune these tools entirely from AIR, or add a "general SaaS" classifier to keep them but mark them as out-of-scope. Once decided, communicate to /ai-registry skill maintainers.

## Context

The Hercules / Lovable / Replit / Claude Design / Google Stitch comparison revealed a structural gap: without a categorisation taxonomy, the AI Registry's related-tools check produces inconsistent results, and the standup methodology's comparables search can't run. Scope clarity is part of fixing that.

## Quoted reasoning

**Euclid (IT, 6 May):** "I'm so glad that Michael define[s] it's not [an] AI tool. What's wrong with you guys?"

## Next steps (by 13 May)

1. Decide: prune entirely vs. add "general SaaS" classifier
2. Communicate decision to /ai-registry skill maintainers
3. Related parent item 2891609456 to advance full taxonomy proposal after scope settles

## Related work

- [[build-categorisation-taxonomy-for-ai-tools]] (parent item, in-progress)
- [[ai-registry-v2]] (downstream user)
- [[linear]] (AIR team)

## Confidence

High — agreement reached across Michael, Jehad, and Euclid.
