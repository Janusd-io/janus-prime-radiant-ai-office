---
type: question
title: Create an entity page for HGTFT (Janus's customer-facing physical-infrastructure twin)?
slug: ingest-2026-05-21-1015-create-hgtft-entity-page
created: 2026-05-21
updated: 2026-05-21
departments: [ai-office, engineering, office-of-ceo]
status: active
owner: michael-bruck
sources: [2026-04-coordination-leverage-model-v0.3, 2026-04-coordination-leverage-model-v0.1]
related: [coordination-leverage-model, organisational-digital-twin, digital-twin, ai-native-janus-positioning, ai-native-enterprise-restructuring]
---

# Create an HGTFT entity page?

## Context

The [[coordination-leverage-model]] v0.3 (ingested 2026-05-21) references **HGTFT** four times as Janus's customer-facing product — *"a structured, continuously updated digital twin of a building"* — and uses it as the analogical and architectural foundation for the [[organisational-digital-twin]]:

> *"This is not an analogy. It is the same engineering discipline applied at a different scale, and Janus Digital is uniquely positioned to build it because the organisational thinking — ontologies, knowledge graphs, structured data, continuous model updates — is already the company's core competency."*

The framework's most distinctive positioning argument depends on this product being the engineering precedent. But HGTFT itself doesn't have a wiki entity page yet. Grep across `entities/`, `concepts/`, `projects/`, `briefs/` finds 0 prior mentions before this ingest.

## Proposed action

Create one or both of:

1. **`entities/vendors/hgtft.md`** — if HGTFT is best classified as a Janus product / capability that vendors might integrate with (rare).
2. **`projects/hgtft.md`** or **`entities/internal/janus-products/hgtft.md`** — more likely shape: HGTFT is *Janus's own* product, not a vendor or external entity. It's the engineering surface that AIO frequently cites as architectural precedent. Best home is probably a `projects/`-shaped or a new `entities/products/` namespace.

This is borderline outside the AIO Prime Radiant's scope (Engineering owns HGTFT, not AIO), but the cross-reference frequency from AIO-side framing artefacts (this Coordination Leverage Model brief, the AI-Native positioning brief, the organisational-digital-twin concept) makes the missing page a real gap.

## Why this is being escalated

Per CLAUDE.md §5.1, creating a new entity page is **high-stakes** (name-collision risk, duplication risk; also a vocabulary question — do Janus products warrant their own folder?). The escalation asks Michael to:

1. Confirm HGTFT is the right slug (vs. an internal Janus marketing name).
2. Confirm the right namespace (`projects/`, new `entities/products/`, or wait for an Engineering Prime Radiant instance to own it).
3. Confirm whether Janus's product portfolio is in AIO Prime Radiant scope at all, or whether HGTFT references stay as plain unlinked text until the Engineering Prime Radiant instance is stood up.

## Alternative — defer

Leave HGTFT references as plain text (not wikilinks) in the AIO wiki until Engineering's Prime Radiant instance ships. Pro: respects the federation pattern (each domain owns its entities). Con: the AI-Native positioning argument loses its strongest in-wiki anchor; the *Janus is uniquely positioned to build this because* claim doesn't resolve to a citable internal artefact.

**Recommendation:** create as `projects/hgtft.md` (a project hub describing the product as the AIO sees it), with explicit framing that the canonical Janus product page will eventually live in the Engineering Prime Radiant instance. The AIO project hub captures the AIO-side framing — *"HGTFT is the engineering precedent for the organisational digital twin"* — while leaving the canonical product description to Engineering when their instance exists.

## Status

Awaiting Michael's confirmation. No action taken yet.
