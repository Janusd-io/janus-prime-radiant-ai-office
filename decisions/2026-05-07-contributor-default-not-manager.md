---
type: decision
title: "Default Shared Drive role for department members is Contributor, not Manager"
slug: 2026-05-07-contributor-default-not-manager
created: 2026-05-07
updated: 2026-05-07
departments: [ai-office]
status: resolved
owner: euclid-wong
decided_by: michael-bruck
sources: [2026-05-07-michael-jehad-euclid-andre-it-operations]
related: []
audience: department
captured_by: jehad-altoutou
confidence: high
---

# Default Shared Drive role for department members is Contributor, not Manager

## Decision

On per-department Shared Drives, members are added as Contributors by default; only the department head holds the Manager role. Contributors can add and modify files but cannot change permissions.

## Why

Manager-by-default would let every member change permissions and kick others out, which is unsafe; pinning Manager to the department head and giving everyone else Contributor preserves the IT-administered permission boundary while still allowing day-to-day work. Onboarding adds people to the Google Group; the group then maps to Contributor on the drive.

## Evidence

> Michael Bruck: A contributors can only add delete files… you can't change permissions.

## When

2026-05-07 · meeting [[2026-05-07-michael-jehad-euclid-andre-it-operations]] · decided by [[michael-bruck]] · owned by [[euclid-wong]]

## Implications

- (to be populated by the owner)
