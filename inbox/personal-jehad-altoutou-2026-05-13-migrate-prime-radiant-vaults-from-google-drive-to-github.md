---
type: decision
title: Migrate Prime Radiant vaults from Google Shared Drive to GitHub
slug: 2026-05-13-migrate-prime-radiant-vaults-from-google-drive-to-github
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

# Migrate Prime Radiant vaults from Google Shared Drive to GitHub

## Decision

Prime Radiant Obsidian vaults will be stored in GitHub repositories (synced via the Obsidian Git plugin every five minutes), not on Google Shared Drive.

## Why

Google Shared Drive streams file content on demand, so Claude Code / Cowork sees empty directories when scanning the synced folder — it cannot read the markdown until each file is clicked. GitHub also delivers version control, audit logs, account-based access control, and protection against accidental deletion that Drive does not provide. The setup is fiddlier but a one-time cost.

## Evidence

> Speaker 3: GitHub. We set up a repo in GitHub, and Obsidian, which is the database that we're using, has a plugin, extension, for GitHub.

## When

2026-05-13 · meeting [[2026-05-13-aio-it-meeting]] · decided by [[michael-bruck]]

## Implications

- (to be populated by the owner)
