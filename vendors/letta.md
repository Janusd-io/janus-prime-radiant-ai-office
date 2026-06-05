---
type: vendor
title: Letta
slug: letta
created: 2026-06-05
updated: 2026-06-05
departments: [ai-office, engineering]
status: active
confidence: medium
sources: [letta-context-constitution, letta-continual-learning-token-space, letta-context-constitution-github-readme, letta-memory-not-plugin-wooders, your-harness-your-memory-hwchase17]
related: [agent-memory, agent-harness, context-engineering, memgpt]
---

# Letta

**Type:** Agent framework / memory-first harness  
**Website:** letta.com  
**Mission:** "Machines that learn" — AI agents with continual, experience-driven memory

## What they do

Letta (formerly MemGPT) builds **memory-first agent harnesses** — the premise being that context management is not a plugin but the foundational layer of any agent framework. The company's flagship product is **Letta Code**, a memory-first agent harness that gives agents real ownership of their context.

Letta Code's distinguishing architecture:
- **Git-versioned memory filesystem** — agent context (system prompt + external memory) lives in a git-backed repo, versioned and inspectable
- **Self-modifying system prompt** — agents have tools to rewrite their own system prompt as they learn, treating context updates as a form of online learning
- **Sleep-time compute** — background memory subagents that consolidate, compress, and reorganise context between active sessions (analogous to sleep-phase memory consolidation in humans)
- **Multi-conversation memory** — memories persist and carry across sessions and model upgrades

## Core thesis: token-space learning

Letta frames "continual learning" not as weight updates but as **learning in token space**: agents should actively manage their context — creating, updating, compressing, and organising token-space representations of memory and identity. The argument (from the [[letta-continual-learning-token-space|Continual Learning in Token Space]] blog post):

- Weight-based continual learning has proven impractical in production (catastrophic forgetting, data-curation burden, deployment complexity)
- In-context learning is model-agnostic, interpretable, and rollback-trivial
- But append-only context is insufficient — agents need to actively *refine* and *consolidate* learned memories, not just accumulate logs

This positions Letta as the *harness that implements the learning* rather than a tool layered on top of an existing harness.

## Context Constitution

Letta's **Context Constitution** (released 2026, open-sourced CC0) is a document written directly to Letta agents describing principles for context management. Key principles:
- Context is identity, memory, and continuity — not just operational state
- Context management via progressive disclosure: compact summaries in context, full detail loaded on-demand
- System prompt learning: durable learnings should be written back to the system prompt, not just appended to conversation history
- Efficiency without identity loss: aggressive pruning is wrong if it destroys the agent's accumulated identity

The Context Constitution has been released as a living document on GitHub (`letta-ai/context-constitution`) under CC0 — Letta explicitly wants the principles to propagate widely.

## Strategic positioning

Per Sarah Wooders ([[letta-memory-not-plugin-wooders]]), the most common misframing of Letta's work is "how do I plug your memory system into my agent?" The answer: memory isn't a plugin. Context management — which IS memory — is the core job of the harness. A harness that isn't managing context is just scaffolding. MemGPT was a stateful harness *before* the word "harness" existed.

This places Letta in direct competition with Claude Code, Codex, OpenCode, and any harness that builds context-management-as-native rather than as an add-on.

## Alignment with Era of Experience framing

Letta's work sits directly at the intersection of Silver & Sutton's "Era of Experience" thesis ([[era-of-experience-silver-sutton]]): agents should learn continually from their own experience. Letta's answer is that the learning mechanism is token-space context updates; the harness is the implementation layer for that learning. The Context Constitution is effectively the operating manual for an experiential AI agent.

## Janus relevance

- As of 2026-06-05: **not evaluated**. Not in Linear AIR.
- Letta Code competes for the same developer/power-user segment as Claude Code (Anthropic). Key differentiator: Letta Code is model-agnostic + memory-first; Claude Code is Anthropic-native.
- The token-space learning framing is directly relevant to the Prime Radiant wiki system itself: the wiki is a manual/curator-driven instance of exactly the kind of long-horizon, context-updating, structured memory repository that Letta is trying to automate at the agent layer.
- Watch for: whether Letta Code becomes a viable alternative harness for AI Office agent workflows; whether the Context Constitution vocabulary converges with Anthropic's memory model in future Claude releases.

## Notes

- Sarah Wooders and Charles Packer are co-founders (both formerly RISE Lab / Berkeley)
- MemGPT (the academic paper, arxiv 2310.08560) is the research origin; Letta is the company built on that work
- Letta Code available via `npm install -g @letta-ai/letta-code`; BYOK or Codex plans
