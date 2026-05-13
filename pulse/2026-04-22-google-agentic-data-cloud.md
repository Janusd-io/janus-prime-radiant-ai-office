---
type: pulse
title: Google announces Agentic Data Cloud at Cloud Next 2026
slug: 2026-04-22-google-agentic-data-cloud
created: 2026-05-06
updated: 2026-05-06
departments: [ai-office]
confidence: high
sources: [google-agentic-data-cloud]
related: [agentic-ai, retrieval-augmented-generation]
---

# Google announces Agentic Data Cloud (2026-04-22)

At Cloud Next 2026, [[google-cloud|Google]] announced its **Agentic Data Cloud** — a rewiring of BigQuery, the data catalog, and pipeline tooling around autonomous AI agents instead of human-scale scheduled queries.

Three pillars:

- **Knowledge Catalog** — automates semantic metadata curation, inferring business logic from query logs without manual data steward intervention.
- **Cross-cloud lakehouse** — BigQuery queries Iceberg tables on AWS S3 via private network, no egress fees.
- **Data Agent Kit** — drops MCP tools into VS Code, Claude Code, and Gemini CLI so engineers describe outcomes rather than write pipelines.

Andi Gutmans (VP/GM Data Cloud, Google Cloud): "The data architecture has to change now. We're moving from human scale to agent scale."

## Why this matters

Sits alongside [[2026-05-04-pinecone-nexus-launch]] as a parallel vendor move from human-RAG to agent-native data infrastructure. Google's framing — "human scale → agent scale" — captures the shift cleanly.

Two specific things worth tracking from Janus's perspective:

- **MCP tool integration with VS Code.** Directly relevant to the [[vs-code]] vendor page and Janus's coding workflows.
- **Cross-cloud Iceberg lakehouse.** Reduces lock-in objections to BigQuery; reshapes the multi-cloud-data architecture conversation.

## Watch for

- Adoption of the Knowledge Catalog vs. existing data-cataloging tools.
- Whether "Data Agent Kit" becomes a standardised pattern or remains Google-specific.
- Whether AWS / Azure ship analogous agent-native data layers in response.
