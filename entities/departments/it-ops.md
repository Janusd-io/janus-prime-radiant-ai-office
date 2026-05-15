---
type: department
title: IT, Project Management, and Operations
slug: it-ops
created: 2026-05-08
updated: 2026-05-15
departments: [it-ops]
status: active
owner: euclid-wong
sources: [2026-05-11-aio-standup-with-jehad, 2026-05-13-aio-pm-meeting, 2026-05-14-pm-workflow-walkthrough-lysander]
related: [euclid-wong, andrey-timokhov, dhyey-mehta, it-helpdesk-triage-bot, it-department-standup-pilot, ai-policy-gate-approval, peer-to-peer-mesh-federation-pattern, janus-prime-radiant-build, april-2026-aio-transcripts-recovery, project-management-digital-delivery-workflow, lysander-liu, rosa-wu, spike-zhao]
---

# IT, Project Management, and Operations

Janus's combined department covering **three teams** under [[euclid-wong|Euclid]]: **IT** (infrastructure, internal tooling, helpdesk), **Project Management** (project delivery), and **Operations** (operational backbone). The combined function is the operational counterpart to AIO's policy-and-evaluation function — ITO holds production systems and the project delivery discipline; AIO sandboxes new tools and hands them off through the policy gate.

> **Naming note (2026-05-14):** The wiki slug stays `it-ops` for stability and inbound-reference continuity, but Euclid's actual remit is broader. The display title now reflects the three teams. The `entities/departments/` vocabulary will eventually need to consider whether Project Management warrants its own department entity once the Prime Radiant rollout proves out — for now, kept under IT-Ops since Euclid runs all three.

## People

- **[[euclid-wong]]** — Head of all three teams (IT + Project Management + Operations).
- **IT team:**
  - **[[andrey-timokhov]]** — IT team member (mentioned as "Andre" in some earlier source files; canonical name andrey-timokhov).
  - **[[dhyey-mehta|Dhyey Mehta]]** — recent IT-team joiner; first wiki touchpoint = 2026-05-15 Singapore strategy alignment session. Role detail TBD pending enrichment.
- **Project Management team** (titles confirmed 2026-05-14):
  - **[[rosa-wu|Rosa Wu]]** — **Co-head of Project Management** (with [[euclid-wong|Euclid]] at the senior level).
  - **[[lysander-liu|Lysander Liu]]** — **Head of Project Management** (operational lead under the Euclid + Rosa co-head structure); authored the canonical [[project-management-digital-delivery-workflow|28-phase workflow]].
  - **[[spike-zhao|Spike Zhao]]** — **Digital modeling engineer** (delivery side; works in Phases 16–18 of the workflow).
- **Operations team:** roles TBC; full team detail surfaces once Deel is in place.

## Prime Radiant instance

Queued. ITO is one of the more obvious second-wave instance candidates — the IT department standup pilot ([[it-department-standup-pilot]]) and the helpdesk triage bot project ([[it-helpdesk-triage-bot]]) already generate the kind of operational signal a Prime Radiant instance would compound. Spin-up sequencing: after Marketing pilot proves the federation pattern.

**First-pilot scope (clarified 2026-05-11; refined 2026-05-14):** [[euclid-wong|Euclid]]'s **Project Management team** is pilot #2 across all Prime Radiant rollouts (after [[andrew-soane|Andrew]] / Marketing). Per the 11 May AIO standup, this team is the largest under Euclid, is technically savvy, and already operates with the kind of documentation discipline that an instance would compound. The 14 May walkthrough with Lysander captured the [[project-management-digital-delivery-workflow|full 28-phase workflow]] as the canonical content the instance initialises against. The IT and Operations teams (Andrey + others) remain a separate, later target — IT is where production handover happens, so its instance follows the Project Management one.

The [[peer-to-peer-mesh-federation-pattern|mesh federation pattern]] applies here: an `entities/departments/it-ops/` shared subfolder in the AIO vault, mirrored from the IT-Ops Prime Radiant once it stands up. Weekly AIO↔IT-Ops meetings (already a recurring cadence) land in that shared folder; both vaults' ingest passes process the content.

## Infrastructure layer (per three-layer model)

When the ITO instance stands up: production infrastructure inventory, runbooks, SLA frameworks, vendor contracts, security policies, ISO 9001 compliance evidence (overlaps with [[office-of-ceo]] / Bonaventure's ISO programme).

## AIO ↔ ITO interface

AIO sandboxes AI tools; ITO operates production. The handover is governed by the [[ai-policy-gate-approval]] process, with ISO 9001 as the compliance anchor and a two-step approval (AIO → joint → ITO production). The originating discussion was the 2026-04-30 AIO/ITO compliance reset standup — currently un-filed because the April 2026 AIO standup entries were lost from Notion. Will be reconstructed via [[april-2026-aio-transcripts-recovery]] from the raw [[fireflies]] transcript when that project runs.

## Key projects

[[it-helpdesk-triage-bot]] · [[it-department-standup-pilot]]

## Cross-instance federation

ITO federates closely with [[ai-office]] (sandbox-to-production handover for every AI tool), [[office-of-ceo]] (ISO compliance), and [[finance]] (vendor contracts and infrastructure budgets).
