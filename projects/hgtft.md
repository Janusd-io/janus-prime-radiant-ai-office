---
type: project
title: HGTFT — Janus's heterogeneous-graph building digital-twin platform
slug: hgtft
created: 2026-05-21
updated: 2026-05-21
departments: [engineering, ai-office]
status: active
owner: michael-bruck
sources: [hgtft-neurips-2025, 2026-04-coordination-leverage-model-v0.3]
related: [coordination-leverage-model, organisational-digital-twin, digital-twin, ai-native-janus-positioning, ai-native-enterprise-restructuring, ingest-2026-05-21-1015-create-hgtft-entity-page]
audience: department
---

# HGTFT — Janus's heterogeneous-graph building digital-twin platform

Janus Digital's customer-facing platform for **structured, continuously-updated digital twins of buildings** — geometry, mechanical systems, relationships, and the physics governing their behaviour. Built on the **Heterogeneous Graph Temporal Fusion Transformer (HGTFT)** model architecture documented in the [[hgtft-neurips-2025|NeurIPS 2025 submission]] (anonymous per blind review; Janus / Janus-affiliated authorship inferred from the product-name match and application domain).

## Why this page exists in the AIO Prime Radiant

HGTFT is **Engineering-owned**, not AI-Office-owned. This project page exists in the AIO instance because:

1. **It's the architectural precedent for the [[organisational-digital-twin]].** The [[coordination-leverage-model|Coordination Leverage Model]] (Michael, April 2026) names HGTFT four times as the engineering pattern Janus already has — *"It is not an analogy. It is the same engineering discipline applied at a different scale, and Janus Digital is uniquely positioned to build it because the organisational thinking — ontologies, knowledge graphs, structured data, continuous model updates — is already the company's core competency."* That positioning argument requires HGTFT to be a citable in-wiki artefact.
2. **AIO references multiply.** AI-native-positioning content, the framework brief, and the organisational-digital-twin concept all link here.
3. **The federation pattern allows duplication-light wiki coverage.** When Engineering's Prime Radiant instance is stood up, the canonical product page will live there. This AIO page reflects HGTFT *as the AIO sees it* — engineering precedent, sales-asset substrate, evidence for the AI-Native pitch — and will eventually point at the Engineering instance's canonical page. Per CLAUDE.md §1's "Cross-instance federation."

## What HGTFT does

The product maintains a digital twin of a building that supports the same class of operations as Janus's organisational twin (per the [[coordination-leverage-model]] mapping in §4.4):

| Twin operation | HGTFT (physical) | Organisational twin (AIO) |
|---|---|---|
| **Entities + ontology** | Building geometry + mechanical systems | Departments, roles, workflows, tools |
| **Sensors** | IoT (temperature, occupancy, vibration, energy) | Systems of record (Xero, Airwallex, Asana, Slack, Deel, CRM, Linear, Notion, Google Workspace) + [[fireflies]] capture |
| **Physics engine** | Multiphysics simulation (HVAC, thermal, flow, energy) | [[coordination-leverage-model\|Agentic pipelines executing coordination logic]] |
| **Knowledge graph** | Component dependencies | Workflow dependencies, decision chains, data flows |
| **Queries** | "What is the thermal load on floor 3?" | "What is the AI adoption state in Finance?" |
| **Predictions** | "When will this HVAC unit fail?" | "Which workflows will bottleneck at 3× headcount?" |
| **Continuous updates** | From IoT sensor streams | From transactional + conversational data |

## Technical architecture (from the NeurIPS paper)

Three stacked layers in the HGTFT model:

1. **Fusion Layer** — Static + Dynamic Variable Selection → BILSTM → Mean Pooling. Converts heterogeneous data (different sensor types, different physical entities) into unified-dimensional vectors.
2. **Temporal Layer** — Self-Transformer + Transformer layers per-object, shared across all objects.
3. **Graph Layer** — Graph Attention Network across K relation types; Cross-temporal Aggregation for all connected node types.

Plus a **multi-stage training pipeline** with progressive specialisation, and a **four-term loss function** that explicitly enforces physics consistency: MSE + RCS (Reasonableness Checks Score, penalising predictions that violate physical laws) + CRS (Correlation-Based Score) + FDS (Frequency Domain Similarity).

**Adaptation mode:** zero-shot generalisation to unseen buildings + few-shot fine-tuning with project-specific data (only lightweight components updated, preserving generalisation).

## Performance (selected results from the paper)

On the self-constructed **MBS (Multiphysics Building System) dataset** (50 building cases; 7-day look-back → 1-day forecast at 15-min intervals; 10-run average), HGTFT zero-shot and few-shot both **outperform every baseline on every metric**:

| Metric | Best baseline | HGTFT zero-shot | HGTFT few-shot |
|---|---|---|---|
| MSE | 0.0044 (TFT) | 0.0027 | **0.0023** |
| RCS | 0.0133 (HTGNN) | **0.0012** | 0.0029 |

Baselines tested: LSTM, Autoformer, TFT, HTGNN, STD-MAE, TimesFM, MOIRAI, LLMTime, Time-LLM.

The RCS result is the most strategically meaningful — *physics-consistency* of HGTFT predictions is an order of magnitude better than baselines. For real-world building deployment, this is the gate criterion: a model that violates physical laws produces unsafe recommendations.

## How HGTFT informs AIO work

- **It's the load-bearing positioning argument** in [[ai-native-janus-positioning|Janus's AI-Native pitch]] for technical audiences. "We already build digital twins of buildings; the organisational twin is the same architecture at a different scale" is the most distinctive positioning claim Janus can make.
- **It's the engineering-precedent citation** when the AIO explains the [[organisational-digital-twin]] roadmap to other departments — *"the company already does this, we're just applying it to ourselves."*
- **It motivates the AIO's structured-data discipline** in the [[coordination-leverage-model|framework]] (Principle 3 — Structured Data Is Capital). The HGTFT lesson — sensor fidelity bounds the twin's accuracy — translates directly to the AIO Principle 5 (Systems of Record Are the Sensor Network) and Principle 6 (Capture Before You Coordinate).
- **It's a candidate Layer-3 sensor itself.** HGTFT-equipped customer projects produce structured operational data (energy usage patterns, anomaly detections, maintenance forecasts) that — if cleanly federated back to Janus's organisational twin — close a feedback loop between customer deployments and Janus's own operational learning.

## Scope notes — what this page is NOT

- **Not a canonical product description.** Engineering owns the product; that page lives in the future Engineering Prime Radiant instance. This is the AIO-side framing.
- **Not a sales / marketing page.** That's [[andrew-soane|Andrew's]] domain in the Marketing Prime Radiant.
- **Not a deployment runbook.** That's customer-engineering territory.

## Watch for

- **Engineering Prime Radiant instance stand-up.** When it ships, this page transitions to a thin pointer at the canonical Engineering version. Federation pattern.
- **NeurIPS 2025 publication outcome.** Blind-review window resolution will confirm or expand author / affiliation attribution on the paper. If accepted, the proceedings citation becomes a Janus-leadership-facing positioning artefact.
- **Customer deployments as Layer-3 sensors.** The closed-loop between HGTFT customer projects and the AIO's organisational twin is a strategic option not yet operationalised. Worth exploring when ≥3 customer projects are in steady-state production.
- **HGTFT-applied-to-self storyline.** Currently a footnote in the [[coordination-leverage-model]] brief and the [[ai-native-janus-positioning]] brief. May warrant being elevated to a fourth pillar in the positioning spine (Society / Business / Individual + HGTFT-applied-to-self as the differentiated engineering substrate).
