---
type: concept
title: Model Context Protocol (MCP)
slug: model-context-protocol
created: 2026-05-06
updated: 2026-05-06
departments: [ai-office, engineering]
confidence: high
sources: [a2a-mcp-five-integration-patterns, google-agentic-data-cloud]
related: [agent-to-agent-protocol, agentic-ai, agent-skills]
---

# Model Context Protocol (MCP)

Open standard for how LLMs access external context: tools, data sources, and prompts. Originally introduced by [[anthropic|Anthropic]]; now broadly adopted across the industry, including [[google-cloud|Google]]'s Agentic Data Cloud (which exposes BigQuery and pipelines via MCP servers in [[vs-code|VS Code]], [[claude|Claude]] Code, and Gemini CLI per [[2026-04-22-google-agentic-data-cloud]]).

## How it fits

MCP is the *vertical* protocol — connecting one LLM to many external tools and data sources. It pairs with [[agent-to-agent-protocol]] (A2A) which is the *horizontal* protocol connecting agents to other agents.

Five integration patterns for MCP + A2A together are documented in [[a2a-mcp-five-integration-patterns]]:
1. Pattern 1, 2, 3, 4, 5 — to be expanded on later read; placeholder until depth is needed.

## Relevance to Janus

- **Tool exposure surface.** Internal services exposed as MCP servers become callable by any MCP-aware agent (Claude Desktop/Code, Cursor, Cowork, etc.) without bespoke integrations.
- **Vendor proliferation.** Increasingly the question for new SaaS tools is "do they ship an MCP server?" — which makes MCP support a Gate 1 viability criterion in the [[ai-tool-evaluation]] framework.
- **Cowork plugins.** Plugins in Cowork (Janus's adopted Claude desktop interface) are bundles of MCP servers, skills, and tools. The plugin format is the local artifact; MCP is the wire protocol underneath.
