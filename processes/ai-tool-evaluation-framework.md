---
type: process
title: AI Tool Evaluation & Approval Framework
slug: ai-tool-evaluation-framework
created: 2026-05-14
updated: 2026-05-19
departments: [ai-office, it-ops]
status: active
owner: michael-bruck
captured_by: jehad-altoutou
audience: [department]
sources: [ai-tool-evaluation-framework, marketing-stack-technical-writeup]
related: [ai-tool-evaluation, ai-registry, ai-native-mandate, ai-policy, stack-composition-framework, agentic-lean-marketing-stack]
---

The formal Janus Digital AI Tool Evaluation & Approval Framework (DRAFT v0.1, last updated 25 February 2026, owned by Office of the COO — AI & Technology). Supersedes Section 5.2.4 (Justification Protocol) and operationalises the [[ai-native-mandate]]'s procurement rule. The [[ai-tool-evaluation]] skill executes this framework in practice; the [[ai-registry]] is its output of record.

**Default posture.** No AI tool may be used by any employee unless formally approved and listed in the AI Registry. Burden of proof lies with the evaluation process.

## Four sequential gates

1. **Gate 1 — Initial Viability Screen (binary, all required).** G1.1 Google Workspace integration · G1.2 Slack integration · G1.3 Data portability · G1.4 Data training exclusion (contractual) · G1.5 Documented API. Any single failure is rejection.
2. **Gate 2 — Technical & Strategic Fit (structured).** Must-Have binary criteria: G2.1 MCP/AI orchestration compatibility · G2.2 Enterprise-grade SSO · G2.3 Vendor viability (24-month horizon; sole-founder hobby projects fail). Should-Have (scored 0-5): efficiency gain, ease of adoption, multi-platform access, audit trail, Gemini integration. Nice-to-Have (scored 0-5): workflow automation, competitive differentiation, cost efficiency. Pass = all Must-Have + Should-Have ≥15/25; Conditional Pass = Should-Have 10-14 with Head of AI Office discretion; Fail otherwise.
3. **Gate 3 — Operational Validation.** Sandbox provisioning + test brief + 3-5 working days of domain-expert use + Structured Evaluation Form completion. G3.1 ≥50% positive domain-expert recommendation · G3.2 zero critical defects · G3.3 viable workflow integration path (no unsanctioned parallel processes).
4. **Gate 4 — Approval & Registry Listing.** Evaluator compiles dossier → Head of AI Office final approval → IT Department handover (security review, SSO/identity provisioning, network/firewall, licence/billing, first-level support ownership) → AI Registry listing (tier, use cases, data boundary, department, IT contact, 3-month review date) → Slack AI Hub announcement.

## Ongoing review triggers

- Scheduled review every 3 months from listing date (full re-evaluation from Stage 2).
- Vendor material change (acquisition, pricing, ToS, data policy) → immediate re-evaluation.
- Security incident → immediate suspension pending investigation.
- Obsolescence by a superior approved alternative → de-listing review.

The document includes a flowchart node/edge reference (N01-N34) ready for translation into BPMN.

## Proposed pre-G1 filter — [[stack-composition-framework|Stack Composition Framework]]

A pre-G1 layer was proposed on 2026-05-19 in the [[marketing-stack-technical-writeup|marketing stack technical writeup]] (Michael → Jehad) and validated by the [[agentic-lean-marketing-stack|agentic-lean marketing stack]] selections. The framework adds three lenses — **composability**, **agent operability**, **reversibility** — scored 0–3 before G1.

- **3/3** → preferred default, proceeds to G1 normally.
- **2/3** → proceeds with a documented trade-off attached to the evaluation.
- **1/3** or **0/3** → rejected before G1 runs, saving evaluator hours.

The three lenses overlap partially with existing gate criteria (agent operability ↔ G2.1 MCP compatibility; reversibility ↔ G1.3 data portability). The pre-filter framing avoids double-evaluation by making these lenses an entry condition rather than a scored criterion downstream. Status: **proposed**, not yet ratified — Michael to formalise as a framework amendment when the holistic MarTech vendor assessment for [[bonaventure-wong]] lands.
