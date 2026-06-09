---
type: vendor
title: Glean
slug: glean
air_id: AIR-58
status: Backlog
labels: []
departments: []
url: https://linear.app/janusd/issue/AIR-58/glean
created: 2026-03-12
updated: 2026-06-09
captured_by: jehad-altoutou
audience: department
sensitivity: dept
sensitivity_confidence: 0.9
---
<!-- jb:air-vendor-callout -->
> Part of [[ai-registry|AI Registry]]


# Glean

> AI Registry entry [AIR-58](https://linear.app/janusd/issue/AIR-58/glean) — status **Backlog** as of 2026-04-01. Departments: —.

**Category:** Enterprise AI Search & Knowledge Management
**Status:** Backlog
**Cost:** TBC (per-seat enterprise; sales engagement)
**Departments:** TBC
**Requested by:** AI & Technology Office (horizon scan)

## Overview

Enterprise AI-powered search and knowledge management. Unified search layer across all company applications and data sources. Builds knowledge graph of org's data. Natural language Q&A. Semantic understanding (not just keyword), personalised by role/permissions.

## Key Capabilities

* AI-powered semantic search across 100+ enterprise data sources
* Natural language Q&A grounded in company data
* Unified knowledge graph indexing/connecting information across apps
* Personalised results (org context, role, access permissions)
* Real-time indexing
* AI agents for specific workflows (e.g. Zendesk agent for support)
* Enterprise security — federated search respects source permissions
* Integrations: Workspace, M365, [[salesforce|Salesforce]], Jira, Confluence, Slack, Zendesk

## Why Evaluating

Addresses universal enterprise pain point: information fragmentation across dozens of tools. As org scales, finding right document/policy/conversation becomes costly. Zendesk agent integration particularly interesting for customer support automation.

## Key Evaluation Areas

* Integration coverage with current stack
* Data security and permission model (§5.2.3)
* Quality of AI-generated answers
* TCO at Janus scale

*Backlog. Pending Stage 1 — Intake & Triage.*

## Scale data — mid-2026 (added 2026-06-09)

Per [[odt-competitive-analysis-2026]], which cites SaaStr coverage:

- **$200M ARR** — reached as of the reporting period
- **27 billion documents indexed** across enterprise SaaS connections
- **20 trillion tokens consumed annually** — making Glean one of the highest-token-throughput enterprise AI deployments publicly disclosed

The 20T tokens/year figure puts Glean's token consumption at a scale that eclipses most Workspace Platform competitors. At that scale, the value proposition is the **depth of indexing** (27B docs across all SaaS silos) rather than model quality — which is why the Teamwork-Graph architecture (Atlassian Rovo, no-RAG approach) is positioned as a direct architectural competitor: pre-structured relationships beat brute-force vector indexing on latency and cost even if Glean's index is broader.

## "Glean Skills" product (added 2026-06-09)

Glean launched **Glean Skills** (per [[odt-competitive-analysis-2026]]; source: [glean.com/blog/skills-may-drop-2026](https://www.glean.com/blog/skills-may-drop-2026)) — packaging institutional knowledge into reusable workflows and context templates. Same product vocabulary as Anthropic's Claude Cowork "plugins/skills" architecture. The convergence on "skills as reusable context packages" across Glean, Anthropic, and GBrain is further evidence that the skill-as-compiled-knowledge-bundle is the consensus pattern for enterprise AI delivery.

Differentiator vs Anthropic plugins: Glean's depth of enterprise indexing (27B docs, 100+ integrations) vs Anthropic's agent execution environment (local, Cowork, Managed Agents). Different surface — Glean is the retrieval layer; Anthropic is the execution layer. Worth keeping that distinction in the evaluation if both are in scope simultaneously.
