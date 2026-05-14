---
type: source
source_type: laptop
title: 05-JARGON-DECODER
slug: 05-jargon-decoder
created: 2026-05-07
captured_by: jehad-altoutou
audience: personal
original_path: /Users/jehad/Documents/janus-puls-onboarding/05-JARGON-DECODER.md
original_size: 6368
original_ext: .md
category: notes
extracted_with: text-copy
extracted_at: "2026-05-14T09:51:46Z"
sensitivity: dept
sensitivity_confidence: 0.90
sensitivity_reason: "PULS onboarding repo doc — jargon glossary; near-duplicate of skills references copy"
---

# 05-JARGON-DECODER

_Extracted from `Documents/janus-puls-onboarding/05-JARGON-DECODER.md` on 2026-05-14._

# 05 — Jargon Decoder

> Every buzzword in the deck, translated to plain English.

---

## Terms from the deck

| Term | What it actually means |
|---|---|
| **IMS** (Integrated Management System) | The 20 process documents + 11 policies + the dashboard, all together. The whole compliance machinery. |
| **PULS** (Predictive Unified Live System) | A live dashboard that shows the status of all 20 processes. **Doesn't exist yet — needs to be built.** |
| **First Voice** | A 6-question survey for each employee about their job. Becomes the seed data for their process document. |
| **Process Owner** | The one named C-level person responsible if that process fails. Accountable to the auditor. |
| **Certification Body** | An external company (BSI, TÜV, DNV, LRQA, SGS) that does the official ISO audit and issues the certificate. |
| **AI Systems Register** | A list of every AI tool/model the company uses (Claude API, etc.). Required by ISO 42001. |
| **Audit-ready** | Records and evidence are continuously captured so when the auditor shows up, no one panics. |
| **Internal audit** | When Janus audits itself before the external auditor arrives. ISO requires this. |
| **Nonconformity / CAPA** | A process failure (nonconformity) and the fix (Corrective And Preventive Action). |
| **Management Review** | A formal meeting where leadership reviews how the IMS is performing. ISO requires this at planned intervals. |
| **Predecessor / subsequent processes** | Process A's output is process B's input. The deck's slide 8 diagram shows this chain. |

---

## ISO standards explained

| Standard | What it certifies |
|---|---|
| **ISO 9001:2015** | Quality management. The original. Proves you have good, documented processes. |
| **ISO 27001:2022** | Information security. Proves you protect data, manage access, handle incidents. |
| **ISO 42001:2023** | AI management. Proves you govern AI responsibly — impact assessments, human oversight, lifecycle management. Brand new. |
| **ISO 27701:2025** | Privacy extension to 27001. Adds GDPR-style PII controls. Listed in the deck as "applicable, certifiable." |
| **ISO 20000-1:2018** | IT service management. ITIL-style operations. Listed as "applicable, certifiable." |
| **ISO 22301:2019** | Business continuity. [[disaster-recovery|Disaster recovery]]. Listed as "applicable, certifiable." |
| **ISO 27017** / **27018** | Cloud security + PII-in-clouds. Listed as "supporting" — not directly certified but applied. |
| **ISO 50001** / **41001** | Energy + facility management. **Client environment** — for the buildings Janus monitors, not Janus itself. |

---

## Frameworks and concepts

| Concept | Plain English |
|---|---|
| **PDCA — Plan-Do-Check-Act** | The repeating loop every ISO process must show: plan it, do it, check it worked, act on what you learned. Slide 7 of the deck. |
| **[[iso-9001-figure-1|ISO 9001 Figure 1]]** | The standard process diagram from slide 8. Sources → Inputs → Activities → Outputs → Receivers, with controls on top and resources below. **Every process document must follow this shape.** |
| **RACI** | Responsible · Accountable · Consulted · Informed. The role assignment per step in a process. |
| **Risk register** | A list of every risk to the business with likelihood, impact, mitigation, owner. ISO 27001 + 42001 both require one. |
| **AI Impact Assessment** | An ISO 42001 requirement — for every AI feature, document its purpose, risks, mitigations, oversight before deploying. |

---

## "What do they mean by..."

| Phrase from deck | What they mean |
|---|---|
| "One certificate, four jurisdictions" | Janus wants ONE ISO audit covering Dubai + Singapore + UK + others — not separate audits per country. The auditor inspects all sites under one engagement. |
| "Dubai HQ is the master" | Build the IMS once for Dubai. Then **copy** it (with local legal tweaks) to every new branch. Don't rebuild. |
| "Every new entity is a deployment, not a rebuild" | Same idea, restated. Treat the IMS like software — package it, deploy it, configure for local context. |
| "Live · Visible · Trusted" | The PULS dashboard's three properties. Live = real-time. Visible = anyone can inspect anything. Trusted = built on ISO standards. |
| "Continuous audit trail" | The PULS dashboard logs everything that happens, so there's always evidence. No "let me dig that up" moments. |
| "Pre-certification audit" | A dry-run audit. Janus hires an auditor (or an internal one) to find gaps **before** the real Certification Body comes in. |

---

## Acronym key

| Acronym | Stands for |
|---|---|
| IMS | Integrated Management System |
| PULS | Predictive Unified Live System |
| ISO | International Organization for Standardization |
| IEC | International Electrotechnical Commission (joint standards with ISO, e.g., ISO/IEC 27001) |
| KPI | Key Performance Indicator |
| RACI | Responsible · Accountable · Consulted · Informed |
| CAPA | Corrective And Preventive Action |
| PDCA | Plan-Do-Check-Act |
| MAS | Monetary Authority of Singapore (regulator) |
| IMDA | Infocomm Media Development Authority Singapore |
| ICO | Information Commissioner's Office (UK data protection regulator) |
| FCA | Financial Conduct Authority (UK financial regulator) |
| L3 / L5 | Document hierarchy levels — L3 = procedure, L5 = record. The deck mentions "55 records defined · L5". |
| GRC | Governance, Risk, Compliance — the category of platforms we're avoiding by building PULS |

---

## When you get stuck

**Confused about what a process is?** → Look at slide 8/9 of the deck (or the diagram in [01-START-HERE.md](./01-START-HERE.md)). Every process has the same shape: things go in, activities happen, things come out. That's it.

**Don't know who to ask?**
- ISO/compliance/process questions → ISO lead
- Ownership and budget questions → [[michael-bruck|Michael Bruck]]
- Tooling and drafting → Claude (me) or your own engineering instinct

**Worried this is huge?** It is. But: deck says "~6 months orientation," the whole company contributes (not just you), and the ISO lead drafts most of the documents from First Voice answers. Your direct authoring is much smaller than it looks.

**Worried you don't know ISO?** You don't need to. The ISO lead knows ISO. You know how Janus actually works. He needs your reality; you need his structure. That's the trade.

---

← Back to [README](./README.md)
