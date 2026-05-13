---
type: concept
title: Agentic AI
slug: agentic-ai
created: 2026-05-06
updated: 2026-05-07
departments: [ai-office]
confidence: high
sources: [better-models-wont-save-your-agent, rag-era-ending-for-agentic-ai, google-agentic-data-cloud, agent-native-architectures, anthropic-building-effective-agents, a2a-mcp-five-integration-patterns, 100x-business-with-ai, are-ai-agents-slowing-us-down, get-good-at-agents, token-anxiety, agentic-entity-resolution]
related: [retrieval-augmented-generation, context-engineering, agent-memory, agent-harness, agent-skills, model-context-protocol, agent-to-agent-protocol, ralph-loop-pattern]
---

# Agentic AI

Umbrella term for AI systems that act with autonomy on behalf of users — issuing tool calls, navigating multi-step workflows, and operating around the clock rather than answering one-off human queries.

The term is broad and rapidly being claimed by vendors. In this wiki, prefer using more specific subterms (agent loop, tool use, MCP, autonomous workflow) when accuracy matters; reserve "agentic AI" for high-level framing.

## What's distinctive about the agentic context

- **Autonomous, not interactive.** Agents act around the clock without a human waiting at the prompt; latency and cost compound differently.
- **Tool-call heavy.** Each step is more likely to involve external systems than producing prose, which changes what data infrastructure must support.
- **Loops, not single shots.** An agent task is many decisions over time; whatever fails compounds rather than getting one shot.

## Infrastructure implications surfacing in 2026

- Existing data stacks (built for human-scale queries) are creaking. Vendors racing to rebuild — see [[2026-04-22-google-agentic-data-cloud]].
- RAG-as-runtime-retrieval is hitting limits — see [[retrieval-augmented-generation]] limitations section. Successor framings include [[context-engineering]] and pre-compiled knowledge layers.
- Tool ecosystems (MCP, Claude Code, Gemini CLI, VS Code agentic features) are where developer attention is concentrating.

## Recommended primers (from this wiki's sources)

- **[[anthropic-building-effective-agents]]** — Anthropic's house view: simple, composable patterns beat heavy frameworks.
- **[[agent-native-architectures]]** — `every.to` guide; technical framing for "agents as first-class citizens" in application design.
- **[[a2a-mcp-five-integration-patterns]]** — practical patterns for combining vertical (MCP) and horizontal (A2A) protocols.

## Status

Active and rapidly evolving as of 2026-05-06. Watch for: standardisation of agent-data interfaces, MCP adoption curves, vendor consolidation around context engines, and convergence of harness and memory implementations.
