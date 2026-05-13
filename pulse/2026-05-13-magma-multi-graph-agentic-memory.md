---
type: pulse
title: MAGMA — second multi-graph agent-memory architecture in a week, same four-graph shape as Mnemon
slug: 2026-05-13-magma-multi-graph-agentic-memory
created: 2026-05-13
updated: 2026-05-13
departments: [ai-office, engineering]
confidence: high
sources: [magma-multi-graph-agentic-memory]
related: [agent-memory, agent-memory-2026-q2, 2026-05-12-mnemon-llm-supervised-memory, janus-prime-radiant-build, transformers-are-graph-neural-networks-2026-05-13]
---

# MAGMA — second multi-graph agent-memory architecture in a week

[[magma-multi-graph-agentic-memory|MAGMA]] (UT Dallas / U. Florida; arxiv 2601.03236) proposes a multi-graph agentic memory architecture that represents each memory item across four orthogonal graphs — **semantic, temporal, causal, entity** — and reframes retrieval as policy-guided traversal over those views. Outperforms state-of-the-art agentic memory systems on LoCoMo and LongMemEval, with substantial efficiency gains at ultra-long contexts. Open source: `github.com/FredJiang0324/MAGMA`.

## Why this matters now

The four-graph decomposition is **identical** to what Mnemon proposed a day earlier (see [[2026-05-12-mnemon-llm-supervised-memory]]): temporal, entity, causal, semantic. Two independent research surfacings of the same four-dimensional carve-up of "agent memory" within 48 hours is a strong convergence signal — the multi-graph pattern is no longer a single research group's idea; it's becoming the *consensus shape* of structured agent memory. The Mnemon pulse from yesterday was hedged on the basis of being a single README-only data point; MAGMA's experimental validation on standard benchmarks removes that hedge.

For [[agent-memory|the agent-memory taxonomy]], this is now a distinct row alongside files-as-memory, harness-as-memory, and memory-palace patterns — the **multi-graph relational** pattern, where the storage substrate explicitly carries semantic / temporal / causal / entity edges and retrieval is graph traversal rather than vector similarity.

## Janus implication

The Janus Prime Radiant frontmatter (`departments`, `related`, `sources`, plus the implicit temporal axis via `created`/`updated`) is already a primitive multi-graph: entity edges via `departments`, semantic edges via `related`, causal edges via decision/lesson links, temporal axis via dates. We're operating the same shape MAGMA and Mnemon are validating in the agent-runtime layer — at the institutional-KB layer instead. This is reassuring for [[janus-prime-radiant-build|the program direction]] and worth folding into the next CLAUDE.md revision as explicit framing (currently the four-axis decomposition is implicit).

## Open question

Do MAGMA's reported gains hold up under adversarial / noisy memory inputs? The "Limitations" section acknowledges that graph quality depends on the underlying LLM's reasoning fidelity during consolidation — extraction errors can propagate. Same caveat applies to Prime Radiant's ingest-and-link discipline. Worth tracking whether either MAGMA or Mnemon publishes a noise-robustness study.

## Watch for

- Whether the four-graph (semantic/temporal/causal/entity) decomposition becomes named vocabulary across the wider agent-memory literature.
- Independent reproductions of MAGMA's LoCoMo / LongMemEval gains.
- Whether the [[claude]] Managed Agents file format converges toward exposing graph structure rather than only file content.
