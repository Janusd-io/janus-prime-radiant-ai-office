---
title: "A Step-by-Step Coding Tutorial to Implement GBrain: The Self-Wiring Memory Layer Built by Y Combinator's Garry Tan for AI Agents"
source: "https://www.marktechpost.com/2026/05/22/a-step-by-step-coding-tutorial-to-implement-gbrain-the-self-wiring-memory-layer-built-by-y-combinators-garry-tan-for-ai-agents/"
author:
  - "[[Asif Razzaq]]"
published: 2026-05-22
created: 2026-05-23
description: "A Step-by-Step Coding Tutorial to Implement GBrain: The Self-Wiring Memory Layer Built by Y Combinator's Garry Tan for AI Agents"
tags:
  - "clippings"
---
Your AI agent is smart but forgetful. Every new session starts from zero — no memory of who you met, what you read, what you decided last Tuesday. **[GBrain](https://github.com/garrytan/gbrain)** is an open-source fix for that. Built by Garry Tan (President and CEO of Y Combinator) to power his own OpenClaw and Hermes deployments, it’s a markdown-first, Postgres-backed knowledge layer that ingests meetings, emails, tweets, and notes, then auto-wires a typed knowledge graph on top — with zero LLM calls for the graph extraction. The production brain behind Garry’s actual agents currently holds **146,646 pages, 24,585 people, 5,339 companies, and 66 autonomous cron jobs**. On its own benchmark (BrainBench, a 240-page rich-prose corpus), GBrain hits **P@5 49.1% and R@5 97.9%**, a +31.4-point P@5 lead over the same codebase with the graph layer disabled.

This is a hands-on tutorial. You’ll install GBrain locally, import a small notes folder, run a real search, watch the knowledge graph wire itself, and connect it to Claude Code via MCP. About 20 minutes start to finish. All terminal outputs below were captured from a live install of **GBrain v0.38.2.0**. The repository (MIT-licensed) lives at [github.com/garrytan/gbrain](https://github.com/garrytan/gbrain).

[Join 150k+ members of our ML Subreddit Community..](https://www.reddit.com/r/machinelearningnews/)

## What you’re building

By the end of the tutorial, you’ll have:

<iframe src="https://subscribe-forms.beehiiv.com/v3/forms/10d6e3ed-a6a3-4bad-aae3-269120a6be50?utm_source=app.mivory.app&amp;utm_medium=referral&amp;referrer=https%253A%252F%252Fwww.marktechpost.com%252F2026%252F05%252F22%252Fa-step-by-step-coding-tutorial-to-implement-gbrain-the-self-wiring-memory-layer-built-by-y-combinators-garry-tan-for-ai-agents%252F" frameborder="0"></iframe>
- A local `~/.gbrain/brain.pglite` database — embedded **Postgres 17 (via WASM)** with pgvector, zero server config.
- A small “brain repo” of markdown notes about people, companies, and concepts.
- A working hybrid-search CLI that combines vector + BM25 keyword + Reciprocal Rank Fusion (RRF), with a ZeroEntropy reranker on top by default.
- A typed knowledge graph (`works_at`, `founded`, `invested_in`, `attended`, `advises`, `mentions`) auto-extracted from your notes.
- An MCP server exposing **74 tools** so Claude Code, Cursor, and Windsurf can read and write to the brain directly.

## Prerequisites

- macOS or Linux (Windows users: use WSL2).
- A code editor.
- Bun ≥ 1.3.10 (the runtime GBrain ships on; the repo’s `package.json` declares this as the minimum engine). We’ll install it in Step 1.
- An embedding API key from **one** of: ZeroEntropy (default), OpenAI, or Voyage. Without one, you can still install and run keyword search, but `gbrain query` (hybrid + vector) will return no results.
- Optional: an Anthropic API key for multi-query expansion during search.

## Step 1 — Install Bun and GBrain

GBrain is written in TypeScript and runs on Bun. Install it first:

```php
curl -fsSL https://bun.sh/install | bash
exec $SHELL                 # reload shell so \`bun\` is on PATH
bun --version
```

Now install GBrain. As of v0.38, the canonical install path is a single global Bun install:

```php
bun install -g github:garrytan/gbrain
gbrain --version
# gbrain 0.38.2.0
```

## Step 2 — Initialize your brain

`gbrain init --pglite` provisions a local PGLite database in `~/.gbrain/`. PGLite is full Postgres compiled to WASM — no server, no Docker, ready in roughly two seconds.

For this tutorial we’ll defer the embedding provider so you can follow along without an API key right away — we’ll wire it up in Step 6 when we run hybrid search:

```php
gbrain init --pglite --no-embedding
```

(If you’d rather configure embeddings now, set one of `OPENAI_API_KEY`, `ZEROENTROPY_API_KEY`, or `VOYAGE_API_KEY` in your environment before running plain `gbrain init --pglite`.)

Real output captured from a fresh install (truncated for brevity — there are 81 migrations from schema v1 → v85):

```php
Setting up local brain with PGLite (no server needed)...
  Schema version 1 → 85 (81 migration(s) pending)
  [2] slugify_existing_pages...
  [2] ✓ slugify_existing_pages
  [3] unique_chunk_index...
  [3] ✓ unique_chunk_index
  ...
  Brain ready at /home/you/.gbrain/brain.pglite
  0 pages. Engine: PGLite (local Postgres).
```

You now have an empty brain. Confirm:

```php
gbrain stats
# Pages:     0
# Chunks:    0
# Embedded:  0
# Links:     0
# Tags:      0
# Timeline:  0
```

## Step 3 — Create a tiny brain repo

The brain repo is just a directory of markdown files. Each file follows GBrain’s **compiled truth + timeline** pattern: a current best-understanding section on top, an append-only evidence trail below.

**Important:** wikilinks must use the full slug path (e.g., `[[people/alice-chen]]`, not just `[[alice-chen]]`) for the graph extractor to resolve them. This is a real gotcha — I tested both forms; the short form silently produces zero links.

```php
mkdir -p ~/my-brain/people ~/my-brain/companies ~/my-brain/concepts
cd ~/my-brain
```

Create a person page:

```php
cat > people/alice-chen.md <<'EOF'
---
type: person
title: Alice Chen
tags: [founder, ai-infra]
---

Founder and CEO of [[companies/acme-ai]]. Previously staff engineer at
Google Brain. Focus area: inference optimization for small language models.

---

- 2024-03-12: Met at AI Engineer Summit. Discussed sparse MoE routing.
- 2024-09-04: Announced $12M seed led by Sequoia.
- 2025-01-18: Shipped open-source inference router on GitHub.
EOF
```

A company page:

```php
cat > companies/acme-ai.md <<'EOF'
---
type: company
title: Acme AI
tags: [startup, inference]
---

YC W24 inference-optimization startup. Founded by [[people/alice-chen]].
Building latency-aware routing for sub-7B models.

---

- 2024-09-04: $12M seed, led by Sequoia.
- 2025-01-18: Open-sourced their inference router.
EOF
```

And a concept page:

```php
cat > concepts/inference-optimization.md <<'EOF'
---
type: concept
title: Inference Optimization
tags: [ml-systems]
---

Techniques to reduce latency and cost when serving language models:
quantization, speculative decoding, KV-cache reuse, and request batching.
EOF
```

## Step 4 — Import the repo

`gbrain import` is idempotent (content-hash deduplicated). We’ll pass `--no-embed` so this step is deterministic for readers who don’t have an embedding key set yet — embeddings get backfilled in Step 6. Real output:

```php
gbrain import ~/my-brain/ --no-embed
```

```php
[gbrain phase] import.collect_files start dir=/home/you/my-brain/ strategy=markdown
[gbrain phase] import.collect_files done 2ms files=3
Found 3 markdown files
[import.files] 3/3 (100%) imported=3 skipped=0 errors=0

Import complete (0.3s):
  3 pages imported
  0 pages skipped (0 unchanged, 0 errors)
  3 chunks created
```

Confirm:

```php
gbrain list
# companies/acme-ai           company   2026-05-22  Acme AI
# concepts/inference-optimization  concept  2026-05-22  Inference Optimization
# people/alice-chen           person    2026-05-22  Alice Chen
```

## Step 5 — Wire the knowledge graph

For a first-time import, run the link extractor explicitly to backfill the graph from your wikilinks. This is pure regex + typed inference — **zero LLM calls**.

```php
gbrain extract links --source db
```

Real output:

```php
[extract.links_db] 3/3 (100%) done
Links: created 2 from 3 pages (db source)
Done: 2 links, 0 timeline entries from 3 pages
```

Two typed edges were inferred from the wikilinks: `alice-chen --works_at--> acme-ai` (from “Founder and CEO of …”) and `acme-ai --founded--> alice-chen` (from “Founded by …”). The inference cascade fires in order: `FOUNDED → INVESTED → ADVISES → WORKS_AT → MENTIONS`. No model in the loop.

Inspect the graph directly:

```php
gbrain graph-query people/alice-chen --depth 1
# [depth 0] people/alice-chen
#   --works_at-> companies/acme-ai (depth 1)
```

```php
gbrain backlinks companies/acme-ai
# [
#   {
#     "from_slug": "people/alice-chen",
#     "to_slug": "companies/acme-ai",
#     "link_type": "works_at",
#     "context": "Founder and CEO of [[companies/acme-ai]]...",
#     "link_source": "markdown",
#     ...
#   }
# ]
```

This is the difference between vector search and structured retrieval. “Who works at Acme AI?” is now a one-hop typed-edge traversal, not a similarity score. That structural channel is what drives the +31.4-point P@5 lift over the graph-disabled variant on BrainBench.

## Step 6 — Run a search

GBrain ships two search verbs. `gbrain search` is keyword-only (BM25 on Postgres `tsvector`) and works without embeddings:

```php
gbrain search "inference"
# [0.3648] companies/acme-ai -- YC W24 inference-optimization startup...
# [0.3648] people/alice-chen -- Founder and CEO of [[companies/acme-ai]]...
```

`gbrain query` is the full hybrid pipeline: vector (HNSW on pgvector) + BM25 + Reciprocal Rank Fusion + optional multi-query expansion (Anthropic Haiku) + an optional ZeroEntropy reranker. It needs embeddings, which we deferred in Step 2 — wire them up now:

```php
# Set one of: ZEROENTROPY_API_KEY (default), OPENAI_API_KEY, or VOYAGE_API_KEY
export OPENAI_API_KEY=sk-...
gbrain config set embedding_model openai:text-embedding-3-large
gbrain embed --all          # one-time backfill against your embedding provider
gbrain query "who works on small-model inference?"
```

```php
# Set one of: ZEROENTROPY_API_KEY (default), OPENAI_API_KEY, or VOYAGE_API_KEY
export OPENAI_API_KEY=sk-...
gbrain config set embedding_model openai:text-embedding-3-large
gbrain embed --all          # one-time backfill against your embedding provider
gbrain query "who works on small-model inference?"
```

Three search modes ship out of the box — `conservative`, `balanced`, `tokenmax` — bundling the cost/quality knobs into one config key. Default is `balanced` with the ZeroEntropy reranker on. RRF formula: `score = sum(1 / (60 + rank))`.

## Step 7 — Connect to Claude Code via MCP

The brain is more useful when an AI agent can read and write to it directly. GBrain exposes **74 tools** over the Model Context Protocol via stdio. The canonical setup is one command (not a hand-edited JSON file):

```php
claude mcp add gbrain -- gbrain serve
```

Verify the install:

```php
claude mcp list
# gbrain  stdio  gbrain serve
```

Now ask Claude Code something like *“search the brain for inference optimization”* and it’ll route through the `search` tool and return your indexed results. The actual MCP tool names are plain snake\_case: `get_page`, `put_page`, `delete_page`, `list_pages`, `search`, `query`, `add_link`, `get_backlinks`, `add_tag`, and 65 more.

**Cursor and Windsurf** use the standard MCP JSON config in their respective settings UIs. The server spec is the same:

```php
{
  "mcpServers": {
    "gbrain": { "command": "gbrain", "args": ["serve"] }
  }
}
```

**Claude Desktop** uses `claude_desktop_config.json` for *local stdio* MCP servers with the same JSON spec. *Remote* HTTP MCP servers must be added through Settings → Integrations with a bearer token. See `docs/mcp/CLAUDE_DESKTOP.md` in the repo for the GUI walkthrough.

If you want remote access from any machine, swap stdio for HTTP:

```php
gbrain serve --http --port 8787
# Bearer auth, default-deny CORS, two-bucket rate limit, per-request audit log.
# Postgres-only by design (PGLite is local-only).
```

## Step 8 — Let the brain run itself

GBrain ships an autopilot loop. As of v0.36.4, one command computes a dependency-ordered remediation plan, submits each step as a Minion job, re-checks the brain’s health score between steps, and refuses to spend past your cost cap:

```php
gbrain doctor --remediate --yes --target-score 90 --max-usd 5
```

Or run it as a daemon:

```php
gbrain autopilot --install        # cron-driven, 5-minute tick
```

Healthy brains sleep for 60 minutes between ticks. Unhealthy ones get the full overnight cycle: sync, extract, embed, consolidate, synthesize. Three phases (`synthesize`, `patterns`, `consolidate`) are protected so an MCP-connected agent can’t silently burn API credits.

For ad-hoc background work, the **Minions** queue takes shell jobs and LLM subagent jobs side by side:

```php
gbrain jobs submit sync --params '{}' --follow
gbrain jobs stats
gbrain jobs work --queue default
```

**One PGLite caveat:** `gbrain jobs supervisor` (the auto-restarting worker daemon) is **Postgres-only**. PGLite’s exclusive file lock blocks the separate worker process — the CLI rejects with a clear error if `config.engine === 'pglite'`. If you’re on PGLite, stick with inline `--follow` jobs for the tutorial, or run `gbrain migrate --to supabase` before standing up a persistent worker.

Routing rule: deterministic work (pull tweets, parse JSON, write a page) goes to Minions; judgment work (triage an inbox, assess priority) goes to LLM sub-agents.

## What just happened, in one diagram

```php
markdown files  ──>  PGLite + pgvector  <──>  43 skills
(your repo,           (hybrid retrieval +     (HOW to use the brain;
 source of truth)      typed graph)           RESOLVER.md routes intent)
       ▲                                              │
       └──────────────  agent reads/writes  ──────────┘
```

The markdown repo is the system of record. GBrain is the retrieval + graph layer over it. The agent reads and writes through both, and humans can always open any `.md` file and edit it directly — `gbrain sync` picks up the change.

## Where to go next

- **One-line capture** (new in v0.38): `gbrain capture "the thought I want to remember"` lands directly in `inbox/YYYY-MM-DD-<hash>`. Also accepts `--file`, `--stdin`, and webhook ingestion via `gbrain serve --http /ingest`.
- **Migrate to Supabase** when your brain outgrows local (PGLite is good up to ~50K pages): `gbrain migrate --to supabase`.
- **Ingest real data** with one of the recipes: voice (Twilio + OpenAI Realtime), email + calendar, 16 embedding providers, credential gateway.
- **Run the benchmarks** in the sibling repo [gbrain-evals](https://github.com/garrytan/gbrain-evals): BrainBench (synthetic) and `gbrain eval longmemeval` (the public LongMemEval benchmark).
- **Author your own skills.** A skill is a fat markdown file that encodes a workflow — triggers, checks, quality gate. `gbrain check-resolvable` validates the skill tree for reachability / MECE / DRY.

The deeper bet behind GBrain is that **thin harness, fat skills** beats thin skills behind a fat agent. The runtime stays small; the intelligence lives in markdown files the agent reads at decision time. Each commit you make to your brain repo is permanent context your agent inherits the next time it wakes up. The longer you run it, the smarter it gets.

## Marktechpost’s Visual Explainer

Step-by-Step Tutorial

## Implementing GBrain: The Self-Wiring Memory Layer for AI Agents

A hands-on walkthrough of **Garry Tan’s open-source agent brain**: install, import, hybrid search, graph wiring, and MCP integration in ~20 minutes.

v0.38.2Latest release

43Skills shipped

98%TypeScript

MITLicense

The Problem

## AI Agents Are Smart But Forgetful

Every session starts from zero. No memory of who you met, what you read, or what you decided last week.

- **Vector DBs alone miss exact phrases and structural questions**
- **Keyword search alone misses conceptual matches**
- **Most memory layers can’t answer “who works at X?”**
- **Sub-agents are slow and expensive for deterministic work**

What Is GBrain

## The Brain Powering Y Combinator’s CEO

Production stats from Garry Tan’s personal OpenClaw/Hermes deployment, current as of v0.38.2.0.

146,646Pages indexed

24,585People tracked

5,339Companies

66Cron jobs

Hybrid search on BrainBench: **P@5 49.1%, R@5 97.9%** — a +31.4-point P@5 lead over the same code with the graph layer disabled.

## Install Bun, Then GBrain

As of v0.38, the canonical install is **a single global Bun install**.

```
# Install Bun
curl -fsSL https://bun.sh/install | bash
exec $SHELL

# Install GBrain
bun install -g github:garrytan/gbrain

gbrain --version
gbrain 0.38.2.0
```

## Create a Local Brain in Two Seconds

**PGLite** is full Postgres 17 compiled to WASM. No Docker, no server.

```
# Defer embedding setup until search step
gbrain init --pglite --no-embedding
Setting up local brain with PGLite...
  Schema version 1 → 85 (81 migration(s) pending)
  [2] slugify_existing_pages... ✓
  [3] unique_chunk_index...     ✓
  ...
Brain ready at ~/.gbrain/brain.pglite
0 pages. Engine: PGLite.
```

## Compiled Truth + Timeline Pattern

Every page is one markdown file. **Wikilinks need full slug paths** — `[[people/alice-chen]]`, not `[[alice-chen]]`.

```
--- people/alice-chen.md ---
type: person
title: Alice Chen
tags: [founder, ai-infra]
———

Founder/CEO of [[companies/acme-ai]].
Previously staff engineer at Google Brain.

———

- 2024-09-04: $12M seed, Sequoia led
- 2025-01-18: Open-sourced router
```

## Import is Idempotent (SHA-256 Dedup)

Captured from a real run. **Pass `--no-embed`** to defer embeddings until the search step.

```
gbrain import ~/my-brain/ --no-embed
Found 3 markdown files
[import.files] 3/3 (100%) imported=3 skipped=0 errors=0

Import complete (0.3s):
  3 pages imported
  3 chunks created
```

## Wire the Graph with Zero LLM Calls

Regex inference cascade: **FOUNDED → INVESTED → ADVISES → WORKS\_AT → MENTIONS**.

```
gbrain extract links --source db
Links: created 2 from 3 pages
Done: 2 links, 0 timeline entries

gbrain graph-query people/alice-chen --depth 1
[depth 0] people/alice-chen
  --works_at-> companies/acme-ai (depth 1)
```

## Hybrid: Vector + BM25 + RRF + Reranker

Three modes ship out of the box: **conservative, balanced, tokenmax**. RRF formula: `score = sum(1 / (60 + rank))`.

```
gbrain search "inference"
[0.3648] companies/acme-ai — YC W24
        inference-optimization startup...
[0.3648] people/alice-chen — Founder/CEO of
        [[companies/acme-ai]]...

gbrain query "who works on small-model inference?"
# Hybrid: vector + BM25 + RRF + ZeroEntropy rerank
```

Step 7 — MCP

## Wire Into Claude Code in One Command

GBrain exposes **74 tools** over MCP via stdio. The canonical setup is one CLI call — not a hand-edited JSON file.

```
claude mcp add gbrain -- gbrain serve

# For Cursor / Windsurf, use the standard JSON config:
{
  "mcpServers": {
    "gbrain": {
      "command": "gbrain",
      "args": ["serve"]
    }
  }
}
```

Tool names are plain snake\_case: **get\_page, put\_page, search, query, add\_link, get\_backlinks**, and 68 more.

Key Takeaways

## What You Just Built

- **Markdown-first memory** — humans can always read and edit the source of truth
- **Self-wiring graph** — typed edges extracted on every save, zero LLM cost
- **Hybrid search** — vector + BM25 + RRF + ZeroEntropy reranker, three preset modes
- **Local Postgres** — PGLite by default (up to ~50K pages), Supabase on demand
- **MCP-native** — 74 tools across Claude Code, Cursor, Windsurf

## Key Takeaways

- GBrain (v0.38.2.0) gives AI agents a persistent, markdown-first memory layer — built by Garry Tan to power his own OpenClaw/Hermes deployments holding 146,646 pages and 24,585 people.
- Install runs locally in ~30 minutes on PGLite (Postgres 17 compiled to WASM, zero server) and scales to Supabase or self-hosted Postgres when needed.
- Every wikilink is parsed by a regex inference cascade (`FOUNDED → INVESTED → ADVISES → WORKS_AT`) that writes typed graph edges with zero LLM calls.
- Hybrid search (vector + BM25 + RRF + ZeroEntropy reranker) hits P@5 49.1% / R@5 97.9% on BrainBench — a +31.4-point P@5 lift over the graph-disabled variant.
- Exposes 74 tools over MCP — wire it into Claude Code with a single `claude mcp add gbrain -- gbrain serve` and your agent can read/write the brain directly.

---

Check out the [**GitHub** **Repo**](https://github.com/garrytan/gbrain) and **[Implementation Codes](https://github.com/Marktechpost/AI-Agents-Projects-Tutorials/blob/main/Agentic%20AI%20Codes/gbrain-tutorial.ipynb).** Also, feel free to follow us on **[==Twitter==](https://x.com/intent/follow?screen_name=marktechpost)** and don’t forget to join our **[150k+ ML SubReddit](https://www.reddit.com/r/machinelearningnews/)** and Subscribe to **[our Newsletter](https://www.aidevsignals.com/)**. Wait! are you on telegram? **[now you can join us on telegram as well.](https://t.me/machinelearningresearchnews)**

Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.? **[==Connect with us==](https://forms.gle/MTNLpmJtsFA3VRVd9)**