---
type: vendor
title: Repo Prompt
slug: repo-prompt
air_id: AIR-37
status: Rejected
labels: [AI Policy, Functional]
departments: []
url: https://linear.app/janusd/issue/AIR-37/repo-prompt
created: 2026-02-25
updated: 2026-04-08
captured_by: jehad-altoutou
audience: department
sensitivity: dept
sensitivity_confidence: 0.9
---
<!-- jb:air-vendor-callout -->
> Part of [[ai-registry|AI Registry]]


# Repo Prompt

> AI Registry entry [AIR-37](https://linear.app/janusd/issue/AIR-37/repo-prompt) — status **Rejected** as of 2026-04-08. Departments: —.

**Category:** AI Development Tool / Context Management
**Status:** REJECTED
**Cost:** $9.99 one-time (macOS App Store) or free open-source CLI

## Overview

macOS app + open-source CLI for aggregating and formatting repository context for AI coding assistants. Select files/folders → generates structured, token-optimised context document for AI chatbots ([[claude|Claude]], [[chatgpt|ChatGPT]], [[gemini|Gemini]]).

## Rejection Rationale

* **Superseded by [[claude-code|Claude Code]] ([[claude-code|AIR-13]])** — Claude Code automatically handles codebase navigation and context. No manual file selection needed.
* **Manual workflow** — time-consuming, error-prone
* **Not agentic** — only formats context, cannot execute tasks or modify code
* **Limited to macOS** — native app macOS-only (CLI cross-platform but less user-friendly)

## Policy Alignment

No compliance concerns — runs locally with no data transmission. Rejected on functional grounds.

*Rejected. Superseded by Claude Code (AIR-13).*
