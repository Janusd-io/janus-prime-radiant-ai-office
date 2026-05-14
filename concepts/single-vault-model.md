---
type: concept
title: Single-vault model (Prime Radiant 2026-05-14)
slug: single-vault-model
created: 2026-05-14
updated: 2026-05-14
departments: [ai-office]
status: active
confidence: high
sources: [rewrite-spec, handover, readme-11, skill-3]
related: [prime-radiant, prime-radiant-three-layer-architecture, janus-brain-bootstrap, federation, peer-to-peer-mesh-federation-pattern]
captured_by: jehad-altoutou
audience: department
---

# Single-vault model

The architecture the [[janus-brain-bootstrap]] skill adopted on 2026-05-14, superseding the earlier two-vault (personal-repo + dept-clone + federation) design. Signed off by [[jehad-altoutou]] in [[rewrite-spec]].

## Shape

One GitHub repo per department under `Janusd-io/janus-prime-radiant-<dept>`. Every employee in that dept clones it once to `~/janus/prime-radiant/` — that single clone is their Obsidian vault. Dept-shared content (decisions, projects, processes, vendors, concepts, top-level people stubs) lives at the vault root. Per-person content lives at `people/<person-slug>/` with `sources/`, `meetings/`, and a gitignored `private/`.

```
~/janus/prime-radiant/                       <- single clone of dept repo
├── decisions/  projects/  processes/  vendors/  concepts/   <- dept-shared
├── people/
│   ├── <other-teammates>/                   <- read-only via git pull
│   └── <self-slug>/
│       ├── CLAUDE.md   self.md   .config.yaml
│       ├── sources/  meetings/              <- dept-visible
│       ├── private/                          <- gitignored
│       └── .review-queue.md                  <- gitignored
└── .gitignore
```

Multiple teammates push to the same repo. The Obsidian Git community plugin pulls/pushes every 5 min while the vault is open.

## What got deleted

Per [[rewrite-spec]]:

- `bootstrap-personal-vault.sh` (per-employee private repo creation)
- `federate-to-department.sh` / `.py` and the dedup-hash logic
- `refresh-from-aio.sh` (no separate AIO clone)
- `~/.config/janus-brain/sync.conf`
- The `Janusd-io/janus-prime-radiant-personal-<slug>` repo family (archived)
- The `/janus-brain federate` subcommand

## Why

The two-vault design split a single conceptual artefact across two repos and required a federation script to keep them in sync — that script accumulated dedup-hash complexity and edge cases the moment more than one contributor used it. Collapsing to one repo per department per [[prime-radiant-three-layer-architecture]] (the dept is the unit of curation) gave: simpler mental model, no federation step, GitHub Teams as the ACL boundary, no chance of two copies drifting. Privacy is handled in-tree via `private/` + the [[sensitivity-classification]] classifier rather than via vault separation.

## What's still out of scope

- Org-tier repo. A future read-only "CEO brain" skill will federate across dept repos.
- Curator-mediated `inbox/` promotion workflow.
- Linux support (macOS-only initially per the launchd / AppleScript / path assumptions).

## See also

- [[rewrite-spec]] — the authoritative 2026-05-14 spec
- [[prime-radiant-three-layer-architecture]] — the layer model the single-vault preserves
- [[sensitivity-classification]] — how privacy is handled without a separate vault
- [[janus-brain-bootstrap]] — the project that landed this rewrite
