---
type: concept
title: Digital twin
slug: digital-twin
created: 2026-05-04
updated: 2026-05-21
captured_by: jehad-altoutou
departments: [ai-office, engineering]
status: active
sources: [2026-05-04-bonaventure-michael-jehad-and-andrew-meeting, 2026-04-coordination-leverage-model-v0.3]
related: [organisational-digital-twin, digital-twin-of-the-company, knowledge-graph, coordination-leverage-model]
---

# Digital twin

A structured, continuously-updated model of a system (physical or organisational) — built on ontologies and knowledge graphs that define what entities exist, how they relate, and what rules govern their behaviour. Sensors feed real-time data into the model. The model supports queries, simulations, and predictions impossible from raw data alone.

## Two surfaces at Janus

- **Physical twin (HGTFT)** — Janus's customer-facing product. Maintains digital twins of buildings: geometry, mechanical systems, relationships, physics. Sensors are IoT (temperature, occupancy, vibration). Janus's core engineering competency.
- **Organisational twin** — covered at [[organisational-digital-twin]]. The same engineering discipline applied to the company itself: departments, roles, workflows, decisions, tools. Sensors are systems of record + AI-assisted capture ([[fireflies]]). The central compounding mechanism of the [[coordination-leverage-model|Coordination Leverage Model]].

## Why one engineering discipline serves both

The argument from §4 of [[coordination-leverage-model]]: the twin's value compounds whether the entities are HVAC units or HR processes. Ontology + knowledge graph + sensor network + continuous model updates are the constant; the specific entity vocabulary changes per domain. **It is not an analogy** — it is the same architecture at a different scale, which is why Janus is uniquely positioned to build the organisational version.

## See also

- [[organisational-digital-twin]] — the canonical concept page for the company-as-twin construction.
- [[digital-twin-of-the-company]] — predecessor stub, redirects here / to organisational-digital-twin.
- [[knowledge-graph]] — the underlying data structure.
- [[coordination-leverage-model]] — the framework that makes the twin load-bearing for the AIO mission.
