---
type: source
source_type: laptop
title: REWRITE-SPEC
slug: rewrite-spec
created: 2026-05-14
captured_by: jehad-altoutou
audience: personal
original_path: /Users/jehad/Documents/janus-brain-bootstrap/REWRITE-SPEC.md
original_size: 6057
original_ext: .md
category: notes
extracted_with: text-copy
extracted_at: "2026-05-14T09:51:46Z"
sensitivity: dept
sensitivity_confidence: 0.95
sensitivity_reason: "Architecture spec for the janus-brain rewrite — internal dept-shared design doc."
---

# REWRITE-SPEC

_Extracted from `Documents/janus-brain-bootstrap/REWRITE-SPEC.md` on 2026-05-14._

# Janus Brain — Rewrite Spec (2026-05-14)

Signed-off by Jehad on 2026-05-14. Supersedes the two-vault model in HANDOVER.md.

## Architecture

**One GitHub repo per department.** Every employee in that dept clones it as their single Obsidian vault. Their personal content lives in `people/<slug>/`; shared dept content at repo root. Sync = Obsidian Git plugin push/pull.

**Repos (Janusd-io):** `janus-prime-radiant-ai-office`, `…-marketing`, `…-hr`, `…-it-ops`, `…-finance`, `…-iso`, `…-pm`, `…-office-of-ceo`. Created on first contributor enrollment from `janus-prime-radiant-template`.

**No org-tier repo.** A future read-only "CEO brain" skill federates across dept repos. Out of scope for this rewrite.

**Local layout (every employee):**
```
~/janus/prime-radiant/                       ← single clone of dept repo
├── decisions/                               ← dept-shared
├── projects/
├── processes/
├── vendors/
├── people/
│   ├── <other-teammates>/                   ← read-only via git pull
│   └── <self-slug>/
│       ├── .config.yaml                     ← task_tracker, prefs
│       ├── CLAUDE.md
│       ├── self.md
│       ├── sources/                         ← dept-visible
│       ├── meetings/                        ← dept-visible
│       ├── private/                         ← gitignored (sensitivity=self|confidential)
│       └── .review-queue.md                 ← low-confidence sensitivity items
└── inbox/                                   ← optional staging (curator workflow, future)
```

## Enrollment flow (`/janus-brain`)

1. **Pre-flight** — existing checks
2. **Identity** — git config + `config/departments.yaml` lookup
3. **Task-tracker prompt** — Linear / Monday / Asana / Notion tasks / none / other → `people/<slug>/.config.yaml`
4. **Clone dept repo** — create from template if missing. Single clone at `~/janus/prime-radiant/`.
5. **Scaffold `people/<slug>/`** subtree
6. **Notion + Fireflies pulls** → `people/<slug>/sources/` and `people/<slug>/meetings/`
7. **Phase 3.5 meeting parser** — output follows `/standup` skill schema:
   - Frontmatter: `meeting_id`, `date`, `attendees`, `dept_scope`, `sensitivity`, `task_tracker`
   - Sections: `## Summary`, `## Decisions`, `## Action items`, `## This week`, `## Long-horizon`, `## Findings`, `## Open questions`, `## Related` (wikilinks)
   - Full transcript → sibling `<meeting>.transcript.md` linked from note (not inline)
   - Action items formatted for the employee's `task_tracker` (Linear-style for AI, Monday-style for PM, plain checkboxes for `none`)
8. **Phase 4 + 4.5** laptop walk + content extraction (unchanged)
9. **Phase 5 enrichment + sensitivity classifier**:
   - `sensitivity: dept|self|confidential` + `sensitivity_confidence: 0–1`
   - Heuristics: credentials → `confidential`; HR/salary/legal/health/family → `confidential`; 1:1 manager meetings → `self`; default → `dept`
   - `self|confidential` → routes to `people/<slug>/private/` (gitignored)
   - confidence < 0.7 → logged to `.review-queue.md`
10. **Apply + lint** — wikilinks resolve across whole vault (single namespace)
11. **Commit + push** to dept repo. No federation step.

## What's deleted

- `bootstrap-personal-vault.sh`
- `federate-to-department.sh` / `.py`
- Dedup hash logic
- `janus-prime-radiant-personal-template` GitHub repo (archive)
- `janus-prime-radiant-personal-jehad-altoutou` GitHub repo (archive after Jehad's rebuild)
- Notion as writeback sink (read-only ingest only)
- Linear/Monday writes from brain (those stay in `/standup` for AI only)
- `refresh-from-aio.sh` (no separate AIO clone)
- Two-vault references in README, ENROLLMENT, INSTALL

## What changes in existing files

- `SKILL.md` — Phase 2 (single clone), Phase 3 (task-tracker prompt), Phase 3.5 (standup-schema parser), Phase 5 (sensitivity classifier), Phase 7 (push not federate)
- `config/departments.yaml` — keep dept list, drop personal repo refs
- `templates/meeting-source.md` — rewrite to standup-schema shape
- `prompts/meeting-parser-subagent.md` — rewrite to produce standup-schema output
- `prompts/enrichment-subagent.md` — add sensitivity classification
- `scripts/discover.sh` / `bootstrap-dept-vault.sh` — single-vault flow
- `install.sh` — drop personal-vault subcommand
- `templates/personal-claude-md.md` → becomes the `people/<slug>/CLAUDE.md` template
- New: `scripts/classify-sensitivity.py`
- New: `templates/dept-gitignore` with `people/*/private/` and `*.confidential.md`

## Jehad's vault rebuild

1. Archive `janus-prime-radiant-personal-jehad-altoutou` on GitHub
2. Delete `~/janus/prime-radiant/personal/` and `~/janus/prime-radiant/ai-office/`
3. Run new `/janus-brain` → produces `~/janus/prime-radiant/` cloned from `janus-prime-radiant-ai-office`, with `people/jehad-altoutou/` populated correctly
4. Existing items in AIO's `inbox/` (from old federation) — leave; Jehad can curate them into proper locations or delete

## Acceptance criteria (must all pass before Andrew)

- [ ] Single local vault, no `personal/` + `ai-office/` split
- [ ] Every meeting note uses standup-schema sections, no raw transcript inline
- [ ] Transcript appendix file is wikilinked from the meeting note
- [ ] Action items formatted per `task_tracker` config
- [ ] Every source has `sensitivity` + `sensitivity_confidence` frontmatter
- [ ] `people/<slug>/private/` exists, is gitignored, contains items classified `self|confidential`
- [ ] `.review-queue.md` lists low-confidence items
- [ ] `git push` from the vault → dept repo updates visibly
- [ ] Vault lint: 0 errors
- [ ] All decisions/projects/entities cross-link correctly (no broken wikilinks)
- [ ] Task tracker prompt fires on enrollment and adapts downstream output

## Out of scope (defer)

- CEO-level cross-dept federation (future skill)
- Curator-mediated `inbox/` promotion workflow
- Org-tier repo
- Linux support
