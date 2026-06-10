---
type: concept
title: IMS Documentation Hierarchy (L1–L6)
slug: ims-documentation-hierarchy
created: 2026-06-10
updated: 2026-06-10
departments: [ai-office, iso]
captured_by: jehad-altoutou
confidence: high
sources: [ims-doc-system-hierarchy]
related: [ims-digital-twin, iso-ims-puls, unified-process-design-template, ims-process-register, ims-process-visualization-standard, three-iso-standards, simon-tarskih]
tags: [iso, ims, documentation, hierarchy]
status: active
---
# IMS Documentation Hierarchy (L1–L6)

Six-level pyramid defining every documentation type in the Janus IMS, received from [[simon-tarskih|Simon]] on 2026-06-10 ([[ims-doc-system-hierarchy|source]]). This is the structural backbone the entire document set hangs off — each artefact in the IMS has exactly one home level, and audit evidence flows bottom-up.

| Level | Name | Contains |
|---|---|---|
| **L1** | Strategic — Policies & Objectives | Policies (top-management framework + commitment to improvement) · Objectives (measurable, monitored, communicated results) |
| **L2** | System & Process — IMS Description & Architecture | Management System Manual · Process Maps (inputs, outputs, sequence, interaction) · Organizational Charts |
| **L3** | Operational — Procedures & Work Instructions | Procedures (the established way to carry out a process) · Work Instructions (detailed task-level how-to) |
| **L4** | Data Capture — Forms & Checklists | Forms and checklists that record compliance data |
| **L5** | Evidence — Records | Retained documented information proving processes run as planned |
| **L6** | External Documentation | Documents of external origin the IMS depends on — must be identified and controlled |

## How Simon's existing document set maps onto the levels

As of 2026-06-10 (per the [[ims-readiness-assessment-2026-06-08|2026-06-08 readiness assessment]], all DRAFT):

- **L1** — the 11 IMS Manual policies (planned; see [[iso-ims-puls]]) and the unified IMS privacy policy (pending UAE/Singapore legal research). The canonical AI Policy v2.1 (Section 5 AI Charter) is an existing L1 artefact.
- **L2** — [[ims-process-register]] (the 41-process inventory), the process maps produced from [[unified-process-design-template]], swimlane diagrams per [[ims-process-visualization-standard]], and the future Management System Manual.
- **L3** — the per-process procedure content inside each Unified Process Design document (activities, gate criteria); the `/ims-enrolment` skill generates L2+L3 content for departments.
- **L4** — Simon's form codes (F1–F8 in IMS-PRC-AI-001); digital-equivalent mapping (Linear AIR comments, Notion templates, Slack forms) still an open question ([[ims-open-questions-for-simon|Q2]]).
- **L5** — records produced by the running processes (Linear AIR issue history, Monday task trails, Notion standup logs are the natural digital record surfaces).
- **L6** — the ISO standards themselves, GDPR/PDPA legal texts, client-imposed requirements.

## Why it matters

This hierarchy gives the [[ims-digital-twin]] its vertical axis: the two templates and the visualization standard are L2/L3 *tooling*, the 41 processes are L2/L3 *content*, and audit readiness is demonstrated when L4 forms feed L5 records that trace back to L1 policy commitments. When drafting any new IMS artefact, name its level first — it determines who approves it, how it's controlled, and what evidence it must generate.

## Related

[[iso-ims-puls]] · [[ims-digital-twin]] · [[ims-process-register]] · [[unified-process-design-template]] · [[three-iso-standards]]
