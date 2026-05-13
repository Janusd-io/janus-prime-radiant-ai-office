---
type: pulse
title: Mnemon — fourth agent-memory pattern enters the field (LLM-Supervised)
slug: 2026-05-12-mnemon-llm-supervised-memory
created: 2026-05-12
updated: 2026-05-12
departments: [ai-office]
confidence: medium
sources: [mnemon-github-readme]
related: [agent-memory, agent-memory-2026-q2, agent-harness, claude, openclaw, model-context-protocol]
---

# Mnemon — fourth agent-memory pattern enters the field (LLM-Supervised)

A new open-source agent-memory project, **Mnemon** (github.com/mnemon-dev/mnemon), surfaced via Web Clipper on 2026-05-12. Mnemon is a single-binary, Go-based persistent-memory store for CLI agents — Claude Code, [[openclaw]], NanoClaw, and "any CLI agent that supports skills, rules, or event hooks." It uses a four-graph knowledge architecture (temporal / entity / causal / semantic edges plus optional vector via local Ollama) and a three-primitive intent-native protocol (`remember`, `link`, `recall`).

The interesting framing is the explicit taxonomy Mnemon places itself in:

| Pattern | LLM role | Representative |
|---|---|---|
| **LLM-Embedded** | Executor inside the pipeline | Mem0, Letta |
| **File Injection** | None — file read at session start | Claude Code Memory |
| **MCP Server** | Tool provider via [[model-context-protocol|MCP]] | claude-mem |
| **LLM-Supervised** | External supervisor of a standalone binary | **Mnemon** |

This is a cleaner decomposition than the one currently used in [[agent-memory|the wiki's agent-memory concept page]] (Files-as-memory / Harness-as-memory / Memory palace), and the "LLM-Supervised" axis — host LLM decides what to remember, deterministic binary handles storage — is a meaningfully different pattern from anything captured to date in the [[agent-memory-2026-q2]] brief. The Q2 brief tracks Anthropic (file-based, vendor-managed) and OpenAI (in-session Session primitive); Mnemon represents a *third stance*: portable, open-source, vendor-neutral, runs against any subscription LLM as the supervisor.

## Notable claims (per `mnemon-github-readme`)

- **Zero API keys.** Works through an existing Claude Max/Pro subscription; the host LLM is the intelligence layer.
- **Markdown-installable harness.** `SKILL.md` + `GUIDELINE.md` + four lifecycle hooks (Prime / Remind / Nudge / Compact). Hooks are reminders, not a hard workflow — closer to a [[ralph-loop-pattern|naive-iteration discipline]] than a rigid pipeline.
- **Cross-framework shared store.** `~/.mnemon` is intended as a single pool any agent (Claude Code, OpenClaw, NanoClaw, OpenCode, Gemini CLI) can read and write — the vendor-neutral counter-position to "your harness is your memory."
- **Theoretical grounding cited:** Recursive Language Models (Zhang/Kraska/Khattab 2025), MAGMA multi-graph agentic memory (Zou et al. 2025), and the Graph-LLM structural-equivalence work (Joshi & Zhu 2025; Yang et al. 2026 survey). Confidence: medium — papers cited but not independently verified in this ingest.

## Why this is on watch

Mnemon's vendor-neutral, file-portable, LLM-supervised stance is the closest external system seen to date to [[janus-prime-radiant-build|the Prime Radiant pattern]] applied at the agent-memory layer rather than the institutional-knowledge layer. The wiki's bet is on *compilation-stage* knowledge for organisations; Mnemon's bet is on *runtime* knowledge for individual agents — but the underlying disciplines rhyme: user-owned files, structured graphs over flat embedding stores, the LLM as supervisor over deterministic storage. Worth tracking whether Mnemon (or a sibling) becomes the de facto open-source counterweight to Claude Managed Agents' file-based memory.

Confidence remains medium pending: (a) independent corroboration of adoption / star history beyond the README, (b) the papers cited actually delivering on the architectural claims at production scale, (c) whether the cross-framework shared-store vision survives contact with real concurrent agents.

## Pointers

Repo: github.com/mnemon-dev/mnemon. Architecture detail: `docs/DESIGN.md` in the repo (deferred — not fetched in this ingest). Source: `mnemon-github-readme`.
