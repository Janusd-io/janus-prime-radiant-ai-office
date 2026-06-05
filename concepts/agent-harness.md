---
type: concept
title: Agent Harness
slug: agent-harness
created: 2026-05-06
updated: 2026-06-05
departments: [ai-office, engineering]
confidence: medium
sources: [your-harness-your-memory-hwchase17, claude-code-limits-harness-pawelhuryn, building-agents-claude-agent-sdk, anatomy-of-claude-folder, harness-design-long-running-apps, 100x-business-with-ai, jehad-vault-agent-harness, letta-memory-not-plugin-wooders, letta-context-constitution]
related: [agent-memory, agentic-ai, model-context-protocol, ralph-loop-pattern, letta]
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

## Update — 2026-06-05: memory is the harness (Letta / Wooders)

Sarah Wooders (Letta co-founder, [[letta-memory-not-plugin-wooders]], 2026-03-31) sharpens the Chase thesis with a direct repudiation of the "plug memory into my agent" framing:

> Asking to plug memory into an agent harness is like asking to plug driving into a car. Managing context, and therefore memory, is a core capability and responsibility of the agent harness. If a harness isn't managing context, what is it doing?

The invisible decisions the harness makes — how AGENTS.md / CLAUDE.md is loaded, how skill metadata is shown, whether the agent can modify its own system instructions, what survives compaction, how interactions are stored and made queryable — are all *memory decisions*. RAG can be a plugin; full context management cannot.

MemGPT (now [[letta|Letta]]) was built as a stateful harness before the term "harness" existed. The Context Constitution ([[letta-context-constitution]]) is the explicit policy document for how a memory-first harness should operate.

**Practical implication:** when evaluating any agent tool, the harness context-management behaviour is the most important factor to probe — not the model, not the tool catalog, not the UI. Different harnesses answer memory questions fundamentally differently, and those answers determine lock-in, portability, and long-term performance trajectory.

## Implication for tool evaluation

Two agents on the same model can perform very differently if their harnesses differ. When Janus evaluates tools, distinguishing model capability from harness quality is non-trivial — and probably the single biggest source of "this works in demos but not for us" outcomes.
