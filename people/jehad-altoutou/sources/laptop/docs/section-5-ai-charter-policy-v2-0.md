---
type: source
source_type: laptop
title: Section_5_AI_Charter_Policy_v2.0
slug: section-5-ai-charter-policy-v2-0
created: 2026-04-02
captured_by: jehad-altoutou
audience: personal
original_path: /Users/jehad/Desktop/Section_5_AI_Charter_Policy_v2.0.docx
original_size: 78989
original_ext: .docx
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:43Z"
sensitivity: dept
sensitivity_confidence: 0.95
sensitivity_reason: "Janus AI Charter & Policy v2.1 (ISO 42001 compliance) — formal organisational policy, AI Office owned, intended for org-wide compliance reference"
project: desktop-captures

---

# Section_5_AI_Charter_Policy_v2.0

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Section_5_AI_Charter_Policy_v2.0.docx` on 2026-05-14._

<table style="width:96%;">
<colgroup>
<col style="width: 96%" />
</colgroup>
<thead>
<tr>
<th><p><strong>JANUS DIGITAL</strong></p>
<p><strong>Section 5: AI Charter &amp; Policy</strong></p>
<p><em>AI Native Framework</em></p>
<p>Compliance Standard: ISO/IEC 42001:2023 (Artificial Intelligence
Management System)</p>
<p>Version: 2.1 Date: 30 March 2026 Owner: AI Office</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# **5.1 The “AI Native” Mandate**

Janus Digital operates as an **AI Native organisation.** Unlike
traditional companies that layer technology over existing processes, we
integrate Artificial Intelligence (AI) as the foundational baseline for
all operations. At Janus, AI is not a supplementary tool; it is the
primary engine of our operational infrastructure.

Proficiency in AI utilisation is a core competency required for all
roles. We are committed to the responsible, safe, and ethical
development and deployment of AI systems in strict compliance with our
Artificial Intelligence Management System (AIMS) and ISO/IEC 42001:2023.

# **5.2 Strategic Pillars of AI Value**

All AI initiatives and usage must align with the following three
strategic pillars, designed to drive value and organisational
resilience.

| **Pillar** | **Objective** | **Requirement** |
|----|----|----|
| **1. Operational Optimisation** | Automate core administrative and operational functions to eliminate friction and redundancy. | Employees are expected to identify workflows where AI can reduce manual latency. Automation must never compromise accuracy; critical outputs require human verification. |
| **2. Strategic Innovation** | Leverage AI to create new capabilities, services, and value propositions that were previously impossible. | Innovation must be balanced with responsibility. New use cases must undergo impact assessments to prevent unintended harm or bias. |
| **3. Institutional Intelligence** | Systematically capture, structure, and refine data to build a centralised, queryable knowledge base that fuels our AI ecosystem. | Data integrity is paramount. All information fed into our systems must be accurate, traceable, and properly classified. |

# **5.3 The Register of Approved AI Providers**

Janus Digital strictly prohibits **“Shadow AI”** — the use of unverified
or unauthorised AI tools. The AI Office maintains a **Register of
Approved AI Providers** (the AI Registry), which is the authoritative
and continuously updated list of all tools and platforms approved for
use within the organisation.

Only tools listed in the AI Registry are permitted for use. Employees
who require a tool not currently on the approved list must submit a
formal request to the AI Office for evaluation. Using unapproved
alternatives to circumvent this process is a policy violation subject to
disciplinary action.

## **5.3.1 Tool Tiers**

All approved tools are classified into one of three tiers:

| **Tier** | **Scope** | **Description** |
|----|----|----|
| **Core Infrastructure** | Universal — all staff | Mandatory platforms integrated into the Janus Digital operating environment. Vetted for maximum security and compliance. Deployed organisation-wide. |
| **Functional Tools** | Department-specific | Specialised applications approved for specific use cases or departments. Access is granted by department and role. |
| **AI Office Infrastructure** | AI Office managed | Platforms and services operating below the employee-facing layer — development infrastructure, model APIs, and internal tooling. Employees do not interact with these directly. |

## **5.3.2 Tool vs Infrastructure Distinction**

For the purposes of evaluation and governance, all candidates are
classified as either a **Tool** (a user-facing application that
employees interact with directly) or **Infrastructure** (a platform or
service operating below the user-facing layer). This classification
determines which evaluation criteria apply and prevents the
misapplication of standards designed for one category to the other.

## **5.3.3 Data Sovereignty Requirement**

No tool may be listed in the AI Registry unless it satisfies the
following non-negotiable requirements, which reflect our commitment to
avoiding vendor lock-in:

- **Data Portability:** The tool must allow full export of all data to
  Janus-controlled infrastructure in a standard, non-proprietary format.

- **Documented API:** The tool must provide a documented API to ensure
  integration with our central technology stack and future automation
  layers.

# **5.4 [[ai-tool-evaluation-framework|AI Tool Evaluation & Approval Framework]]**

All proposed AI tools must pass through a formal four-stage, gate-based
evaluation process before being listed in the AI Registry and approved
for use. The detailed criteria for each stage are governed by the **AI
Tool Evaluation & Approval Framework** document (maintained by the AI
Office, DRAFT v0.1). This section provides the governance-level
overview.

## 

## **5.4.1 Process Overview**

The evaluation follows a strictly sequential process. Failure at any
gate results in rejection or deferral; the candidate does not advance to
the next stage.

## <img src="media/image1.png" style="width:10.11291in;height:1.80556in" />

## **5.4.2 Stage 1 — Intake & Triage**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>STAGE 1 | Gate type: Binary pass/fail — all criteria must
be met</strong></p>
<p>Any employee may identify and submit a candidate tool via the
designated #ai-internal-hub Slack channel. Submissions are deliberately
lightweight — a brief description of the tool and its potential use is
sufficient. The AI Office assumes full ownership of the evaluation from
that point.</p>
<p>The AI Office classifies the candidate as a Tool or Infrastructure,
conducts a rapid desk review of public documentation, and assesses it
against Gate 1: Initial Viability. Gate 1 is a binary pass/fail screen —
there is no scoring or weighting. Any tool that does not meet all of the
following criteria is rejected immediately:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

- Integration compatibility with [[google-workspace|Google Workspace]] and Slack

- Full data portability in a standard, non-proprietary format

- Contractual guarantee that Janus Digital data will not be used to
  train public AI models

- Availability of a publicly documented API

## **5.4.3 Stage 2 — Technical Qualification**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>STAGE 2 | Gate type: Mandatory requirements + scored
assessment</strong></p>
<p>Tools that pass Gate 1 undergo a structured technical assessment.
Stage 2 has two components:</p>
<p>Mandatory Requirements (binary): AI orchestration compatibility;
enterprise-grade Single Sign-On (SSO) authentication compatible with
Google Workspace; and vendor viability assessed over a 24-month
horizon.</p>
<p>Scored Assessment: A set of desirable qualities is scored against
defined criteria, including quantifiable efficiency gains, ease of
adoption, multi-platform accessibility, audit trail capability, and
integration with our core AI platforms.</p>
<p>Gate 2 produces one of three outcomes: Pass (proceed to Stage 3);
Conditional Pass (escalated to the Head of AI Office for discretionary
judgement); or Fail (rejected, with reasons formally recorded).</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## **5.4.4 Stage 3 — Sandbox & Domain Expert Evaluation**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>STAGE 3 | Gate type: Domain expert recommendation +
defect and integration checks</strong></p>
<p>Tools that clear Gate 2 are provisioned in the Janus Digital Sandbox
Environment (see §5.5) for a time-boxed pilot evaluation of three to
five working days. The AI Office defines a structured test brief using
representative tasks and non-sensitive or synthetic data only.</p>
<p>Designated Domain Experts — subject-matter specialists from the
relevant department — execute the test brief and complete a structured
evaluation form.</p>
<p>Domain expert participation in Stage 3 is mandatory when assigned.
This is a professional obligation, not an optional activity; it reflects
our organisational commitment to responsible AI adoption.</p>
<p>Gate 3 requires: a majority of domain experts recommending approval;
zero critical defects identified during sandbox testing; and the AI
Office confirming a viable integration path.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## **5.4.5 Stage 4 — Approval, IT Handover & Registry Listing**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>STAGE 4 | Two sequential sub-gates: Head of AI Office
approval, then IT Department sign-off</strong></p>
<p>Stage 4 comprises two sequential gates. Both must be cleared before a
tool is listed in the AI Registry.</p>
<p>Sub-Gate A — Head of AI Office Approval: The AI Office compiles a
full evaluation dossier covering all prior gate evidence, scoring, and
the Stage 3 domain expert report, and presents it to the Head of AI
Office for a formal approval decision.</p>
<p>Sub-Gate B — IT Department Handover: Upon approval, the dossier is
formally submitted to the IT Department. IT conducts a mandatory
security review covering identity and access configuration (SSO),
network and firewall requirements, licence provisioning, and first-level
support ownership. The IT Department must confirm clearance before any
tool is listed in the AI Registry. IT retains the authority to raise
blocking issues; unresolvable conflicts are escalated to the Head of AI
Office.</p>
<p>Upon IT confirmation: accounts and access are provisioned; the tool
is added to the AI Registry at the appropriate tier; a company-wide
announcement is published; and any required training is
scheduled.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## **5.4.6 Ongoing Review & De-listing**

Approved tools are subject to periodic re-evaluation. The following
triggers initiate a review or immediate suspension:

| **Trigger** | **Action** |
|----|----|
| Scheduled Review | Full re-evaluation from Stage 2 onwards at the applicable review interval. (The AI Office will communicate any change to the current schedule.) |
| Vendor Material Change | Acquisition, significant pricing change, material update to Terms of Service, or change to data handling policy triggers immediate re-evaluation from the relevant stage. |
| Security Incident | Any confirmed breach, identified vulnerability, or policy violation triggers immediate suspension pending investigation. |
| Obsolescence | Where a superior approved alternative exists, a de-listing review is initiated. |

# **5.5 The Sandbox Environment**

Janus Digital operates a dedicated Sandbox Environment that mirrors our
production infrastructure with full fidelity. The sandbox exists to
enable the safe evaluation of third-party tools and the development of
internal AI solutions, without risk to production data, client data, or
live operational systems.

## **5.5.1 Purpose & Scope**

The sandbox is the mandatory environment for all Stage 3 tool
evaluations (see §5.4.4) and for all internal AI solution development
prior to production deployment (see §5.6). It is not an informal test
area; it is a governed environment with formal data restrictions and
defined entry and exit conditions.

## **5.5.2 Data Restrictions**

**Only non-sensitive or synthetic data** may be processed within the
sandbox at any time. The following are strictly prohibited:

- Production data of any kind

- Client data or client-related information

- Personally Identifiable Information (PII)

- Confidential company information or intellectual property

These restrictions apply without exception, regardless of the purpose of
the evaluation or development activity. Violation of sandbox data
boundaries is treated as a breach of the Data Governance policy (§5.7)
and is subject to the disciplinary provisions set out in §5.10.

## **5.5.3 Promotion to Production**

A tool or solution exits the sandbox only upon formal approval through
the relevant gate process: Gate 3 for third-party tools, or formal
acceptance testing for internally developed solutions. Promotion to
production is a deliberate, documented act, not an informal transition.

# **5.6 Internal AI Solution Development**

In addition to evaluating and approving third-party tools, the AI Office
designs and builds bespoke AI solutions for internal operational use.
These solutions are developed against a structured pipeline that
enforces governance, scope control, and data safety at each stage.

## **5.6.1 Pipeline Overview**

| **Stage** | **Description** |
|----|----|
| Intake | Departments submit requests via \#ai-internal-hub. Requests describe the problem, not a proposed solution. |
| Discovery | The AI Office conducts a structured engagement to translate the problem into a buildable specification. |
| Triage | First formal gate: the AI Office decides whether to commit to development (Go) or defer (Park). Not all requests are AI Office problems. |
| PRD / SoW Sign-Off | A Product Requirements Document defining scope, deliverables, and acceptance criteria is drafted and formally signed. No development commences without a signed PRD. This is a hard gate. |
| Product Specification | A detailed functional specification is authored before any build work begins. This is a first-class deliverable, not a formality. |
| Sandbox Build | Development takes place exclusively in the Sandbox Environment using non-sensitive data only. |
| Acceptance | The requesting department validates the solution against the signed PRD acceptance criteria. Pass advances to production; fail returns to build with a documented change request. |
| Production & Monitor | The solution is promoted to production, listed in the AI Registry where applicable, and handed over to the department with documented support terms. |

## **5.6.2 Governance Principles**

- **No build without a signed PRD.** This is a hard gate. No exceptions.

- **Sandbox is non-negotiable.** All development takes place in the
  Sandbox Environment using non-sensitive data, regardless of perceived
  sensitivity of the task.

- **Scope control is absolute.** All scope changes must be reflected in
  a signed PRD amendment. Verbal scope changes have no standing.

- **The AI Office does not provide general IT support.** SaaS selection
  advisory, general technology support, and non-AI process work are
  redirected to the appropriate teams.

# **5.7 Data Governance & Sovereignty**

Protecting Janus Digital’s intellectual property and client data is
non-negotiable. The following data classification protocols apply to all
employees without exception.

| **Environment** | **Permitted Data** | **Key Restriction** |
|----|----|----|
| **Public / Free-Tier AI Models** | None | Employees must NEVER use public, non-enterprise AI models for any work-related task or input any form of company data. This includes internal communications, client details, and intellectual property. If a required tool is not on the approved list, submit a formal request to the AI Office. |
| **Enterprise AI Instances (Approved)** | Confidential data permitted | Confidential data may only be processed within approved enterprise instances where data privacy is contractually guaranteed and inputs are isolated from public model training. |
| **Sandbox Environment** | Non-sensitive / synthetic only | No production data, client data, or PII. See §5.5. |
| **Recording & Transcription** | Meeting recordings (consent required) | All participants must be explicitly notified and grant consent before any AI recording or transcription tool is activated. In compliance with GDPR, CCPA, and applicable local regulations. |

# **5.8 Risk Management & Impact Assessment**

In accordance with **ISO/IEC 42005** (AI System Impact Assessment) and
**ISO/IEC 23894** (Risk Management), Janus Digital requires a proactive
approach to AI risk.

## **Impact Assessments**

Before deploying any AI workflow that significantly affects clients,
employees, or decision-making processes, an AI Impact Assessment must be
conducted to evaluate potential risks regarding bias, transparency, and
societal impact.

## **Human-in-the-Loop (HITL)**

For high-stakes decisions, AI must serve as a decision-support tool, not
a decision-maker. A qualified human must always review and approve the
final output.

## **Incident Reporting**

AI language models are probabilistic systems and may produce factually
incorrect outputs (“hallucinations”). Users are responsible for
verifying and correcting routine errors as part of their standard
professional responsibilities. However, extreme cases of model
deviation, recurring systemic failures, or safety guardrail breaches
must be reported to the AI Office immediately.

# **5.9 Accountability & Transparency**

## **Ultimate Responsibility**

AI is a tool, and the employee remains the **“Pilot in Command.”** All
staff are professionally accountable for work produced under their name,
regardless of AI assistance. Employees must verify facts, validate
logic, and critically assess AI outputs before use or distribution.

## **Prohibition of “AI Slop”**

The distribution of raw, unverified, or low-quality AI-generated content
is strictly prohibited.

## **Transparency**

Internal and external communications that are significantly generated by
AI must be disclosed as such, ensuring clarity about the nature of the
work product.

# **5.10 Roles and Responsibilities**

| **Role** | **Responsibilities** |
|----|----|
| **The AI Office** | Central authority for AI strategy, tool evaluation and lifecycle management, the AI Registry, internal solution development, training, and best practices. |
| **Head of AI Office** | Final approval authority for tool adoption (Stage 4 gate). Escalation point for IT handover disputes and conditional evaluation outcomes. Day-to-day authority for AI governance operations. |
| **IT Department** | Mandatory security review and sign-off before any tool enters production. Owns identity and access configuration (SSO), network and firewall provisioning, licence management, and first-level support ownership. |
| **Team Leads** | Responsible for ensuring direct reports adhere to this policy and for identifying new opportunities for Operational Optimisation within their departments. |
| **Domain Experts** | Required to participate in Stage 3 sandbox evaluations when assigned by the AI Office. Participation is a mandatory professional obligation; it is part of the job description, not an optional activity. |
| **AI Management Representative** | Operational lead responsible for maintaining the ISO 42001 management system, overseeing the Risk Register, and ensuring continuous improvement of the AI governance framework. |
| **All Employees** | Responsible for compliance with all provisions of this policy, particularly Data Governance (§5.7), Sandbox Data Restrictions (§5.5.2), and Accountability (§5.9). |

<table style="width:96%;">
<colgroup>
<col style="width: 96%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Policy Compliance Notice</strong></p>
<p>Failure to comply with these governance protocols — particularly Data
Sovereignty (§5.7), Sandbox Data Restrictions (§5.5.2), and
Accountability (§5.9) — may result in disciplinary action, up to and
including termination of employment.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
