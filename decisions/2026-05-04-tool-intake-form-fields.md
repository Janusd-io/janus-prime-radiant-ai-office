---
type: decision
title: Lock the Slack intake form fields for new AI tool requests
slug: 2026-05-04-tool-intake-form-fields
created: 2026-05-04
updated: 2026-05-13
departments: [ai-office]
status: resolved
owner: michael-bruck
decided_by: bonaventure-wong
sources: [2026-05-04-bonaventure-michael-jehad-and-andrew-meeting, jehad-vault-import-2026-05-13]
related: []
captured_by: jehad-altoutou
confidence: high
---

# Lock the Slack intake form fields for new AI tool requests

## Decision

The canonical intake record for a new AI tool is URL, submitter name, timestamp, location, and organization - nothing more; no approval step is required at intake.

## Why

Bonaventure pushed for richer fields and an approval gate; Michael argued the intake is purely data capture and downstream checks (duplicate detection, policy evaluation) happen inside the agent pipeline. Cost of error at intake is low, so adding heavier authentication / approval is unjustified at this stage.

## Evidence

> Bonaventure Wong: URL, the name of the submitter, and we can track it. ... Organization. And that's it. We don't need more than that.

## When

2026-05-04 · meeting [[2026-05-04-bonaventure-michael-jehad-and-andrew-meeting]] · decided by [[bonaventure-wong]] · owned by [[michael-bruck]]

## Implications

- (to be populated by the owner)
