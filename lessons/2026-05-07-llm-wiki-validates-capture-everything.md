---
type: lesson
title: LLM Wiki validates the "capture everything" thesis — knowledge surfaces only when written down
slug: 2026-05-07-llm-wiki-validates-capture-everything
created: 2026-05-07
updated: 2026-05-13
departments: [ai-office]
status: resolved
owner: michael-bruck
sources: [aio-2026-05-07, jehad-vault-2026-05-07-llm-wiki-validates-capture-everything]
related: [llm-wiki, janus-prime-radiant-build, 2026-05-05-notion-degrades-as-ai-searchable-kb, 2026-05-07-llm-wiki-extends-to-marketing-domain]
---

# LLM Wiki validates "capture everything"

**Surfaced:** 2026-05-07
**Source:** [[aio-2026-05-07]]

## What we observed

In the 7 May standup, on demoing the LLM Wiki prototype, Michael said: **"all this knowledge came out of these meetings."**

The wiki — built by ingesting the same Notion standups, Mivory backfill, Web Clipper articles, and Linear AIR entries that everyone already had access to — surfaced decisions, lessons, vendor relationships, and project narratives that were not visible in any of the source systems individually.

## Why it matters

This is the foundational validation for the [[janus-prime-radiant-build]] project and, by extension, for the Karpathy LLM Wiki pattern itself. The thesis was: a synthesis layer over already-curated sources will compound value beyond what any single source produces. The 7 May demo showed the thesis working in practice.

It also closes the loop on [[2026-05-05-notion-degrades-as-ai-searchable-kb]] — Notion-as-KB degrades at scale because there's nothing extracting and indexing the latent structure inside the journal entries. The LLM Wiki *is* the extraction layer.

## Implications

- The pattern is now sufficiently validated to extend to a sibling marketing-domain wiki ([[2026-05-07-llm-wiki-extends-to-marketing-domain]]).
- The "capture everything" discipline pays off only when there's a maintenance layer that does the synthesis. Capture without synthesis is just a bigger pile.
- The lesson generalises beyond Janus: any organisation sitting on ingested-but-unsurfaced knowledge in Notion / Slack / Linear / Monday could likely run the same pattern and surface the same compounding effect.

## Self-referential note

This page is itself an example of the validation it's documenting. The 7 May standup mentioned the validation moment; the wiki captured it in a source file; this lesson page synthesises the meaning. Three pages reference each other ([[aio-2026-05-07]] → this lesson → [[janus-prime-radiant-build]] → back), and all three live in the system whose value they're documenting.

## Related

- [[2026-05-05-notion-degrades-as-ai-searchable-kb]] — the originating lesson that drove the project.
- [[2026-05-05-kb-direction-markdown-progressive-exposure-not-rag]] — the architectural choice.
- [[janus-prime-radiant-build]] — the project this lesson validates.
- [[2026-05-07-llm-wiki-extends-to-marketing-domain]] — the next-step extension this lesson enables.
