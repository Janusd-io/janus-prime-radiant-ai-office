---
type: source
source_type: laptop
title: Janus Brain Bootstrap — README
slug: readme-12
created: 2026-05-14
captured_by: jehad-altoutou
audience: personal
original_path: /Users/jehad/Documents/janus-brain-bootstrap/skills/janus-brain/README.md
original_size: 2923
original_ext: .md
category: notes
extracted_with: text-copy
extracted_at: "2026-05-14T09:51:46Z"
sensitivity: dept
sensitivity_confidence: 0.95
sensitivity_reason: "Public skill README shipped in the public-ish bootstrap repo."
project: janus-brain-bootstrap

---
<!-- jb:project-callout -->
> Part of [[janus-brain-bootstrap|Janus Brain Bootstrap]] — automatically linked by /janus-brain.


# README

> Part of [[janus-brain-bootstrap|Janus Brain Bootstrap]] — captured by /janus-brain.

_Extracted from `Documents/janus-brain-bootstrap/skills/janus-brain/README.md` on 2026-05-14._

# /janus-brain

The one-and-only skill for Janus's [[prime-radiant|Prime Radiant]] programme — single-vault model (rewrite 2026-05-14).

**Trigger:** `/janus-brain` in Claude Desktop

**What it does:** clones your department's shared Prime Radiant [[github|GitHub]] repo (`Janusd-io/janus-prime-radiant-<dept>`) as your single [[obsidian|Obsidian]] vault at `~/janus/prime-radiant/`, scaffolds your `people/<your-slug>/` subtree inside it, pulls your Notion + [[fireflies|Fireflies]] + laptop content via Claude Desktop's MCP connectors, classifies sensitivity (`dept` / `self` / `confidential`) and routes private items to a gitignored `private/`, then commits + pushes to the shared dept repo. Multiple teammates contribute to the same dept repo.

**Subcommands** (for repeat use after first run): `sync`, `status`, `exclude`, `reset`. See `SKILL.md`.

## Install (one time)

```bash
gh repo clone Janusd-io/janus-brain-bootstrap ~/Documents/janus-brain-bootstrap
~/Documents/janus-brain-bootstrap/install.sh
```

Restart Claude Desktop.

## Run (one time, takes ~10–20 min)

In Claude Desktop:

```text
/janus-brain
```

The skill walks through Phases 0-8 (pre-flight → identity + task tracker → bootstrap + scaffold → cloud pulls → meeting parser → laptop walk → extraction → enrichment + sensitivity → apply + route → commit + push → lint + open). It pauses for two confirmation prompts (your name/dept + your task tracker, then the scope of the laptop scan) and otherwise runs end-to-end.

## After first run

Sync runs continuously via the [[obsidian-git|Obsidian Git]] community plugin (auto-pull + auto-commit-and-push every 5 min). No cron required. See `ENROLLMENT.md` step 4 for the one-time plugin setup.

To pull yesterday's Fireflies meetings or fresh Notion entries on demand:

```text
/janus-brain sync
```

To check the state:

```text
/janus-brain status
```

## Prerequisites

| Requirement | How to verify |
| --- | --- |
| Claude Desktop installed | You're reading this in Claude Desktop |
| `gh` CLI authenticated to `Janusd-io` | `gh auth status` |
| Fireflies MCP connected | Settings → Connectors → Fireflies (signed in) |
| Notion MCP connected | Settings → Connectors → Notion (signed in) |
| Obsidian.app | Installed at `/Applications/Obsidian.app` |

The installer verifies these at the bottom of `install.sh --check`.

## Privacy

- 5-layer exclusion filter applied to every laptop file (`~/.claude/skills/janus-brain/references/privacy-filter.md`)
- Phase 5 enrichment subagent classifies every source as `dept` / `self` / `confidential` with a confidence score
- Anything `self`, `confidential`, or `dept`-with-confidence-<0.7 is routed to `people/<slug>/private/`, which is gitignored
- Low-confidence classifications are logged to `people/<slug>/.review-queue.md` for human review
- The dept repo is private at the GitHub-permission level — only dept members and org admins can read it

## Support

Questions: jehada@janusd.io
