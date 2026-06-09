---
type: concept
title: Organisational digital twin
slug: organisational-digital-twin
created: 2026-05-21
updated: 2026-06-08
departments: [ai-office, office-of-ceo, engineering]
status: active
sources: [2026-04-coordination-leverage-model-v0.3, 2026-04-coordination-leverage-model-v0.1, 2026-03-31-block-from-hierarchy-to-intelligence, 2026-04-24-yc-diana-hu-ai-native-company-from-ground-up, 2026-05-21-yc-blomfield-self-improving-company, park-van-der-aalst-dto-process-mining]
related: [coordination-leverage-model, coordination-three-layer-model, coordination-tax, digital-twin, digital-twin-of-the-company, fireflies, knowledge-graph, ai-tool-evaluation-framework, ai-native-mandate, janus-prime-radiant-build, prime-radiant-three-layer-architecture, ai-native-enterprise-restructuring, recursive-self-improving-loop, hgtft]
---

# Organisational digital twin

The compounding mechanism at the centre of the [[coordination-leverage-model|Coordination Leverage Model]]. A continuously-updated, structured model of the company itself — built on the same engineering discipline (ontologies, knowledge graphs, sensor networks, continuous model updates) that Janus already deploys in its **HGTFT** customer-facing platform for physical infrastructure. **It's not an analogy. It is the same architecture applied at a different scale, and Janus is uniquely positioned to build it because the engineering DNA is already in the company.**

## Why "digital twin" and not "knowledge base" or "data warehouse"

A data warehouse stores rows. A knowledge base stores documents. A digital twin maintains a *model* — entities, relationships, rules of behaviour — that supports queries, simulations, and predictions impossible from raw data alone.

The HGTFT (Janus's customer product) maintains a structured, continuously updated digital twin of a building: geometry, mechanical systems, their relationships, the physics that governs them. Built on ontologies and knowledge graphs defining what entities exist, how they relate, and what rules govern behaviour. Sensors feed real-time data into the model. The model supports queries ("what is the thermal load on floor 3?"), simulations ("if we replace this HVAC unit, what changes?"), and predictions ("when will this system fail?"). The twin's value compounds: every new data point makes it more accurate, every new relationship makes it more useful.

The **organisational** digital twin applies the same architecture to the company itself:

| HGTFT (physical twin) | Organisational digital twin |
|---|---|
| Building geometry and systems | Departments, roles, workflows, tools |
| Ontology of physical entities and relationships | Ontology of organisational entities and relationships |
| IoT sensors (temperature, occupancy, vibration) | Systems of record (Xero, Airwallex, Asana, Slack, Deel, CRM, Linear, Notion, Google Workspace) |
| Environmental monitoring (air quality, humidity) | AI-assisted capture ([[fireflies|Fireflies]] transcription — tacit knowledge made explicit) |
| Physics engine simulating behaviour | Agentic pipelines executing coordination logic |
| Knowledge graph of component dependencies | Knowledge graph of workflow dependencies, decision chains, data flows |
| Physical access zones and credential-gated systems | IAM layer: Entra SSO, RBAC, data-classification enforcement, agent-scoped credentials |
| Queries: "What is the thermal load on floor 3?" | Queries: "What is the AI adoption state in Finance?" |
| Predictions: "When will this system fail?" | Predictions: "Which workflows will bottleneck at 3× headcount?" |
| Continuous model updates from sensor data | Continuous model updates from transactional + conversational data |

## The sensor network

The fidelity of any digital twin is bounded by the breadth and accuracy of its sensor network. Every unstructured document, every decision made in email rather than a system of record, every piece of institutional knowledge that lives only in someone's head is a *dead sensor* — a gap in the twin that agents cannot see through.

Two classes of sensor feed the organisational twin:

### Systems of record — the transactional sensor network

Each enterprise system captures a different dimension of organisational state:

| System | What it captures | Organisational dimension |
|---|---|---|
| Xero | Invoices, expenses, reconciliations | Financial health and cash flow |
| Airwallex | Cross-border payments, FX, treasury | Multi-market financial operations |
| Asana | Tasks, projects, dependencies, workload | Operational execution and capacity |
| [[slack]] | Channels, threads, decisions-in-context, cross-department communication | Real-time coordination patterns and information flow |
| Deel | Contractors, compliance, payroll by jurisdiction | Workforce structure across geographies |
| CRM ([[agentic-lean-marketing-stack|Attio]]) | Pipeline, client interactions, conversion | Revenue generation and market engagement |
| [[linear]] | AI Registry, AI Projects, tool lifecycle | AI governance and internal build state |
| [[notion]] | Operational logs, meeting actions, knowledge base | Institutional memory and decision history |
| Google Workspace | Documents, communication, calendar | Collaboration patterns and information flow |

The architectural task is *not* to build new data sources but to connect existing ones into a coherent model — to wire the sensors into the twin. As systems of record are connected, the twin's resolution increases: it can answer questions spanning financial, operational, and strategic dimensions simultaneously, the way HGTFT spans structural, mechanical, and environmental dimensions of a building.

### AI-assisted capture — the tacit-knowledge sensor

[[fireflies|Fireflies]] is the **foundational capture layer**. Systems of record capture transactional data — *what was decided, what was paid, what was assigned*. But the most valuable organisational knowledge is generated *before* and *between* transactions: in the discussions where context is shared, trade-offs are weighed, priorities are debated, and decisions are shaped. This is tacit knowledge — the institutional intelligence that traditionally lives only in the heads of the people who were in the room.

Every meeting transcribed is a sensor reading that captures not just *what was decided* but **why** — the reasoning, the alternatives considered, the constraints acknowledged, the commitments made. Qualitatively different from meeting minutes or summaries. A summary is lossy compression; a transcription is a complete signal that can be reprocessed, queried, and connected to other data sources as the twin's analytical capability evolves.

This is why Fireflies is classified as **Core Infrastructure** in the AI Registry, not as a productivity tool. **Every meeting that is not recorded is a sensor that was never installed: the knowledge generated in that room is invisible to the twin and lost to the compounding mechanism.**

## The trust layer — identity, access, permissioning

A building's digital twin does not expose every sensor reading to every user. Facilities managers see mechanical-system data; tenants see comfort metrics; security personnel see access logs. The physical twin enforces access zones.

The organisational twin requires the same architecture. As more enterprise systems are wired in, the data flowing through it spans every confidentiality tier: financial records in Xero, payroll data in Deel, client pipeline in the CRM, strategic discussions in Fireflies transcripts. Without a robust IAM layer, the twin becomes a single point of data exposure rather than a controlled coordination mechanism.

**This is not peripheral — it is a hard architectural gate.** The twin cannot scale beyond a single team without it. The framework codifies four requirements:

- **Identity is the foundation.** Microsoft **Entra** is the single source of truth for authentication across all connected systems. SSO compatibility is already a Gate 1 criterion in the [[ai-tool-evaluation-framework]] (G2.2) — *this is why*. Tools that cannot integrate with the IdP cannot be wired into the twin.
- **Permissioning is granular and role-based (RBAC).** Permissions tied to organisational roles, not individual accounts. When someone changes role, their access profile changes automatically.
- **Data-classification enforcement is architectural, not policy-driven.** AI Policy §5.2.3 data-boundary rules (no sensitive data in public models; enterprise instances only for confidential data) must be enforced architecturally. The twin's query layer must respect classification tiers.
- **Agent credentials are scoped per task.** An agent processing standup transcripts should not have access to payroll data. Technical implementation of the "calibrate autonomy per task" design principle.

**Multi-jurisdiction compliance is a Layer-3 prerequisite.** Scaling across countries introduces data-residency requirements (GDPR, CCPA, PDPA, etc.) and cross-border data-transfer constraints. The IAM layer must enforce these at the infrastructure level: a Singapore-based agent querying the twin cannot surface EU employee data subject to GDPR restrictions, for example.

The framework principle: **the twin's value scales with the breadth of its sensor network; its viability scales with the rigour of its trust layer.** Connect more systems without adequate permissioning and you don't get a smarter organisation — you get a larger attack surface.

## How it compounds

The three-layer flywheel from the [[coordination-three-layer-model]]:

1. Individuals produce structured outputs (Layer 1) — the sensor network's edges.
2. Agentic pipelines connect and contextualise those outputs (Layer 2) — the data-integration layer.
3. The twin becomes richer and more capable (Layer 3) — the model.
4. Richer institutional context enables better individual outputs (back to Layer 1) — the feedback loop.
5. Coordination costs decrease as a proportion of total activity with each cycle — the compound return.

## Janus state

As of 2026-05-21, the twin is *aspirational at Layer 3*. Sub-mechanisms in flight:

- **Sensor network — partial.** [[linear]] AIR + AIP, [[monday]] execution, [[notion]] Operations Notebook, [[fireflies]] for AIO standups + recruitment + strategic meetings are wired. Xero / Airwallex / Asana / Deel / Slack-as-system-of-record / Google Workspace not yet wired. CRM ([[agentic-lean-marketing-stack|Attio]]) coming online in the June post-Singapore-launch window.
- **Trust layer — partial.** Microsoft Entra is the IdP; G2.2 enforces SSO at vendor evaluation. RBAC + data-classification + agent-scoped credentials not yet architecturally enforced — these are policy-driven today and need an [[it-ops-prime-radiant|IT/Ops workstream]] to harden.
- **Pipelines — first instances live.** [[standup]] (Fireflies → Linear → Notion → Prime Radiant inbox) and the [[ai-registry|/ai-registry]] + [[ai-tool-evaluation|/ai-tool-evaluation]] subagent dispatch are the current operational pipelines.
- **Ontology — emerging.** The wiki's frontmatter schema (entity / semantic / temporal / causal edges per CLAUDE.md §4) is the de-facto ontology layer for one corner of the twin. Full company-wide ontology not yet built.

The [[janus-prime-radiant-build|Janus Prime Radiant rollout]] is the operational expression of building the twin one department at a time.

## Academic grounding — action-oriented process mining (added 2026-06-08)

Park & van der Aalst (RWTH Aachen, PADS Group; [[park-van-der-aalst-dto-process-mining]]) provide the most concrete formal realization of a DTO for business process improvement yet surfaced. The same research group that produced the Object-Centric Petri Net (OCPN) formalism underlying HGTFT's graph layer.

Their **Digital Twin Interface Model (DT-IM)** architecture maps directly onto this concept's layers:

| DT-IM component | Mapping |
|---|---|
| **OCPN** — formal multi-object process model | Knowledge graph / ontology layer |
| **Operational view** — marking (which objects reside where) + diagnostics (KPIs, wait times) | Sensor network readout — real-time process state |
| **Control view** — valves and guards (configuration + routing/resource rules) | The configuration surface that agents can act on |
| **Action patterns** — `(constraint, action)` pairs | Closed-loop control rules: *if [avg-wait > 16h], then [skip-notification]* |
| **Action engine** — continuously evaluates constraints, triggers actions | Agentic pipeline layer — automated coordination logic |

Per [[park-van-der-aalst-dto-process-mining]] §I: *"a concrete realization and implementation of DTOs are missing both in research and in practice."* This paper fills that gap — and places Janus's operational pipelines (standup, AI registry, Prime Radiant) ahead of the academic state-of-the-art on "are these loops actually closed?"

**Proof-of-concept result.** Action patterns reduced average sojourn time in a notification step from 20 hours (no-intervention baseline) to 9 hours — 55% improvement, **fully automated**. The action engine detected the constraint violation and adjusted system configuration without human intervention. This is the clearest published evidence of a DTO closing the monitor-act loop in a real business process.

**PADS/RWTH connection.** Van der Aalst is the originator of process mining; PADS is the canonical research group in the space. The OCPN formalism they use is also the foundation of [[hgtft-neurips-2025]]'s graph layer. Janus's engineering DNA is directly downstream of this research lineage.

## External validation — Block (added 2026-05-31)

[[2026-03-31-block-from-hierarchy-to-intelligence|Block's "From Hierarchy to Intelligence" essay]] articulates the same architecture under different vocabulary at Fortune-500 scale (full read at [[2026-05-31-block-intelligence-not-hierarchy]]). The closest external articulation surfaced to date.

Block decomposes its company architecture into four components:

| Block component | Mapping to this concept |
|---|---|
| **Capabilities** — atomic financial primitives (payments, lending, card issuance, etc.) | The product / platform primitives layer; outside the twin proper |
| **Company world model** — *"how the company understands itself and its own operations, performance, and priorities, replacing the information that used to flow through layers of management"* | Identical to the **organisational digital twin** described above |
| **Customer world model** — per-customer / per-merchant representation built from transaction data, evolving toward causal and predictive models | The HGTFT-pattern customer twin — the customer-facing analogue Janus already operates in physical-infrastructure form |
| **Intelligence layer** — *"composes capabilities into solutions for specific customers at specific moments and delivers them proactively"* | The agentic pipelines layer that operates on top of the twin to drive coordination |

The architectural rhyme is striking. Block's framing of the *compounding signal* — *"The richer the signal, the better the model. The better the model, the more transactions. The more transactions, the richer the signal"* — is the same flywheel described under "How it compounds" above, named in transaction-platform vocabulary.

Block's org-design corollary — *"The intelligence lives in the system. The people are on the edge"* — is a useful complement to the [[builders-sellers-measurers]] frame for naming what humans contribute once the substrate is in place. The edge is where humans bring *"intuition, opinionated direction, cultural context, trust dynamics, the feeling in a room … especially ethical decisions, novel situations, and high-stakes moments."* This crisply names what [[pilot-in-command]] and the broader AIO governance vocabulary gesture toward.

Caveat: Block's framing is forward-looking. The essay states *"Block is in the early stages of this transition. It will be a difficult one, and parts of it will likely break before they work."* Treat the architecture as **what Block intends to operate**, not necessarily what Block operates today. The fact that Block has *publicly committed* to the pattern is itself the most important signal — see [[ai-native-enterprise-restructuring]] for the cross-cutting consensus-restructuring narrative.

## The loop dimension — added 2026-05-31 via the YC talks

The twin is the *substrate*. What operates against it is a population of [[recursive-self-improving-loop|recursive self-improving loops]] — surfaced into teachable vocabulary in Q2 2026 via two YC batch talks ([[2026-04-24-yc-diana-hu-ai-native-company-from-ground-up|Diana Hu, 2026-04-24]] and [[2026-05-21-yc-blomfield-self-improving-company|Tom Blomfield, 2026-05-21]]; pulse at [[2026-05-31-yc-formalises-self-improving-company-playbook]]). The twin without loops is inert; the loops without a twin are blind.

The architectural primitive (Sensor → Policy → Tools → Quality Gate → Learning) is the canonical instance of an *agentic pipeline* operating on the twin's data. Each loop:
- **reads** from the twin's sensor network (the systems-of-record + AI-captured conversation streams documented above);
- **acts** within policy-defined autonomy boundaries that match the twin's data-classification + permissioning tiers;
- **writes back** via tools that produce new structured artefacts the twin then absorbs;
- **filters** through a quality gate (evals, escalations to a human, supersession of prior decisions);
- **learns** by feeding its own failure cases back as next-iteration sensor inputs.

**Diana Hu's open-loop / closed-loop control-theory framing** is the most useful single addition to the twin's vocabulary that the YC talks contribute. Most pre-AI enterprise systems are open-loop: a decision is made, an action is taken, and the outcome is not systematically captured back into the deciding system. The twin's compounding property only materialises when the company's important processes are **closed-loop** — every output measured, every measurement fed back into the model. The list of AIO pipelines under "Janus state" below is, in those terms, the list of *closed loops* the twin already has; the work ahead is to identify the *open loops* (places where the company decides and acts but doesn't systematically learn) and convert them.

**AI-as-operating-system framing** — Diana Hu: *"AI should not be a tool your company uses. It should be the operating system your company runs on."* The twin is the substrate on which that operating system runs. The cleanest framing surfaced to date for what Prime Radiant *is*, and why Janus is building it.

## Related concepts

- **[[coordination-leverage-model]]** — the parent framework. This concept is the *compounding mechanism* the framework relies on.
- **[[coordination-three-layer-model]]** — the architectural sequence (Individual → Department → Organisation) that produces the twin's sensor data.
- **[[coordination-tax]]** — the economic primitive being reduced.
- **[[digital-twin]]** / **[[digital-twin-of-the-company]]** — predecessor stub concept pages that this entry promotes / supersedes. The two stubs are folded into this canonical page.
- **[[knowledge-graph]]** — the underlying data structure for the twin's ontology.
- **[[fireflies]]** — the foundational capture layer; Core Infrastructure per the framework.
- **[[ai-tool-evaluation-framework]]** — Gate 2.2 (Enterprise SSO) is the trust-layer enforcement mechanism.

## Watch for

- **HGTFT cross-reference.** The framework's claim that Janus is uniquely positioned because the engineering discipline already exists in HGTFT is the most distinctive positioning argument. **(Resolved 2026-05-21: [[hgtft]] project hub created and backed by the [[hgtft-neurips-2025|NeurIPS 2025 paper]]. The cross-reference now resolves.)**
- **Premature-abstraction risk.** The Layer-3 twin is only as good as the Layer-2 substrate. Building a "company dashboard" or "organisational query interface" before the sensors are wired is the anti-pattern the framework names explicitly.
- **The IAM hardening workstream.** Principle 9 (Identity Is the Perimeter) is currently policy-driven. Architectural enforcement (RBAC + data-classification + agent-scoped credentials) is the gating capability for Layer-3 activation. Worth a focused [[it-ops-prime-radiant|IT/Ops]] workstream.
- **Wiki-as-twin-substrate.** Janus Prime Radiant *is* one corner of the organisational twin — the synthesis layer + ontology. The relationship between the per-domain Prime Radiants and the company-wide twin is worth a future framing brief.
