---
type: concept
title: Prime Radiant
slug: prime-radiant
created: 2026-05-08
updated: 2026-06-08
departments: [ai-office]
confidence: high
sources: [2026-05-08-jehad-michael-bonaventure-meeting, prime-radiant-continual-learning-memory, karpathy-llm-wiki, magma-multi-graph-agentic-memory, mnemon-github-readme]
related: [llm-wiki, compounding-learning, agent-memory, prime-radiant-three-layer-architecture, janus-prime-radiant-build, prime-radiant-storage-substrate, per-instance-curator-role, retrieval-augmented-generation]
captured_by: claude
---

# Prime Radiant

The **Janus Prime Radiant** is the organisation's continual learning memory system: a compounding, multi-graph institutional knowledge base maintained by LLM against a strict schema (`CLAUDE.md`), version-controlled via git, and owned by Janus regardless of AI vendor. Named after Hari Seldon's living psychohistory instrument in Asimov's Foundation series — a contributed-to instrument that practitioners refine over time, not a black-box oracle queried for answers.

The central bet: **institutional memory compounds; inference capability commoditises.** Every organisation will have access to capable AI inference within the next 18–24 months. Not every organisation will have a decade of structured, cross-referenced institutional knowledge. The organisations that do will make better decisions and make fewer repeated mistakes.

## The problem it solves

### We wanted Mike Ross. We got Dory.

Organisations deploying AI for knowledge work imagined something like Mike Ross (the *Suits* character with eidetic memory — recall any statute, any case, any client conversation years after the fact). What they got was Dory: genuinely capable in the moment, but no thread connecting this session to the last one. Ask her tomorrow what you discussed today — she has no idea.

That is the default state of every commercial AI system. Every conversation starts cold. The intelligence produced in a session evaporates when it ends. The next session recomputes it from scratch.

This is tolerable for one-off queries. It is fatal for strategic knowledge work, where almost all value comes from accumulation: the second decision builds on the first, the tenth brief synthesises the previous nine, and institutional intelligence is precisely the web of connections between past choices, their outcomes, and the context that shaped them.

### Why existing systems don't solve it

Linear, Notion, Slack, Fireflies, Monday — the knowledge is there, but fragmented. These systems are authoritative for their own domains but not connected, not synthesised, and not queryable across the whole. An AI that can search each independently cannot answer "why did we make the decision we made in April?" because the answer requires pulling the meeting transcript, the Notion log, the Linear evaluation, and the Slack thread where it was contested. No single system holds the synthesis. The AI reconstructs it every time.

More fundamentally, these systems are not designed for AI-native access. They are human knowledge tools that AI can query, not AI-native structures that compound automatically as new information arrives.

## The multi-graph architecture

### Why not a vector database

The reflex response to "AI querying institutional knowledge" is a vector database (RAG pattern). Genuinely useful for document search. Insufficient for institutional memory.

Vector similarity captures one relationship type: semantic closeness. Institutional knowledge runs on four simultaneously:

| Relationship | What it captures | Example query |
|---|---|---|
| **Semantic** | Conceptual similarity | "What do we know about agent frameworks?" |
| **Entity** | Org graph — who, department, vendor | "Every decision Bonaventure has touched" |
| **Temporal** | Sequence, evolution, before/after | "What changed between April and May?" |
| **Causal** | What led to what — decisions, rationale, outcomes | "Why did we reject that vendor?" |

"Why did we reject a vendor?" requires traversing the causal graph: evaluation decision → meeting where it was discussed → principle it violated → prior lesson that motivated the principle. Semantic similarity doesn't surface that chain — graph traversal does.

### The May 2026 research convergence

In May 2026, two independent research groups published the same insight within 48 hours: [[mnemon-github-readme|Mnemon]] proposed a four-graph knowledge store with exactly these four dimensions; [[magma-multi-graph-agentic-memory|MAGMA]] independently proposed the same decomposition and validated it experimentally, substantially outperforming vector-similarity approaches on complex multi-hop queries. When two groups arriving from different premises converge on the same architecture in the same week, it suggests the decomposition reflects something true about the structure of knowledge.

What the Prime Radiant had already implemented — before either paper was published — was a primitive version of this same four-graph structure, encoded in the wiki's frontmatter schema. The `departments:` field encodes entity edges. `related:` encodes semantic edges. Date-prefixed filenames and `created`/`updated` fields encode temporal edges. `sources:` pointing from decisions to their motivating evidence encodes causal edges. The research literature validated the design in retrospect.

## Why the wiki construct

### The candidate approaches compared

| Approach | What it gets right | The fatal limitation |
|---|---|---|
| Fine-tuning | Knowledge in weights, fast retrieval | Expensive to update; opaque; vendor-locked; one training run per knowledge update |
| Pure context injection | No infrastructure overhead | Volatile (session-scoped); finite; noisy at scale |
| Structured database | Queryable, durable | Not human-readable; engineering overhead; schema migrations |
| RAG / vector store | Semantic search at scale | Single relationship type; inadequate for entity/temporal/causal queries |
| **Wiki (chosen)** | Human+machine readable; updatable; multi-graph; portable; zero operational overhead | Maintenance burden — solved by LLM |

### The research case for in-context learning

The fine-tuning comparison reflects operational arguments. Research grounds them. The core finding, established since Brown et al.'s 2020 GPT-3 work: **in-context learning** — providing structured knowledge in the prompt at inference time — is competitive with fine-tuning for knowledge retrieval and outperforms it on dimensions that matter most:

- **Updatability.** In-context knowledge changes by editing a file. In-weights knowledge requires a new training run. For knowledge that evolves weekly, this is not marginal — it is the difference between a living record and a degrading snapshot.
- **Inspectability.** Context is readable by anyone; weights are opaque. You cannot audit what a fine-tuned model "knows" or identify where it is wrong.
- **Precision over volume.** Well-structured, curated context outperforms large-volume raw injection. Quality and organisation matter more than quantity — exactly the problem the wiki solves.
- **Vendor independence.** In-context knowledge travels across model generations unchanged. Fine-tuned weights are locked to the model they were trained on.

The wiki solves the remaining challenge — scale — by injecting only the relevant subset on each query. The multi-graph frontmatter makes targeted retrieval possible: a query about Singapore filters by `countries: [sg]`; a query about a vendor pulls the entity page and linked decisions. Context stays signal-dense regardless of vault size.

### Why flat files of markdown

- **Simultaneously human-readable and machine-queryable.** A human opens it in any text editor; an AI greps and manipulates via standard file operations. No translation layer, no API dependency.
- **Portable across vendor cycles.** If Janus moves from Claude to any other AI, the knowledge base is unchanged.
- **Zero operational overhead.** No database to maintain, no search index to rebuild, no schema migrations.
- **Git provides the audit trail.** Every change is tracked, every write attributable. Decision filed in April + meeting from May that modified it + brief from June that synthesised it — all in the same version history, connected by commit messages and cross-references. Git log is the causal graph substrate.

### Why LLM-maintained

The personal wiki tradition going back to Vannevar Bush's 1945 Memex failed consistently for the same reason: maintenance burden. By 50 pages, the average person has stopped maintaining it. By 200 pages, cross-references are stale.

The LLM solves this. Every ingest: source arrives in inbox → LLM reads it → identifies affected pages → updates them → creates new pages → adds cross-references → logs → updates index. What would take a knowledge worker 30 minutes takes the LLM two minutes of automated processing, never getting behind, never forgetting to update cross-references, applying the same standards on the thousandth ingest as on the first.

### The CLAUDE.md schema — the operating contract

The LLM's maintenance is disciplined by `CLAUDE.md`, which is not documentation — it is an operating contract governing every write. Without it, a thousand ingested articles produce a thousand pages with idiosyncratic structure, broken cross-references, and contradictory claims. With it, the same thousand articles produce a coherent knowledge graph where any LLM or human can navigate from any entry point to any other relevant page.

The schema evolves: v0.10 added explicit multi-graph framing; v0.11 documented the GitHub substrate; v0.12 added attribution discipline after discovering Fireflies systematically misattributes speech from shared microphones; v0.14 codified the curation workflow and carry-forward lint convention; v0.15 formalised the per-instance curator role. The schema is the accumulated lesson of operating the system.

## The compounding effect

A wiki with 50 pages and a wiki with 500 pages are not the same system at different sizes. The 500-page wiki has connections the 50-page wiki cannot — because many connections only become visible when enough pages exist to be connected. A brief synthesising three vendor evaluations, two strategic decisions, and one competitor signal requires all five inputs to exist before synthesis is possible. Compounding is not linear; it is network-valued.

Three specific mechanisms are built into the design:

1. **Cross-reference compounding.** Every ingest not only adds a page but updates existing pages with new cross-references. A new competitor signal may simultaneously update the vendor evaluation, the concept page, the project hub, and the current quarter's brief — those cross-references make subsequent queries faster and more complete.

2. **Query-back compounding.** Every time the wiki answers a question, the answer can be filed back as a new brief. The wiki's own output becomes input to future reasoning.

3. **Lint compounding.** Periodic health checks surface contradictions, stale claims, orphan pages, and open questions that have accumulated enough evidence to resolve. Each lint pass tightens the graph. The wiki becomes more accurate over time, not less.

See [[compounding-learning]] for the general concept; the Prime Radiant is the institutional instantiation.

## Architecture and federation

See [[prime-radiant-three-layer-architecture]] for the full Signals → Infrastructure → Outputs model. The build sequence is fixed: Signals first, Infrastructure second, Outputs emerge.

The Janus Prime Radiant is not an AI Office tool — it is a pattern for the whole organisation. The AIO instance is the first. Marketing is in progress. HR, Finance, IT/Ops, Office-of-CEO, Engineering, Training, and ISO are queued. Cross-instance federation happens at the Outputs ↔ Signals boundary: an AIO brief on a regulatory shift becomes a Signal in the Marketing instance; a Marketing brief on a brand moment becomes a Signal in AIO when AI tooling is implicated. The long-term vision is a Janus digital knowledge twin — federated, leadership-visible institutional memory across every department, with the same four-graph structure operating at organisational scale that MAGMA and Mnemon validate at the agent-runtime level.

## Why now (as of 2026)

Three conditions converged in early 2026:

1. **LLM capability crossed a threshold.** Prior to approximately 2025, LLMs could not maintain a structured wiki with the consistency required for it to be more useful than a human-maintained one — applying naming conventions correctly, updating cross-references without errors, preserving attribution, distinguishing low-stakes from high-stakes operations.

2. **File-based memory became industry-validated.** Anthropic's April 2026 launch of file-based agent memory, combined with the MAGMA and Mnemon research in May, validated that the multi-graph, file-based, user-owned approach is architecturally correct — not a pragmatic compromise but the right shape.

3. **The cost of waiting is compounding.** A knowledge base built today will be more useful in six months than one started in six months, by a non-linear margin. Decisions made now and the context that motivated them will not be reconstructable later from systems-of-record alone. Institutional memory that isn't captured is permanently lost.

## Naming

Named after Hari Seldon's living psychohistory instrument in *Foundation* — deliberately over Asimov's other metaphors. The Multivac / Galactic AC lineage are *computational oracles*: black-box mainframes you query for answers. The Prime Radiant is a *contributed-to instrument*: Speakers each refine the equations over time. The wiki is the same shape — practitioners contribute signals, the LLM synthesises knowledge, and the system accumulates organisational intelligence. See [[llm-wiki]] for the full naming rationale.

Per-instance naming: one Prime Radiant, many domain facets — *Janus Prime Radiant · AI Office* (this instance), *· Marketing*, *· HR*, etc.
