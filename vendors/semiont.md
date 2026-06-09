---
type: vendor
title: Semiont
slug: semiont
created: 2026-06-08
updated: 2026-06-08
departments: [ai-office]
confidence: medium
status: active
sources: [annunziata-context-model-compute-semiont, semiont-github-readme, semiont-protocol-readme]
related: [context-engineering, agent-memory, prime-radiant, retrieval-augmented-generation, knowledge-compilation, 2026-06-07-context-model-compute-semiont]
---

# Semiont

Open-source semantic knowledge platform from **The AI Alliance** (IBM-backed nonprofit consortium). GitHub: `The-AI-Alliance/semiont`. As of 2026-06-08: **Alpha** — API not yet stable, breaking changes between 0.x releases expected.

**One-line:** a structured annotation + knowledge graph platform where humans and AI agents work as peers on shared document corpora.

## What it is

Semiont ingests raw documents and builds a knowledge graph as a *byproduct of annotation* — no upfront schema design, no batch ETL pipeline. Humans and AI agents both annotate the same corpus through the same API (entity detection, passage linking, reference binding). The result is an interconnected semantic network anchored to source passages.

Self-hosted (Docker/Podman/Apple Container). Inference: Anthropic (cloud) or Ollama (local) — mix providers per worker to balance cost, capability, and privacy. Storage: event-sourced backend. Frontend: browser UI on port 3000, backend KB server on port 4000.

W3C Web Annotation compliance for the annotation layer.

## The eight flows

All operations — human and AI — go through eight composable verbs:

| Flow | What it does |
|---|---|
| **Frame** | Define/evolve the KB's schema vocabulary (entity types, relation types) |
| **Yield** | Introduce new resources — upload docs, load pages, generate content |
| **Mark** | Add structured metadata — highlights, assessments, tags, entity references |
| **Match** | Multi-source retrieval + composite scoring + LLM re-ranking |
| **Bind** | Resolve ambiguous references to specific resources (entity disambiguation) |
| **Gather** | Assemble related context around a focal annotation for generation/analysis |
| **Browse** | Navigate resources, panels, and views |
| **Beckon** | Direct participant focus to specific annotations (coordination signal) |

The eight flows are also the eight verb namespaces on the TypeScript SDK (`client.frame.X(...)`, `client.yield.X(...)`, etc.) — the protocol vocabulary and the API surface are 1:1.

## Three programmable surfaces

- **SDK** (`@semiont/sdk`) — type-safe TypeScript; RxJS-native but `PromiseLike<T>` so `await` works without learning RxJS
- **CLI** — pipe the full annotation pipeline from the terminal (`semiont mark`, `semiont gather`, `semiont match`, `semiont bind`)
- **Agent Skills** — ready-made skill definitions for agentic coding assistants including Claude Code

## Core tenets

1. **Peer collaboration** — humans and AI agents as architectural equals; every operation flows through the same API, event bus, and event-sourced storage
2. **Document-grounded knowledge** — all knowledge anchored to source passages; the knowledge graph is a projection of grounded relationships, not a replacement for raw material
3. **Coordination is first-class** — real-time collaboration signals (`beckon:hover`, `mark:shape-changed`, `bind:initiate`, `browse:click`) fan out to all connected participants via the shared event bus; multi-participant coordination is woven into the protocol, not bolted on

## Demo knowledge bases

Ships demo KBs for: literature (Gutenberg), research papers (arXiv), legal, U.S. case law, clinical evidence, newsroom/investigative journalism, household records. The value is the *skills* (ingest → mark → canonicalize → wire-edges → compose-aggregates), not the data — skills are corpus-generic.

## Relationship to Prime Radiant / AIO

See [[prime-radiant]] for the comparative analysis. The key differences: Semiont is annotation-grounded and database-backed (higher fidelity, higher overhead); Prime Radiant is synthesis-first and file-based (zero overhead, LLM-maintained). The eight-flows vocabulary and "calibrate the Human-AI Mix" framing are concepts worth absorbing regardless of whether Semiont itself is adopted. Not recommended for evaluation at current maturity (Alpha).

## Status

Not in AIR. Not under evaluation. Watch-list only — re-evaluate when post-Alpha (stable API, post-1.0 release).
