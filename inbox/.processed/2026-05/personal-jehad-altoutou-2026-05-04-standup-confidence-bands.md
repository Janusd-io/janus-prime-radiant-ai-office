---
type: decision
title: Use three confidence bands for standup-skill auto-updates
slug: 2026-05-04-standup-confidence-bands
created: 2026-05-04
updated: 2026-05-04
departments: [ai-office]
status: resolved
owner: michael-bruck
decided_by: michael-bruck
sources: [2026-05-04-bonaventure-michael-jehad-and-andrew-meeting]
related: []
audience: department
captured_by: jehad-altoutou
confidence: high
---

# Use three confidence bands for standup-skill auto-updates

## Decision

The standup skill auto-updates Monday tasks at >=85% confidence, asks the user to confirm at 60-80%, and surfaces-only without acting below 60%.

## Why

Michael built confidence scoring across Monday + Linear + Notion + transcript cross-references to keep the agent autonomous on high-signal matches but cautious on ambiguous ones, avoiding silent bad writes to Monday.

## Evidence

> Michael Bruck: confidence of 90% and above. ... it will update it automatically. Between 60 to 80. It will ask you ... lower than that. It will not update.

## When

2026-05-04 · meeting [[2026-05-04-bonaventure-michael-jehad-and-andrew-meeting]] · decided by [[michael-bruck]]

## Implications

- (to be populated by the owner)
