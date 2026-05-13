---
type: concept
title: Context Engineering
slug: context-engineering
created: 2026-05-06
updated: 2026-05-07
departments: [ai-office]
confidence: high
sources: [better-models-wont-save-your-agent, openai-agents-sdk-session-memory]
related: [retrieval-augmented-generation, agentic-ai, agent-memory, agent-harness]
---

# Context Engineering

The discipline of *shaping data into knowledge the model can use*, rather than asking the agent to reassemble it from raw data at query time. Term articulated in Pinecone's introduction of Nexus (May 2026), though the underlying practice — preparing retrieval indices, structuring metadata, materialising views — predates the term.

## Why it's emerging now

Per [[better-models-wont-save-your-agent]]: "Most agent failures are data failures, not model failures." Frontier models can already do the reasoning; what breaks is everything before the reasoning step. The gap defining agent infrastructure in 2026 is the work of operationalising context pipelines per business domain (sales, legal, finance, support, R&D, ops) — and hand-building one context layer per domain doesn't scale past the first one or two.

## Two scales of the problem

The term is starting to be used at *two distinct scales*, and conflating them is a source of confusion:

1. **Compilation-stage / pre-query context engineering** — preparing the underlying data pipeline so the agent has good knowledge to draw from before any conversation starts. This is the Pinecone Nexus / Google Knowledge Catalog framing, and the broader [[post-rag-agent-data-stack|post-RAG data stack]] direction.
2. **Conversation-level / in-session context management** — shaping what fits in the model's active context window *during* a multi-turn run. Trimming old turns, summarising history, deciding what tool results to keep verbatim. Per [[openai-agents-sdk-session-memory|OpenAI's Cookbook]] (May 2026): two named techniques — **trimming** (drop older turns, keep last-N verbatim) and **summarisation** (compress older turns into structured synthetic messages). OpenAI's Agents SDK exposes a `Session` primitive that codifies the slot where this logic lives.

The two scales feed each other: bad compilation-stage context forces in-session context management to compensate; good in-session management buys the ability to stretch what the compilation layer doesn't cover.

## Adjacent / overlapping concepts

- [[retrieval-augmented-generation]] — predecessor; treats context shaping as a runtime concern.
- [[agent-memory]] — the persistent counterpart to in-session context management; what survives across sessions.
- [[agent-harness]] — the orchestration layer that *implements* context engineering at runtime (the Session abstraction is a harness primitive).
- Knowledge compilation / compilation-stage knowledge — moves the shaping work to a pre-query stage. (Promote to its own concept page once a second source surfaces.)
- Semantic metadata curation — the analogous shift on the data-catalog side. See [[2026-04-22-google-agentic-data-cloud]] for Google's "Knowledge Catalog" treatment.

## Open questions

- Does context engineering settle into a per-vendor stack (Pinecone Nexus, Google Knowledge Catalog) or a portable open-source layer?
- Will the trimming-vs-summarisation framing become standard vocabulary across vendor SDKs, or stay OpenAI-specific?
- How does this map onto Janus's own AI tool evaluation — what should we evaluate context engines against?
