---
type: pulse
title: "The RAG Obituary — Bustamante argues agentic search + context-window expansion kill traditional RAG"
slug: 2026-06-02-rag-obituary-bustamante-post-retrieval-age
created: 2026-06-02
updated: 2026-06-02
departments: [ai-office, engineering]
confidence: medium
sources: [2025-10-01-bustamante-rag-obituary]
related: [retrieval-augmented-generation, post-rag-agent-data-stack, agentic-ai, context-engineering, claude-code, organisational-digital-twin]
---

# The RAG Obituary — Bustamante argues agentic search + context-window expansion kill traditional RAG

Nicolas Bustamante (founder of Fintool; previously Doctrine, *"the largest European legal search engine"*) published *"The RAG Obituary: Killed by Agents, Buried by Context Windows"* on 2025-10-01 ([[2025-10-01-bustamante-rag-obituary]]) — a practitioner-grade post-mortem on the RAG paradigm from someone who *"spent three years building, optimizing, and scaling LLMs with RAG systems."* Surfaced via the inbox on 2026-06-02.

## The core argument

RAG was *"a clever workaround for a context-poor era"* — the architectural response to GPT-3.5's 4,096-token / GPT-4's 8,192-token windows colliding with 51,000-token SEC 10-K filings. *"It's like reading a financial report through a keyhole."*

Two structural changes have invalidated the workaround:

1. **Context windows exploded.** Claude Sonnet 4 at 200K tokens, Gemini 2.5 at 1M, Grok 4-fast at 2M. *"At 2M tokens, you can fit an entire year of SEC filings for most companies."* Sam Altman has signalled billion-token horizons.
2. **Agents replaced retrieval with navigation.** Claude Code's filesystem-tool architecture (Grep / Glob / Task Agents) demonstrated that *"with sufficient context and intelligent navigation, you don't need RAG at all."* Grep — invented 1973 — outperforms vector embeddings for code search because the agent can investigate, follow cross-references, and load whole files rather than juggle 500-token chunks.

The structural failure modes Bustamante details for traditional RAG (cascading failures, embedding/keyword/reranker pipeline complexity, chunking destroying cross-references, semantic-search failing on numbers and exact financial terms, $0 ripgrep vs $$$ Elasticsearch infrastructure burden) are the kind of accumulated practitioner pain that pre-Q3-2025 RAG-stack vendors don't talk about publicly.

## Why this matters to the AI Office

Three reads, all reinforcing existing AIO stances:

1. **Direct validation of the AIO stance against vector stores.** The wiki's [[retrieval-augmented-generation|RAG concept page]] already documents the "every standalone vector database is losing adoption share" trend per VentureBeat Q1 2026, and [[post-rag-agent-data-stack]] tracks the successor patterns. Bustamante's piece is the cleanest practitioner-narrative version of the same story. The AIO's Prime Radiant architecture has never depended on a vector store — markdown + grep + agentic navigation is the same pattern Bustamante endorses, applied to institutional knowledge rather than financial filings.

2. **The grep-as-search insight maps directly onto the wiki's design.** Bustamante: *"By the way, Grep was invented in 1973. It's so... primitive. And that's the genius of it."* The wiki uses exactly this pattern — `grep -l "departments:.*ai-office"` is the wiki's frontmatter-slicing tool per CLAUDE.md §5.2. The Bustamante piece supplies external corroboration that this is the correct architectural choice for a knowledge substrate, not a frugal compromise.

3. **The "cross-reference following" pattern is the wiki's `[[wikilinks]]` discipline applied to documents.** Bustamante describes Claude Code's strength as *"following references like a human analyst would. No chunks. No embeddings. No reranking. Just intelligent navigation."* This is precisely the navigation pattern the wiki's wikilink graph supports — by encoding entity / semantic / temporal / causal edges in frontmatter (CLAUDE.md §4 four-graph framing), the wiki is queryable through navigation rather than retrieval. The architectural rhyme is strong.

## Where the piece overreaches

- Bustamante writes from a context-rich position (financial filings, where context windows can now hold a year of 10-Ks for one company). For *cross-corpus* search — finding patterns across thousands of companies / decades of filings — he concedes hybrid search remains useful *"as a tool for agents."* The AIO equivalent: queries across thousands of meeting transcripts or hundreds of vendor pages may still benefit from a coarse filtering step before agent navigation. The piece doesn't kill the "filter then navigate" pattern; it kills the "embed-and-rerank-only" pattern.
- The piece predates [[recursive-self-improving-loop]] / Block / YC framings by 5-7 months. Its argument is more retrieval-architectural than organisational. The current 2026-Q2 consensus is broader: not just *"RAG is dying"* but *"the whole hierarchy-of-information-routing is being replaced by agentic loops."* Bustamante is one slice of that.

## Watch for

- Whether vector-database vendors (Pinecone, Weaviate, Qdrant) reposition explicitly as *"agent tools, not retrieval backbones."* Pinecone Nexus is already pivoting per [[pinecone]]; the others will likely follow.
- Whether Fintool ships a public benchmark of its own (legal / financial document analysis) that compares agentic navigation to traditional RAG with numbers. Bustamante's piece references *"a [benchmark](https://rlancemartin.github.io/2025/04/03/vibe-code/)"* on code but doesn't supply one for financial documents. A Fintool benchmark would be the load-bearing empirical anchor for the post-retrieval thesis in non-code domains.
- Whether the AIO needs to publish its own *"why the wiki doesn't use a vector store"* explainer. The case is now fully external; AIO could either link Bustamante directly or write a Janus version tying his thesis to Prime Radiant's architecture.
