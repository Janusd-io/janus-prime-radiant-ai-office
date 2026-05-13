---
type: decision
title: Self-host n8n on Hostinger instead of GCP
slug: 2026-04-22-self-host-n8n-on-hostinger
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

# Self-host n8n on Hostinger instead of GCP

## Decision

n8n will run on the Hostinger VPS rather than on GCP or Tencent Cloud.

## Why

A prior cost analysis put basic n8n on GCP at roughly $70/month scaling to $4-5k over two years versus ~$900 on Hostinger; the DevOps overhead of AWS/GCP is the bigger hidden cost, and Hostinger's bundled AI/agent control surface, 400GB storage and Singapore/Malaysia data centres are an acceptable fit while the company is small.

## Evidence

> Speaker 3: So this is our host at N8N. Our host... We don't need AWS. Or Google. It's much lighter than DevOps.

## When

2026-04-22 · meeting [[2026-04-22-it-team-meeting]] · decided by [[andrey-timokhov]]

## Implications

- (to be populated by the owner)
