---
type: reference
title: IMS Process Owners Map
slug: ims-process-owners-map
created: 2026-05-08
updated: 2026-06-09
departments: [ai-office]
captured_by: jehad-altoutou
audience: [department]
migrated_from: personal-obsidian-vault (07 ISO IMS PULS)
tags: [iso, ims, ownership, raci]
status: draft-pending-michael-confirmation
---
# Process Owners Map

> Each of the 20 IMS process documents must have **one named C-level Process Owner** accountable for that process. This is the proposed map — **pending Michael's confirmation**.

---

## My proposed slots (Jehad)

| Code | Process | Why this is mine |
|---|---|---|
| **C1** | AI System Design & Development | I lead AI system design (AirWallex platform · Assessify · agentic layers) |
| **C2** | Software Development & Release | I run the dev → sandbox → IT handover pipeline (file [[janus-puls-onboarding|09]]) |
| **S2** | IT Infrastructure & Data Governance | I run the Hostinger VPS, n8n hosting decisions, Vercel/Neon stack — overlaps with IT department but I own the dev/sandbox side |

**Status:** Proposed in [[janus-puls-onboarding|repo file 02]] (today's email to Simon). Awaiting Michael's sign-off before formal acceptance.

---

## Likely top management slots

| Code | Process | Likely owner |
|---|---|---|
| M1 | Strategic Leadership & IMS Planning | Michael Bruck or Top Management |
| M5 | Management Review & Corrective Action | Top Management |

---

## Slots that need conversations

These don't have an obvious owner from Janus's current org chart:

| Code | Process | Needs decision |
|---|---|---|
| C3 | Partner Enablement & Certification | Who owns partner relationships? |
| C4 | Customer Onboarding & Activation | Customer-facing role lead |
| C5 | Service Delivery & Operations | IT department or Operations head? |
| C6 | Commercial Performance & Revenue | Sales / Commercial lead |
| C7 | Incident Management | Could be IT, could be split (security incidents to security, ops incidents to ops) |
| C8 | Management of Outsourced Services | Procurement or COO? |
| C9 | Procurement of External Providers | Procurement function (overlaps with [[janus-puls-onboarding|repo file 08]] — Tool Evaluation Procedure) |
| C10 | Partner & Client Training | Training / customer success function |
| S1 | Control of Documented Information | Could fall to Simon (the ISO lead) himself, or to a Quality Manager |
| S3 | Legal Compliance & Contract Management | Legal counsel |
| M2 | Integrated Risk Management | Risk officer or COO |
| M3 | Performance Monitoring & KPI | Could be the Quality Manager / Simon |
| M4 | Internal Audit | Internal auditor (must be independent from operations being audited) |
| A1 | Marketing & Brand Management | Marketing lead |
| A2 | Intellectual Property Management | Legal counsel + CTO |

---

## Authority hierarchy (per Simon's IMS-PRC-AI-001 v0.4)

Simon's doc names specific roles for the AI tool evaluation flow:

| Simon's role | Janus equivalent (proposed — needs Michael confirmation) |
|---|---|
| AI Department / Evaluator | Jehad |
| Head of AI Native | TBD |
| Head of AI Office | Michael Bruck |
| Department Head | Per requesting department |
| IT / Security / Legal | TBD per Janus org chart |
| Approval authority for Stage 4 (final AI tool decision) | Michael for routine · Top Management for high-risk |

This needs locking down with Michael — see [[ims-open-questions-for-simon]] item 4.

---

## Why ownership matters

**For ISO 9001:** Every process must have a single accountable owner. "Shared" or "TBD" ownership is an audit finding waiting to happen.

**For ISO 27001 and 42001:** Specific clauses require named owners for asset management, AI systems lifecycle, and risk acceptance. Without explicit ownership, those clauses can't be evidenced.

**For Janus operationally:** Without ownership clarity, every cross-process decision (e.g., "should this AI tool be approved?") gets escalated unnecessarily because no one is empowered to decide.

---

## Recommended next move

**Half-day with Michael** (this week) to lock:

1. Confirmation of my proposed slots (C1 · C2 · S2)
2. M1 and M5 owners
3. Authority hierarchy for AI tool approval (Stage 4 in [[janus-puls-onboarding|repo file 08]])
4. A pass through the "needs decision" list above — Michael probably knows who 60% of these should be

The remaining 40% gets routed to Simon for him to align with Janus's broader org chart.

---

## Related

- [[ims-process-documents]] — the full process list
- [[ims-open-questions-for-simon]] — decisions blocking ownership lock-in
- [[janus-puls-onboarding|repo file 02]] — the email that asks Michael for clarification

← Back to [[iso-ims-puls]]

## Authoritative register (2026-06-09)
The canonical 41-process owners list now lives in [[ims-process-register]] (source: [[reg-ims-process-register|REG-IMS-ProcessRegister v0.5]]). Conflict resolution: two owner claims → [[simon-tarskih|Simon]]; none → [[bonaventure-wong|Bonaventure]].
