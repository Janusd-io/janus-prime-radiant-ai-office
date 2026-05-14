---
type: source
source_type: laptop
title: ENROLLMENT
slug: enrollment
created: 2026-05-14
captured_by: jehad-altoutou
audience: personal
original_path: /Users/jehad/Documents/janus-brain-bootstrap/ENROLLMENT.md
original_size: 8573
original_ext: .md
category: notes
extracted_with: text-copy
extracted_at: "2026-05-14T09:51:46Z"
sensitivity: dept
sensitivity_confidence: 0.95
sensitivity_reason: "Public-internal onboarding guide shipped in the bootstrap repo."
project: janus-brain-bootstrap

---
<!-- jb:project-callout -->
> Part of [[janus-brain-bootstrap|Janus Brain Bootstrap]] — automatically linked by /janus-brain.


# ENROLLMENT

> Part of [[janus-brain-bootstrap|Janus Brain Bootstrap]] — captured by /janus-brain.

_Extracted from `Documents/janus-brain-bootstrap/ENROLLMENT.md` on 2026-05-14._

# Enrollment — onboarding a Janus employee into the [[prime-radiant|Prime Radiant]] programme

This guide walks one employee from zero to a working Janus brain: a **single [[github|GitHub]]-backed [[obsidian|Obsidian]] vault** at `~/janus/prime-radiant/` — a clone of their department's shared Prime Radiant repo — populated with their Notion + [[fireflies|Fireflies]] + selected laptop content. Per-person content lives in `people/<your-slug>/` inside that shared repo. Multiple teammates contribute to the same dept repo over time.

> **2026-05-14 rewrite.** This document describes the single-vault model from [`REWRITE-SPEC.md`](REWRITE-SPEC.md). The earlier two-vault model (separate private personal repo + dept clone + [[federation|federation]]) has been retired. See [HANDOVER.md §15](HANDOVER.md) for the migration story.

**Time:** ~15 minutes of mostly watching. Two confirmation prompts (Identity + Task tracker).

**Substrate:** Git on GitHub under the `Janusd-io` org. Each dept gets one private repo (`Janusd-io/janus-prime-radiant-<dept>`), and every employee in that dept clones it as their single Obsidian vault. Sync runs continuously via the [[obsidian-git|Obsidian Git]] plugin — no cron jobs.

---

## What you'll end up with

```text
~/janus/prime-radiant/                          ← single clone of your dept repo
├── decisions/, projects/, processes/, vendors/, concepts/, people/   ← dept-shared
├── people/<your-slug>/
│   ├── .config.yaml          ← task_tracker, primary_dept, …
│   ├── CLAUDE.md             ← rules for your subtree
│   ├── self.md
│   ├── sources/              ← dept-visible (Notion entries, laptop docs)
│   ├── meetings/             ← dept-visible (notes + sibling .transcript.md)
│   ├── private/              ← GITIGNORED (sensitivity=self|confidential)
│   └── .review-queue.md      ← GITIGNORED (low-confidence sensitivity items)
└── .gitignore
```

---

## 1. Prerequisites (~2 min)

1. **Claude Desktop** is installed and has the Code (or [[cowork|Cowork]]) tab. Fireflies and Notion connectors are connected (Settings → Connectors).
2. **`gh` CLI** is installed and authenticated to GitHub.
   ```bash
   brew install gh           # if missing
   gh auth login              # GitHub.com, HTTPS, web browser
   gh auth status              # confirm
   ```
   Your GitHub account must be a member of the `Janusd-io` org with access to your dept's Prime Radiant repo. If not, ping Jehad or Michael.
3. **Obsidian.app** is installed (free download from <https://obsidian.md>).

## 2. Install the skill (~1 min)

```bash
gh repo clone Janusd-io/janus-brain-bootstrap ~/Documents/janus-brain-bootstrap
~/Documents/janus-brain-bootstrap/install.sh
```

Restart Claude Desktop after install so the new skill loads.

Verify anytime: `~/Documents/janus-brain-bootstrap/install.sh --check`.

## 3. Run `/janus-brain` (~10–20 min)

Open Claude Desktop → Code or Cowork tab → New chat → type `/janus-brain`.

The skill autopilots through 8 phases:

| Phase | What happens |
| --- | --- |
| **0. Pre-flight** | Verifies tools, MCP connectors, vault-root hygiene |
| **1. Identity + task tracker** | Asks you to confirm your name + dept, then asks which task tracker ([[linear|Linear]] / Monday / Asana / Notion tasks / none / other) for action-item formatting |
| **2. Bootstrap + scaffold** | `bootstrap-dept-vault.sh` clones (or creates from template) `Janusd-io/janus-prime-radiant-<your-dept>` to `~/janus/prime-radiant/`. `scaffold-person-subtree.sh` creates your `people/<slug>/` subtree |
| **3. Cloud pulls** | Notion → `people/<slug>/sources/notion/`. Fireflies meetings → `people/<slug>/meetings/` (note + sibling `.transcript.md`) |
| **3.5. Meeting parser** | One Claude subagent per meeting, in parallel. Produces a standup-schema digest (Summary · Decisions · Action items · 🎯 This week · 🏔️ Long horizon · Findings · Open questions · Blockers · Tool mentions · Topics · Related). Raw transcript is split out to the sibling file and linked from the note. Action items are formatted per your `task_tracker` |
| **4. Laptop walk** | Walks `$HOME` minus hidden/Library/excluded paths. Asks if scope needs narrowing |
| **4.5. Content extraction** | pdftotext / pandoc / pandas / tesseract → markdown. You pick (a) everything / (b) text-only / (c) documents only / (d) skip |
| **5. Enrichment + sensitivity** | Parallel Claude subagents enrich each source and classify sensitivity (`dept` / `self` / `confidential`) with a confidence score |
| **6. Apply + sensitivity routing** | Decisions / projects / concepts written to vault root. Sources scored `self`, `confidential`, or `dept` <0.7 confidence are moved to `people/<slug>/private/` (gitignored). Low-confidence items also logged to `.review-queue.md` |
| **7. Commit + push** | `git add && commit && push` from the single vault to the dept repo |
| **8. Lint + open** | Vault lint summary + opens Obsidian |

**Total: ~10–20 minutes.** You'll see the final summary block; Obsidian opens automatically.

## 4. Enable Obsidian Git plugin (one-time, ~2 min)

The skill can't install Obsidian community plugins for you (Obsidian gates that behind its UI):

1. Open `~/janus/prime-radiant/` in Obsidian (the vault switcher should already show it).
2. Settings → Community plugins → Turn on (one-time per vault; accept disclaimer).
3. Browse → search **Git** → install **Git by vinzent03** → Enable.
4. Settings → Git → set:
   - Auto pull interval (minutes): **5**
   - Auto pull on startup: **on**
   - Auto backup interval (minutes): **5**
   - Commit message template: `vault backup: {{date}} {{hostname}}`
   - Pull strategy: **rebase**

That's it — your vault now pulls teammates' work every 5 min and pushes your own edits every 5 min while Obsidian is open.

## 5. Daily use

| Command | Purpose |
| --- | --- |
| `/janus-brain sync` | Pull yesterday's Notion + Fireflies, re-enrich any new laptop files, push |
| `/janus-brain status` | Health check (vault size, last sync, review-queue length) |
| `/janus-brain exclude <pattern>` | Add a pattern to your privacy filter |
| `/janus-brain reset` | Wipe local state metadata (keeps the vault) |

## 6. Sensitivity routing — what stays private

The Phase 5 classifier scores every source as one of:

- **`dept`** (default) → stays in `people/<slug>/sources/` and `people/<slug>/meetings/`, pushed to the dept repo.
- **`self`** → personal context (1:1 notes, journal entries) → moved to `people/<slug>/private/` (gitignored).
- **`confidential`** → credentials, HR/salary, legal, health, family, personal finance → moved to `people/<slug>/private/` (gitignored).

Anything scored under 0.7 confidence is also appended to `people/<slug>/.review-queue.md` (also gitignored) so you can confirm or move the file by hand.

You can also explicitly mark a file `sensitivity: self` or `sensitivity: confidential` in its frontmatter; the next sync will re-route it.

## 7. Troubleshooting

| Symptom | Fix |
| --- | --- |
| `gh auth login` fails | Make sure you're using a personal-access GitHub account with `Janusd-io` membership |
| `bootstrap-dept-vault.sh: REFUSED — $LOCAL is already a git repo with a different remote` | You have an old vault at `~/janus/prime-radiant`. Move it (`mv ~/janus/prime-radiant ~/janus/prime-radiant.bak`) and re-run |
| Vault root inside iCloud / Drive / Dropbox | The bootstrap refuses. Move your `~/janus/` outside those sync layers |
| Fireflies / Notion MCP shows zero results | Settings → Connectors in Claude Desktop; re-auth the connector |
| Subagent chunk fails | Re-dispatch that specific chunk; idempotent |
| `git push` fails | `git -C ~/janus/prime-radiant remote -v` and `gh auth status`; surface the error |

## 8. Migrating from the old two-vault layout

If you previously had `~/janus/prime-radiant/personal/` + `~/janus/prime-radiant/ai-office/`:

1. **Archive** your old personal repo on GitHub (`Janusd-io/janus-prime-radiant-personal-<slug>`).
2. **Delete** both local clones:
   ```bash
   rm -rf ~/janus/prime-radiant/personal ~/janus/prime-radiant/ai-office
   ```
3. **Re-run** `/janus-brain`. It will clone the dept repo into `~/janus/prime-radiant/` and scaffold your `people/<slug>/`.

Any content from the old personal vault you still want is recoverable from your GitHub archive — copy and re-file into the new subtree by hand.

## 9. Contact

- **Programme questions, dept-vocabulary changes** → [[michael-bruck|Michael Bruck]]
- **Installer / sync / parser issues** → [[jehad-altoutou|Jehad Altoutou]] (`jehada@janusd.io`)
