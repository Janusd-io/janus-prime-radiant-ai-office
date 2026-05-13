---
type: concept
title: Agent-to-Agent Protocol (A2A)
slug: agent-to-agent-protocol
created: 2026-05-06
updated: 2026-05-13
departments: [ai-office, engineering]
confidence: medium
sources: [a2a-mcp-five-integration-patterns, jehad-vault-agent-to-agent-protocol]
related: [model-context-protocol, agentic-ai]
---

# Agent-to-Agent Protocol (A2A)

Open protocol for agents to discover, communicate with, and delegate work to other agents — across teams, vendors, and platforms. Pushed primarily by Google (positioned alongside MCP in Cloud Next 2026 messaging).

The core premise per [[a2a-mcp-five-integration-patterns]]: "No organization will build every agent it needs from scratch. The real value comes from discovering agents built by different teams, in different organizations." A2A is the *horizontal* protocol — agent-to-agent — paired with [[model-context-protocol]] which is the *vertical* (LLM-to-tools) protocol.

## Status as of 2026-05-06

Adoption is early. Standards-track status is unclear. Worth tracking, not yet worth building against. Janus's evaluation framework should treat A2A as Watch (not Adopt) until at least one major Anthropic / Microsoft / OpenAI announcement signals industry alignment.

## Watch for

- Cross-vendor compatibility: does Anthropic / OpenAI ship A2A clients?
- Authentication and trust models: agent-to-agent across organisations needs robust identity primitives.
- Convergence vs. competing standards (e.g., LangChain's various agent-orchestration patterns).
