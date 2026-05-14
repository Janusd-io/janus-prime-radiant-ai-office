---
type: decision
title: Migrate Prime Radiant substrate from Google Shared Drive to GitHub
slug: 2026-05-13-migrate-prime-radiant-substrate-from-google-drive-to-github
created: 2026-05-13
updated: 2026-05-13
departments: [ai-office]
status: resolved
owner: michael-bruck
decided_by: michael-bruck
sources: [2026-05-13-aio-it-meeting]
related: []
audience: department
captured_by: jehad-altoutou
confidence: high
---

# Migrate Prime Radiant substrate from Google Shared Drive to GitHub

## Decision

The Prime Radiant vaults move off Google Shared Drive and onto GitHub, with Obsidian's Git plugin doing a push roughly every five minutes.

## Why

Google Shared Drive streams file content on demand, so when an Obsidian vault is mirrored there, Claude Code and Claude Cowork see directory listings but the file bodies are not pulled in until each file is clicked — they read empty directories and the vault is unusable. GitHub additionally gives the vault version control, an audit trail of every change, account-based access control, and protection against accidental deletion (which on Google Drive would be unrecoverable without a separately implemented backup). The trade-off is more fiddly setup, mitigated by 'do it once and forget'.

## Evidence

> Speaker 3: GitHub. We set up a repo in GitHub, and Obsidian... has a plugin, extension, for GitHub.

## When

2026-05-13 · meeting [[2026-05-13-aio-it-meeting]] · decided by [[michael-bruck]]

## Implications

- (to be populated by the owner)
