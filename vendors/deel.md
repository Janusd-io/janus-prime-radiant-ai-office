---
type: vendor
title: Deel
slug: deel
created: 2026-05-06
updated: 2026-05-06
departments: [hr]
status: active
confidence: medium
sources: [aio-2026-05-04]
related: [assessify, linear]
migrated_from: entities/vendors/deel.md
---
# Deel

HR / payroll platform with developer API. At Janus, currently used as the **headless backend** for HR operations — line managers do not interact with Deel directly; they interact via agentic UIs that sit on top of Deel.

## Status

- **Linear AIP-15** "Deel API & Developer Platform — Capability Assessment" — Planned in Linear as of 2026-05-04. Today's standup discussed using Deel as backend (operational use), but no transcript evidence of explicit status change → AIP-15 not auto-advanced. Worth a follow-up to formally start the AIP-15 evaluation given Deel is now an active backend dependency.

## Janus architecture pattern (decided 2026-05-04)

Deel becomes the headless backend; agentic UIs become the user surface. Rationale: Deel's UI is suboptimal for line-manager workflows, and the agentic-UI middleware lets Janus shape the interaction without forking the data layer.

## Watch for

- AIP-15 evaluation moving from Planned to In Progress now that Deel is operationally critical.
- Whether the agentic-UI-as-middleware pattern generalises to other vendors with awkward native UIs.
