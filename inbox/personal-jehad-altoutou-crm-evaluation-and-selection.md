---
type: project
title: CRM Evaluation & Selection
slug: crm-evaluation-and-selection
created: 2026-05-07
updated: 2026-05-13
departments: [marketing, ai-office, office-of-ceo]
status: active
owner: michael-bruck
sources: [pr-backup-2026-05-11-project-crm-evaluation-and-selection]
related: [andrew-soane, bonaventure-wong, michael-bruck, euclid-wong, ai-tool-evaluation-framework, crm-evaluation, janus-crm-selection, hubspot, attio, salesforce]
audience: [department]
captured_by: jehad-altoutou
---

# CRM Evaluation & Selection

Hub for locking down Janus's CRM platform choice. High-stakes architectural commitment — the chosen CRM becomes the system-of-record hub for customer data with a 2–3 year horizon, and frames a broader SaaS rationalisation thesis (CRM-centric integration vs. point-solution sprawl).

> Dedupe note: see also the canonical stubs [[crm-evaluation]] and [[janus-crm-selection]]; this hub is the richer narrative version restored from PR backup. Orchestrator/curator should reconcile.

## Candidates

| Candidate | Posture | Notes |
|---|---|---|
| [[hubspot]] | Michael leans toward | Strong all-in-one stack; integration breadth. Dispatched to /ai-registry for Gate 1. |
| [[attio]] | In matrix evaluation | Newer entrant; modern data model. Andrew running matrix analysis. |
| [[salesforce]] | In matrix evaluation | Industry default; Gate 1 dispatched. Heavier deployment. |
| Pipedrive | In matrix evaluation | Lightweight; sales-pipeline focused. |

## Decision framing

CRM lock-in is paired with the Monday production push, while [[bonaventure-wong]] is in the room. The window is now or post-his-return — choosing now is operationally easier.

The decision is the project. Once chosen, post-selection integration work may warrant its own project hub or fold into existing departmental projects (marketing automation, recruitment pipeline, etc.).

## Stakeholders

- **Decision lead:** [[michael-bruck]]
- **Matrix analysis:** [[andrew-soane]]
- **Approval / strategic veto:** [[bonaventure-wong]]
- **Implementation:** [[euclid-wong]] / IT (post-selection)

## Linkage to [[ai-tool-evaluation-framework]]

CRM candidates run through the standard Gate 1 viability screen via `/ai-registry` and `/ai-tool-evaluation` skills. As of 2026-05-06, HubSpot and Salesforce are dispatched for Gate 1; Attio and Pipedrive on the matrix but not yet dispatched.

## Watch for

- HubSpot and Salesforce Gate 1 outcomes.
- Andrew's matrix analysis output.
- Lock-in window before Bonaventure's departure.
- Post-selection scope: does the chosen CRM trigger an integration project hub, or fold into existing operational work?
