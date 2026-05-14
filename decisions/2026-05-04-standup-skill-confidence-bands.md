---
type: decision
title: Standup skill writes to Monday using three confidence bands
slug: 2026-05-04-standup-skill-confidence-bands
created: 2026-05-04
updated: 2026-05-04
departments: [ai-office]
status: resolved
owner: jehad-altoutou
decided_by: michael-bruck
sources: [2026-05-04-bonaventure-michael-jehad-and-andrew-meeting]
related: []
audience: department
captured_by: jehad-altoutou
confidence: high
---

# Standup skill writes to Monday using three confidence bands

## Decision

The rewritten standup skill auto-applies Monday updates at >=90% confidence, prompts the user between 60-80%, and ignores anything below 60%.

## Why

Confidence is computed by cross-matching the Fireflies transcript against Monday tasks and the Notion running log. The bands give a clean automation / human-in-the-loop / silent split so the agent doesn't manufacture work from low-signal mentions.

## Evidence

> Michael Bruck: Making like confidence of 90% and above. ... it will update it automatically. Between 60 to 80. It will ask you for your permission. ... lower than that. It will not update anything.

## When

2026-05-04 · meeting [[2026-05-04-bonaventure-michael-jehad-and-andrew-meeting]] · decided by [[michael-bruck]] · owned by [[jehad-altoutou]]

## Implications

- (to be populated by the owner)
