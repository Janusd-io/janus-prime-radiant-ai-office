---
type: decision
title: "Drive permissions are managed via Google Groups, not per-user grants"
slug: 2026-05-07-google-groups-drive-permissions
created: 2026-05-07
updated: 2026-05-07
departments: [ai-office]
status: resolved
owner: euclid-wong
decided_by: jehad-altoutou
sources: [2026-05-07-michael-jehad-euclid-andre-it-operations]
related: []
audience: department
captured_by: jehad-altoutou
confidence: high
---

# Drive permissions are managed via Google Groups, not per-user grants

## Decision

Access to department Shared Drives will be granted to Google Groups (e.g. `it@janisd.com`, `finance@janisd.com`), so adding an employee to a group automatically grants drive access.

## Why

Per-user grants would force IT to handle every access request individually and would scale badly to hundreds of folders. Group-based permissions let onboarding flows assign group membership once and inherit access everywhere.

## Evidence

> Jehad Altoutou: And if you use Google Groups, when you add an employee to that group, they will get automatically added to the permission for that role.

## When

2026-05-07 · meeting [[2026-05-07-michael-jehad-euclid-andre-it-operations]] · decided by [[jehad-altoutou]] · owned by [[euclid-wong]]

## Implications

- (to be populated by the owner)
