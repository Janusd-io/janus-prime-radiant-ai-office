---
type: concept
title: Retrieval-Augmented Generation (RAG)
slug: retrieval-augmented-generation
created: 2026-05-06
updated: 2026-06-02
departments: [ai-office]
confidence: high
sources: [better-models-wont-save-your-agent, rag-era-ending-for-agentic-ai, retrieval-after-rag-turbopuffer, 2025-10-01-bustamante-rag-obituary]
related: [agentic-ai, context-engineering, post-rag-agent-data-stack, organisational-digital-twin, claude-code]
---

# Retrieval-Augmented Generation (RAG)

A pattern where an LLM augments its prompt by retrieving relevant chunks from an external knowledge store (typically a vector database) before generating a response. RAG was the dominant approach for grounding LLM outputs in enterprise data through 2024-2025.

## Architecture (canonical)

1. Documents → embedding model → vectors stored in a vector database.
2. User query → embedding → similarity search → top-k chunks retrieved.
3. Retrieved chunks + query → LLM prompt → generated response.

## Limitations surfacing in 2026 (per Pinecone, VentureBeat)

- **Agent-loop overhead.** Agents searching, retrieving, evaluating, looping consume most of the token/latency budget *before* the reasoning step. See [[better-models-wont-save-your-agent]].
- **Reassembly tax.** Raw retrieved chunks force the agent to reassemble context at query time rather than reading already-shaped knowledge.
- **Adoption shift.** Per VentureBeat's Q1 2026 Pulse, every standalone vector database is losing adoption share; hybrid retrieval intent has tripled to 33.3%.

## Successor patterns being floated

- **Compilation-stage knowledge layers** — pre-compute task-specific knowledge artifacts before agent query time. See [[2026-05-04-pinecone-nexus-launch]] and [[knowledge-compilation]] (when created).
- **Post-RAG hybrid retrieval** — Simon Hørup Eskildsen (Turbopuffer) argues for hybrid search (semantic + keyword + metadata) + agent-driven query refinement rather than semantic-only RAG. The operational layer between raw retrieval and vendor knowledge engines.
- **Agent-native data stacks** — rebuild the data plane around autonomous agents acting around the clock. See [[2026-04-22-google-agentic-data-cloud]].

## Status (as of 2026-05-06)

RAG is not dead but the consensus is shifting. The interesting frontier is what replaces or augments it for agentic workloads. See [[context-engineering]] for the broader discipline that this discussion sits within.

## Post-retrieval read — Bustamante "RAG Obituary" (added 2026-06-02)

Nicolas Bustamante (Fintool / formerly Doctrine) published *"The RAG Obituary: Killed by Agents, Buried by Context Windows"* on 2025-10-01 ([[2025-10-01-bustamante-rag-obituary]]) — a practitioner-grade post-mortem from someone who spent three years building and scaling RAG systems. Full read at [[2026-06-02-rag-obituary-bustamante-post-retrieval-age]].

The headline argument: RAG was a *"clever workaround for a context-poor era"*. Two structural changes invalidate it:

1. **Context windows expanded** — Claude Sonnet 4 at 200K, Gemini 2.5 at 1M, Grok 4-fast at 2M. At 2M tokens an entire year of SEC filings for one company fits in context.
2. **Agentic search replaces retrieval with navigation** — Claude Code's Grep + Glob + Task Agents pattern outperforms vector-embedding pipelines on code by orders of magnitude. Grep (1973) beats Elasticsearch (heavy infrastructure) for in-context exploration; the agent loads whole files, follows cross-references, and reasons about structure.

Bustamante's structural failure-mode list for traditional RAG — cascading-failure pipeline (chunking → embedding → BM25 → fusion → reranking), tables-split-mid-row, semantic-search-fails-on-numbers, $0 ripgrep vs $$$ Elasticsearch — is the kind of accumulated practitioner pain that pre-Q3-2025 RAG-stack vendors don't talk about publicly.

**Caveat:** Bustamante concedes hybrid search remains useful *"as a tool for agents"* for cross-corpus filtering before navigation. The piece doesn't kill "filter then navigate" — it kills "embed-and-rerank-only." The wiki's current architecture (markdown + grep + wikilink navigation + agent-driven exploration) is the discipline Bustamante endorses; the wiki has never relied on a vector store.

**Implication for Prime Radiant.** The wiki's design is now externally validated as the correct architectural posture for a context-rich agent substrate. The grep + frontmatter-slicing + wikilink-navigation pattern is the same one Bustamante endorses for SEC filings. See [[organisational-digital-twin]] for the broader framing — the twin is queried via navigation, not retrieval; that's a design feature, not a limitation.
