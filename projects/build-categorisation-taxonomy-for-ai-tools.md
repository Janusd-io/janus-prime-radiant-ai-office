---
type: project
title: Build categorisation taxonomy for AI tools
slug: build-categorisation-taxonomy-for-ai-tools
created: 2026-05-06
updated: 2026-05-20
departments: [ai-office, it-ops]
status: active
owner: michael-bruck
sources: [2026-05-06-ai-tool-taxonomy-scope-policy]
related: [2026-05-06-ai-tool-taxonomy-scope-policy, ai-registry, ai-tool-evaluation, ai-tool-evaluation-framework, stack-composition-framework, ai-registry-v2, linear]
audience: department
---

# Build categorisation taxonomy for AI tools

The parent execution work behind the [[2026-05-06-ai-tool-taxonomy-scope-policy|2026-05-06 scope-policy decision]] — building the categorisation taxonomy that lets the [[ai-registry|AI Tools Registry]] produce consistent related-tools comparisons and lets [[ai-tool-evaluation|/ai-tool-evaluation]] apply the right Gate 1 criteria per tool class.

## Scope

Two layered classifications:

1. **In-scope / out-of-scope** (resolved 2026-05-06). Non-AI SaaS tools — Monday.com, Notion, Deel, Xero, Airwallex — are NOT AI tools and should be either pruned from AIR or marked with a "general SaaS" classifier. Decision-due 13 May 2026; outcome to be communicated to `/ai-registry` skill maintainers.
2. **Tool / Infrastructure / Workload trichotomy** (in progress). The classification that determines which Gate 1 criteria apply per AIR entry. Codified in [[ai-tool-evaluation-framework]] but not yet uniformly applied across the existing registry — a backfill pass is part of this project.

## Status

**Active.** The scope-policy sub-decision is resolved; the trichotomy backfill across existing AIR entries is ongoing. Linear parent item `2891609456` advances the full taxonomy proposal after scope settles.

## Connection to the Stack Composition Framework

The [[stack-composition-framework]] (surfaced 2026-05-19 in the [[agentic-lean-marketing-stack]] brief) is upstream of this taxonomy work — its three lenses (composability, agent operability, reversibility) sit *before* the Tool/Infrastructure/Workload classification as a pre-G1 filter. If both proposals ratify, the evaluation flow becomes: stack composition pre-filter → tool/infra/workload classification → Gate 1–4.

## Watch for

- Resolution of the scope-policy sub-decision (prune vs. classify) and downstream `/ai-registry` skill update.
- Trichotomy backfill across existing AIR entries — completion criteria and owner.
- Whether the [[stack-composition-framework]] is formally ratified and integrated alongside this taxonomy.

_Stub promoted from a recurring lint finding on 2026-05-20. To enrich as taxonomy work progresses._
