---
type: vendor
title: Solace
slug: solace
air_id: AIR-97
status: Backlog
labels: [Functional, Office of CEO, Technology]
departments: [office-of-ceo]
url: https://linear.app/janusd/issue/AIR-97/solace
created: 2026-05-11
updated: 2026-05-11
captured_by: jehad-altoutou
audience: department
sensitivity: dept
sensitivity_confidence: 0.9
---
<!-- jb:air-vendor-callout -->
> Part of [[ai-registry|AI Registry]]
> Departments: [[office-of-ceo]]


# Solace

> AI Registry entry [AIR-97](https://linear.app/janusd/issue/AIR-97/solace) — status **Backlog** as of 2026-05-11. Departments: office-of-ceo.

**Category:** Event-Driven Integration Platform + Agentic AI Orchestration
**Status:** Backlog
**Cost:** Enterprise contract-based; usage tied to event-broker capacity. Open-source Solace Agent Mesh (SAM) is Apache 2.0, free to run.
**Departments:** Technology, AI Office, Office of CEO
**Entity:** Solace (founded 2001, Ottawa)
**Requested by:** Bonaventure Wong via #ai-internal-hub 2026-05-05

## Overview

Long-established enterprise event-driven messaging vendor. **PubSub+ Event Broker** deployed at tier-1 banks (Barclays, RBC), Airbus, Renault, Stellantis, Danone, Heineken, Unilever, United Airlines, PSA Singapore. Recent rebrand around "Real-time integration for the agentic age." Shipped **Solace Agent Mesh (SAM)** — open-source event-driven framework for orchestrating multi-agent AI systems. Uses Google ADK + Solace AI Connector. Implements A2A protocol.

**Not a SaaS app — INFRASTRUCTURE for connecting real-time data, legacy systems, APIs, and AI agents at enterprise scale.**

## Capabilities

* **PubSub+ Event Broker** — high-throughput multi-protocol (AMQP, JMS, MQTT, REST, WebSocket); AWS/Azure/GCP/Kubernetes/on-prem
* **Event Mesh** — federation across cloud/edge/on-prem for global event distribution
* **Event Portal** — design-time governance (event catalogs, schema management)
* **Solace Agent Mesh (SAM)** — open-source (`SolaceLabs/solace-agent-mesh`, Apache 2.0, ~2.4k stars). Universal A2A Agent Host with dynamic peer discovery, task delegation, file artifacts, SQL/JQ/visualisation tools
* **Solace AI Connector (SAC)** — bridge from broker to AI models/services
* Micro-Integrations — pre-built bridges for mainframe, SAP, IBM MQ
* Integration Hub — Boomi, MuleSoft, Kong, Gravitee

## Janus Strategic Position (Updated 2026-05-11)

Original angles: (1) internal AI Office stack infrastructure, (2) commercial fluency. Assessed as "unlikely needed today at Janus scale."

**2026-05-08 Marketing Prime Radiant brainstorm + separate-vault decision produced exploratory third angle: Solace Agent Mesh as Prime Radiant cross-instance federation infrastructure.** Cross-vault signal flow at Outputs ↔ Signals boundary (Marketing brief → AIO Signal when AI tooling implicated; AIO decision → Marketing when vendor matters for outreach) is *deferred infrastructure* in current architecture. Today manual cross-reference; eventually needs event-driven if federation scales across HR/Finance/IT-Ops/Office-of-CEO/Engineering/Training instances.

That's structurally what an event mesh + agent orchestration platform does. **SAM (open-source) sits exactly where PR federation gap is** — event-driven A2A protocol for cross-vault signal flow. Open-source angle means evaluation possible WITHOUT engaging Solace commercial entity at all.

**Priority of angles:**
1. **PR cross-instance federation infrastructure** (new, exploratory — observed need but not yet observed pain). SAM as substrate for automated event-driven signal flow between dept-vault PRs.
2. **Internal AI Office stack** (subsumed by #1 when framed as PR infrastructure)
3. **Commercial fluency** — Solace "agentic age" positioning clean for FS/manufacturing client conversations

**Exploratory framing matters:** Not observed demand yet. Marketing PR doesn't NEED SAM today — manual federation works at current scale (1 live + 1 in flight). SAM becomes relevant when (a) federation pattern proven across multiple instances, (b) manual cross-reference becomes clear bottleneck. **Repo desk-review pays for itself** as architectural reference regardless of adoption.

## Security

* Solace deployed at tier-1 institutions with strict procurement bars — strong baseline
* Trust/Compliance Center published; specific cert list TBD via evaluation
* SAM Apache 2.0 — fully auditable in source

*Backlog. Functional tier (could shift to AI Office Infrastructure Tier 3 if becomes core stack). Exploratory federation infrastructure candidate.*
