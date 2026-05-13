---
type: article
title: "Anatomy of the .claude/ folder"
slug: anatomy-of-claude-folder
created: 2026-05-07
updated: 2026-05-07
source: "https://x.com/akshay_pachaar/status/2035341800739877091"
author: Akshay Pachaar
published: 2026-03-21
confidence: high
---

Complete schema for .claude/ control center. Two folders: project-level (committed, team config) and ~/.claude/ (personal preferences, session history). Key files: CLAUDE.md (instructions, load-bearing), CLAUDE.local.md (personal overrides, gitignored), settings.json (permissions, hooks). Structures: rules/ (modular instructions by concern), hooks/ (deterministic event handlers at PreToolUse, PostToolUse, Stop points), skills/ (auto-invoked workflows), agents/ (specialized subagent personas with isolated context). Best practice: start with CLAUDE.md under 200 lines, add rules/ when it exceeds that, use hooks for security gates and post-edit formatters, use agents for specialized read-only tasks with model downselection.
