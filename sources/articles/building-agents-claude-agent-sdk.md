---
type: article
title: "Building agents with the Claude Agent SDK"
slug: building-agents-claude-agent-sdk
created: 2026-05-07
updated: 2026-05-07
source: "https://claude.com/blog/building-agents-with-the-claude-agent-sdk"
author: Anthropic
published: 2026-09-29
confidence: high
---

Anthropic's canonical guide. Claude Agent SDK (renamed from Claude Code SDK) operationalizes the agent harness pattern: Gather Context (agentic search + file system, semantic search, subagents, compaction) -> Take Action (tools, bash, code generation, MCPs) -> Verify Work (rules-based feedback, visual feedback, linters). Key innovation: giving agents a computer unlocks general-purpose automation. Feedback loop: gather -> act -> verify -> repeat. Subagents enable parallelization and context isolation. Compaction prevents context exhaustion on long-running tasks. MCPs provide standardized integrations (Slack, GitHub, Asana, etc.). Visual feedback for UI tasks. Rules-based verification (linters, validators) most effective for catching mistakes before they compound.
