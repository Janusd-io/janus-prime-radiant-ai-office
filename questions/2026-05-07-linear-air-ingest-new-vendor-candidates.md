---
type: question
title: New vendor candidates from Linear AIR Phase 4 ingest
slug: 2026-05-07-linear-air-ingest-new-vendor-candidates
created: 2026-05-07
updated: 2026-05-07
status: resolved
owner: michael
sources: [air-39, air-38, air-20, air-21]
related: [nemoclaw, viktor, openclaw]
---

# New vendor candidates from Linear AIR Phase 4 ingest (resolved)

Resolved 2026-05-07 per Michael's "follow your recommendations" directive.

## Resolutions

| Candidate | Recommendation | Decision | Notes |
|---|---|---|---|
| NemoClaw | Create | **Approved (created)** | `entities/vendors/nemoclaw.md`. Production tier-1 agent infrastructure per AIR-39. |
| Viktor | Create | **Approved (created)** | `entities/vendors/viktor.md` (status: archived). Rejected vendor; retained because the rejection drove [[2026-04-22-per-user-data-control-hard-requirement-agent-platforms]]. |
| Make | Skip | **Confirmed skip** | Source-only reference (`sources/linear/air-20.md`); rejected workflow automation; lower signal. |
| Lindy | Skip | **Confirmed skip** | Source-only reference (`sources/linear/air-21.md`); rejected AI agent builder; fails G1.4 (data training policy). |
| Dify | Defer | **Confirmed defer** | Mentioned in Lindy evaluation as alternative for RAG-intensive workflows; create vendor page if/when Janus formally evaluates. |

## Closeout

`status: resolved` 2026-05-07.
