---
type: concept
title: Agent Harness
slug: agent-harness
created: 2026-05-06
updated: 2026-05-13
departments: [ai-office, engineering]
confidence: medium
sources: [your-harness-your-memory-hwchase17, claude-code-limits-harness-pawelhuryn, building-agents-claude-agent-sdk, anatomy-of-claude-folder, harness-design-long-running-apps, 100x-business-with-ai, jehad-vault-agent-harness]
related: [agent-memory, agentic-ai, model-context-protocol, ralph-loop-pattern]
---

# Agent Harness

The orchestration layer surrounding an LLM that turns it into a useful agent: the prompt scaffolding, tool dispatch, memory management, retry/loop logic, and connector wiring. Term increasingly used (per Harrison Chase et al.) to distinguish the *system around the model* from the model itself.

## Why the term is emerging

Harnesses were implicit when agents were simple. As 2026 architectures get denser, the harness becomes the locus of:
- **Memory implementation** — see [[agent-memory]]; per Chase, "your harness is your memory."
- **Tool/MCP wiring** — see [[model-context-protocol]]. Per Anthropic's [[building-agents-claude-agent-sdk|Claude Agent SDK guide]], tools should be primary high-context actions; MCPs handle OAuth/auth seamlessly.
- **Feedback loops and verification** — See [[ralph-loop-pattern|Ralph Loop]]: iterating agent output against concrete feedback (tests, lints, type-checks) is the harness's job, not the model's. Per [[100x-business-with-ai|100x business article]], architecture (solo vs. parallel vs. collaborative agents) matters more than model selection.
- **Context management** — [[harness-design-long-running-apps|long-running app patterns]] use compaction, subagent isolation, and staged information flow to prevent context exhaustion.
- **Performance optimisation** — prompt caching, batching, latency budgets. See [[claude-code-prompt-caching-lessons]] for [[claude|Claude]] Code's specific learnings here.
- **Failure handling** — most agent failures aren't model failures. See [[claude-code-limits-harness-pawelhuryn]] making the case that hitting [[claude|Claude]] Code's limits is usually a harness problem, not a model problem.

## Implication for tool evaluation

Two agents on the same model can perform very differently if their harnesses differ. When Janus evaluates tools, distinguishing model capability from harness quality is non-trivial — and probably the single biggest source of "this works in demos but not for us" outcomes.
