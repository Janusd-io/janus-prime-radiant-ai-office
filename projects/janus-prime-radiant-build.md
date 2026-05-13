---
type: project
title: Janus Prime Radiant Build
slug: janus-prime-radiant-build
created: 2026-05-05
updated: 2026-05-12
departments: [ai-office]
status: active
owner: michael
sources: [karpathy-llm-wiki, aio-2026-05-05, aio-2026-05-06, 2026-05-11-aio-standup-with-jehad, 2026-05-12-bonaventure-ai-native-call]
related: [llm-wiki, michael-bruck, jehad-altoutou, obsidian, linear, notion, 2026-05-05-kb-direction-markdown-progressive-exposure-not-rag, 2026-05-05-notion-degrades-as-ai-searchable-kb, peer-to-peer-mesh-federation-pattern, 2026-05-11-bonaventure-prime-radiant-shoutout, 2026-05-11-notion-restricted-to-aio-no-broad-rollout, 2026-05-11-internal-branding-prime-radiant-vs-nomi-vs-brain, ai-native-janus-positioning, 2026-05-12-html-as-presentation-format-adopted]
---

# Janus Prime Radiant Build

Program hub for rolling out **Janus Prime Radiant** instances across Janus departments toward a company-wide digital knowledge twin. Janus Prime Radiant is the system of LLM-maintained, domain-specific institutional knowledge bases implementing Karpathy's [[llm-wiki|LLM Wiki]] pattern. The first instance (**Janus Prime Radiant · AI Office**, this wiki) is live and in active development — the pattern has been validated, but the schema and conventions are still being honed (CLAUDE.md is on its 7th version in 4 days; v0.8 pending). The second instance (Marketing, with [[andrew-soane]] as stakeholder) is being kicked off now per the 2026-05-08 brainstorm session, in parallel with the AIO honing — not after it. HR, Finance, IT/Ops, Office-of-CEO, Engineering, and Training instances are queued for rollout in phases as departmental knowledge surfaces grow.

## Origin

This project was authorised on 2026-05-05 ([[aio-2026-05-05]]). The originating context: Notion search degrades as an AI-searchable KB at scale ([[2026-05-05-notion-degrades-as-ai-searchable-kb]]); the AIO chose Markdown + front-matter YAML + progressive exposure over RAG ([[2026-05-05-kb-direction-markdown-progressive-exposure-not-rag]]); Michael was tasked with prototyping the Karpathy LLM Wiki concept as the candidate pattern. The Monday tracking item is "Engage large-scale data architecture specialist" with sub-tasks for the wiki experiment and the broader KB architecture work. Reinforced 2026-05-06 ([[aio-2026-05-06]]) — Notion + MCP retrieval being too slow / expensive at scale was cited as further validation.

## Scope

**Program scope:** Architect and roll out the Janus Prime Radiant pattern (LLM-maintained, durable, schema-driven knowledge bases) across Janus departments; define federation between instances; build toward a company-level digital knowledge twin visible to leadership.

**Instance status:**
- **AI Office** (this wiki): Live and in active development. Pattern validated per 2026-05-07 lesson, but schema and conventions are still being honed. CLAUDE.md v0.7 (v0.8 pending), 20 vendor pages, 9 concepts, 2 briefs, 3 processes, full ingest pipeline live. Honing continues in parallel with the Marketing pilot — kicking off other instances does not freeze AIO development.
- **Marketing** (with [[andrew-soane]]): Pilot kicking off now per 2026-05-08 brainstorm. **Vault topology decided 2026-05-08** ([[2026-05-08-marketing-prime-radiant-as-separate-vault]]): separate Google Shared Drive folder + own `CLAUDE.md` derived from AIO. This is the **federation precedent** — every subsequent department instance follows the same shape. CLAUDE.md v0.8 is now landed; the Marketing CLAUDE.md will derive from it and may add domain-specific entity folders (outlets / campaigns / personas TBD). Pre-CRM architecture work proceeds immediately; CRM-dependent Signals integration follows when CRM selection lands.
- **HR / Finance / IT/Ops / Office-of-CEO / Engineering / Training**: Queued for rollout in phases as departmental knowledge surfaces grow and the Marketing pilot proves the federation pattern.

**Architecture (emerging, to be formalised in CLAUDE.md v0.8):**
- **Signals layer:** Raw inputs (Fireflies transcripts, Linear exports, Slack bookmarks, Monday snapshots, articles, PDFs).
- **Infrastructure layer:** Durable reference pages (Janus mission, ICP, long-term plans, approved vendor categories, policy frameworks).
- **Outputs layer:** Synthesis (briefs connecting external signals to department bets, quarterly plans, reporting decks, campaign briefs).

**Federation:** Instances cross-link via `entities/departments/` pages (new entity type in v0.8). This allows marketing and HR and finance to share signal across each other and feed the company-level knowledge twin without duplicating sources or schemas. The 11 May 2026 AIO standup sharpened the federation design into the [[peer-to-peer-mesh-federation-pattern]] — every department-to-department relationship gets its own shared `entities/departments/<other>/` subfolder visible to both vaults; meetings between the two departments land in that shared folder; both vaults' ingest passes process the content. Mesh, not hub-and-spoke, and not (initially) event-broker. The strategic rationale is cross-pollinisation (Pixar / Bell Labs / SRI precedents) — see the concept page for details.

**GitHub as the backbone:** Per the 11 May standup, [[github]] is now the confirmed substrate for vault sync — personal repos, department repos, and (eventually) company-level. The canonical template repo `janus-prime-radiant-template` ([github.com/Janusd-io/janus-prime-radiant-template](https://github.com/Janusd-io/janus-prime-radiant-template), at v0.9.0 as of 2026-05-12 — BOOTSTRAP Step 1 sequencing fix + ISO added to departments) is the seed for every new instance; the `/ims-enrolment` skill (owned by [[jehad-altoutou]]) and the `/janus-pulse` onboarding skill (owned by [[michael-bruck]]) both write into GitHub-backed personal/department repos. This is a program-level architectural decision, not just template-repo-specific.

**Curation:** Primary Michael for the AIO instance; each domain instance has an owner. Cross-instance signal sharing (e.g., AI tools discovered in the AIO wiki that matter to Marketing) is handled via federation pages and shared-source ingest flagging (mechanism deferred to v0.8).

## Status (as of 2026-05-08)

**AIO instance sub-effort:**
- Folder scaffolding: done
- Schema doc (`CLAUDE.md`): **v0.7** — §1 reframed to AIO-co-maintained institutional KB (v0.6, 2026-05-08); system named "Janus Prime Radiant" at title level (v0.7, 2026-05-08); domain generalisability + brief-shape rules baked in (v0.5, 2026-05-07); system-of-record map aligned with `/standup` v3.13 (v0.4, 2026-05-06). v0.8 pending — will formalise architecture layers, add entities/departments/ entity type, define federation cross-reference rules.
- Seed entity + concept pages: done — 20 vendor pages, 9 concept pages, 2 briefs, 3 process pages
- Inaugural source ingested: Karpathy gist
- Mivory backfill: 23 articles ingested
- Web Clipper for ongoing intake: working
- Notion ingest Phases 1–2: complete (operations notebook + 9 sub-pages + standups for 1, 4, 5, 6 May)
- Linear AIR Phase 4: complete (4 substantive sources ingested; vendor pages updated)
- Monday Automations Phase 5: complete (14 source files; 5 project hubs created from escalation)
- 7 May standup: ingested 2026-05-07
- **Pattern validated 2026-05-07 per [[2026-05-07-llm-wiki-validates-capture-everything|the lesson]]** — "all this knowledge came out of these meetings." Validation extended 2026-05-08 by [[andrew-soane]] brainstorm confirming cross-departmental appetite. Pattern is now solid enough to begin next-instance rollout (Marketing pilot starting 2026-05-08); AIO instance itself remains in active honing — schema, brief shape, ingest discipline all still evolving.
- Standup skill markdown-to-wiki integration: **deferred** per Michael — wiki should mature further before the integration surface is locked.
- Scheduled ingest jobs: deferred per Michael (manual cadence preferred until volume settles)

**Program-level sub-effort:**
- Marketing instance design: in flight; [[andrew-soane]] stakeholder confirmed as active test case (per 11 May standup); CLAUDE.md v0.8 derivation pending; Andrew's input/output sketch outstanding
- Federation architecture: v0.8 added `entities/departments/` entity type; 11 May standup sharpened the design into the [[peer-to-peer-mesh-federation-pattern|peer-to-peer mesh pattern]] (shared `entities/departments/<other>/` subfolders bidirectionally visible between paired vaults). CLAUDE.md amendment to promote the entity from file to folder is queued — deferred until the pattern is exercised concretely with Andrew (Marketing) and Euclid's project-management team (IT-Ops first pilot).
- **GitHub as backbone confirmed** (11 May standup) — personal repos, department repos, and company-level all sync through GitHub; the `janus-prime-radiant-template` repo ([github.com/Janusd-io/janus-prime-radiant-template](https://github.com/Janusd-io/janus-prime-radiant-template), v0.9.0 as of 2026-05-12) is the canonical seed. Template version tracks the AIO CLAUDE.md schema version — schema-bump → template-bump.
- HR / Finance / IT-Ops / Office-of-CEO / Engineering / Training instances: queued for sequential rollout once the Marketing pilot proves the federation pattern (running in parallel with continued AIO honing — these are not blocked on AIO being "done"). IT-Ops first pilot scope clarified in the 2026-05-11 standup: [[euclid-wong|Euclid]]'s **project-management team** (the largest and most technically-savvy IT-Ops sub-team), kicking off at the Wednesday meeting. Separate from the IT sub-team itself. [[mariam-mahmood|Mariam]] (HR) deferred — good non-technical test case but not yet. [[simon-tarskih|Simon]] deferred — no clear use case yet.
- **Stakeholder signal:** [[bonaventure-wong|Bonaventure]] gave a positive shout-out on the company-wide knowledge-base work; impressed it's happening sooner than expected. See [[2026-05-11-bonaventure-prime-radiant-shoutout]]. Validates pacing.
- **Notion narrowing complement:** [[2026-05-11-notion-restricted-to-aio-no-broad-rollout|Bonaventure's no-broad-Notion-rollout decision]] validates the Prime Radiant pattern as the company-wide substitute substrate.
- **Internal branding open question:** multiple sub-names are in circulation for the user-facing surface (Prime Radiant, Nomi, brain, wiki, Pulse, PULS). See [[2026-05-11-internal-branding-prime-radiant-vs-nomi-vs-brain]] — consolidation conversation pending with [[andrew-soane|Andrew]]. The internal *system* name stays Janus Prime Radiant; what the user-facing surface gets called for non-technical audiences is open.
- **Commercial-asset framing locked (2026-05-12).** Per [[ai-native-janus-positioning]] — Bonaventure on the AI Native CEO call: *"this is eventually going to be part of our selling point."* Prime Radiant is no longer internal-tooling-only; it's the operational proof point under the [[ai-native-janus-positioning|three-pillar messaging spine]]. Externalisability, polish, and demo-readiness now matter for non-AIO audiences. Also captured a gamification idea from Bonaventure for onboarding ("Have you connected Fireflies? Have you tested this?") — feature direction for whichever skill owns user onboarding (currently `/janus-pulse`).
- **Employee-centric architecture framing reinforced (2026-05-12).** Bonaventure: *"everything is kind of connected to the user because that's how you're onboard yourself onto us... that unique identity that might be very valuable. And then whatever you connect through it, this could be the centre of everything."* User identity drives authority chart drives access boundaries drives ISO scope. Aligns with the [[peer-to-peer-mesh-federation-pattern]] design intent and the personal-vault-feeds-department-vault pattern.

## Nomenclature anchors (immutable by schema)

Per CLAUDE.md filing convention, certain slugs are immutable and cannot be renamed:

- **Concept page `concepts/llm-wiki.md`** — stays as-is. This page documents Karpathy's *methodology* of LLM-readable wikis. Janus Prime Radiant is one *implementation instance* of that concept; the concept page legitimately keeps its historical name.
- **Source page `sources/articles/karpathy-llm-wiki.md`** — stays as-is. Historical source slug immutable per ingest protocol.
- **Decision page slugs containing "llm-wiki"** (e.g., `decisions/2026-05-07-llm-wiki-extends-to-marketing-domain.md`) — stay as-is. Decision / lesson page slugs are date-stamped and immutable; the *system* they reference was renamed, not the historical record of *decisions about* that system.

## Tracking

Going forward this project will be tracked in Monday alongside other research-y work. Atomic updates (decisions, lessons) live in `decisions/` and `lessons/` and are linked back here.

## Related

[[llm-wiki]] (methodology) · [[andrej-karpathy]] (source) · [[obsidian]] (interface) · [[linear]] (system of record for AI Registry) · [[notion]] (system of record for ops/project docs)
