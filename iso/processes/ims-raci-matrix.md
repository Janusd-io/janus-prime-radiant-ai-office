---
type: process
title: IMS RACI Matrix (41 processes)
slug: ims-raci-matrix
created: 2026-06-09
updated: 2026-06-09
departments: [ai-office, ims-compliance]
captured_by: jehad-altoutou
audience: [department]
confidence: medium
document_status: DRAFT v0.1
sources: [reg-ims-process-register]
related: [ims-process-register, ims-digital-twin, iso-ims-puls, simon-tarskih, bonaventure-wong, michael-bruck, andrew-soane, euclid-wong, rosa-wu, ann-greed]
---

# IMS RACI Matrix (41 processes)

Responsibility assignment across all 41 IMS processes — the **next-step deliverable** the [[ims-process-register|Process Register]] calls for (*"v1.0 register → RACI matrix → pilot process card → mass roll-out"*). Owner: [[simon-tarskih|Simon]] (Head of IMS & Compliance).

**Status — DRAFT v0.1.** The **Accountable** and **Responsible** columns are populated from the register's proposed owners (real data). **Consulted** and **Informed** are a first-pass proposal to be confirmed with each process owner during process documentation (via the [[tmpl-light-process-discovery|Light discovery template]]). Vacant/Hiring roles act as future owner; `interim:` is who covers it today.

## RACI key
- **R — Responsible**: does the work.
- **A — Accountable**: owns the outcome (one per process; = the register's Process Owner).
- **C — Consulted**: two-way input before/during. By IMS convention [[simon-tarskih|Simon]] (IMS & Compliance) is a standing **C** on every process for IMS coherence; ISO-clause-relevant SMEs added per process.
- **I — Informed**: kept up to date one-way.

> Convention used here: **A = Process Owner** (from register). For governance/management processes whose owner is the CEO, the functional lead is **R**. Top management ([[bonaventure-wong|Bonaventure]]) is **I** on all (Management Review, M5). `[TBD]` = confirm during documentation.

## Governance (13)
| Code | Process | A (Accountable / Owner) | R (Responsible) | C (Consulted) | I (Informed) |
|---|---|---|---|---|---|
| G1 | Policy Management | [[simon-tarskih|Simon]] (Head IMS & Compliance) | Simon | Process owners; [[bonaventure-wong|Bonaventure]] | All staff |
| G2 | Org Roles & Authorities | Chief Talent Officer *[Hiring Aug 2026]* | interim: HR Mgr (Mariam) | Simon; [[bonaventure-wong|Bonaventure]] | All staff |
| G3 | Objectives Management | [[bonaventure-wong|Bonaventure]] (Global CEO) | Simon | Dept heads | All staff |
| G4 | Change Management | [[simon-tarskih|Simon]] | Simon | Affected owners; [[michael-bruck|Michael]] | Affected teams |
| G5 | Competence Management | HR Mgr (Mariam) | Mariam | Simon; dept heads | All staff |
| G6 | Awareness Management | HR Mgr (Mariam) | Mariam | Simon | All staff |
| G7 | Communications Management | [[andrew-soane|Andrew]] (CMO) | Andrew | Simon | All staff |
| G8 | Requirements for Products & Services | [[michael-bruck|Michael]] (Head AI Native) | Michael | Simon; Sales/CCO | Delivery teams |
| G9 | Nonconformity Management | [[simon-tarskih|Simon]] | Simon | Process owners; [[michael-bruck|Michael]] | [[bonaventure-wong|Bonaventure]] |
| G10 | AI Systems Impact Assessment | [[michael-bruck|Michael]] | Michael | Simon; [TBD legal/DPO] | [[bonaventure-wong|Bonaventure]] |
| G11 | AI Components/Assets/Data Mgmt | [[michael-bruck|Michael]] | AI Native team | Simon; IT | Delivery teams |
| G12 | AI Tools Approval for Use | [[michael-bruck|Michael]] | AI Evaluator; IT | Simon; Domain experts | Requesters (Slack) |
| G13 | AI Skills Development | [[michael-bruck|Michael]] | AI Native team | Simon | Product teams |

See [[ai-tool-evaluation-process-map|G12 process map]] for the worked example.

## Core (15)
| Code | Process | A (Accountable / Owner) | R (Responsible) | C | I |
|---|---|---|---|---|---|
| C1 | External AI Product — D&D | Chief AI Officer *[Hiring]* | op: [[michael-bruck|Michael]] | Simon; CTO | Sales; clients |
| C2 | Software Development & Release | CTO *[Vacant]* | Eng team | Simon; Michael | Delivery |
| C3 | Partner Enablement & Certification | Head Training & Cert *[Vacant]* | interim: [[euclid-wong|Euclid]] + [[rosa-wu|Rosa]] | Simon; CMO | Partners |
| C4 | Customer Onboarding & Activation | CCO *[Vacant]* | interim: [[euclid-wong|Euclid]] + [[rosa-wu|Rosa]] | Simon | Customers |
| C5 | Service Delivery & Operations | Chief Platform Officer *[Vacant]* | Ops team | Simon; CTO | Customers |
| C6 | Commercial Performance & Revenue | CCO *[Vacant]* | Sales | [[ann-greed|Ann Greed]] (Finance) | [[bonaventure-wong|Bonaventure]] |
| C7 | Incident Management | CTO *[Vacant]* | interim: [[michael-bruck|Michael]] | Simon; SecOps | Affected customers |
| C8 | Management of Outsourced Services | Head Global Facilities *[Vacant]* | [TBD] | Simon; CFO | Owners |
| C9 | Procurement of External Providers | CFO *[Hiring]* | interim: [[ann-greed|Ann Greed]] | Simon; Legal | Requesters |
| C10 | Partner & Client Training | Head Training & Cert *[Vacant]* | Training team | CMO | Partners; clients |
| C11 | Threat & Vulnerability Management | CTO *[Vacant]* (CISO fn) | SecOps | Simon | IT; owners |
| C12 | Internal AI Product ([[ims-digital-twin\|IMS Digital Twin]]) | [[michael-bruck|Michael]] | AI Native team | Simon | Dept owners |
| C13 | Subsidiary Mgmt & Regional Ops | [[bonaventure-wong|Bonaventure]] | Regional leads | Simon; Legal | All staff |
| C14 | Customer Satisfaction & Success | [[andrew-soane|Andrew]] (CMO) | Success team | C7/G9 owners | [[bonaventure-wong|Bonaventure]] |
| C15 | Marketing & Brand Management | [[andrew-soane|Andrew]] (CMO) | Marketing team | Simon | All staff |

## Support (8)
| Code | Process | A (Accountable / Owner) | R | C | I |
|---|---|---|---|---|---|
| S1 | Control of Documented Information | [[simon-tarskih|Simon]] | Simon | Process owners | All staff |
| S2 | IT Assets & Access Management | Head IT Administration *[Vacant]* | IT team | Simon; SecOps | All staff |
| S3 | Legal Compliance & Contract Mgmt | CLO *[Hiring Jul 2026]* | [TBD] | Simon | Owners |
| S4 | Physical & Environmental Security | Head Global Facilities *[Vacant]* | Facilities | Simon | Office staff |
| S5 | Network/Endpoint/Cloud SecOps | Head Infrastructure *[Vacant]* | SecOps | Simon; CTO | IT |
| S6 | Business Continuity & ICT Resilience | CTO *[Vacant]* | interim: Head Infra | Simon | Owners |
| S7 | Privacy & Data Subject Rights | CLO *[Hiring Jul 2026]* (DPO) | [TBD] | Simon; SecOps | Data subjects |
| S8 | Intellectual Property Management | CLO *[Hiring Jul 2026]* | [TBD] | Simon | Owners |

## Management (5)
| Code | Process | A (Accountable / Owner) | R | C | I |
|---|---|---|---|---|---|
| M1 | Strategic Leadership & IMS Planning | [[bonaventure-wong|Bonaventure]] | Simon | Dept heads | All staff |
| M2 | Integrated Risk Management | [[simon-tarskih|Simon]] | Simon | Process owners; [[michael-bruck|Michael]] | [[bonaventure-wong|Bonaventure]] |
| M3 | Performance Monitoring & KPI | [[bonaventure-wong|Bonaventure]] | Simon | Dept heads | All staff |
| M4 | Internal Audit | [[simon-tarskih|Simon]] | Simon | Auditees | [[bonaventure-wong|Bonaventure]] |
| M5 | Management Review & Corrective Action | [[bonaventure-wong|Bonaventure]] | Simon | Dept heads | All staff |

## Notes & next steps
- **Accountable/Responsible** = register's proposed owners (real). **Consulted/Informed** = first-pass proposal — confirm with each owner during process documentation; replace every `[TBD]` and validate the standing-Consulted convention with [[simon-tarskih|Simon]].
- Conflict resolution (per register): two owner claims → Simon; no owner claim → [[bonaventure-wong|Bonaventure]].
- Source of owners + clause refs: [[reg-ims-process-register|REG-IMS-ProcessRegister v0.5]]. Methodology: [[ims-digital-twin]]. Area map: [[iso-ims-puls]].
