---
type: question
title: "What to do about the people/jehad-altoutou/ nested Prime Radiant instance (1,116 files)?"
slug: lint-2026-06-05-jehad-altoutou-nested-corpus
created: 2026-06-05
updated: 2026-06-09
departments: [ai-office]
status: active
owner: michael-bruck
related: [2026-06-05-lint, per-instance-curator-role, prime-radiant-instance-setup, janus-brain-enrollment]
---

# What to do about the `people/jehad-altoutou/` nested Prime Radiant instance?

**Surfaced by:** the 2026-06-05 lint ([[2026-06-05-lint]]). Not touched — flagged for a curator+Jehad decision because it's someone else's work and only reversible by them.

## What it is

`people/jehad-altoutou/` is **not a person page**. It is a **complete, self-contained Prime Radiant instance** committed into the AIO repo:

- its own **`CLAUDE.md`** and **`.config.yaml`**
- **`self.md`** — "the self-page maintained by `/janus-brain`… updates as the ingest pass observes patterns in Jehad Altoutou's work"
- **`sources/`** (1,096 files), **`meetings/`** (14), **`projects/`**, **`entities/`**, **`questions/`**
- **1,116 files total**, all git-tracked.

This is Jehad's personal `/janus-brain` vault (see [[janus-brain-enrollment]]) living *inside* the AIO vault rather than as a sibling clone under `~/janus/prime-radiant/`.

## Why it matters

1. **It distorts every vault-wide metric.** The AIO wiki is ~582 pages; the repo reports ~1,700 `.md` files, ~1,116 of which are this one corpus. Every lint must now manually exclude `people/jehad-altoutou/` or the counts are meaningless (orphans, broken-refs, frontmatter compliance all polluted).
2. **It's a second instance in one repo.** Per [[per-instance-curator-role]] (v0.15) and the substrate model (§1, "GitHub-backed Git repos"), each Prime Radiant instance lives in *its own repo* cloned under `~/janus/prime-radiant/<instance>/`. A `janus-brain` personal corpus is arguably its own instance — it has its own CLAUDE.md — and by the substrate rule should be its own repo, not nested.
3. **Schema violation.** `people/` is specified (§2/§3) as one `<firstname-lastname>.md` per person. A person-named *directory* containing 1,096 sources is outside the schema.

## Options

1. **Extract to its own instance repo** (recommended). Move `people/jehad-altoutou/` → a sibling clone `~/janus/prime-radiant/janus-brain-jehad/` (or similar), remove from the AIO repo. It already has the CLAUDE.md + .config.yaml to stand alone. Cleanest; matches the substrate model. Requires Jehad's sign-off and a `git rm` + history note.
2. **Gitignore it in place.** Add `people/jehad-altoutou/` to `.gitignore` and `git rm --cached` so it stays on Jehad's disk but leaves the shared repo. Keeps Jehad's local workflow untouched; stops polluting the shared vault.
3. **Keep, but formally exclude from AIO metrics.** Codify in CLAUDE.md that `people/*/` subdirectories are personal `janus-brain` corpora excluded from lint/index. Lowest effort; leaves the two-instances-in-one-repo smell and bloats clones for every contributor.
4. **Keep a thin `people/jehad-altoutou.md` person page** (the normal schema page) regardless of which option above is chosen for the corpus — the *person* should still have a standard entity page.

## Recommendation

Option 1 (extract to own repo) + Option 4 (keep a normal `people/jehad-altoutou.md` person stub). This matches the substrate + curator-role model and de-pollutes the AIO vault. Decision owner: Michael + Jehad. **Do not delete** the corpus content in any case — extract or de-track only.

## How it got here (hypothesis, unconfirmed)
Likely a `janus-brain` enrollment that wrote into the AIO clone's `people/` rather than a dedicated clone, then got swept into a `vault backup:` auto-commit. The git log shows people/ activity on the Jehad workstation (b91d766, 2026-06-01). Confirm with Jehad in the next sync.

---

## Status (2026-06-09) — still open; corpus grew during the personal-vault migration

**Decision still pending (Michael + Jehad).** The corpus remains nested in the AIO repo and is now **~1,193 files** — it grew on 2026-06-09 when Jehad's personal Obsidian vault was migrated in (that pass added `people/jehad-altoutou/self.md` profile content and `people/jehad-altoutou/personal-vault-index.md`; laptop sources still live under this subtree). See the 2026-06-09 migration `log.md` curation entry.

- **Option 4 (keep a normal `people/jehad-altoutou.md` person page):** ✅ already satisfied — that page exists alongside the directory.
- **Option 1 (extract the corpus to its own instance repo) / Option 2 (gitignore in place):** ❌ still not done — this is the open decision. Recommended path remains **Option 1 + Option 4**.

**Note:** until this is resolved, vault-wide lint metrics (orphans, file counts) must continue to exclude `people/jehad-altoutou/` — e.g. the 2026-06-09 orphan audit counted ~1,148 orphans in `people/` that are this corpus's leaf source nodes, not real wiki orphans. Owner: [[michael-bruck|Michael]] + [[jehad-altoutou|Jehad]]. **Do not delete** — extract or de-track only. Stays `active`.
