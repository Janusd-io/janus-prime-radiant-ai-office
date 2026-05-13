---
type: department
title: IT and Operations
slug: it-ops
created: 2026-05-08
updated: 2026-05-12
departments: [it-ops]
status: active
owner: euclid-wong
sources: [2026-05-11-aio-standup-with-jehad]
related: [euclid-wong, andrey-timokhov, it-helpdesk-triage-bot, it-department-standup-pilot, ai-policy-gate-approval, peer-to-peer-mesh-federation-pattern, janus-prime-radiant-build, april-2026-aio-transcripts-recovery]
---

# IT and Operations

Janus's IT and Operations department — infrastructure, internal tooling, helpdesk, and the operational counterpart to AIO's policy-and-evaluation function. ITO holds production systems; AIO sandboxes new tools and hands them off to ITO once they pass the policy gate.

## People

- **[[euclid-wong]]** — Head of IT and Operations.
- **[[andrey-timokhov]]** — IT team member (mentioned as "Andre" in some earlier source files; canonical name andrey-timokhov).

## Prime Radiant instance

Queued. ITO is one of the more obvious second-wave instance candidates — the IT department standup pilot ([[it-department-standup-pilot]]) and the helpdesk triage bot project ([[it-helpdesk-triage-bot]]) already generate the kind of operational signal a Prime Radiant instance would compound. Spin-up sequencing: after Marketing pilot proves the federation pattern.

**First-pilot scope (clarified 2026-05-11):** [[euclid-wong|Euclid]]'s **project-management team**, not the IT sub-team itself. Per the 11 May AIO standup, the project-management team is the largest sub-team under Euclid, is technically savvy, and already operates with the kind of documentation discipline that an instance would compound (process docs for onboarding, vendor-management, infrastructure-ops). AIO to kick off at Wednesday meeting with Euclid. The IT sub-team (Andre + the new joiner) remains a separate, later target — IT is where production handover happens, so its instance follows the project-management one.

The [[peer-to-peer-mesh-federation-pattern|mesh federation pattern]] applies here: an `entities/departments/it-ops/` shared subfolder in the AIO vault, mirrored from the IT-Ops Prime Radiant once it stands up. Weekly AIO↔IT-Ops meetings (already a recurring cadence) land in that shared folder; both vaults' ingest passes process the content.

## Infrastructure layer (per three-layer model)

When the ITO instance stands up: production infrastructure inventory, runbooks, SLA frameworks, vendor contracts, security policies, ISO 9001 compliance evidence (overlaps with [[office-of-ceo]] / Bonaventure's ISO programme).

## AIO ↔ ITO interface

AIO sandboxes AI tools; ITO operates production. The handover is governed by the [[ai-policy-gate-approval]] process, with ISO 9001 as the compliance anchor and a two-step approval (AIO → joint → ITO production). The originating discussion was the 2026-04-30 AIO/ITO compliance reset standup — currently un-filed because the April 2026 AIO standup entries were lost from Notion. Will be reconstructed via [[april-2026-aio-transcripts-recovery]] from the raw [[fireflies]] transcript when that project runs.

## Key projects

[[it-helpdesk-triage-bot]] · [[it-department-standup-pilot]]

## Cross-instance federation

ITO federates closely with [[ai-office]] (sandbox-to-production handover for every AI tool), [[office-of-ceo]] (ISO compliance), and [[finance]] (vendor contracts and infrastructure budgets).
