---
type: decision
title: Decommission Signature Hound dependency
slug: 2026-04-22-decommission-signature-hound
created: 2026-04-22
updated: 2026-05-13
departments: [ai-office]
status: resolved
owner: andrey-timokhov
decided_by: andrey-timokhov
sources: [2026-04-22-it-team-meeting, jehad-vault-import-2026-05-13]
related: []
captured_by: jehad-altoutou
confidence: high
---

# Decommission Signature Hound dependency

## Decision

Janus email-signature assets will be moved off the Signature Hound CDN onto Janus's own AWS bucket, removing the paid Signature Hound integration.

## Why

Signature Hound's paid tier was only needed for automatic push into Google Workspace; the free tier remains adequate for generating signatures, and self-hosting the images on AWS avoids ongoing vendor dependency and an already-expired account.

## Evidence

> Speaker 1: I downloaded them. I managed to access our AWS... if we want to integrate it automatically, push to Google Workspace, that costs money... we don't need it.

## When

2026-04-22 · meeting [[2026-04-22-it-team-meeting]] · decided by [[andrey-timokhov]]

## Implications

- (to be populated by the owner)
