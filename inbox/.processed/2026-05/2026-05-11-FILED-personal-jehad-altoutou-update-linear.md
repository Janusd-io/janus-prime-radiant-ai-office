---
type: question
slug: update-linear
title: Proposed update to entities/vendors/linear.md
created: 2026-05-11
updated: 2026-05-11
status: active
owner: jehad-altoutou
audience: [department]
departments: [ai-office]
captured_by: jehad-altoutou
target_page: entities/vendors/linear.md
---

# Proposed update to entities/vendors/linear.md

**Reason:** Personal linear.md identifies AIR and AIP teams by name but omits the team UUIDs and AIP status UUIDs that are operationally load-bearing. Also missing the snapshot of recent AIP issues — useful for cross-reference when transcripts mention them.

**Patch block** (append to existing canonical page):

---


## Team identifiers and AIP status UUIDs

From AI Office Brain `Systems-of-Record/Linear-AIR.md` and `Linear-AIP.md` (4 May 2026). Sources: [[aio-brain-sor-linear-air]], [[aio-brain-sor-linear-aip]].

- **AI Registry (AIR) team UUID:** `598dd614-dce5-4ede-98ef-207f3bdff33c`. Issue prefix `AIR-N`. Note: team was originally created with the name "AI Office" but issues are prefixed `AIR-N` — the prefix is what matters.
- **AI Projects (AIP) team UUID:** `2d1b5c04-94fd-4087-8e95-a5a7aa244a16`. Issue prefix `AIP-N`.

### AIP status UUIDs

| Status | UUID |
|---|---|
| Backlog | `57d6d704-7a3b-41f9-b936-a7d64252d00a` |
| Planned | `d5ccd469-37b4-4b5b-92d6-21be9f27dc90` |
| In Progress | `210b719c-eb51-4d5f-88fb-dcde85ae9939` |
| Done | `661dd6ca-5d5b-4378-8cb4-f1b0384975dc` |
| Cancelled | `ebfcf4e3-f40e-4599-a2b2-827656299627` |

### AIR pipeline

`Backlog → Evaluating → Sandbox → Production` (or `→ Monitor`); also `→ Deprecated / Rejected / Duplicate`.

### Snapshot of recent AIP issues (May 2026)

- AIP-1 Finance Department API Integration (Planned)
- AIP-15 Deel API & Developer Platform — Capability Assessment (Planned)
- AIP-16 Town Hall Transcript Processing — Pilot (Planned)
- AIP-17 CEO Dashboard — Global Operations View (Backlog)
- AIP-18 Cross-Department Action Routing (Backlog)
- AIP-19 Invoice Bot v3/v4 (Done)
- AIP-20 HR Employee Form Replacement (Done)
- AIP-21 Assessify — Candidate Assessment Platform (Done — expansion underway, conflict logged)
- AIP-22 Decide n8n hosting (Done)

### AIR snapshot stats (May 2026)

74 active issues. Most recent: **AIR-92 Wispr Flow (Whisper Flow)** — added 1 May 2026 standup; Backlog; Functional + Technology + AI Policy.

