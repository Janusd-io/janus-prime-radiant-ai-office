---
type: vendor
title: Google Cloud
slug: google-cloud
created: 2026-05-06
updated: 2026-05-12
departments: [ai-office, engineering, it-ops]
status: active
confidence: high
sources: [google-agentic-data-cloud, google-skills-repository, a2a-mcp-five-integration-patterns]
related: [agentic-ai, model-context-protocol, agent-to-agent-protocol, agent-skills, 2026-04-20-gcp-self-host-metering-complexity-hostinger-simplicity-wins, hostinger]
---

# Google Cloud

Google's enterprise cloud arm. Distinct from "Google" generally — this entity covers the GCP product surface specifically: BigQuery, Vertex AI, Gemini API, GKE, Cloud Run, the data catalog, and the broader agent-ecosystem moves Google has been making at speed in 2026.

## Notable 2026 launches relevant to this wiki

- **Agentic Data Cloud** ([[2026-04-22-google-agentic-data-cloud]]) — Cloud Next 2026. Knowledge Catalog + cross-cloud lakehouse + Data Agent Kit. Reframes BigQuery for agent-scale workloads.
- **Official Agent Skills Repository** ([[2026-04-22-google-skills-repository]]) — same Cloud Next event. Condensed expertise for GCP products as agent skills.
- **A2A protocol push** ([[a2a-mcp-five-integration-patterns]]) — Google is the most visible advocate for cross-vendor [[agent-to-agent-protocol]] standards.

## Posture

Sharper agent-platform play than I would have expected from Google a year ago. The "human scale → agent scale" framing (Andi Gutmans, VP/GM Data Cloud) is doing real work — it gives an organising story for the data + skills + protocol announcements landing together.

## Janus relevance

Currently low active dependency at Janus (no production GCP workloads to my knowledge as of 2026-05-06; correct me if wrong). Worth tracking primarily as a reference point against which Anthropic / OpenAI / AWS positioning gets evaluated, and as an MCP / A2A standards bellwether.

**Past evaluation note:** GCP was the original candidate for self-hosting Janus workloads but was rejected in favour of [[hostinger]] on metering-complexity / cost grounds (~$4,290–5,000 vs $920–1,020). See [[2026-04-20-gcp-self-host-metering-complexity-hostinger-simplicity-wins]] for the lesson record. This precedent doesn't preclude future GCP adoption for managed services (BigQuery, Vertex AI) — only the self-hosting compute path.

## Watch for

- Whether AWS / Azure ship analogous "agentic data cloud" stories.
- Skill format compatibility: Google skills vs. Anthropic skills vs. ecosystem fragmentation.
- Pricing for the Data Agent Kit when it leaves preview.
