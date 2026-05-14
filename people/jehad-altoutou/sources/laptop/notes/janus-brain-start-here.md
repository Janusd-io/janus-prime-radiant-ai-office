---
type: source
source_type: laptop
title: Janus Brain - Start Here
slug: janus-brain-start-here
created: 2026-05-13
captured_by: jehad-altoutou
audience: personal
original_path: /Users/jehad/Desktop/Janus Brain - Start Here.md
original_size: 1848
original_ext: .md
category: notes
extracted_with: text-copy
extracted_at: "2026-05-14T09:51:43Z"
sensitivity: dept
sensitivity_confidence: 0.92
sensitivity_reason: "Public welcome doc for /janus-brain skill — dept-shareable onboarding pointer."
---

# Janus Brain - Start Here

_Extracted from `Desktop/Janus Brain - Start Here.md` on 2026-05-14._

# Janus Brain — Start Here

The `/janus-brain` skill is now installed in your Claude Desktop.

## What it does

Scans your laptop (Documents, Desktop, project folders), pulls your Notion entries + [[fireflies|Fireflies]] meetings via the MCP connectors you have set up in Claude Desktop, and turns everything into a Personal [[prime-radiant|Prime Radiant]] — your own [[obsidian|Obsidian]] vault aligned with Michael's [[janus-prime-radiant|Janus Prime Radiant]] programme.

It then syncs your vault to your department's Drive folder so the rest of your team can see your contributions.

## How to use it

1. Open Claude Desktop
2. Make sure your Fireflies and Notion connectors are signed in (Settings → Connectors)
3. Type one of these:
   - `/janus-brain`
   - *"Set up my Janus brain"*
   - *"Onboard me into the wiki"*
4. The skill walks you through Phases 0-8 (pre-flight → identity → scaffold → cloud pulls → laptop scan → enrich → apply → sync → done)
5. After it finishes, open Obsidian — your new vault is in the vault switcher

## Subcommands (after first run)

- `/janus-brain sync` — pull yesterday's Notion + Fireflies + re-enrich any new laptop files
- `/janus-brain status` — health check (last cron run, vault size, [[federation|federation]] queue)
- `/janus-brain exclude <pattern>` — add to your privacy filter
- `/janus-brain federate` — re-run department federation only
- `/janus-brain reset` — wipe state, keep vault

## Verify, update, uninstall

| What | Command |
|---|---|
| Verify install | `~/Documents/janus-brain-bootstrap/install.sh --check` |
| Reinstall cron | `~/Documents/janus-brain-bootstrap/install.sh --install-cron` |
| Update to latest | `cd ~/Documents/janus-brain-bootstrap && git pull && ./install.sh` |
| Uninstall | `~/Documents/janus-brain-bootstrap/install.sh --uninstall` |

## Owner / contact

Jehad — AI Operations Engineer · jehada@janusd.io
