---
type: decision
title: Slack is the canonical source for AI tool-evaluation requests
slug: 2026-05-05-slack-is-canonical-source-of-tool-requests
created: 2026-05-05
updated: 2026-05-05
departments: [ai-office]
status: resolved
owner: unknown-speaker-2
decided_by: unknown-speaker-2
sources: [2026-05-05-may-05-11-03-am]
related: []
audience: department
captured_by: jehad-altoutou
confidence: high
---

# Slack is the canonical source for AI tool-evaluation requests

## Decision

All AI tool-evaluation requests will originate from Slack messages, and the Slack-extracted JSON (user, channel, timestamp, URL, company name) provides the required fields for the input request form.

## Why

Slack is already the company's primary communication channel, every message carries unique IDs and structured metadata, and using one origin point lets the AI agent (Nomi/successor) parse, enrich and trigger the right skill automatically rather than relying on screenshots or unstructured submissions. The team is also expecting clients to standardise on Slack over Teams, so this aligns the internal workflow with the future external interface.

## Evidence

> Speaker 2: So now if we're using Slack as our go-to. Let's see what else Slack gives us in certain surfaces like that. And that will drive your input form.

## When

2026-05-05 · meeting [[2026-05-05-may-05-11-03-am]] · decided by [[unknown-speaker-2]]

## Implications

- (to be populated by the owner)
