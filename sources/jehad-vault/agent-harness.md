---
type: concept
title: Agent Harness
slug: agent-harness
created: 2026-05-06
updated: 2026-05-13
departments: [ai-office, engineering]
confidence: medium
sources: [jehad-vault-import-2026-05-13]
related: [agent-memory, agentic-ai, model-context-protocol, llm-harness]
captured_by: jehad-altoutou
---

> _Jehad's personal-vault articulation of this topic, imported 2026-05-13. The canonical wiki page is at `concepts/agent-harness.md` — this file is preserved as a source for divergent framing / additional context._

# Agent Harness

The orchestration layer surrounding an LLM that turns it into a useful agent: the prompt scaffolding, tool dispatch, memory management, retry/loop logic, and connector wiring. Term increasingly used (per Harrison Chase et al.) to distinguish the *system around the model* from the model itself.

## Why the term is emerging

Harnesses were implicit when agents were simple. As 2026 architectures get denser, the harness becomes the locus of:

- **Memory implementation** — see [[agent-memory]]; per Chase, "your harness is your memory."
- **Tool/MCP wiring** — see [[model-context-protocol]]. Per Anthropic's Claude Agent SDK guide, tools should be primary high-context actions; MCPs handle OAuth/auth seamlessly.
- **Feedback loops and verification** — Iterating agent output against concrete feedback (tests, lints, type-checks) is the harness's job, not the model's. Architecture (solo vs. parallel vs. collaborative agents) matters more than model selection.
- **Context management** — Long-running app patterns use compaction, subagent isolation, and staged information flow to prevent context exhaustion.
- **Performance optimisation** — prompt caching, batching, latency budgets.
- **Failure handling** — most agent failures aren't model failures; they're harness problems.

## Implication for tool evaluation

Two agents on the same model can perform very differently if their harnesses differ. When Janus evaluates tools, distinguishing model capability from harness quality is non-trivial — and probably the single biggest source of "this works in demos but not for us" outcomes.

## Naming note

The live vault has a stub at `concepts/llm-harness.md`. "Agent harness" and "LLM harness" describe overlapping ideas — the orchestration around the model. See escalation `questions/ingest-2026-05-13-1500-agent-harness-vs-llm-harness-merge.md` for the merge / canonical-slug decision.
