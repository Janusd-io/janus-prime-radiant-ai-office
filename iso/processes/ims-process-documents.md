---
type: reference
title: 20 IMS Process Documents
slug: ims-process-documents
created: 2026-05-08
updated: 2026-06-09
departments: [ai-office]
captured_by: jehad-altoutou
audience: [department]
migrated_from: personal-obsidian-vault (07 ISO IMS PULS)
tags: [iso, ims, processes]
---
# 20 IMS Process Documents (+ 11 IMS Manual policies)

> The full list of process documents that must exist in Notion to satisfy the IMS. Each document follows the [[three-iso-standards|ISO 9001 Figure 1 schematic]] with 7 sections (Controls · Inputs · Activities & control points · Monitoring & measurement · Resources · Outputs & records · Process Owner).

---

## CORE — how Janus delivers value (10)

| Code | Process | Plain-English description | Likely owner |
|---|---|---|---|
| **C1** | AI System Design & Development | How AI features get designed and built | **Jehad** (proposed) |
| **C2** | Software Development & Release | How code ships to production | **Jehad** (proposed) |
| C3 | Partner Enablement & Certification | How partners are onboarded and qualified | TBD |
| C4 | Customer Onboarding & Activation | How new customers go live | TBD |
| C5 | Service Delivery & Operations | How the live service is run day-to-day | TBD |
| C6 | Commercial Performance & Revenue | Sales pipeline and revenue management | TBD |
| C7 | Incident Management | How things-going-wrong are handled | TBD |
| C8 | Management of Outsourced Services | Managing third parties doing work for us | TBD |
| C9 | Procurement of External Providers | How we buy tools, services, subcontractors | TBD |
| C10 | Partner & Client Training | How we train people who use our stuff | TBD |

---

## SUPPORT — what keeps the business running (3)

| Code | Process | Plain-English description | Likely owner |
|---|---|---|---|
| S1 | Control of Documented Information | How documents are stored, versioned, retired | TBD |
| **S2** | IT Infrastructure & Data Governance | Servers, networks, data classification | **Jehad** (proposed) |
| S3 | Legal Compliance & Contract Management | Contracts, regulatory compliance | TBD |

---

## MANAGEMENT — leadership and oversight (5)

| Code | Process | Plain-English description | Likely owner |
|---|---|---|---|
| M1 | Strategic Leadership & IMS Planning | Setting direction · IMS planning · top management commitments | Michael / Top Management |
| M2 | Integrated Risk Management | Identifying and handling risks across the IMS | TBD |
| M3 | Performance Monitoring & KPI | Measuring how things are going | TBD |
| M4 | Internal Audit | Auditing ourselves before the auditor does | TBD |
| M5 | Management Review & Corrective Action | Leadership reviews + fixing problems | Top Management |

---

## ADDITIONAL (2)

| Code | Process | Plain-English description | Likely owner |
|---|---|---|---|
| A1 | Marketing & Brand Management | How the brand is run | TBD |
| A2 | Intellectual Property Management | Managing IP, patents, trademarks | TBD |

---

## IMS Manual — 11 policy-level documents

These sit **above** the 20 process documents — they're company-wide policies, not detailed procedures.

| # | Policy |
|---|---|
| 1 | Policy Management |
| 2 | Management of Organisational Roles and Authorities |
| 3 | Objectives Management |
| 4 | Change Management |
| 5 | Competence Management |
| 6 | Awareness Management |
| 7 | Communications Management |
| 8 | Management of Requirements for Products and Services |
| 9 | Management of Nonconforming Outputs |
| 10 | AI Systems Impact Assessment |
| 11 | AI Systems Data Management |

These are **Simon's job to draft, not mine** — unless Michael delegates one of the AI-specific ones (10 or 11) to me, which would be reasonable given my role.

---

## What goes inside each of the 20 process documents

Per Simon's deck (slide 9), every document must have these 7 sections:

| # | Section | Content |
|---|---|---|
| 1 | **Controls** | Which laws / policies / ISO clauses apply (UAE · SG · UK + ISO clause refs) |
| 2 | **Inputs** | Trigger events · preceding process outputs · client requests · data feeds · scheduled intervals |
| 3 | **Activities & control points** | Step-by-step sequence · decision points · responsibilities · escalation rules · approval gates · RACI per step |
| 4 | **Monitoring & measurement** | KPIs per process · target values · measurement frequency · PULS dashboards · automated alerts |
| 5 | **Resources** | Process Owner · team roles · systems · tools · budget · training requirements |
| 6 | **Outputs & records** | Deliverables to next process or client · documented evidence · mandatory records retained in Notion · audit-ready |
| 7 | **Process Owner** | One named C-level person · accountable for performance and compliance |

---

## Mapping to Simon's IMS-PRC codes

Simon uses formal process IDs: `IMS-PRC-AI-001` (Management of Internal AI Tools) is his first.

We've proposed in our [[janus-puls-onboarding|repo file 10]]:

| Repo file | Proposed code | Maps to which process |
|---|---|---|
| 07 Meeting → Task → Build | IMS-PRC-AI-002 | Implementation of step 1 of C1/C2/S2 |
| 08 Tool Evaluation Procedure | **IMS-PRC-AI-001** (matches Simon) | C9 Procurement + IMS Manual #10 + #11 |
| 09 Platform Development Process | IMS-PRC-AI-003 | Becomes the Activities section of C2 |

---

## Status — what's drafted today

| Process | Drafted? | Where |
|---|---|---|
| C1 / C2 / S2 (combined Activities section) | ✅ Drafted at the Activities level (5-step real flow) | Repo file 04 |
| C9 + IMS Manual #10 + #11 | ✅ Drafted as IMS-PRC-AI-001 candidate | Repo file 08 |
| C2 (full design and development cycle) | ✅ Drafted with Assessify worked example | Repo file 09 |
| Activity 1 of C1/C2/S2 (requirements gathering) | ✅ Drafted | Repo file 07 |
| Everything else (C3-C10 except C9, S1, S3, M1-M5, A1, A2) | ❌ Not drafted | Awaiting Process Owner assignment |

See [[ims-process-owners-map]] for the ownership picture and [[ims-open-questions-for-simon]] for what's blocking the rest.

---

## Related

- [[three-iso-standards]] — what each clause requires
- [[ims-process-owners-map]] — assignment + escalation
- [[janus-puls-onboarding|GitHub repo]] — all drafted documents

← Back to [[iso-ims-puls]]

## Authoritative source set (2026-06-09)
Superseded/expanded by the real ISO/IMS document set from Simon — see [[ims-digital-twin]] and `iso/sources/`: [[ims-readiness-assessment-2026-06-08]], [[reg-ims-process-register]], [[ims-clause-comparison-matrix]], [[diag-ims-visualization-standard]], [[tmpl-unified-process-design]], [[proc-ims-ai-tool-evaluation]].
