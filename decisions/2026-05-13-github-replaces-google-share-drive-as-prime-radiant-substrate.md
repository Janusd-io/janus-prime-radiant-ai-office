---
type: decision
title: GitHub replaces Google Shared Drive as the Prime Radiant sync substrate
slug: 2026-05-13-github-replaces-google-share-drive-as-prime-radiant-substrate
created: 2026-05-13
updated: 2026-05-13
departments: [ai-office]
status: resolved
owner: jehad-altoutou
decided_by: euclid-wong
sources: [2026-05-13-aio-project-management-meeting]
related: []
audience: department
captured_by: jehad-altoutou
confidence: high
---

# GitHub replaces Google Shared Drive as the Prime Radiant sync substrate

## Decision

Prime Radiant vaults move off Google Shared Drive onto GitHub as the central sync substrate; each user's local vault is on their laptop and Obsidian's Git plugin auto-commits and pulls.

## Why

Google Shared Drive does not work as a Claude Code / Obsidian vault backend — the database-style file access the system needs (markdown index, hidden files, fast directory reads) is incompatible with Drive's file-virtualisation model, and Claude Code + Obsidian 'just broke' when pointed at a Shared Drive. GitHub gives a central database with push/pull, local files on disk for Obsidian and Claude, and per-file privacy via the front-matter sensitivity classifier plus gitignore.

## Evidence

> Euclid: So we're going to use GitHub. Absolutely. It has a central database. Then we do push and pull. ... So between Obsidian and Claude, it just broke.

## When

2026-05-13 · meeting [[2026-05-13-aio-project-management-meeting]] · decided by [[euclid-wong]] · owned by [[jehad-altoutou]]

## Implications

- (to be populated by the owner)
