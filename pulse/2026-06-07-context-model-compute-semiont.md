---
type: pulse
title: "Context-Model-Compute: The AI Alliance proposes a unified context layer (Semiont)"
slug: 2026-06-07-context-model-compute-semiont
created: 2026-06-08
updated: 2026-06-08
departments: [ai-office]
confidence: medium
sources: [annunziata-context-model-compute-semiont]
related: [context-engineering, agent-memory, retrieval-augmented-generation, knowledge-compilation, post-rag-agent-data-stack]
---

# Context-Model-Compute: The AI Alliance proposes a unified context layer (Semiont)

Anthony J. Annunziata (IBM Research / The AI Alliance) published a LinkedIn post on 2026-06-07 proposing "Context–Model–Compute" as the correct mental model for AI infrastructure — displacing the traditional software stack framing.

## The frame

Annunziata's argument: the AI "stack" isn't a software stack. It is:

- **Context** — scenario-specific knowledge supplied at the moment of use (prompts, RAG, knowledge graphs, MCP tools, humans-in-the-loop, etc.)
- **Model** — the generalised intelligence engine (LLMs, world models/JEPA)
- **Compute** — the underlying execution fuel

Key claim: *context is where application-level value lives*. Models are commoditising; compute is infrastructure; context is the differentiation layer. "The future of AI infrastructure will not just be about serving models faster. It will be about organizing, governing, and applying knowledge better."

## Semiont — The AI Alliance's context-unification project

Semiont (GitHub: `The-AI-Alliance/semiont`) is described as supporting "human+AI collaborative knowledge work" — positioned as a Wiki, Knowledge Base, Context Graph, Semantic Layer, or Agentic Memory. Annunziata frames it as a potential "kernel for knowledge" or "Kubernetes-and-containers ecosystem for knowledge."

No technical details in this post. The GitHub repo and Project Tapestry (for LLM training diversity) are the companion links. Both are early-stage open-source efforts from the AI Alliance (IBM-backed nonprofit consortium).

## Relevance to AIO

The Context-Model-Compute framing is a clean articulation of what the post-RAG infrastructure discussion has been circling. It maps directly to the existing [[context-engineering]] concept page (which covers compilation-stage, in-session, and inference-time modes) and to [[knowledge-compilation]] (pre-compiled knowledge beats runtime retrieval).

Semiont's framing — "wiki, knowledge base, context graph, semantic layer, agentic memory" — is interesting as an emerging project that overlaps in spirit with the [[prime-radiant]] approach. Worth tracking as it matures.

The "kernel for knowledge" metaphor Annunziata reaches for is adjacent to what Janus already has operationally — the Prime Radiant as the context layer, CLAUDE.md as the operating contract. The open question is whether Semiont becomes a tool to evaluate or a conceptual peer.

## Watch for

- Semiont GitHub repo content (no technical details yet)
- Annunziata's promised follow-up post (deeper dive into these ideas)
- Whether The AI Alliance / Project Tapestry produces anything relevant for the LLM training diversity angle
