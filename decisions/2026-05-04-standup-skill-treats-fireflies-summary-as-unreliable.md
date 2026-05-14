---
type: decision
title: "Standup skill ignores Fireflies' own summary and uses the raw transcript"
slug: 2026-05-04-standup-skill-treats-fireflies-summary-as-unreliable
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

# Standup skill ignores Fireflies' own summary and uses the raw transcript

## Decision

The standup skill explicitly discards the Fireflies-generated summary and works only from the raw transcript, because the Fireflies summary is one-off and context-free.

## Why

All three attendees confirmed the Fireflies summary is unreliable ('it's crap', 'out of context'). The Notion running log and the raw transcript carry the real signal; the summary risks polluting the standup output with shallow interpretations.

## Evidence

> Michael Bruck: it will fetch the transcript from Fireflies. It will remove the summary from Fireflies. Because we can't count on it.

## When

2026-05-04 · meeting [[2026-05-04-bonaventure-michael-jehad-and-andrew-meeting]] · decided by [[michael-bruck]] · owned by [[jehad-altoutou]]

## Implications

- (to be populated by the owner)
