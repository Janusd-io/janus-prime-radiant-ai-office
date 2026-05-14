---
type: source
source_type: laptop
title: ai_tool_evaluation_framework
slug: ai-tool-evaluation-framework
created: 2026-04-23
captured_by: jehad-altoutou
audience: personal
original_path: /Users/jehad/Desktop/ai_tool_evaluation_framework.md
original_size: 21558
original_ext: .md
category: notes
extracted_with: text-copy
extracted_at: "2026-05-14T09:51:43Z"
sensitivity: dept
sensitivity_confidence: 0.92
sensitivity_reason: "Formal Janus AI Tool Evaluation & Approval Framework (DRAFT v0.1, Office of the COO) — dept-shareable governance document."
---

# ai_tool_evaluation_framework

_Extracted from `Desktop/ai_tool_evaluation_framework.md` on 2026-05-14._

# Janus Digital — [[ai-tool-evaluation-framework|AI Tool Evaluation & Approval Framework]]

**Document Status:** DRAFT v0.1
**Supersedes:** Section 5.2.4 (Justification Protocol)
**Owner:** Office of the COO — AI & Technology
**Last Updated:** 25 February 2026

---

## 1. Purpose & Governing Principle

This framework establishes the mandatory, multi-stage evaluation process through which any AI tool or platform is assessed for adoption within Janus Digital. It replaces the high-level criteria in Section 5.2.4 of the AI & Automated Systems Policy with a granular, gate-based process designed for transparency, repeatability, and auditability.

**Default Posture:** No AI tool, platform, or service may be used by any employee unless it has been formally approved and listed in the Janus Digital AI Registry. The burden of proof lies with the evaluation process, not with the requesting employee.

---

## 2. Definitions

| Term | Definition |
|---|---|
| **Tool** | A user-facing application or service that employees interact with directly to perform their work (e.g., a legal research assistant, a design application, a transcription service). |
| **Infrastructure** | A platform, library, or service that operates below the user-facing layer and enables other tools, agents, or automations to function. End users do not interact with it directly (e.g., [[google-cloud|Google Cloud]], Google AI Studio, Claude Console). |
| **Requester** | Any Janus Digital employee who identifies a candidate tool or infrastructure component. |
| **Evaluator** | The AI & Technology office (or delegate) responsible for conducting the formal assessment. |
| **Domain Expert** | A subject-matter specialist from the relevant department (e.g., Legal, Finance, HR) who assesses functional fit. |
| **AI Registry** | The authoritative, maintained list of all approved tools and infrastructure, categorised by tier (Core, Functional, Sandbox) per Section 5.2.1. |

---

## 3. Process Overview

The evaluation process consists of four sequential stages, each terminated by a binary gate decision. Failure at any gate halts progression and returns the candidate to a holding state or rejection.

```
[REQUEST] → [STAGE 1: Intake & Triage] → GATE 1 (Pass/Fail)
                                              ↓ Pass
                                   [STAGE 2: Technical Qualification] → GATE 2 (Pass/Fail)
                                              ↓ Pass
                                   [STAGE 3: Sandbox & Domain Expert Evaluation] → GATE 3 (Pass/Fail)
                                              ↓ Pass
                                   [STAGE 4: Approval & Registry Listing] → PRODUCTION
```

---

## 4. Stage 1 — Intake & Triage

### 4.1 Trigger
- An employee identifies a candidate tool and submits a suggestion via the designated Slack AI Hub channel.
- The AI & Technology office identifies a candidate through its own horizon-scanning activity.

### 4.2 Process
| Step | Action | Actor | Output |
|---|---|---|---|
| 1.1 | Candidate tool or infrastructure component is identified. | Requester OR Evaluator | Candidate name and URL logged. |
| 1.2 | Evaluator classifies the candidate as **Tool** or **Infrastructure**. | Evaluator | Classification recorded on tracking sheet. |
| 1.3 | Evaluator conducts a rapid desk review: public documentation, vendor website, pricing model, stated integrations. | Evaluator | Triage summary (brief notes). |
| 1.4 | Evaluator assesses against **Gate 1 Criteria**. | Evaluator | Gate 1 Decision. |

### 4.3 Gate 1 — Initial Viability Screen

**Decision type:** Binary pass/fail. All criteria must be met. Failure on any single criterion is an immediate rejection. No scoring. No weighting.

| # | Criterion | Rationale | Evidence Required |
|---|---|---|---|
| G1.1 | **[[google-workspace|Google Workspace]] / Cloud Integration** — The candidate must integrate with or export to the Janus Digital Google Cloud/Drive ecosystem. | Per Sovereignty Standard (Section 5.2.2). Non-negotiable infrastructure dependency. | Published documentation or marketplace listing confirming Google integration. |
| G1.2 | **Slack Integration** — The candidate must integrate with Slack, or at minimum provide webhook/notification capability into Slack. | Slack is the mandated internal communication and workflow hub. A tool that cannot surface within Slack creates a parallel portal, which is prohibited. | Published Slack App Directory listing, documented webhook support, or confirmed MCP connector. |
| G1.3 | **Data Portability** — The candidate must permit full export of all user data and generated outputs in a standard, non-proprietary format. | Per Sovereignty Standard (Section 5.2.2). Vendor lock-in is rejected. | Export functionality documented; format specification identified (e.g., CSV, JSON, Markdown, PDF). |
| G1.4 | **Data Training Exclusion** — The candidate must contractually guarantee that client or internal data input into the platform is not used to train its models or any third-party models. | Per Data Security Boundaries (Section 5.2.3). Prerequisite for processing any data beyond public information. | Enterprise terms of service, data processing agreement (DPA), or equivalent contractual clause. |
| G1.5 | **Documented API** — The candidate must expose a documented API. | Per Sovereignty Standard (Section 5.2.2). Required for integration with the central technology stack and future automation/agent layers. | Published API reference documentation. |

### 4.4 Gate 1 Outcomes
| Outcome | Action |
|---|---|
| **PASS** | Candidate proceeds to Stage 2. Logged on tracking sheet with date and Gate 1 evidence references. |
| **FAIL** | Candidate is rejected. Reason recorded. Requester notified via Slack. Candidate may be re-evaluated if vendor circumstances change. |

---

## 5. Stage 2 — Technical Qualification

### 5.1 Purpose
To assess the candidate against deeper technical, operational, and strategic criteria. Unlike Gate 1, these criteria use a **tiered classification**: **Must Have**, **Should Have**, and **Nice to Have**.

### 5.2 Process
| Step | Action | Actor | Output |
|---|---|---|---|
| 2.1 | Evaluator conducts a detailed technical review using vendor documentation, free/trial account access, and any available sandbox environment. | Evaluator | Technical assessment record. |
| 2.2 | Evaluator scores the candidate against **Gate 2 Criteria** using the classification matrix below. | Evaluator | Completed scoring matrix. |
| 2.3 | Evaluator determines Gate 2 outcome. | Evaluator | Gate 2 Decision. |

### 5.3 Gate 2 — Technical & Strategic Fit

**Decision type:** Structured. All **Must Have** criteria are binary (pass/fail). **Should Have** and **Nice to Have** criteria are scored 0–5 and inform the overall recommendation but do not independently block progression.

#### 5.3.1 Must Have (Binary — all required to pass)

| # | Criterion | Test |
|---|---|---|
| G2.1 | **MCP / AI Orchestration Compatibility** — The candidate supports the Model Context Protocol or an equivalent mechanism enabling integration with Claude or other approved AI orchestration layers. | Confirmed MCP server, plugin, or connector; or documented alternative integration path with the AI orchestration stack. |
| G2.2 | **Enterprise-Grade Authentication** — The candidate supports SSO (SAML/OIDC) or integrates with the Janus Digital identity provider. | SSO documentation or confirmed compatibility with Google Workspace identity. |
| G2.3 | **Vendor Viability** — The vendor demonstrates sufficient operational stability to mitigate abandonment risk within a 24-month horizon. | Assessment of funding status, customer base, public roadmap, and market position. Sole-founder hobby projects without commercial backing fail this criterion. |

#### 5.3.2 Should Have (Scored 0–5)

| # | Criterion | Scoring Guidance |
|---|---|---|
| G2.4 | **Quantifiable Efficiency Gain** — The candidate demonstrably reduces time-to-output or increases output quality for a defined workflow. | 0 = No measurable improvement. 5 = Eliminates or automates an entire manual workflow step. |
| G2.5 | **Ease of Adoption** — The learning curve is proportionate to the benefit. Non-technical users can achieve basic proficiency within a defined onboarding window. | 0 = Requires specialist training exceeding 2 weeks. 5 = Intuitive; productive within 1 hour. |
| G2.6 | **Multi-Platform Accessibility** — The candidate is accessible across desktop, web, and mobile environments without degraded functionality. | 0 = Single platform only. 5 = Full feature parity across all platforms. |
| G2.7 | **Audit Trail / Logging** — The candidate provides activity logs sufficient for compliance and internal audit requirements. | 0 = No logging. 5 = Comprehensive, exportable audit trail with user-level attribution. |
| G2.8 | **[[gemini|Gemini]] / Core AI Platform Integration** — The candidate integrates with Gemini as the core enterprise AI platform, via Workspace extension, Google AI Studio connector, Vertex AI, or equivalent pathway. | 0 = No integration path with Gemini. 5 = Native Gemini integration with full feature support. |

#### 5.3.3 Nice to Have (Scored 0–5)

| # | Criterion | Scoring Guidance |
|---|---|---|
| G2.9 | **Workflow Automation Support** — The candidate natively supports triggers, scheduled actions, or integrates with workflow automation platforms (e.g., Asana Workflows, Zapier, Make). | 0 = No automation capability. 5 = Native workflow builder with conditional logic. |
| G2.10 | **Competitive Differentiation** — The candidate offers capability not replicated by any tool already in the AI Registry. | 0 = Fully duplicated by existing approved tool. 5 = Unique, category-defining capability. |
| G2.11 | **Cost Efficiency** — Per-seat or usage-based pricing is commercially reasonable relative to the value delivered. | 0 = Prohibitively expensive for the use case. 5 = Free tier sufficient, or cost negligible relative to ROI. |

### 5.4 Gate 2 Outcomes
| Outcome | Condition | Action |
|---|---|---|
| **PASS** | All Must Have criteria met; cumulative Should Have score ≥ 15/25. | Candidate proceeds to Stage 3. |
| **CONDITIONAL PASS** | All Must Have criteria met; cumulative Should Have score 10–14/25. | Evaluator may escalate to Head of AI Office for discretionary approval to proceed, with noted risks. |
| **FAIL** | Any Must Have criterion not met, OR cumulative Should Have score < 10/25. | Candidate rejected. Reason recorded. |

---

## 6. Stage 3 — Sandbox & Domain Expert Evaluation

### 6.1 Purpose
To validate the candidate in a controlled environment using non-sensitive data, and to obtain structured feedback from the domain expert(s) who would use the tool in production.

### 6.2 Process
| Step | Action | Actor | Output |
|---|---|---|---|
| 3.1 | Evaluator provisions the candidate within the designated Experimental Sandbox environment (per Section 5.2.1, Tier 3). | Evaluator | Sandbox instance active; access credentials issued. |
| 3.2 | Evaluator defines a **test brief**: a set of representative tasks aligned to the intended use case, using only non-sensitive or synthetic data. | Evaluator | Written test brief document. |
| 3.3 | Domain Expert(s) execute the test brief. This is a mandatory, time-boxed activity (recommended: 3–5 working days). | Domain Expert(s) | Completed test tasks. |
| 3.4 | Domain Expert(s) complete the **Structured Evaluation Form** (see Section 6.3). | Domain Expert(s) | Completed evaluation form. |
| 3.5 | Evaluator reviews domain expert feedback, aggregates findings, and assesses against **Gate 3 Criteria**. | Evaluator | Stage 3 summary report. Gate 3 Decision. |

### 6.3 Structured Evaluation Form — Domain Expert

The following form is completed by each domain expert following the sandbox test period. Responses are structured to enable aggregation and comparison.

| Question | Response Format |
|---|---|
| What specific task(s) did you perform with the tool? | Free text. |
| Did the tool produce the expected output for each task? | Yes / Partially / No — per task. |
| Rate the accuracy and reliability of outputs. | 1–5 scale (1 = Unusable; 5 = Production-ready with no correction). |
| Rate the ease of use for your workflow. | 1–5 scale (1 = Obstructive; 5 = Seamless). |
| Does this tool replace, augment, or duplicate an existing approved tool? | Replace / Augment / Duplicate. |
| Would you use this tool daily if it were approved? | Yes / Occasionally / No. |
| What limitations or risks did you identify? | Free text. |
| Recommendation. | Approve / Approve with conditions / Reject. |

### 6.4 Gate 3 — Operational Validation

**Decision type:** Qualitative review by Evaluator, informed by structured domain expert feedback.

| # | Criterion | Threshold |
|---|---|---|
| G3.1 | **Domain Expert Recommendation** — Majority of domain experts recommend Approve or Approve with conditions. | ≥ 50% positive recommendation. |
| G3.2 | **No Critical Defects** — No issues identified during sandbox testing that would compromise data security, output integrity, or operational reliability. | Zero critical defects. |
| G3.3 | **Workflow Integration Feasibility** — The evaluator confirms a viable path to integrate the tool into existing departmental workflows without creating unsanctioned parallel processes. | Evaluator confirmation. |

### 6.5 Gate 3 Outcomes
| Outcome | Action |
|---|---|
| **PASS** | Candidate proceeds to Stage 4. |
| **FAIL** | Candidate rejected or returned to Stage 3 for re-evaluation with modified test brief. |

---

## 7. Stage 4 — Approval & Registry Listing

### 7.1 Process
| Step | Action | Actor | Output |
|---|---|---|---|
| 4.1 | Evaluator compiles the full evaluation dossier: Gate 1 evidence, Gate 2 scoring matrix, Stage 3 summary report, domain expert forms. | Evaluator | Complete evaluation dossier. |
| 4.2 | Evaluator presents recommendation to Head of AI Office for final approval. | Evaluator → Head of AI Office | Approval or rejection decision. |
| 4.3 | Upon approval, Evaluator initiates **IT Department Handover** by submitting the approved tool dossier to IT with deployment requirements (see Section 7.2). | Evaluator → IT Department | Handover request submitted. |
| 4.4 | IT Department conducts a security review and confirms infrastructure readiness: SSO/identity provider configuration, network/firewall requirements, licence provisioning, and first-level support ownership. | IT Department | IT Security & Readiness Confirmation (sign-off or issues raised). |
| 4.5 | If IT raises blocking issues, Evaluator and IT collaborate to resolve. Unresolvable issues are escalated to Head of AI Office. | Evaluator + IT Department | Issues resolved or tool rejected. |
| 4.6 | Upon IT confirmation, Evaluator adds the tool to the **AI Registry** with: tier classification (Core / Functional), approved use cases, data boundary classification, designated department(s), IT support contact, and review date. | Evaluator | AI Registry updated. |
| 4.7 | IT Department provisions user accounts, SSO integration, and any required infrastructure configuration. | IT Department | Deployment complete. |
| 4.8 | Evaluator publishes an announcement to the Slack AI Hub confirming the new tool's availability, permitted use cases, and any constraints. | Evaluator | Slack notification posted. |
| 4.9 | If mandatory training is required for the tool (per Section 5.3.5), Evaluator coordinates with the relevant department to schedule onboarding. | Evaluator + Department | Training scheduled. |

### 7.2 IT Department Handover Requirements

The handover submission to IT must include the following:

| Item | Description |
|---|---|
| **Tool Name & Vendor** | Name, vendor URL, and primary contact. |
| **Tier Classification** | Core or Functional. |
| **Authentication Requirements** | SSO configuration details (SAML/OIDC endpoints, Google Workspace integration). |
| **User Provisioning Scope** | Number of seats, designated departments, named users or group-based access. |
| **Network / Firewall Requirements** | Any domains, ports, or IP ranges requiring whitelisting. |
| **Data Boundary Classification** | Per Section 5.2.3 — what data types are permitted within the tool. |
| **First-Level Support Ownership** | Confirmation that IT accepts first-level support responsibility; escalation path to vendor. |
| **Licence & Billing** | Licence type, renewal date, cost centre allocation. |

---

## 8. Ongoing Review & De-listing

Approved tools are not permanent. The following triggers initiate a re-evaluation:

| Trigger | Action |
|---|---|
| **Scheduled Review** — Every 3 months from the date of Registry listing. | Full re-evaluation from Stage 2 onwards. |
| **Vendor Material Change** — Acquisition, significant pricing change, terms of service modification, or data policy change. | Immediate re-evaluation from the relevant Stage. |
| **Security Incident** — Any data breach, vulnerability disclosure, or policy violation involving the tool. | Immediate suspension from Registry pending investigation. |
| **Obsolescence** — A superior alternative is approved that fully subsumes the tool's functionality. | De-listing review initiated. |

---

## 9. Roles & Responsibilities Summary

| Role | Responsibilities |
|---|---|
| **Requester (Any Employee)** | Identify candidate tools; submit suggestions via Slack AI Hub. Does not evaluate. Does not self-approve usage. |
| **Evaluator (AI & Technology Office)** | Owns the end-to-end evaluation process. Conducts Stages 1–2. Coordinates Stage 3. Compiles dossier. Initiates IT handover. Maintains AI Registry. |
| **Domain Expert** | Participates in Stage 3 sandbox testing. Completes structured evaluation form. Participation is a mandatory duty when assigned. |
| **IT Department** | Conducts security review at Stage 4. Provisions SSO, user accounts, and infrastructure. Owns first-level support for deployed tools. Signs off on deployment readiness. |
| **Head of AI Office** | Final approval authority at Stage 4. Discretionary authority for Conditional Pass escalations at Gate 2. Resolves escalations from IT handover. |

---

## 10. Process Flow Reference

The following node definitions are provided for direct translation into a flowchart (ISO 5807 / BPMN compatible):

### 10.1 Nodes

| Node ID | Type | Label |
|---|---|---|
| N01 | Start | Candidate Identified |
| N02 | Process | Log candidate on tracking sheet |
| N03 | Process | Classify: Tool or Infrastructure |
| N04 | Process | Conduct rapid desk review |
| N05 | Decision | GATE 1: All G1.1–G1.5 met? |
| N06 | Terminator | Rejected — Gate 1 Fail (record reason, notify requester) |
| N07 | Process | Conduct detailed technical review |
| N08 | Process | Score against Gate 2 matrix |
| N09 | Decision | GATE 2: All Must Haves met AND Should Have ≥ 15? |
| N10 | Decision | GATE 2 (Conditional): Must Haves met AND Should Have 10–14? |
| N11 | Process | Escalate to Head of AI Office for discretionary approval |
| N12 | Terminator | Rejected — Gate 2 Fail (record reason) |
| N13 | Process | Provision sandbox environment |
| N14 | Process | Define test brief |
| N15 | Process | Domain Expert(s) execute test brief |
| N16 | Process | Domain Expert(s) complete evaluation form |
| N17 | Process | Evaluator aggregates findings |
| N18 | Decision | GATE 3: Majority recommend AND zero critical defects AND integration feasible? |
| N19 | Terminator | Rejected — Gate 3 Fail (record reason or return to Stage 3) |
| N20 | Process | Compile evaluation dossier |
| N21 | Process | Present to Head of AI Office for approval |
| N22 | Decision | Head of AI Office Approves? |
| N23 | Terminator | Rejected — Final (record reason) |
| N24 | Process | Submit handover to IT Department |
| N25 | Process | IT conducts security review and confirms readiness |
| N26 | Decision | IT confirms — no blocking issues? |
| N27 | Process | Resolve issues (Evaluator + IT); escalate if unresolvable |
| N28 | Terminator | Rejected — IT blocker unresolvable (record reason) |
| N29 | Process | IT provisions accounts, SSO, and infrastructure |
| N30 | Process | Add to AI Registry (Core/Functional, use cases, data boundary, department, IT contact, review date) |
| N31 | Process | Publish Slack announcement |
| N32 | Decision | Mandatory training required? |
| N33 | Process | Schedule and deliver onboarding training |
| N34 | End | Tool in Production |

### 10.2 Edges

| From | To | Condition |
|---|---|---|
| N01 | N02 | — |
| N02 | N03 | — |
| N03 | N04 | — |
| N04 | N05 | — |
| N05 | N06 | Any G1 criterion FAIL |
| N05 | N07 | All G1 criteria PASS |
| N07 | N08 | — |
| N08 | N09 | — |
| N09 | N13 | PASS |
| N09 | N10 | NOT full pass |
| N10 | N11 | CONDITIONAL PASS |
| N10 | N12 | FAIL |
| N11 | N13 | Head of AI Office grants discretionary approval |
| N11 | N12 | Head of AI Office declines |
| N13 | N14 | — |
| N14 | N15 | — |
| N15 | N16 | — |
| N16 | N17 | — |
| N17 | N18 | — |
| N18 | N19 | FAIL |
| N18 | N20 | PASS |
| N20 | N21 | — |
| N21 | N22 | — |
| N22 | N23 | REJECTED |
| N22 | N24 | APPROVED |
| N24 | N25 | — |
| N25 | N26 | — |
| N26 | N27 | Blocking issues raised |
| N26 | N29 | No blocking issues |
| N27 | N25 | Issues resolved |
| N27 | N28 | Unresolvable — escalation fails |
| N29 | N30 | — |
| N30 | N31 | — |
| N31 | N32 | — |
| N32 | N33 | YES |
| N32 | N34 | NO |
| N33 | N34 | — |

---

*End of document.*
