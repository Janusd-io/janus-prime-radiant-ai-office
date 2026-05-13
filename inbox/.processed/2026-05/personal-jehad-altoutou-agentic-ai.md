---
type: concept
title: Agentic AI
slug: agentic-ai
created: 2026-05-06
updated: 2026-05-13
departments: [ai-office]
confidence: high
sources: [pr-backup-2026-05-11-1432-concept-agentic-ai]
related: [retrieval-augmented-generation, context-engineering, agent-memory, agent-harness, agent-skills, model-context-protocol]
audience: [department]
captured_by: jehad-altoutou
---

# Agentic AI

Umbrella term for AI systems that act with autonomy on behalf of users — issuing tool calls, navigating multi-step workflows, and operating around the clock rather than answering one-off human queries.

The term is broad and rapidly being claimed by vendors. In this wiki, prefer using more specific subterms (agent loop, tool use, MCP, autonomous workflow) when accuracy matters; reserve "agentic AI" for high-level framing.

## What's distinctive about the agentic context

- **Autonomous, not interactive.** Agents act around the clock without a human waiting at the prompt; latency and cost compound differently.
- **Tool-call heavy.** Each step is more likely to involve external systems than producing prose, which changes what data infrastructure must support.
- **Loops, not single shots.** An agent task is many decisions over time; whatever fails compounds rather than getting one shot.

## Infrastructure implications surfacing in 2026

- Existing data stacks (built for human-scale queries) are creaking. Vendors racing to rebuild.
- RAG-as-runtime-retrieval is hitting limits — see [[retrieval-augmented-generation]]. Successor framings include [[context-engineering]] and pre-compiled knowledge layers.
- Tool ecosystems (MCP, Claude Code, Gemini CLI, VS Code agentic features) are where developer attention is concentrating.

## Status

Active and rapidly evolving as of 2026-05-06. Watch for: standardisation of agent-data interfaces, MCP adoption curves, vendor consolidation around context engines, and convergence of harness and memory implementations.
