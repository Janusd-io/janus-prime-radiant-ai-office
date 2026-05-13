---
type: decision
title: AI Tools Registry source of truth stays in Linear AIR; Monday AITR deprecated
slug: 2026-05-01-ai-registry-source-of-truth-stays-in-linear-air
created: 2026-05-06
updated: 2026-05-13
departments: [ai-office]
status: resolved
owner: michael-bruck
decided_by: michael-bruck
sources: [aio-2026-05-01, jehad-vault-2026-05-01-ai-registry-source-of-truth-stays-in-linear-air]
related: [linear, ai-tool-evaluation, janus-prime-radiant-build]
---

# AI Tools Registry source of truth stays in Linear AIR

**Decision date:** 2026-05-01
**Decided by:** Michael Bruck, Jehad Altoutou
**Source:** [[aio-2026-05-01]]

## What

The AI Tools Registry remains in Linear (`AIR` team) as its sole source of truth. The Monday AI Tools Registry board (`5095577150`) is deprecated as an active execution surface and retained only as historical reference.

## Why

Prior migrations from Monday to Linear (and back) had introduced duplication-sync issues — fields drifting out of step, two copies of the same evaluation in different stages, manual reconciliation overhead. Keeping a single canonical surface — Linear AIR — eliminates the sync problem at its root. The `/ai-registry` and [[ai-tool-evaluation]] skills already operate against Linear AIR, so the tooling supports this decision.

## Implications

- The Monday AITR board is read-only / historical going forward. No new tools created there. No status updates pushed there from `/standup`.
- All AI tool work flows through the Linear AIR pipeline (Backlog → Evaluating → Sandbox → Production → Monitor → Deprecated/Rejected/Duplicate).
- The wiki's [[linear]] vendor page reflects this; this wiki ingests Linear AIR closed/resolved issues per `CLAUDE.md` §5.1.

## Related

- [[2026-05-06-monday-com-to-production-this-week]] — separate decision; that's about Monday-the-vendor going to production, not about the AITR board.
- [[ai-tool-evaluation]] framework operates against Linear AIR exclusively.
