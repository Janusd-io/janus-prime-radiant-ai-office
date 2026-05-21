---
type: brief
title: The Coordination Leverage Model — the AIO's theoretical framework for AI-native transformation
slug: coordination-leverage-model
created: 2026-04-13
updated: 2026-05-21
departments: [ai-office, office-of-ceo, marketing, hr, finance, it-ops, engineering]
confidence: high
sources: [2026-04-coordination-leverage-model-v0.3, 2026-04-coordination-leverage-model-v0.1]
related: [coordination-tax, coordination-three-layer-model, organisational-digital-twin, ai-native-mandate, ai-native-janus-positioning, ai-native-enterprise-restructuring, builders-sellers-measurers, agentic-lean-marketing-stack, stack-composition-framework, janus-prime-radiant-build, ai-tool-evaluation-framework, fireflies, prime-radiant-three-layer-architecture]
---

# The Coordination Leverage Model — the AIO's theoretical framework for AI-native transformation

Michael Bruck's working draft of the AI Office's foundational thesis. Reframes "AI Native" from marketing shorthand into a measurable management system: **agentic AI's primary strategic value is not productivity, it is the radical reduction of coordination costs — the overhead that grows superlinearly with organisational complexity and has historically been the binding constraint on scalable growth**. Authoritative within the AIO; intended as a Janus-leadership-facing artefact once polished. v0.3 is the current draft; the brief here is the wiki-canonical narrative reference, with the framework's load-bearing primitives broken out as cross-linked concept pages.

## Why this matters to the AI Office

This brief is the *why* behind every other AIO artefact in the wiki:

1. **The [[ai-native-mandate]] gets a theoretical spine.** The Section 5 AI Charter Policy describes the *rules* (no shadow AI, no public LLMs with company data, HITL, pilot-in-command). The Coordination Leverage Model describes the *organisational economics* the rules are designed to capture. The mandate without the model is policy compliance; the model without the mandate is academic theory. Both together give the AIO an operating system.
2. **The [[janus-prime-radiant-build|Janus Prime Radiant rollout]] IS the Layer-3 substrate.** Every per-department instance (Marketing, HR, Finance, IT-Ops, Office-of-CEO, Engineering, Training, ISO) is a measurer-replacement deployment that produces the structured data feeding the [[organisational-digital-twin|organisational digital twin]]. The rollout is not a knowledge-management project; it is the sensor network the framework requires.
3. **The [[builders-sellers-measurers|Drucker frame]] from 2026-05-21 is the role-taxonomy companion** to the layered architecture. Drucker tells you *which people* AI displaces (measurers) vs *which it amplifies* (builders, sellers); the Coordination Leverage Model tells you *which organisational functions* are eligible for agent-substitution (coordination, not judgment). Together they make personnel decisions and architectural decisions consistent.
4. **The [[agentic-lean-marketing-stack]] is the first concrete Layer-2 case study.** Andrew + Jehad operating the marketing stack via MCP-native tooling with one engineer-equivalent is the framework in production for a single function. The CMS / CRM / hosting / edge selections are the connective-tissue choices the framework prescribes.
5. **The [[ai-tool-evaluation-framework|Gate framework]] enforces the trust layer.** §4.3 of the model names Identity-as-the-Perimeter as a hard architectural gate; G2.2 in the evaluation framework (Enterprise SSO via Microsoft Entra) is the operational expression of that gate. The framework page should cross-reference Principle 9 ("Identity Is the Perimeter") at next iteration.

Operationally: the Coordination Leverage Model is what makes the AIO's substrate work *legible to Janus leadership*. When Bonaventure asks "what does the AIO actually do" — the answer is: *we build the coordination layer that lets Janus scale across geographies without the coordination tax scaling with us.* Not "we ship skills" or "we run standups." Those are tactics; this is the strategy.

## Below: the framework itself (summary)

The full v0.3 narrative lives at [[2026-04-coordination-leverage-model-v0.3]]; v0.1 ([[2026-04-coordination-leverage-model-v0.1]]) is the academically-grounded predecessor (Coase, Drucker, Grove, Brooks, Nonaka citations); the synopsis below tracks v0.3.

### §1 — The problem with "AI Native"

"AI Native" / "AI First" have become marketing shorthand for "we bought some licences and wrote a policy." They describe an aspiration, not a management system. They tell you nothing about how work is organised, how decisions are made, how the organisation scales, or how value compounds. The framework starts from the business problem (coordination), not the technology (AI), and asks: what organisational problems does agentic AI actually solve, and what management disciplines are required to capture that value systematically?

### §2 — The [[coordination-tax]]

Coordination is the management layers, reporting structures, status meetings, approval chains, information-routing functions, and context-translation activities that exist not to produce value directly but to enable value-producing work to happen at scale. Communication paths grow as `n(n-1)/2`; hierarchy reduces `n` but introduces latency, distortion, and rigidity. Geographic expansion compounds it multiplicatively. **Agentic AI is the first technology that automates coordination itself, not just transactions** — the inversion that makes the coordination tax proportional to agent-infrastructure capability rather than headcount and geography.

### §3 — The [[coordination-three-layer-model|three-layer model]] (Individual / Department / Organisation)

Sequential, cumulatively compounding, distinct management disciplines per layer:

| Layer | Unit of analysis | Management discipline | AI function |
|---|---|---|---|
| **1. Individual** | One person's output | Task design & leverage | Force multiplier |
| **2. Department** | Team information topology | Process architecture | Connective tissue |
| **3. Organisation** | Company-wide knowledge | Structural design | Coordination layer |

The model is sequential because each layer produces the structured data that enables the next: machine-readable individual outputs → departmental knowledge with lineage → continuously updated company model agents can query and act upon. **Skip a layer and you build premature abstraction** — a digital twin built on incomplete sensor data is worse than no twin at all.

(Note: distinct from the [[prime-radiant-three-layer-architecture|Signals / Infrastructure / Outputs]] three-layer model in the Prime Radiant pattern — these are orthogonal lenses on the same Janus infrastructure. The Prime Radiant pattern describes how *a single domain instance* is decomposed; this Individual / Department / Organisation model describes how *the company* is decomposed. Both apply simultaneously.)

### §4 — The compounding mechanism: the [[organisational-digital-twin]]

The framework's most distinctive contribution: a Janus-built-not-bought organisational digital twin patterned on Janus's own HGTFT product (the customer-facing physical-infrastructure twin). The HGTFT maintains a structured, continuously updated model of a building (geometry, mechanical systems, relationships, physics); the organisational twin maintains the same shape for the company (departments, roles, workflows, decisions, tools). **It's the same engineering discipline applied at a different scale, and Janus is uniquely positioned to build it because the organisational thinking — ontologies, knowledge graphs, structured data, continuous model updates — is already the company's core competency.**

Three sub-mechanisms make the twin viable:

- **§4.2 The sensor network — systems of record + AI-assisted capture.** Every enterprise system (Xero, Airwallex, Asana, Slack, Deel, CRM, Linear, Notion, Google Workspace) is a sensor; [[fireflies|Fireflies]] is elevated from "productivity tool" to **Core Infrastructure** because it converts tacit-knowledge meeting context into structured queryable signal. Every unrecorded meeting is a dead sensor.
- **§4.3 The trust layer — identity, access, permissioning.** The twin's viability scales with the rigour of its IAM. Microsoft Entra is the single identity source of truth; permissioning is role-based + data-classification-aware + jurisdiction-scoped; agent credentials are scoped per task. This is **Principle 9 — Identity Is the Perimeter**, a hard architectural gate, not a future concern.
- **§4.5 The flywheel.** Individuals produce structured outputs → agentic pipelines connect them → the twin becomes richer → richer context enables better individual outputs → coordination costs decrease as a proportion of total activity each cycle.

### §5 — Management disciplines per layer

| Layer | Manager's question | Failure mode | Success metric |
|---|---|---|---|
| Individual | Is this person doing high-leverage work? | Productivity theatre | Output quality per decision |
| Department | Is information flowing without human bottlenecks? | Over-engineering, brittle pipelines | Cycle time, data completeness |
| Organisation | Can we enter a new market without replicating the coordination layer? | Premature abstraction, empty digital twin | Revenue per employee, time to market entry |

Plus two cross-cutting disciplines: **Calibrating Agent Autonomy** (per task, not per agent; routine pipelines run unattended, strategic / financial decisions require HITL) and **The Effectiveness Gate** (before amplifying any activity with AI, ask: should this activity exist at all? Efficiency applied to unnecessary work is waste at scale).

### §6 — Application to Janus Digital

Current state by layer:

| Layer | Current Janus initiatives | Framework alignment |
|---|---|---|
| Individual | Claude Pro licences, Claude Code for Technology, Cowork for document workflows, Gemini for universal access | Force multiplier deployed; task-design discipline not yet formalised |
| Department | AIO standup pipeline ([[fireflies]] → Linear → Notion), Skills Library on GitHub, AI Registry as governance infrastructure, AIP-1 Finance API integration | Process architecture emerging; AIO is the proof-of-concept department |
| Organisation | AI Policy §5, AI Tool Evaluation Framework, organisational digital twin concept, AIP-11 Discovery Tool for cross-department intake; Entra as IdP with SSO compatibility enforced via G2.2 | Governance scaffolding in place; twin not yet populated with structured cross-department data; Layer 3 aspirational until Layer 2 replicates beyond AIO |

The AIO is deliberately operating as the **Layer-2 prototype**. Sequence: build it for ourselves → prove the compounding dynamic → document patterns (skills library) → replicate to Technology (via Euclid's team), Finance (via AIP-1), country operations.

### §7 — The nine [[architectural-design-principles|architectural design principles]]

The principles that govern system-design decisions across all three layers:

1. **Layer Sequence Is Not Optional** — Layer 1 feeds Layer 2 feeds Layer 3. Bottom-up build, top-down architecture.
2. **Automate Coordination, Not Judgment** — agents handle routing, context, status, structured data; humans handle strategy, relationships, exception handling, consequential decisions.
3. **Structured Data Is Capital** — every output should ask: does this produce machine-readable data that feeds the twin? PDFs / emails / unstructured Slack messages are dead sensors.
4. **Calibrate Autonomy Per Task** — per task, not per agent. Routine = autonomous; consequential = HITL.
5. **Systems of Record Are the Sensor Network** — Xero / Airwallex / Asana / Slack / Deel / CRM / Linear / Notion / Google Workspace. Slack is both communication surface AND system of record; the discipline is moving consequential information from the former into the latter (Canvases, structured intake, channel conventions).
6. **Capture Before You Coordinate** — universal meeting transcription is the foundational sensor layer for institutional memory. Every unrecorded meeting is a dead sensor.
7. **Portability Over Optimisation** — department-level agentic architectures must be designed for replication across geographies. Optimise for portability and standardisation before optimising for local performance.
8. **The Effectiveness Gate** — before amplifying any activity with AI, ask: should this activity exist at all?
9. **Identity Is the Perimeter** — every human and every agent authenticates through a single IdP (Entra). Permissions are role-based, data-classification-aware, jurisdiction-scoped. Agent credentials are scoped to the minimum systems and data tiers required.

### §8 — How to know it's working

Layer indicators + anti-indicators. The north-star metric is **revenue per employee increases as the organisation scales** — because the coordination tax is not scaling with headcount. The anti-indicators name the failure modes: outputs unconnected to systems of record, brittle pipelines, AI tools deployed without a layer-theory, agents with broader data access than task requires, coordination tax growing alongside AI investment rather than displaced by it.

## v0.1 → v0.3 drift

Both versions filed. v0.1 (2026-04-13) carries the academic grounding: Coase 1937 ("why do firms exist") on transaction costs as the basis for the coordination tax, Drucker 1954 (only marketing and innovation produce results; everything else is cost), Grove 1983 (manager's output as coordination equation; high-leverage activities), Brooks 1975 (n(n-1)/2 communication paths), Nonaka (tacit-to-explicit knowledge conversion). v0.3 (2026-04-30 / current) strips the academic citations for a more business-direct voice — same framework, different tone. v0.1's §2 was "Theoretical Foundations" (Coase / Drucker / Grove / Brooks); v0.3 reframes the same section as "The Coordination Tax" without naming the lineage. v0.1's §8 was "The Grove Test"; v0.3 retitles to "How to Know It's Working" with the Grove citation removed.

The academic lineage is still load-bearing for understanding *why* the framework is structured the way it is — Coase explains why the firm exists; Drucker explains why coordination is the tax; Grove explains why leverage matters; Brooks explains why it scales nonlinearly. Future versions may re-introduce a "Theoretical Lineage" appendix; for now, the citations live in v0.1 source as the reference.

## Cross-references — the Janus wiki application surface

- **Concepts**: [[coordination-tax]], [[coordination-three-layer-model]], [[organisational-digital-twin]], [[builders-sellers-measurers]] (Drucker-companion role taxonomy), [[stack-composition-framework]] (the vendor-selection lens), [[prime-radiant-three-layer-architecture]] (orthogonal three-layer model — distinct from this one).
- **Briefs (sibling AIO-thesis artefacts)**: [[ai-native-janus-positioning]] (Bonaventure's three-pillar positioning; this framework is the operational underpinning), [[ai-native-enterprise-restructuring]] (external validation from JPMorgan / Cloudflare / KPMG / Anthropic Q2), [[agentic-lean-marketing-stack]] (Layer 2 case study for Marketing).
- **Process**: [[ai-tool-evaluation-framework]] (Gate 2.2 = Principle 9 in operation), [[ai-registry]] (the governance infrastructure for the Layer-3 tool inventory).
- **Vendor**: [[fireflies]] (Core Infrastructure per §4.2), [[anthropic]] / [[claude]] (the Layer-1 force multiplier + Layer-2 connective tissue substrate), [[linear]] (Layer-2 system of record), [[notion]] (Layer-2 journal + decision capture), [[monday]] (Layer-2 execution surface).
- **Projects**: [[janus-prime-radiant-build]] (the Layer-3 substrate rollout), [[marketing-prime-radiant]] / [[it-ops-prime-radiant]] / [[hr-recruitment-pipeline]] / [[iso-compliance-programme]] (Layer-2 prototypes per department).

## Watch for

- **Promotion to thought-leadership content.** The framework is strong enough to externalise. Worth a Bonaventure-review cycle before publishing under Janus's name — both as positioning (the AI Native pitch gains a theoretical spine) and as risk-management (the "we built this management framework" narrative is more defensible than "we adopted AI tools").
- **v0.4 / v1.0 evolution.** Likely deltas: a "theoretical lineage" appendix re-introducing Coase / Drucker / Grove / Brooks / Nonaka; case studies as each Janus department's Layer-2 prototype matures (Marketing first per [[agentic-lean-marketing-stack]]); explicit metric thresholds (what cycle time is "good" at Layer 2? what revenue-per-employee target signals Layer 3 success?).
- **HGTFT-applied-to-self storyline.** §4.1's claim that Janus is "uniquely positioned" because the engineering discipline already exists in HGTFT is the most distinctive positioning argument in the document. Worth surfacing into [[ai-native-janus-positioning]] as a fourth-pillar candidate or as an underlay across the three existing pillars. **(Update 2026-05-21: HGTFT now has a wiki project hub at [[hgtft]] backed by the [[hgtft-neurips-2025|NeurIPS 2025 paper]] — the citable in-wiki artefact this positioning argument needs.)**
- **Identity-Is-the-Perimeter rollout.** Principle 9 is currently a Gate-1 SSO criterion (G2.2) but not yet enforced architecturally across systems. As Layer-3 sensor connections multiply, this becomes the binding constraint. Worth a focused [[it-ops-prime-radiant|IT/Ops]] workstream.
- **Microsoft Entra dependency.** The framework hard-codes Entra as the IdP. If Janus's identity strategy shifts (e.g., a different IdP per acquired entity, federation across jurisdictions), Principle 9 needs revisiting.

## Status

**Draft v0.3, ingested 2026-05-21.** Authoritative within the AIO as the operating thesis; not yet promoted to Janus-wide thought-leadership content. The wiki carries v0.3 as the canonical narrative reference; v0.1 retained as superseded provenance.
