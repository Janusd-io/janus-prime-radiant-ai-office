---
type: source
source_type: laptop
title: README
slug: readme-11
created: 2026-05-14
captured_by: jehad-altoutou
audience: personal
original_path: /Users/jehad/Documents/janus-brain-bootstrap/README.md
original_size: 7954
original_ext: .md
category: notes
extracted_with: text-copy
extracted_at: "2026-05-14T09:51:46Z"
sensitivity: dept
sensitivity_confidence: 0.95
sensitivity_reason: "Public top-level README for the bootstrap repo."
project: janus-brain-bootstrap

---
<!-- jb:project-callout -->
> Part of [[janus-brain-bootstrap|Janus Brain Bootstrap]] — automatically linked by /janus-brain.


# README

> Part of [[janus-brain-bootstrap|Janus Brain Bootstrap]] — captured by /janus-brain.

_Extracted from `Documents/janus-brain-bootstrap/README.md` on 2026-05-14._

# janus-brain-bootstrap

Installer + source for the **`/janus-brain`** [[claude-code|Claude Code]] skill — the single-vault [[prime-radiant|Prime Radiant]] onboarding pipeline for Janus employees.

> **2026-05-14 architecture rewrite.** This skill now follows the **single-vault model** described in [`REWRITE-SPEC.md`](REWRITE-SPEC.md). One [[github|GitHub]] repo per department; every employee in that dept clones it as their single [[obsidian|Obsidian]] vault and contributes to it. The earlier two-vault model (private personal repo + sibling dept repo + [[federation|federation]]) has been retired. See also [HANDOVER.md §15](HANDOVER.md).

---

## 60-second mental model

- **Substrate:** Git on GitHub under the `Janusd-io` org.
- **One repo per department:** `Janusd-io/janus-prime-radiant-<dept>` (e.g. `…-ai-office`, `…-marketing`, `…-iso`).
- **Every employee in the dept clones that repo once** to `~/janus/prime-radiant/` — that's their Obsidian vault.
- **Per-person content** lives inside the shared vault at `people/<person-slug>/` with subfolders `sources/`, `meetings/`, `private/`.
- **Dept-shared content** (decisions, projects, processes, vendors, concepts, top-level people-stubs) lives at the vault root.
- **`private/` and `.review-queue.md` are gitignored** — they never reach GitHub. The Phase 5 enrichment subagent classifies each source as `dept` | `self` | `confidential`; private items are routed there automatically.
- **Sync** runs continuously via the [[obsidian-git|Obsidian Git]] community plugin (auto-pull + auto-commit-and-push every 5 min). No cron.

```text
~/janus/prime-radiant/                          ← single clone of dept repo
├── decisions/                                  ← dept-shared
├── projects/
├── processes/
├── vendors/
├── concepts/
├── people/
│   ├── <other-teammates>.md                   ← stubs for non-vault-owner people
│   └── <your-slug>/
│       ├── .config.yaml                       ← task_tracker, primary_dept, …
│       ├── CLAUDE.md                          ← per-person rulebook
│       ├── self.md
│       ├── sources/                           ← dept-visible
│       ├── meetings/                          ← dept-visible (notes + sibling transcripts)
│       ├── private/                           ← gitignored
│       └── .review-queue.md                   ← gitignored; low-confidence items
└── .gitignore                                  ← from templates/dept-gitignore
```

## What `/janus-brain` does

| Phase | Action |
| --- | --- |
| **0. Pre-flight** | Tools, MCP connectors, vault-root path hygiene |
| **1. Identity + task tracker** | Detect git user, look up in `departments.yaml`, ask which task tracker ([[linear|Linear]] / Monday / Asana / Notion tasks / none / other) |
| **2. Bootstrap + scaffold** | `bootstrap-dept-vault.sh` clones (or creates from template) the dept repo as the single vault; `scaffold-person-subtree.sh` creates `people/<slug>/` |
| **3. Cloud pulls** | Notion → `people/<slug>/sources/notion/`; [[fireflies|Fireflies]] meetings → `people/<slug>/meetings/` (note + sibling `.transcript.md`) |
| **3.5. Meeting parser** | One subagent per meeting, parallel. Produces standup-schema digest (Summary · Decisions · Action items · 🎯 This week · 🏔️ Long horizon · Findings · Open questions · Blockers · Tool mentions · Topics · Related). Action items rendered per the user's `task_tracker`. Raw transcript stays in the sibling file, never inlined. |
| **4. Laptop walk** | Manifest of in-scope files |
| **4.5. Content extraction** | pdftotext / pandoc / pandas / tesseract → markdown |
| **5. Enrichment + sensitivity** | Parallel subagents enrich + classify each source as `dept` / `self` / `confidential` (with confidence) |
| **6. Apply + route** | Decisions / projects / concepts to vault root; sensitive items moved to `people/<slug>/private/`; low-confidence logged to `.review-queue.md` |
| **7. Commit + push** | `git add && commit && push` from the single vault to the dept repo. **No federation.** |
| **8. Lint + open** | Vault lint summary + open Obsidian |

## Action item formatting

The user's task tracker (asked in Phase 1, stored in `people/<slug>/.config.yaml`) drives how action items render:

| Tracker | Output |
| --- | --- |
| `linear` | `- [ ] @assignee text (due: X) — file in Linear AIP` |
| `monday` | `- [ ] @assignee text (due: X) — Monday` |
| `asana` / `notion` / `none` / `other` | `- [ ] @assignee text (due: X)` (plain checkbox; native syntax for Asana/Notion is a v2 TODO) |

## Sensitivity routing

Every source that lands in the vault carries `sensitivity` and `sensitivity_confidence` in frontmatter. The applier moves anything classified `self` or `confidential` — or `dept` below 0.7 confidence — to `people/<slug>/private/`. Items below 0.7 confidence are also appended to `people/<slug>/.review-queue.md` so the user can confirm or promote them.

## Install

```bash
gh repo clone Janusd-io/janus-brain-bootstrap ~/Documents/janus-brain-bootstrap
~/Documents/janus-brain-bootstrap/install.sh
# Restart Claude Desktop
# Type /janus-brain in the Code or [[cowork|Cowork]] tab
```

Verify: `./install.sh --check`. Uninstall: `./install.sh --uninstall` (keeps the vault).

## Subcommands

| Command | Purpose |
| --- | --- |
| `/janus-brain` | First-run autopilot (all 8 phases) |
| `/janus-brain sync` | Pull yesterday's Notion + Fireflies, re-enrich new laptop files, push |
| `/janus-brain status` | Health check (vault size, last sync, review-queue length) |
| `/janus-brain exclude <pattern>` | Add a pattern to the privacy filter |
| `/janus-brain reset` | Wipe local state metadata (keeps the vault) |

## Repository layout

```text
janus-brain-bootstrap/
├── README.md                        ← this file
├── ENROLLMENT.md                    ← step-by-step user-facing flow
├── REWRITE-SPEC.md                  ← 2026-05-14 architecture spec (authoritative)
├── HANDOVER.md                      ← programme context, including the rewrite
├── install.sh                       ← installer / --check / --uninstall / --install-auto-sync
└── skills/janus-brain/
    ├── SKILL.md                     ← orchestration (read by Claude Desktop)
    ├── config/departments.yaml      ← locked dept vocab + person roster
    ├── prompts/
    │   ├── meeting-parser-subagent.md
    │   └── enrichment-subagent.md
    ├── scripts/
    │   ├── bootstrap-dept-vault.sh        ← clone or create-from-template the dept repo
    │   ├── scaffold-person-subtree.sh     ← create people/<slug>/ subtree (new)
    │   ├── apply-meeting-digests.py       ← deterministic applier (transcript-sibling files)
    │   ├── fetch-fireflies.py
    │   ├── walk-and-filter.py
    │   ├── extract-content.py / .sh
    │   ├── lint-vault.py / .sh
    │   └── auto-sync.sh + plist template
    └── templates/
        ├── personal-claude-md.md          ← lands as people/<slug>/CLAUDE.md
        ├── personal-self-page.md          ← lands as people/<slug>/self.md
        ├── meeting-source.md
        ├── dept-gitignore                 ← new; keeps people/*/private/ out of git
        └── decision.md / lesson.md / pulse.md / entity-*.md
```

## What was deleted in the 2026-05-14 rewrite

- `scripts/bootstrap-personal-vault.sh`
- `scripts/federate-to-department.sh` / `.py`
- `scripts/refresh-from-aio.sh`
- `scripts/write-sync-config.sh`
- All references to `~/.config/janus-brain/sync.conf`
- The `Janusd-io/janus-prime-radiant-personal-<slug>` repo family (existing instances should be archived)
- Federation-related subcommands (`/janus-brain federate`)

## Owner / contact

[[jehad-altoutou|Jehad Altoutou]] — AI Operations Engineer · jehada@janusd.io. Programme owner: [[michael-bruck|Michael Bruck]].
