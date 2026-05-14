---
type: source
source_type: laptop
title: simon-ims-prc-ai-001-v0.4
slug: simon-ims-prc-ai-001-v0-4
created: 2026-05-11
captured_by: jehad-altoutou
audience: personal
original_path: /Users/jehad/Documents/janus-puls-onboarding/skills/ims-enrolment/references/simon-ims-prc-ai-001-v0.4.md
original_size: 4702
original_ext: .md
category: notes
extracted_with: text-copy
extracted_at: "2026-05-14T09:51:46Z"
sensitivity: dept
sensitivity_confidence: 0.90
sensitivity_reason: "ISO/IMS reference doc — Simon's formal template summary; work content"
project: janus-puls-onboarding

---

# simon-ims-prc-ai-001-v0.4

> Part of [[janus-puls-onboarding|Janus PULS Onboarding]] — captured by /janus-brain.

_Extracted from `Documents/janus-puls-onboarding/skills/ims-enrolment/references/simon-ims-prc-ai-001-v0.4.md` on 2026-05-14._

# Simon's IMS-PRC-AI-001 v0.4 — Summary

> Summary of the formal IMS process document template Simon (ISO Lead) is using. Source: `IMS-AI-Process_Elements_Table_ISO9001_Figure1_v0.4.docx`. Read this to understand the **vocabulary, structure, and formality** Simon expects in IMS-grade documentation.

## The document

- **Title:** Process Elements Table according to [[iso-9001-figure-1|ISO 9001 Figure 1]] Logic
- **Process:** Management of Internal AI Tools
- **Document reference:** IMS-PRC-AI-001
- **Format:** Table with 9 numbered process stages

## The 9 stages

| # | Process stage | Form (output record) |
|---|---|---|
| 1 | Request / Proposal | F1 — AI Tool Request Form |
| 2 | Stage 1 — Intake and Triage (Gate 1) | F2 — Stage 1 Intake and Triage Record |
| 3 | Stage 2 — Technical Qualification (Gate 2) | F3 — Stage 2 Technical Qualification Record |
| 4 | Stage 3 — Sandbox and Domain Expert Evaluation (Gate 3) | F4 — Stage 3 Sandbox Test Brief and Domain Expert Evaluation Form |
| 5 | Stage 4 — Approval Decision | F5 — Stage 4 Approval Decision Record |
| 6 | IT Readiness / Deployment Preparation | F6 — IT Readiness Confirmation |
| 7 | AI Tools Register Listing | F7 — AI Tools Register Entry Template |
| 8 | Production Use / Implementation | (training / guidance record) |
| 9 | Ongoing Review, Re-evaluation, Suspension or De-listing | F8 — Re-evaluation, Suspension or De-listing Record |

## Key conventions Simon uses

| Convention | Detail |
|---|---|
| **Process code** | `IMS-PRC-XXX-NNN` (e.g., IMS-PRC-AI-001 for the AI tools process) |
| **Form codes** | `F1`–`F8` — every stage produces a numbered record |
| **Gate decisions** | Recorded as **outputs and control results within the relevant stage**, not as separate process activities |
| **Approval authority** | Named explicitly per stage — Head of AI Native, Head of AI Office, Department Head, IT/Security/Legal as relevant |
| **Slack/email** | "Notification channels only — **not** official approval records" |
| **Personal accounts** | "Not permitted. Access must be limited to approved users, departments, and use cases." |
| **Appendix A** | References "Appendix A — AI Tool Evaluation and Approval Methodology" for detailed gate criteria |
| **Domain Expert** | Explicit role in Stage 3 — performs sandbox testing with approved test data |

## What this means for departments using `/ims-enrolment`

If your department's process is going to slot into Simon's IMS, your documentation should:

1. **Be structured as a 9-stage process** when describing a multi-stage workflow (intake → triage → evaluation → approval → deployment → use → review)
2. **Define output records** for every stage (the equivalent of F1-F8 in your domain)
3. **Name approval authorities** with specific roles, not "the team"
4. **Treat Slack/email as notifications**, not approval records
5. **Reference your equivalent of "Appendix A"** for detailed evaluation methodology — even if it lives in a separate document (an MCP skill, an internal SOP, etc.)
6. **Include re-evaluation / sunset** as the final stage — every tool, every process must have a path to retirement

## Mapping our existing AI Department documents to Simon's structure

| Simon's stage | Our equivalent in the AI Department worked example |
|---|---|
| 1. Request / Proposal | Path A (meeting via `/standup`) or Path B (Slack request) in `sub-process-tool-evaluation.md` |
| 2. Stage 1 — Intake & Triage | `/ai-registry` performs intake; Gate 1 control |
| 3. Stage 2 — Technical Qualification | Gate 2 in our 4-gate model (we'd collapse to 3 to match Simon) |
| 4. Stage 3 — Sandbox & Domain Expert | Sandbox + [[5-area-stress-test|5-area stress test]] (Domain Expert = requester for simple cases, designated SME for complex) |
| 5. Stage 4 — Approval Decision | Decision point at end of evaluation + requester sign-off |
| 6. IT Readiness | Handover package to IT department |
| 7. AI Tools Register Listing | [[linear|Linear]] AIR status → Active |
| 8. Production Use | Tool live · all employees have access |
| 9. Ongoing Review | **Currently a gap in our docs** — needs Stage 9 added |

See [10-GAP-ANALYSIS-vs-SIMON.md](https://[[github|github]].com/Jehada-Janusd/janus-puls-onboarding/blob/main/10-GAP-ANALYSIS-vs-SIMON.md) in the GitHub repo for the full mapping and gap analysis.

## When in doubt

Simon's vocabulary > our vocabulary. If a department's document conflicts with Simon's IMS-PRC-AI-001 conventions, **defer to Simon's** unless there's a strong domain-specific reason to deviate (in which case, document the deviation in the Open Items section).

## Source

`/Users/jehad/Desktop/IMS-AI-Process_Elements_Table_ISO9001_Figure1_v0.4.docx`
