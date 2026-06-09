---
type: vendor
title: GBrain
slug: gbrain
created: 2026-05-23
updated: 2026-05-23
departments: [ai-office, engineering]
status: monitored
confidence: medium
sources: [2026-05-22-marktechpost-gbrain-tutorial, odt-competitive-analysis-2026]
related: [agent-memory, openclaw, anthropic, claude-code, mcp, janus-prime-radiant-build, observed-exposure-ai-labor-measure]
migrated_from: entities/vendors/gbrain.md
---
# GBrain

Open-source markdown-first agent memory layer built by **[[garry-tan|Garry Tan]]** (President and CEO of [Y Combinator](https://www.ycombinator.com/)). MIT licensed; repo at [github.com/garrytan/gbrain](https://github.com/garrytan/gbrain). Built to power Tan's own personal [[openclaw|OpenClaw]] and Hermes agent deployments. Surfaced to the AIO 2026-05-22 via MarkTechPost's hands-on tutorial — see [[2026-05-22-marktechpost-gbrain-tutorial]].

Pulse: [[2026-05-22-gbrain-yc-tan-memory-layer]] for the dated entry.

## What it is

A markdown-first, Postgres-backed knowledge layer that ingests meetings, emails, tweets, notes — then auto-wires a typed knowledge graph on top with **zero LLM calls** for the graph extraction. Hybrid retrieval: vector (HNSW on pgvector) + BM25 keyword (Postgres `tsvector`) + Reciprocal Rank Fusion + optional reranker (ZeroEntropy by default).

Architecture in one diagram (per the tutorial):

```
markdown files  ──>  PGLite + pgvector  <──>  43 skills
(your repo,           (hybrid retrieval +     (HOW to use the brain;
 source of truth)      typed graph)           RESOLVER.md routes intent)
       ▲                                              │
       └──────────────  agent reads/writes  ──────────┘
```

Key design elements:

- **Compiled truth + timeline page pattern.** Each page is one markdown file with a current best-understanding section at the top and an append-only evidence trail below. Strikingly close to the AIO's own [[janus-prime-radiant-build|Prime Radiant]] frontmatter+body discipline and `decisions/` / `lessons/` append-only convention.
- **PGLite (Postgres 17 compiled to WASM)** — embedded local Postgres, zero server config, ready in ~2 seconds. Supabase / self-hosted Postgres migration available when a brain outgrows local (~50K pages).
- **Self-wiring knowledge graph.** Regex inference cascade extracts typed edges from wikilinks: `FOUNDED → INVESTED → ADVISES → WORKS_AT → MENTIONS`. No LLM in the loop for graph extraction. Reports a +31.4 point P@5 lift over the same code with the graph layer disabled on the internal *BrainBench* benchmark.
- **MCP-native.** Exposes 74 tools via MCP/stdio (`get_page`, `put_page`, `search`, `query`, `add_link`, `get_backlinks`, etc.). One-command wire-up: `claude mcp add gbrain -- gbrain serve`.
- **Autopilot / Minions queue.** `gbrain doctor --remediate` computes dependency-ordered remediation plans; `gbrain autopilot --install` runs a 5-minute cron tick. Deterministic work (pull tweets, parse JSON) goes to Minions; judgment work goes to LLM sub-agents.
- **Thin harness, fat skills.** Explicitly stated design philosophy. The runtime stays small; intelligence lives in markdown skills the agent reads at decision time. Same operating thesis as Anthropic's [[agent-skills]] direction.

## Production-deployment scale ([[garry-tan|Garry Tan]]'s personal brain, v0.38.2.0)

| Metric | Value |
|---|---|
| Pages indexed | 146,646 |
| People tracked | 24,585 |
| Companies tracked | 5,339 |
| Autonomous cron jobs | 66 |
| BrainBench P@5 / R@5 | 49.1% / 97.9% |
| P@5 lift from graph layer | +31.4 pts |

The scale is significant. 146K pages and 24K people is materially larger than the AIO Prime Radiant (current scale ~450 wiki + 145 sources). This is *not* a prototype — it's the running brain of YC's CEO.

## Why this matters to Janus

GBrain is the closest external system to the [[janus-prime-radiant-build|Janus Prime Radiant]] pattern surfaced to date — closer than [[2026-05-12-mnemon-llm-supervised-memory|Mnemon]] or [[2026-05-13-magma-multi-graph-agentic-memory|MAGMA]] because it converges on the *same* design choices:

| Design dimension | Prime Radiant | GBrain | Convergence |
|---|---|---|---|
| Source of truth | markdown files | markdown files | yes |
| Linking discipline | `[[wikilinks]]` (slug form) | `[[wikilinks]]` (full slug path required) | yes — both reject the title-form heuristic |
| Knowledge graph | frontmatter + wikilinks + dated decision/lesson slugs encode entity/semantic/temporal/causal edges (CLAUDE.md §4) | typed regex extraction from wikilinks: FOUNDED → INVESTED → ADVISES → WORKS_AT → MENTIONS | yes — both are markdown-first multi-graph |
| Append-only state | dated `decisions/`, `lessons/`, `log.md`, `pulse/`; existing pages have updated/created timestamps | "compiled truth on top, append-only timeline below" per page | yes — same kaizen-on-state-hygiene pattern |
| Agent access | Cowork + Claude Code via filesystem | 74-tool MCP server (`gbrain serve`) | partial — Prime Radiant relies on whichever harness reads files; GBrain ships a dedicated MCP surface |
| Retrieval | filesystem grep + Obsidian wikilink resolution + LLM reasoning over read files | hybrid vector + BM25 + RRF + reranker | divergent — GBrain has dedicated retrieval infra; Prime Radiant relies on the agent doing the reasoning |
| Engine | git-backed file vault | PGLite + pgvector (file vault as input) | divergent — different storage substrate, same source-of-truth shape |

The *architectural family* is the same: markdown-first, multi-graph, file-canonical, MCP-accessible, agent-readable-and-writable. The *implementations* diverge — Prime Radiant is a file vault optimised for direct-LLM reading; GBrain layers retrieval-infrastructure on top of a similar file vault.

Strategic reads for AIO:

1. **Validation that the markdown-first / multi-graph / append-only pattern is the consensus shape**, not a Janus idiosyncrasy. Two independent surfacings (Mnemon and MAGMA in May 2026) converged on multi-graph; GBrain converges on markdown-first + multi-graph + compiled-truth-plus-timeline-per-page. Prime Radiant is on the consensus path, not an idiosyncratic one.
2. **The retrieval-infrastructure layer is the next architectural decision Prime Radiant will face.** As the AIO instance scales (currently ~450 pages; comparable scale to GBrain is ~30× larger) the filesystem-grep + LLM-reading model may degrade in latency / token-cost. GBrain's PGLite + pgvector + RRF stack is one credible answer. The [[prime-radiant-storage-substrate|substrate brief]] should add a "retrieval-layer-on-top-of-git-vault" watch-for.
3. **MCP server pattern as alternative to direct-filesystem-access.** GBrain ships a 74-tool MCP surface for agent reads/writes. Prime Radiant currently relies on the agent reading files directly. The MCP server pattern is more portable (any MCP client can integrate) but adds an indirection. Worth evaluating whether Prime Radiant should ship a thin MCP server wrapper when it scales beyond the curator-on-Obsidian use case.
4. **The "thin harness, fat skills" philosophy** is now articulated by both Anthropic ([[agent-skills]]) and GBrain. Convergent evidence that the [[knowledge-compilation|compiled-knowledge-as-skill-files]] pattern is the dominant architectural shape for the next agent generation.

## Janus posture

**Monitored, not adopted as of 2026-05-23.** The Prime Radiant pattern is working for the AIO instance and there's no immediate failure mode forcing adoption of GBrain's retrieval-infrastructure layer. Reasons to monitor closely:

- If multi-instance Prime Radiant federation hits search-latency or cross-vault-query problems, GBrain's PGLite + pgvector + RRF stack becomes a credible upgrade path.
- If Andrew (or future department-instance owners) need richer retrieval over their vault than file-grep, GBrain provides a working pattern.
- [[garry-tan|Garry Tan]]'s adoption signal: YC's CEO uses this in production. That's evidence the design is robust.

Reasons NOT to adopt yet:

- Adds PGLite/Postgres + Bun runtime + ZeroEntropy/embedding API + 81 migrations to a stack that currently has zero infrastructure overhead (git + Obsidian).
- The "thin harness, fat skills" benefit is already largely captured by the existing Prime Radiant + Claude Code skill-bundle pattern.
- 74-tool MCP surface is fat compared to Janus's `/standup`, `/ai-registry`, `/ai-tool-evaluation` skill set. Adoption would mean integrating a separate tool surface into the AIO skill layer.

**Stage path if adoption is considered:** Stage 1 triage in AIR (per [[ai-tool-evaluation-framework]]). Likely categorisation: AI Office Infrastructure tier (per [[tool-tiers]]) — internal-only, no client data, would replace or augment the existing file-vault retrieval layer. Gate 2.2 (SSO) and Gate 2.3 (vendor viability) are the gates worth pre-checking — Tan is the maintainer; vendor-viability depends on whether GBrain stays a personal project or becomes a YC-supported open-source layer.

## Cross-cutting context

- **The compiled-truth-plus-timeline-per-page pattern** is a precise sub-pattern within the broader markdown-first agent-memory family. Worth bookmarking — Prime Radiant uses this pattern at the *vault* level (the `log.md` for the wiki, the `decisions/` dated slugs, the `pulse/` timeline) but not strictly at the *per-page* level. GBrain enforces it per page. A future Prime Radiant convention pass could consider whether per-page timeline appendices would add value (vs the current pattern of dated body claims and explicit updated: frontmatter).
- **[[garry-tan|Garry Tan]] as an external surface.** Tan is YC's CEO; OpenClaw is the YC-derived OSS agent harness lineage Janus already tracks ([[openclaw]], [[nemoclaw]], [[nanoclaw]]). GBrain extends that lineage to memory infrastructure. The lineage signals YC is broadly committing to open-source agent infrastructure over closed-vendor lock-in — useful for [[ai-native-janus-positioning|Bonaventure's positioning]] when discussing the open-source-substrate angle.

## "Company Brain Confinement" structural issue (added 2026-06-09)

[[odt-competitive-analysis-2026]] identifies a fundamental architectural tension in deploying shared corporate GBrains: **the single-writer constraint**. Standard embedded databases (like PGLite) allow only one writer at a time. Running an automated sync operation requires locking the database and halting all active MCP servers. This is the Janus sandbox's git-lock problem at the database layer.

Scaling GBrain safely to multi-user, multi-agent writes requires:
- HTTP MCP server (vs stdio MCP, which is single-session)
- Dynamic Client Registration
- Scope-gated **OAuth 2.1** authentication to isolate user-level access

This is a meaningful architectural tax before GBrain becomes a genuine team-shared substrate (vs a personal or single-curator deployment). Worth factoring into any Janus adoption evaluation — the setup that works for Garry Tan's personal brain may not cleanly generalise to a 10-department Prime Radiant deployment without the HTTP + OAuth layer. The [[prime-radiant-storage-substrate|substrate brief]] should capture this as the "write-concurrency" design decision for the retrieval-infrastructure path.

## Watch for

- Whether YC adopts GBrain officially as part of the OpenClaw / YC AI Stack release surface (vs staying a Tan-personal project).
- LongMemEval benchmark scores (the public benchmark in the sibling `gbrain-evals` repo) once Tan or others publish them.
- Adoption by other YC portfolio companies — that would be a strong signal the pattern travels.
- Migration paths off PGLite — the documented Supabase migration is the obvious one; whether self-hosted Postgres (e.g., on Hostinger, consistent with [[hostinger|Janus's hosting posture]]) becomes a documented configuration.
- Whether GBrain's `gbrain capture` one-line + webhook ingestion endpoint becomes a standard surface other vendors clone.
- Comparison datapoints against [[2026-05-12-mnemon-llm-supervised-memory|Mnemon]] (LLM-supervised, files-as-memory) and Claude Code's "dreaming" feature ([[2026-05-21-code-with-claude-london]]) — three converging vendor implementations of the same multi-graph-markdown-first family.
