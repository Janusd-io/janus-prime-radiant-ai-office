---
type: decision
title: Adopt Obsidian Git community plugin as the sync mechanism; drop GitHub Desktop app and CLI
slug: 2026-05-14-adopt-obsidian-git-plugin-drop-github-desktop-and-cli
created: 2026-05-14
updated: 2026-05-14
departments: [ai-office]
status: resolved
owner: jehad-altoutou
decided_by: jehad-altoutou
sources: [2026-05-14-data-management-system-overhaul-meeting]
related: []
audience: department
captured_by: jehad-altoutou
confidence: high
---

# Adopt Obsidian Git community plugin as the sync mechanism; drop GitHub Desktop app and CLI

## Decision

Use the Obsidian Git community plugin (by Vinzent03) inside each vault for pull/push to GitHub; no GitHub Desktop app, no separate CLI workflow.

## Why

When Jehad opened Obsidian he saw the plugin auto-running git pull/push notifications, confirming background sync works end-to-end. Claude Code does not need a desktop GitHub app, and Jehad confirmed CLI is not required either. The plugin has all the settings needed (auto-commit interval, host name for attribution).

## Evidence

> Speaker 3: So I don't think we need CLI. Speaker 2: No, I think. Just push. Just like it does it directly.

## When

2026-05-14 · meeting [[2026-05-14-data-management-system-overhaul-meeting]] · decided by [[jehad-altoutou]]

## Implications

- (to be populated by the owner)
