---
type: vendor
title: Google Cloud
slug: google-cloud
air_id: AIR-7
status: Production
labels: [AI Policy, AI Office Infrastructure]
departments: [ai-office, engineering, it-ops]
url: https://linear.app/janusd/issue/AIR-7/google-cloud
created: 2026-02-25
updated: 2026-05-31
captured_by: jehad-altoutou
audience: department
sensitivity: dept
sensitivity_confidence: 0.9
confidence: high
sources: [google-agentic-data-cloud, google-skills-repository, a2a-mcp-five-integration-patterns, jehad-vault-google-cloud, 2026-05-20-every-google-io-agents-agents-agents, 2026-05-19-nyt-google-winning-ai-race]
related: [agentic-ai, model-context-protocol, agent-to-agent-protocol, agent-skills, 2026-04-20-gcp-self-host-metering-complexity-hostinger-simplicity-wins, hostinger, claude, ai-native-enterprise-restructuring]
migrated_from: entities/vendors/google-cloud.md
---
<!-- jb:air-vendor-callout -->
> Part of [[ai-registry|AI Registry]]
> Departments: [[ai-office]]


# Google Cloud

> AI Registry entry [AIR-7](https://linear.app/janusd/issue/AIR-7/google-cloud) — status **Production** as of 2026-05-04. Departments: ai-office.

**Category:** Cloud Infrastructure / AI Platform
**Cost per User/Month:** $100 (usage-based)
**Number of Licences:** 1
**Total Monthly Cost:** $100
**Departments:** AI Policy

## Overview

Google Cloud Platform (GCP) — Google's enterprise cloud computing service. Underlying infrastructure for AI Office's development and deployment work — hosting n8n workflows (until April 2026 migration to [[hostinger|Hostinger]]), Vertex AI API access, custom AI automation. Classified as AI Office Infrastructure rather than company-wide.

## Capabilities

* Compute and hosting (VMs, Cloud Run, Cloud Functions, App Engine)
* Vertex AI — managed ML platform with [[gemini|Gemini]], [[claude|Claude]] (via Model Garden)
* AI APIs: Vision, Speech-to-Text, NLP, Translation, Document AI
* Data: BigQuery, Cloud SQL, Firestore, Cloud Storage
* Networking: VPC, Load Balancing, CDN, DNS
* DevOps: Cloud Build, Artifact Registry, Cloud Deploy
* Security: IAM, Secret Manager, Cloud Armor

## Security & Compliance

* SOC 1/2/3, ISO 27001/27017/27018, GDPR, FedRAMP, PCI DSS
* Configurable data residency
* IAM, encryption at rest/in transit
* VPC Service Controls

## Relevance

AI Office infrastructure backbone. Single-licence $100/month is modest relative to capabilities enabled.

*AI Office infrastructure. Single licence managed by AI Policy.*

## Merged from `entities/vendors/google-cloud.md`

# Google Cloud

Google's enterprise cloud arm. Distinct from "Google" generally — this entity covers the GCP product surface specifically: BigQuery, Vertex AI, Gemini API, GKE, Cloud Run, the data catalog, and the broader agent-ecosystem moves Google has been making at speed in 2026.

## Notable 2026 launches relevant to this wiki

- **Agentic Data Cloud** ([[2026-04-22-google-agentic-data-cloud]]) — Cloud Next 2026. Knowledge Catalog + cross-cloud lakehouse + Data Agent Kit. Reframes BigQuery for agent-scale workloads.
- **Official Agent Skills Repository** ([[2026-04-22-google-skills-repository]]) — same Cloud Next event. Condensed expertise for GCP products as agent skills.
- **A2A protocol push** ([[a2a-mcp-five-integration-patterns]]) — Google is the most visible advocate for cross-vendor [[agent-to-agent-protocol]] standards.

## Google I/O 2026 — "agents are the product" (2026-05-19/20)

Coverage at [[2026-05-20-every-google-io-agents-agents-agents]] and the pulse entry [[2026-05-19-google-io-2026-agents-as-product]]. The I/O keynote split announcements cleanly along the *collaborate with* vs *delegate to* axis for agents:

- **Gemini 3.5 Flash** — new frontier model; claimed 4× speed and half the cost of comparable LLMs; per Every's reading of the benchmark slide, delivers Opus-4.7-level intelligence "in a quadrant of its own" on the speed/cost frontier. Engine for most of the agentic features below.
- **AI Mode + new search box** (collaborate with). AI Mode becomes the default search mode; box widened for conversational queries; can build custom mini-apps (e.g., personalised fitness tracker) directly within search.
- **Antigravity 2.0** (collaborate with). Google's agentic-development platform becomes a desktop app for managing teams of agents — new CLI tool, new SDK for custom workflows. Direct competitor framing against Anthropic's Cowork-and-Managed-Agents stack.
- **Gemini Spark** (delegate to). 24/7 cloud-resident personal agent across Gmail / Docs / Workspace / Chrome / (eventually) third-party tools via MCP. Pitched by Josh Woodward (VP, Google Labs / Gemini / AI Studio): *"You can just throw tasks over your shoulder. Spark will catch them and then run with them."*
- **Daily Brief** (delegate to). Out-of-the-box overnight agent — scans inbox/calendar/tasks and prepares a morning digest.
- **Universal Cart + Universal Commerce Protocol** — cross-merchant cart with proactive price-tracking, restock alerts, and compatibility flagging (e.g., notice that a CPU and motherboard you selected are incompatible). The protocol is co-developed with Amazon, Meta, Microsoft and others — another emerging cross-vendor standard alongside [[model-context-protocol|MCP]] and [[agent-to-agent-protocol|A2A]] that Janus needs to track.

Strategic read for Janus: the Gemini-3.5-Flash + AI-Mode-default combination is positioned to bring "billions of users" into a first agentic AI interaction without them having to opt into "AI" as a distinct product. Google's data moat (Gmail + Calendar + Docs context) materially reduces the agent-setup tax — Apple-via-Gemini will compound this. For Janus's [[ai-native-janus-positioning|three-pillar positioning]], the Society pillar's "AI for everyone" framing now has a credible vendor-side execution path (consumer ambient agents) — but the AIO's pillar contribution stays B2B / enterprise-infrastructure shaped, not consumer-shaped.

## Consumer reach — NYT read (added 2026-05-31)

NYT's *How Google Is Starting to Win the A.I. Race* (Brian X. Chen, 2026-05-19; [[2026-05-19-nyt-google-winning-ai-race]]) packages the consumer-side execution case that pairs with the I/O announcements above:

- **Gemini reports 900M regular users**, on par with OpenAI's self-reported ChatGPT figure and **~30× the estimated web traffic of Claude** (per the NYT piece — note that this measures consumer chatbot web traffic, not enterprise API usage where Claude's positioning is materially different).
- **Apple Siri integration**: per a January 2026 announcement (recapped in the NYT piece), Gemini becomes the foundational AI model for a future version of Siri. Paired with existing Android availability, this effectively bakes Gemini into virtually every smartphone globally — the consumer ambient-agent distribution channel referenced in the [[2026-05-19-google-io-2026-agents-as-product|I/O pulse]] now has a concrete shipping path.
- **AI ad revenue**: Q1 2026 advertising revenue +16% to $77B, attributed to AI tooling that *"helped marketers collect deeper information about users' interests."* Google is the only frontier vendor with a clear AI-monetisation flywheel that doesn't depend on raising per-seat enterprise pricing.
- **AI Overviews accuracy**: an internal NYT analysis [pegs Google's AI Overviews at 90% accuracy](https://www.nytimes.com/2026/04/07/technology/google-ai-overviews-accuracy.html) — disputed by Google as too low. Either way, the early "eat rocks" failure mode (2024) has been largely resolved and AI Overviews are now opt-out-impossible on Google.com.

The NYT framing — Gary Rivlin (author of a tech-industry AI race book): *"If I had to put a wager on the biggest winner of A.I., I would say it's Google"* — is the cleanest external articulation of the *consumer-distribution moat* angle. Useful counterweight to the enterprise-narrative thread (where Anthropic's KPMG / preferred-partner-for-PE narrative dominates) when summarising the competitive landscape in any positioning context.

## Posture

Sharper agent-platform play than I would have expected from Google a year ago. The "human scale → agent scale" framing (Andi Gutmans, VP/GM Data Cloud) is doing real work — it gives an organising story for the data + skills + protocol announcements landing together.

## Janus relevance

Currently low active dependency at Janus (no production GCP workloads to my knowledge as of 2026-05-06; correct me if wrong). Worth tracking primarily as a reference point against which Anthropic / OpenAI / AWS positioning gets evaluated, and as an MCP / A2A standards bellwether.

**Past evaluation note:** GCP was the original candidate for self-hosting Janus workloads but was rejected in favour of [[hostinger]] on metering-complexity / cost grounds (~$4,290–5,000 vs $920–1,020). See [[2026-04-20-gcp-self-host-metering-complexity-hostinger-simplicity-wins]] for the lesson record. This precedent doesn't preclude future GCP adoption for managed services (BigQuery, Vertex AI) — only the self-hosting compute path.

## Watch for

- Whether AWS / Azure ship analogous "agentic data cloud" stories.
- Skill format compatibility: Google skills vs. Anthropic skills vs. ecosystem fragmentation.
- Pricing for the Data Agent Kit when it leaves preview.
- Universal Commerce Protocol uptake — whether it ships outside the Google/Amazon/Meta/Microsoft founding-member set, and whether it overlaps awkwardly with MCP for transactional surfaces.
- Antigravity 2.0 vs Claude Cowork / Managed Agents — direct enterprise-agent-platform competition; pricing + ecosystem moves to watch through H2 2026.
- Gemini Spark's MCP-to-third-party-tools maturity — current keynote claim is "eventually"; real-world tool coverage will determine whether Spark stays a Google-stack assistant or becomes a competitor to Claude in the personal-agent slot.

## Merged from `entities/vendors/google-cloud.md`

# Google Cloud

Google's enterprise cloud arm. Distinct from "Google" generally — this entity covers the GCP product surface specifically: BigQuery, Vertex AI, Gemini API, GKE, Cloud Run, the data catalog, and the broader agent-ecosystem moves Google has been making at speed in 2026.

## Notable 2026 launches relevant to this wiki

- **Agentic Data Cloud** ([[2026-04-22-google-agentic-data-cloud]]) — Cloud Next 2026. Knowledge Catalog + cross-cloud lakehouse + Data Agent Kit. Reframes BigQuery for agent-scale workloads.
- **Official Agent Skills Repository** ([[2026-04-22-google-skills-repository]]) — same Cloud Next event. Condensed expertise for GCP products as agent skills.
- **A2A protocol push** ([[a2a-mcp-five-integration-patterns]]) — Google is the most visible advocate for cross-vendor [[agent-to-agent-protocol]] standards.

## Google I/O 2026 — "agents are the product" (2026-05-19/20)

Coverage at [[2026-05-20-every-google-io-agents-agents-agents]] and the pulse entry [[2026-05-19-google-io-2026-agents-as-product]]. The I/O keynote split announcements cleanly along the *collaborate with* vs *delegate to* axis for agents:

- **Gemini 3.5 Flash** — new frontier model; claimed 4× speed and half the cost of comparable LLMs; per Every's reading of the benchmark slide, delivers Opus-4.7-level intelligence "in a quadrant of its own" on the speed/cost frontier. Engine for most of the agentic features below.
- **AI Mode + new search box** (collaborate with). AI Mode becomes the default search mode; box widened for conversational queries; can build custom mini-apps (e.g., personalised fitness tracker) directly within search.
- **Antigravity 2.0** (collaborate with). Google's agentic-development platform becomes a desktop app for managing teams of agents — new CLI tool, new SDK for custom workflows. Direct competitor framing against Anthropic's Cowork-and-Managed-Agents stack.
- **Gemini Spark** (delegate to). 24/7 cloud-resident personal agent across Gmail / Docs / Workspace / Chrome / (eventually) third-party tools via MCP. Pitched by Josh Woodward (VP, Google Labs / Gemini / AI Studio): *"You can just throw tasks over your shoulder. Spark will catch them and then run with them."*
- **Daily Brief** (delegate to). Out-of-the-box overnight agent — scans inbox/calendar/tasks and prepares a morning digest.
- **Universal Cart + Universal Commerce Protocol** — cross-merchant cart with proactive price-tracking, restock alerts, and compatibility flagging (e.g., notice that a CPU and motherboard you selected are incompatible). The protocol is co-developed with Amazon, Meta, Microsoft and others — another emerging cross-vendor standard alongside [[model-context-protocol|MCP]] and [[agent-to-agent-protocol|A2A]] that Janus needs to track.

Strategic read for Janus: the Gemini-3.5-Flash + AI-Mode-default combination is positioned to bring "billions of users" into a first agentic AI interaction without them having to opt into "AI" as a distinct product. Google's data moat (Gmail + Calendar + Docs context) materially reduces the agent-setup tax — Apple-via-Gemini will compound this. For Janus's [[ai-native-janus-positioning|three-pillar positioning]], the Society pillar's "AI for everyone" framing now has a credible vendor-side execution path (consumer ambient agents) — but the AIO's pillar contribution stays B2B / enterprise-infrastructure shaped, not consumer-shaped.

## Consumer reach — NYT read (added 2026-05-31)

NYT's *How Google Is Starting to Win the A.I. Race* (Brian X. Chen, 2026-05-19; [[2026-05-19-nyt-google-winning-ai-race]]) packages the consumer-side execution case that pairs with the I/O announcements above:

- **Gemini reports 900M regular users**, on par with OpenAI's self-reported ChatGPT figure and **~30× the estimated web traffic of Claude** (per the NYT piece — note that this measures consumer chatbot web traffic, not enterprise API usage where Claude's positioning is materially different).
- **Apple Siri integration**: per a January 2026 announcement (recapped in the NYT piece), Gemini becomes the foundational AI model for a future version of Siri. Paired with existing Android availability, this effectively bakes Gemini into virtually every smartphone globally — the consumer ambient-agent distribution channel referenced in the [[2026-05-19-google-io-2026-agents-as-product|I/O pulse]] now has a concrete shipping path.
- **AI ad revenue**: Q1 2026 advertising revenue +16% to $77B, attributed to AI tooling that *"helped marketers collect deeper information about users' interests."* Google is the only frontier vendor with a clear AI-monetisation flywheel that doesn't depend on raising per-seat enterprise pricing.
- **AI Overviews accuracy**: an internal NYT analysis [pegs Google's AI Overviews at 90% accuracy](https://www.nytimes.com/2026/04/07/technology/google-ai-overviews-accuracy.html) — disputed by Google as too low. Either way, the early "eat rocks" failure mode (2024) has been largely resolved and AI Overviews are now opt-out-impossible on Google.com.

The NYT framing — Gary Rivlin (author of a tech-industry AI race book): *"If I had to put a wager on the biggest winner of A.I., I would say it's Google"* — is the cleanest external articulation of the *consumer-distribution moat* angle. Useful counterweight to the enterprise-narrative thread (where Anthropic's KPMG / preferred-partner-for-PE narrative dominates) when summarising the competitive landscape in any positioning context.

## Posture

Sharper agent-platform play than I would have expected from Google a year ago. The "human scale → agent scale" framing (Andi Gutmans, VP/GM Data Cloud) is doing real work — it gives an organising story for the data + skills + protocol announcements landing together.

## Janus relevance

Currently low active dependency at Janus (no production GCP workloads to my knowledge as of 2026-05-06; correct me if wrong). Worth tracking primarily as a reference point against which Anthropic / OpenAI / AWS positioning gets evaluated, and as an MCP / A2A standards bellwether.

**Past evaluation note:** GCP was the original candidate for self-hosting Janus workloads but was rejected in favour of [[hostinger]] on metering-complexity / cost grounds (~$4,290–5,000 vs $920–1,020). See [[2026-04-20-gcp-self-host-metering-complexity-hostinger-simplicity-wins]] for the lesson record. This precedent doesn't preclude future GCP adoption for managed services (BigQuery, Vertex AI) — only the self-hosting compute path.

## Watch for

- Whether AWS / Azure ship analogous "agentic data cloud" stories.
- Skill format compatibility: Google skills vs. Anthropic skills vs. ecosystem fragmentation.
- Pricing for the Data Agent Kit when it leaves preview.
- Universal Commerce Protocol uptake — whether it ships outside the Google/Amazon/Meta/Microsoft founding-member set, and whether it overlaps awkwardly with MCP for transactional surfaces.
- Antigravity 2.0 vs Claude Cowork / Managed Agents — direct enterprise-agent-platform competition; pricing + ecosystem moves to watch through H2 2026.
- Gemini Spark's MCP-to-third-party-tools maturity — current keynote claim is "eventually"; real-world tool coverage will determine whether Spark stays a Google-stack assistant or becomes a competitor to Claude in the personal-agent slot.
