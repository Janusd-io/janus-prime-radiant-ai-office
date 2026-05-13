---
type: concept
title: Agent Memory
slug: agent-memory
created: 2026-05-06
updated: 2026-05-12
departments: [ai-office]
confidence: high
sources: [agent-memory-engineering-nicbstme, your-harness-your-memory-hwchase17, mempalace-milla-jovovich, claude-managed-agents-memory, claude-managed-agents-memory-rlancemartin, himanshustwts-claude-code-memory-architecture, openai-agents-sdk-session-memory, mnemon-github-readme]
related: [context-engineering, agentic-ai, agent-harness, retrieval-augmented-generation]
---

# Agent Memory

The mechanisms by which AI agents persist and recall information across sessions, tasks, and users. As of 2026, this is one of the most actively contested areas of agent infrastructure — the dominant theme across the May 2026 article batch.

## Why it matters

Without memory, every agent session starts cold: re-loading context, re-deriving user preferences, re-discovering tools and constraints. With memory, agents accumulate competence over time. The interesting design questions:

- **What gets stored?** Verbatim transcripts, summaries, structured facts, relational graphs, or some combination.
- **Where does it live?** In the model's context window (volatile), in a vector store (retrieval-on-demand), as files (per [[anthropic|Anthropic]]'s [[claude|Claude]] Managed Agents approach), or in a structured graph.
- **Who owns it?** Embedded in the platform vs. portable across providers.

## Observable long-term patterns (as of 2026-05-12)

The original three patterns observed in early Q2 2026:

1. **Files-as-memory** — Anthropic's Claude Managed Agents stores memories as files; users can export, manage via API, retain control. See [[2026-04-08-claude-managed-agents-launch]] and [[claude-managed-agents-memory]].
2. **Harness-as-memory** — per Harrison Chase ([[your-harness-your-memory-hwchase17]]): agent harnesses (the orchestration layer around the model) are increasingly tied to specific memory implementations. The harness *is* the memory.
3. **Memory palace / structured indices** — MemPalace ([[mempalace-milla-jovovich]]) is an offline, palace-based system; alternative to model-heavy approaches. Niche but interesting as a portability/lock-in counterweight.

A finer-grained decomposition surfaced by the Mnemon project ([[mnemon-github-readme]], 2026-05-12) cuts the field along *LLM role* rather than *storage substrate* and is worth holding alongside the above:

| Pattern | LLM role | Representative |
|---|---|---|
| **LLM-Embedded** | Executor inside the memory pipeline | Mem0, Letta |
| **File Injection** | None — file read at session start | Claude Code Memory |
| **MCP Server** | Tool provider via [[model-context-protocol|MCP]] | claude-mem |
| **LLM-Supervised** | External supervisor of a standalone binary | Mnemon |

The two taxonomies are not redundant: the storage axis (where memory lives) and the LLM-role axis (who decides what to store) are orthogonal. Mnemon, for example, is "Files-as-memory" on the storage axis *and* "LLM-Supervised" on the role axis. Anthropic's Managed Agents are "Files-as-memory" on storage *and* effectively "LLM-Embedded" (the platform decides). The role axis is the better predictor of vendor lock-in; the storage axis is the better predictor of portability mechanics. See [[2026-05-12-mnemon-llm-supervised-memory]] for the surfacing pulse entry.

## Short-term vs long-term

The above patterns are about *long-term* memory — what survives across sessions. There's a separate short-term axis: what fits in the active context window during a single multi-turn run. Per [[openai-agents-sdk-session-memory|OpenAI's Agents SDK Cookbook]] (May 2026), short-term memory is managed via a `Session` primitive with two canonical techniques: **trimming** (keep last-N user turns verbatim, drop the rest — deterministic, low latency, weak long-range recall) and **summarisation** (compress older turns into a synthetic summary message — strong long-range recall, vulnerable to "context poisoning" if a bad fact enters the summary). See [[context-engineering]] for the broader discipline; the Session abstraction is what makes the in-session technique a first-class harness concern rather than ad-hoc prompt wrangling.

This makes [[openai|OpenAI]]'s memory story explicit: short-term context management is well-developed (the Cookbook lays out concrete patterns and code); long-term/portable memory is comparatively under-articulated. The opposite of [[anthropic|Anthropic]]'s position, where the Managed Agents file-based memory is the public surface and short-term in-session context management is comparatively implicit.

## Open question for Janus

How portable is agent memory? If Janus standardises on Claude Managed Agents memory, can those memories migrate to a different provider later? This is a load-bearing question for any tool evaluation involving memory features. See [[ai-tool-evaluation]] framework — memory portability should likely be a Stage 1 viability criterion going forward.

## Adjacent concepts

[[retrieval-augmented-generation]] — the predecessor pattern; memory was previously delegated to retrieval over an external store, now increasingly first-class in agent platforms.
[[context-engineering]] — the broader discipline of shaping what agents see; memory is one input.
[[agent-harness]] — the orchestration layer around the model; tightly coupled to memory in current architectures.
