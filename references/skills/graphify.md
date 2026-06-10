---
type: tool
tags: [graphify, graph, ai]
---

# 🌐 Graphify — AI Knowledge Graph Engine

**Repo**: https://github.com/safishamsi/graphify
**Install**: `pipx install graphifyy --python python3.14` (installed ✅)
**Global skill**: `~/.claude/skills/graphify/SKILL.md` (installed ✅)

## What It Does

Graphify builds a **multi-layer knowledge graph** from any folder — code, docs, PDFs, images, video/audio. It uses:
1. **AST extraction** (tree-sitter) — deterministic code structure
2. **Whisper transcription** — local video/audio
3. **Claude subagents** — semantic concept + relationship extraction
4. **Leiden clustering** — community detection

Every relationship is tagged `EXTRACTED`, `INFERRED`, or `AMBIGUOUS` so you always know what's trusted.

## Commands

```bash
/graphify .                                    # Build graph of current folder
/graphify <path> --obsidian                    # Export as Obsidian vault structure
/graphify <path> --update                      # Merge with existing graph
graphify query "how does X connect to Y?"      # BFS traversal
graphify path "NodeA" "NodeB"                  # Shortest path between nodes
graphify explain "NodeX"                       # Neighbors + context
graphify watch <path>                          # Auto-rebuild on changes
```

Output goes to `graphify-out/`:
- `graph.html` — interactive visualization
- `graph.json` — queryable persistent graph
- `GRAPH_REPORT.md` — high-value nodes + connections

## How We Use It Here

1. **Per-project**: Run `/graphify .` inside a project folder. Then link its `GRAPH_REPORT.md` from the project note in [[index|Projects]].
2. **Vault-wide**: Run `/graphify "/Users/jehad/Documents/Obsidian Vault"` to graph the brain itself — find which notes are "god nodes" and which are orphans.
3. **Cross-session recall**: `graphify query "..."` is a token-efficient alternative to re-reading files (71.5× reduction per the project docs).

## Integration Points

- [[brain|/brain]] — wraps Graphify commands for this vault
- [[references|Home]]

## Latest Graph

*(After running `graphify` on the vault, paste `GRAPH_REPORT.md` link here)*
