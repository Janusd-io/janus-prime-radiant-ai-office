---
type: concept
title: Agent-to-Agent Protocol (A2A)
slug: agent-to-agent-protocol
created: 2026-05-06
updated: 2026-05-13
departments: [ai-office, engineering]
confidence: medium
sources: [jehad-vault-import-2026-05-13]
related: [model-context-protocol]
captured_by: jehad-altoutou
---

> _Jehad's personal-vault articulation of this topic, imported 2026-05-13. The canonical wiki page is at `decisions/concepts/agent-to-agent-protocol.md` — this file is preserved as a source for divergent framing / additional context._

# Agent-to-Agent Protocol (A2A)

Open protocol for agents to discover, communicate with, and delegate work to other agents — across teams, vendors, and platforms. Pushed primarily by Google (positioned alongside MCP in Cloud Next 2026 messaging).

A2A is the *horizontal* protocol — agent-to-agent — paired with [[model-context-protocol]] which is the *vertical* (LLM-to-tools) protocol. Core premise: no organisation will build every agent it needs from scratch; the real value comes from discovering agents built by different teams in different organisations.

## Status as of 2026-05-06

Adoption is early. Standards-track status is unclear. Worth tracking, not yet worth building against. Janus's evaluation framework should treat A2A as **Watch (not Adopt)** until at least one major Anthropic / Microsoft / OpenAI announcement signals industry alignment.

## Watch for

- Cross-vendor compatibility: do Anthropic / OpenAI ship A2A clients?
- Authentication and trust models: agent-to-agent across organisations needs robust identity primitives.
- Convergence vs. competing standards (e.g., LangChain's various agent-orchestration patterns).
