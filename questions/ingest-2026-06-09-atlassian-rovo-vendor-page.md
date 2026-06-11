---
type: question
title: "Create vendor page for Atlassian Rovo — Teamwork Graph architecture"
slug: ingest-2026-06-09-atlassian-rovo-vendor-page
created: 2026-06-09
updated: 2026-06-09
departments: [ai-office, engineering]
status: resolved
owner: michael-bruck
sources: [odt-competitive-analysis-2026]
related: [organisational-digital-twin, retrieval-augmented-generation, pinecone, glean]
---

# Create vendor page for Atlassian Rovo — Teamwork Graph architecture

## What this is

Atlassian Rovo is a Workspace Platform product from Atlassian (Jira / Confluence company) that queries their 20-year "Teamwork Graph" directly rather than running vector RAG. Featured prominently in [[odt-competitive-analysis-2026]] as one of the two major proofs of the anti-RAG architectural shift.

No vendor page currently exists for Atlassian or Rovo in this wiki.

## Proposed action

Create `vendors/atlassian-rovo.md` (or `vendors/atlassian.md` as the parent vendor page with a Rovo section).

## Key data points from [[odt-competitive-analysis-2026]]

- **Architecture**: Direct "Teamwork Graph" query — maps existing Jira issues, sprints, Confluence pages, and developer relationships. Bypasses vector RAG entirely. 20 years of pre-structured relational data > any runtime retrieval system.
- **Results**: Doubled customer ARR growth vs non-Rovo Atlassian customers. Contributed to 32% YoY Atlassian stock growth. Token costs halved.
- **Scale**: 27B documents (comparable to Glean); relationship density is the differentiator.
- Source: [mindstudio.ai/blog/atlassian-rovo-knowledge-graph-vs-rag-arr-growth](https://www.mindstudio.ai/blog/atlassian-rovo-knowledge-graph-vs-rag-arr-growth)

## Relevance to Janus

Rovo is a direct architectural proof-of-concept for the anti-RAG argument in [[organisational-digital-twin]] — the claim that pre-structured knowledge graphs outperform runtime RAG on latency, cost, and accuracy. Atlassian's commercial results (doubled ARR growth, halved token costs) are the strongest published business-case numbers for this architectural bet. Relevant to the HGTFT / Prime Radiant build narrative.

Also worth noting: Atlassian is in the **Workspace Platform** segment (alongside Microsoft Loop, Notion, Google Agentic Data Cloud), not the **Analyst-DTO** segment — which means it's positioned as an enterprise productivity platform that happens to deliver DTO-like capabilities via the Teamwork Graph, not as an explicit DTO vendor. This framing matters for how Janus positions relative to the space.

## Decision needed

Do you want a Rovo-specific page or a parent Atlassian vendor page? Given Jira and Confluence already exist in the Janus stack context (AIR entries?), a parent Atlassian page with a prominent Rovo section is probably the right shape.
