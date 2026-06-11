---
type: project
title: Janus Prime Radiant Build
slug: janus-prime-radiant-build
created: 2026-05-05
updated: 2026-06-11
departments: [ai-office]
status: active
owner: michael-bruck
sources: [karpathy-llm-wiki, aio-2026-05-05, aio-2026-05-06, 2026-05-11-aio-standup-with-jehad, 2026-05-12-bonaventure-ai-native-call, 2026-05-13-aio-it-meeting, 2026-05-13-aio-pm-meeting, 2026-05-14-pm-workflow-walkthrough-lysander, jehad-vault-janus-prime-radiant-build, 2026-05-18-ai-native-ceo, 2026-04-coordination-leverage-model-v0.3, janus-ai-software-engineer-jd-2026, haber-everything-is-recorded-now]
related: [llm-wiki, michael-bruck, jehad-altoutou, obsidian, linear, notion, 2026-05-05-kb-direction-markdown-progressive-exposure-not-rag, 2026-05-05-notion-degrades-as-ai-searchable-kb, peer-to-peer-mesh-federation-pattern, 2026-05-11-bonaventure-prime-radiant-shoutout, 2026-05-11-notion-restricted-to-aio-no-broad-rollout, 2026-05-11-internal-branding-prime-radiant-vs-nomi-vs-brain, ai-native-janus-positioning, 2026-05-12-html-as-presentation-format-adopted, project-management-digital-delivery-workflow, 2026-05-14-ai-bounded-role-in-project-management, 2026-05-14-project-management-document-management-gap, euclid-wong, joyce-woo, bonaventure-wong, 2026-05-18-ceo-global-kb-unified-market-ui, coordination-leverage-model, coordination-three-layer-model, organisational-digital-twin]
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

## Status (as of 2026-05-14)

**AIO instance sub-effort:**
- **Migration executed (2026-05-13).** AIO instance moved from the Google Shared Drive substrate to a private GitHub repo (`janus-prime-radiant-ai-office` under `Janusd-io`), cloned to `~/janus/prime-radiant/ai-office/` on the curator's machine. Obsidian Git plugin handles auto-pull/commit/push; Cowork sees real files on real disk (no streaming-mount placeholder layer). The substrate decision rationale lives in [[prime-radiant-storage-substrate]]; the curator-side runbook (with bash script) is at [[prime-radiant-instance-setup]]. Jehad's first round-trip is the validation test that gates extracting the per-member runbook.
- Folder scaffolding: done
- Schema doc (`CLAUDE.md`): **v0.11** (2026-05-14) — added Git-substrate documentation in §1 + git-awareness framing in §5. v0.10 (2026-05-13) formalised the multi-graph framing (entity/semantic/temporal/causal frontmatter edges per the agent-memory community vocabulary) + `decided_by` / `captured_by` fields. v0.8 added entities/departments/ entity type + federation rules. Prior versions (v0.4–v0.7) layered in the AIO-as-institutional-KB framing, the Janus Prime Radiant naming, the domain-generalisability rules, and the brief-shape discipline.
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
- **Two GitHub orgs, distinct purposes (clarified 2026-05-14).** AIO instance and the template repo live on **`Janusd-io`** (AI Office's internal-tooling org). All other department instances (Project Management, IT, Operations, ISO, HR, Finance, Office of CEO, Engineering, Training, Marketing) live on **`Janusd-com`** (Janus's main company org). The split keeps internal AIO experimentation isolated from company-operational vaults while still using the same Prime Radiant template + tooling. Marketing's existing vault should be migrated to `Janusd-com` if not already there.
- HR / Finance / IT-Ops / Office-of-CEO / Engineering / Training instances: queued for sequential rollout once the Marketing pilot proves the federation pattern (running in parallel with continued AIO honing — these are not blocked on AIO being "done"). IT-Ops first pilot scope clarified in the 2026-05-11 standup: [[euclid-wong|Euclid]]'s **project-management team** (the largest and most technically-savvy IT-Ops sub-team), kicking off at the Wednesday meeting. Separate from the IT sub-team itself. [[mariam-mahmood|Mariam]] (HR) deferred — good non-technical test case but not yet. [[simon-tarskih|Simon]] deferred — no clear use case yet.
- **Stakeholder signal:** [[bonaventure-wong|Bonaventure]] gave a positive shout-out on the company-wide knowledge-base work; impressed it's happening sooner than expected. See [[2026-05-11-bonaventure-prime-radiant-shoutout]]. Validates pacing.
- **Notion narrowing complement:** [[2026-05-11-notion-restricted-to-aio-no-broad-rollout|Bonaventure's no-broad-Notion-rollout decision]] validates the Prime Radiant pattern as the company-wide substitute substrate.
- **Internal branding open question:** multiple sub-names are in circulation for the user-facing surface (Prime Radiant, Nomi, brain, wiki, Pulse, PULS). See [[2026-05-11-internal-branding-prime-radiant-vs-nomi-vs-brain]] — consolidation conversation pending with [[andrew-soane|Andrew]]. The internal *system* name stays Janus Prime Radiant; what the user-facing surface gets called for non-technical audiences is open.
- **Commercial-asset framing locked (2026-05-12).** Per [[ai-native-janus-positioning]] — Bonaventure on the AI Native CEO call: *"this is eventually going to be part of our selling point."* Prime Radiant is no longer internal-tooling-only; it's the operational proof point under the [[ai-native-janus-positioning|three-pillar messaging spine]]. Externalisability, polish, and demo-readiness now matter for non-AIO audiences. Also captured a gamification idea from Bonaventure for onboarding ("Have you connected Fireflies? Have you tested this?") — feature direction for whichever skill owns user onboarding (currently `/janus-pulse`).
- **Employee-centric architecture framing reinforced (2026-05-12).** Bonaventure: *"everything is kind of connected to the user because that's how you're onboard yourself onto us... that unique identity that might be very valuable. And then whatever you connect through it, this could be the centre of everything."* User identity drives authority chart drives access boundaries drives ISO scope. Aligns with the [[peer-to-peer-mesh-federation-pattern]] design intent and the personal-vault-feeds-department-vault pattern.
- **Drive connector replaces path-based mounting for Cowork onboarding (2026-05-13).** Andrew's Cowork mounting failure root-caused to path-based workspace mounting unreliability; Google Drive MCP connector is the supported alternative. Two prerequisite Monday sub-items under Prime Radiant: (1) move Andrew's vault to his `.com` Drive (2912592151); (2) set up Drive connector in Cowork (2912593759). Sequencing: vault migration before connector. Per [[2026-05-13-aio-it-meeting]].
- **Vault-event ingest direction set (2026-05-13).** Kafka evaluated and rejected as event broker (<100 events/day; overkill). Drive webhooks API to be investigated as the right-sized replacement for cron-based ingest (Monday 2912592197). Adjacent research stream "Claude OS" (Hostinger-hosted vault files exposed via purpose-built APIs/MCPs; 2912590122) approved for exploration under Engage data architecture — depends on Drive webhooks research outcome.
- **Schema governance surfaces as a new requirements layer (2026-05-13).** Euclid's 5,000-document personal vault validates the Prime Radiant architecture at scale but surfaces schema drift as a real risk; schema linter + ISO 27001 evidence-chain cross-linking are now first-class requirements for both repos (Monday 2912631119, 2912592188). Folds into the `entities/departments/iso/` federation pattern.
- **Standup skill v3.15 in production (2026-05-13).** Step 5G now writes to the Drive vault inbox via MCP connector (not filesystem path). Today's standup file is the first v3.15 Step 5G output — feedback loop closed (skill output lands as wiki ingest input).
- **Notion deprecation target confirmed: end of May 2026 (2026-05-13).** Dual-write to vault inbox via Step 5G is the transition path. Hard date; subsequent decisions should plan around Notion being offline as a Janus surface from June.
- **PM Prime Radiant initialisation plan locked (2026-05-14).** [[project-management-digital-delivery-workflow|The full 28-phase PM digital delivery workflow]] is now captured as a process page, derived from Lysander Liu's ~60-minute walkthrough on 14 May. This is the **canonical content the PM instance is initialised against** — once PM enrolls (post-tooling-install), the workflow gives the instance a running start: schema, entity vocabulary, AI-bounded role, decision-trail discipline. The session also surfaced two structural insights captured as lessons: [[2026-05-14-ai-bounded-role-in-project-management|AI's bounded role (~30–60%, first-draft only)]] and [[2026-05-14-project-management-document-management-gap|document-management as an acknowledged ISO gap]]. Lysander and Spike Zhao pending entity-page creation via [[ingest-2026-05-14-lysander-liu-and-spike-zhao]]. [[euclid-wong|Euclid]] confirmed as PM Lead in addition to IT-Ops Head — wears both hats, simplifies federation.

## Status (as of 2026-05-18)

**CEO-level validation received.** On 18 May 2026, Jehad demo'd the Prime Radiant system to Bonaventure Wong and Joyce Woo ([[2026-05-18-ai-native-ceo]]). The demo included: entity nodes auto-sourced from Joyce's white paper, Obsidian graph view, and an HTML deck generated from the system with interim Janus brand CSS. Both received it positively. GitHub sync confirmed as the canonical vault backend at CEO level — Google Shared Drive ruled out definitively (streaming service incompatible with Claude Code's local-file requirement).

This demo prompted Bonaventure to articulate the long-arc architectural intent, now captured as a formal decision ([[2026-05-18-ceo-global-kb-unified-market-ui]]):

- **One unified global knowledge base** — market-specific UI layer on top; open access across departments.
- **Singapore two-layer model** — SG team has read access to the full global KB; local Singapore vault feeds back upward into the global KB.
- **Known constraint (deferred)** — Obsidian's single-repo limitation blocks full cross-department connectivity at scale. Federation redesign needed before this is fully operationalisable (see [[peer-to-peer-mesh-federation-pattern]]).

**Implications for program scope:**
- The [[janus-prime-radiant-build]] program is now explicitly scoped toward a company-wide unified KB, not just per-department instances. The CEO direction elevates the program's end-state from "department instances" to "company-level digital knowledge twin."
- The Singapore market rollout ([[joyce-woo|Joyce Woo]]) is the first practical test of the two-layer model. A separate Prime Radiant demo session for Joyce is queued (Monday 2917860605).
- Cross-department connectivity design and the UI layer become first-class engineering requirements alongside the federation redesign work.
- Andrew Prime Radiant initialisation (bulk Fireflies + Markdown doc import as primary seed) is near-term.
- **CLAUDE.md:** v0.11 (2026-05-14). Standup skill: v3.17.

## External validation — Prime Radiant as engineering identity (2026-06-10)

The [[janus-ai-software-engineer-jd-2026|AI Software Engineer JD]] (filed 2026-06-10) explicitly names the Prime Radiant memory system as a core engineering responsibility and a defining challenge of the Janus platform:

> *"Contribute to and evolve the memory and knowledge architecture at the core of the platform — a structured, multi-graph, file-based system underpinning institutional intelligence across the company. This is among the hardest and most consequential engineering problems on the platform."*

This is the first time the Prime Radiant architecture appears in an outbound Janus document. As of 2026-06-10, the system is no longer just an internal AIO project — it's part of Janus's engineering hiring identity and the public-facing description of what the AI Office builds. The JD also confirms multi-model orchestration (Claude + Gemini), MCP, and Claude Code as standard tooling expectations.

CLAUDE.md version at time of filing: v0.16.

## External validation — a16z names the pattern (2026-06-10)

David Haber (a16z) published "Everything is Recorded Now" (Jun 10, 2026) coining the "living context layer" — the new enterprise system of record built from voice/conversation rather than structured text. Per [[haber-everything-is-recorded-now]]:

> *"The model that's ingested two years of your company's internal discussion is simply a better assistant than the one that only read your documentation."*

This is an independent external arrival at the same thesis Janus Prime Radiant is executing. Haber names Bridgewater, OpenAI, and Granola as practitioners. The Prime Radiant is the same pattern at the institutional KB layer. The a16z framing also opens a product question: Haber calls this a "large enterprise opportunity with no obvious winner yet" — relevant to whether the Prime Radiant pattern becomes a Janus product offering or remains internal competitive advantage. See [[2026-06-10-haber-living-context-layer]].

## Nomenclature anchors (immutable by schema)

Per CLAUDE.md filing convention, certain slugs are immutable and cannot be renamed:

- **Concept page `concepts/llm-wiki.md`** — stays as-is. This page documents Karpathy's *methodology* of LLM-readable wikis. Janus Prime Radiant is one *implementation instance* of that concept; the concept page legitimately keeps its historical name.
- **Source page `sources/articles/karpathy-llm-wiki.md`** — stays as-is. Historical source slug immutable per ingest protocol.
- **Decision page slugs containing "llm-wiki"** (e.g., `decisions/2026-05-07-llm-wiki-extends-to-marketing-domain.md`) — stay as-is. Decision / lesson page slugs are date-stamped and immutable; the *system* they reference was renamed, not the historical record of *decisions about* that system.

## Tracking

Going forward this project will be tracked in Monday alongside other research-y work. Atomic updates (decisions, lessons) live in `decisions/` and `lessons/` and are linked back here.

## Related

[[llm-wiki]] (methodology) · [[andrej-karpathy]] (source) · [[obsidian]] (interface) · [[linear]] (system of record for AI Registry) · [[notion]] (system of record for ops/project docs)
