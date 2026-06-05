---
type: concept
title: Knowledge Compilation
slug: knowledge-compilation
created: 2026-05-14
updated: 2026-05-14
departments: [ai-office, engineering]
confidence: high
sources: [better-models-wont-save-your-agent, recursive-language-models, anthropic-self-service-data-analytics]
related: [context-engineering, retrieval-augmented-generation, post-rag-agent-data-stack, llm-wiki, janus-prime-radiant-build, pinecone, google-cloud]
---

# Knowledge Compilation

The architectural pattern of **pre-compiling knowledge artefacts** so an agent has good knowledge to draw from before any conversation starts, rather than retrieving and shaping context at query time (the RAG pattern). The shift moves the data work to a pre-query stage, into persistent task-specific artefacts that the agent reads or queries directly.

## Why it matters

The 2026 industry observation: "most agent failures are data failures, not model failures." Frontier models can already do the reasoning; what breaks is everything *before* the reasoning step. Hand-building one runtime retrieval pipeline per business domain doesn't scale past the first one or two — compiling knowledge ahead of time amortises the work across queries and decouples the agent from the data plumbing. See [[post-rag-agent-data-stack]] for the brief.

## Vendor instantiations

- **Pinecone Nexus** (2026-05-04) — explicit "knowledge compiler" framing; KnowQL is the declarative compilation query language. See [[pinecone]].
- **Google Knowledge Catalog** (2026-04-22) — auto-curated semantic metadata as the compilation target. See [[google-cloud]].
- **Janus Prime Radiant** (this wiki + sibling instances) — file-based, schema-driven, LLM-maintained. The compilation target is markdown + YAML frontmatter; the maintenance engine is Claude. See [[janus-prime-radiant-build]].
- **Anthropic's self-service analytics stack** (2026-06-04) — in-production validation, not a vendor product. Anthropic's data team compiles canonical governed datasets + a human-owned semantic layer + LLM-retrieval-optimised reference docs ("skills"), reaching ~95% analytics accuracy. The load-bearing finding: a negative ablation showed raw grep access to thousands of prior queries moved accuracy <1 point — *structure*, not retrieval *access*, was the bottleneck. The cleanest practitioner evidence that compilation beats runtime retrieval. See [[2026-06-04-anthropic-self-service-analytics-stack]] and [[anthropic-self-service-data-analytics]].

## Cross-references

- [[context-engineering]] — the broader discipline; knowledge compilation is the compilation-stage scale within it.
- [[retrieval-augmented-generation]] — the predecessor pattern this displaces.
- [[recursive-language-models]] — orthogonal: handles inference-time long-context dense access. Complementary to compilation, not a substitute.

## Open

Whether knowledge compilation settles into a per-vendor stack (Pinecone, Google) or a portable open-source layer (the Janus Prime Radiant bet on the markdown + LLM-maintenance pattern). Resolves by Q4 2026 at the earliest.
