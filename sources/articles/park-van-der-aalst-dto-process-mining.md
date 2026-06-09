---
type: source
title: "Realizing A Digital Twin of An Organization Using Action-oriented Process Mining"
slug: park-van-der-aalst-dto-process-mining
created: 2026-06-08
updated: 2026-06-08
departments: [ai-office, engineering]
authors: [Gyunam Park, Wil M.P. van der Aalst]
affiliation: RWTH Aachen University — Process and Data Science Group (PADS)
related: [organisational-digital-twin, hgtft, coordination-leverage-model]
---

# Realizing A Digital Twin of An Organization Using Action-oriented Process Mining

Park, G. & van der Aalst, W.M.P. RWTH Aachen University, PADS Group. Conference paper (IEEE; exact venue 2021).

GitHub implementation: https://github.com/gyunamister/dtween

## Abstract (lightly paraphrased)

A Digital Twin of an Organization (DTO) is a mirrored representation of an organization that improves business processes by providing a transparent view and automating management actions to deal with existing and potential risks. Unlike wide applications of digital twins to product design and predictive maintenance, no concrete realizations of DTOs for business process improvement had been studied. This paper realizes DTOs using **action-oriented process mining** — techniques to evaluate violations of constraints and produce required actions. The authors suggest a **Digital Twin Interface Model (DT-IM)** as a transparent representation of an organization describing the current state of business processes and possible configurations in underlying information systems. Process analysts interact with the representation to elicit constraints and actions that are continuously monitored and triggered by an action engine.

## Core architecture

### Digital Twin Interface Model (DT-IM)

Formal definition: a tuple `(ON, V, G)` where:
- `ON` = Object-Centric Petri Net (OCPN) — formal representation of the business process
- `V` = set of **valves** (configuration parameters and options in information systems, used in guards)
- `G` = guards — formulas defined over attributes using relational and logical operators; govern routing and resource allocation rules

OCPNs model multi-object processes: each place is associated with an object type; variable arcs represent variable-amount token consumption/production. Enables representing interactions among different object types (e.g., orders, items, routes, resources) in a single unified model.

### Two views of the DT-IM

**Operational view** — the real-time state of the process:
- **Marking**: which objects reside in which phase (e.g., "o1 and o2 waiting for send-notification")
- **Diagnostics**: performance/compliance metrics (e.g., "avg waiting time for send-notification in the last 2 days = 2h")
- Updated continuously via streaming event data + token-based replay

**Control view** — the configuration surface:
- Current value assignments to valves (e.g., `sn-price = 200`, `capacity = 10`)
- Describes possible configurations process analysts can act on

### Action patterns and action engine

An **action pattern** = `(constraint, action)` pair:
- **Constraint**: formula over diagnostics (e.g., `[avg-st-sn-2d > 16h]`)
- **Action**: function from current configuration to new configuration (e.g., set `sn-price = 220`)

**Action engine**: continuously monitors operational state against action patterns; produces and applies actions to update information system configuration.

### Taxonomy of constraint violations

1. **Compliance-oriented**: existence (unnecessary executions) / non-existence (skipped necessary executions) — for single activities or sub-processes
2. **Performance-oriented**: temporal (absolute/relative time — average sojourn time, waiting time) / non-temporal (frequency, volume)

### Taxonomy of management actions

1. **Inflow control**: block (all/some) / allow (all/some) execution of activities
2. **Routing**: parallel / extra / alternative / skip routing
3. **Resource allocation**: group / role / experience-based assignment changes
4. **Capacity**: increase or decrease maximum concurrent process instances

## Implementation

Cloud-based web service (Python; Docker; microservices). Four components:
1. Build DT-IMs from OCEL event data + user-provided guards/valves
2. Update states via streaming OCEL events (token-based replay at user-defined intervals)
3. Visualise DT-IMs (operational + control views)
4. Action engine: evaluate patterns, trigger actions, update configurations

## Proof-of-concept results

Order-handling process; 14 resources; action patterns AP1 `[avg-st-sn-2d > 16h → skip-more-notifications]` and AP2 `[avg-st-sn-2d < 10h → skip-fewer-notifications]`. Evaluated every 12 hours for 24 days.

With action engine active: average sojourn time held between 9–16 hours (automatic regulation). Without action engine: sojourn time grew to 20 hours with no correction. **55% improvement** in average sojourn time at the peak differential (9 hours with actions vs. 20 hours without at day 7).

The reduction was **fully automated** — the action engine detected the constraint violation and adjusted system configuration without human intervention.

## Key claims

- "A concrete realization and implementation of DTOs are missing both in research and in practice" — this paper fills the gap
- Most prior DTO work focuses on product design and manufacturing (IoT/physical assets); business-process DTOs are unstudied
- Object-Centric Petri Nets enable multi-object process models that standard process mining (single case notion) cannot represent
- Action-oriented process mining (conformance checking + predictive monitoring + automated action) is the technology stack that closes the monitor-act loop

## Relation to Janus / AIO

See [[organisational-digital-twin]] for the full mapping. The DT-IM architecture provides the academic grounding and formal vocabulary for the "agentic pipelines operating on the twin's data" layer. The PADS group at RWTH Aachen is the same research lineage underlying the OCPN formalism in [[hgtft-neurips-2025]].
