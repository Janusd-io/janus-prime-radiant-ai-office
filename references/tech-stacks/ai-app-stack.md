---
type: stack
tags: [stack, ai]
---

# AI App Stack

Used by [[ai-engineer|/ai-engineer]], [[agent-build|/agent-build]], [[rag-build|/rag-build]].

## Core
- **AI SDK** (`ai`) — Text/chat/tool calling/streaming
- **AI Gateway** — Multi-provider routing (Vercel)
- **Workflow DevKit** — Durable workflows with pause/resume
- **ToolLoopAgent** — Agent loop primitive from AI SDK

## Models
- Default: Anthropic Claude Opus 4.6 / Sonnet 4.6
- Fetch current IDs via AI Gateway: `curl -s https://ai-gateway.vercel.sh/v1/models`

## Storage (optional)
- **Neon Postgres + pgvector** — Vector embeddings
- **Upstash Redis** — Semantic cache
- **Vercel Blob** — Asset storage

## Related Skills
- [[ai-engineer|/ai-engineer]]
- [[agent-build|/agent-build]]
- [[rag-build|/rag-build]]
- [[llm-ops|/llm-ops]]
- [[prompt-engineer|/prompt-engineer]]
