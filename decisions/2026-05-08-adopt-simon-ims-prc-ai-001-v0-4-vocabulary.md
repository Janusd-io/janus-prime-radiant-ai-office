---
type: decision
title: Adopt Simon's IMS-PRC-AI-001 v0.4 vocabulary for the v0.5 AI Tool Evaluation doc
slug: 2026-05-08-adopt-simon-ims-prc-ai-001-v0-4-vocabulary
created: 2026-05-08
updated: 2026-05-14
status: active
owner: jehad-altoutou
decided_by: jehad-altoutou
captured_by: jehad-altoutou
audience: department
departments: [ai-office, iso]
sources: [10-gap-analysis-vs-simon, simon-ims-prc-ai-001-v0-4, 08-tool-evaluation-procedure]
related: [iso-compliance-programme, iso-ims-puls, ai-tool-evaluation, ai-registry, simon-tarskih, 2026-05-08-ims-prc-ai-001-gap-analysis-3-dev-days-to-align]
---

# Adopt Simon's IMS-PRC-AI-001 v0.4 vocabulary for the v0.5 AI Tool Evaluation doc

**Decision (2026-05-08):** Re-shape Janus's internal AI Tool Evaluation Procedure (`08-TOOL-EVALUATION-PROCEDURE`) to align with Simon's formal IMS-PRC-AI-001 v0.4 template — adopting his 9-stage process structure, F1-F8 form codes, 3-gate distribution, and explicit approval-authority roles. Target: v0.5 draft to Simon by 15 May 2026.

## Why

Per the [[2026-05-08-ims-prc-ai-001-gap-analysis-3-dev-days-to-align|gap analysis]], ~70% of our content already matches Simon's structure. The ~30% delta is mostly vocabulary plus one functional gap (Stage 9 lifecycle review). Closing it pre-emptively means the auditor sees one IMS shape across Janus rather than ten departmental dialects.

## Scope of the change

- Re-distribute our 4 evaluation gates across Simon's 3 stages (Intake / Technical / Sandbox)
- Add Stage 9 (Ongoing Review / Suspension / De-listing) — currently missing
- Map Linear AIR comments + Notion templates + Slack workflow forms to F1-F8 form codes (digital mapping, not PDFs)
- Introduce Domain Expert as a named two-tier role (Requester for simple cases; designated Domain Expert for cross-functional)
- Lock approval-authority hierarchy with Michael — Head of AI Native / Head of AI Office / Department Head / IT-Security-Legal
- Adopt IMS-PRC-AI-NNN naming codes; clarify Slack/email = notifications only; add personal-accounts-not-permitted control; add user-guidance receipt record

## Alternatives considered

- **Keep our own structure** — rejected; creates audit friction and undermines the "one IMS shape" promise the auditor will look for.
- **Wait until Simon publishes v0.5** — rejected; we have working operational documentation today, blocking on Simon stalls the entire AI-Ops compliance evidence chain.

## Effort

~3 dev-days total, of which one half-day requires [[michael-bruck]]'s input on the role mapping.

## Status

Active — awaiting Simon's confirmation on F-code physical/digital question (#1 of the open questions list) and on the HR architecture recommendation (Option 1 with migration trigger to Option 2).
