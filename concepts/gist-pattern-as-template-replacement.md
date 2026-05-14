---
type: concept
title: Gist pattern — adaptable starting points instead of rigid templates
slug: gist-pattern-as-template-replacement
created: 2026-05-08
updated: 2026-05-13
departments: [marketing, ai-office]
sources: [karpathy-llm-wiki, 2026-05-08-andrew-marketing-prime-radiant, jehad-vault-gist-pattern-as-template-replacement]
related: [llm-wiki, andrej-karpathy, prime-radiant-three-layer-architecture, marketing-prime-radiant, janus-prime-radiant-build]
---

# Gist pattern — adaptable starting points instead of rigid templates

## What it is

A **gist** is a compressed representation of a concept — enough information that an LLM (or a competent human) can expand it into a working implementation, while leaving the implementation details flexible to local context. The term comes from [[andrej-karpathy]]'s "LLM Wiki" GitHub gist — the originating source for [[llm-wiki]] — which Karpathy described as:

> *"I'm not going to give you the recipe. I'll give you enough information that if you give it to your LLM like Claude or OpenAI, it will then figure it out and build it for you."*

The gist is the inverse of the traditional template. Where a template encodes a fixed structure that local users fill in, a gist encodes the *intent* and *essence* of a deliverable, leaving structure flexible.

## Why it matters now

The 2026-05-08 brainstorm with [[andrew-soane]] surfaced gists as a candidate replacement for marketing templates — campaign templates, brief templates, positioning frameworks. Andrew's framing in the conversation: *"You give them a gist because the gist will actually have — this is what you have to do, this is what we're trying to accomplish. But then they have some flexibility to adapt."*

Michael's case study in the same conversation: the **Intel Inside campaign** lineage. Dentsu Japan came up with "Intel Init" as a local Japan adaptation; the head of corporate marketing in the US looked at it and said *this is brilliant, I'll adapt it and make it global*. That global adaptation is what became "Intel Inside." The Japanese local adaptation was a gist of the brand-strategy intent, not a rigid template — which is what allowed it to be reabsorbed and globalised.

## The pattern

A gist contains:

1. **What you have to do** — the core action or deliverable (build a Prime Radiant; run a regional brand campaign; evaluate a new AI tool).
2. **What we're trying to accomplish** — the strategic intent (institutional memory; brand differentiation in a new market; tool fit for our policy gate).
3. **Examples or precedent** — what's been done before, in adjacent contexts.
4. **Flexibility envelope** — what's intentionally unspecified so local context can fill it in.

A gist is *not*:
- A template with blanks to fill (too rigid).
- A free-form brief (too unspecified).
- A finished artefact (the local adaptation hasn't happened yet).

## Application across the Prime Radiant rollout

Each department Prime Radiant instance is itself a gist of the AIO Prime Radiant. CLAUDE.md is shared across instances; the entity vocabulary adapts per domain (vendors / outlets / candidates / etc.); the brief shape is shared; the topic taxonomy is local. This is the gist pattern at the schema level.

The [[janus-prime-radiant-build|program-level project]] is rolling out gists, not clones. Marketing's Prime Radiant won't be a copy of AIO's — it'll be the AIO instance treated as a gist, expanded under Marketing's local conditions (Andrew as curator, marketing infrastructure layer, marketing-specific topic taxonomy and Outputs).

## Application beyond Prime Radiants

The gist pattern is a candidate replacement for many traditional "template" surfaces in Janus:

- **Campaign templates** → campaign gists per topic / vertical / country, expanded with local market context.
- **Brief templates** → brief shape rules in CLAUDE.md §6 are themselves a gist (intent: "land the strategic implication"; flexibility: how the supporting evidence is structured).
- **Onboarding documentation** → role-specific onboarding gists, expanded by AI based on the new hire's background and current Janus state.
- **Project hub templates** → no fixed template; a project hub gist is "scope, status, narrative; link out, don't duplicate" (per CLAUDE.md §2 filing rules).

Wherever Janus currently uses a rigid template, ask: would this be more useful as a gist that an LLM expands, with the flexibility envelope made explicit?

## Cross-references

The gist pattern is a sibling concept to [[prime-radiant-three-layer-architecture]] — both emerged from Karpathy-pattern thinking, both are about structuring intent for LLM-assisted expansion. The [[llm-wiki]] concept page describes the methodology; this page describes the implementation pattern that makes the methodology portable.

## Provenance

Originating gist: [[karpathy-llm-wiki]] (Karpathy's GitHub gist). Janus adoption signal: 2026-05-08 brainstorm with [[andrew-soane]] surfaced gists as a candidate for marketing template replacement, with the Intel Inside / Dentsu Japan precedent cited as a real-world example of the pattern working.
