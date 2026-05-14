---
type: source
source_type: laptop
title: SKILL
slug: skill-3
created: 2026-05-14
captured_by: jehad-altoutou
audience: personal
original_path: /Users/jehad/Documents/janus-brain-bootstrap/skills/janus-brain/SKILL.md
original_size: 24186
original_ext: .md
category: notes
extracted_with: text-copy
extracted_at: "2026-05-14T09:51:46Z"
sensitivity: dept
sensitivity_confidence: 0.95
sensitivity_reason: "The canonical orchestration prompt for /janus-brain — internal-use dept documentation."
---

# SKILL

_Extracted from `Documents/janus-brain-bootstrap/skills/janus-brain/SKILL.md` on 2026-05-14._

---
name: janus-brain
description: One-shot Janus employee brain bootstrap into the single dept-shared Prime Radiant vault. Clones the employee's department GitHub repo (Janusd-io/janus-prime-radiant-<dept>) as their one local Obsidian vault at ~/janus/prime-radiant, scaffolds people/<slug>/ inside it, pulls their Notion + Fireflies + laptop content via MCP and parallel Claude subagents, classifies sensitivity (dept | self | confidential) and routes private items to a gitignored people/<slug>/private/, then commits + pushes back to the shared dept repo. Multiple teammates push to the same dept repo. Invoke when an employee says "/janus-brain", "set up my Janus brain", "onboard me into the wiki", "bring my work into Obsidian". Assumes Claude Desktop is connected to Fireflies and Notion via MCP and `gh` CLI is authenticated to the Janusd-io org. Substrate: Git on GitHub (per 2026-05-13 brief). Single-vault rewrite per 2026-05-14 REWRITE-SPEC.md. Aligned with the Janus Prime Radiant programme (Michael Bruck, program owner).
trigger: /janus-brain
---

# /janus-brain — Your Janus brain in one command

The entry point for Janus's Prime Radiant programme. Run once. Get the shared dept Obsidian vault cloned locally, your personal subtree scaffolded inside it (`people/<your-slug>/`), and your Notion + Fireflies + laptop content ingested, classified, and either pushed to the shared repo (dept-visible) or kept local (private). Multiple teammates contribute to the same dept repo over time.

**Subcommands:** `/janus-brain` (autopilot first run) · `/janus-brain sync` (pull yesterday's Notion + Fireflies + re-enrich new laptop files) · `/janus-brain status` (health check) · `/janus-brain exclude <pattern>` (add to your privacy filter) · `/janus-brain reset` (wipe state, keep vault).

## Pre-flight (what should already be true)

- Claude Desktop is running with **Code** or **Cowork** tab access, this skill installed via `~/Documents/janus-brain-bootstrap/install.sh`
- `gh` CLI installed and authenticated (`gh auth login`); GitHub user has access to the `Janusd-io` org
- **Fireflies MCP** connected in Claude Desktop (Settings → Connectors → Fireflies)
- **Notion MCP** connected in Claude Desktop (Settings → Connectors → Notion)
- Obsidian.app installed
- `python3`, `git`, `gh` on PATH (installer verifies)

If any are missing, the skill stops at Phase 0 with specific instructions.

## What this skill produces

A single fully-populated **dept Prime Radiant vault** at:

```
~/janus/prime-radiant/
```

…backed by the shared dept GitHub repo `Janusd-io/janus-prime-radiant-<dept-slug>` that the whole department contributes to. Inside the vault, dept-shared content lives at the root (`decisions/`, `projects/`, `processes/`, `vendors/`, `concepts/`, `people/`) and your personal content lives at `people/<your-slug>/` with subfolders `sources/`, `meetings/`, `private/` (the last is gitignored). Items the enrichment classifier scores `self` or `confidential` (or `dept` with confidence < 0.7) get routed to `private/` and never reach GitHub.

No cron jobs are installed. Sync runs continuously via the Obsidian Git community plugin (auto-pull on open + auto-commit-and-push every 5 min).

---

## Phase flow (everything below runs without interruption unless the user changes scope)

### Phase 0 — Pre-flight

Run these checks in parallel via Bash:

```bash
command -v python3 >/dev/null && echo "✓ python3" || echo "✗ python3"
command -v git     >/dev/null && echo "✓ git"     || echo "✗ git"
command -v gh      >/dev/null && echo "✓ gh CLI"  || echo "✗ gh CLI (brew install gh)"
command -v graphify >/dev/null && echo "✓ graphify" || echo "⚠ graphify (installer will set up)"
gh auth status >/dev/null 2>&1 && echo "✓ gh authenticated" || echo "✗ gh not authenticated (gh auth login)"
ls -d /Applications/Obsidian.app >/dev/null 2>&1 && echo "✓ Obsidian.app" || echo "✗ Obsidian.app (https://obsidian.md)"
ls -d ~/.claude/skills/janus-brain >/dev/null 2>&1 && echo "✓ janus-brain installed" || echo "✗ janus-brain missing"

# Path hygiene: vault root must not be inside any other sync root
VAULT_ROOT="$HOME/janus/prime-radiant"
case "$VAULT_ROOT" in
  *"/Library/CloudStorage/"*|*"/iCloud Drive/"*|*"/Dropbox/"*)
    echo "✗ Vault root sits inside another sync layer — refuse to proceed" ;;
  *) echo "✓ Vault root path is safe ($VAULT_ROOT)" ;;
esac
```

Also verify MCP connectivity (required for Phases 3 and 3.5):

- Try a small `mcp__claude_ai_Fireflies__fireflies_search` call with a recent date filter; expect ≥0 results, not an auth error
- Try `mcp__claude_ai_Notion__notion-search` with `query_type: user` for the user's own email; expect a hit

If any check fails: stop, tell the user what's missing, give them the fix command. Do not proceed.

### Phase 1 — Identity + task tracker

1. Detect the user: `whoami`, `git config --global user.name`, `git config --global user.email`.
2. Derive a kebab-case slug: `firstname-lastname` (e.g. `theresa-wong`, `andrew-soane`, `jehad-altoutou`).
3. Read `~/.claude/skills/janus-brain/config/departments.yaml` and look up the slug:
   - If found: use the recorded `name` and `departments`. Confirm with the user: "Setting up your Janus brain for **<Name>** in **<Dept>** — correct?"
   - If not found: ask the user for their full name and their primary department (must be one of the locked vocabulary: `ai-office`, `marketing`, `hr`, `it-ops`, `finance`, `office-of-ceo`, `iso`, `pm`, `engineering`, `training`). Append the new person to `departments.yaml`.
4. **Ask the task-tracker question.** Prompt the user:

   > Which task tracker should I file your action items into?
   >
   > 1. **Linear** — `- [ ] @assignee text (due: X) — file in Linear AIP`
   > 2. **Monday** — `- [ ] @assignee text (due: X) — Monday`
   > 3. **Asana** — plain checkbox (Asana-native syntax coming in v2)
   > 4. **Notion tasks** — plain checkbox (Notion-native syntax coming in v2)
   > 5. **None** — plain checkbox only
   > 6. **Other** — plain checkbox only

   Store the answer (`linear` | `monday` | `asana` | `notion` | `none` | `other`) — it becomes the `task_tracker` field in `people/<slug>/.config.yaml` and flows downstream to the meeting-parser subagent and the action-item renderer.

The user can correct any of this before proceeding. They cannot invent a department outside the locked vocabulary.

### Phase 2 — Bootstrap the single dept vault + scaffold your subtree

**Step 1 — Clone (or create from template) the dept repo as the single vault:**

```bash
~/.claude/skills/janus-brain/scripts/bootstrap-dept-vault.sh \
  --dept-slug "<dept-slug>" \
  --curator-slug "<curator-slug-from-departments.yaml>" \
  --curator-name "<Curator Name>" \
  --vault-root "$HOME/janus/prime-radiant"
```

This is idempotent: if the remote exists and the local clone matches it, no-op. If the remote exists and there's no local clone, clones. If neither exists, creates from `Janusd-io/janus-prime-radiant-template` and pushes. **Refuses** if `$VAULT_ROOT/.git` already points at a different remote.

**Step 2 — Scaffold `people/<your-slug>/` inside the vault:**

```bash
~/.claude/skills/janus-brain/scripts/scaffold-person-subtree.sh \
  --vault-root "$HOME/janus/prime-radiant" \
  --person-slug "<person-slug>" \
  --person-name "<Person Name>" \
  --primary-dept "<dept-slug>" \
  --task-tracker "<linear|monday|asana|notion|none|other>"
```

Creates `people/<slug>/.config.yaml`, `CLAUDE.md` (from the `personal-claude-md.md` template), `self.md`, `sources/`, `meetings/`, `private/`, and `.review-queue.md`. Idempotent.

**Step 3 — Add the vault to Obsidian's known-vaults config:**

```bash
python3 - <<'PY'
import json, secrets, time, pathlib
config = pathlib.Path.home() / "Library/Application Support/obsidian/obsidian.json"
data = json.loads(config.read_text()) if config.exists() else {"vaults": {}}
vault_path = pathlib.Path.home() / "janus" / "prime-radiant"
vault_path_str = str(vault_path)
if not any(v.get("path") == vault_path_str for v in data["vaults"].values()):
    data["vaults"][secrets.token_hex(8)] = {"path": vault_path_str, "ts": int(time.time() * 1000), "open": False}
    config.write_text(json.dumps(data))
PY
```

### Phase 3 — Cloud pulls (Notion + Fireflies via MCP)

**Notion** — pull the user's recent forward-looking work into `people/<slug>/sources/notion/`:

1. Call `mcp__claude_ai_Notion__notion-search` with `query: "<person-name> discussion task tracker"` filtered to last 60 days.
2. Call `mcp__claude_ai_Notion__notion-search` with `query: "<dept-name> daily standup"` filtered to last 30 days. (Adapt the query to the person's dept.)
3. For each hit (cap at 20 most-recent), call `mcp__claude_ai_Notion__notion-fetch`, write to `people/<slug>/sources/notion/<page-slug>.md` with PR frontmatter:

```yaml
---
type: source
source_type: notion
slug: <kebab-case>
title: <human title>
created: <YYYY-MM-DD from page metadata>
captured_by: <person-slug>
notion_url: <url>
audience: department
departments: [<dept-slug>]
sensitivity: dept           # default; enrichment classifier may revise
sensitivity_confidence: 0.5
---
```

**Fireflies** — pull the user's recent meetings directly to `people/<slug>/meetings/` (no inbox staging):

1. **List meetings** — `mcp__claude_ai_Fireflies__fireflies_get_transcripts` with `mine: true`, `fromDate: <30 days ago>`, `limit: 30`, `format: "json"`. We **ignore** Fireflies' own summary / keywords / action_items — those are shallow and anonymize speakers. The parser subagent in Phase 3.5 does its own extraction.

2. **Skip recurring/personal meetings** — title matches `*standup*`, `*1:1*`, `*one on one*`.

3. **For each kept transcript**, call `mcp__claude_ai_Fireflies__fireflies_get_transcript` with the `id`. Parse: `Speakers:` (real attendee list), `Title`, `Transcript Url`, `Duration`. The sentences start after the `Sentences:` prefix on the first sentence line and continue until the `Title:` line.

4. **Stage two sibling files per meeting**, both directly in `people/<slug>/meetings/`:

   - **Meeting note** at `people/<slug>/meetings/<YYYY-MM-DD>-<meeting-slug>.md` — frontmatter + empty digest scaffolding pointing at the transcript sibling. Use the shape in `templates/meeting-source.md`. Set `task_tracker` from Phase 1.
   - **Transcript file** at `people/<slug>/meetings/<YYYY-MM-DD>-<meeting-slug>.transcript.md` — minimal frontmatter (`type: transcript`, `source: meeting`, `meeting_slug`, `captured_by`, `created`) followed by the verbatim `Name: utterance` lines.

   Default the meeting note's `audience: department` and `dept_scope: [<dept-slug>]`; the parser subagent in Phase 3.5 may revise based on the actual attendee mix.

Print the count of Notion entries + Fireflies meetings staged.

### Phase 3.5 — Fireflies enrichment (parse transcripts into digests)

Every Fireflies meeting note staged in Phase 3 lives at `people/<slug>/meetings/<date>-<slug>.md` with the transcript at the sibling `<date>-<slug>.transcript.md`. Before the generic enrichment pass touches them, run the dedicated meeting parser — it produces the standup-schema digest (Summary · Decisions · Action items · 🎯 This week · 🏔️ Long horizon · Findings · Open questions · Blockers · Tool mentions · Topics · Related) and creates one `decisions/<slug>.md` per substantive decision plus stubs for previously-unknown attendees.

**Step 1 — Discover the meetings to parse:**

```bash
VAULT="$HOME/janus/prime-radiant"
PERSON="<person-slug>"
ls "$VAULT/people/$PERSON/meetings/"*.md \
  | grep -v '\.transcript\.md$'
```

**Step 2 — Dispatch one meeting-parser subagent per meeting, IN A SINGLE MESSAGE (parallel).**

Cap: 10 concurrent. If more than 10 meetings, dispatch in batches of 10, waiting between batches.

Each subagent gets the prompt from `~/.claude/skills/janus-brain/prompts/meeting-parser-subagent.md` with substitutions:

- `PERSON_SLUG` — kebab slug for the vault owner
- `DEPT_SLUGS` — comma-separated dept slugs from `config/departments.yaml`
- `VAULT_PATH` — absolute vault path (`$HOME/janus/prime-radiant`)
- `MEETING_FILE` — absolute path to the meeting note (NOT the transcript sibling)
- `OUT_FILE` — `<VAULT>/.state/meeting-digest/<meeting-slug>.json`
- `PEOPLE_ROSTER` — paste the `people:` block from `config/departments.yaml`
- `TASK_TRACKER` — the answer from Phase 1

The subagent reads the meeting note's frontmatter + the sibling `.transcript.md` body and writes its JSON manifest to `OUT_FILE`. **Subagents do not modify the vault directly.**

**Step 3 — Wait for all manifests, then run the applier (deterministic):**

```bash
python3 ~/.claude/skills/janus-brain/scripts/apply-meeting-digests.py \
    --vault "$VAULT" \
    --person "$PERSON" \
    --depts "<comma-sep dept slugs>" \
    --ingest-dir "$VAULT/.state/meeting-digest"
```

The applier rewrites each meeting note with the standup-schema digest sections + a `## Transcript` wikilink to the sibling, writes `decisions/<slug>.md` per substantive decision (never overwrites), creates `people/<slug>.md` stubs for newly-mentioned people, and renders action items formatted per the person's `task_tracker` (read from their `.config.yaml`). Idempotent.

Print the report. Failures are surfaced inline; the applier exits non-zero if any meeting rewrite was skipped due to an error.

### Phase 4 — Laptop walk

```bash
python3 ~/.claude/skills/janus-brain/scripts/walk-and-filter.py \
    --root "$HOME" \
    --vault "$HOME/janus/prime-radiant" \
    --config ~/.claude/skills/janus-brain/config \
    --out ~/.claude/skills/janus-brain/state/manifest.json
```

**5k file hard-stop applies.** If the walker exits with "too many files", show the top 5 subdirectories by count and ask the user which to include. Most people's first run wants to start narrow: `~/Documents/`, maybe `~/Desktop/`. Target ≤ 200 files for the first run (token-cost discipline).

Once the walker returns a manageable count, show the summary block (notes / docs / pdfs / code / images / config / excluded) and ask: "Walk complete. Narrow scope, or proceed to extraction (Phase 4.5)?"

### Phase 4.5 — Content extraction (full conversion to markdown)

**Pause and ask the user** which categories to extract: (a) all / (b) text-only / (c) documents only / (d) skip. See REWRITE-SPEC.md for prompt copy. Then run:

| Choice | Command |
| --- | --- |
| (a) all | `JB_PERSON_SLUG=<slug> ~/.claude/skills/janus-brain/scripts/extract-content.sh` |
| (b) text-only | `JB_PERSON_SLUG=<slug> ~/.claude/skills/janus-brain/scripts/extract-content.sh --only-categories notes,docs,pdfs,slides` |
| (c) documents only | `JB_PERSON_SLUG=<slug> ~/.claude/skills/janus-brain/scripts/extract-content.sh --only-categories pdfs,docs` |
| (d) skip | _(don't run the extractor; proceed to Phase 5 directly)_ |

Tools used (all local, free): `pdftotext` (poppler), `pandoc`, `pandas`, `tesseract`. Each output lands at `people/<slug>/sources/laptop/<category>/<slug>.md` with frontmatter (`original_path`, `original_size`, `extracted_with`, plus default `sensitivity: dept`, `sensitivity_confidence: 0.5`; the Phase 5 classifier revises these). The wrapper auto-detects `JB_PERSON_SLUG` when exactly one `people/<slug>/` subtree exists in the vault, so the env var prefix can be omitted on a fresh single-person enrollment.

### Phase 5 — Enrichment (parallel subagents) + sensitivity classifier

Split the `included` list into chunks of 18-22 files each, grouped by source directory. Cap at 8 chunks total.

**Dispatch ALL chunks as parallel general-purpose Agent calls IN A SINGLE MESSAGE.**

Each subagent receives the prompt from `~/.claude/skills/janus-brain/prompts/enrichment-subagent.md` with substitutions: `CHUNK_NUM`, `TOTAL_CHUNKS`, `PERSON_SLUG`, `DEPT_SLUGS`, `VAULT_PATH`, `OUT_FILE`, file list.

**Sensitivity classification** — every source frontmatter must have `sensitivity` (one of `dept` | `self` | `confidential`) and `sensitivity_confidence` (0.0–1.0). Heuristics in the subagent:

- credentials / API keys / passwords → `confidential`
- HR / salary / performance review / legal / health / family / personal finance → `confidential`
- 1:1 personal manager context → `self`
- default → `dept`

The subagent emits these per-source in its manifest. **The applier (Phase 6) routes accordingly.**

**Rules adapted for the single-vault layout:**

1. Files have already been extracted by Phase 4.5 to `people/<slug>/sources/laptop/<category>/<slug>.md` with FULL content. The subagent's job is enrichment on top of that content, not summarisation.
2. **For images flagged `needs_vision_description: true`** — open the file at `original_path` (you have vision) and append a `## Visual description` heading.
3. **Subagents DO NOT modify existing wiki pages directly.** Race conditions. Write only to the source's own page and proposed creates as PROPOSALS in the manifest.
4. **Subagents include `draft_content` for every `proposed_pages_created`.** No half-proposals.

Wait for all chunks to complete. Verify each chunk's manifest exists.

### Phase 6 — Apply proposals + sensitivity routing + validate

Iterate the chunk manifests and apply serially:

```python
for each chunk manifest:
    for each source in chunk.sources:
        sens = source.sensitivity
        conf = source.sensitivity_confidence
        if sens in ("self", "confidential") or (sens == "dept" and conf < 0.7):
            move the source file from people/<slug>/sources/... to people/<slug>/private/<...same relative path...>
        if conf < 0.7:
            append a line to people/<slug>/.review-queue.md noting the file, proposed sens, confidence, and reason
    for each proposed_pages_created with draft_content:
        write to <vault>/<path>     # decisions, projects, vendors, concepts, people at vault root
    for each escalation:
        log it (subagent already wrote the questions/ingest-*.md file)
```

After applying, run the validator + index rebuild:

```bash
python3 ~/.claude/skills/janus-brain/scripts/ingest-to-radiant.py \
    --vault "$HOME/janus/prime-radiant" \
    --person "<person-slug>" \
    --ingest-dir ~/.claude/skills/janus-brain/state/ingest \
    --templates ~/.claude/skills/janus-brain/templates
```

> **TODO(jehad):** `ingest-to-radiant.py` predates this rewrite — it likely still expects a personal-vault layout. Review when first run surfaces failures and fix in place.

### Phase 7 — Commit + push

**No federation. No sibling clones. No AIO read-only clone.** Single vault, one `git push`:

```bash
cd "$HOME/janus/prime-radiant"
git add -A
git commit -m "janus-brain bootstrap for <person-slug> ($(date -u +%Y-%m-%d))" || true
git push
```

`private/` and `.review-queue.md` are gitignored (per `templates/dept-gitignore`, applied at bootstrap time) — they never reach GitHub. Everything else is now visible to your dept teammates.

**Tell the user how to enable the Obsidian Git plugin** for transparent ongoing sync:

```
1. Open the vault in Obsidian
2. Settings → Community plugins → Turn on (one-time per vault; accept disclaimer)
3. Browse → search "Git" → install "Git" by vinzent03 → Enable
4. Settings → Git → set:
   - Auto pull interval (minutes): 5
   - Auto pull on startup: on
   - Auto backup interval (minutes): 5
   - Commit message template: "vault backup: {{date}} {{hostname}}"
   - Pull strategy: rebase
```

After this, the plugin auto-pulls every 5 min (latest team knowledge appears in your vault) and auto-commits + pushes every 5 min (your edits propagate back to the dept repo).

**Cowork-side commit responsibility.** When the user runs `/janus-brain sync` or similar workflows in Cowork/Code mode, the skill should `git pull` at the start and `git add -A && git commit && git push` at the end.

### Phase 8 — Lint + open + report

Run a vault health check:

```bash
~/.claude/skills/janus-brain/scripts/lint-vault.sh --quiet
```

Open the vault in Obsidian:

```bash
open -a Obsidian "$HOME/janus/prime-radiant"
```

(If Obsidian was already running, instruct the user: "Quit Obsidian with Cmd+Q and reopen — vault switcher will show 'prime-radiant'.")

Final user-facing summary:

```
Janus brain ready.

Vault: ~/janus/prime-radiant
  remote: Janusd-io/janus-prime-radiant-<dept-slug>
  your subtree: people/<your-slug>/

Content:
  • <N1> Notion entries imported into people/<slug>/sources/notion/
  • <N2> Fireflies meetings parsed (digests + transcripts split out)
  • <N3> laptop documents enriched into people/<slug>/sources/laptop/
  • <N4> new wiki pages at the vault root (decisions, projects, concepts, …)
  • <N5> items routed to private/ (sensitivity=self|confidential)
  • <N6> items logged to .review-queue.md (low-confidence classifications)

Lint:
  <X> errors, <Y> warnings — review with /janus-brain lint

Next steps:
  1. Open Obsidian — your "prime-radiant" vault is in the vault switcher
  2. Settings → Community plugins → install "Git" by vinzent03 → enable
  3. Skim people/<your-slug>/.review-queue.md and confirm or move flagged items
  4. Browse index.md / decisions/ / projects/ to see what was cataloged
```

---

## Subcommands (lightweight; the meat is `/janus-brain` for power users)

- `/janus-brain` — first-run autopilot (everything above)
- `/janus-brain sync` — pull yesterday's Notion + Fireflies + re-enrich new laptop files + push
- `/janus-brain status` — health check (vault size, last sync, review-queue length)
- For everything else (`exclude`, `reset`, custom scope, etc.), redirect users to `/janus-brain`

---

## Cost discipline

A first run with the default scope (≤ 200 files + ~30 Notion entries + ~20 Fireflies meetings) dispatches roughly 6-10 parallel subagents. Token cost is meaningful but bounded.

If the user's scope balloons past 1000 files at Phase 4, **stop and narrow**.

---

## Failure modes

| Failure | Recovery |
| --- | --- |
| `gh` not authenticated | `gh auth login` (choose GitHub.com, HTTPS, web browser) |
| `gh` user lacks `Janusd-io` access | Ask Michael / org admin to add the user to the org and the relevant Team |
| `gh repo create` fails | User lacks create-repo permission in `Janusd-io` — same fix as above |
| Vault root inside iCloud/Drive/Dropbox | Refuse to proceed; instruct user to move the vault root |
| `$VAULT_ROOT/.git` exists with different remote | bootstrap-dept-vault.sh refuses; move or remove the old vault |
| Fireflies MCP not connected | Send to Claude Desktop → Settings → Connectors → Fireflies |
| Notion MCP not connected | Same flow for Notion |
| Department not in locked vocabulary | Escalate via `questions/ingest-*.md`; user proceeds with closest existing department |
| Subagent chunk fails | Re-dispatch that specific chunk with the same prompt |
| `git push` fails | Likely auth or remote-mismatch. Run `git -C ~/janus/prime-radiant remote -v` and `gh auth status` |

---

## See also

- `~/.claude/skills/janus-brain/templates/personal-claude-md.md` — the per-person rulebook (lands as `people/<slug>/CLAUDE.md`)
- `~/.claude/skills/janus-brain/prompts/meeting-parser-subagent.md` — standup-schema meeting digest spec
- `~/.claude/skills/janus-brain/prompts/enrichment-subagent.md` — generic source enrichment + sensitivity classification
- `~/.claude/skills/janus-brain/config/departments.yaml` — locked dept vocabulary + per-person roster
- `REWRITE-SPEC.md` (repo root) — 2026-05-14 single-vault architecture spec

## Janus Prime Radiant programme

This skill implements the Janus Prime Radiant programme (Michael Bruck, programme owner) under the **single-vault model** (rewrite 2026-05-14). One GitHub repo per department; every employee in that dept clones it as their single Obsidian vault and contributes to it via Git. The personal repo + federation machinery from the earlier two-vault design has been deleted. A future read-only "CEO brain" skill will federate across dept repos — out of scope here. Substrate (Git on GitHub) per Michael's 2026-05-13 brief.
