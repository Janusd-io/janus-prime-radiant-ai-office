---
type: concept
title: AI Registry
slug: ai-registry
created: 2026-05-15
updated: 2026-05-15
captured_by: jehad-altoutou
audience: department
departments: [ai-office]
sensitivity: dept
sensitivity_confidence: 1.0
---

# AI Registry

The **AI Registry** (formally `Janusd Linear → AI Registry team`, identifier prefix `AIR-N`) is Janus Digital's system of record for every AI tool the company has evaluated, deployed, rejected, or is tracking. Every entry is one Linear issue with a fixed workflow: **Backlog → Evaluating → Sandbox → Production → Monitor**, with side states **Deprecated**, **Rejected**, and **Duplicate**.

> The AI Registry is the source of truth. Vault vendor pages mirror the Linear data for offline / graph-based exploration — the canonical record lives in [Linear](https://linear.app/janusd/team/AI-Registry).

## Pipeline

| Status | Meaning | What's expected |
|---|---|---|
| **Backlog** | Surfaced; not yet evaluated | Initial dossier; pending Gate 1 |
| **Evaluating** | Active desk review | Gate 1 + Gate 2 evaluation |
| **Sandbox** | Approved for non-sensitive pilot | Gate 3 trial in controlled environment |
| **Production** | Deployed; live for one or more departments | Operationally managed under §5.2 |
| **Monitor** | Tracked for competitive awareness | Periodic review; no active deployment |
| **Rejected** | Did not meet gates | Decision + rationale documented |
| **Deprecated** | Was Production, now retired | Decommission path documented |
| **Duplicate** | Merge target — manual dedup required | Closed in favour of canonical AIR |

## Gate framework

**Gate 1 (Baseline)** — five hard criteria that any tool must satisfy before progressing:
- **G1.1** Google Workspace integration (or strong rationale)
- **G1.2** Slack integration (or strong rationale)
- **G1.3** Data portability (export, API access)
- **G1.4** **Data training exclusion** — explicit contractual guarantee customer data is not used to train vendor models. **Most common Gate 1 failure.**
- **G1.5** Documented API

**Gate 2 (Technical Qualification)** — fit for purpose, score-based:
- MCP / agent-compatibility
- Enterprise authentication (SSO/SAML, Microsoft Entra)
- Vendor viability (revenue, customer base, certifications)

**Gate 3 (Sandbox Evaluation)** — controlled live trial:
- Per-user data control architecture (added as hard requirement after Viktor [[viktor|AIR-38]] failure)
- Real-world workflow fit
- Cost validation

**Gate 4 (Production Approval)** — IT handover + documentation + SOP.

## Lessons captured (running list)

- **2026-04-22 — [[viktor|AIR-38 Viktor]] rejected on per-user ACL architecture**: integrations connected per-user but used workspace-wide. Now a Gate 1/2 criterion for any agent platform: integrations must run under the *requesting* user's permissions, not the connecting user's.
- **2026-04-20 — [[n8n|AIR-19 n8n]] moved from GCP to [[hostinger|AIR-79 Hostinger]]**: GCP pilot exposed opaque, non-forecastable unit costs (egress, per-request). Hostinger flat-fee + Docker-native + one-click n8n won on transparent pricing and APAC residency.
- **2026-05-04 — Bakeoff cohort discipline**: [[hercules|AIR-87 Hercules]] + [[lovable|AIR-88 Lovable]] + [[bolt|AIR-89 Bolt]] + [[v0|AIR-90 v0]] + [[replit|AIR-32 Replit]] all evaluated in parallel. Decision: pick ONE primary chat-to-app tool, not approve all five.
- **2026-05-05 — CRM matrix**: [[hubspot|AIR-77 HubSpot]] + [[attio|AIR-76 Attio]] + [[monday-com|AIR-83 Monday.com]] + [[salesforce|AIR-93 Salesforce]] benchmarked. Salesforce registered as benchmark only (NOT adoption candidate at current scale).
- **2026-05-08 — [[obsidian|AIR-74 Obsidian]] promoted Evaluating → Sandbox** following heavy active use across AI Office (Jehad's personal vault, Michael's Prime Radiant LLM Wiki prototype).
- **2026-05-08 — [[draw-io|AIR-95 draw.io]] adopted** as canonical diagramming tool for ISO platform-and-tool-development with Simon. Open XML format = AI-readable.

## Cross-references

- Linear team: [AI Registry](https://linear.app/janusd/team/AI-Registry) (id `598dd614-dce5-4ede-98ef-207f3bdff33c`)
- Linear team: [AI Projects](https://linear.app/janusd/team/AI-Projects) — sibling team tracking project work (AIP-N) including evaluations driven from this registry
- Policy: [[ai-policy|AI & Automated Systems Policy]] — §5.2 Tool Categorisation, §5.2.3 Data Boundaries, §5.2.4 Justification Protocol
- Curator: [[michael-bruck]] (programme owner), [[jehad-altoutou]] (sandbox builds, integrations)
- Related concept: [[ai-tool-evaluation]] — the formal Stage 1-4 gate-based methodology applied to every registry entry
