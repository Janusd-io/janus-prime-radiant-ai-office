---
type: concept
title: "Ralph Loop Pattern"
slug: ralph-loop-pattern
created: 2026-05-07
updated: 2026-05-23
departments: [ai-office, engineering]
confidence: high
related: [agent-harness, agentic-ai, agent-memory, context-engineering, janus-prime-radiant-build, claude-code, gbrain, 2026-01-04-ralph-for-idiots-singh]
sources: [ralph-wiggum-simpsons-ai, ralph-wiggum-software-engineer, 2026-01-04-ralph-for-idiots-singh]
---

# Ralph Loop Pattern

An agent iteration pattern that treats context pollution as a certainty rather than an accident and **deliberately rotates context** between iterations. State persists externally (filesystem + git + dedicated state files); failures evaporate with the context window. The agent is a volatile process, not a reliable collaborator.

> **One-line takeaway** (per Agrim Singh, 2026-01): "*Your progress should persist. Your failures should evaporate.*"

## Origin

- **Geoffrey Huntley** (May 2025, rural Australia) coined and popularised the pattern. Canonical post: [ghuntley.com/ralph](https://ghuntley.com/ralph/). The minimal kernel is a bash loop that keeps starting a fresh agent context against the same task:

  ```bash
  while :; do cat prompt.md | agent ; done
  ```

  Same task. New brain each iteration. The "memory" is not the chat history — it's the **filesystem + git**.

- **Agrim Singh** (2026-01-04) wrote the canonical 5-minute, copy-paste, no-mysticism explainer that this concept page is now built against — see [[2026-01-04-ralph-for-idiots-singh]]. Singh's Cursor port at [github.com/agrimsingh/ralph-wiggum-cursor](https://github.com/agrimsingh/ralph-wiggum-cursor) extends the pattern with per-iteration model swap, signal-based rotation, and gutter detection.

## The actual insight: context pollution

Every AI coding session has a context window. Stuff goes in — files read, commands run, outputs produced, **wrong turns taken, half-baked plans hallucinated at 2:13am**. The cursed property: *you can keep adding, but you can't delete*.

Failures accumulate like plaque. Eventually the familiar symptom cluster:

- Repeating itself
- "Fixing" the same bug in slightly different ways
- Confidently undoing its own previous fix
- Circular reasoning, but with commit rights

That's context pollution. Once you're there, **adding more instructions doesn't help. More tokens don't help. More patience doesn't help.** Once the ball is in the gutter, adding spin doesn't save it.

Ralph doesn't try to clean the memory. It **throws it away and starts fresh**.

> The loop is not the technique. **State hygiene is the technique.**

## The mechanics: externalise state, rotate context

If you rotate context constantly, how do you make progress? You externalise the parts that matter — to files, to git, to dedicated state directories — and let the volatile parts die with the conversation.

| Channel | Good for | Bad for |
|---|---|---|
| **Context window** | Current reasoning, fresh attempts | Persistence — dies with the conversation, polluted by dead ends |
| **Filesystem + git** | What you choose to write; auditable history; rollback-able | "Memory" can drift if writes are ad-hoc; needs discipline |

Each fresh agent starts clean, reads the anchor file + the `.ralph/` state directory, then reconstructs reality from files. The progress accumulates in the files; the failures evaporate with the rotated context.

### The anchor file (source of truth)

Every Ralph setup needs a single source-of-truth file that survives rotations and tells a brand-new agent what reality looks like. Per Singh's Cursor implementation, that file is `ralph_task.md`:

```markdown
---
task: build a rest api
test_command: "npm test"
---

# task: rest api

## success criteria
1. [ ] get /health returns 200
2. [ ] post /users creates a user
3. [ ] all tests pass
```

Checkboxes are the *machine-verifiable definition of done*. If you can't write checkboxes, you're not ready to loop — you're ready to think.

### The `.ralph/` state directory

Per Singh's Cursor implementation:

| File | Purpose |
|---|---|
| `guardrails.md` | Learned constraints ("signs") — append-only |
| `progress.md` | What's done, what's next |
| `errors.log` | What blew up |
| `activity.log` | Tool usage + token tracking |

The loop reads these every iteration. Fresh context, persistent state.

## Guardrails: the kaizen mechanism

Ralph will do something stupid. The win condition is not "no mistakes." The win condition is **the same mistake never happens twice**.

When something breaks, the agent appends a *sign* to `guardrails.md`:

```markdown
### sign: check imports before adding
- trigger: adding a new import statement
- instruction: check if import already exists
- added after: iteration 3 (duplicate import broke build)
```

Guardrails are append-only. Mistakes evaporate. Lessons accumulate. Next iteration reads guardrails first. Cheap, brutal, effective — kaizen for a golden retriever with a soldering iron.

## When to use Ralph (and when not to)

**Use Ralph for implementation** — when the specs are crisp, success is machine-verifiable (tests, types, lint), and the work is bulk execution: CRUD, migrations, refactors, porting. Ralph excels at long-running implementation work where humans become the bottleneck.

**Don't use Ralph for exploration** — when you're still deciding what to build, when taste and judgment matter more than correctness, or when you can't cleanly define what "done" even means. If the real work is *thinking*, looping is the wrong tool — that's interactive territory.

> If you can't write checkboxes, you're not ready to loop. You're ready to think.

The role of the human in Ralph mode is **steering, not rowing**:
- You define what "done" means.
- You add constraints when things go wrong.
- You review outcomes, not keystrokes.
- You decide when to intervene.

## Why per-iteration model swap matters

Singh's Cursor port surfaces a non-obvious benefit of Ralph: **different models fail in different ways**. The 5-line bash version locks you into one model and therefore one failure mode. The Cursor port lets you swap models per iteration:

- Starting a new project → Opus (architecture matters)
- Stuck on something weird → Codex

Singh reports better results on some workloads with GPT-Codex models than Opus 4.5 — vibes, tokenisation, inductive bias, or unclear, but repeatable. The under-discussed lesson vs the "one agent to rule them all" framing: Ralph lets you *exploit* the heterogeneity of model failure modes rather than be stuck with one.

## Why Claude Code is "accidentally anti-Ralph"

Singh's piece is explicit: the Claude Code plugin approach (one long-running session, context grows, auto-compaction kicks in when context fills) is **accidentally anti-Ralph**. Specifically:

- It keeps pounding the model in a single session until context rots.
- The session grows until it falls apart.
- No visibility into context health.
- No deliberate rotation.
- Locked into a single model (per session).

> Claude Code treats context rot as an accident. Ralph treats it as a certainty.

This is a meaningful critique for Janus to hold while operating Claude Code as the primary engineering surface. The mitigation in current AIO practice is that long-running coding work tends to be broken across multiple Claude Code sessions naturally (per-task, per-day, per-feature) — which is an *accidental* Ralph approximation. But explicit Ralph mechanics (the `.ralph/` directory, guardrails-as-append-only, machine-verifiable completion checkpoints) would make this discipline *deterministic* rather than dependent on the operator's habits. Note: the *dreaming* feature inside Claude Code ([[2026-05-21-code-with-claude-london]]) is partially convergent — it's a vendor-side attempt to address the same context-rot failure mode by writing notes/summaries that bridge sessions. Whether it's Ralph-flavoured or session-bridging-flavoured depends on whether the dreams cause deliberate rotation or just compress the current session.

## Practitioner mechanics — Huntley's tuning discipline

Huntley's canonical post ([[ralph-wiggum-software-engineer]]; ghuntley.com/ralph) adds a layer of operational discipline beyond the kernel mechanic. Worth lifting because these are the lessons from running Ralph on a real, multi-month codebase (CURSED, a new esoteric programming language built entirely via Ralph):

- **One item per loop.** Only one thing. Trust Ralph to choose which thing — LLMs are good at reasoning about *what's important next*. Multi-task loops degrade fast; single-item loops compound.
- **Deterministically allocate the stack the same way every loop.** The same plan file (e.g., `fix_plan.md`) + the same specs folder loaded into context, every iteration. This is what makes the loop a *loop* rather than a sequence of unrelated agent invocations.
- **Specs folder pattern.** Up front: a long conversation with the LLM about requirements; then *write the specifications out, one per file*, in a `specs/` folder. Each iteration reads the relevant spec. Specs are the contract; Ralph implements against them.
- **Two-phase rhythm: generate → backpressure.** Phase 1 produces code; Phase 2 applies pressure (tests, lint, type-checks, observation) that forces Phase 1 to iterate again. Without backpressure, Ralph hallucinates progress.
- **Capture the importance of tests in the moment.** When you notice a class of failure, write the test that would have caught it *now* — not "later when we have time." Tests are how Ralph backpressures itself.
- **No cheating.** Anti-pattern: letting Ralph mark something "done" before the test passes. The completion-promise mechanic (and the Stop Hook variant) exists to prevent this.
- **Ralph is monolithic, not microservice.** Multi-agent / agent-to-agent / multiplexing patterns are "a red hot mess" for the same reason microservices are operationally expensive — non-deterministic agents in a graph compound failure. A single process per repo per task scales vertically and is debuggable.
- **Tune Ralph like a guitar.** When Ralph makes a mistake, don't blame the tool — *add a sign*. Singh's `guardrails.md` is the same mechanic, formalised. The discipline is: every observed bad behaviour becomes a permanent guardrail; the next Ralph never makes that mistake.
- **You will wake up to a broken codebase.** Long-running Ralph runs (overnight, multi-day) will sometimes converge to broken state. Recovery is via `git reset --hard` to the last known good commit, then re-running with a stronger guardrail. *Failures evaporate; the guardrail persists.* This is the same kaizen mechanic Singh names.
- **Any problem created by AI can be resolved through a different series of prompts.** Huntley's optimistic closer. The implicit Janus-relevant claim: there's no failure mode that's uniquely AI-shaped — the operator's job is to find the prompt structure that surfaces and resolves it.

These are the *Huntley operational layer* on top of the *Singh structural layer*. Singh tells you the architecture (anchor file + `.ralph/` directory + per-iteration rotation); Huntley tells you the operating discipline (one item per loop, deterministic stack, specs folder, tuning-as-signs).

## Earlier framing: the Anthropic-plugin "Official Ralph" variant

Before Singh's canonical explainer, the wiki entry distinguished two implementations:

- **The Huntley Ralph (community bash script)** — chaotic, unbridled, best for creative exploration. Loop runs until human kills it or model succeeds.
- **The Official Ralph (Anthropic plugin, late 2025)** — uses a Stop Hook that intercepts exit attempts, checks for a Completion Promise (e.g., "All tests passed"), and feeds failure as structured data back into the loop. Prevents infinite hallucination spirals.

Singh's reframing is sharper because it surfaces the actual mechanic (deliberate context rotation + externalised state) underlying *both* variants. The Stop Hook is one way to encode the rotation trigger; the bash loop is another. The point isn't the loop mechanism — it's the state hygiene.

## How Ralph relates to Janus Prime Radiant

There are striking convergences between Ralph's state-hygiene discipline and the [[janus-prime-radiant-build|Prime Radiant]] pattern. Both treat the agent's working context as volatile and put the load-bearing state in files. The discipline-level overlaps:

| Ralph discipline | Prime Radiant analogue |
|---|---|
| Anchor file (`ralph_task.md`) — single source of truth for the current task | `CLAUDE.md` + `index.md` — single source of truth for the wiki state |
| `.ralph/guardrails.md` — append-only learned constraints | `decisions/` + `lessons/` — append-only learned constraints + retros |
| `.ralph/progress.md` — what's done, what's next | `log.md` (chronological) + `questions/` (open threads) |
| `.ralph/errors.log` — what blew up | `lessons/` + `pulse/YYYY-MM-DD-lint.md` reports |
| Per-iteration context rotation | Per-session context rotation (each Claude / Cowork session starts fresh, reads CLAUDE.md + relevant pages) |
| Machine-verifiable completion via checkboxes | Lint pass + ingest counter + explicit `status:` frontmatter |
| Kaizen ("same mistake never happens twice") | CLAUDE.md schema evolution + memory entries + lint-followup pattern |

The Prime Radiant pattern can be read as **Ralph applied to institutional knowledge work**: rotate the operator's context (curator, agent, both) frequently; never trust the conversation window to hold state; encode everything important into files; let lessons accumulate; let failures evaporate. Both patterns answer the same underlying question — *how do you build a durable system on top of a volatile process?* — at different scales: Ralph at the per-task agent-coding scale; Prime Radiant at the institutional-knowledge-base scale.

Worth noting: [[gbrain|GBrain]] (Garry Tan's open-source agent memory layer, surfaced 2026-05-22) makes this connection explicit in the *other* direction — markdown files as the durable layer, agent as the volatile reader-writer. Ralph + Prime Radiant + GBrain are three points on the same architectural shape.

## Enterprise wins (from Huntley's original framing)

- $50K contracts executed for $297 in API costs (cost arbitrage between human + agent).
- 6 repositories auto-generated overnight (YC hackathon stress test).
- 14-hour autonomous codebase upgrades (React v16→v19 without human input).
- Singh: large-repo TypeScript ports in the tens of thousands of LoC, without faceplanting every 10 minutes.

These are the *implementation*-territory wins. They are not exploration wins — Ralph won't help you decide *what* React-version-to-port-to; it will execute the port once you've decided.

## See also

- [[2026-01-04-ralph-for-idiots-singh]] — the canonical 2026 explainer.
- [[agent-harness]] — the orchestration layer; Ralph is a specific harness discipline.
- [[agent-memory]] — the broader memory family; Ralph is the *deliberate-amnesia* / externalised-state variant.
- [[janus-prime-radiant-build]] — institutional-knowledge analogue of Ralph's per-task discipline.
- [[gbrain]] — markdown-first agent memory layer; the converse architectural shape (durable markdown + volatile agent).
- [[claude-code]] — the surface Ralph critiques as "accidentally anti-Ralph" when run as a long-session default.
- [[context-engineering]] — the broader discipline of shaping what agents see; Ralph is a state-hygiene technique within it.
