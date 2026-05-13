---
type: concept
title: Prime Radiant three-layer architecture
slug: prime-radiant-three-layer-architecture
created: 2026-05-08
updated: 2026-05-08
departments: [ai-office]
sources: [2026-05-08-andrew-marketing-prime-radiant]
related: [llm-wiki, janus-prime-radiant-build, marketing-prime-radiant, 2026-05-08-signals-sensors-inferences-input-architecture, agent-memory, agentic-ai]
---

# Prime Radiant three-layer architecture

The Prime Radiant pattern decomposes any domain instance into three layers: **Signals**, **Infrastructure**, and **Outputs**. The model emerged from the 2026-05-08 brainstorm with [[andrew-soane]] designing the Marketing instance and was retroactively formalised in CLAUDE.md v0.8 as the canonical Prime Radiant architecture.

The three layers stack in a specific order, and the build sequence for any new instance follows that order.

## The three layers

### 1. Signals — raw inputs

Everything the instance is exposed to. The dense sensor array.

- Fireflies meeting transcripts
- Slack threads (typically bookmarked subset)
- System-of-record exports (Linear, Notion, Monday, CRM, ticket systems)
- Inbound web messages, contact-form submissions
- Emails (CRM-routed or raw)
- Curated articles via Web Clipper
- Automated news scraping per topic taxonomy
- Industry analyst opinions, competitor intel
- Voice / video conversations beyond Fireflies

**Discipline:** throw the net wide. AI handles volume. Under-collecting is the failure mode, not over-collecting. Each signal type has its own ingest rule documented in CLAUDE.md §5.1.

**Metaphor:** signals are *sensors* — like building sensors. An instance is only as smart as its sensor array is dense and varied.

### 2. Infrastructure — durable reference

Domain-specific framing documents that don't change often but provide the lens through which Signals become Outputs.

- Company mission and multi-year strategy
- Country plans (per `countries:` frontmatter values)
- Ideal Customer Profile (Marketing context)
- Target Personas (Marketing context)
- Tool evaluation criteria (AIO context)
- Policy frameworks
- Approved vendor categories
- Topic taxonomy (what's relevant to this domain?)
- The `departments:` and `countries:` vocabularies themselves

**Discipline:** Infrastructure tells the system *what relevance looks like*. Without it, dense Signals produce dense noise. With it, the same Signals produce precise relevance flags.

**Implicit vs explicit:** existing AIO Infrastructure is mostly implicit (CLAUDE.md itself, the SoR map, accumulated vendor evaluations). For new instances, the Infrastructure layer often needs to be made explicit before Outputs can emerge — that's the gating dependency for a Marketing or HR instance, not Signals (Signals can light up immediately).

### 3. Outputs — synthesis

What the instance produces back to the world.

- **Briefs** — the canonical Outputs artefact (see CLAUDE.md §6 brief shape). Aha-shape: the strategic implication for the owning entity, supported by industry analysis.
- Plans (annual, quarterly, country-specific)
- Positioning documents (Marketing — comes first, before campaigns)
- Campaign briefs and supporting assets (Marketing)
- White papers and long-form analysis
- Decision records (atomic, dated, in `decisions/`)
- Reporting decks (performance metrics that feed back into Signals as performance data)

**Discipline:** Outputs cannot be designed top-down without the Infrastructure layer. Pre-specifying what insights an instance "should" produce is a failure mode — narrow data + narrow questions = brittle outputs. Let Outputs emerge from the Signals × Infrastructure intersection.

**Outputs feed back as Signals.** Performance metrics from a campaign become Signals for the next planning cycle. A brief from one instance becomes a Signal in another instance when the topic crosses departments. The architecture is recursive at the boundary.

## Build sequence for a new instance

Per CLAUDE.md §1, this is the canonical order:

1. **Identify the Signals** (which sensors does this department have or need?). Stand up the sensor array as fast as possible — Fireflies, Slack bookmarks, system-of-record exports, Web Clipper.
2. **Curate the Infrastructure** (which strategic anchors define relevance?). Document the ICP, Personas, mission, country plans, topic taxonomy as durable reference pages.
3. **Let Outputs emerge.** Briefs, plans, positioning. Don't try to design these top-down before Signals are flowing and Infrastructure is documented.

Trying to skip step 2 produces brittle synthesis. Trying to start at step 3 produces empty templates. The order matters.

## Federation between instances

Cross-instance federation primarily happens at the **Outputs ↔ Signals boundary**. A brief from the Marketing instance becomes a Signal in the AIO instance when AI tooling is implicated. A decision from the AIO instance about a CRM evaluation becomes a Signal in the Marketing instance. The lightweight federation layer is the [[marketing|departments]] entity type — every instance has stub pages describing every department from its own vantage point, with cross-links pointing to the canonical Prime Radiant for that department.

Heavier federation mechanisms (shared backend, programmatic cross-vault references, automated signal flow between instances) are deferred until the multi-instance pattern is proven beyond Marketing.

## Per-domain examples

### AIO instance
- **Signals:** Fireflies (AIO meetings), Slack (bookmarked), Linear (AIR + AIP), Notion Operations Notebook, Monday Automations board, Web Clipper articles.
- **Infrastructure:** CLAUDE.md (rulebook), SoR map, AI Tool Evaluation Framework, vendor categories, policy gate process.
- **Outputs:** [[post-rag-agent-data-stack]] brief, [[agent-memory-2026-q2]] brief, AI Tool evaluation reports, decision records, lessons.

### Marketing instance (in flight)
- **Signals:** Fireflies (Andrew's calls), Slack, CRM (once selected), inbound web messages, emails, curated articles, news scraping per topic taxonomy.
- **Infrastructure (pending):** ICP, Target Personas, mission, country plans, topic taxonomy.
- **Outputs (pending):** Strategic POVs, white papers, blog posts, marketing plans, campaign briefs, positioning docs, reporting decks.

### HR instance (queued)
- **Signals:** Fireflies (interviews via centralised webhook), Slack, candidate flow data, scoring outputs from Rubric skill, exit interview data.
- **Infrastructure:** role profiles, scoring rubrics, employment templates per jurisdiction, employer brand guidelines.
- **Outputs:** hiring briefs, retention analysis, role calibration, capability gap analysis.

## Provenance

This concept page is the durable artefact for the architectural model that emerged in [[2026-05-08-andrew-marketing-prime-radiant|the 2026-05-08 brainstorm]] and was formalised in CLAUDE.md v0.8 the same day. The companion lesson [[2026-05-08-signals-sensors-inferences-input-architecture]] captures *how the model was discovered* in the conversation; this page captures *what the model is*.
