---
type: pulse
title: GBrain — Garry Tan's open-source markdown-first agent memory layer surfaces (146K-page production deployment)
slug: 2026-05-22-gbrain-yc-tan-memory-layer
created: 2026-05-23
updated: 2026-05-23
departments: [ai-office, engineering]
confidence: high
sources: [2026-05-22-marktechpost-gbrain-tutorial]
related: [gbrain, agent-memory, agent-memory-2026-q2, janus-prime-radiant-build, claude-code, 2026-05-21-code-with-claude-london, 2026-05-13-magma-multi-graph-agentic-memory, 2026-05-12-mnemon-llm-supervised-memory, openclaw]
---

# GBrain — Garry Tan's open-source markdown-first agent memory layer surfaces (146K-page production deployment)

MarkTechPost published a hands-on tutorial for **GBrain** on 2026-05-22 — open-source, MIT-licensed, built and maintained by **Garry Tan** (President and CEO of Y Combinator). Surfaced to the AIO inbox 2026-05-23. Source: [[2026-05-22-marktechpost-gbrain-tutorial]]. Vendor entry: [[gbrain]].

## What it is in one sentence

A markdown-first, Postgres-backed, MCP-native knowledge layer that ingests notes / meetings / emails / tweets and auto-wires a typed knowledge graph from wikilinks with zero LLM calls. Tan runs his personal deployment (which drives his OpenClaw + Hermes agents) at **146,646 pages, 24,585 people, 5,339 companies, 66 cron jobs** as of v0.38.2.0. Hybrid retrieval: vector (HNSW on pgvector) + BM25 + Reciprocal Rank Fusion + ZeroEntropy reranker. Reports +31.4 pts P@5 lift from the graph layer on the internal BrainBench benchmark.

## Why it matters

**This is the closest external system to the [[janus-prime-radiant-build|Janus Prime Radiant]] pattern surfaced to date.** The convergence list is striking:

- Markdown files as source of truth — yes
- `[[wikilinks]]` (slug form; full path for resolution) — yes
- Multi-graph encoding (typed edges from wikilinks) — yes, via regex inference cascade `FOUNDED → INVESTED → ADVISES → WORKS_AT → MENTIONS`
- "Compiled truth + timeline" per page (current best-understanding on top, append-only evidence trail below) — yes; mirrors Prime Radiant's vault-level pattern (`log.md`, `decisions/`, `pulse/`)
- MCP-native (74 tools, one-command setup) — yes
- "Thin harness, fat skills" design philosophy — yes (same direction Anthropic [[agent-skills]] articulates)

The implementations diverge in two ways:
- **Retrieval substrate.** Prime Radiant relies on filesystem grep + LLM-reading-files. GBrain layers PGLite + pgvector + BM25 + RRF on top of the markdown vault.
- **Engine.** Prime Radiant is a git-backed file vault (per the [[prime-radiant-storage-substrate|substrate brief]]). GBrain ships an embedded Postgres database alongside the file vault.

## Three reads for the AIO

1. **Validation that the markdown-first / multi-graph / append-only pattern is the consensus shape** of the next-generation agent memory layer, not a Janus idiosyncrasy. Prior surfacings on this thread:
   - [[2026-05-12-mnemon-llm-supervised-memory|Mnemon]] — four-graph store; LLM-supervised architecture.
   - [[2026-05-13-magma-multi-graph-agentic-memory|MAGMA]] — independent experimental validation of the same four-graph carve-up (semantic / temporal / causal / entity).
   - [[2026-05-21-code-with-claude-london|Claude Code "dreaming"]] — agent-memory landing inside Claude Code natively, via task-note consolidation passes.
   - **GBrain (this surfacing)** — markdown-first + multi-graph + compiled-truth-plus-timeline + MCP-native, deployed at YC-CEO scale.

   That's *four independent surfacings of the same architectural family within ~10 days*. Prime Radiant's design is on the consensus path.

2. **The retrieval-infrastructure layer is the next architectural decision Prime Radiant will face.** As the AIO instance scales (currently ~450 wiki pages) the filesystem-grep + LLM-reading-files model may degrade in latency / token cost. GBrain's PGLite + pgvector + RRF stack is one credible answer if and when that bottleneck arrives. Worth adding a "retrieval-layer-on-top-of-git-vault" watch-for to the [[prime-radiant-storage-substrate|substrate brief]].

3. **MCP server pattern as alternative to direct-filesystem-access for agent integration.** GBrain ships a 74-tool MCP surface (`get_page`, `put_page`, `search`, `query`, `add_link`, `get_backlinks`, etc.) — a separate integration surface for any MCP client. Prime Radiant currently relies on agents reading the vault directly. The MCP server pattern is more portable (any MCP client can integrate without needing filesystem access) but adds an indirection. Worth evaluating whether a thin MCP server wrapper makes sense when Prime Radiant scales beyond the curator-on-Obsidian use case (e.g., when each department-instance has multiple agent consumers).

## Janus posture

**Monitored, not adopted as of 2026-05-23.** Vendor entity created at [[gbrain]] with monitoring rationale. Stage path if adoption is considered: Stage 1 triage in AIR (per [[ai-tool-evaluation-framework]]); likely categorisation as AI Office Infrastructure tier per [[tool-tiers]]. The Stage 2 gates worth pre-checking are G2.2 (SSO — none yet; it's a personal-CLI tool) and G2.3 (vendor viability — Tan is the maintainer; depends on whether GBrain stays a personal project or becomes YC-supported OSS).

## Watch for

- Whether YC adopts GBrain officially as part of the OpenClaw / YC AI Stack release surface (vs Tan-personal-project).
- LongMemEval benchmark scores from the sibling `gbrain-evals` repo.
- Adoption signal from other YC portfolio companies.
- Whether `gbrain serve --http` becomes the documented self-hosted multi-tenant Prime-Radiant-equivalent path.
- Comparison data points against Mnemon, MAGMA, Claude Code "dreaming" as the multi-vendor markdown-first-agent-memory family matures.
