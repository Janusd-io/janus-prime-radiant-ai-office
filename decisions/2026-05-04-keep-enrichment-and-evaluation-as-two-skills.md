---
type: decision
title: Keep enrichment and evaluation as two distinct skills
slug: 2026-05-04-keep-enrichment-and-evaluation-as-two-skills
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

# Keep enrichment and evaluation as two distinct skills

## Decision

The AI Registry pipeline keeps the enrichment skill (writes the rich Linear memo) separate from the evaluation skill (AI policy hard gates), rather than collapsing them into one.

## Why

Bonaventure argued for combining them since they run back-to-back. Michael held the line: the enrichment pass builds a rich memo cache so repeat encounters with similar tools don't rescan from scratch ('it's a memory'), and the evaluation pass is the binary policy gate. Different responsibilities, different outputs. Iteration on the split is open.

## Evidence

> Michael Bruck: But it's two distinct steps of the process. ... it's kind of like the memory. It's a way of keeping track of what we've looked at in a much more detailed format.

## When

2026-05-04 · meeting [[2026-05-04-bonaventure-michael-jehad-and-andrew-meeting]] · decided by [[michael-bruck]]

## Implications

- (to be populated by the owner)
