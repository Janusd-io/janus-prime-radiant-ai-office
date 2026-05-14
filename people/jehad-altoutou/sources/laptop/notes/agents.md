---
type: source
source_type: laptop
title: AGENTS
slug: agents
created: 2026-05-12
captured_by: jehad-altoutou
audience: personal
original_path: /Users/jehad/assessify/AGENTS.md
original_size: 3764
original_ext: .md
category: notes
extracted_with: text-copy
extracted_at: "2026-05-14T09:51:32Z"
sensitivity: dept
sensitivity_confidence: 0.90
sensitivity_reason: "Internal coding-agent rulebook — operational"
project: assessify

---

# AGENTS

_Extracted from `[[assessify|assessify]]/AGENTS.md` on 2026-05-14._

<!-- BEGIN:nextjs-agent-rules -->
# This is NOT the Next.js you know

This version has breaking changes — APIs, conventions, and file structure may all differ from your training data. Read the relevant guide in `node_modules/next/dist/docs/` before writing any code. Heed deprecation notices.
<!-- END:nextjs-agent-rules -->

<!-- BEGIN:handoff-pointer -->
## Session handoff — read this on turn 1

`HANDOFF.md` at the project root captures the state of the most recent
session: what just shipped, what's mid-flight, the user's open threads,
and the production deploy workflow. Reading it first is cheaper than
re-deriving context from git log + greps.

If `HANDOFF.md` is missing or older than the latest commit on `main`, fall
back to the project brain below.
<!-- END:handoff-pointer -->

<!-- BEGIN:project-brain -->
## Project brain — read this before exploring the codebase

A curated, hand-maintained summary of Assessify lives at:
**`/Users/jehad/Documents/[[obsidian|Obsidian]] Vault/03 Projects/Assessify/_BRAIN.md`**

Always consult `_BRAIN.md` first when you need:

- Current state of the project (what's shipped, what's next)
- Key file paths for recurring tasks (intake form, candidate detail, MCP tools, PDF, email)
- Data model summaries (Candidate, Application, RecruitmentRubric, etc.)
- Production deploy + DB-migration patterns

Reading the brain is cheaper than running 5+ grep / find / Explore calls. Update the brain at the end of any non-trivial change so the next session has accurate context. Ignore the 614 auto-graphified `*().md` notes in the same folder — they're machine-generated noise; only `_BRAIN.md` is canonical.
<!-- END:project-brain -->

<!-- BEGIN:efficiency-rules -->
## Token-efficiency rules (mandatory)

These exist because earlier sessions burned through usage on avoidable habits. Follow them; they are not optional.

1. **Read sections, not whole files.** When a file > 100 lines and you only need a known function/block, use `offset`/`limit` on Read or grep for the exact symbol first. Don't load 800-line files to change one line.

2. **Don't run `npx tsc --noEmit` after every micro-edit.** Run it once at the end of a coherent change set, immediately before deploy. Type errors that matter will be caught then; running it 5 times in one task is ~30s × 5 of wasted compute and tokens reading the output.

3. **Don't run smoke tests after every restart.** One curl per deploy, not per file.

4. **No verbose end-of-turn summaries.** Two sentences max: what changed, what's next. No tables of changed files, no per-file bullet lists, no "Verified on prod" rituals — the diff and the deploy log are the source of truth. The user can read the diff.

5. **No preamble before action.** Don't restate the task or list the plan in prose before executing. State the one thing you're doing in a sentence, then do it.

6. **Bundle parallel work into single tool calls.** When multiple reads/greps are independent, send them in one message with parallel tool blocks — not sequentially across turns.

7. **Don't re-read files you just edited.** The harness tracks state. Don't run `tail` or `cat` to "verify the change" — Edit/Write would have errored if the change failed.

8. **Skip exploration when the user gave you the path.** If the message names a file or function, go straight there. Do not Explore-agent or grep "to confirm".

9. **Pick the cheapest model that can do the task.** For routine edits / single-line fixes, suggest `/model sonnet` or `/model haiku`. Reserve Opus for plans, debugging stack traces, and multi-file refactors.

10. **One workstream per session.** If the user pivots to an unrelated task, suggest `/clear`. Old context is dead weight on every subsequent turn.
<!-- END:efficiency-rules -->
