---
type: source
source_type: laptop
title: personal-claude-md
slug: personal-claude-md
created: 2026-05-14
captured_by: jehad-altoutou
audience: personal
original_path: /Users/jehad/Documents/janus-brain-bootstrap/skills/janus-brain/templates/personal-claude-md.md
original_size: 16711
original_ext: .md
category: notes
extracted_with: text-copy
extracted_at: "2026-05-14T09:51:46Z"
sensitivity: dept
sensitivity_confidence: 0.95
sensitivity_reason: "Per-person CLAUDE.md template scaffolded by `/janus-brain`; documents the single-vault model — no PII"
---

# personal-claude-md

_Extracted from `Documents/janus-brain-bootstrap/skills/janus-brain/templates/personal-claude-md.md` on 2026-05-14._

# CLAUDE.md — {{PERSON}} (`people/{{PERSON_SLUG}}/` inside the {{PRIMARY_DEPT}} vault)

> **Status:** Per-person rulebook v0.2 (single-vault model, rewrite 2026-05-14). Scaffolded {{DATE}} by `/janus-brain`. **This file is the contract for everything {{PERSON}} captures into the shared {{PRIMARY_DEPT}} Prime Radiant.** Edit it when rules feel wrong — do not silently deviate.

> **Important:** the surrounding repo is **shared with your teammates** in the {{PRIMARY_DEPT}} department. Anything you commit to `people/{{PERSON_SLUG}}/sources/` or `people/{{PERSON_SLUG}}/meetings/` is visible to them once pushed. Genuinely private items go in `people/{{PERSON_SLUG}}/private/`, which is **gitignored** and never leaves your laptop. The enrichment subagent classifies sensitivity (`dept` | `self` | `confidential`) per source and routes accordingly; items below 0.7 confidence are logged to `.review-queue.md` for you to confirm.

---

## 1. Purpose

This file scopes **{{PERSON}}'s personal subtree** (`people/{{PERSON_SLUG}}/`) inside the shared {{PRIMARY_DEPT}} Prime Radiant vault. The repo is one of the dept-tier Prime Radiants under `Janusd-io/janus-prime-radiant-<dept>`; every teammate clones the same repo as their single Obsidian vault and contributes to it. Your subtree captures everything you personally touched (meetings, Notion entries, laptop docs) before it surfaces in dept-shared structures (decisions, projects, vendors, concepts at the vault root).

### Three purposes

1. **Personal work reference** — fast retrieval of what {{PERSON}} has worked on, decided, learned, and read.
2. **Department contribution** — sanitised personal pages federate up to the relevant department Prime Radiant (e.g. `departments: [ai-office]` → AI Office instance).
3. **Signal source** — meetings, articles, laptop documents that {{PERSON}} captures become signals for their department's synthesis layer.

### Where this fits

The wiki is **the synthesis layer**. Linear, Notion, Fireflies, Slack, Monday remain authoritative for their respective domains. This wiki holds {{PERSON}}'s *narrative* and *cross-cutting analysis* across them.

### Curation

{{PERSON}} is the curator of this instance. The `/janus-brain` skill (nightly cron + on-demand `/janus-brain sync`) handles ingest. New entities and high-stakes changes escalate to `questions/` for {{PERSON}}'s review.

---

## 2. Top-level structure

```
CLAUDE.md          → this file
index.md           → content catalog, organised by category, one line per page
log.md             → append-only chronological activity log

inbox/             → INTAKE QUEUE. Bootstrap drops sources here (Fireflies, laptop scan, manual).
                     Skill auto-ingests, files into sources/, updates wiki pages.
                     Originals move to inbox/.processed/ after successful ingest.

sources/           → immutable raw inputs. Read, never modified after filing.
  laptop/          → files captured from {{PERSON}}'s laptop scan (deeply enriched)
  meetings/        → Fireflies transcripts (raw, not Fireflies-generated summaries)
  articles/        → Web Clipper, Mivory backfill, Arxiv PDFs
  linear/          → exported Linear issue snapshots
  notion/          → exported Notion page snapshots
  slack/           → exported Slack bookmarked threads
  monday/          → exported Monday task snapshots
  misc/            → standalone screenshots, slides, supplementary attachments

entities/
  internal/        → Janus teammates {{PERSON}} works with (mirrors AIO vocabulary)
  vendors/         → AI tools, SaaS vendors {{PERSON}} evaluates or uses
  clients/         → client context (when applicable)
  external/        → external network: analysts, founders, partners
  departments/     → Janus departments as entities; federation layer up to dept instances.
                     Slugs match the AIO-locked vocabulary (see §4).

concepts/          → frameworks, methodologies, technical primitives
processes/         → runbooks, how-tos, internal procedures {{PERSON}} owns or uses
projects/          → durable hub pages for projects {{PERSON}} is involved in
decisions/         → atomic decision records (what / options / why / when / owner)
lessons/           → emergent retros: what didn't work and why
questions/         → open threads; ALSO escalation channel for high-stakes ingest ambiguity
pulse/             → dated running log of industry / Janus-relevant developments
briefs/            → synthesis output: state-of-X, comparisons, quarterly recaps
```

### Filing rules

- **Folders answer "what kind of thing is this?"** Tags (`departments:`, `countries:`) answer "who cares about it?"
- A page belongs in exactly one folder. If unclear, prefer the more atomic folder.
- `projects/` pages are **hubs**. They link to decisions, lessons, vendor entities — they do not duplicate them.
- `briefs/` is for synthesis worth preserving. A query result that earns its keep gets filed here.
- `pulse/` is the timeline; `briefs/` is the atemporal current view. Pulse entries feed briefs.
- A `question` becomes a `brief` once enough is known. Move the file; update the index.

---

## 3. Naming conventions

- **All filenames are kebab-case**, lowercase, no spaces, no underscores.
- ASCII only. Strip diacritics. Replace `&` with `and`.
- Prefer short slugs. Disambiguate by adding context, not by lengthening.

### Per-folder naming

| Folder | Pattern | Example |
|---|---|---|
| `entities/vendors/` | `<vendor-slug>.md` | `linear.md`, `cursor-ide.md` |
| `entities/clients/` | `<client-slug>.md` | `acme-corp.md` |
| `entities/external/` | `<firstname-lastname>.md` | `andrej-karpathy.md` |
| `entities/internal/` | `<firstname-lastname>.md` | `michael-bruck.md` |
| `entities/departments/` | `<dept-slug>.md` | `ai-office.md`, `marketing.md` |
| `concepts/` | `<concept-slug>.md` | `retrieval-augmented-generation.md` |
| `processes/` | `<process-slug>.md` | `vendor-onboarding.md` |
| `projects/` | `<project-slug>.md` | `airwallex-finance-platform.md` |
| `decisions/` | `YYYY-MM-DD-<slug>.md` | `2026-04-15-adopt-linear-for-ai-registry.md` |
| `lessons/` | `YYYY-MM-DD-<slug>.md` | `2026-03-02-fireflies-summaries-too-shallow.md` |
| `questions/` | `<question-slug>.md` | `do-we-need-a-vector-store.md` |
| `pulse/` | `YYYY-MM-DD-<slug>.md` | `2026-05-01-anthropic-skills-ga.md` |
| `briefs/` | `<topic>.md` or `<topic>-YYYY-qN.md` | `agent-frameworks-2026-q2.md` |
| `sources/laptop/` | `<rel-source-path-as-slug>.md` | `documents-clients-acme-notes.md` |
| `sources/meetings/` | `YYYY-MM-DD-<meeting-slug>.md` | `2026-04-22-vendor-eval-cursor.md` |
| `sources/articles/` | `<source-slug>.md` | `karpathy-llm-wiki.md` |

### Disambiguation

If two candidates collide on slug, add the most distinguishing qualifier (`cursor-ide.md` vs `cursor-cli.md`). Never use numeric suffixes.

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
departments: [ai-office, it-ops, office-of-ceo, hr, finance, marketing, engineering, training]
countries: [sg, gb, us]
status: active | resolved | dormant | archived | superseded
owner: {{PERSON_SLUG}}          # for project / decision / question
confidence: high | medium | low | rumor
sources: [karpathy-llm-wiki, 2026-04-22-vendor-eval-cursor]
related: [linear, ai-registry-v2]
audience: [personal | department | org | ceo-only]   # routing key for federation (§5.5)
captured_by: {{PERSON_SLUG}}    # liability anchor — set on capture, never strippable
---
```

### Field rules

- `type`, `title`, `slug`, `created`, `updated`, `captured_by` are **required on every page**.
- `departments` is required for any page tied to operational work. Omit for universal `concept` pages with no organizational locus.
- `countries` is required for pages with geographic specificity. Omit when geo-agnostic.
- `status` is required for `project`, `decision`, `question`, `lesson`.
- `owner` is required for `project`, `decision`, `question`.
- `confidence` is required for `vendor`, `pulse`, `brief`.
- `audience` is required for every wiki page (used by federation; see §5.5). Defaults to `[department]` when uncertain (per user preference 2026-05-11).
- `sources` lists the slugs (not paths) of items in `sources/` that informed the page.
- `related` lists wiki page slugs. Use Obsidian-style `[[wikilinks]]` in the body too.

### Department vocabulary (locked — mirrors AIO)

`ai-office`, `it-ops`, `office-of-ceo`, `hr`, `finance`, `marketing`, `engineering`, `training`.

Do not invent new departments. File any proposed addition as a `questions/` page and surface to Michael (AIO curator).

### Country vocabulary (expandable)

ISO 3166-1 alpha-2 codes, lowercase. Currently in scope: `sg`, `gb`, `us`.

### Audience vocabulary

| Value | Federates to |
|---|---|
| `personal` | Personal vault only |
| `department` | The Person's primary department instance(s) only — never org, never CEO |
| `departments:<a>,<b>` | Only the listed department instances (cross-dept meetings) |
| `org` | All department instances + the Org instance |
| `ceo-only` | Personal + CEO instance, never any department |

---

## 5. Workflows

Five operations: **Ingest**, **Query**, **Lint**, **Index update**, **Federate**.

### 5.1 Ingest

**Trigger:** anything appearing in `inbox/`. The `/janus-brain` skill drops sources there (Fireflies pull, laptop scan, manual drop).

1. **Detect** the file. Identify type from extension + content (laptop file, Fireflies transcript, article markdown, PDF, Linear/Notion/Monday/Slack export).
2. **Normalize and file the source.** Move to `sources/<subfolder>/` with kebab-case name per §3.
3. **Read it fully.**
4. **Identify wiki impact** — entities, concepts, decisions, projects, briefs referenced or affected.
5. **Update the wiki directly** for low-stakes updates.
6. **Escalate high-stakes actions** to `questions/` rather than acting unilaterally.
7. **Move the original** from `inbox/` to `inbox/.processed/<YYYY-MM>/`. Never delete.
8. **Append one entry to `log.md`** detailing what happened.
9. **Update `index.md`** for any created/renamed/deleted pages.
10. **Increment the ingest counter** (lint trigger at 10).

### Low-stakes vs high-stakes (the trust line)

**Low-stakes — write directly:**
- Updating an existing entity/concept/project page with new factual content from the source.
- Adding a `pulse/` entry (atomic, reversible).
- Adding source slugs to `sources:` frontmatter.
- Adding `[[wikilinks]]` between existing pages.
- Creating a new source file in `sources/`.

**High-stakes — file a `questions/` page:**
- Creating a new entity page (vendor, person, client, internal).
- Creating a new concept page when a similarly-named one might exist.
- Merging, renaming, or deleting any existing page.
- Removing or contradicting a load-bearing claim.
- Anything where `confidence` is `low` or `rumor` and the change is durable.
- **Any laptop file with sensitivity markers** ({{PERSON}}-specific: salary, performance, legal, medical, financial-personal) — defaults to `audience: [personal]` and escalates if the bootstrap can't decide.

The escalation page is named `questions/ingest-YYYY-MM-DD-HHMM-<slug>.md` with the proposed action, reasoning, and alternative interpretations.

### Per-source ingest rules

**Laptop files (`sources/laptop/`)** — captured from `$HOME` by the bootstrap walker.
- Filter applied at capture time (see `~/.claude/skills/janus-brain/config/exclude-*`).
- Treat as low-signal by default — most laptop files are workaday docs.
- Auto-classify importance: bias to `medium` unless markers say otherwise.
- Likely outputs: 0-1 entity update per file, occasional decision/lesson extraction from notes.

**Meetings (`sources/meetings/`)** — Fireflies transcripts via per-user API key.
- **Use raw transcript.** Ignore Fireflies' summary.
- **Skip recurring 1:1s and team standups by default.** `/standup` skill handles standups separately.
- **Manual override:** if {{PERSON}} flags a transcript as `force-ingest`, process normally.
- Audience defaults to **the union of all attendees' departments** (cross-dept meeting → all those depts).
- Likely outputs: 1-3 decisions, 0-2 lessons, vendor entity updates, project hub updates.
- Extract action items as candidates for Linear/Monday — flag in log, do not create tickets from wiki ingest.

**Articles, Linear, Notion, Slack, Monday** — same rules as AIO CLAUDE.md §5.1.

### 5.2 Query

Standard AIO query flow: read `index.md`, identify candidate pages by category/slug, synthesise, offer to file back.

### 5.3 Lint

Trigger: automatic at 10 ingests since last lint, or on-demand. Same checks as AIO §5.3 (contradictions, stale claims, orphans, missing pages, broken refs, frontmatter compliance, question aging, unresolved escalations).

### 5.4 Index update

`index.md` updated on every create/rename/merge/delete during ingest. Format per AIO §5.4.

### 5.5 Federate (NEW — personal-tier specific)

After ingest, the federation pass pushes sanitised wiki pages up to the relevant department Prime Radiant(s).

**For each wiki page with frontmatter:**

1. Compute target instances from `audience` + `departments:`:
   - `audience: personal` → nowhere (stays here)
   - `audience: department` → for each slug in `departments:`, push to `<Drive>/Janus <Dept>/Prime Radiant — <Dept>/inbox/`
   - `audience: departments:a,b` → push to instances `a` and `b` only
   - `audience: org` → push to every department instance + the Org instance
   - `audience: ceo-only` → push to CEO instance only

2. **Sanitisation before push:**
   - Strip absolute `source_path` frontmatter
   - Strip any field starting with `personal_`
   - Strip `audience: personal` notes entirely (they shouldn't reach this step)
   - Keep `captured_by` (liability anchor) — this is the chain-of-custody record

3. **Conflict policy:**
   - If the same slug exists in the target instance, drop the personal copy into `<target>/inbox/personal-<{{PERSON_SLUG}}>-<slug>.md` for the department curator's review (high-stakes per §5.1).
   - Never overwrite a department instance page from a personal push.

4. **Logging:**
   - Append one line to `log.md` per federation pass:
     ```
     ## [YYYY-MM-DD HH:MM] federate
     - pushed: <count> notes to <list of instances>
     - sanitised: <count> notes had fields stripped
     - conflicts: <list>
     ```

---

## 6. Tone and style

- **Terse and concrete.** Prose over bullets unless the content is genuinely a list.
- **Date claims.** "As of 2026-05-11, …"
- **Cite sources.** Reference source slugs in `sources:` and inline where load-bearing.
- **Cross-link liberally** with `[[wikilinks]]`. Use slug form.
- **In `related:` frontmatter, use plain slugs.** Never `[[wikilink]]` syntax inside YAML.
- **Hedge appropriately** with `confidence` frontmatter and inline hedges.
- **Don't paraphrase to fill space.** A 3-sentence vendor page is fine if 3 sentences is what's known.
- **Never quote sources at length.** Summarise. Brief quotes (under 15 words) only when wording matters.

For brief shape, follow AIO CLAUDE.md §6 — strategic-aha shape, not industry-summary shape.

---

## 7. Personal-tier specifics (deviations from AIO)

- This instance has a `sources/laptop/` subfolder the AIO instance doesn't have — captures bootstrap walker output.
- `entities/internal/{{PERSON_SLUG}}.md` is **this person's self-page**. The bootstrap maintains it as new context emerges.
- `audience:` frontmatter is **required** here (optional in AIO).
- `captured_by:` frontmatter is **required and never strippable** — chain-of-custody for federation.
- Federation flows **up only** (personal → department). Department instances do not push back to personal.

---

## 8. Things this rulebook does not yet cover

- Cross-departmental audience conflicts (e.g. a meeting with HR + Finance where Finance attendees want narrower distribution than HR attendees).
- Personal data retention policy when someone leaves Janus.
- Auto-detecting when a private note has been auto-classified incorrectly (false-negative privacy errors).
- Programmatic bidirectional sync if a department instance wants to push corrections back to personal.

File proposed edits as `questions/` pages and surface to Michael for cross-instance consistency.
