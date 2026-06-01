---
type: vendor
title: OpenAI
slug: openai
created: 2026-05-14
updated: 2026-05-14
departments: [ai-office, engineering]
status: monitored
confidence: high
sources: [openai-agents-sdk-session-memory]
related: [claude, anthropic, agent-memory, context-engineering, ingest-2026-05-12-1545-openai, recursive-language-models]
migrated_from: entities/vendors/openai.md
---
# OpenAI

Frontier model and agent-platform vendor. Janus's posture: **monitor, not adopt as a primary surface.** [[claude]] (Anthropic) is the chosen substrate for AIO automation; OpenAI is tracked for landscape awareness and for cases where its specific products become operationally relevant.

## Notable products / surfaces

- **GPT-5** — frontier model; baseline for comparison in agent-memory / long-context evaluations (see [[recursive-language-models]] where it's the headline benchmark).
- **Codex** — coding assistant; flagged as a [[claude]] Code fallback per [[2026-04-22-evaluate-openai-codex-as-claude-fallback]] but not adopted.
- **Agents SDK** (May 2026) — exposes a `Session` primitive that codifies short-term context management via trimming and summarisation. See [[context-engineering]] and [[openai-agents-sdk-session-memory]].

## Posture

OpenAI's short-term context management story is more developed than [[anthropic|Anthropic]]'s; Anthropic's long-term file-based memory story is more developed than OpenAI's. Janus picks Anthropic as the primary platform because **long-term portable memory is the load-bearing property for the [[janus-prime-radiant-build]] direction**. See [[agent-memory-2026-q2]] brief for the full vendor comparison.

## Open

[[ingest-2026-05-12-1545-openai]] is the surfacing escalation — pending Michael's triage on whether any OpenAI-specific signals warrant deeper evaluation than current "monitor" posture.
