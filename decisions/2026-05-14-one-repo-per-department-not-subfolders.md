---
type: decision
title: "One GitHub repo per department, not subfolders inside one repo"
slug: 2026-05-14-one-repo-per-department-not-subfolders
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

# One GitHub repo per department, not subfolders inside one repo

## Decision

Each department (marketing, AI office, PM, IT, ...) gets its own top-level private GitHub repo mirroring its vault directory structure; departments are not subfolders inside a single mono-repo.

## Why

Clean access control — different departments need different group memberships and permission scopes. Mirroring vault structure 1:1 to repo structure keeps the Obsidian Git plugin wiring straightforward.

## Evidence

> Speaker 3: Each department gets get its own top-level repo. Speaker 2: Repo. Oh, okay. Speaker 3: Wh-which mirrors the directory structure.

## When

2026-05-14 · meeting [[2026-05-14-data-management-system-overhaul-meeting]] · decided by [[jehad-altoutou]]

## Implications

- (to be populated by the owner)
