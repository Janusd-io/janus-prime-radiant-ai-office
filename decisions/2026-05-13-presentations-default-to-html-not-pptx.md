---
type: decision
title: Default to HTML output for presentations instead of PowerPoint
slug: 2026-05-13-presentations-default-to-html-not-pptx
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

# Default to HTML output for presentations instead of PowerPoint

## Decision

Going forward, presentations generated with Claude are produced as HTML rather than PowerPoint to avoid burning tokens.

## Why

Generating PowerPoint via Claude is expensive because the model must write Python via a skill rather than emit text natively; HTML output is cheap, fast, and looks good. One AIO user (referenced in the meeting as the bottleneck Simon) was observed hitting Claude usage limits primarily because they were generating PowerPoint after PowerPoint.

## Evidence

> Speaker 2: From now on, I'm only doing presentations at HTML.

## When

2026-05-13 · meeting [[2026-05-13-aio-it-meeting]] · decided by [[jehad-altoutou]] · owned by [[michael-bruck]]

## Implications

- (to be populated by the owner)
