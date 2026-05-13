---
type: concept
title: Gist pattern — adaptable starting points instead of rigid templates
slug: gist-pattern-as-template-replacement
created: 2026-05-08
updated: 2026-05-13
departments: [marketing, ai-office]
confidence: high
sources: [jehad-vault-import-2026-05-13]
related: [llm-wiki, prime-radiant-three-layer-architecture, janus-prime-radiant-build]
captured_by: jehad-altoutou
---

> _Jehad's personal-vault articulation of this topic, imported 2026-05-13. The canonical wiki page is at `decisions/concepts/gist-pattern-as-template-replacement.md` — this file is preserved as a source for divergent framing / additional context._

# Gist pattern — adaptable starting points instead of rigid templates

## What it is

A **gist** is a compressed representation of a concept — enough information that an LLM (or a competent human) can expand it into a working implementation, while leaving the implementation details flexible to local context. The term comes from Andrej Karpathy's "LLM Wiki" GitHub gist — the originating source for [[llm-wiki]] — where he framed the artefact as: enough information that if given to an LLM, it can figure out and build the implementation.

The gist is the inverse of the traditional template. Where a template encodes a fixed structure that local users fill in, a gist encodes the *intent* and *essence* of a deliverable, leaving structure flexible.

## Why it matters now

The 2026-05-08 brainstorm with Andrew Soane surfaced gists as a candidate replacement for marketing templates — campaign templates, brief templates, positioning frameworks. Andrew's framing: a gist tells you what to do and what we're trying to accomplish, but leaves flexibility to adapt.

Michael's case study: the **Intel Inside campaign** lineage. Dentsu Japan came up with "Intel Init" as a local Japan adaptation; the head of US corporate marketing saw it and adapted it to make it global, which became "Intel Inside." The Japanese local adaptation was a gist of brand-strategy intent, not a rigid template — which is what allowed it to be reabsorbed and globalised.

## The pattern

A gist contains:

1. **What you have to do** — the core action or deliverable.
2. **What we're trying to accomplish** — the strategic intent.
3. **Examples or precedent** — what's been done before, in adjacent contexts.
4. **Flexibility envelope** — what's intentionally unspecified so local context can fill it in.

A gist is *not* a template with blanks to fill (too rigid), a free-form brief (too unspecified), or a finished artefact (the local adaptation hasn't happened yet).

## Application across the Prime Radiant rollout

Each department Prime Radiant instance is itself a gist of the AIO Prime Radiant. CLAUDE.md is shared; entity vocabulary adapts per domain; brief shape is shared; topic taxonomy is local. The [[janus-prime-radiant-build]] program is rolling out gists, not clones.

## Application beyond Prime Radiants

Candidate replacement for rigid templates in Janus:

- **Campaign templates** → campaign gists per topic / vertical / country.
- **Brief templates** → brief shape rules in CLAUDE.md §6 are themselves a gist.
- **Onboarding documentation** → role-specific onboarding gists, expanded by AI.
- **Project hub templates** → no fixed template; "scope, status, narrative; link out, don't duplicate."

Wherever Janus uses a rigid template, ask: would this be more useful as a gist that an LLM expands, with the flexibility envelope made explicit?
