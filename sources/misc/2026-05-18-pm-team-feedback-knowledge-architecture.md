---
type: source
title: "PM team feedback on Prime Radiant knowledge architecture (Lysander → Michael, 2026-05-18)"
slug: 2026-05-18-pm-team-feedback-knowledge-architecture
created: 2026-05-19
updated: 2026-05-19
source_type: article
source_format: html
source_authors: [lysander-liu]
source_publisher: Janus Digital — Project Management team
source_published: 2026-05-18
source_ref: KSR-PM-2026-0514-001 / COR-PM-2026-0514-001
binary: 2026-05-18-pm-team-feedback-knowledge-architecture.html
---

# PM team feedback — Prime Radiant knowledge architecture (2026-05-18)

Bilingual HTML deck (Chinese default + English toggle) sent by [[lysander-liu|Lysander Liu]] on behalf of the Janusd PM team to Michael. Substantive response to the Project Management Prime Radiant standup proposal — answers Michael's 8 open questions, surfaces a critical Stage-5/G4 correction, and proposes a refined A/B/C three-pillar knowledge architecture.

Document references: **KSR-PM-2026-0514-001** + **COR-PM-2026-0514-001**.

## Part A — 8 questions answered

| # | Question | PM team response |
|---|---|---|
| 1 | Where do portfolios sit (above products)? | Use **Obsidian tags** (`#portfolio/xxx`) — not physical directories — at this stage. Re-evaluate at Month 3. |
| 2 | Where do programmes live? | Same as Q1 — tags (`#programme/xxx`), evaluated alongside portfolio at Month 3. Don't add a physical programme layer prematurely. |
| 3 | Where does vendor / third-party content live? | `A-PMO/3-Resources/` split as `hardware-vendors/`, `construction-vendors/`, `delivery-partners/`. Cross-project vendor credentials, compliance, history at PMO level. Project-specific vendor contacts + contract details stay in `B-projects/<project>/planning/` or `raid/`. |
| 4 | Phases where naming doesn't match? | 28-phase **content** is endorsed (PM team: 9/10). One critical **stage-grouping** error on Stage 5 — see correction below. Minor Stage 3/4 split also flagged. |
| 5 | Confirm scope & sponsor | ✅ **Confirmed.** Euclid Wong as sponsor across his three teams (IT/PM/Operations); PM as pilot #2 after Marketing. |
| 6 | Pick one project to backfill | **KSC project** — richest historical material, full G1–G4 coverage, highest team familiarity. ✅ **Confirmed.** |
| 7 | Personal vaults deferred | ✅ **Fully agreed.** Team brains first; personal-vault → team-vault flow rules need a separate design conversation. Not blocking. |
| 8 | AIO × PM federation | ✅ **Agreed as a separate conversation.** GitHub substrate move means the previous mesh-subfolder pattern needs redesign. Suggest starting during Week 3-4 synthesis window. Not blocking. |

## The critical correction — G1-G4 gate system, no Stage 5

**Janusd uses a strict four-gate system (G1-G4). There is no Stage 5.** The "Stage 1–5" labels used in [[2026-05-14-project-management-prime-radiant-standup-proposal|Michael's standup proposal]] map a generic PM framework onto Janusd's actual gate structure — fine for content, factually wrong on stage grouping.

| Gate | Name | Phases | Notes |
|---|---|---|---|
| **G1** | Pre-Sales Review | Phases 1–4 → G1 pass | |
| **G2** | Planning Readiness | Phases 5–8 → G2 pass | |
| **G3** | Execution Readiness | Phases 9–22 | G3 triggers parallel flows: DC / DD / DS / DY / DB |
| **G4** | Acceptance & Handover | **Phases 23–28 = G4 *prerequisites*** | Not post-G4 closeout activities |

**Phases 23–28 are NOT "Closure."** They are G4 prerequisites — commissioning + handover gate inputs:

- **UAT (phase 24) = G4 criterion DT002**
- **Training (phase 25) = G4 criterion DU001**
- **Trial run completion = G4 trigger condition**

**True "Project Closeout" is absent from the 28 phases.** After G4 passes, Janusd needs lessons-learned capture + project archival + PMO retrospective. None of those are in the 28 phases — they need their own placeholder (`closeout/`, post-G4) in the vault structure.

### Stage 3/4 split (minor)

The boundary between Michael's "Stage 3" (phases 9–17) and "Stage 4" (phases 18–22) doesn't correspond to any Janusd gate — it's editorial grouping. PM team recommends:

- **Merge** into "G3 Execution" covering phases 9–22, OR
- **Annotate** that the 9–17 vs 18–22 split has no gate significance.

## Part B — Recommended architecture (A/B/C three pillars)

```
janusd-platform-delivery/
├── A-PMO/                              ← Governance & Knowledge Layer
│   ├── 1-committee-decisions/          [source: committee meetings + Fireflies]
│   │   ├── pre-sales-approvals/
│   │   ├── planning-reviews/
│   │   ├── change-decisions/
│   │   └── acceptance-closeout/
│   ├── 2-pm-knowledge/                 [source: PMO admin]
│   │   ├── delivery-process/           # G1-G4 SOP, 28-phase docs
│   │   ├── training-materials/         # ADDIE + Kirkpatrick templates
│   │   ├── pm-methodology/             # PMP, PGMP, soft skills
│   │   └── delivery-solutions/         # ← Michael's products/ relocated here
│   ├── 3-resources/                    [source: PMO + project PMs + vendors]
│   │   ├── team-allocation/
│   │   ├── hardware-vendors/
│   │   ├── construction-vendors/
│   │   └── delivery-partners/
│   ├── 4-pmo-dashboard/ ★ NEW          [source: auto-read from B-Projects + Monday.com]
│   │   ├── health-metrics/             # health indicators across active projects
│   │   ├── alerts/                     # auto-warnings (overdue / RAID escalations / gate approaching)
│   │   └── portfolio-view/             # cross-project portfolio view
│   └── 5-lessons-learned/              [source: each project PM, mandatory pre-G4]
│
├── B-projects/                         ← Active project workspace
│   └── <project>/                      [source: project PM, access-controlled]
│       ├── charter.md
│       ├── scope.md
│       ├── G1-initiation/              # phases 1–4 (pre-sales → G1)
│       ├── G2-planning/                # phases 5–8 (G1 → G2)
│       ├── G3-execution/               # phases 9–22 (G2 → G3 → execution)
│       │   ├── entry-readiness/        # phases 9–11
│       │   ├── parallel-tracks/        # phases 12–17 (DC/DD/DS/DY/DB)
│       │   └── system-delivery/        # phases 18–22
│       ├── G4-commissioning-handover/  # phases 23–28 (G4 prerequisites) ← was "closure"
│       ├── closeout/                   # post-G4 → links to A-5 lessons learned
│       ├── raid/
│       ├── meetings/
│       └── decisions/
│
└── C-products/                         ← Janusd Software Product Catalogue
    │                                   [source: solutions team]
    ├── WEB-APC/
    ├── WEB-AMC/
    ├── WEB-DTX/
    ├── APP-APC/
    ├── APP-DTX/
    ├── industry-solutions/
    └── industry-cases/
```

### Important renaming

**Michael's `products/`** (cross-project reusable delivery solutions) → **rename to `delivery-solutions/`** and move into **A-2 PM knowledge**, to avoid confusion with **C-products** (Janusd's actual software product catalogue — `WEB-APC`, `APP-DTX`, etc. — a completely different concept).

### ★ PMO Dashboard (A-4) — net new

Not in Michael's original proposal. PM team adds this as the auto-fed cross-project surface — health metrics, alerts (overdue / RAID-escalation / gate-approaching), and a portfolio view. Data flows from B-projects + Monday.com on a scheduled refresh + event-triggered alerts.

### Data ownership table (verbatim)

| Domain | Data source | Owner | Method |
|---|---|---|---|
| **A-1** Committee Decisions | Committee meeting records | Meeting scribe | Fireflies auto + manual review, archive within 24h |
| **A-2** PM Knowledge | PMO knowledge base | PMO admin | Manual update on process change |
| **A-3** Resources | PMO, project PMs, vendors | PMO admin | Update on project start or resource change |
| **A-4 ★** PMO Dashboard | B-Projects + Monday.com | Auto-generated | Scheduled refresh + event-triggered alerts |
| **A-5** Lessons Learned | Project PM submissions | Project PM | Mandatory pre-G4 gate submission |
| **B-Projects** | Project site data | Project PM | Continuous update, access-controlled |
| **C-Products** | Product documentation | Solutions team | Maintain on product version update |

### Day 1 README claim (mandatory)

> **Monday.com = Task SSOT; Prime Radiant = Knowledge SSOT. Complementary, not substitutes for each other.**

PM team's framing — adopt this as a load-bearing statement in the PM Prime Radiant's vault README on Day 1.

## Six items for Michael's confirmation

1. **A/B/C three-pillar structure overall** — endorse the A-PMO / B-Projects / C-Products split?
2. **Q1/Q2** — Portfolio + Programme via Obsidian tags now, evaluate physical directories at Month 3 — agreed?
3. **Q3** — Vendor content into A-3 Resources rather than top-level — agreed?
4. **(MANDATORY) Phases 23–28 reclassified as G4 prerequisites** — folder renamed `G4-commissioning-handover/`, not `closure/`. Structural factual correction.
5. **Q7** — Personal vaults deferred (record-only confirmation).
6. **Q8** — AIO × PM federation as separate conversation, not blocking PM standup (record-only confirmation).

## Why this matters

- **Confidence boost on the workflow capture itself.** The PM team formally endorses the 28-phase content as 9/10 accurate. The standup proposal's substantive content is validated by the people who actually own the discipline.
- **One factual correction with structural consequences.** The Stage 5 → G4 prerequisites fix is non-trivial — it changes where phases 23–28 live in the vault folder structure and which gate criteria they satisfy. This is the kind of correction that *had to* come from the PM team; the wiki-side could not have inferred it from the workflow walkthrough alone.
- **PM team is actively engaged.** This deck shows ownership of the rollout from the PM side — substantive, structured, signed, referenced. Strong signal that the Project Management Prime Radiant rollout is on track.
- **Architecture refinement adds the PMO Dashboard** (A-4) — auto-fed from B-projects + Monday.com — which is the missing piece for cross-project portfolio visibility. Worth adopting.

## Wiki actions taken (2026-05-19)

- This source filed at `sources/misc/2026-05-18-pm-team-feedback-knowledge-architecture.{html,md}`.
- [[project-management-digital-delivery-workflow|PM digital delivery workflow process page]] updated to incorporate the G1-G4 gate framing + reclassify phases 23–28 as G4 prerequisites + flag the post-G4 closeout gap.

## Related

- [[lysander-liu]] — author / sender
- [[project-management-digital-delivery-workflow]] — the workflow capture being responded to
- [[2026-05-14-project-management-prime-radiant-standup-proposal|standup-proposal HTML deck]] — the artefact this is feedback on
- [[lessons/2026-05-14-project-management-document-management-gap|document-management-gap lesson]] — adjacent context
- [[euclid-wong]] — sponsor confirmed across the three teams
