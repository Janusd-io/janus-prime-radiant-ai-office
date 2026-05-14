---
type: process
title: /janus-brain enrollment flow
slug: janus-brain-enrollment
created: 2026-05-14
updated: 2026-05-14
departments: [ai-office, it-ops]
status: active
sources: [skill-3, readme-12, install-2, enrollment, readme-11, rewrite-spec, handover]
related: [janus-brain-bootstrap, prime-radiant, single-vault-model, sensitivity-classification, prime-radiant-instance-setup, claude-md-rulebook]
captured_by: jehad-altoutou
owner: jehad-altoutou
audience: department
---

# /janus-brain enrollment flow

The 8-phase autopilot the `/janus-brain` skill runs the first time any Janus employee invokes it in Claude Desktop. Single-vault model per [[single-vault-model]] (2026-05-14 rewrite). One run takes ~15 minutes of mostly watching, with two confirmation prompts.

## Phases

| # | Phase | What happens |
| --- | --- | --- |
| 0 | Pre-flight | Verifies python3 / git / gh / Obsidian / MCP connectivity / vault-root path hygiene (refuses if inside iCloud, Drive, or Dropbox). |
| 1 | Identity + task tracker | Detects git user, looks up the slug in `departments.yaml`, asks the user which task tracker (Linear / Monday / Asana / Notion / none / other) to format action items for. Stored in `people/<slug>/.config.yaml`. |
| 2 | Bootstrap + scaffold | `bootstrap-dept-vault.sh` clones (or creates from template) `Janusd-io/janus-prime-radiant-<dept>` to `~/janus/prime-radiant/`. `scaffold-person-subtree.sh` creates the `people/<slug>/` subtree with `CLAUDE.md`, `self.md`, `sources/`, `meetings/`, `private/`, `.review-queue.md`. |
| 3 | Cloud pulls | Notion MCP fetches the user's recent forward-looking pages to `people/<slug>/sources/notion/`. Fireflies MCP fetches their non-standup meetings to `people/<slug>/meetings/` as `<date>-<slug>.md` plus a sibling `.transcript.md`. |
| 3.5 | Meeting parser | One parallel subagent per meeting produces the standup-schema digest (Summary · Decisions · Action items · This week · Long-horizon · Findings · Open questions · Blockers · Tool mentions · Topics · Related). Raw transcript stays in the sibling file. Action items are formatted per the user's task tracker. |
| 4 | Laptop walk | `walk-and-filter.py` walks `$HOME` minus excludes from [[exclude-patterns]] + [[exclude-paths]]. Hard-stops at 5k files. |
| 4.5 | Content extraction | Prompted: all / text-only / docs-only / skip. Uses `pdftotext`, `pandoc`, `pandas`, `tesseract`, plus direct copy for plain text + fenced-code for source. Output lands at `people/<slug>/sources/laptop/<category>/<slug>.md`. |
| 5 | Enrichment + sensitivity | Up to 8 parallel chunks of 18-22 files each. Each subagent enriches on top of the extracted content and writes `sensitivity` + `sensitivity_confidence` to every source (see [[sensitivity-classification]]). |
| 6 | Apply + sensitivity routing | Decisions / projects / concepts written to the vault root. Sources scored `self` / `confidential` / `dept`<0.7 moved to `people/<slug>/private/`; low-confidence items logged to `.review-queue.md`. |
| 7 | Commit + push | `git add && commit && push` from the single vault to the dept repo. No federation. |
| 8 | Lint + open | `lint-vault.sh` schema + integrity checks; opens Obsidian. User installs the [[obsidian]] Git community plugin manually (one-time, ~2 min, ~5 settings). |

## Subcommands after first run

| Command | Purpose |
| --- | --- |
| `/janus-brain sync` | Pull yesterday's Notion + Fireflies + re-enrich new laptop files + push |
| `/janus-brain status` | Health check (vault size, last sync, review-queue length) |
| `/janus-brain exclude <pattern>` | Add a basename pattern to `user-exclude.txt` |
| `/janus-brain reset` | Wipe local state metadata (keeps the vault) |

## Cost discipline

A first run with default scope (≤ 200 laptop files + ~30 Notion entries + ~20 Fireflies meetings) dispatches roughly 6-10 parallel subagents. If scope balloons past 1000 files at Phase 4, the skill stops and asks the user to narrow.

## See also

- [[janus-brain-bootstrap]] — the project that built this
- [[single-vault-model]] — the architecture the 2026-05-14 rewrite landed
- [[sensitivity-classification]] — Phase 5 / 6 privacy routing
- [[prime-radiant]] — the program-wide pattern
