---
type: vendor
title: OpenAI Codex
slug: openai-codex
air_id: AIR-84
status: Sandbox
labels: [Functional, Technology]
departments: []
url: https://linear.app/janusd/issue/AIR-84/openai-codex
created: 2026-04-21
updated: 2026-04-22
captured_by: jehad-altoutou
audience: department
sensitivity: dept
sensitivity_confidence: 0.9
---
<!-- jb:air-vendor-callout -->
> Part of [[ai-registry|AI Registry]]


# OpenAI Codex

> AI Registry entry [AIR-84](https://linear.app/janusd/issue/AIR-84/openai-codex) — status **Sandbox** as of 2026-04-22. Departments: —.

**Category:** SW Development / Agentic Coding Assistant
**Cost per User/Month:** Bundled with [[chatgpt|ChatGPT]] plans — Free, Plus $20, Pro from $100, Business pay-as-you-go, Enterprise. API key option also available.
**Departments:** Technology

## Overview

OpenAI's agentic coding platform — desktop app (macOS, Windows), IDE extension, CLI, cloud/web surface. Direct competitor to [[claude-code|Claude Code]] and GitHub Copilot agentic modes. Bundled into ChatGPT paid plans. Powered by GPT-5.4, GPT-5.3-Codex, GPT-5.3-Codex-Spark.

## Key Products & Capabilities

* Codex Desktop App — multi-project command centre, parallel agent threads, built-in review pane
* IDE Extension — native [[vs-code|VS Code]]-family integration
* Codex CLI — terminal-native agent for headless/scripted workflows
* Codex Web / Cloud — long-running cloud environments
* Automations — scheduled recurring tasks
* Worktrees — native Git worktree support
* Skills, Plugins & Subagents — reusable workflows, MCP support
* Codex SDK & App Server
* GitHub Action — tag @Codex for automated code review

## Integrations

* GitHub — first-class integration
* Slack — cloud thread/task notifications
* [[linear|Linear]] — issue-driven coding workflows
* MCP support
* IDE Extension for VS Code
* Codex SDK / App Server / MCP Server

## Security & Compliance

* Business: No training on business data, SAML SSO, MFA, dedicated workspace, admin controls
* Enterprise & Edu: SCIM, EKM, domain verification, data retention/residency controls, audit logs
* Sandboxing with approval gates
* Threat model docs at developers.openai.com/codex/security

## Relevance

Most credible direct alternative to [[claude|Claude]] Code. Monitoring gives AI Office comparative benchmark for agentic coding capability, pricing, enterprise controls. Hedges against over-reliance on single foundation model vendor. Linear/Slack/GitHub integrations overlap directly with existing AI Office stack — controlled pilot low-friction.

## Considerations

* Overlaps with Claude Code (Production) — parallel capability not replacement
* Bundled with ChatGPT plans — complicates licence counting
* Multi-vendor complexity — Claude Code + Codex governance overhead
* Free/Plus may train on inputs — only Business/Enterprise gives no-training guarantee
* Some features still research preview (GPT-5.3-Codex-Spark)

*Sandbox. Functional tier. Direct comparator to Claude Code ([[claude-code|AIR-13]]).*
