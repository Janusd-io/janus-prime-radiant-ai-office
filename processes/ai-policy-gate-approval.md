---
type: process
title: AI Policy Gate Approval
slug: ai-policy-gate-approval
created: 2026-05-07
updated: 2026-05-07
departments: [ai-office, it-ops, office-of-ceo]
related: [ai-tool-evaluation, linear, claude, euclid-wong, michael-bruck]
---

# AI Policy Gate Approval

Reusable governance process for moving an AI tool from "in active use" to "formally approved." Janus's AI Policy gate runs alongside the [[ai-tool-evaluation]] framework — the latter qualifies a tool against technical and integration criteria; this gate qualifies it against the AI Policy itself.

> **Boundary with [[ai-tool-evaluation]].** That framework has Gates 1–3 (intake/triage, technical qualification, sandbox evaluation) plus Stage 4 (approval & registry listing). This process is the **policy clearance** that runs in parallel — typically alongside Stage 4 — for tools that need explicit AI Policy sign-off rather than just registry listing.

## When this process applies

Any tool that:
- Is already in active use (or about to be) at Janus, AND
- Has not previously been formally approved through the AI Policy gate

Tools that come through the [[ai-tool-evaluation]] framework from cold start usually clear the AI Policy gate as part of Stage 4. This process is for **retrofit approvals** — tools that escaped formal clearance because they were adopted operationally before the gate existed, or where the gate's surface needs explicit closure.

## The 4-of-4 gate

A candidate tool must pass all four criteria. Failure on any criterion blocks approval.

| # | Criterion | What it asks |
|---|---|---|
| 1 | Data training exclusion | Does the vendor exclude Janus data from model training? Enterprise tier or ZDR is the typical answer. |
| 2 | Security posture | Does the vendor's security model meet Janus's threshold? SSO, RBAC, audit logs, data residency. |
| 3 | Integration alignment | Does the tool integrate with Janus's existing surfaces (Google Workspace / Slack / Linear / Monday) per [[ai-tool-evaluation]] G1.1–G1.5 baseline? |
| 4 | Usage scope clarity | Is the intended scope defined: who uses it, for what tasks, with which data classes? |

The exact 4th criterion is recorded in the AI Policy doc; this page summarises the structure rather than duplicating the policy. Authoritative criteria live in the AI Policy doc.

## The approval flow

```
1. Candidate identified              ← Michael / AIO surfaces the tool
2. Linear AIR record opened          ← /ai-registry skill files an AIR-N entry
3. 4-of-4 gate review                ← Michael runs the policy clearance
4. Approval outcome recorded         ← AIR-N updated with approver name + date
5. AI Policy doc updated             ← lists the tool as approved with usage scope
6. IT approved-tools list updated    ← Euclid / IT adds to v3+ list
7. Entra / browser policy updated    ← if browser-mode access restrictions apply
8. AI Hub Slack announcement         ← per [[ai-tool-evaluation]] Stage 4
```

## Cross-system coordination

This process touches **four systems** in coordination — getting any of them wrong leaves a hole:

- **AI Policy doc** ([[notion]]) — the authoritative criteria and approval log.
- **Linear AIR** — the per-tool record where the approval is timestamped.
- **IT approved-tools list** (managed by [[euclid-wong]] / IT) — the operational allow-list.
- **Entra / browser policy** — the access-control enforcement layer.

The four must be kept consistent. A tool that's approved in Linear AIR but missing from the IT list is functionally not approved (users can't access it); a tool on the IT list but not in AIR has no policy paper trail.

## Inaugural case study: Cowork

[[claude|Cowork]] is in active use across the AI Office (it's how this wiki is being maintained) but hasn't been through the AI Policy gate. Per Monday item `2891633403` (In Definition as of 2026-05-06):

- **Owner:** [[michael-bruck]] (approver), [[euclid-wong]] / IT (list updater).
- **Outstanding:** 4-of-4 gate review pending; approval not yet recorded in AIR; AI Policy doc not yet updated; IT approved-tools list (v3) does not yet include Cowork; Entra browser-mode access restriction is a separate IT policy thread (Monday `2896109889`).
- **Definition of done:** all 8 steps in the approval flow complete.

Cowork's clearance is the inaugural case for this process. Lessons from running it should feed back into refining this page.

## Roles

| Role | Holder | Responsibility |
|---|---|---|
| Gate reviewer | [[michael-bruck]] | Runs the 4-of-4 review, makes the approval call. |
| AIR record owner | per `/ai-registry` skill | Files and updates the AIR-N entry. |
| AI Policy doc maintainer | [[michael-bruck]] / AIO | Updates the policy doc with approved tools and usage scopes. |
| IT approved-tools list owner | [[euclid-wong]] / IT | Maintains the v3+ list. |
| Entra / browser policy | [[euclid-wong]] / IT | Configures access-control enforcement. |
| Slack announcement | AIO | Posts to AI Hub channel on go-live. |

## Watch for

- Drift between the four systems — a quarterly reconciliation should be queued once Janus has more than ~20 approved tools.
- Whether the gate criteria stay binary (4-of-4) or evolve into something weighted as the tool ecosystem grows.
- Cowork's clearance outcome — first real test of this process end-to-end.
