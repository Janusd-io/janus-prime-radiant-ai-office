---
type: source
title: AI Tool Evaluation — Process Diagram (Level 1 swimlane)
slug: ai-tool-evaluation-diagram
created: 2026-06-09
updated: 2026-06-09
source_type: diagram
source_origin: Google Drive — ISO/IMS department (Simon Tarskih)
document_id: DIAG-PROC-AIToolEvaluation
document_version: v0.1
document_status: DRAFT
captured_by: jehad-altoutou
departments: [ai-office, ims-compliance]
related: [ai-tool-evaluation-process-map, ims-process-visualization-standard, ims-digital-twin]
ingested_in_full: true
---

> Text labels extracted from the editable `.drawio` source (raw file at `iso/sources/_assets/DIAG-PROC-AIToolEvaluation-v0.1-2026-06-05.drawio`). 5 swimlanes (Requester, AI Evaluator, Domain Expert, IT, Head of AI Office), full flow with escalation + conditional approval. ISO 9001 cl.6.1 / ISO 27001 A.5.9 / ISO 42001 §8.2.

## Node labels (in order)

- AI Tool Evaluation & Approval — Process Diagram  |  PROC-IMS-AIToolEvaluation  |  v0.1  |  2026-06-05  |  DRAFT  |  Owner: Office of the COO — AI & Technology  |  ISO 9001 cl. 6.1 / ISO 27001 A.5.9 / ISO 42001 §8.2
- Requester&#xa;(Any Employee)
- AI Evaluator&#xa;(AI & Technology Office)
- Domain Expert&#xa;(Relevant Department)
- IT Department
- Head of AI Office
- Incoming Request&#xa;Source: 3P (Slack&#xa;#ai-tool-requests)
- Tool Mention&#xa;in Meeting&#xa;Source: AI-03 (Fireflies)
- START
- Request data&#xa;complete & valid?
- Form 1A1&#xa;AI Tool Intake Log&#xa;[CREATE]
- Notification:&#xa;request rejected /&#xa;requires clarification
- STAGE 1: Intake & Triage&#xa;1.1 Log candidate&#xa;1.2 Classify: Tool / Infrastructure&#xa;1.3 Rapid desk review (vendor documentation)&#xa;Source: §TBD System
- Form 1A1&#xa;UPDATE:&#xa;classification,&#xa;triage summary
- All criteria&#xa;G1.1–G1.5&#xa;met?
- Form 1A1&#xa;UPDATE:&#xa;G1 decision + date&#xa;+ evidence references
- Notification:&#xa;failed&#xa;G1 criteria
- STAGE 2: Technical Qualification&#xa;2.1 Detailed technical review&#xa;2.2 Score against G2.1–G2.11 matrix&#xa;Source: §TBD System (external sources)
- Form 1A1&#xa;UPDATE:&#xa;technical review,&#xa;G2 matrix
- All Must Have&#xa;+ Should Have&#xa;≥15/25?
- Form 1A1&#xa;UPDATE:&#xa;G2 decision + date
- Conditional Approval&#xa;Head of AI Office&#xa;(Should Have 10–14/25)&#xa;Source: §TBD
- Notification:&#xa;failed&#xa;G2 criteria
- STAGE 3: Sandbox Preparation&#xa;3.1 Provision sandbox (Tier 3)&#xa;3.2 Define test brief&#xa;3.5 Aggregate findings&#xa;Source: §TBD Sandbox
- STAGE 3: Domain Expert Testing&#xa;3.3 Execute test brief&#xa;(3–5 working days)&#xa;3.4 Complete evaluation form&#xa;Source: §TBD System
- Form 1A1&#xa;UPDATE:&#xa;Stage 3 summary,&#xa;form references
- Majority of experts&#xa;recommend + no&#xa;critical defects?
- Form 1A1&#xa;UPDATE:&#xa;G3 decision + date
- Notification:&#xa;failed&#xa;Stage 3 review
- STAGE 4A: Compilation & Approval&#xa;4A.1 Compile full evaluation dossier&#xa;Source: §TBD System
- Form 1A2&#xa;AI Tool Evaluation&#xa;Report [CREATE]
- Head of AI Office&#xa;approves?
- Form 1A2&#xa;UPDATE:&#xa;decision + date
- 4A.3 Add to AI Registry&#xa;(tier, use cases, data boundary, IT contact)&#xa;Source: §TBD AI Registry
- AI Registry&#xa;Source: §TBD
- Notification:&#xa;final&#xa;rejection
- STAGE 4B: IT Handover&#xa;Security review, SSO, deployment&#xa;Source: §TBD IT System&#xa;&#xa;          [ + ]
- STAGE 4C: Announcement&#xa;4C.1 Publish to Slack #ai-tool-requests&#xa;Source: 3P (Slack Production)
- Outcome&#xa;Notification&#xa;(Slack)
- END&#xa;Approved
- END&#xa;Rejected
- LEGEND:  [Oval] Start / End     [Rectangle] Activity/Stage     [Diamond] Decision Point — question determines next path     [Document ≋] Record created / updated     [Cylinder] Data Store / Registry     [Parallelogram] Input / Output data     [Envelope] Notification     [Dashed+] Sub-process     ——  Main flow     - - -  Conditional / Rejection path
- YES — data valid
- YES — all G1 met
- YES — PASS
- parallel
- YES
- YES
- CONDITIONAL — Should Have 10-14
- Approved
- Rejected
- NO — request unclear
- NO
- NO — FAIL
- NO
- NO
- Escalation: request clarification&#xa;Dept Head (1A) consulted&#xa;Source: 3P (Slack)
