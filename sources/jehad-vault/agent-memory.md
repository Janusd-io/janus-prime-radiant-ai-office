---
type: concept
title: Agent Memory
slug: agent-memory
created: 2026-05-06
updated: 2026-05-13
departments: [ai-office]
confidence: high
sources: [jehad-vault-import-2026-05-13]
related: [context-engineering, agentic-ai, agent-harness, retrieval-augmented-generation, memory-engineering]
captured_by: jehad-altoutou
---

> _Jehad's personal-vault articulation of this topic, imported 2026-05-13. The canonical wiki page is at `decisions/concepts/agent-memory.md` — this file is preserved as a source for divergent framing / additional context._

# Agent Memory

The mechanisms by which AI agents persist and recall information across sessions, tasks, and users. As of 2026, this is one of the most actively contested areas of agent infrastructure.

## Why it matters

Without memory, every agent session starts cold: re-loading context, re-deriving user preferences, re-discovering tools. With memory, agents accumulate competence over time. Key design questions:

- **What gets stored?** Verbatim transcripts, summaries, structured facts, relational graphs, or some combination.
- **Where does it live?** In the model's context window (volatile), in a vector store (retrieval-on-demand), as files (per [[anthropic|Anthropic]]'s Claude Managed Agents approach), or in a structured graph.
- **Who owns it?** Embedded in the platform vs. portable across providers.

## Three observable patterns (as of 2026-05-06)

1. **Files-as-memory** — Anthropic's Claude Managed Agents stores memories as files; users can export, manage via API, retain control.
2. **Harness-as-memory** — per Harrison Chase: agent harnesses (the orchestration layer around the model) are increasingly tied to specific memory implementations. The harness *is* the memory.
3. **Memory palace / structured indices** — MemPalace is an offline, palace-based system; alternative to model-heavy approaches. Niche but interesting as a portability/lock-in counterweight.

## Short-term vs long-term

The above patterns are about *long-term* memory — what survives across sessions. There's a separate short-term axis: what fits in the active context window during a single multi-turn run. Per OpenAI's Agents SDK Cookbook (May 2026), short-term memory is managed via a `Session` primitive with two canonical techniques:

- **Trimming** — keep last-N user turns verbatim, drop the rest. Deterministic, low latency, weak long-range recall.
- **Summarisation** — compress older turns into a synthetic summary message. Strong long-range recall, vulnerable to "context poisoning" if a bad fact enters the summary.

## Open question for Janus

How portable is agent memory? If Janus standardises on Claude Managed Agents memory, can those memories migrate to a different provider later? Memory portability should be a Stage 1 viability criterion in the AI tool evaluation framework.

## Naming note

Live vault has stub `concepts/memory-engineering.md`. The two concepts overlap. See escalation `questions/ingest-2026-05-13-1500-agent-memory-vs-memory-engineering-merge.md`.
