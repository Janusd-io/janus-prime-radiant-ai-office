---
type: concept
title: Context Engineering
slug: context-engineering
created: 2026-05-06
updated: 2026-06-08
departments: [ai-office]
confidence: high
sources: [better-models-wont-save-your-agent, openai-agents-sdk-session-memory, jehad-vault-context-engineering, recursive-language-models, annunziata-context-model-compute-semiont]
related: [retrieval-augmented-generation, agentic-ai, agent-memory, agent-harness, 2026-05-13-recursive-language-models, 2026-05-13-claude-os-concept-surfaced, 2026-06-07-context-model-compute-semiont, knowledge-compilation]
---

# Context Engineering

The discipline of *shaping data into knowledge the model can use*, rather than asking the agent to reassemble it from raw data at query time. Term articulated in Pinecone's introduction of Nexus (May 2026), though the underlying practice — preparing retrieval indices, structuring metadata, materialising views — predates the term.

## Why it's emerging now

Per [[better-models-wont-save-your-agent]]: "Most agent failures are data failures, not model failures." Frontier models can already do the reasoning; what breaks is everything before the reasoning step. The gap defining agent infrastructure in 2026 is the work of operationalising context pipelines per business domain (sales, legal, finance, support, R&D, ops) — and hand-building one context layer per domain doesn't scale past the first one or two.

## Three modes of the problem

The term is used at *three distinct scales / modes*. Conflating them is a source of confusion:

1. **Compilation-stage / pre-query context engineering** — preparing the underlying data pipeline so the agent has good knowledge to draw from before any conversation starts. This is the Pinecone Nexus / Google Knowledge Catalog framing, and the broader [[post-rag-agent-data-stack|post-RAG data stack]] direction. *Who does the work:* data engineering, ahead of time.
2. **Conversation-level / in-session context management** — shaping what fits in the model's active context window *during* a multi-turn run. Trimming old turns, summarising history, deciding what tool results to keep verbatim. Per [[openai-agents-sdk-session-memory|OpenAI's Cookbook]] (May 2026): two named techniques — **trimming** (drop older turns, keep last-N verbatim) and **summarisation** (compress older turns into structured synthetic messages). OpenAI's Agents SDK exposes a `Session` primitive that codifies the slot where this logic lives. *Who does the work:* the harness, deterministically, during the run.
3. **Inference-time programmatic context engineering** *(new May 2026)* — the LLM itself writes code that inspects, decomposes, and recursively queries snippets of a long prompt at inference time. Surfaced by [[recursive-language-models|RLM]] (MIT CSAIL, arxiv 2512). The prompt becomes a variable in a REPL environment; the model uses code to navigate it. Empirically outperforms compaction by ~26% and CodeAct-with-sub-calls by ~130% on GPT-5 across long-context benchmarks at comparable cost. *Who does the work:* the model, dynamically, while answering. See [[2026-05-13-recursive-language-models]] for the surfacing pulse.

The three modes feed each other: bad compilation-stage context forces in-session management to compensate; good in-session management buys the ability to stretch what the compilation layer doesn't cover; inference-time programmatic context engineering removes a class of failures that neither of the other two can handle (dense access across the whole prompt without lossy summarisation).

**Adjacent: the Claude OS direction.** [[2026-05-13-claude-os-concept-surfaced|Jehad's Claude OS research direction]] (raised at this morning's standup) is the same intuition arriving from a different angle — Claude interacts with a *structured environment* via APIs rather than reading files directly. RLM does it in-prompt with a REPL; Claude OS would do it across the entire vault via purpose-built MCPs. Same underlying move: shift the context-shaping work from "everything as text in the prompt" to "model writes code over a structured environment."

## Adjacent / overlapping concepts

- [[retrieval-augmented-generation]] — predecessor; treats context shaping as a runtime concern.
- [[agent-memory]] — the persistent counterpart to in-session context management; what survives across sessions.
- [[agent-harness]] — the orchestration layer that *implements* context engineering at runtime (the Session abstraction is a harness primitive).
- Knowledge compilation / compilation-stage knowledge — moves the shaping work to a pre-query stage. (Promote to its own concept page once a second source surfaces.)
- Semantic metadata curation — the analogous shift on the data-catalog side. See [[2026-04-22-google-agentic-data-cloud]] for Google's "Knowledge Catalog" treatment.

## Update — 2026-06-08

Annunziata (IBM Research / The AI Alliance) published a LinkedIn post on 2026-06-07 proposing **"Context-Model-Compute"** as the correct mental model for AI infrastructure — context is the differentiation layer (models commoditise, compute is fuel). Directly validates this concept's framing and signals it is now entering mainstream infrastructure discourse.

Annunziata also introduced **Semiont** (GitHub: `The-AI-Alliance/semiont`) — an open-source project aiming to unify context-management into common principles and architectural practices. Framed as a potential "kernel for knowledge" or "Kubernetes-for-context." Immature/early-stage; technical details not yet available. See [[2026-06-07-context-model-compute-semiont]] pulse entry; Semiont entity escalated to [[ingest-2026-06-08-semiont-entity-page]].

## Open questions

- Does context engineering settle into a per-vendor stack (Pinecone Nexus, Google Knowledge Catalog) or a portable open-source layer?
- Will the trimming-vs-summarisation framing become standard vocabulary across vendor SDKs, or stay OpenAI-specific?
- Does inference-time programmatic context engineering (RLM-style) require model post-training, or do off-the-shelf frontier models do it well enough zero-shot? RLM's GPT-5 zero-shot results say "well enough already" but RLM-Qwen3-8B's gains suggest training helps.
- How does this map onto Janus's own AI tool evaluation — what should we evaluate context engines against?
- Does Semiont / The AI Alliance's "Context-Model-Compute" framing produce a concrete open standard, or remain a conceptual framework?
