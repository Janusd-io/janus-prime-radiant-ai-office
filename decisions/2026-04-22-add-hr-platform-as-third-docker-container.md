---
type: decision
title: Run the HR platform as its own Docker container
slug: 2026-04-22-add-hr-platform-as-third-docker-container
created: 2026-04-22
updated: 2026-04-22
departments: [ai-office]
status: resolved
owner: jehad-altoutou
decided_by: jehad-altoutou
sources: [2026-04-22-it-team-meeting]
related: []
audience: department
captured_by: jehad-altoutou
confidence: high
---

# Run the HR platform as its own Docker container

## Decision

The HR leave-request platform will be deployed as a third Docker container on the Hostinger VPS, separate from n8n and the reverse proxy.

## Why

Container isolation means failure of one component (n8n, proxy, HR platform) doesn't take the others down. Jehad designed it explicitly so each container fails alone.

## Evidence

> Speaker 1: Once we add the platform, we're going to have a third container as a Docker.

## When

2026-04-22 · meeting [[2026-04-22-it-team-meeting]] · decided by [[jehad-altoutou]]

## Implications

- (to be populated by the owner)
