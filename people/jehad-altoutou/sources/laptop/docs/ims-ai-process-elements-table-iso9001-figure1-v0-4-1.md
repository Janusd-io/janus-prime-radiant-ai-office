---
type: source
source_type: laptop
title: IMS-AI-Process_Elements_Table_ISO9001_Figure1_v0.4 (1)
slug: ims-ai-process-elements-table-iso9001-figure1-v0-4-1
created: 2026-05-08
captured_by: jehad-altoutou
audience: personal
original_path: /Users/jehad/Downloads/IMS-AI-Process_Elements_Table_ISO9001_Figure1_v0.4 (1).docx
original_size: 32824
original_ext: .docx
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:49Z"
sensitivity: dept
sensitivity_confidence: 0.90
sensitivity_reason: "ISO 9001 process elements table for AI Tools management — clearly dept-wide IMS/ISO work product"
---

# IMS-AI-Process_Elements_Table_ISO9001_Figure1_v0.4 (1)

_Extracted from `Downloads/IMS-AI-Process_Elements_Table_ISO9001_Figure1_v0.4 (1).docx` on 2026-05-14._

**Process Elements Table according to ISO 9001 Figure 1 Logic**

**Process: Management of Internal AI Tools**

*Process document reference: IMS-PRC-AI-001*

**Form / record code legend**

| **Code** | **Form / Record name**                                       |
|----------|--------------------------------------------------------------|
| **F1**   | AI Tool Request Form                                         |
| **F2**   | Stage 1 Intake and Triage Record                             |
| **F3**   | Stage 2 Technical Qualification Record                       |
| **F4**   | Stage 3 Sandbox Test Brief and Domain Expert Evaluation Form |
| **F5**   | Stage 4 Approval Decision Record                             |
| **F6**   | IT Readiness Confirmation                                    |
| **F7**   | AI Tools Register Entry Template                             |
| **F8**   | Re-evaluation, Suspension or De-listing Record               |

*Note: Gate decisions are recorded as outputs and control results within
the relevant process stage. They are not shown as separate process
activities.*

<table style="width:91%;">
<colgroup>
<col style="width: 1%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 12%" />
<col style="width: 16%" />
<col style="width: 12%" />
<col style="width: 11%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr>
<th><strong>No.</strong></th>
<th><strong>Process stage</strong></th>
<th><strong>Sources of inputs / resources</strong></th>
<th><strong>Input document / record</strong></th>
<th><strong>Process activity / control</strong></th>
<th><strong>Output document / record</strong></th>
<th><strong>Receivers of outputs</strong></th>
<th><strong>Monitoring / measurement / control</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td><strong>Request / Proposal</strong></td>
<td><p><mark>Department Head</mark></p>
<p>Slack</p></td>
<td>F1 - AI Tool Request Form. The form records the request type,
business need, proposed or required AI tool, intended users, expected
data to be used and expected business benefit.</td>
<td>The request is submitted and registered according to IMS-PRC-AI-001
Management of Internal AI Tools, section 6.1, and routed to AI
Department for initial review.</td>
<td>Completed F1 - AI Tool Request Form. If the request concerns access
to an already approved tool, the process may be routed directly to
access confirmation and user guidance.</td>
<td>AI Department / Evaluator.</td>
<td>Request completeness is checked. If the business need, intended
users, expected data or expected benefit are unclear, the request is
returned to the requester for clarification.</td>
</tr>
<tr>
<td>2</td>
<td><strong>Stage 1 - Intake and Triage</strong></td>
<td>AI Department / Evaluator; requester;</td>
<td>Completed F1 - AI Tool Request Form; available tool link, vendor
website, public description, pricing or integration information.</td>
<td>AI Department performs intake and triage according to
IMS-PRC-AI-001, section 6.1 and Appendix A - AI Tool Evaluation and
Approval Methodology. The candidate is identified, classified and
checked for basic viability.</td>
<td>F2 - Stage 1 Intake and Triage Record, including Stage 1 result and
Gate 1 decision: Pass / Fail / More information required.</td>
<td>AI Department; requester; Head of AI Native if escalation is
required.</td>
<td>Gate 1 control is performed within Stage 1. The evaluator checks
whether the tool is relevant, sufficiently described, not obviously
unsuitable and has minimum information available for further evaluation.
Rejection or return for clarification must be recorded in F2.</td>
</tr>
<tr>
<td>3</td>
<td><strong>Stage 2 - Technical Qualification</strong></td>
<td>AI Department / Evaluator; vendor documentation; available trial or
demo access; technical documentation.</td>
<td>F2 - Stage 1 Intake and Triage Record with Gate 1 pass; vendor
documentation; authentication information; integration information; data
export information; pricing information; logging / audit trail
information where available.</td>
<td>AI Department performs technical qualification according to
IMS-PRC-AI-001, section 6.1 and Appendix A. The evaluator reviews
technical and strategic fit, including minimum requirements, usability,
integration, auditability, vendor viability and cost
reasonableness.</td>
<td>F3 - Stage 2 Technical Qualification Record, including Gate 2
decision: Pass / Conditional Pass / Fail and summary of key risks,
limitations and required conditions.</td>
<td>AI Department; Head of AI Native; Department Head where relevant;
requester if rejected or more information is required.</td>
<td>Gate 2 control is performed within Stage 2. Minimum criteria must be
met before sandbox testing. Conditional pass must state conditions and
required escalation. Failure must include documented reason in F3.</td>
</tr>
<tr>
<td>4</td>
<td><strong>Stage 3 - Sandbox and Domain Expert Evaluation</strong></td>
<td>AI Department / Evaluator; Domain Expert; Department Head; approved
test environment.</td>
<td>F3 - Stage 2 Technical Qualification Record with Gate 2 pass or
conditional pass; defined use case; approved test tasks; permitted
non-sensitive or synthetic data.</td>
<td>AI Department prepares controlled sandbox testing according to
IMS-PRC-AI-001, section 6.1 and Appendix A. Domain Expert performs
testing using only approved test data and records practical feedback on
output quality, usability, limitations and risks.</td>
<td>F4 - Stage 3 Sandbox Test Brief and Domain Expert Evaluation Form,
including test brief, domain expert feedback, test results and Gate 3
recommendation / decision: Pass / Fail / Return for re-test.</td>
<td>AI Department / Evaluator; Head of AI Native; Department Head;
requester if rejected or returned for further testing.</td>
<td>Gate 3 control is performed within Stage 3. The evaluator checks
whether the tool works for the intended use case, whether there are
critical defects, whether output quality is acceptable and whether the
tool can be integrated into the workflow without creating uncontrolled
parallel processes.</td>
</tr>
<tr>
<td>5</td>
<td><strong>Stage 4 - Approval Decision</strong></td>
<td>AI Department / Evaluator; Head of AI Native / Head of AI Office;
Department Head; IT / Security / Legal where applicable.</td>
<td>Evaluation dossier consisting of F1, F2, F3, F4, vendor
documentation and any required review comments or conditions.</td>
<td>AI Department compiles the evaluation dossier and presents the
recommendation for final decision according to IMS-PRC-AI-001, section
6.1 and Appendix A. The approval authority decides whether the tool may
be approved, approved with conditions, rejected or put on hold.</td>
<td>F5 - Stage 4 Approval Decision Record, including final decision,
approved use cases, prohibited use cases, data boundary, restrictions,
approved users/departments, required training and review date.</td>
<td>AI Department; IT; requester; Department Head; approved users where
applicable.</td>
<td>Final approval control is performed at Stage 4. No tool may proceed
to production use unless the approval decision is recorded in F5 and all
mandatory restrictions and conditions are defined.</td>
</tr>
<tr>
<td>6</td>
<td><strong>IT Readiness / Deployment Preparation</strong></td>
<td>IT Department; AI Department; approved users / departments.</td>
<td>Approved F5 - Stage 4 Approval Decision Record; deployment
requirements; user access scope; authentication requirements; licensing
information; support requirements.</td>
<td>IT readiness is confirmed according to IMS-PRC-AI-001, section 6.1
and the applicable IT handover requirements. IT confirms work accounts,
access provisioning, authentication, support ownership, licence /
billing and any required configuration.</td>
<td>F6 - IT Readiness Confirmation, including readiness decision: Ready
/ Ready with conditions / Blocked.</td>
<td>AI Department; IT Department; Head of AI Native; Department
Head.</td>
<td>No production use is permitted until blocking IT issues are resolved
or escalated. Personal accounts are not permitted. Access must be
limited to approved users, departments and use cases.</td>
</tr>
<tr>
<td>7</td>
<td><strong>AI Tools Register Listing</strong></td>
<td>AI Department / Register owner; IT Department; approval
authority.</td>
<td>Approved F5 - Stage 4 Approval Decision Record; completed F6 - IT
Readiness Confirmation; approved restrictions and review date.</td>
<td>AI Department updates the official AI Tools Register according to
IMS-PRC-AI-001, section 6.1. The tool is listed only with its approved
use cases, restrictions, data boundary, users/departments, owner, IT
support contact and review date.</td>
<td>F7 - AI Tools Register Entry Template, completed and added to the
official AI Tools Register.</td>
<td>Approved users; Department Heads; IT; IMS / Compliance; AI
Department.</td>
<td>Register control: the tool is not considered approved for use until
the relevant F7 entry is completed and available in the official AI
Tools Register.</td>
</tr>
<tr>
<td>8</td>
<td><strong>Production Use / Implementation</strong></td>
<td>Approved users; Department Heads; AI Department; IT Department.</td>
<td>Completed F7 - AI Tools Register Entry Template; approved use cases;
restrictions; user guidance; work account access.</td>
<td>Approved users use the AI tool only within the approved use cases,
data boundary and restrictions defined in F5 and F7. AI Department and
Department Heads ensure users understand permitted and prohibited
use.</td>
<td>User access confirmation and, where applicable, training / guidance
record. If a separate training form is not used, completion is recorded
in the approved system or register.</td>
<td>Approved users; Department Heads; AI Department; IT.</td>
<td>Use is monitored against approved restrictions. Any misuse,
incident, unclear use case or request to expand use must trigger
reassessment or additional approval.</td>
</tr>
<tr>
<td>9</td>
<td><strong>Ongoing Review, Re-evaluation, Suspension or
De-listing</strong></td>
<td>AI Department; IT; Security; Legal / Compliance where applicable;
approved users; vendor notifications; incident records.</td>
<td>F7 - AI Tools Register Entry Template; usage feedback; incident
record; vendor material change notice; scheduled review date; new use
case request; new data type request.</td>
<td>AI Department reviews the approved tool according to IMS-PRC-AI-001,
section 6.1 and Appendix A. Re-evaluation is triggered by scheduled
review, vendor change, incident, obsolescence, new use case, new data
type or other significant change.</td>
<td>F8 - Re-evaluation, Suspension or De-listing Record, including
decision: Continue / Continue with restrictions / Reassess / Suspend /
Withdraw. Updated F7 if the register status changes.</td>
<td>AI Department; IT; affected users; Department Heads; IMS /
Compliance; Top Management if required.</td>
<td>Review control: decisions must be recorded in F8 and reflected in
F7. Suspended or withdrawn tools must be communicated to affected users,
but Slack/email are only notification channels and not official approval
records.</td>
</tr>
</tbody>
</table>

Use of the table: This table aligns the process stages with ISO 9001
Figure 1 process elements: sources of inputs, inputs, activities,
outputs, receivers, and monitoring/control points. It is intended for
inclusion in IMS-PRC-AI-001 and future workflow design.
