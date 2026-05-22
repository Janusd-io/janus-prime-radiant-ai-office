---
type: concept
title: Sandbox to production handover
slug: sandbox-to-production-handover
created: 2026-05-06
updated: 2026-05-22
captured_by: jehad-altoutou
departments: [ai-office, it-ops, iso]
status: active
sources: [2026-05-06-ai-and-it-department-meeting, section-5-ai-charter-policy-v2.1]
related: [sandbox-environment, ai-policy, ai-tool-evaluation-framework, ai-policy-gate-approval, ai-registry]
---

# Sandbox to production handover

The procedural step that moves a tool or internal solution **out of the [[sandbox-environment|Sandbox Environment]] into production**. Codified in §5.5.3 of the [[ai-policy|AI Policy v2.1]] as a *deliberate, documented act* via the relevant gate process — Gate 3 for third-party tools (per [[ai-tool-evaluation-framework]]), formal Acceptance testing for internally developed solutions (per §5.6 pipeline). **Not an informal transition.**

The handover for third-party tools includes the §5.4 Stage 4 sub-gates:

- **Sub-Gate A — Head of AI Office approval** based on the full evaluation dossier (Gate 1–3 evidence + Stage 3 domain expert report).
- **Sub-Gate B — IT Department handover** covering identity and access configuration (SSO / Microsoft Entra), network and firewall provisioning, licence management, and L1 support ownership.

Operational detail for the reusable Sub-Gate B handover lives in [[ai-policy-gate-approval]].

## Current SOP gap

Originally flagged in the 2026-05-06 AI ↔ IT department meeting as a procedure gap — *"Procedure gap explicitly named; awaiting SOP, training, tests, sign-off."* The AI Policy v2.1 (30 March 2026) now codifies the *what* (Stage 4 Sub-Gates A + B); the operational SOP — runbooks, sign-off templates, training requirements, test gates — is still being authored on the IT/Ops side.

The [[ai-policy-gate-approval]] process page captures the AIO-side framing; the IT-side SOP is the missing complement. Worth tracking as a workstream item until the SOP is published.

## Related

- [[sandbox-environment]] — the venue.
- [[ai-policy]] — §5.5.3 (this rule) + §5.4.5 (the gate process).
- [[ai-tool-evaluation-framework]] — the upstream four-stage framework.
- [[ai-policy-gate-approval]] — the reusable governance process for Sub-Gate B.
