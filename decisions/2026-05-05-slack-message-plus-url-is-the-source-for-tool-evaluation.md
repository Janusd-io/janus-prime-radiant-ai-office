---
type: decision
title: Slack message + URL is the canonical Source for the AI tool-evaluation process
slug: 2026-05-05-slack-message-plus-url-is-the-source-for-tool-evaluation
created: 2026-05-05
updated: 2026-05-05
departments: [ai-office]
status: resolved
owner: michael-bruck
decided_by: michael-bruck
sources: [2026-05-05-may-05-11-03-am]
related: []
audience: department
captured_by: jehad-altoutou
confidence: high
---

# Slack message + URL is the canonical Source for the AI tool-evaluation process

## Decision

The Source row of the ISO Figure-1 mapping for tool evaluation is a Slack message containing at minimum a URL; the auto-extracted request form is the Input, not the Source.

## Why

Slack is already the team's primary communication channel and carries the requester identity, timestamp, channel, and link out of the box. Making it the canonical Source lets a downstream agent (Nomi-style bot) trigger the evaluation skill automatically. A URL policy is required because picture-only requests can't trigger anything.

## Evidence

> Speaker 2: So source of inputs is a URL. Plus a date. Plus a submitter. That's it.

## When

2026-05-05 · meeting [[2026-05-05-may-05-11-03-am]] · decided by [[michael-bruck]]

## Implications

- (to be populated by the owner)
