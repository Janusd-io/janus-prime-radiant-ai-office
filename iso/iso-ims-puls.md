---
type: moc
title: ISO / IMS / PULS
slug: iso-ims-puls
created: 2026-05-08
updated: 2026-06-09
departments: [ai-office]
captured_by: jehad-altoutou
audience: [department]
migrated_from: personal-obsidian-vault (07 ISO IMS PULS)
tags: [iso, ims, puls, compliance, governance]
status: active
---
# 🏛️ ISO · IMS · PULS — Map of Content

> Entry point for everything related to Janus Digital's ISO certification programme: the Integrated Management System (IMS), the PULS dashboard, the 20 process documents, and the gap analysis against Simon's drafts.
> All deliverables-as-code live in the **[[janus-puls-onboarding|GitHub repo]]**. This section of the vault is the navigational + conceptual layer.

---

## 🎯 At a glance

| Field | Value |
|---|---|
| **Goal** | Get certified against **ISO 9001 + ISO 27001 + ISO 42001** on **one** certificate covering Dubai HQ + Singapore + UK + future entities |
| **The dashboard we're building** | **PULS** — Predictive Unified Live System |
| **Total IMS process documents needed** | **20** (Core 10 · Support 3 · Management 5 · Additional 2) + 11 IMS Manual policies |
| **My direct ownership (proposed)** | C1 AI System Design & Development · C2 Software Development & Release · S2 IT Infrastructure & Data Governance |
| **ISO Lead** | Simon (working with us on `IMS-PRC-AI-001` v0.4) |
| **Strategic owner** | Michael Bruck (AI Projects lead) |
| **Target rollout** | 10 entities this year · 20/yr from 2027 · ~6 months orientation |

---

## 📍 Navigate this section

- [[puls-programme]] — what we're building and why · the 60-second story
- [[three-iso-standards]] — 9001 · 27001 · 42001 explained · plus the 7 supporting/client-side standards
- [[ims-process-documents]] — full list with status, owners, IMS-PRC codes
- [[ims-process-owners-map]] — who owns what · my proposed slots flagged
- [[ims-open-questions-for-simon]] — pending decisions blocking progress
- [[janus-puls-onboarding]] — link out to GitHub + one-line summary of each of the 11 docs
- [[ims-enrolment]] — `/ims-enrolment` Claude Desktop skill that walks any department through ISO documentation · ships with AI Department worked example

---

## 🔗 Related sections elsewhere in the vault

- [[assessify|Assessify]] — the worked example for `09 Platform Development Process` in the repo
- [[standup|/standup skill]] — implements `07 Meeting → Task → Build` workflow
- [[assessify|/assessify-hr skill]] — MCP driver for Assessify, referenced from the Platform Development Process
- AirWallex Finance Intelligence Platform — multi-entity pattern that mirrors PULS multi-entity needs
- [[jehad-altoutou|Jehad's profile]] — role context for First Voice answers
- [[saas-default-stack|SaaS Default Stack]] — what the PULS dashboard will be built on

---

## 🚦 Status snapshot — 11 May 2026

> Last sync: 11 May 2026. No material changes since 8 May — items below are unchanged from the previous review.

| Item | Status | Days pending |
|---|---|---|
| Read Simon's IMS deck and respond to him | ✅ Done — responded; awaiting reply | — |
| First Voice answers drafted | ✅ Done — file 06 in repo | — |
| Tooling proposal for Step 4 | ✅ Drafted in file 04 | — |
| Process Owner confirmation from Michael | ⚠️ Pending — blocking Tasks 4-5 | **3 days** |
| Meeting → Task workflow documented | ✅ Done — file 07 | — |
| Tool Evaluation Procedure documented | ✅ Done — file 08 | — |
| Platform Development Process documented | ✅ Done — file 09 (Assessify worked example) | — |
| Gap analysis vs Simon's IMS-PRC-AI-001 v0.4 | ✅ Done — file 10 (10 specific gaps identified) | — |
| Reply to Simon on gap analysis + HR architecture | ⚠️ Pending — drafted but not sent | **3 days** |
| Half-day with Michael on Process Ownership | ⚠️ Not scheduled | **3 days** |
| Doc 08 v0.5 aligned to Simon's structure | ⏳ Blocked until Simon replies | — |
| PULS dashboard MVP build | ⏳ Phase 2 — after tooling decision locked | — |

### 🔔 Nudges

Three items have been sitting for 3 days. If they're stuck on someone else, that's normal — but if they're stuck on you:

- **Send the gap-analysis reply to Simon** (drafted in [[janus-puls-onboarding|repo file 10]] sections 5 + 6). It unblocks the doc 08 v0.5 work.
- **Ping Michael for the 30-min ownership conversation** — see [[ims-process-owners-map]] for the questions to ask. Without this, the rest of the IMS docs can't be drafted with named owners.
- **Send the First Voice form** ([[janus-puls-onboarding|repo file 06]]) if Simon hasn't formally requested it yet — proactive send is fine and signals momentum.

---

## 🧭 How to use this section

When ISO/IMS/PULS comes up:

1. Start at this index
2. Pick the relevant note (programme overview · standards · process list · ownership · open questions)
3. For deep procedural content, jump to [[janus-puls-onboarding|the GitHub repo]] — that's where the full process documents live (with Mermaid diagrams, ISO clause maps, KPIs, etc.)
4. Cross-link any new ISO-related note back to this index

---

## 🔁 Maintenance

Update this index when:

- Any item in the status snapshot changes state
- Simon assigns or changes Process Ownership
- A new process document is drafted in the repo
- A new ISO standard becomes relevant

Run `/brain status` periodically to ensure links are intact.

---

← Back to [[index]]

## Related processes
- [[ims-enrolment-interview-flow]] — the IMS enrolment interview flow.
- [[ims-process-documents]] · [[ims-process-owners-map]] · [[ims-open-questions-for-simon]]

## IMS document set — ingested from Simon, 2026-06-09

The [[ims-digital-twin|IMS Digital Twin]] build. Full-fidelity source documents under `iso/sources/`; synthesised knowledge pages below.

**Methodology & tooling**
- [[ims-digital-twin]] — the two-template, AI-translated digital-twin approach (core concept).
- [[ims-documentation-hierarchy]] — L1–L6 documentation pyramid (policies → manual/maps → procedures → forms → records → external docs); received from Simon 2026-06-10 ([[ims-doc-system-hierarchy|source]]).
- [[unified-process-design-template]] — technical + light ([[tmpl-unified-process-design]] / [[tmpl-light-process-discovery]]).
- [[ims-process-visualization-standard]] — diagram notation + 19-rule AI build prompt.

**Scope & mapping**
- [[ims-process-register]] — 41 processes (G13/C15/S8/M5) + owners ([[reg-ims-process-register|source]]).
- [[ims-raci-matrix]] — responsibility assignment (R/A/C/I) across the 41 processes.
- [[ims-clause-comparison-matrix]] — ISO 9001/27001/42001 clauses × 41 processes (source).
- [[three-iso-standards]] — the three standards overview.

**Pilot**
- [[ai-tool-evaluation-process-map]] (+ [[ai-tool-evaluation-diagram|diagram]]) — first end-to-end documented process.

**Status** — [[ims-readiness-assessment-2026-06-08|build progress report]] (2026-06-08): foundation complete, all DRAFT; next = validate pilot, prove Light→Technical translation, prioritise the sprint. Owner: [[simon-tarskih|Simon]] (Head of IMS & Compliance).

**AIO proposal (2026-06-10, awaiting Michael)** — [[iso-skill-to-platform-staged-path]]: staged skill → dashboard → interactive platform path; AIO proves the Light→Technical translation and merges [[ims-enrolment]] with Simon's Light template (see [[2026-06-10-enrolment-approaches-converge-light-template-vs-ims-enrolment-skill|convergence pulse]]).

