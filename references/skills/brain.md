---
type: skill
tags: [skill, meta, brain]
command: /brain
path: ~/.claude/commands/brain.md
---

# /brain

Manage the Obsidian brain at `~/Documents/Obsidian Vault/`. Keeps every project, skill, and decision interlinked.

## Subcommands
- `/brain init <project-name>` — create a project note, link to user + skills + stacks
- `/brain update <project-name>` — add decisions, blockers, progress
- `/brain sync` — run [[README|Graphify]] on the vault to rebuild the knowledge graph
- `/brain connect <A> <B>` — add a wikilink between two notes
- `/brain recall <query>` — search the vault via Graphify query

## Always-On Behavior
Claude automatically creates/updates project notes when starting new work — no need to invoke manually.

## Related
- [[README|Graphify workflow]]
- [[index|Projects]]
- [[references|Home]]
