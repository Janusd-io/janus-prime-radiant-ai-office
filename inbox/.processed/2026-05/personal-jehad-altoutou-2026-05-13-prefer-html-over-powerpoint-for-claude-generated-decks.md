---
type: decision
title: Prefer HTML over PowerPoint for Claude-generated decks
slug: 2026-05-13-prefer-html-over-powerpoint-for-claude-generated-decks
created: 2026-05-13
updated: 2026-05-13
departments: [ai-office]
status: resolved
owner: michael-bruck
decided_by: jehad-altoutou
sources: [2026-05-13-aio-it-meeting]
related: []
audience: department
captured_by: jehad-altoutou
confidence: medium
---

# Prefer HTML over PowerPoint for Claude-generated decks

## Decision

Going forward, presentations generated via Claude will be produced as HTML rather than PowerPoint to reduce token consumption.

## Why

PowerPoint generation forces Claude to write Python via a special skill, which burns disproportionate tokens — one user was discovered hitting their plan limits primarily from generating PowerPoint after PowerPoint. HTML is native to a language model, cheap, and produces visually comparable output.

## Evidence

> Speaker 2: From now on, I'm only doing presentations at HTML.

## When

2026-05-13 · meeting [[2026-05-13-aio-it-meeting]] · decided by [[jehad-altoutou]] · owned by [[michael-bruck]]

## Implications

- (to be populated by the owner)
