---
type: concept
title: Coordination three-layer model (Individual / Department / Organisation)
slug: coordination-three-layer-model
created: 2026-05-21
updated: 2026-05-21
departments: [ai-office, office-of-ceo]
status: active
sources: [2026-04-coordination-leverage-model-v0.3, 2026-04-coordination-leverage-model-v0.1]
related: [coordination-leverage-model, coordination-tax, organisational-digital-twin, prime-radiant-three-layer-architecture, builders-sellers-measurers, ai-native-mandate, agentic-lean-marketing-stack, janus-prime-radiant-build]
---

# Coordination three-layer model

Agentic AI transformation occurs across three distinct organisational layers — **Individual / Department / Organisation**. From §3 of the [[coordination-leverage-model|Coordination Leverage Model]]. Each layer has different unit economics, different management disciplines, and different failure modes. Critically, **each layer produces the structured data that enables the next** — making them sequentially dependent but cumulatively compounding.

## The three layers

| Layer | Unit of analysis | Management discipline | AI function |
|---|---|---|---|
| **1. Individual** | One person's output | Task design & leverage | Force multiplier |
| **2. Department** | Team information topology | Process architecture | Connective tissue |
| **3. Organisation** | Company-wide knowledge | Structural design | Coordination layer |

### Layer 1 — Individual leverage

AI at this layer acts as a *force multiplier* on existing tasks: drafting, research, analysis, synthesis, code generation, translation. The individual produces more output per unit of time.

- **Management discipline: task design.** A high-leverage activity amplified by AI produces disproportionate output; but AI also makes people faster at low-leverage activities. Without deliberate task design, individuals optimise for throughput on the wrong work. The manager's job is not to monitor output volume but to ensure AI-amplified effort is directed at the highest-leverage activities.
- **Failure mode: productivity theatre.** More of the wrong things, faster. The distinction between *efficiency* (doing things right) and *effectiveness* (doing the right things) has never been more operationally critical.
- **Output to next layer:** structured, machine-readable work products — *not* PDFs and emails — that can be ingested by department-level systems.

### Layer 2 — Department architecture

AI is no longer a tool attached to an individual; it is the **connective tissue** of the department — the pipelines, workflows, and agentic processes that move information between people, between systems, and between decisions. The AIO [[standup]] pipeline ([[fireflies]] → Linear → Notion → Prime Radiant inbox), the [[ai-registry]], the structured-data hygiene practices — these are Layer-2 artefacts.

- **Management discipline: process architecture.** The process is not merely documented and enforced by humans — it is *enacted by agents*. Coordinators, project managers, and administrative staff are replaced by agentic pipelines that maintain context, route information, and surface exceptions for human judgment.
- **Foundational capability: tacit-to-explicit conversion.** The most significant bottleneck in traditional organisations is converting tacit knowledge in people's heads into explicit, structured, institutional knowledge. AI-assisted capture — particularly meeting transcription via [[fireflies]] — becomes a foundational Layer-2 capability, not a convenience feature. Every transcribed meeting is an automated conversion event.
- **Failure mode: over-engineering.** Not every process benefits from agentic automation. The prototype-to-production gap is real; cognitive load of managing multiple agents is itself a coordination cost. Process architecture must be selective — automate the high-frequency, high-context coordination tasks first.
- **Output to next layer:** clean, structured, continuously updated departmental data that feeds the company-wide knowledge base.

### Layer 3 — Organisational scale

AI as **coordination layer** spanning the company. The traditional answer to geographical scaling is the multidivisional form — semi-autonomous country / regional units with their own management layers, connected to HQ through reporting lines. That structure exists because the coordination cost of tight integration across geographies historically exceeded the cost of local duplication.

Agentic AI at Layer 3 inverts this. When agents maintain institutional context, translate between regulatory frameworks, aggregate cross-market intelligence, and route decisions to the appropriate human authority regardless of timezone — the rationale for heavy local management structures weakens. The organisation can operate with a thinner human layer in each geography, focused on the judgment-intensive work that requires local presence: relationship building, regulatory navigation, cultural adaptation, strategic market positioning.

- **Management discipline: structural design.** Not "how do we replicate our structure in each new country?" but "what is the minimum viable human presence per geography, given that the coordination layer is handled by agents?"
- **Hard prerequisite:** identity and access management infrastructure that enforces data boundaries, role-based permissions, and multi-jurisdiction compliance at the architectural level. Without it, the coordination layer cannot be trusted with cross-geography data flows. This is **Principle 9 — Identity Is the Perimeter**.
- **Failure mode: premature abstraction.** The [[organisational-digital-twin]] must be built from real, clean, structured data — *not* from aspirational data architectures. Layer 3 is only as good as the data produced by Layer 2, which is only as good as the structured outputs from Layer 1. A digital twin built on incomplete sensor data is worse than no twin at all — it produces confident answers from an inaccurate model.

## Layer sequence is not optional

The framework's first architectural principle. Layer 1 feeds Layer 2 feeds Layer 3. Attempting to build higher layers before lower layers are producing structured data is *premature abstraction*. **Build bottom-up, architect top-down.**

This is what makes the AIO's current operating posture deliberate: the AI Office is the Layer-2 prototype. Sequence: build it for ourselves → prove the compounding dynamic → document the patterns (skills library) → replicate to Technology / Finance / country operations. The Layer-3 organisational digital twin is *aspirational* until Layer 2 is replicated beyond the AIO.

## Disambiguation — not the Prime Radiant three-layer architecture

This is a *different* three-layer model from the [[prime-radiant-three-layer-architecture|Prime Radiant Signals / Infrastructure / Outputs]] model. Both are valid; both apply simultaneously:

- **Coordination model** (this page) — Individual / Department / Organisation. Decomposes **the company**. Asks "where in the org does this AI capability sit, and what management discipline applies?"
- **Prime Radiant model** — Signals / Infrastructure / Outputs. Decomposes **a single domain instance** (AIO, Marketing, HR, etc.). Asks "what are the inputs / framing / outputs of this knowledge instance?"

A single AIO artefact maps to both: the standup pipeline is *Layer 2* in the coordination model AND it's a *Signals-layer ingest mechanism* feeding the AIO's Prime Radiant in the per-domain model. Future schema iterations should keep the two distinct in the wiki vocabulary.

## Companion lenses

- **[[builders-sellers-measurers]]** — the role-taxonomy lens. Builders and sellers are the human roles that *survive* AI restructuring; measurers are the role-population that the Layer 2 + Layer 3 substrate displaces. Together: the coordination-three-layer-model is *where* the substrate sits; builders-sellers-measurers is *who* the substrate replaces.
- **[[coordination-tax]]** — the economic primitive being reduced.
- **[[organisational-digital-twin]]** — what Layer 3 ultimately produces.
- **[[stack-composition-framework]]** — the vendor-selection lens for choosing Layer-2 tooling (composability + agent operability + reversibility).

## Watch for

- **Layer 2 replication beyond the AIO.** The framework's current state is Layer-1 deployed, Layer-2 prototyped in AIO only, Layer-3 aspirational. The activation gate for Layer 3 is "Layer 2 working in ≥2 departments." Marketing rollout ([[marketing-prime-radiant]]) is the first replication test.
- **Layer-skipping in queued Prime Radiant rollouts.** HR / Finance / IT-Ops / Engineering / Training / ISO will each be tempted to start with Layer-3 ambitions (a dashboard, a company-wide tool) before Layer 1 is producing structured outputs in their domain. The build sequence is bottom-up; the temptation to skip is the anti-pattern.
- **The two-three-layer-model conflation risk.** Wiki readers encountering both this page and [[prime-radiant-three-layer-architecture]] need disambiguation. Worth a top-level "Coordination model vs Prime Radiant model" reference page if confusion surfaces.
