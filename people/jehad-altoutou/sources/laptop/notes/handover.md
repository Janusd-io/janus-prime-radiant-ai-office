---
type: source
source_type: laptop
title: HANDOVER
slug: handover
created: 2026-05-14
captured_by: jehad-altoutou
audience: personal
original_path: /Users/jehad/Documents/janus-brain-bootstrap/HANDOVER.md
original_size: 32720
original_ext: .md
category: notes
extracted_with: text-copy
extracted_at: "2026-05-14T09:51:46Z"
sensitivity: dept
sensitivity_confidence: 0.90
sensitivity_reason: "Comprehensive build-session handover. Contains email addresses (already public on the user's CLAUDE.md), GitHub repo URLs, and architectural decisions — all dept-internal but no secrets, salaries, or "
project: janus-brain-bootstrap

---

# HANDOVER

_Extracted from `Documents/janus-brain-bootstrap/HANDOVER.md` on 2026-05-14._

# HANDOVER — [[janus-brain-bootstrap|Janus Brain bootstrap]]

> Last updated: 2026-05-14 (end of focused build session 2026-05-12 → 2026-05-14)
> Owner: [[jehad-altoutou|Jehad Altoutou]] · AI Operations Engineer · `jehada@janusd.io`
> Programme owner: [[michael-bruck|Michael Bruck]] (`michael-bruck@janusd.io`)

A self-contained context document for the next Claude session (or any collaborator) to pick up from where we left. Read this first.

---

## 1. TL;DR

The `/janus-brain` skill creates a private [[github|GitHub]]-backed [[obsidian|Obsidian]] "Personal [[prime-radiant|Prime Radiant]]" vault for any Janus employee, populates it from their Notion + [[fireflies|Fireflies]] + laptop content, clones the canonical department vault as a sibling, and federates curated knowledge into the dept vault's inbox/.

- **Substrate:** Git on GitHub under `Janusd-io` org (migrated off [[google-drive|Google Drive]] on 2026-05-13 per Michael's brief)
- **Deployment surface:** Claude Desktop → Code tab (or [[cowork|Cowork]])
- **Sync model:** [[obsidian-git|Obsidian Git]] plugin (continuous, 5-min) + optional launchd auto-sync (daily, triggers `/janus-brain sync` via AppleScript)
- **User enrollment:** Jehad enrolled himself on 2026-05-13. Real data flowed through. Andrew (Marketing) is the next planned enrollment.
- **Production state:** Pipeline is production-grade for first-time enrollment of a Janus employee in a known department. One known gap (Phase 4.5 wasn't run in Jehad's enrollment — needs `/janus-brain sync` with full extraction selected).

---

## 2. Repos that compose the system

All under [`Janusd-io`](https://github.com/Janusd-io) GitHub org, all private.

| Repo | Role | Owner | State |
| --- | --- | --- | --- |
| [`janus-brain-bootstrap`](https://github.com/Janusd-io/janus-brain-bootstrap) | Skill installer + scripts + docs (this repo) | Jehad | `main` HEAD has all the work below |
| [`janus-prime-radiant-template`](https://github.com/Janusd-io/janus-prime-radiant-template) | Dept-tier canonical template (v0.9.0) | Michael | Stable; cloned by `bootstrap-dept-vault.sh` |
| [`janus-prime-radiant-personal-template`](https://github.com/Janusd-io/janus-prime-radiant-personal-template) | Personal-tier canonical template (v0.1.0) | Jehad | **Created this session.** Cloned by `bootstrap-personal-vault.sh` |
| [`janus-prime-radiant-ai-office`](https://github.com/Janusd-io/janus-prime-radiant-ai-office) | Live AIO dept vault | Michael | Exists with template baseline + 121 inbox items from Jehad's [[federation|federation]] |
| `janus-prime-radiant-personal-jehad-altoutou` | Jehad's personal vault | Jehad | Created during enrollment. 507 files. |
| _(future)_ `janus-prime-radiant-personal-andrew-soane` | Andrew's personal vault | Andrew | Will be auto-created when Andrew runs `/janus-brain` |
| _(future)_ `janus-prime-radiant-marketing` | Marketing dept vault | Andrew (curator) | Will be auto-created from template on Andrew's first run if it doesn't yet exist |
| _(future)_ `janus-prime-radiant-hr`, `…-finance`, `…-it-ops`, `…-engineering`, `…-training`, `…-office-of-ceo`, `…-iso` | Other dept vaults | Per dept curator | Will be auto-created on first contributor enrollment |

---

## 3. Local state on Jehad's machine (verified end-of-session)

```text
~/Documents/janus-brain-bootstrap/           ← this repo, clone for development
~/.claude/skills/janus-brain/                ← installed skill (40 files)
~/.config/janus-brain/sync.conf              ← user config (correct paths)

~/janus/prime-radiant/personal/              ← Jehad's personal vault clone (507 files)
~/janus/prime-radiant/ai-office/             ← AIO clone (400 files; Michael's working content)

~/Documents/_PR-Backups/                     ← pre-migration backup tarball
  obsidian-backup-pre-git-migration-2026-05-13T115546Z.tar.gz   (~852 KB)
  obsidian-backup-pre-git-migration-2026-05-13T115546Z.manifest.txt
```

Drive-era vaults are untouched but no longer the source of truth:

```text
~/Documents/Prime Radiant — Jehad Altoutou/  ← old Drive-era personal vault, 191 files (kept for reference)
~/Documents/Obsidian Vault/                  ← unrelated personal Obsidian vault, 1093 files
~/Library/CloudStorage/GoogleDrive-jehada@janusd.io/Shared drives/Janus AI Office/  ← Michael's Drive AIO copy (pending his own Drive→Git migration step)
```

Git state on the two Git-substrate vaults:

| Vault | Branch | Sync state | Uncommitted |
| --- | --- | --- | --- |
| `personal` | `main` | in sync with origin | 2 files (`.obsidian/` workspace state + `log.md` change from federate run) |
| `ai-office` | `main` | in sync with origin | clean |

No launchd auto-sync schedule currently installed (we set up the infrastructure but uninstalled the test schedule at end of session — user picks their time when they install).

No cron entries (we retired the Drive-era cron model when migrating).

---

## 4. Commit history of this session (recent first)

All on `main` at github.com/Janusd-io/janus-brain-bootstrap:

| Commit | Summary |
| --- | --- |
| `0c55c23` | Federation dedup (new / overwrote_own / skipped_duplicate / enriched_others) |
| `040524b` | Auto-sync: daily launchd job that opens Claude Desktop + types `/janus-brain sync` |
| `1a912dd` | Phase 4.5 prompt: ask user before content extraction with category-scope choice |
| `1961167` | Phase 4.5: full content extraction (pdftotext / pandoc / tesseract / pandas) |
| `e5e509f` | Created `janus-prime-radiant-personal-template` repo + refactored bootstrap-personal-vault.sh to clone from it |
| `8900df0` | Substrate migration: Google Drive → Git on GitHub |
| `60d66c0` | Fireflies parser: validated against real MCP transcripts (full extraction, not pass-through) |
| `3910699` | Vault linter (schema + integrity checks) |
| `f44ddde` | Replace wholesale dept mirror with bootstrap-then-federate model |
| `453fa94` | Make /janus-brain portable for any Janus employee (no Jehad-specific paths) |
| `7f8b1e9` | Rewrite README + add ENROLLMENT guide |
| `0b63b4b` | Meeting parser: full extraction from raw transcript (not Fireflies pass-through) |

(See `git log --oneline` for full history.)

---

## 5. What's been built and tested

### Phase 0 — Pre-flight
Verifies `python3`, `git`, `gh auth`, Obsidian, MCP connectivity, path hygiene (refuses if vault root is under iCloud/Drive/Dropbox). **Tested.**

### Phase 1 — Identity
`git config` + `config/departments.yaml` lookup. **Tested in Jehad's enrollment.**

### Phase 2 — Scaffold + bootstrap personal repo
`bootstrap-personal-vault.sh` → clones `janus-prime-radiant-personal-template` → substitutes placeholders → creates private repo `janus-prime-radiant-personal-<slug>` → pushes initial commit. **Tested end-to-end (Jehad's repo created and pushed cleanly).**

### Phase 3 — Cloud pulls
Notion MCP + Fireflies MCP. Skips recurring standups. **Tested in Jehad's enrollment: 11 meetings + 12 Notion sources captured.**

### Phase 3.5 — Fireflies meeting parser
`meeting-parser-subagent.md` dispatched per meeting; each subagent reads the raw transcript (with real speaker names per sentence), extracts substantive summary + decisions + action items + topics + entity links. `apply-meeting-digests.py` applies the manifest deterministically. **Real-data validated** against the Andrew Marketing meeting (815 sentences, 7 decisions extracted with verbatim evidence quotes, 13 action items mapped with assignee + assigned_by, 19 related entities, 0 lint errors on the output). **Jehad's enrollment produced 84 decisions across 11 meetings.**

Note: `AIO <date>` daily standups are intentionally skipped by Phase 3 (per the standup-skip heuristic) — they're handled by the dedicated `/standup` skill.

### Phase 4 — Laptop walk
`walk-and-filter.py` walks `$HOME` (or narrower scope) with the 5-layer privacy filter; produces manifest at `<vault>/.state/manifest.json`. 5k-file hard-stop. **Substrate-agnostic, no Drive references.**

### Phase 4.5 — Content extraction (NEW; NOT YET RUN IN PRODUCTION)
**Prompt-gated.** Asks the user: all categories / text-only / docs-only / skip.

`extract-content.py` converts every file to full markdown:
- `pdftotext` for PDFs → `sources/laptop/pdfs/<slug>.md`
- `pandoc` for DOCX/PPTX/RTF/ODT/HTML/EPUB → `sources/laptop/{docs,slides}/<slug>.md`
- `pandas` for XLSX/XLS; stdlib `csv` for CSV/TSV → `sources/laptop/sheets/<slug>.md`
- `tesseract` OCR for images → `sources/laptop/images/<slug>.md` (flags `needs_vision_description: true` if OCR yields < 50 chars)
- Direct copy for plain text + fenced-code embed for source code

**Smoke-tested on 4 real files from Jehad's machine** (AI Charter PDF, PULS-First-Voice DOCX, Screenshot, Janus Logo). 3 extracted cleanly, 1 graceful error (source path moved). **NOT YET RUN VIA ORCHESTRATOR** — Jehad's enrollment skipped Phase 4.5; needs `/janus-brain sync` with option (a) to populate.

Toolchain installed on Jehad's Mac:
```text
✓ pdftotext (poppler)
✓ pandoc
✓ tesseract
✓ pandas
```

### Phase 5 — Enrichment (generic subagents)
`enrichment-subagent.md` dispatched up to 8 in parallel per chunk of files. For images flagged `needs_vision_description: true`, the subagent opens the file via vision and appends a `## Visual description` section. **Jehad's enrollment produced 137 enriched sources + 56 concepts + 38 projects + 84 decisions + 74 vendor stubs + 20 internal/4 external people stubs + 6 lessons + 3 processes + 3 questions.**

### Phase 6 — Apply
`ingest-to-radiant.py` validates + rebuilds index. **Substrate-agnostic, ran in Jehad's enrollment.**

### Phase 7 — Federation setup
1. `write-sync-config.sh` → `~/.config/janus-brain/sync.conf`
2. `bootstrap-dept-vault.sh` clones (or creates from template) the dept repo
3. Clones AIO if user is not in AIO
4. `git add -A && commit && push` on personal repo
5. `federate-to-department.sh --mode initial` → pushes `audience: department/org/...` items to dept inbox

**Federation dedup** (committed today): four-way decision per (item, target): `new` / `overwrote_own` / `skipped_duplicate` / `enriched_others`. Normalised hash strips volatile frontmatter (`captured_by`, timestamps) so two contributors who ingest the same meeting produce identical hashes and the second push is skipped.

**Jehad's enrollment: 121 items federated to AIO inbox.** Smoke-tested all 4 dedup decisions against fixture.

### Phase 8 — Lint + open
`lint-vault.sh` runs schema + integrity checks. **Jehad's vault: 19 errors, 34 warnings** (errors are all broken wikilinks to entities not yet stubbed; warnings are orphan pages + unresolved source refs). Then `open -a Obsidian "<personal-vault>"`.

### Auto-sync (NEW, optional, NOT YET ENABLED)
`auto-sync.sh` + launchd plist template. Fires daily at user-chosen time → opens Claude Desktop → AppleScript types `/janus-brain sync`. Idle check (skips if user has been active in last hour). No API keys. Uses Claude Desktop's existing MCP setup.

Install / status / uninstall:
```bash
~/Documents/janus-brain-bootstrap/install.sh --install-auto-sync --time 07:30
~/Documents/janus-brain-bootstrap/install.sh --auto-sync-status
~/Documents/janus-brain-bootstrap/install.sh --uninstall-auto-sync
```

**Smoke-tested end-to-end** during build; user has NOT yet enabled it on their machine.

---

## 6. What is NOT yet validated end-to-end

| Component | Why not validated | Risk |
| --- | --- | --- |
| Phase 4.5 via orchestrator | Jehad's enrollment skipped this phase | Medium — needs `/janus-brain sync` with option (a) to confirm orchestrator dispatches `extract-content.sh` correctly |
| Phase 5 enrichment dispatch since substrate migration | Phase 5 ran in Jehad's enrollment but new substrate paths weren't stressed | Low — paths are substrate-agnostic |
| Auto-sync first fire on a real day | Schedule not yet installed by user | Low — script logic + plist rendering smoke-tested |
| Andrew's enrollment | Not yet run | Low — Jehad's enrollment surfaced no orchestrator bugs; Andrew's flow is identical |
| `bootstrap-dept-vault.sh` creating a brand-new dept repo | Marketing dept repo doesn't exist yet; will be created on Andrew's run | Low — script tested with fake-drive fixture + dry-runs against real Janusd-io |
| `gh repo create` for a per-employee personal repo (Andrew) | Only Jehad's personal repo has been created | Low — Jehad's worked; Andrew is org member with same perms |

---

## 7. Known issues / open items (prioritized)

### High priority (blocking polish on Jehad's vault)

1. **Phase 4.5 not yet run** — Jehad's vault has summary-mode laptop content, not full-text extraction. Fix: `/janus-brain sync` in Code tab → pick option (a) at the Phase 4.5 prompt.
2. **2 uncommitted files** in personal vault: `log.md` (federate-run log entry) + new `.obsidian/` entries from opening the vault. Fix:
   ```bash
   cd ~/janus/prime-radiant/personal
   git add -A && git commit -m "Post-enrollment: federate log + obsidian session" && git push
   ```
3. **19 broken wikilinks** (lint errors). All are references to entities/decisions/vendors that exist in AIO but weren't auto-stubbed in personal. Either (a) accept and let future federate cycles fill them, (b) run a stub-creation pass, or (c) auto-stub on-write in Phase 6.

### Medium priority (for company-wide rollout)

4. **AIO Drive → AIO GitHub migration** — Michael's responsibility per his 2026-05-13 brief Migration Sequence step 1. The repo `Janusd-io/janus-prime-radiant-ai-office` exists with template baseline; Michael needs to push his Drive working content into it. (User can't do this on Michael's behalf.)
5. **Obsidian Git plugin installation** — Jehad and any new employee need to install it manually in each vault (Code tab can't do it). One-time per vault, takes 2 min. Documented in ENROLLMENT.md.
6. **Andrew's enrollment** — ENROLLMENT.md is production-ready. Forward to Andrew. He needs Code-tab access (confirmed yes earlier).

### Low priority (polish + future-proofing)

7. **Schema-version CI alignment** between `janus-prime-radiant-template` (Michael's, currently v0.9.0) and `janus-prime-radiant-personal-template` (Jehad's, v0.1.0). When Michael bumps schema, the personal template should match. Currently manual. Could add a GitHub Action that fails CI when versions diverge.
8. **AIO daily standup filter decision** — currently `AIO <date>` titles are skipped by Phase 3 (designed for `/standup` to handle). User asked about this but didn't make a final call. If they want both pipelines to ingest the same meeting, the standup filter needs adjustment.
9. **`.obsidian/` directory in personal repo** — currently 7 files are tracked. The `.gitignore` only excludes session files (`workspace*.json`, `cache`). User preferences (theme, plugin enable state, etc.) ARE tracked. Probably fine; matches AIO's pattern. But consider whether plugin data files should be excluded.
10. **`needs_vision_description` follow-up** — image files flagged for vision in Phase 4.5 currently get a description from the Phase 5 enrichment subagent. Validate the subagent actually opens the image file via vision when it sees that frontmatter flag.
11. **Fireflies API key for cron path** — `fetch-fireflies.py` REST fallback still uses an API key. Not strictly needed (MCP is preferred), but installer mentions it as optional. Could be retired entirely.

---

## 8. Next actions

### For the user

1. **Run `/janus-brain sync`** in Claude Desktop → Code tab, pick Phase 4.5 option (a). This converts every laptop file (PDFs, DOCX, images, etc.) to full markdown in `sources/laptop/<category>/`.
2. **Commit the 2 uncommitted files** in personal vault.
3. **Install the Obsidian Git community plugin** in `~/janus/prime-radiant/personal/` and `~/janus/prime-radiant/ai-office/`. Settings → Community plugins → "Git" by vinzent03. Configure: auto-pull on startup, auto-pull every 5 min, auto-commit-and-push every 5 min, pull strategy: rebase.
4. **(Optional)** Install auto-sync: `~/Documents/janus-brain-bootstrap/install.sh --install-auto-sync --time 07:30` (pick your time).
5. **Forward [ENROLLMENT.md](ENROLLMENT.md) to Andrew** when ready. He runs the same 3-command setup and `/janus-brain` works identically.

### For Michael (programme owner)

6. **Push the Drive AIO content to `Janusd-io/janus-prime-radiant-ai-office`** per his 2026-05-13 brief. The repo exists; he just needs to seed it with his working content (replacing/augmenting the template baseline). After that, his `~/janus/prime-radiant/ai-office/` should be the canonical source.

### For a future Claude session

If picking up from here:
1. Read this HANDOVER.md
2. Read `SKILL.md` for the orchestration model
3. Read `README.md` for the architecture overview
4. Run `~/Documents/janus-brain-bootstrap/install.sh --check` to verify install state
5. Run `git -C ~/Documents/janus-brain-bootstrap log --oneline -15` to see recent history
6. Ask the user what they want to do next.

Likely "what's next" topics:
- **The 19 broken wikilinks**: build a stub-creation pass that runs after Phase 6 to auto-create empty entity stubs for unresolved `[[wikilink]]` targets. ~30 min.
- **Schema-version CI**: GitHub Action that compares `TEMPLATE-VERSION` between dept template and personal template; fails if they don't match a known compatibility table. ~45 min.
- **Andrew's actual enrollment**: walk him through it (or remotely diagnose if he hits anything).
- **Per-tool extensibility** ([[linear|Linear]], [[hubspot|HubSpot]], Figma, Asana ingest) — earlier we discussed a hybrid where MCP-mediated tools get pulled during `/janus-brain sync`. Foundation is there; just needs MCP-call additions to Phase 3. ~half-day.
- **Promotion gate** (curator-side workflow that reviews dept `inbox/` and promotes to canonical) — separate skill or extension. Worth building once 3+ contributors are federating to a dept vault.
- **Cross-vault search / unified query** — once 5+ depts have repos, build a query layer that searches across them. Not urgent.

---

## 9. User preferences captured this session

These should be respected in future sessions:

| Preference | Source |
| --- | --- |
| **Substrate is Git, not Drive** | Michael's 2026-05-13 brief |
| **Personal vault is a separate private repo per employee** (not merged into dept repo) | User explicit, 2026-05-13 |
| **Both Code and Cowork tab support** | User explicit (chose "both" when asked) |
| **No API keys for automation** — auto-sync uses launchd + AppleScript + Claude Desktop's existing MCP | User explicit |
| **Full content conversion in Phase 4.5**, not summaries (pdftotext, pandoc, tesseract, pandas) | User explicit |
| **Phase 4.5 must prompt user** before kicking off (extract all / text-only / docs-only / skip) | User explicit |
| **Image handling: both OCR + vision** (tesseract first, vision model for visual-heavy) | User explicit |
| **Federation dedup**: skip identical pushes, enrich on overlap | User explicit, this conversation |
| **Subagent does FULL extraction from raw transcript**, not delegate to Fireflies' shallow AI output | User explicit, 2026-05-13 (with strong opinion: "we don't trust fireflies summary, tasks, action items extractions, they're lame and not proper") |
| **No "Generated with [[claude-code|Claude Code]]" branding** in PRs/commits | From CLAUDE.md memory |
| **Authorization is per-action**, not blanket | From CLAUDE.md base instructions |

---

## 10. How to verify current state from a fresh session

Bash sequence that surfaces everything important:

```bash
# 1. Installer state
~/Documents/janus-brain-bootstrap/install.sh --check

# 2. Repo state
git -C ~/Documents/janus-brain-bootstrap log --oneline -10
git -C ~/Documents/janus-brain-bootstrap status

# 3. Local vault clones
for d in ~/janus/prime-radiant/*/; do
  name=$(basename "$d")
  if [[ -d "$d/.git" ]]; then
    files=$(find "$d" -type f -not -path "*/.git/*" | wc -l | tr -d ' ')
    branch=$(git -C "$d" branch --show-current)
    sync=$(git -C "$d" status --porcelain | wc -l | tr -d ' ')
    echo "✓ $name: $files files, $branch, $sync uncommitted"
  fi
done

# 4. GitHub repos
for repo in \
  janus-prime-radiant-template \
  janus-prime-radiant-personal-template \
  janus-prime-radiant-ai-office \
  janus-prime-radiant-personal-jehad-altoutou; do
  gh repo view Janusd-io/$repo >/dev/null 2>&1 && echo "✓ Janusd-io/$repo" || echo "✗ $repo"
done

# 5. Federation status (in AIO inbox)
ls ~/janus/prime-radiant/ai-office/inbox/ 2>/dev/null | grep "^personal-jehad-altoutou-" | wc -l
# expect: 121 (or higher if more sync runs happened)

# 6. Lint
python3 ~/.claude/skills/janus-brain/scripts/lint-vault.py \
  --vault ~/janus/prime-radiant/personal --quiet
# expect: errors=~19 warnings=~34 (or improved if user has fixed broken wikilinks)

# 7. Phase 4.5 done?
[[ -f ~/janus/prime-radiant/personal/.state/extract-content.json ]] && \
  echo "✓ Phase 4.5 has run" || echo "✗ Phase 4.5 not yet run"

# 8. Auto-sync schedule
~/Documents/janus-brain-bootstrap/install.sh --auto-sync-status
```

---

## 11. File map

```text
janus-brain-bootstrap/
├── HANDOVER.md                                ← THIS FILE
├── README.md                                  ← architecture overview
├── ENROLLMENT.md                              ← copy-paste guide for any new Janus employee
├── install.sh                                 ← idempotent installer with subcommands
├── LICENSE.md
└── skills/
    └── janus-brain/
        ├── SKILL.md                           ← Phase 0-8 orchestration prompt (read this first)
        ├── README.md
        ├── INSTALL.md
        ├── config/
        │   ├── departments.yaml               ← locked dept vocabulary + people roster (Jehad, Michael, Andrew, etc.)
        │   ├── exclude-patterns.txt           ← privacy filter: basename patterns (credentials, etc.)
        │   ├── exclude-paths.txt              ← privacy filter: path prefixes
        │   ├── include-extensions.txt
        │   └── user-exclude.txt               ← per-user privacy additions
        ├── scripts/
        │   ├── discover.sh                    ← vault detection + scaffold helper
        │   ├── walk-and-filter.py             ← Phase 4: laptop walker
        │   ├── extract-content.py             ← Phase 4.5: full content conversion (NEW)
        │   ├── extract-content.sh             ← wrapper for Phase 4.5
        │   ├── apply-meeting-digests.py       ← Phase 3.5 applier
        │   ├── ingest-to-radiant.py           ← Phase 6 applier
        │   ├── bootstrap-personal-vault.sh    ← Phase 2: per-user repo creation (NEW; clones personal-template)
        │   ├── bootstrap-dept-vault.sh        ← Phase 7: dept repo creation (clones dept template if missing)
        │   ├── write-sync-config.sh           ← writes ~/.config/janus-brain/sync.conf
        │   ├── federate-to-department.py      ← personal → dept inbox, with dedup
        │   ├── federate-to-department.sh      ← wrapper
        │   ├── refresh-from-aio.sh            ← thin `git pull --rebase` on AIO clone
        │   ├── auto-sync.sh                   ← NEW: launchd-fired daily Claude Desktop trigger
        │   ├── com.janus.brain-sync.plist.template  ← NEW: launchd template
        │   ├── lint-vault.py                  ← schema + integrity linter
        │   ├── lint-vault.sh                  ← wrapper
        │   ├── fetch-fireflies.py             ← REST fallback (rarely needed; MCP preferred)
        │   ├── nightly-sync.sh                ← legacy entrypoint (kept for backward compat)
        │   └── install-cron.sh                ← legacy (retired model)
        ├── templates/
        │   ├── personal-claude-md.md          ← personal-tier CLAUDE.md template
        │   ├── personal-self-page.md
        │   ├── entity-internal.md
        │   ├── entity-vendor.md
        │   ├── decision.md
        │   ├── lesson.md
        │   ├── pulse.md
        │   └── meeting-source.md              ← updated for Phase 3.5 digest+transcript shape
        ├── prompts/
        │   ├── enrichment-subagent.md         ← Phase 5 generic enrichment
        │   └── meeting-parser-subagent.md     ← Phase 3.5 meeting parser (full extraction, not Fireflies pass-through)
        ├── references/
        │   ├── privacy-filter.md
        │   └── prime-radiant-personal.md
        └── briefs/
            └── personal-prime-radiant-proposal.md   ← original proposal sent to Michael
```

---

## 12. Architectural decisions (the why, captured for future context)

1. **Git over Drive** — Drive's stream-on-demand sync caused Cowork mount failures (2026-05-12 incident). Cross-Workspace identity (`.com` vs `.io`) was also broken. Git solved both structurally. Per Michael's 2026-05-13 brief.
2. **One repo per Prime Radiant instance** — symmetric, scalable, GitHub Teams = ACL boundary. Dept + personal use the same shape.
3. **Templates seed every instance** — schema changes propagate via template repo bumps, not code releases.
4. **Federation = git commit/push to sibling clone's inbox/** — not wholesale mirror (which was the failed Drive-era pattern). Curator-mediated promotion.
5. **No cron for sync** — Obsidian Git plugin handles continuous edit sync. Auto-sync (launchd) is only for triggering /janus-brain sync (ingest of new content). Decoupled cleanly.
6. **Subagent does its own extraction from raw transcript** — Fireflies' built-in AI output is shallow and anonymizes speakers. Subagent uses real speaker attribution from per-sentence prefixes.
7. **Phase 4.5 is gated, not silent** — content extraction can be substantial. User picks scope explicitly.
8. **Federation dedup uses normalised hash** — strips volatile frontmatter (timestamps, captured_by) before comparing. Two contributors who ingest the same meeting produce hash match → skip.
9. **No API keys for automation** — auto-sync uses launchd + AppleScript + Claude Desktop's existing MCP. User's explicit constraint.
10. **macOS only initially** — launchd + AppleScript + macOS paths. Linux support deferred. Tesseract + pandoc are cross-platform but the wrapper layer is Mac-first.

---

## 13. Quick reference — the user's most common commands

| Goal | Command |
| --- | --- |
| Verify everything is installed | `~/Documents/janus-brain-bootstrap/install.sh --check` |
| Update the skill to latest main | `cd ~/Documents/janus-brain-bootstrap && git pull && ./install.sh` |
| Run the full enrollment / sync | In Claude Desktop Code tab: `/janus-brain` or `/janus-brain sync` |
| Federate tagged items manually | `~/.claude/skills/janus-brain/scripts/federate-to-department.sh` |
| Refresh AIO clone | `~/.claude/skills/janus-brain/scripts/refresh-from-aio.sh` |
| Lint personal vault | `~/.claude/skills/janus-brain/scripts/lint-vault.sh` |
| Schedule auto-sync | `~/Documents/janus-brain-bootstrap/install.sh --install-auto-sync --time 07:30` |
| Check auto-sync status | `~/Documents/janus-brain-bootstrap/install.sh --auto-sync-status` |
| Stop auto-sync | `~/Documents/janus-brain-bootstrap/install.sh --uninstall-auto-sync` |
| Manually trigger auto-sync now | `~/.claude/skills/janus-brain/scripts/auto-sync.sh --force` |
| Uninstall everything (keeps vaults) | `~/Documents/janus-brain-bootstrap/install.sh --uninstall` |

---

## 14. Contact

- **Jehad Altoutou** (this repo, installer, personal-tier programme) — `jehada@janusd.io`
- **Michael Bruck** (Prime Radiant programme owner, dept-tier template, schema) — `michael-bruck@janusd.io`
- **[[bonaventure-wong|Bonaventure Wong]]** (CEO, org admin) — for GitHub Teams / repo permission escalations
- **[[simon-tarskih|Simon Tarskih]]** (ISO Lead, IMS programme) — for compliance + audit-chain concerns

---

## 15. Architecture rewrite 2026-05-14

Signed-off in [`REWRITE-SPEC.md`](REWRITE-SPEC.md). Supersedes the two-vault model described earlier in this document.

**Headline change.** Each employee's local Obsidian vault is now a **single clone** of their department's shared GitHub repo (`Janusd-io/janus-prime-radiant-<dept>`) at `~/janus/prime-radiant/`. Per-person content lives at `people/<slug>/` inside that single repo. Multiple teammates push to the same dept repo. The private personal repo (`Janusd-io/janus-prime-radiant-personal-<slug>`) and all federation machinery are deleted. A future read-only "CEO brain" skill will federate across dept repos — out of scope for this rewrite.

**Two other big changes shipped at the same time:**

1. **Meeting notes follow the `/standup` skill's Meeting Intelligence Digest schema.** Sections: Summary, Decisions, Action items, 🎯 This week, 🏔️ Long horizon, Findings, Open questions, Blockers, Tool mentions, Topics, Related. The raw transcript is split out to a sibling `<meeting>.transcript.md` file (wikilinked from the note) — never dumped inline. Action items are formatted per the user's task tracker (Linear / Monday native suffixes; Asana / Notion / none render plain).
2. **Sensitivity classifier added to Phase 5 enrichment.** Every source carries `sensitivity` (`dept` | `self` | `confidential`) + `sensitivity_confidence` (0.0–1.0). The applier moves `self` / `confidential` items (or `dept` with confidence < 0.7) to `people/<slug>/private/` (gitignored). Sub-0.7 items are also logged to `people/<slug>/.review-queue.md` for human review.

**Files deleted:**

- `skills/janus-brain/scripts/bootstrap-personal-vault.sh`
- `skills/janus-brain/scripts/federate-to-department.sh` / `.py`
- `skills/janus-brain/scripts/refresh-from-aio.sh`
- `skills/janus-brain/scripts/write-sync-config.sh`
- All references to `~/.config/janus-brain/sync.conf`

**Files added:**

- `skills/janus-brain/scripts/scaffold-person-subtree.sh` — creates `people/<slug>/` inside the dept vault with `.config.yaml`, `CLAUDE.md`, `self.md`, `sources/`, `meetings/`, `private/`, `.review-queue.md`.
- `skills/janus-brain/templates/dept-gitignore` — the canonical dept-vault `.gitignore` (excludes `people/*/private/`, `*.confidential.md`, `.state/`, etc.). Dropped at the vault root on first bootstrap.

**Files rewritten:**

- `skills/janus-brain/SKILL.md` — full single-vault flow.
- `skills/janus-brain/scripts/bootstrap-dept-vault.sh` — local clone is `$VAULT_ROOT` directly (not `$VAULT_ROOT/<dept>`). Refuses if `$VAULT_ROOT/.git` has a different remote.
- `skills/janus-brain/scripts/apply-meeting-digests.py` — `PARSER_VERSION=2`. Splits transcript to sibling file. Renders standup-schema sections. Reads `people/<slug>/.config.yaml` to format action items per task tracker. Routes to single-vault paths (`decisions/`, `projects/`, `vendors/`, `concepts/`, `people/<slug>.md`).
- `skills/janus-brain/scripts/lint-vault.py` — adds single-vault folder vocab; flags legacy `entities/*` and `inbox/` as deprecated. Adds `transcript` to structural types. Adds `pm` to LOCKED_DEPTS.
- `skills/janus-brain/prompts/meeting-parser-subagent.md` — v4 schema with `this_week`, `long_horizon`, `findings`, `open_questions`, `blockers`, `tool_mentions` (each with verbatim `evidence_quote` + discipline blocks).
- `skills/janus-brain/prompts/enrichment-subagent.md` — adds Step 4.5 sensitivity classifier.
- `skills/janus-brain/templates/meeting-source.md` — standup-schema scaffolding + transcript wikilink.
- `skills/janus-brain/templates/personal-claude-md.md` — header reframed as the per-person rulebook inside a shared dept vault.
- `skills/janus-brain/config/departments.yaml` — replaces `instance_path` (Drive era) with `repo` (`Janusd-io/janus-prime-radiant-<slug>`). Adds `iso` and `pm` depts.
- `install.sh` — drops legacy required-files. `--check` reports the single-vault path, remote URL, per-person subtrees, and warns if the legacy two-vault layout is detected.
- `README.md`, `ENROLLMENT.md`, `skills/janus-brain/README.md`, `skills/janus-brain/INSTALL.md` — single-vault language end-to-end.

**Migration (for existing Jehad / Andrew / Theresa vaults):**

1. Archive `Janusd-io/janus-prime-radiant-personal-<slug>` on GitHub.
2. `rm -rf ~/janus/prime-radiant/personal ~/janus/prime-radiant/ai-office` (or whichever pair you have locally).
3. Re-run `/janus-brain`. It clones the dept repo into `~/janus/prime-radiant/` and scaffolds `people/<slug>/`.

---

*End of handover. Save and read this file at the start of any new session to orient quickly.*
