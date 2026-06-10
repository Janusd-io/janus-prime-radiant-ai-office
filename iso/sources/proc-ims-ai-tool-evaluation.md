---
type: source
title: AI Tool Evaluation & Approval — Process Map (IMS pilot)
slug: proc-ims-ai-tool-evaluation
created: 2026-06-09
updated: 2026-06-09
source_type: document
source_origin: Google Drive — ISO/IMS department (Simon Tarskih)
document_id: PROC-IMS-AIToolEvaluation
document_version: v0.1
document_status: DRAFT
captured_by: jehad-altoutou
departments: [ai-office, ims-compliance]
related: [ims-digital-twin, iso-ims-puls, three-iso-standards, ims-enrolment, simon-tarskih]
ingested_in_full: true
---

> Full-fidelity ingest of the ISO/IMS source document `PROC-IMS-AIToolEvaluation v0.1` (DRAFT), received from Simon (IMS & Compliance) via Google Drive, 2026-06-09. Content preserved verbatim (pandoc/xlsx → markdown); not summarized.

**AI Tool Evaluation & Approval — Process Map**

*PROC-IMS-AIToolEvaluation-v0.1-2026-06-05*

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 29%" />
<col style="width: 15%" />
<col style="width: 35%" />
</colgroup>
<tbody>
<tr>
<td style="text-align: left;"><strong>Process ID</strong></td>
<td style="text-align: left;">§TBD</td>
<td style="text-align: left;"><strong>Version</strong></td>
<td style="text-align: left;">v0.1</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Title</strong></td>
<td style="text-align: left;"><strong>AI Tool Evaluation &amp; Approval
— Process Map</strong></td>
<td style="text-align: left;"><strong>Status</strong></td>
<td style="text-align: left;"><strong>DRAFT</strong></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Process Owner</strong></td>
<td style="text-align: left;">Office of the COO — AI &amp; Technology
(§USR_HEAD_AI)</td>
<td style="text-align: left;"><strong>Date</strong></td>
<td style="text-align: left;">2026-06-05</td>
</tr>
<tr>
<td style="text-align: left;"><strong>IMS Standards</strong></td>
<td colspan="3" style="text-align: left;">ISO 9001 cl. 6.1/7.5/9.1 | ISO
27001 A.5.9/A.5.12 | ISO 42001 §8.2</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Supersedes</strong></td>
<td colspan="3" style="text-align: left;">—</td>
</tr>
</tbody>
</table>

|                          |
|:-------------------------|
| **PROCESS PARTICIPANTS** |

> *Participants include persons, departments, AI systems, and AI agents.
> Participant_ID for persons: User_ID Registry (§TBD). For AI agents: AI
> Models & Agents Registry (Appendix A.3). For departments: Organisation
> Document Registry (Appendix B.1).*

|  |  |  |  |
|:---|:---|:---|:---|
| **Participant_ID** | **Name / Role** | **Type** | **Involvement** |
| **§USR_REQUESTER** | Any Employee — Requester | Person | Submits tool request via Slack; receives outcome notification |
| **§USR_EVALUATOR** | AI Evaluator (AI & Technology Office) | Person | Conducts full evaluation Stages 1–3; compiles Form A1/A2; initiates IT Handover; publishes announcement |
| **§USR_HEAD_AI** | Head of AI Office — Process Owner | Person | Final approval authority (Step 4A.2); discretionary Gate 2 escalation; process owner |
| **§USR_DOMAIN_EXPERT** | Domain Expert (relevant department) | Person | Stage 3 sandbox testing; completes Structured Evaluation Form — from Domain Experts Registry (§TBD — to be created, see IMPROVEMENT LOG) |
| **§USR_IT** | IT Department representative | Person | Stage 4B — security review; provisioning accounts/SSO/infrastructure |
| **AI-03** | Fireflies AI | AI Agent | Captures tool mentions from meetings (Source B — Input B); AI Models & Agents Registry Appendix A.3 |

|                       |
|:----------------------|
| **PROCESS RESOURCES** |

> *People & Competencies: list skills and knowledge — roles are in
> Process Participants above.*

<table>
<colgroup>
<col style="width: 39%" />
<col style="width: 60%" />
</colgroup>
<tbody>
<tr>
<td style="text-align: left;"><strong>Resource Type</strong></td>
<td style="text-align: left;"><strong>Required for this
Process</strong></td>
</tr>
<tr>
<td style="text-align: left;"><p><strong>People &amp;
Competencies</strong></p>
<p><em>Skills and knowledge required</em></p></td>
<td style="text-align: left;">Familiarity with IMS-001 and gate criteria
G1.1–G1.5, G2.1–G2.11, G3.1–G3.3. Domain expertise: independent SME with
no conflict of interest — from Domain Experts Registry (§TBD). IT:
SSO/SAML, network security, software provisioning (Stage 4B).</td>
</tr>
<tr>
<td style="text-align: left;"><p><strong>Hardware &amp;
Infrastructure</strong></p>
<p><em>Physical and cloud infrastructure required</em></p></td>
<td style="text-align: left;">Sandbox environment Tier 3 — isolated, no
production data; configuration §TBD. IT infrastructure for SSO
configuration and enterprise deployment (Stage 4B).</td>
</tr>
<tr>
<td style="text-align: left;"><p><strong>Software &amp;
Licenses</strong></p>
<p><em>Applications and platforms in use</em></p></td>
<td style="text-align: left;">Slack Business+/Enterprise Grid (3P —
#ai-tool-requests). AI Registry — Linear, active subscription with AIR
project access. Fireflies AI — Business plan (AI-03). All listed in
Software Registry Appendix A.2.</td>
</tr>
<tr>
<td style="text-align: left;"><p><strong>AI Systems &amp;
Models</strong></p>
<p><em>AI tools and agents involved in the process</em></p></td>
<td style="text-align: left;">Fireflies AI (AI-03) — meeting transcript
capture for horizon-scanning trigger (Source B, Block 1). Human
oversight: AI Evaluator reviews all AI-identified tool mentions before
logging on Form 1A1. Documented in AI Models &amp; Agents Registry
Appendix A.3.</td>
</tr>
<tr>
<td style="text-align: left;"><p><strong>Data &amp; Information
Resources</strong></p>
<p><em>Data sources, documents, and information assets</em></p></td>
<td style="text-align: left;">IMS-001 — AI Tool Evaluation &amp;
Approval Framework (IMS Document Register Appendix C). Form 1A1 — AI
Tool Intake Log (Org Doc Registry Appendix B.2, Form_ID 1A1). Form 1A2 —
AI Tool Evaluation Report (Form_ID 1A2). 3P — Slack Production (Data
Sources Registry Appendix A.1).</td>
</tr>
<tr>
<td style="text-align: left;"><p><strong>Work Environment</strong></p>
<p><em>Conditions required to perform the process</em></p></td>
<td style="text-align: left;">Digital-first process — all steps executed
via approved digital systems (Slack, sandbox, AI Registry). No physical
workspace requirements. Domain Experts must have isolated, independent
test environment during Stage 3 sandbox testing.</td>
</tr>
</tbody>
</table>

|                                    |
|:-----------------------------------|
| **PROCESS PERFORMANCE INDICATORS** |

|  |  |  |  |
|:---|:---|:---|:---|
| **\#** | **Indicator** | **Target** | **Formula** |
| **1** | Request Processing Timeliness | ≥ 95% | Kt = At / Atot × 100%, where At — requests processed within the established timeframe; Atot — total requests received in the reporting period |
| **2** | Re-evaluation Rate | ≤ 5% | Rr = Ar / Atot × 100%, where Ar — re-evaluations initiated for previously assessed tools; Atot — total completed evaluations in the reporting period |
| **3** | Tool Adoption Rate | ≥ §TBD% | Ra = Au / Aapp × 100%, where Au — approved tools with confirmed active usage N months after deployment; Aapp — total approved tools in the reporting period |

> *Target for KPI 3 to be established after first reporting period.
> Reporting period: §TBD (recommended: quarterly). Process owner: Office
> of the COO — AI & Technology.*

|                            |
|:---------------------------|
| **BLOCK 1. INPUT SOURCES** |

|  |  |
|:---|:---|
| **Source A** |  |
| **Source_ID** | 3P (Slack Production — Data Sources Registry — Appendix A.1) |
| **Sub_Location** | \#ai-tool-requests |
| **Initiator_ID** | §USR_REQUESTER (User_ID Registry) |

|  |  |
|:---|:---|
| **Source B** |  |
| **Source_ID** | AI-03 (Fireflies AI — AI Models & Agents Registry — Appendix A.3) |
| **Sub_Location** | §TBD |
| **Initiator_ID** | §USR_EVALUATOR (User_ID Registry) |

|                     |
|:--------------------|
| **BLOCK 2. INPUTS** |

|                   |                                                   |
|:------------------|:--------------------------------------------------|
| **Input A**       |                                                   |
| **Entity Format** | Data — Text (tool name, URL, brief justification) |
| **Object_ID**     | Slack message permalink (system-assigned — 3P)    |

|  |  |
|:---|:---|
| **Input B** |  |
| **Entity Format** | File — §TBD format (meeting transcript/recording) |
| **Object_ID** | \[external file — preserves original Fireflies naming — AI-03\] |

|                                            |
|:-------------------------------------------|
| **BLOCK 3. ACTIVITIES AND CONTROL POINTS** |

**3.1 Trigger Start Point**

|  |  |
|:---|----|
| **System_Code** | 3P (Slack Production — Data Sources Registry — Appendix A.1) |
| **Sub_Location** | \#ai-tool-requests |
| **Routing_Target** | 1A (AI Native — Organisation Document Registry — Appendix B.1) |
| **Description** | New AI tool request message posted in Slack \#ai-tool-requests channel, OR Evaluator identifies candidate via horizon-scanning activity |
| **Record_Object_ID** | (none at trigger point — Form A1 created in Block 3.2) |

**3.2 Input Control**

<table style="width:100%;">
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<tbody>
<tr>
<td style="text-align: left;"><strong>Source_ID</strong></td>
<td>3P (Slack Production — Data Sources Registry — Appendix A.1)</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Doc_Location</strong></td>
<td>IMS-001 (AI Tool Evaluation &amp; Approval Framework — IMS Document
Register — Appendix C)</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Executor_ID</strong></td>
<td>§USR_EVALUATOR (User_ID Registry)</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Decision_Maker</strong></td>
<td>1A (AI Native — Organisation Document Registry — Appendix B.1)</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Status_Code</strong></td>
<td><p>• Approved → data complete, tool not in AIR → proceed to Block
3.3</p>
<p>• Rejected → request too unclear to process → notify §USR_REQUESTER
via Slack</p>
<p>• Escalation → partial data (URL present / name incorrect, or name
present / URL broken) — intent clear, requires Dept Head confirmation →
1A (AI Native)</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Record_Object_ID</strong></td>
<td>Form A1 — AI Tool Intake Log, created: tool name, URL, date,
Initiator_ID (Organisation Document Registry — Appendix B.2)</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Record_Source_ID</strong></td>
<td>§TBD (Data Sources Registry — Appendix A.1)</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Sub_Location</strong></td>
<td>§TBD</td>
</tr>
</tbody>
</table>

**3.3 Scenario**

|                               |
|:------------------------------|
| **STAGE 1 — Intake & Triage** |

|  |  |
|:---|:---|
| **Step 1.1 — Log candidate** |  |
| **Source_ID** | §TBD (Data Sources Registry — Appendix A.1) |
| **Executor_ID** | §USR_EVALUATOR (User_ID Registry) |
| **Action_Type** | CREATE |
| **Object_Ref** | IMS-001 (AI Tool Evaluation & Approval Framework — IMS Document Register — Appendix C), §4.2 step 1.1 — candidate name and URL logged |
| **Record_Object_ID** | Form A1 — AI Tool Intake Log (Organisation Document Registry — Appendix B.2) |
| **Record_Source_ID** | §TBD (Data Sources Registry — Appendix A.1) |
| **Sub_Location** | §TBD |

|  |  |
|:---|:---|
| **Step 1.2 — Classify Tool or Infrastructure** |  |
| **Source_ID** | §TBD (Data Sources Registry — Appendix A.1) |
| **Executor_ID** | §USR_EVALUATOR (User_ID Registry) |
| **Action_Type** | UPDATE |
| **Object_Ref** | IMS-001 (AI Tool Evaluation & Approval Framework — IMS Document Register — Appendix C), §4.2 step 1.2 — classify Tool or Infrastructure |
| **Record_Object_ID** | Form A1 updated — classification: Tool or Infrastructure (Organisation Document Registry — Appendix B.2) |
| **Record_Source_ID** | §TBD (Data Sources Registry — Appendix A.1) |
| **Sub_Location** | §TBD |

|  |  |
|:---|:---|
| **Step 1.3 — Rapid desk review** |  |
| **Source_ID** | §TBD external sources (Data Sources Registry — Appendix A.1) |
| **Executor_ID** | §USR_EVALUATOR (User_ID Registry) |
| **Action_Type** | READ |
| **Object_Ref** | IMS-001 (AI Tool Evaluation & Approval Framework — IMS Document Register — Appendix C), §4.2 step 1.3 — desk review: public docs, vendor site, pricing, integrations |
| **Record_Object_ID** | Form A1 updated — triage summary: brief notes (Organisation Document Registry — Appendix B.2) |
| **Record_Source_ID** | §TBD (Data Sources Registry — Appendix A.1) |
| **Sub_Location** | §TBD |

<table style="width:100%;">
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<tbody>
<tr>
<td style="text-align: left;"><strong>Step 1.4 — GATE 1</strong></td>
<td style="text-align: left;"><strong>CONTROL POINT</strong></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Source_ID</strong></td>
<td style="text-align: left;">§TBD (Data Sources Registry — Appendix
A.1)</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Doc_Location</strong></td>
<td style="text-align: left;">IMS-001 (AI Tool Evaluation &amp; Approval
Framework — IMS Document Register — Appendix C), §4.3 criteria
G1.1–G1.5</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Executor_ID</strong></td>
<td style="text-align: left;">§USR_EVALUATOR (User_ID Registry)</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Decision_Maker</strong></td>
<td style="text-align: left;">§USR_EVALUATOR (User_ID Registry)</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Status_Code</strong></td>
<td style="text-align: left;"><p>• PASS → Stage 2</p>
<p>• FAIL → record reason + notify §USR_REQUESTER via Slack</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Record_Object_ID</strong></td>
<td style="text-align: left;">Form A1 updated — Gate 1 decision + date +
evidence references per G1.1–G1.5 (Organisation Document Registry —
Appendix B.2)</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Record_Source_ID</strong></td>
<td style="text-align: left;">§TBD (Data Sources Registry — Appendix
A.1)</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Sub_Location</strong></td>
<td style="text-align: left;">§TBD</td>
</tr>
</tbody>
</table>

|                                       |
|:--------------------------------------|
| **STAGE 2 — Technical Qualification** |

|  |  |
|:---|:---|
| **Step 2.1 — Detailed technical review** |  |
| **Source_ID** | §TBD external sources (Data Sources Registry — Appendix A.1) |
| **Executor_ID** | §USR_EVALUATOR (User_ID Registry) |
| **Action_Type** | READ |
| **Object_Ref** | IMS-001 (AI Tool Evaluation & Approval Framework — IMS Document Register — Appendix C), §5.2 step 2.1 — detailed technical review: vendor docs, trial/sandbox access |
| **Record_Object_ID** | Form A1 updated — technical assessment record (Organisation Document Registry — Appendix B.2) |
| **Record_Source_ID** | §TBD (Data Sources Registry — Appendix A.1) |
| **Sub_Location** | §TBD |

|  |  |
|:---|:---|
| **Step 2.2 — Score Gate 2 matrix** |  |
| **Source_ID** | §TBD (Data Sources Registry — Appendix A.1) |
| **Executor_ID** | §USR_EVALUATOR (User_ID Registry) |
| **Action_Type** | UPDATE |
| **Object_Ref** | IMS-001 (AI Tool Evaluation & Approval Framework — IMS Document Register — Appendix C), §5.3 criteria G2.1–G2.11 — Must Have / Should Have / Nice to Have |
| **Record_Object_ID** | Form A1 updated — completed Gate 2 scoring matrix (Organisation Document Registry — Appendix B.2) |
| **Record_Source_ID** | §TBD (Data Sources Registry — Appendix A.1) |
| **Sub_Location** | §TBD |

<table style="width:100%;">
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<tbody>
<tr>
<td style="text-align: left;"><strong>Step 2.3 — GATE 2</strong></td>
<td style="text-align: left;"><strong>CONTROL POINT</strong></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Source_ID</strong></td>
<td style="text-align: left;">§TBD (Data Sources Registry — Appendix
A.1)</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Doc_Location</strong></td>
<td style="text-align: left;">IMS-001 (AI Tool Evaluation &amp; Approval
Framework — IMS Document Register — Appendix C), §5.3–5.4 criteria
G2.1–G2.11</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Executor_ID</strong></td>
<td style="text-align: left;">§USR_EVALUATOR (User_ID Registry)</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Decision_Maker</strong></td>
<td style="text-align: left;">§USR_EVALUATOR (User_ID Registry)</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Status_Code</strong></td>
<td style="text-align: left;"><p>• PASS (all Must Have + Should Have
≥15) → Stage 3</p>
<p>• CONDITIONAL PASS (Should Have 10–14) → ESCALATE to §USR_HEAD_AI</p>
<p>• FAIL → record reason + notify §USR_REQUESTER via Slack</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Record_Object_ID</strong></td>
<td style="text-align: left;">Form A1 updated — Gate 2 decision + date +
scoring summary (Organisation Document Registry — Appendix B.2)</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Record_Source_ID</strong></td>
<td style="text-align: left;">§TBD (Data Sources Registry — Appendix
A.1)</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Sub_Location</strong></td>
<td style="text-align: left;">§TBD</td>
</tr>
</tbody>
</table>

|                                                  |
|:-------------------------------------------------|
| **STAGE 3 — Sandbox & Domain Expert Evaluation** |

|  |  |
|:---|:---|
| **Step 3.1 — Provision sandbox environment** |  |
| **Source_ID** | §TBD (Data Sources Registry — Appendix A.1) |
| **Executor_ID** | §USR_EVALUATOR (User_ID Registry) |
| **Action_Type** | CREATE |
| **Object_Ref** | IMS-001 (AI Tool Evaluation & Approval Framework — IMS Document Register — Appendix C), §6.2 step 3.1 — provision Tier 3 sandbox environment |
| **Record_Object_ID** | Form A1 updated — sandbox environment reference + provisioning date (Organisation Document Registry — Appendix B.2) |
| **Record_Source_ID** | §TBD (Data Sources Registry — Appendix A.1) |
| **Sub_Location** | §TBD |

|  |  |
|:---|:---|
| **Step 3.2 — Define test brief** |  |
| **Source_ID** | §TBD (Data Sources Registry — Appendix A.1) |
| **Executor_ID** | §USR_EVALUATOR (User_ID Registry) |
| **Action_Type** | CREATE |
| **Object_Ref** | IMS-001 (AI Tool Evaluation & Approval Framework — IMS Document Register — Appendix C), §6.2 step 3.2 — test brief: representative tasks, non-sensitive data only |
| **Record_Object_ID** | Form A1 updated — test brief document reference (Organisation Document Registry — Appendix B.2) |
| **Record_Source_ID** | §TBD (Data Sources Registry — Appendix A.1) |
| **Sub_Location** | §TBD |

|  |  |
|:---|:---|
| **Step 3.3 — Domain Expert(s) execute test brief** |  |
| **Source_ID** | §TBD (Data Sources Registry — Appendix A.1) |
| **Executor_ID** | §USR_DOMAIN_EXPERT (User_ID Registry) |
| **Action_Type** | VALIDATE |
| **Object_Ref** | IMS-001 (AI Tool Evaluation & Approval Framework — IMS Document Register — Appendix C), §6.2 step 3.3 — execute test brief, time-boxed 3–5 working days |
| **Record_Object_ID** | Form A1 updated — execution date + Domain Expert ID(s) (Organisation Document Registry — Appendix B.2) |
| **Record_Source_ID** | §TBD (Data Sources Registry — Appendix A.1) |
| **Sub_Location** | §TBD |

|  |  |
|:---|:---|
| **Step 3.4 — Domain Expert(s) complete Structured Evaluation Form** |  |
| **Source_ID** | §TBD (Data Sources Registry — Appendix A.1) |
| **Executor_ID** | §USR_DOMAIN_EXPERT (User_ID Registry) |
| **Action_Type** | CREATE |
| **Object_Ref** | IMS-001 (AI Tool Evaluation & Approval Framework — IMS Document Register — Appendix C), §6.3 Structured Evaluation Form — Domain Expert |
| **Record_Object_ID** | Form A1 updated — evaluation form reference(s) per Domain Expert (Organisation Document Registry — Appendix B.2) |
| **Record_Source_ID** | §TBD (Data Sources Registry — Appendix A.1) |
| **Sub_Location** | §TBD |

<table style="width:100%;">
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<tbody>
<tr>
<td style="text-align: left;"><strong>Step 3.5 — GATE 3</strong></td>
<td style="text-align: left;"><strong>CONTROL POINT</strong></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Source_ID</strong></td>
<td style="text-align: left;">§TBD (Data Sources Registry — Appendix
A.1)</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Doc_Location</strong></td>
<td style="text-align: left;">IMS-001 (AI Tool Evaluation &amp; Approval
Framework — IMS Document Register — Appendix C), §6.4 criteria
G3.1–G3.3</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Executor_ID</strong></td>
<td style="text-align: left;">§USR_EVALUATOR (User_ID Registry)</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Decision_Maker</strong></td>
<td style="text-align: left;">§USR_EVALUATOR (User_ID Registry)</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Status_Code</strong></td>
<td style="text-align: left;"><p>• PASS → Stage 4</p>
<p>• FAIL → reject or return to Step 3.1 with modified test
brief</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Record_Object_ID</strong></td>
<td style="text-align: left;">Form A1 updated — Stage 3 summary report +
Gate 3 decision + date (Organisation Document Registry — Appendix
B.2)</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Record_Source_ID</strong></td>
<td style="text-align: left;">§TBD (Data Sources Registry — Appendix
A.1)</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Sub_Location</strong></td>
<td style="text-align: left;">§TBD</td>
</tr>
</tbody>
</table>

|                                       |
|:--------------------------------------|
| **STAGE 4A — Compilation & Approval** |

|  |  |
|:---|:---|
| **Step 4A.1 — Compile evaluation dossier** |  |
| **Source_ID** | §TBD (Data Sources Registry — Appendix A.1) |
| **Executor_ID** | §USR_EVALUATOR (User_ID Registry) |
| **Action_Type** | CREATE |
| **Object_Ref** | IMS-001 (AI Tool Evaluation & Approval Framework — IMS Document Register — Appendix C), §7.1 step 4.1 — compile: Gate 1 evidence, Gate 2 matrix, Stage 3 summary, domain expert forms |
| **Record_Object_ID** | Form A2 — AI Tool Evaluation Report, created: full evaluation dossier (Organisation Document Registry — Appendix B.2) |
| **Record_Source_ID** | §TBD (Data Sources Registry — Appendix A.1) |
| **Sub_Location** | §TBD |

<table style="width:100%;">
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<tbody>
<tr>
<td style="text-align: left;"><strong>Step 4A.2 — Head of AI Office
approval</strong></td>
<td style="text-align: left;"><strong>CONTROL POINT</strong></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Source_ID</strong></td>
<td style="text-align: left;">§TBD (Data Sources Registry — Appendix
A.1)</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Doc_Location</strong></td>
<td style="text-align: left;">IMS-001 (AI Tool Evaluation &amp; Approval
Framework — IMS Document Register — Appendix C), §7.1 step 4.2</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Executor_ID</strong></td>
<td style="text-align: left;">§USR_EVALUATOR (User_ID Registry)</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Decision_Maker</strong></td>
<td style="text-align: left;">§USR_HEAD_AI (User_ID Registry)</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Status_Code</strong></td>
<td style="text-align: left;"><p>• APPROVED → Step 4A.3</p>
<p>• REJECTED → record reason on Form A2 + end</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Record_Object_ID</strong></td>
<td style="text-align: left;">Form A2 updated — approval decision + date
(Organisation Document Registry — Appendix B.2)</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Record_Source_ID</strong></td>
<td style="text-align: left;">§TBD (Data Sources Registry — Appendix
A.1)</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Sub_Location</strong></td>
<td style="text-align: left;">§TBD</td>
</tr>
</tbody>
</table>

|  |  |
|:---|:---|
| **Step 4A.3 — Add tool to AI Registry** |  |
| **Source_ID** | §TBD (Data Sources Registry — Appendix A.1) |
| **Executor_ID** | §USR_EVALUATOR (User_ID Registry) |
| **Action_Type** | CREATE |
| **Object_Ref** | IMS-001 (AI Tool Evaluation & Approval Framework — IMS Document Register — Appendix C), §7.1 step 4.6 — register: tier, use cases, data boundary, dept, IT contact, review date |
| **Record_Object_ID** | AI Registry entry created — tier (Core/Functional), use cases, data boundary, dept, IT contact, review date (Organisation Document Registry — Appendix B.2) |
| **Record_Source_ID** | §TBD (Data Sources Registry — Appendix A.1) |
| **Sub_Location** | §TBD |

|                            |
|:---------------------------|
| **STAGE 4B — IT Handover** |

|  |  |
|:---|:---|
| **Step 4B.1 — Submit IT Handover request** |  |
| **Source_ID** | §TBD (Data Sources Registry — Appendix A.1) |
| **Executor_ID** | §USR_EVALUATOR (User_ID Registry) |
| **Action_Type** | SEND |
| **Object_Ref** | IMS-001 (AI Tool Evaluation & Approval Framework — IMS Document Register — Appendix C), §7.1 step 4.3 + §7.2 IT Handover Requirements |
| **Record_Object_ID** | Form A2 updated — IT Handover package reference (Organisation Document Registry — Appendix B.2) |
| **Record_Source_ID** | §TBD (Data Sources Registry — Appendix A.1) |
| **Sub_Location** | §TBD |

<table style="width:100%;">
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<tbody>
<tr>
<td style="text-align: left;"><strong>Step 4B.2 — IT security
review</strong></td>
<td style="text-align: left;"><strong>CONTROL POINT</strong></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Source_ID</strong></td>
<td style="text-align: left;">§TBD (Data Sources Registry — Appendix
A.1)</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Doc_Location</strong></td>
<td style="text-align: left;">IMS-001 (AI Tool Evaluation &amp; Approval
Framework — IMS Document Register — Appendix C), §7.1 step 4.4 — review:
SSO, network, licensing, support ownership</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Executor_ID</strong></td>
<td style="text-align: left;">§USR_IT (User_ID Registry)</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Decision_Maker</strong></td>
<td style="text-align: left;">§USR_IT (User_ID Registry)</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Status_Code</strong></td>
<td style="text-align: left;"><p>• CONFIRMED → Step 4B.4</p>
<p>• ISSUES RAISED → Step 4B.3</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Record_Object_ID</strong></td>
<td style="text-align: left;">§TBD — IT Security &amp; Readiness
Confirmation (Organisation Document Registry — Appendix B.2, Form_ID
§TBD — IT dept)</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Record_Source_ID</strong></td>
<td style="text-align: left;">§TBD (Data Sources Registry — Appendix
A.1)</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Sub_Location</strong></td>
<td style="text-align: left;">§TBD</td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<tbody>
<tr>
<td style="text-align: left;"><strong>Step 4B.3 — Resolve blocking
issues</strong></td>
<td style="text-align: left;"><strong>CONTROL POINT</strong></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Source_ID</strong></td>
<td style="text-align: left;">§TBD (Data Sources Registry — Appendix
A.1)</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Doc_Location</strong></td>
<td style="text-align: left;">IMS-001 (AI Tool Evaluation &amp; Approval
Framework — IMS Document Register — Appendix C), §7.1 step 4.5</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Executor_ID</strong></td>
<td style="text-align: left;">§USR_EVALUATOR + §USR_IT (User_ID
Registry)</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Decision_Maker</strong></td>
<td style="text-align: left;">§USR_HEAD_AI (User_ID Registry)</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Status_Code</strong></td>
<td style="text-align: left;"><p>• RESOLVED → Step 4B.4</p>
<p>• UNRESOLVABLE → escalate to §USR_HEAD_AI → record reason on Form A2
+ end</p></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Record_Object_ID</strong></td>
<td style="text-align: left;">Form A2 updated — resolution record or
rejection reason (Organisation Document Registry — Appendix B.2)</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Record_Source_ID</strong></td>
<td style="text-align: left;">§TBD (Data Sources Registry — Appendix
A.1)</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Sub_Location</strong></td>
<td style="text-align: left;">§TBD</td>
</tr>
</tbody>
</table>

|  |  |
|:---|:---|
| **Step 4B.4 — IT provisions accounts, SSO, infrastructure** |  |
| **Source_ID** | §TBD (Data Sources Registry — Appendix A.1) |
| **Executor_ID** | §USR_IT (User_ID Registry) |
| **Action_Type** | CREATE |
| **Sub_Process_Ref** | IT Provisioning & Deployment Process — Process_ID §TBD |
| **Object_Ref** | IMS-001 (AI Tool Evaluation & Approval Framework — IMS Document Register — Appendix C), §7.1 step 4.7 — provision accounts, SSO, infrastructure |
| **Record_Object_ID** | §TBD — Deployment Confirmation (Organisation Document Registry — Appendix B.2, Form_ID §TBD — IT dept) |
| **Record_Source_ID** | §TBD (Data Sources Registry — Appendix A.1) |
| **Sub_Location** | §TBD |

|                              |
|:-----------------------------|
| **STAGE 4C — Communication** |

|  |  |
|:---|:---|
| **Step 4C.1 — Publish Slack announcement \[FINAL ACT\]** |  |
| **Source_ID** | 3P (Slack Production — Data Sources Registry — Appendix A.1) |
| **Executor_ID** | §USR_EVALUATOR (User_ID Registry) |
| **Action_Type** | NOTIFY |
| **Object_Ref** | IMS-001 (AI Tool Evaluation & Approval Framework — IMS Document Register — Appendix C), §7.1 step 4.8 — announce: availability, permitted use cases, constraints |
| **Record_Object_ID** | Slack message permalink (system-assigned — 3P) |
| **Record_Source_ID** | 3P (Slack Production — Data Sources Registry — Appendix A.1) |
| **Sub_Location** | \#ai-tool-requests |

**3.4 Output Control**

> Not applicable — output quality controlled via in-process gate control
> points in Block 3.3 (Gates 1, 2, 3; Head of AI Office approval Step
> 4A.2; IT security review Step 4B.2).

**3.5 Activity End Point**

|  |  |
|:---|----|
| **Description** | AI tool evaluation completed — tool approved, registered in AI Registry, and announced via Slack \| OR evaluation rejected at any gate, reason recorded on Form A1/A2, requester notified via Slack |
| **Source_ID** | 3P (Slack Production — Data Sources Registry — Appendix A.1) |
| **Initiator_ID** | §USR_EVALUATOR (User_ID Registry) |
| **Record_Object_ID** | Form A2 — AI Tool Evaluation Report, final state (Organisation Document Registry — Appendix B.2) |
| **Record_Source_ID** | §TBD (Data Sources Registry — Appendix A.1) |
| **Sub_Location** | §TBD |

|                                  |
|:---------------------------------|
| **BLOCK 4. OUTPUTS & RECEIVERS** |

> Each output is paired with its receiver(s). For each row: the output
> artifact, its format and identifier, the receiving party, and the
> delivery channel.

|  |  |  |  |  |  |
|:---|:---|:---|:---|:---|:---|
| **Output** | **Entity Format** | **Object_ID** | **Receiver_ID** | **Source_ID (delivery)** | **Sub_Location** |
| Form A1 — AI Tool Intake Log (final state) | File — §TBD format | \[YYMMDD\]\_1A1\_\[AI Evaluator ID\]\_\[tool_name\] | 1A (AI Native — Org Doc Registry B.1) | §TBD (Data Sources Registry A.1) | §TBD |
|  |  |  | IT Provisioning & Deployment Process (Process_ID §TBD) | — | — |
| Form A2 — AI Tool Evaluation Report (approved path) | File — §TBD format | \[YYMMDD\]\_1A2\_\[AI Evaluator ID\]\_\[tool_name\] | 1A (AI Native — Org Doc Registry B.1) | §TBD (Data Sources Registry A.1) | §TBD |
|  |  |  | IT Provisioning & Deployment Process (Process_ID §TBD) | — | — |
|  |  |  | Training Process (Process_ID §TBD) — conditional | — | — |
| AI Registry entry (approved path) | Data — structured record: tier, use cases, data boundary, dept, IT contact, review date | §TBD — AI Registry system naming | §TBD — AI Registry system (Software Registry A.2) | §TBD (Data Sources Registry A.1) | §TBD |
| Slack announcement (approved path) | Data — Text | Slack message permalink (system-assigned — 3P) | §USR_REQUESTER (User_ID Registry) | 3P (Slack Production — Data Sources Registry A.1) | \#ai-tool-requests |
|  |  |  | All employees — 1A (AI Native — Org Doc Registry B.1) | 3P (Slack Production) | \#ai-tool-requests |
| Rejection notification (rejected path) | Data — Text | Slack message permalink (system-assigned — 3P) | §USR_REQUESTER (User_ID Registry) | 3P (Slack Production — Data Sources Registry A.1) | \#ai-tool-requests |

|                                                         |
|:--------------------------------------------------------|
| **VARIABLE REGISTRY — Open Items Pending Confirmation** |

**User IDs — pending User_ID Registry creation**

|  |  |  |
|:---|:---|:---|
| **Variable** | **Pending Registry** | **Description** |
| **§USR_REQUESTER** | *User_ID Registry (pending creation)* | Any employee submitting a tool request |
| **§USR_EVALUATOR** | *User_ID Registry (pending creation)* | AI Evaluator (AI & Technology Office) |
| **§USR_HEAD_AI** | *User_ID Registry (pending creation)* | Head of AI Office |
| **§USR_DOMAIN_EXPERT** | *User_ID Registry (pending creation)* | Subject-matter specialist |
| **§USR_IT** | *User_ID Registry (pending creation)* | IT Department representative |
| **§USR_DEPT** | *User_ID Registry (pending creation)* | Representative of the requesting department (department whose Domain Expert(s) participated in Stage 3) |

**Source IDs, Forms, Sub-Processes, and Document Locations — pending
resolution**

|  |  |  |
|:---|:---|:---|
| **Open Item** | **Registry / Document** | **Note** |
| **Storage system for Form A1** | *Data Sources Registry — Appendix A.1* | Pending platform selection |
| **Storage system for Form A2** | *Data Sources Registry — Appendix A.1* | Pending platform selection |
| **IT systems (Stage 4B)** | *Data Sources Registry — Appendix A.1* | Pending IT input |
| **IT Security & Readiness Confirmation** | *Organisation Document Registry — Appendix B.2* | IT dept form — Form_ID §TBD |
| **Deployment Confirmation** | *Organisation Document Registry — Appendix B.2* | IT dept form — Form_ID §TBD |
| **IMS-001 storage location** | *IMS Document Register — Appendix C* | Source_ID + Sub_Location §TBD |
| **IT Provisioning & Deployment Process** | *Process Register* | Process_ID §TBD |
| **Training Process** | *Process Register* | Process_ID §TBD |

*Note: External web sources (vendor websites, public documentation,
pricing pages) — internet/web environment, not registered as internal
source.*

*All §TBD variables must be resolved before this process map moves from
DRAFT to REVIEW status.*

|                                                    |
|:---------------------------------------------------|
| **PROCESS IMPROVEMENT REGISTER — Living Document** |

> Living improvement register for this process. Populate continuously —
> process owner adds operational observations; automation team adds
> technical improvements; IMS adds compliance requirements. Items feed
> into IMS Objectives (ISO 9001 cl. 6.2) and Management Review (ISO 9001
> cl. 9.3.2).

|  |  |  |  |  |  |  |  |
|:---|:---|:---|:---|:---|:---|:---|:---|
| **ID** | **Category** | **Description** | **Priority** | **ISO Reference** | **Owner** | **Status** | **Notes** |
| **1** | Process Documentation | Resolve all §TBD items: User_ID Registry (6 roles), Source_IDs for Form A1/A2 storage, Form_IDs for IT documents | High | *ISO 9001 cl. 7.5.3* | AI Evaluator | Proposed |  |
| **2** | Process Documentation | Add IT Department to Organisation Document Registry (Dept_ID §TBD) | High | *ISO 9001 cl. 7.5* | IMS/Compliance | Proposed |  |
| **3** | Process Documentation | Establish single forms album/repository for Form A1 and Form A2 instances | Medium | *ISO 9001 cl. 7.5.3* | AI Evaluator | Proposed |  |
| **4** | Process Documentation | Develop IT Provisioning & Deployment sub-process map | Medium | *ISO 9001 cl. 4.4* | IT Department | Proposed |  |
| **5** | Process Documentation | Develop Training Process sub-process map | Medium | *ISO 9001 cl. 7.2* | AI Evaluator | Proposed |  |
| **6** | Identification & Traceability | Create User_ID Registry — assign IDs to all 6 defined roles | High | *ISO 9001 cl. 7.5.3, ISO 27001 A.5.9* | IMS/Compliance | Proposed |  |
| **6b** | Identification & Traceability | Create Domain Experts Registry — assign IDs to domain experts by functional area; link to User_ID Registry | High | *ISO 9001 cl. 7.2, ISO 27001 A.5.9* | IMS/Compliance | Proposed |  |
| **7** | Identification & Traceability | Link User_ID to digital accounts (Slack, email, Linear) for full traceability chain | Medium | *ISO 27001 A.5.9* | IT Department | Proposed |  |
| **8** | Identification & Traceability | Register storage location for Form A1/A2 in Data Sources Registry once forms album established | High | *ISO 9001 cl. 7.5.3* | AI Evaluator | Proposed |  |
| **9** | Integration & Automation | Auto-check "Already in AIR?" at intake (Block 3.2) — query AI Registry via API | High | *ISO 42001 §8.4* | AI Evaluator | Proposed |  |
| **10** | Integration & Automation | Auto-route Slack \#ai-tool-requests message to Evaluator queue (Block 3.1→3.2) | High | *ISO 9001 cl. 4.4* | AI Evaluator | Proposed |  |
| **11** | Integration & Automation | Auto-create Form A1 draft from Slack message data (tool name, URL, requestor ID) | Medium | *ISO 9001 cl. 7.5, ISO 42001 §8.4* | AI Evaluator | Proposed |  |
| **12** | Integration & Automation | AI-assisted Gate 1 check: automate G1.1–G1.5 criteria verification via web research | Medium | *ISO 42001 §8.2, §8.4* | AI Evaluator | Proposed |  |
| **13** | Integration & Automation | Auto-notify §USR_REQUESTER on each gate decision via Slack | Medium | *ISO 9001 cl. 7.4* | AI Evaluator | Proposed |  |
| **14** | Data Security & Privacy | Classify Form A1/A2 data per information classification policy (ISO 27001 A.5.12) | High | *ISO 27001 A.5.12* | IMS/Compliance | Proposed |  |
| **15** | Data Security & Privacy | Define retention period for Form A1/A2 evaluation records | Medium | *ISO 27001 A.5.33, ISO 9001 cl. 7.5.3* | IMS/Compliance | Proposed |  |
| **16** | AI Governance | Confirm Gates 1–4 collectively satisfy ISO 42001 §8.2 AI System Impact Assessment requirement | High | *ISO 42001 §8.2* | AI Evaluator | Proposed |  |
| **17** | AI Governance | Document AI agent roles in evaluation process (Fireflies AI-03) per AI Models & Agents Registry | Medium | *ISO 42001 §8.3* | AI Evaluator | Proposed |  |
| **18** | Process Performance | Baseline KPI 3 target (tool adoption rate) after first reporting period; define N months measurement window | Medium | *ISO 9001 cl. 9.1, 9.3.2* | AI Evaluator | Proposed |  |
| **19** | Continual Improvement | Add Process_Ref attribute to Block 1 (upstream process) and Block 4 (downstream process) in template v9 | Low | *ISO 9001 cl. 10.3* | IMS/Compliance | Proposed |  |
| **20** | Continual Improvement | (empty row for process owner) |  |  |  |  |  |
| **21** | (empty for automation team) |  |  |  |  |  |  |
| **22** |  |  |  |  |  |  |  |

