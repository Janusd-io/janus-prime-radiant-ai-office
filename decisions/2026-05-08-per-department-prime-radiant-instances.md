---
type: decision
title: Each Janus department gets its own Prime Radiant instance
slug: 2026-05-08-per-department-prime-radiant-instances
created: 2026-05-08
updated: 2026-05-13
departments: [ai-office]
status: resolved
owner: michael-bruck
decided_by: michael-bruck
sources: [2026-05-08-jehad-michael-bonaventure-meeting, jehad-vault-import-2026-05-13]
related: []
captured_by: jehad-altoutou
confidence: high
---

# Each Janus department gets its own Prime Radiant instance

## Decision

Janus will roll out the Prime Radiant pattern as one instance per department, with shared department folders acting as connecting nodes between instances rather than a single monolithic vault.

## Why

Different departments need different sources (e.g. Andrew's marketing instance pulls from his CRM; HR has its own data shape). Inter-department collaboration is modelled by adding a department entity folder (e.g. 'marketing') inside each peer instance, which becomes the federation surface. This also handles onboarding/offboarding cleanly.

## Evidence

> Michael Bruck: Every department will have a different version... So it becomes the connecting nodes between different departments.

## When

2026-05-08 · meeting [[2026-05-08-jehad-michael-bonaventure-meeting]] · decided by [[michael-bruck]]

## Implications

- (to be populated by the owner)
