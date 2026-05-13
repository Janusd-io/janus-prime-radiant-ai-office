---
type: project
title: Janus Prime Radiant Build
slug: janus-prime-radiant-build
created: 2026-05-05
updated: 2026-05-13
departments: [ai-office]
status: active
owner: michael-bruck
sources: [jehad-vault-import-2026-05-13]
related: [llm-wiki, prime-radiant, michael-bruck, obsidian, linear, notion, janus-prime-radiant, prime-radiant-marketing-rollout, marketing-prime-radiant]
captured_by: jehad-altoutou
---

> _Jehad's personal-vault articulation of this topic, imported 2026-05-13. The canonical wiki page is at `projects/janus-prime-radiant-build.md` — this file is preserved as a source for divergent framing / additional context._

# Janus Prime Radiant Build

Program hub for rolling out **Janus Prime Radiant** instances across Janus departments toward a company-wide digital knowledge twin. Janus Prime Radiant is the system of LLM-maintained, domain-specific institutional knowledge bases implementing Karpathy's [[llm-wiki|LLM Wiki]] pattern.

> Dedupe note: closely related to the canonical stub [[janus-prime-radiant]]; this is the **program-level build** hub (multi-instance rollout) while janus-prime-radiant is the meeting-derived per-instance reference. The curator should reconcile or keep distinct as program vs concept.

## Origin

Authorised on 2026-05-05. The originating context: Notion search degrades as an AI-searchable KB at scale; the AIO chose Markdown + front-matter YAML + progressive exposure over RAG; Michael was tasked with prototyping the Karpathy LLM Wiki concept as the candidate pattern. Reinforced 2026-05-06 — Notion + MCP retrieval being too slow / expensive at scale.

## Scope

**Program scope:** Architect and roll out the Janus Prime Radiant pattern (LLM-maintained, durable, schema-driven knowledge bases) across Janus departments; define federation between instances; build toward a company-level digital knowledge twin visible to leadership.

**Instance status (as of 2026-05-08):**
- **AI Office** (this wiki): Live and in active development. Pattern validated 2026-05-07. CLAUDE.md v0.7 (v0.8 pending), 20 vendor pages, 9 concepts, 2 briefs, 3 processes, full ingest pipeline live.
- **Marketing** (with [[andrew-soane]]): Pilot kicking off per 2026-05-08 brainstorm. **Vault topology decided 2026-05-08**: separate Google Shared Drive folder + own `CLAUDE.md` derived from AIO. This is the **federation precedent**.
- **HR / Finance / IT/Ops / Office-of-CEO / Engineering / Training**: Queued for rollout in phases.

**Architecture (emerging, formalised in CLAUDE.md v0.8):**
- **Signals layer:** Raw inputs (Fireflies transcripts, Linear exports, Slack bookmarks, Monday snapshots, articles, PDFs).
- **Infrastructure layer:** Durable reference pages (Janus mission, ICP, long-term plans, approved vendor categories, policy frameworks).
- **Outputs layer:** Synthesis (briefs connecting external signals to department bets, quarterly plans, reporting decks, campaign briefs).

**Federation:** Instances cross-link via `entities/departments/` pages (new entity type in v0.8).

**Curation:** Primary Michael for the AIO instance; each domain instance has an owner.

## Nomenclature anchors (immutable by schema)

Per CLAUDE.md filing convention, certain slugs are immutable and cannot be renamed:

- **Concept page `concepts/llm-wiki.md`** — stays as-is.
- **Source page `sources/articles/karpathy-llm-wiki.md`** — stays as-is.
- **Decision page slugs containing "llm-wiki"** — stay as-is (date-stamped, immutable).

## Tracking

Going forward this project is tracked in Monday alongside other research-y work. Atomic updates (decisions, lessons) live in `decisions/` and `lessons/` and are linked back here.

## Related

[[llm-wiki]] (methodology) · [[andrej-karpathy]] (source) · [[obsidian]] (interface) · [[linear]] (system of record for AI Registry) · [[notion]] (system of record for ops/project docs)
