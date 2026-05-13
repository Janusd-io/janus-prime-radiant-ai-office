---
type: pulse
title: Anthropic launches Claude Managed Agents — composable APIs for cloud-hosted agents
slug: 2026-04-08-claude-managed-agents-launch
created: 2026-05-06
updated: 2026-05-06
departments: [ai-office, engineering]
confidence: high
sources: [claude-managed-agents-launch, claude-managed-agents-quickstart, claude-managed-agents-scaling, claude-managed-agents-memory, claude-managed-agents-memory-rlancemartin]
related: [agent-memory, agentic-ai, agent-harness]
---

# Anthropic launches Claude Managed Agents (2026-04-08)

[[anthropic|Anthropic]] launched **Claude Managed Agents** (part of the [[claude]] product family), a suite of composable APIs for building and deploying cloud-hosted agents at scale. Goal: "get to production 10x faster" by removing the harness/infra build for teams that want managed agent execution.

The launch sequence:
- **2026-04-08:** Initial announcement ([[claude-managed-agents-launch]]). Composable APIs, cloud-hosted execution.
- **2026-04-08 onward:** Quickstart docs ([[claude-managed-agents-quickstart]]) and the engineering deep-dive on architecture ([[claude-managed-agents-scaling]] — "decoupling the brain from the hands").
- **2026-04-23:** Memory feature lands in public beta ([[claude-managed-agents-memory]]). Memories stored as files; exportable, manageable via API. R Lance Martin's note ([[claude-managed-agents-memory-rlancemartin]]) emphasises file-based persistence and cross-session accessibility.

## Why this matters

Managed Agents pushes Anthropic up the stack from model provider to agent platform. The "decoupling the brain from the hands" framing in [[claude-managed-agents-scaling]] is meaningful — it's an explicit design choice about where intelligence lives vs. where execution happens. See [[agent-harness]].

Memory-as-files is a deliberate portability play vs. the alternative of opaque vendor-managed memory. Combined with [[agent-memory]] more broadly, this becomes a relevant tool-eval criterion: *can we export what the agent has learned?*

## Watch for

- Pricing model for Managed Agents and how it compares to building on the bare API.
- Whether the file-based memory format is portable to non-Anthropic agents.
- Customer adoption signals: who ships production workloads on this in Q3 2026?
- Implications for Janus's `ai-tool-evaluation` framework — Managed Agents could be a worth-evaluating tool itself, and is also a backdrop against which other agent platforms now compete.
