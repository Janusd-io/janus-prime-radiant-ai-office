---
type: decision
title: "Each new departmental Prime Radiant lets Claude propose its directory structure from transcripts, not human-architected upfront"
slug: 2026-05-13-let-claude-propose-vault-structure-not-architect-top-down
created: 2026-05-13
updated: 2026-05-13
departments: [ai-office]
status: resolved
owner: euclid-wong
decided_by: michael-bruck
sources: [2026-05-13-aio-project-management-meeting]
related: []
audience: department
captured_by: jehad-altoutou
confidence: high
---

# Each new departmental Prime Radiant lets Claude propose its directory structure from transcripts, not human-architected upfront

## Decision

For the IT/Ops instance (and future instances), the seeding process is: feed Claude the team's existing meeting transcripts and materials, let it surface patterns and propose a directory structure, then iterate — do not hand-design the folder taxonomy.

## Why

Michael and Euclid argued through this on the call: hand-architecting the structure produces broken links and suboptimal organisation because the human guesses categories before the LLM has seen the content. The Claude.md schema discipline (front-matter, kebab-case slugs, inbox-as-entry-point) is fixed; the per-department directory vocabulary is emergent. The marketing instance with Andrew followed this pattern and worked.

## Evidence

> Michael Bruck: Discuss what you want the outcome to be. Euclid: ... I'm going to ask you to do one thing in the transcript before you send it ...

## When

2026-05-13 · meeting [[2026-05-13-aio-project-management-meeting]] · decided by [[michael-bruck]] · owned by [[euclid-wong]]

## Implications

- (to be populated by the owner)
