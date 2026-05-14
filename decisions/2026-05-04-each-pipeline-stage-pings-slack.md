---
type: decision
title: Each pipeline stage emits a Slack status reply
slug: 2026-05-04-each-pipeline-stage-pings-slack
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
confidence: medium
---

# Each pipeline stage emits a Slack status reply

## Decision

Every transition between AI Registry pipeline stages (backlog -> evaluation -> sandbox -> IT handoff) sends a status ping back into the originating Slack thread.

## Why

Both Michael and Bonaventure agreed visible real-time agent activity in a thread is part of the value — both for the requester and as the visible 'agent at work' demo. Modelled on the Telegram-style thread updates Michael cited.

## Evidence

> Michael Bruck: A quick ping back saying, "It's now moved to the next section." Something like that. Provide feedback. Status updates.

## When

2026-05-04 · meeting [[2026-05-04-bonaventure-michael-jehad-and-andrew-meeting]] · decided by [[michael-bruck]]

## Implications

- (to be populated by the owner)
