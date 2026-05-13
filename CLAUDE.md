# CLAUDE.md — Janus Prime Radiant Schema & Workflows

> **Status:** v0.10, 2026-05-13. This document is the load-bearing rulebook for the wiki. It tells you (the LLM) how to file things, what frontmatter to use, how to handle each source type, and when to run maintenance. It is expected to evolve. When rules feel wrong in practice, propose edits to this file rather than silently deviating.
>
> *v0.10 changes (2026-05-13):* explicit multi-graph framing added to §4 (the frontmatter encodes four orthogonal edge types — entity, semantic, temporal, causal — matching the agent-memory community vocabulary that converged in mid-May 2026); `captured_by` and `decided_by` fields formalised in the frontmatter schema. The Drive → Git substrate language rewrite previously slated for v0.10 has been deferred to v0.11 to keep this bump scoped.

---

## 1. Purpose

This is the **AI Office's institutional knowledge base** — the compounding record of decisions, lessons, vendor intelligence, and strategic synthesis for the Janus AI Office.

**Curation.** Michael Bruck is the primary curator. Other AI Office members ([[jehad-altoutou|Jehad]], [[andrew-soane|Andrew]], [[bonaventure-wong|Bonaventure]], [[simon-tarskih|Simon]], …) contribute directly or indirectly: skills like `/standup` deposit standup entries in Notion that the wiki ingests, and direct human contribution is expected to grow as the wiki matures and conventions stabilise.

**Audience.** AIO operators day-to-day; department heads and adjacent teams (IT/Ops, HR, Marketing, Finance) who reference AIO outputs; selected outward surfaces (Slack threads, Notion shareouts) when a brief or decision warrants it.

It serves three coexisting purposes:

1. **Work reference / lookup** — fast retrieval of vendor details, processes, decisions, project context for anyone working in or around the AI Office.
2. **AI tool & vendor intelligence** — durable, compounding synthesis of the AI tool landscape, complementing the AI Registry in Linear.
3. **Strategic synthesis** — briefs and pulse entries that connect external signals to AIO bets (see §6 brief shape), feeding planning conversations within AIO and surfacing outward when the implication warrants it.

Beyond its role as the AIO institutional KB, this wiki is also the **first live instance** of the Prime Radiant pattern in a Janus-wide rollout. The Marketing instance (pilot kicking off 2026-05-08 with [[andrew-soane]]) is being stood up in parallel; HR, Finance, IT/Ops, Office-of-CEO, Engineering, Training, and ISO are queued. The program-level effort is tracked in [[janus-prime-radiant-build]] and points toward a long-term **Janus digital knowledge twin** — federated, leadership-visible institutional memory across departments. The cross-instance linkage layer is the `entities/departments/` entity type (see §4). This wiki itself remains in active development — running additional instances does not freeze AIO honing.

The wiki is **the synthesis layer**. Linear, Notion, Fireflies, Slack, and Monday remain authoritative for their respective domains. The wiki holds the *narrative* and *cross-cutting analysis* across them.

### Naming — Janus Prime Radiant

The wiki system has a name: **Janus Prime Radiant** (after Hari Seldon's living psychohistory instrument in Asimov's Foundation series — the canonical artifact that holds all the equations of long-arc planning and updates as institutional knowledge accumulates).

The dashboard, the underlying file vault, and any consumer surface all carry this name. Per-domain instances are facets / views of one Prime Radiant rather than separate systems:

- **Janus Prime Radiant · AI Office** (this instance)
- **Janus Prime Radiant · Marketing** (planned per [[2026-05-07-llm-wiki-extends-to-marketing-domain]])
- **Janus Prime Radiant · HR**, **· Finance**, **· IT/Ops**, etc. (when those domains warrant their own instance)

This naming both signals the gravity of the system (this isn't a tracker; it's the institutional record that makes long-arc thinking possible) and gives department heads a familiar handle to ask for one of their own.

The reasoning behind the name — and why it was chosen over Asimov's other knowledge-system metaphors (Multivac, Galactic AC, etc.) — is captured in [[llm-wiki|the LLM Wiki concept page]]. The short version: the Prime Radiant is a *contributed-to instrument* used by trained practitioners to refine evolving equations of long-arc planning. The Multivac/AC lineage are *centralised oracles* that you query for answers. The wiki is the former, not the latter.

### Domain generalisability

This schema is designed to be portable across domain wiki instances, not just the AI Office wiki. A sibling **marketing-domain wiki** is in scope per [[2026-05-07-llm-wiki-extends-to-marketing-domain]], and the same pattern is expected to apply to other departments (HR, Finance, IT/Ops) when their knowledge surfaces grow large enough to warrant their own wiki.

What stays constant across domain instances: kebab-case file naming, frontmatter discipline, low/high-stakes ingest split, slug-form `[[wikilinks]]`, the inbox-as-intake flow, the lint cadence, the per-source-type ingest rules, the brief-shape guidance in §6.

What's per-domain: the entity vocabulary. The AIO wiki has `entities/vendors/`, `concepts/`, `projects/`, etc. A marketing-domain wiki might have `entities/outlets/`, `themes/`, `campaigns/`, `signals/`. The folder shape adapts; the discipline doesn't. Each domain wiki ships its own `CLAUDE.md` derived from this one with the entity vocabulary swapped.

This generalisability is the reason content shape (especially briefs) is captured in this rulebook rather than left to ad-hoc convention — the next domain instance reuses the same content discipline, only adapting the vocabulary.

### Architecture — three-layer model

The Prime Radiant pattern decomposes any domain instance into three layers. The model is portable across departments: the AIO instance and the in-flight Marketing instance both map onto it, and so will the queued HR / Finance / IT-Ops / Office-of-CEO / Engineering / Training instances when they spin up. This model emerged from the 2026-05-08 brainstorm with [[andrew-soane]] and was retroactively formalised here.

1. **Signals layer — raw inputs.** Everything the instance is exposed to: Fireflies transcripts, Slack threads, system-of-record exports (Linear, Notion, Monday, CRM), inbound web messages, emails, articles, news, competitor intel, industry analyst pieces. The discipline is *throw the net wide* — AI handles volume; under-collecting is the failure mode, not over-collecting. Each signal type has its own ingest rule (§5.1). The metaphor: signals are the *sensors* the instance uses to perceive its environment; an instance is only as smart as its sensor array is dense.

2. **Infrastructure layer — durable reference.** Domain-specific framing documents that don't change often but provide the lens through which signals become outputs: company mission, multi-year strategy, country plans (`countries:` frontmatter), Ideal Customer Profile and Personas (Marketing), tool evaluation criteria (AIO), policy frameworks, approved vendor categories, the `departments:` vocabulary. Without this layer, signals produce noise; with it, signals produce relevance. Most existing AIO infrastructure is implicit (CLAUDE.md itself, the SoR map, accumulated vendor evaluations). New instances may need their infrastructure layer made explicit — Marketing's outputs depend directly on the ICP, Personas, and country plans being documented.

3. **Outputs layer — synthesis.** What the instance produces back to the world: briefs (the aha-shape; see §6), plans, positioning documents, campaign briefs (Marketing), white papers, reporting decks, decision records. Outputs are how the instance *thinks out loud* — the brief is the canonical Outputs artefact because it explicitly connects external signals to internal bets. Federation between instances primarily happens at the Outputs ↔ Signals boundary: the Marketing brief on a regulatory shift becomes a Signal in the AIO instance when AI tooling is implicated; the AIO decision on a CRM evaluation becomes a Signal in the Marketing instance.

**Build sequence for a new instance.** Identify the Signals (which sources?), curate the Infrastructure (which strategic anchors?), then let Outputs emerge. Outputs cannot be designed top-down without the Infrastructure layer — that's the lesson from the Marketing brainstorm. The first deliverable when standing up a new domain instance is the Infrastructure inventory; the second is the sensor array; the synthesis follows.

**Cross-instance federation.** Each Prime Radiant instance is its own vault (separate folder, separate `CLAUDE.md` derived from this one). The `entities/departments/` pages are the lightweight federation layer — every instance has a stub for every department, describing that department from the instance's vantage point and pointing at the canonical Prime Radiant for that department where one exists. Heavier federation mechanisms (shared backend, programmatic cross-vault references) are deferred until the multi-instance pattern is proven.

### System-of-record map (as of 2026-05-06)

The canonical reference for the AIO operational flow is the `/standup` skill (v3.13+ by Jehad Altoutou). The wiki references the skill but does not duplicate it; if the skill drifts ahead, this map needs review.

- **Linear AIR** (AI Registry team) — sole source of truth for AI Tools Registry data. Managed *only* via the `/ai-registry` and `/ai-tool-evaluation` skills via subagent dispatch — never written to from this wiki, never written to from `/standup` directly.
- **Linear AIP** (AI Projects team) — status surface for AI Projects, reconciled from Monday execution. Lower wiki-worth than AIR; ingest only when explicitly flagged.
- **Monday Automations board** (`5095012818`) — primary execution surface for tasks, projects, action tracking, and AIO daily-standup execution. Adoption expanding to research projects (including this wiki build). The Monday AI Tools Registry board (`5095577150`) is deprecated as an active surface and not ingested.
- **Notion Operations Notebook** — forward-looking journal / reporting surface. Daily standup logs (`## AIO DD Mon YYYY` entries appended by `/standup`), decisions, next-step planning, registry/evaluation outcomes, project documentation.
- **Fireflies** — raw meeting transcripts. Authoritative for what was said.
- **Slack** — real-time discussion; wiki only ingests bookmarked threads.

---

## 2. Top-level structure

```
CLAUDE.md          → this file
index.md           → content catalog, organised by category, one line per page
log.md             → append-only chronological activity log

inbox/             → INTAKE QUEUE. Michael (or scheduled jobs) drop sources here.
                     LLM auto-ingests anything that lands here, files into sources/
                     and updates wiki pages. Original is moved to inbox/.processed/
                     after successful ingest.

sources/           → immutable raw inputs. LLM reads, never modifies after filing.
  articles/        → clipped web articles, blog posts, research papers
                     (Web Clipper markdown, Mivory backfill, Arxiv PDFs).
                     PDFs are stored as both `<slug>.pdf` (original) and
                     `<slug>.md` (extracted markdown twin) — see §5.1.
  meetings/        → Fireflies transcripts (raw, not Fireflies-generated summaries)
  linear/          → exported Linear issue snapshots
  notion/          → exported Notion page snapshots
  slack/           → exported Slack threads (from bookmarks)
  monday/          → exported Monday task snapshots
  misc/            → non-article binaries that don't deserve their own subfolder:
                     slides, supplementary attachments, standalone screenshots, etc.

entities/
  vendors/         → AI tools, SaaS vendors, services we evaluate or use
  clients/         → client context (when applicable)
  people/          → external network: analysts, founders, partners
  internal/        → Janus teammates, expertise map, role/scope
  departments/     → Janus departments as entities (ai-office, marketing, hr,
                     finance, it-ops, office-of-ceo, engineering, training, iso).
                     Federation layer between Prime Radiant instances — see §1
                     "Architecture — three-layer model" / Cross-instance federation.
                     Entity slugs match the values used in `departments:` frontmatter
                     (so [[marketing]] resolves to entities/departments/marketing.md).

concepts/          → frameworks, methodologies, technical primitives (RAG, MCP, etc.)
processes/         → runbooks, how-tos, internal procedures
projects/          → durable hub pages — link out to atomic pages, do not duplicate
decisions/         → atomic decision records (what / options / why / when / owner)
lessons/           → emergent retros: what didn't work and why
questions/         → open threads, things being investigated without answers yet.
                     ALSO used as the escalation channel for high-stakes ingest
                     ambiguity (see §5.1).
pulse/             → dated running log of industry / Janus-relevant developments
briefs/            → synthesis output: state-of-X, comparisons, quarterly recaps
```

### Filing rules

- **Folders answer "what kind of thing is this?"** Tags answer "who cares about it?"
- A page belongs in exactly one folder. If unclear, prefer the more atomic folder (e.g., file a one-off decision in `decisions/`, not in the project hub).
- `projects/` pages are **hubs**: scope, status, narrative. They link to decisions, lessons, vendor entities — they do not duplicate them.
- `briefs/` is for synthesis you've decided is worth preserving. A query result that earns its keep gets filed here.
- `pulse/` is the timeline; `briefs/` is the atemporal current view. Pulse entries feed briefs.
- A `question` becomes a `brief` once enough is known. Move the file; update the index.

---

## 3. Naming conventions

- **All filenames are kebab-case**, lowercase, no spaces, no underscores.
- ASCII only. Strip diacritics. Replace `&` with `and`.
- Prefer short slugs. Disambiguate by adding context, not by lengthening: `cursor-ide.md` not `cursor-the-ide-by-anysphere.md`.

### Per-folder naming

| Folder | Pattern | Example |
|---|---|---|
| `entities/vendors/` | `<vendor-slug>.md` | `linear.md`, `cursor-ide.md` |
| `entities/clients/` | `<client-slug>.md` | `acme-corp.md` |
| `entities/people/` | `<firstname-lastname>.md` | `andrej-karpathy.md` |
| `entities/internal/` | `<firstname-lastname>.md` | `michael-bruck.md` |
| `entities/departments/` | `<dept-slug>.md` (matches `departments:` frontmatter values) | `marketing.md`, `it-ops.md` |
| `concepts/` | `<concept-slug>.md` | `retrieval-augmented-generation.md` |
| `processes/` | `<process-slug>.md` | `vendor-onboarding.md` |
| `projects/` | `<project-slug>.md` | `ai-registry-v2.md` |
| `decisions/` | `YYYY-MM-DD-<slug>.md` | `2026-04-15-adopt-linear-for-ai-registry.md` |
| `lessons/` | `YYYY-MM-DD-<slug>.md` | `2026-03-02-fireflies-summaries-too-shallow.md` |
| `questions/` | `<question-slug>.md` | `do-we-need-a-vector-store.md` |
| `pulse/` | `YYYY-MM-DD-<slug>.md` | `2026-05-01-anthropic-skills-ga.md` |
| `briefs/` | `<topic>.md` (canonical) or `<topic>-YYYY-qN.md` (snapshot) | `agent-frameworks-2026-q2.md` |
| `sources/articles/` | `<source-slug>.md` | `karpathy-llm-wiki.md` |
| `sources/meetings/` | `YYYY-MM-DD-<meeting-slug>.md` | `2026-04-22-vendor-eval-cursor.md` |
| `sources/linear/` | `<team>-<id>.md` | `aio-142.md` |
| `sources/notion/` | `<page-slug>.md` or `<workspace>-<page-slug>.md` | `ops-notebook-q2-okrs.md` |
| `sources/slack/` | `YYYY-MM-DD-<channel>-<slug>.md` | `2026-04-30-eng-mcp-rollout.md` |
| `sources/monday/` | `<board>-<id>.md` | `ops-3492.md` |

### Disambiguation

If two candidates collide on slug:
- Add the most distinguishing qualifier: `cursor-ide.md` vs `cursor-cli.md`.
- Never use numeric suffixes (`cursor-2.md`). They tell you nothing.

---

## 4. Frontmatter schema

Every page (except `index.md`, `log.md`, raw `sources/*` files, and this file) has YAML frontmatter.

```yaml
---
type: vendor | concept | process | project | decision | lesson | question | pulse | brief | person | client | department
title: Human-readable title
slug: kebab-case-slug-matching-filename
created: YYYY-MM-DD
updated: YYYY-MM-DD
departments: [ai-office, it-ops, office-of-ceo, hr, finance, marketing, engineering, training, iso]
countries: [sg, gb, us]   # ISO 3166-1 alpha-2 codes; expandable as Janus expands
status: active | resolved | dormant | archived | superseded
owner: michael-bruck     # for project / decision / question; entity slug, not bare first name
decided_by: michael-bruck   # for decision pages — who made the call
captured_by: jehad-altoutou   # provenance — whose contribution / ingest produced this page (optional)
confidence: high | medium | low | rumor   # for vendor / pulse / brief
sources: [karpathy-llm-wiki, 2026-04-22-vendor-eval-cursor]   # source slugs
related: [linear, ai-registry-v2]   # other wiki page slugs
---
```

### Field rules

- `type`, `title`, `slug`, `created`, `updated` are **required on every page**.
- `departments` is required for any page tied to operational work. Omit for universal `concept` pages with no organizational locus.
- `countries` is required for pages with geographic specificity — country launches, country-specific vendor availability, jurisdiction-bound processes (HR, legal, tax). Omit when truly geo-agnostic.
- `status` is required for `project`, `decision`, `question`, `lesson`. Optional elsewhere.
- `owner` is required for `project`, `decision`, `question`. Use the entity slug (`michael-bruck`), not the bare first name — this makes the field a clean entity edge.
- `decided_by` is required for `decision` pages. The entity slug of whoever made the call. Distinct from `owner` (who carries the decision forward).
- `captured_by` is optional but encouraged. The entity slug of whoever's contribution or ingest pass produced the page. Useful provenance when a page comes from a personal-vault import (`captured_by: jehad-altoutou`) or a meeting transcript pass (`captured_by: claude` for fully-automated ingest).
- `confidence` is required for `vendor`, `pulse`, `brief`.
- `sources` lists the slugs (not paths) of items in `sources/` that informed the page. Update when new sources reinforce or contradict the page.
- `related` lists wiki page slugs (any folder) for explicit cross-linking. Use Obsidian-style `[[wikilinks]]` in the body too — both are useful.

### Department vocabulary (locked)

`ai-office`, `it-ops`, `office-of-ceo`, `hr`, `finance`, `marketing`, `engineering`, `training`, `iso`.

Do not invent new departments without proposing an addition first (file as a `questions/` page; Michael approves changes here).

**The `departments:` frontmatter values match `entities/departments/` slugs.** A page with `departments: [marketing, ai-office]` is asserting it's relevant to those two departments; the same slugs are the filenames of the entity pages (`entities/departments/marketing.md`, `entities/departments/ai-office.md`). This means `[[marketing]]` resolves cleanly to the entity page, and the frontmatter tag and the entity link share the same vocabulary. When new departments are added to the locked list, also create the corresponding `entities/departments/<slug>.md` page in the same change.

### Country vocabulary (expandable)

ISO 3166-1 alpha-2 codes. Lowercase. Currently in scope: `sg` (Singapore — opens 2026 W19), `gb` (UK — opens 2026 W20). Add others as Janus opens new offices.

### Frontmatter as multi-graph encoding

The frontmatter fields collectively encode this wiki as a **four-graph structure** over its pages. This isn't decorative — it's the same four-dimensional decomposition the agent-memory community converged on in mid-May 2026 (independently surfaced by Mnemon's four-graph store on 2026-05-12 and validated experimentally by MAGMA on 2026-05-13; see [[agent-memory]] for the cross-layer taxonomy and [[2026-05-13-magma-multi-graph-agentic-memory]] for the surfacing). Making the framing explicit here buys cross-domain legibility: anyone reading from the agent-memory literature immediately recognises what the wiki is doing, and downstream tooling (schema linters, query helpers, federation cross-references) can target this four-axis vocabulary as first-class operations.

| Edge type | Frontmatter encoding | Body encoding | Example query it answers |
|---|---|---|---|
| **Entity** | `departments`, `owner`, `decided_by`, `captured_by`; `related` when the target is a person / department / vendor / client | `[[person]]` / `[[department]]` / `[[vendor]]` wikilinks | "Every decision Bonaventure has touched." |
| **Semantic** | `related` when the target is a concept / brief / project | `[[concept]]` wikilinks; `## Adjacent concepts` sections; `## Related` footers | "What do we know about agent memory?" |
| **Temporal** | `created`, `updated`; date-prefixed slugs for `decision` / `lesson` / `pulse` | Dated body claims ("As of 2026-05-13, …") | "What changed between April and May?" |
| **Causal** | `sources` (precedent pages); chains of decision / lesson links via `related` | `## Why` / `## Evidence` sections; explicit "supersedes" prose; decision-record templates | "Why did we reject Viktor?" |

The four dimensions are **orthogonal** — a single page contributes to multiple graphs simultaneously. A decision page like `2026-05-13-andrew-soane-first-cross-dept-prime-radiant-rollout.md` has temporal edges (date prefix, `created`, `updated`), entity edges (`decided_by: michael-bruck`, `[[andrew-soane]]` body link), semantic edges (`related` to other rollout / federation decisions), and causal edges (`sources: [2026-05-13-aio-it-meeting]` pointing at the meeting where the call was made).

**Practical guidance for LLM-side curation.** When updating a page, ask which edges the new content adds or strengthens, not just "what content goes in the body." If a decision is being filed, make sure `decided_by`, `sources` (causal predecessor), and `related` (semantic and entity neighbours) are all populated — content alone without edges produces orphan pages even when the prose is good. When ingesting a meeting transcript, the edges to spend effort on are causal (which decisions did this meeting produce) and entity (who was in the room) — those are the edges the body alone won't reliably encode.

**Cross-layer framing.** Janus Prime Radiant is a long-term, multi-graph, file-based, human-and-LLM-co-maintained knowledge structure — the same architectural shape Mnemon and MAGMA validate at the agent-runtime layer, instantiated at the institutional-KB layer instead. Future schema iteration should preserve the four-axis vocabulary so cross-instance federation (per-department Prime Radiants) and agent-side tooling (Claude OS, MCP-mediated vault access) inherit a shared mental model rather than rederive it.

---

## 5. Workflows

There are four operations: **Ingest**, **Query**, **Lint**, and **Index update**.

### 5.1 Ingest

**Trigger:** anything appearing in `inbox/`. Michael drops sources there manually (clipped articles, PDFs, URL files, transcripts), or scheduled jobs deposit candidates there.

#### The flow

1. **Detect** the new file in `inbox/`. Identify type from extension/content (article markdown, PDF, transcript, Linear export, Notion export, Slack thread, Monday task).
2. **Normalize and file the source.** Move it to the appropriate `sources/<subfolder>/` with the correct kebab-case name per §3. Download embedded images locally where applicable.
3. **Read it fully.**
4. **Identify wiki impact.** Which entities, concepts, decisions, projects, briefs are referenced or affected.
5. **Update the wiki directly** for low-stakes updates (see below).
6. **Escalate high-stakes actions** to a `questions/` page rather than acting unilaterally (see below).
7. **Move the original** from `inbox/` to `inbox/.processed/<YYYY-MM>/` for audit. Never delete.
8. **Append one entry to `log.md`** detailing what happened.
9. **Update `index.md`** for any created/renamed/deleted pages.
10. **Increment the ingest counter** (counted off `log.md`; lint trigger fires at 10).

#### Low-stakes vs. high-stakes (the trust line)

**Low-stakes — write directly:**
- Updating an existing entity/concept/project page with new factual content from the source.
- Adding a new `pulse/` entry (always atomic, always reversible).
- Adding source slugs to a page's `sources:` frontmatter.
- Adding `[[wikilinks]]` between existing pages.
- Creating a new source file in `sources/`.

**High-stakes — file a `questions/` page for Michael's review before acting:**
- Creating a new entity page (vendor, person, client, internal) — name collision risk, duplication risk.
- Creating a new concept page when a similarly-named one might exist.
- Merging, renaming, or deleting any existing page.
- Removing or contradicting an existing claim that's load-bearing on another page.
- Anything where confidence is `low` or `rumor` and the change is durable.

The escalation page is named `questions/ingest-YYYY-MM-DD-HHMM-<slug>.md` with the proposed action, the reasoning, and the alternative interpretations. Michael resolves these in batches.

#### Logging format

```
## [YYYY-MM-DD HH:MM] ingest | <source slug> | <source type>
- filed source: sources/<subfolder>/<slug>.md
- updated: <list of wiki pages modified>
- created: <list of wiki pages created>
- escalated: <list of questions/ pages created, if any>
- notes: <one line>
```

**Batch ingests** are permitted when many sources arrive together as a clear unit of work (e.g., a Mivory backfill, a thematic article dump on the same day). Use one log entry with header `## [YYYY-MM-DD HH:MM] batch-ingest | <description> | N items`, listing the filed source slugs and cumulative wiki impact (created concepts, updated pages, escalations, ingest counter increment). One batch entry per natural unit of work; per-source entries when sources are unrelated.

#### Per-source ingest rules

**Articles (`sources/articles/`)** — clipped web articles, blog posts, and research papers (including Arxiv PDFs).
- *Going-forward intake:* Obsidian Web Clipper writes markdown directly to `inbox/`. iOS share sheet for mobile.
- *One-time backfill:* Mivory bulk export (one-time only, then retire Mivory in favour of Web Clipper).
- Treat as high-signal (Michael curated it).
- Likely outputs: 1 brief or pulse update, 1-3 concept updates, 0-2 vendor updates, 0-1 new question.
- Always download embedded images locally.

*PDFs and research papers* — same pipeline, different ingest detail:
- PDF lands in `inbox/<paper-name>.pdf`.
- Read the PDF natively (chunked for long ones).
- Write a cleaned markdown version to `sources/articles/<paper-slug>.md` with frontmatter (title, authors, Arxiv ID if applicable, abstract, sections preserved as best as fidelity allows).
- Move the original PDF to `sources/articles/<paper-slug>.pdf` so the binary stays alongside its markdown twin. Markdown is the indexable layer; PDF is the source of truth for figures, tables, equations.
- *Arxiv-specific:* when fidelity matters (math-heavy papers), prefer fetching the LaTeX source from `arxiv.org/e-print/<id>` and converting that — cleaner equations, cleaner section structure. For most ingests, PDF read is sufficient.

**Meetings (`sources/meetings/`)** — Fireflies transcripts.
- **Use the raw transcript only.** Ignore Fireflies' own summary (low signal, often misses nuance).
- **Skip recurring 1:1s and team standups by default.** The `standup` skill already handles standups separately; double-ingesting wastes effort.
- **Manual override:** if Michael flags a transcript as `force-ingest` (e.g., a 1:1 where a strategic decision happened), process it normally. The override mechanism is a `force: true` line in a sidecar file `inbox/<transcript-id>.flags.md` or just an instruction in chat.
- Likely outputs: 1-3 decisions, 0-2 lessons, vendor entity updates if vendors discussed, project hub updates.
- Extract action items as candidates for Linear/Monday tickets — flag them in the log entry, do not create tickets from the wiki ingest.

**Linear (`sources/linear/`)** — primarily Linear AIR (AI Tools Registry); selectively Linear AIP (AI Projects).
- *Linear AIR scope:* closed/resolved AI tool evaluation issues with substantive resolution comments. The `/ai-registry` and `/ai-tool-evaluation` skills are the canonical interface; the wiki ingests exported snapshots when an evaluation produced narrative worth synthesising.
- *Linear AIP scope:* lower-priority. AIP is a status surface reconciled from Monday; ingest only when explicitly flagged.
- Filter: closed in the last N days AND has a resolution comment OR is labelled architecture/decision/post-mortem.
- Likely outputs: vendor entity updates, decision records (when resolution explains the *why*), AI Tools Registry / project hub updates.
- Skip routine bug fixes and process tickets unless they reveal a lesson.

**Notion (`sources/notion/`)** — Operations Notebook (the forward-looking journal/reporting surface) plus project documentation.
- Highest-signal entries are the daily standup logs (`## AIO DD Mon YYYY`) appended by `/standup` — these consolidate decisions, next-step planning, and registry/evaluation outcomes from each day in one place.
- Filter: pages updated in the last N days in scoped workspaces (Operations Notebook standup entries, project pages tied to active Monday projects).
- Likely outputs: decision records (extracted from standup `Decisions` blocks), project hub updates, occasional process page updates.
- Notion's structured pages (databases) often map to entity pages — extract carefully.

**Slack (`sources/slack/`)** — bookmarked threads only.
- Treat as high-signal (Michael bookmarked it).
- Pull whole-thread context, not just the bookmarked message.
- Likely outputs: decisions (Slack is where many real decisions actually happen), pulse entries (industry news shared in channels), entity updates.

**Monday (`sources/monday/`)** — primary execution surface: the Automations board (`5095012818`) plus research-flagged boards. The deprecated AI Tools Registry board (`5095577150`) is *not* ingested.
- Filter: completed tasks with substantive notes; tasks on research-flagged boards; standup-execution items where the Description Update (per `/standup`'s Context Coverage Invariant — every touched item carries a `<h2>Description (from meeting notes)</h2>` block) carries non-trivial rationale.
- Likely outputs: project hub updates, lesson records when a task uncovers a runbook gap, occasional decision records.

### 5.2 Query

Trigger: Michael asks a question against the wiki.

1. Read `index.md` first. It is your entry point.
2. Identify candidate pages by category and slug. Read those pages.
3. If the question spans the wiki (e.g., "what do we know about agent frameworks?"), pull all relevant entities/concepts/briefs. Use grep on frontmatter (`grep -l "departments:.*ai-office"`, `grep -l "countries:.*sg"`, etc.) for tag-based slicing.
4. Synthesize the answer. Cite wiki page slugs where claims come from.
5. **Offer to file the answer back as a brief or update.** If Michael accepts, write it directly (low-stakes) or escalate (high-stakes) per §5.1.
6. Append to `log.md`:
   ```
   ## [YYYY-MM-DD HH:MM] query | <one-line question>
   - pages read: <count>
   - filed back: yes/no (target)
   ```

### 5.3 Lint

**Trigger: automatic suggestion after 10 ingests since last lint, or on-demand any time.**

Track ingest count by counting `^## \[.*\] ingest` lines in `log.md` after the most recent `lint` line. When the count hits 10, surface a lint suggestion to Michael at the start of the next session.

Lint pass checks:
1. **Contradictions** — pages that disagree with each other on facts. Flag pairs.
2. **Stale claims** — pages whose `updated` field is older than the most recent source about that topic. Flag for refresh.
3. **Orphan pages** — pages with no `related` references and no inbound `[[wikilinks]]`. Decide: keep, link, or archive.
4. **Missing pages** — concepts/entities/people mentioned across multiple pages but lacking their own page. Propose creation (as `questions/` escalations).
5. **Broken references** — `related:` slugs and `[[wikilinks]]` that point to non-existent files.
6. **Frontmatter compliance** — pages missing required fields per type.
7. **Question aging** — questions older than 30 days that have accumulated 3+ supporting sources are candidates for promotion to brief.
8. **Unresolved escalations** — `questions/ingest-*.md` pages older than 14 days waiting on Michael.

Output a lint report to a single page named `pulse/YYYY-MM-DD-lint.md` (yes, lint reports live in pulse — they're dated observations about the wiki) with sections per check above and proposed remediation for each finding.

Append to `log.md`:
```
## [YYYY-MM-DD HH:MM] lint
- findings: <count>
- report: pulse/YYYY-MM-DD-lint.md
```

### 5.4 Index update

`index.md` is the content catalog. Update it on every create/rename/merge/delete during ingest — never lazily, always immediately.

`index.md` format:

```markdown
# Wiki Index

_Updated: YYYY-MM-DD_

## Vendors
- [linear](entities/vendors/linear.md) — issue tracking, system of record for AI Registry. [active, high]
- ...

## Concepts
- ...

## Decisions
- [2026-04-15-adopt-linear-for-ai-registry](decisions/2026-04-15-adopt-linear-for-ai-registry.md) — chose Linear over Asana for AI Registry. [resolved]
- ...
```

Each line is one wiki page. Format: `- [slug](relative/path.md) — one-line description. [status, confidence if relevant]`. Keep descriptions to ~12 words.

---

## 6. Tone and style for LLM-written pages

- **Terse and concrete.** Prose over bullets unless the content is genuinely a list.
- **Date claims.** "As of 2026-05-06, …". Anything that could go stale gets a date.
- **Cite sources.** Reference source slugs in `sources:` frontmatter and inline where load-bearing: "Per `karpathy-llm-wiki`, …".
- **Cross-link liberally.** Use `[[wikilinks]]` for any wiki entity, concept, project, decision mentioned. Cross-references are half the value of the wiki.
- **Use slug form for `[[wikilinks]]`.** Always link to the kebab-case slug (`[[llm-wiki]]`), optionally with a display alias (`[[llm-wiki|LLM Wiki]]`) when capitalisation matters in prose. Never use the title form alone (`[[LLM Wiki]]`) — it relies on Obsidian's title-matching heuristics and is harder to grep.
- **In `related:` frontmatter, use plain slugs.** Never `[[wikilink]]` syntax inside the YAML list — the brackets break the parser. Correct: `related: [fireflies, llm-wiki, standup]`. Incorrect: `related: [[fireflies]], [[llm-wiki]]`.
- **Hedge appropriately.** Use `confidence` frontmatter and inline hedges ("likely", "reportedly", "unconfirmed") for vendor/pulse claims.
- **Don't paraphrase to fill space.** A 3-sentence vendor page is fine if 3 sentences is what's known.
- **Never quote sources at length.** Summarize. Brief direct quotes (under 15 words) only when wording matters.

### Briefs are the strategic-aha shape, not the industry-summary shape

A brief is *not* a neutral synthesis of external sources. It's the answer to **"so what — why does this aggregated signal matter to the owning entity's bets?"** Industry analysis is the supporting evidence; the strategic implication is the headline.

**Required brief structure:**

1. **Title** — name the strategic angle, not the industry topic. Compare:
   - Weak (industry-shape): "The post-RAG agent data stack"
   - Strong (aha-shape): "Post-RAG agent data stack — why compilation-stage knowledge is the LLM Wiki bet"
2. **Opening paragraph (the lede)** — state the strategic implication for the owning entity in 2–4 sentences. This is what shows up as the page's "summary" in dashboards and indexes, so it has to land the so-what without supporting paragraphs.
3. **"Why this matters to <owner>" section** — expand the implication. What bet does this signal support, challenge, or motivate? What changes operationally as a result? Cross-link to the relevant project / decision pages.
4. **Industry analysis** — the synthesis of external sources, framed as evidence backing the implication. Use the standard "what changed", "what to watch for", "open questions" structure that befits the underlying material.
5. **Cross-references** — to sibling briefs (a brief rarely stands alone — it usually pairs with another aha), to the projects / decisions it informs, and to the source slugs in `sources:`.

**Domain generalisability of the brief shape:**

The AIO wiki's briefs surface ahas behind *AI Office bets* (e.g., the Janus Prime Radiant strategic direction). A marketing-domain wiki's briefs would surface ahas behind *brand / positioning / messaging bets*, synthesised from market signals + the marketing department's operating principles + competitor moves + customer transcripts. An HR-domain wiki's briefs would surface ahas behind *talent / culture bets*. The shape is the same; only the entity vocabulary and the bets being supported differ.

This is what makes the wiki *compounding*: each brief connects external signals to the owning entity's specific bets, so the body of briefs over time documents the evolving strategy — not just "what's happening in the world" but "what's happening, and what we're choosing to do about it."

A neutral industry summary belongs in `concepts/` or `pulse/` instead. A brief earns the name only if it lands a strategic implication.

---

## 7. Things this document does not yet cover

- Publishing to Notion / team sharing (deferred).
- Schema for `pulse/` filtering — what counts as wiki-worthy industry news vs. noise.
- Auto-running scheduled ingest jobs (the cron / scheduled-task layer for Fireflies, Linear, Notion, Monday pulls).
- Exact mechanics of the Mivory one-time bulk import.
- iOS / mobile capture flow once Web Clipper is set up on desktop.
- Treatment of `misc/` binaries (slides, screenshots, supplementary attachments) — covered when the first one arrives.
- Multi-tenant client work (currently `clients/` is one folder; revisit if scope grows).

When these become live questions, propose edits to this file.
