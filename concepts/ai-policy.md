---
type: concept
title: AI Policy (Section 5 AI Charter — Janus's canonical governance)
slug: ai-policy
created: 2026-05-04
updated: 2026-05-22
captured_by: jehad-altoutou
departments: [ai-office, it-ops, hr, office-of-ceo, iso, marketing, finance, engineering, training]
status: active
sources: [section-5-ai-charter-policy-v2.1, 2026-05-04-bonaventure-michael-jehad-and-andrew-meeting]
related: [ai-native-mandate, ai-tool-evaluation-framework, ai-tool-evaluation, ai-registry, ai-policy-gate-approval, shadow-ai-prohibition, pilot-in-command, tool-tiers, sandbox-environment, iso-compliance-programme, coordination-leverage-model, builders-sellers-measurers]
---

# AI Policy

The **company-approved canonical AI policy** at Janus Digital — Section 5 of the AI Charter, currently **v2.1 (30 March 2026)**, owned by the AI Office, compliant with **ISO/IEC 42001:2023** (Artificial Intelligence Management System). Anchors the core principles and governance for everything the AIO does. Source of truth: [[section-5-ai-charter-policy-v2.1]].

Many wiki pages have been built as *derivatives* of this policy — concepts pulling out individual primitives, processes operationalising specific gates, decisions citing specific clauses. This page is the canonical narrative reference into which all of those derivatives flow.

## Structure (the 10 sections of Section 5)

| § | Title | What it codifies |
|---|---|---|
| **5.1** | The "AI Native" Mandate | Janus operates as an AI Native organisation; AI literacy is core competency; ISO/IEC 42001:2023 alignment. Captured in [[ai-native-mandate]]. |
| **5.2** | Strategic Pillars of AI Value | The three pillars: Operational Optimisation / Strategic Innovation / Institutional Intelligence. Each pillar has a measurable objective and a non-optional requirement. |
| **5.3** | Register of Approved AI Providers | The AI Registry exists; [[shadow-ai-prohibition|Shadow AI prohibited]]. Three [[tool-tiers]]: Core Infrastructure (universal), Functional Tools (department-specific), AI Office Infrastructure (below user-facing layer). Tool vs Infrastructure distinction governs which evaluation criteria apply. Data Sovereignty requirements (portability + documented API) are non-negotiable. Operationalised via [[ai-registry|/ai-registry]] skill. |
| **5.4** | AI Tool Evaluation & Approval Framework | Four sequential gates: Stage 1 Intake & Triage (binary) → Stage 2 Technical Qualification (mandatory + scored) → Stage 3 Sandbox & Domain Expert Evaluation → Stage 4 Approval, IT Handover & Registry Listing. Ongoing review triggers. Full operational detail in [[ai-tool-evaluation-framework]]. |
| **5.5** | The Sandbox Environment | Mandatory venue for Stage 3 evaluations + all internal AI development pre-production. **Only non-sensitive / synthetic data**; production / client / PII data strictly prohibited. Promotion to production is a deliberate, documented act. [[sandbox-environment]]. |
| **5.6** | Internal AI Solution Development | Pipeline: Intake → Discovery → Triage → PRD/SoW Sign-Off (hard gate) → Product Specification → Sandbox Build → Acceptance → Production & Monitor. Governance: **no build without signed PRD**; sandbox non-negotiable; scope control absolute; AIO does not provide general IT support. |
| **5.7** | Data Governance & Sovereignty | Four environment tiers: Public/Free-Tier AI Models (NONE permitted), Enterprise AI Instances (confidential data permitted under contractual data-privacy guarantee), Sandbox Environment (non-sensitive only), Recording & Transcription (consent required per GDPR / CCPA). |
| **5.8** | Risk Management & Impact Assessment | ISO/IEC 42005 + ISO/IEC 23894 alignment. Impact Assessments before any client/employee/decision-affecting workflow. **HITL for high-stakes decisions** (AI as decision-support, not decision-maker). Incident Reporting for extreme deviations + recurring failures + guardrail breaches. |
| **5.9** | Accountability & Transparency | [[pilot-in-command|Pilot in Command]] — employee remains professionally accountable. **No "AI Slop"** — raw/unverified/low-quality AI output prohibited. Transparency disclosure required for significantly-AI-generated comms. |
| **5.10** | Roles and Responsibilities | AI Office (central authority), Head of AI Office (Stage 4 approval), IT Department (security review + SSO/network/licence/L1 support), Team Leads (compliance + opportunity identification), Domain Experts (mandatory Stage 3 participation), AI Management Representative (ISO 42001 ops + Risk Register), All Employees (compliance). |

Compliance Notice: failure to comply — particularly with §5.7 Data Sovereignty, §5.5.2 Sandbox Data Restrictions, and §5.9 Accountability — may result in disciplinary action up to termination.

## Why this is the anchor

Many wiki artefacts depend on this policy — they extract one or more sections into more-detailed treatment. Cross-referenced for grep-ability:

- **[[ai-native-mandate]]** — extracts §5.1 (the Mandate) + §5.2 (three pillars). Was previously built against a `section-5-ai-charter-policy-ai-native-framework-30-march-2026-v2` slug; that slug is now superseded by [[section-5-ai-charter-policy-v2.1]] (Wiki source slug normalised).
- **[[ai-tool-evaluation-framework]]** — operationalises §5.4 with the full G1.x / G2.x / G3.x / G4.x criteria detail.
- **[[ai-tool-evaluation|/ai-tool-evaluation]]** — the skill executing the framework end-to-end.
- **[[ai-registry|/ai-registry]]** — operationalises §5.3 (the Register).
- **[[shadow-ai-prohibition]]** — extracts §5.3's "Shadow AI prohibited" rule.
- **[[tool-tiers]]** — extracts §5.3.1's three-tier classification (Core Infrastructure / Functional Tools / AI Office Infrastructure).
- **[[sandbox-environment]]** — extracts §5.5.
- **[[pilot-in-command]]** — extracts §5.9 (the human-accountability framing).
- **[[ai-policy-gate-approval]]** — the reusable governance process for §5.4 Stage 4 (Head of AI Office approval + IT handover).
- **[[iso-compliance-programme]]** — the operational programme for ISO/IEC 42001:2023 alignment named in §5.1.
- **[[coordination-leverage-model]]** — Michael's theoretical framework explaining *why* the policy is structured this way (the policy compliance layer; the framework is the operating economics).

## Cross-cutting non-negotiables (the things every Janus employee must know)

These are the policy's load-bearing one-liners — the rules with no exceptions:

1. **No Shadow AI.** Only tools in the AI Registry may be used. Submit a formal request via `#ai-internal-hub` Slack for tools not yet approved. (§5.3)
2. **No public free-tier LLMs with company data.** Ever. Use approved Enterprise instances only. (§5.7)
3. **HITL for high-stakes decisions.** AI is decision-support, never decision-maker. (§5.8)
4. **Pilot in Command.** Every employee is professionally accountable for output produced under their name, regardless of AI assistance. (§5.9)
5. **No AI Slop.** Raw, unverified, low-quality AI-generated content is prohibited from distribution. (§5.9)
6. **Recording / transcription requires consent.** GDPR / CCPA / local regulations apply. (§5.7)
7. **Sandbox is non-negotiable.** All third-party evaluation and internal AI development uses non-sensitive / synthetic data only. (§5.5)
8. **No build without a signed PRD.** Hard gate for internal AI solution development. (§5.6)

## ISO alignment surface

- **ISO/IEC 42001:2023** — Artificial Intelligence Management System (AIMS). The compliance standard cited in §5.1. Operational programme tracked under [[iso-compliance-programme]].
- **ISO/IEC 42005** — AI System Impact Assessment. Cited in §5.8 as the basis for the Impact Assessment requirement.
- **ISO/IEC 23894** — Risk Management for AI. Also cited in §5.8.

The ISO compliance programme operationalises these standards end-to-end; this policy is the company-facing Section-5 expression of them.

## Versioning

- **v2.1 (30 March 2026)** — current canonical. Filed at [[section-5-ai-charter-policy-v2.1]].
- **v2** (previously referenced via the slug `section-5-ai-charter-policy-ai-native-framework-30-march-2026-v2`) — superseded by v2.1.
- **v1 and earlier** — historical; not in the wiki.

When a new version supersedes v2.1, this concept page gets updated in place, the new version becomes the canonical source, and the previous version is retained under `status: superseded` for provenance.

## Watch for

- **v2.2 / v3.0 evolution.** Likely candidates for change: incorporation of CLAUDE.md v0.12 attribution-discipline language into §5.8 (Risk Management), explicit reference to the [[coordination-leverage-model]] as theoretical underpinning, integration of the proposed [[stack-composition-framework]] pre-G1 filter into §5.4.
- **ISO/IEC 42001 audit-readiness.** §5.10's AI Management Representative role is the operational lead for ISO 42001 surveillance; the AIO's structured-data discipline + AI Registry are direct compliance evidence.
- **Multi-jurisdiction extensions.** As Janus operates across Singapore / UK / additional ccTLDs, §5.7 (Data Governance) and §5.5 (Sandbox) need explicit cross-border data-residency clauses. Currently implicit.
