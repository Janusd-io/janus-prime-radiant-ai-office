---
type: decision
title: AI Tools Registry source of truth stays in Linear AIR; Monday AITR deprecated
slug: 2026-05-01-ai-registry-source-of-truth-stays-in-linear-air
created: 2026-05-06
updated: 2026-05-13
departments: [ai-office]
status: resolved
owner: michael-bruck
confidence: high
sources: [pr-backup-2026-05-11-decision-ai-registry-source-of-truth-linear]
related: [linear, ai-tool-evaluation-framework, ai-registry]
audience: [department]
captured_by: jehad-altoutou
---

# AI Tools Registry source of truth stays in Linear AIR

**Decision date:** 2026-05-01. **Decided by:** [[michael-bruck]], [[jehad-altoutou]]. Source: AIO 2026-05-01 standup.

## What

The AI Tools Registry remains in [[linear]] (`AIR` team) as its **sole source of truth**. The Monday AI Tools Registry board (`5095577150`) is deprecated as an active execution surface and retained only as historical reference.

## Why

Prior migrations from Monday to Linear (and back) had introduced duplication-sync issues — fields drifting out of step, two copies of the same evaluation in different stages, manual reconciliation overhead. Keeping a single canonical surface — Linear AIR — eliminates the sync problem at its root. The `/ai-registry` and [[ai-tool-evaluation-framework]] skills already operate against Linear AIR, so the tooling supports this decision.

## Implications

- The Monday AITR board is read-only / historical going forward. No new tools created there. No status updates pushed there from `/standup`.
- All AI tool work flows through the Linear AIR pipeline (Backlog → Evaluating → Sandbox → Production → Monitor → Deprecated/Rejected/Duplicate).
- The wiki ingests Linear AIR closed/resolved issues per `CLAUDE.md` §5.1.
