---
name: standup
description: "Process AI Office daily standups end-to-end — Fireflies → Monday → Linear AIP → Obsidian. Trigger phrases \"Process today's standup\" or \"Log the standup from [date]\". Includes dry-run / preview mode."
---

# Skill: AI Office Daily Standup Workflow
**Version:** 3.23
**Owner:** Jehad Altoutou, AI Office
**Last Updated:** 2026-05-21
**Scope:** Post-standup processing — Fireflies → Monday Automations → Linear AIP → Obsidian / Prime Radiant (forward-looking journal), executed under a 3-phase Analyse → Plan → Execute model with production-grade hardening: subagent return validation, **mandatory tool registration for every tool mentioned** (any SaaS, AI, infrastructure, analytics, creative, or other software mentioned in a meeting is checked against Linear AIR and registered if absent), execution control mode for large runs, AIP conflict safety, task-volume control, defensive execution, **automatic chained evaluation when new tools are registered**, a **Context Coverage Invariant (Step 3G/3H/3I)** that guarantees every Monday item the skill touches carries a transcript-derived Description Update — no exceptions, no orphans, no group-moves without rationale, and a **two-layer Deduplication Gate (Step 2B.1 planning scan + Step 3.0 pre-create guard)** that prevents duplicate Monday items and sub-items from being created across sessions. Acts as orchestrator for `/ai-registry` and `/ai-tool-evaluation` via isolated Task/Agent subagent dispatch. The Monday AI Tools Registry board is no longer an active execution surface — Linear AIR is the sole source of truth for all tool data (AI and non-AI alike). **As of v3.21 Notion is removed entirely; Obsidian / Prime Radiant is the sole journal output surface. Step 5 writes directly to `~/janus/prime-radiant/sources/meetings/YYYY-MM-DD-<slug>.md` — no git ops are run from the sandbox (v3.23); Obsidian Git handles commit + push on its 5-min cycle. No Notion writes occur anywhere in this skill.**

---

## Core Principle

```
Monday          = tasks / projects / action execution (every touched item has context)
Linear AIR      = AI Tools Registry source of truth
/standup        = orchestrator
/ai-registry    = registry engine (auto-chains evaluation on new tools — v3.10)
/ai-tool-evaluation = evaluation engine
Subagents       = isolated execution layer (Task/Agent tool)
Obsidian / Prime Radiant = final journal / reporting surface (sole output — v3.21)
```

This skill never writes to Linear AIR or to the Monday AI Tools Registry board. All AI tool work flows through subagent dispatch — gated, validated, volume-controlled, and **chained** (registry → evaluation) for new tools.

**Context Coverage Invariant (v3.13):** every Monday item the skill *touches* in any Phase 3 step — create, source bump, status change, group move, sub-item add — is guaranteed to have a `<h2>Description (from meeting notes)</h2>` block in its Updates timeline by the time Phase 3 completes. If the item does not already have one, the skill posts one (Step 3G for creates; Step 3H for backfills; Step 3E.1 for moves). The pipeline does not consider Phase 3 complete until the Step 3I coverage check passes.

**Deduplication Gate (v3.22):** every candidate Monday item or sub-item is name-similarity-checked against existing content on both the main board (`5095012818`) and the sub-items board (`5095012849`) **before creation** — at planning time (Step 2B.1) and again at execution time (Step 3.0). High-confidence matches are blocked; medium-confidence matches require explicit user confirmation. Under-detection is the failure mode, not over-detection.

---

## What's new in v3.22

- **Two-layer Deduplication Gate added.**

  Root cause: the prior Step 2B duplicate detection searched Update bodies (last 30 days) and parent-item names using a 2-keyword threshold. It never queried the sub-items board (`5095012849`) by name, so new sub-items could be created on successive standups without any check against existing ones covering the same scope. Over 36 standups this produced at least 3 confirmed exact/near-exact duplicate sub-items on the "Prime Radiant — company-wide knowledge graph + digital twin" parent item (archived on 2026-05-20).

  Two new steps introduced:

  - **Step 2B.1 — Pre-Create Name-Similarity Scan (planning gate).** Runs in Phase 2 immediately after Step 2B. For every candidate item or sub-item identified in the execution plan, searches the relevant Monday board(s) by name and applies a token-overlap scoring algorithm. High-confidence duplicates (≥3 meaningful token overlap) are removed from the plan and logged as blocked. Medium-confidence (2 meaningful tokens) are flagged for user confirmation at Step 2E. Low confidence (0–1 token) proceeds.

  - **Step 3.0 — Pre-Create Guard (execution gate).** Runs in Phase 3 immediately before every `create_item` or sub-item creation call. Repeats the Step 2B.1 scan against the live board state. If a duplicate is detected that was not caught in Phase 2, the creation is blocked, the item is logged under Issues/Warnings, and execution continues with the next item. This closes the race condition where a duplicate item is created between Phase 2 scan time and Phase 3 execution time (e.g. if another standup run or manual create happened in between).

- **Step 2B.1 and Step 3.0 outputs added to Final Execution Report.** New "Deduplication" section in Step 6: lists every candidate blocked (name + id of the existing item it matched) and every candidate that required user confirmation.

- **Conventions and Execution Checklist updated** to reference both gates.

- **No behaviour change to Context Coverage, Monday writes, Linear, subagent dispatch, or Obsidian.** All v3.21 behaviour is preserved exactly.

## What's new in v3.21

- **Notion removed entirely.** Notion is no longer an output surface for standup content. Step 5 previously appended the forward-looking entry to the Notion Operations Notebook; Step 5G then mirrored the same content to Prime Radiant. v3.21 removes Notion from the pipeline: Step 5 IS the Prime Radiant write — the entry is written once, directly to `{{PRIME_RADIANT_VAULT}}/sources/meetings/YYYY-MM-DD-<slug>.md`, and committed + pushed. No Notion tools are called anywhere in this skill.
- **Step 1.6 — Idempotency check updated to file-existence check.** Previously checked the Notion Operations Notebook page for a `## AIO DD Mon YYYY` heading. Now checks whether the target markdown file already exists at the Prime Radiant path using `stat`. Same three-option prompt (skip / rerun / abort) and same default (skip).
- **Step 5 restructured.** Step 5 now IS the Prime Radiant write — it absorbs the algorithm previously in Step 5G. The old Step 5 (Notion append) is gone. Step 5G as a separate step no longer exists.
- **Notion fallback policy removed.** The Step 5D retry-and-fallback policy (which fell back to `outputs/notion-AIO-<DD-Mon-YYYY>.md`) is replaced by a simpler write-to-file policy: if the Prime Radiant write fails, log the failure and attempt a local fallback write to `outputs/standup-AIO-<DD-Mon-YYYY>.md`. The file-on-disk is always the safety net.
- **Final Report updated.** "Notion entry" → "Obsidian entry". Notion-specific fields (size hygiene, archive trigger, Notion retry) removed from the report template.
- **Notion Size Hygiene section retired.** The 80 KB / 14-day archive rules applied to the Notion master page. With Obsidian as the output, each standup is its own file — no size accumulation. The section is removed.
- **Subagent Return Schema: `notion_journal_addition` field renamed to `obsidian_entry_addition`.** Same semantics — a snippet for the standup journal entry. Field name updated to match the new output surface.
- **No behaviour change to Monday, Linear, or subagent dispatch.** All Phase 3 Monday writes, Description Update convention, Context Coverage Invariant, dispatch gate, and Linear AIP reconciliation are unchanged from v3.20.

## What's new in v3.20

- **Step 1 hardened: `fireflies_get_summary` removed and prohibited.** Step 1 previously listed `Fireflies:fireflies_get_summary` as a tool to call alongside `fireflies_get_transcript`. Although Step 1.5 already stated "The Fireflies summary is unreliable", the presence of the summary call created a failure mode where — if the raw transcript was too large to display inline — the skill fell back to the summary instead. The summary call is now removed entirely and replaced with an explicit `⛔ Never call fireflies_get_summary` prohibition.
- **Persisted-file fallback documented.** When `fireflies_get_transcript` returns a response too large for inline display (saved to a persisted path shown in the tool response), the skill now explicitly instructs the agent to use the `Read` tool on that exact persisted file path to load the full transcript before building the Digest. This closes the only remaining gap that could cause the skill to operate without the raw sentences.
- **No other changes from v3.19.** All v3.18/v3.19 improvements (full dispatch gate, Step 3.7 body, correct vault path `sources/meetings/`, slug generalisation, `parser_version: 3`, `standup_skill_version`) are preserved exactly.

## What's new in v3.19

- **Step 5G path corrected to CLAUDE.md §3 canonical.** v3.17 introduced the single-vault layout and wrote meeting files to `people/{{CAPTURED_BY_SLUG}}/meetings/YYYY-MM-DD-aio-standup.md`. That path was never aligned with the Prime Radiant CLAUDE.md §3 filing rule, which puts all meetings at `sources/meetings/YYYY-MM-DD-<slug>.md`. v3.19 corrects this. The new target is `{{PRIME_RADIANT_VAULT}}/sources/meetings/YYYY-MM-DD-<slug>.md`.
- **`{{CAPTURED_BY_SLUG}}` variable retired from the write path.** The `sources/meetings/` folder is shared — it does not live under any person's subtree. The variable is retained in front-matter (`captured_by: <slug>`) for provenance but is no longer part of the file path.
- **Slug generalised.** Previously hardcoded as `aio-standup`; now derived from the meeting type (e.g. `aio-standup`, `aio-mktg-it-meeting`). Multiple meetings processed in one standup run each produce their own correctly-named file.
- **Migration command updated** in Reference section (from `people/jehad-altoutou/meetings/` → `sources/meetings/`).
- **`standup_skill_version` bumped** to `v3.22` in all front-matter schemas and Conventions.
- **`/ai-registry` Obsidian vendor entity write (companion fix).** The `/ai-registry` skill now writes `entities/vendors/<slug>.md` to the Prime Radiant vault after every create or enrich operation. This is a companion fix to Step 5G's path correction — both gaps were identified on 2026-05-15.

## What's new in v3.18

- **Dispatch Gate completely rewritten (Section 2D.1).** The previous gate was a stub — "Unchanged from v3.12" with no actual criteria present in the file. In practice this caused all tool mentions to be dropped using ad-hoc judgment (typically: "operational SaaS → gated out"). That was wrong. Every tool mentioned in a standup or meeting must be checked against Linear AIR. There is no category of tool that is exempt — not web hosting, not transactional email, not analytics, not creative tools. All of it. The registry exists so Janus has a complete picture of every tool in use or under consideration, and that purpose only works if every tool makes it in.
- **Step 3.7 body written for the first time.** Also a stub ("Unchanged from v3.12") — the actual dispatch algorithm (3.7A registry dispatch, 3.7B return validation, 3.7C chain evaluation, 3.7D Monday follow-up task, 3.7E log outcomes) now lives explicitly in the skill rather than being implied by the schema alone.
- **"AI Tool Mentions" category renamed to "Tool Mentions."** Step 2's category E was labelled "AI Tool Mentions," which incorrectly scoped the registration pipeline to only AI tools. It now reads "Tool Mentions (all tools — SaaS, AI, infrastructure, analytics, creative, email, hosting, etc.)."
- **"AI Registry Source of Truth" section updated.** "When AI tools are discussed" changed to "When ANY tools are discussed" — the registry receives all tools, not just AI platforms.
- **Conventions Dispatch Gate line updated** to reflect the new default-pass behaviour: every tool mention triggers a Linear AIR check; the gate drops only zero-context market references.
- **Root cause of the gate being missing.** The v3.12 gate criteria were replaced with a "(Unchanged from v3.12)" stub at some point during the v3.13–v3.16 changelog consolidation. The original v3.12 criteria likely contained the "PREVENT OVER-TRIGGERING" framing that led to the restrictive interpretation. That framing is now inverted: the real risk is under-registration, not over-registration.

## What's new in v3.17

- **Single-vault layout (2026-05-14 `/janus-brain` rewrite).** The `~/janus/prime-radiant/` directory is a single git repo with one `.git/` root — not two separate repos at `personal/` and `ai-office/`. v3.16's dual-write to `personal/sources/meetings/` was based on the pre-2026-05-14 substrate. v3.17 retargets Step 5G to the `/janus-brain` canonical path: `people/{{CAPTURED_BY_SLUG}}/meetings/YYYY-MM-DD-aio-standup.md` within the single vault.
- **New path variable `{{CAPTURED_BY_SLUG}}`.** Identifies the standup curator's person slug (default `jehad-altoutou`). Derived at runtime by: (1) reading `git config --global user.email` and matching the email to a `people/*/` directory, or (2) finding the single `people/*/` directory in the vault if only one exists. Always defaults to `jehad-altoutou` if derivation is ambiguous.
- **`{{PRIME_RADIANT_VAULT}}` default updated.** Was `~/janus/prime-radiant/personal/`; now `~/janus/prime-radiant/` (the single-repo root). Override if the vault root is elsewhere.
- **`parser_version: 3` in frontmatter.** The 2026-05-14 `/janus-brain` meeting-digest applier bumped to `parser_version: 3`. Standup files must carry this field so the applier's re-processing guard recognises them as already processed and skips them.
- **`standup_skill_version` field retained.** Set to the current skill version (`v3.22`) so the applier can distinguish standup-skill-written files from applier-written curated summaries.

---

## Purpose

After each AI Office daily standup, execute this skill to:
1. Build a **Meeting Intelligence Digest** from the raw Fireflies transcript (the Fireflies summary is a weak hint, never canonical)
2. **Check Obsidian idempotency in Phase 1** — if the target markdown file for today already exists in the Prime Radiant vault, ask the user (skip / rerun / abort) before any writes
3. Construct an explicit **execution plan** with confidence-scored matches, duplicate detection, and parent-project routing — no writes yet
4. **Decide between automatic and Controlled Execution Mode** based on plan complexity (see Execution Control Mode below)
5. Execute the plan with atomic, idempotent writes to Monday Automations only — Strict Write Safety + low-confidence non-create rules enforced
6. **Maintain the Context Coverage Invariant** — every touched item has a Description Update by the end of Phase 3 (Steps 3G create, 3H backfill, 3E.1 move-rationale, 3I coverage check)
7. **Enforce the Deduplication Gate** — every candidate item/sub-item checked for name-similarity against live board content at both planning time (Step 2B.1) and execution time (Step 3.0) before any creation call
8. **Dispatch isolated subagents** via the Task/Agent tool for any `/ai-registry` or `/ai-tool-evaluation` work — gated, validated, volume-controlled — receive structured JSON returns. **Auto-chain `/ai-tool-evaluation` after `/ai-registry` creates a new AIR-N entry.**
9. Reconcile Linear AIP against Monday Automations status, with **Conflict Safety** — only update Linear when transcript or completed Monday execution authorises it
10. Write a forward-looking Obsidian entry with output compression — Clean Meeting Summary, time-bucketed next steps, supporting context, registry/evaluation outcomes, **Step 3H backfill summary**, **Step 3E.1 move summary** — directly to `~/janus/prime-radiant/sources/meetings/YYYY-MM-DD-<slug>.md` (Step 5); no git ops from sandbox — Obsidian Git handles commit + push
11. Emit a structured **Final Execution Report**, including any Subagent Failures, Conflicts, chained-evaluation outcomes, Description-Update failures, **Context Coverage results (covered / backfilled / move-rationales / failures)**, **Deduplication results (blocked / user-confirmed)**

Trigger phrase: *"Process today's standup"* or *"Log the standup from [date]"*

---

## Skill Boundaries — Avoid Duplication

This skill is **not** the source of truth for AI tool descriptions, costs, tier classification, department labels, or formal Gate evaluations. Those live in Linear AIR and are owned by sibling skills.

| Domain | Owning skill | Where data lives |
|---|---|---|
| Tool registry CRUD (create, enrich, status moves, label management, derivative views like Slack Canvas / Excel) **+ related-tools check** | `/ai-registry` | Linear AIR team |
| Formal Gate 1-4 evaluation methodology, scoring matrices, gate-decision comments | `/ai-tool-evaluation` | Linear comments on AIR issues |
| Day-to-day tasks, automations, project planning, action tracking, sub-items, standup execution tasks **with full Context Coverage** | **this skill** | Monday Automations board (`5095012818`) |
| Daily standup logs, decisions, **next-step planning**, registry/evaluation outcomes | **this skill** | Prime Radiant / Obsidian (`~/janus/prime-radiant/sources/meetings/`) |

**Never write to Linear AIR or the Monday AI Tools Registry from this skill.** All tool-side work is delegated via Task/Agent subagent dispatch (Step 3.7) — and only when the Subagent Dispatch Gate authorises it.

---

## AI Registry Source of Truth

**Linear AIR is the only active AI Tools Registry.**

Monday is used only for:
- Automation tasks
- Projects
- Action tracking
- Sub-items
- Standup execution tasks

**Do not create, update, move, or sync AI Tools Registry items in Monday.**

When ANY tools are discussed in a standup — AI, SaaS, infrastructure, analytics, creative, email, hosting, or anything else:
- Check Linear AIR for an existing entry and create / enrich / evaluate via `/ai-registry` or `/ai-tool-evaluation` subagents (Step 3.7) — per the Dispatch Gate rules at Step 2D.1
- **For new tools:** chained evaluation runs automatically after `/ai-registry` creates the entry (see Step 3.7C)
- **Optionally** create a Monday Automations task only if there is operational project work required as a downstream consequence (e.g. "Test tool in sandbox", "Prepare procurement approval", "Schedule vendor demo")

The Monday AI Tools Registry board (`5095577150`) is retained as a historical reference only and is **deprecated as an active execution surface**. See "Reference: Deprecated Surface" at the end of this document.

---

## Sub-Skill Invocation via Subagent Dispatch

The `/standup` skill acts as the **central orchestrator**. Sibling skills are reached via **isolated subagent dispatch** through the Task/Agent tool, never via the `Skill` tool from within this skill (which would load sibling instructions co-resident in this conversation, causing instruction collisions).

### Use `/ai-registry` when:
- A new AI tool must be created in Linear AIR
- Tool metadata needs enrichment (description, vendor, category, etc.)
- Tool status in Linear AIR must be updated or synced
- Tool ownership, departments, or labels must be updated
- Registry-level operations or derivative views (Slack Canvas, Excel workbook) are required

**For new-tool creation:** `/ai-registry` v2.0+ also runs a related-tools check (links to similar AIR entries, or generates suggested alternatives) and signals `evaluation_required: true` in its return — `/standup` then chains Gate 1 automatically.

### Use `/ai-tool-evaluation` when:
- A tool requires Gate 1–4 evaluation
- A tool comparison or recommendation must be scored
- Cost, security, risk, or adoption fit needs structured evaluation
- A standup decision requires formal evaluation backing

**Most evaluation runs are now chained automatically by `/standup` after `/ai-registry` creates a new entry.** Direct dispatch of `/ai-tool-evaluation` is for explicit re-evaluations or later-stage gates (Gate 2/3/4).

### Subagent Hand-Off JSON Schema

```json
{
  "target_skill": "/ai-registry | /ai-tool-evaluation",
  "tool_name": "",
  "air_id": "AIR-N or new",
  "standup_date": "AIO DD Mon YYYY",
  "transcript_evidence": [
    { "speaker": "", "excerpt": "" }
  ],
  "decision_or_action_required": "",
  "owner": "",
  "urgency": "by-next-standup | this-week | longer",
  "expected_output": ""
}
```

### Subagent Return JSON Schema (v3.10, updated v3.21)

```json
{
  "action_completed": "",
  "linear_air_issue": "AIR-N",
  "final_status_or_result": "",
  "monday_task_required": {
    "required": true,
    "task_title": "",
    "reason": ""
  },
  "evaluation_required": {
    "required": true,
    "tool_name": "",
    "air_id": "AIR-N",
    "reason": ""
  },
  "related_tools_summary": "",
  "obsidian_entry_addition": "",
  "unresolved_questions_or_blockers": []
}
```

(Validation rules unchanged from v3.10 / v3.12 — see "Subagent Return Validation" below. Note: `notion_journal_addition` renamed to `obsidian_entry_addition` in v3.21.)

### Default-true rule for new tools

If `/ai-registry` returns valid JSON but the `evaluation_required` field is **missing or null** AND the original hand-off package had `air_id: "new"`, `/standup` defaults to `evaluation_required.required = true` and chains Gate 1 automatically.

If the original hand-off had a specific `air_id` (enrichment, status update, etc.), the missing field defaults to `false` (no chain).

### Context Separation Rule

Never copy or embed reference documents, gate criteria, scoring matrices, evaluation forms, registry templates, or Linear-context tables from `/ai-registry` or `/ai-tool-evaluation` into this skill. All specialised knowledge stays inside the owning skill, accessed via subagent fork.

---

## Minimum Viable Execution Path

For every standup, the minimum required flow is:

1. Build Meeting Intelligence Digest
2. Check Obsidian idempotency in Phase 1 (skip the rest if today's file already exists and user chooses skip)
3. Match actions to Monday Automations tasks/projects
4. **Run Step 2B.1 — name-similarity scan on every candidate item/sub-item before the plan is finalised**
5. Enforce no-orphan next steps
6. **Maintain Context Coverage Invariant on every touched item — Step 3G (creates) + Step 3H (backfills) + Step 3E.1 (moves)**
7. **Run Step 3.0 — pre-create guard immediately before every Monday create call**
8. Dispatch required subagents (gated) for `/ai-registry` / `/ai-tool-evaluation` — chain Gate 1 after new-tool registry creates
9. Reconcile Linear AIP if relevant — with Conflict Safety
10. **Run Step 3I — Context Coverage Check at end of Phase 3**
11. Write Obsidian / Prime Radiant entry — with output compression
12. Emit Final Execution Report

Run deep duplicate scans, full AIP reconciliation, and subagent dispatch only when relevant.

---

## Execution Model — 3 Phases

The skill runs in three strict phases. Phase boundaries are non-negotiable: **no writes happen in Phase 1 or Phase 2.**

### Phase 1 — Analyse (read-only)
- Retrieve the Fireflies transcript (Step 1)
- Build the Meeting Intelligence Digest from the raw transcript (Step 1.5)
- **Obsidian idempotency check** — check whether the target markdown file for today already exists in the Prime Radiant vault; if yes, ask the user (skip / rerun / abort) before proceeding (Step 1.6)
- Parse the Digest into typed items (Step 2)

### Phase 2 — Plan (read-only)
- Match items to Monday Automations / Linear AIP using confidence scoring (Step 2A)
- Run the Duplicate Detection layer with refined keyword rules (Step 2B)
- **Run Step 2B.1 — Pre-Create Name-Similarity Scan on every candidate item and sub-item** (blocks high-confidence duplicates from the plan; flags medium-confidence for user confirmation at Step 2E)
- Apply Parent Project Routing — prefer attach over create (Step 2C)
- Generate the explicit execution plan (Step 2D) — including a **predicted Context Coverage check**: list every item that will be *touched* in Phase 3 and predict which will need Step 3G (create), Step 3H (backfill), and Step 3E.1 (move-rationale) Description Updates. Surface the count.
- Apply the **Subagent Dispatch Gate** to every potential hand-off package (Step 2D.1)
- If any plan element has medium confidence (60–84%) or other ambiguity, present the plan to the user (Step 2E)

### Phase 3 — Execute (writes)
- Apply the **Execution Control Mode** check first
- **Run Step 3.0 — Pre-Create Guard immediately before every create call** (re-checks live board state; blocks any duplicate not caught in Phase 2)
- Apply writes in this **strict priority order**:
  1. Monday Automations writes — Step 3
     - 3A source bumps, 3B sub-items, 3C substantive Updates, 3D new parents, 3E completed-moves to Done, **3E.1 group-move rationale Updates** (any move; bulk reorganisations included)
     - **3G Description Update on every create** (parents + sub-items)
     - **3H Backfill Description Update on every touched-but-undocumented existing item**
  2. No-orphan next-step pass — Step 3.5
  3. Subagent dispatch — Step 3.7
  4. Linear AIP reconciliation — Step 4
  5. **Step 3I — Context Coverage Check** (mandatory; covers every item touched in 3A/3B/3D/3E/3E.1/3.5/3.7E)
  6. Obsidian / Prime Radiant entry — Step 5
  7. Final Execution Report — Step 6

Confidence resolution at write time:
- **High (≥85%)** → execute automatically (subject to Strict Write Safety Rules)
- **Medium (60–84%)** → ask before writing (already surfaced in Phase 2)
- **Low (<60%)** → see Strict Write Safety four-criterion gate

---

## Execution Priority Order

```
1. Monday Automations writes
   ├─ Step 3.0 Pre-Create Guard (runs before every create call)
   ├─ 3A/3B/3C/3D/3E/3E.1 (touches + moves)
   ├─ 3G (Description Update on every create)
   └─ 3H (Backfill Description Update on every touched-but-undocumented existing item)
2. No-orphan next-step pass
3. Subagent dispatch (gated, validated, volume-controlled, chained)
4. Linear AIP reconciliation (with Conflict Safety)
5. Step 3I — Context Coverage Check (mandatory)
6. Obsidian / Prime Radiant entry (compressed, Step 5)
7. Final Execution Report (incl. coverage line, backfill / move-rationale counts, dedup results, failures)
```

**Never skip this order.** Step 3I cannot pass until 3G + 3H + 3E.1 have all succeeded for every touched item.

---

## Execution Control Mode

At the start of Phase 3, evaluate the plan complexity. **If ANY of the following are true:**

- The transcript is long or topic-dense (multiple distinct subjects, > ~30 minutes, > ~50 turns)
- The execution plan contains **more than 15 actions** (updates + creates + sub-items + Updates posts + Description Updates + Step 3H backfills + Step 3E.1 move-rationales, summed)
- **Subagent dispatch count > 3** (count chained dispatches too — registry + evaluation = 2)
- **Multiple medium-confidence (60–84%) matches exist**

**Switch to "Controlled Execution Mode":**

1. Complete Phase 1 (Analyse)
2. Complete Phase 2 (Plan) — note expected chained dispatches and **predicted Context Coverage counts (creates / backfills / move-rationales)** in the plan
3. Present the **full execution plan** to the user
4. **Wait for explicit confirmation** — the literal phrase `Approve execution`
5. **Do not proceed to Phase 3** until the user confirms

If none apply, proceed to Phase 3 normally.

### Compact Execution Reminder

Compact internal checkpoints during long runs:

1. Digest complete
2. Plan complete (with predicted coverage counts + dedup scan results)
3. Approval received (if Controlled Execution Mode triggered)
4. Monday writes complete (incl. Step 3G creates + Step 3H backfills + Step 3E.1 moves; Step 3.0 guard applied before each create)
5. No-orphan pass complete
6. Subagents complete (registry + chained evaluations)
7. AIP reconciliation complete
8. **Step 3I Context Coverage Check passed**
9. Obsidian entry written + pushed
10. Final Report emitted

---

## Dry-Run / Preview Mode

If the user uses any of the following phrases when triggering the skill:
- "dry run"
- "preview only"
- "plan only"
- "do not execute"
- "analyse only"
- "no writes"

Then run **only Phase 1 and Phase 2**. **Do NOT run Phase 3.**

In dry-run mode: same as before, plus the dry-run output now includes a **predicted Context Coverage block** — counts of expected Step 3G / 3H / 3E.1 posts, and a **Deduplication Scan Results block** — items blocked and items flagged for confirmation. Do NOT post any Updates or create any items.

### Dry-run output format

```markdown
## Standup Dry Run — AIO DD Mon YYYY

### Digest Summary
- Topics:
- Decisions:
- Action items:
- Tool mentions:
- Blockers:

### Proposed Monday Changes
- Updates (existing items):
- New parent items:
- Sub-items:
- Substantive Update posts:
- **Description Updates (Step 3G — one per newly created item / sub-item):**
- **Backfill Description Updates (Step 3H — one per touched-but-undocumented existing item):**
- **Group-move rationale Updates (Step 3E.1 — one per moved item):**
- Per-meeting next-step stubs:

### Deduplication Scan Results (Step 2B.1)
- Candidates scanned: X
- Blocked (high-confidence duplicate ≥3 tokens): A
  - "<candidate name>" → matches existing item "<existing name>" (id: XXXXXXX)
- Flagged for confirmation (medium confidence, 2 tokens): B
  - "<candidate name>" → potential match "<existing name>" (id: XXXXXXX)
- Cleared to create: C

### Predicted Context Coverage
- Items to touch: X
- Step 3G creates: A
- Step 3H backfills predicted: B
- Step 3E.1 moves predicted: C
- Already covered (no action needed): D
- Total Description-Update posts expected: A + B + C

### Proposed Subagent Dispatches
(unchanged from v3.12)

### Proposed Linear AIP Reconciliation
(unchanged)

### Draft Obsidian Entry
(compressed preview)

### Requires User Confirmation
(unchanged)

### Next Step
Say "Approve execution" to proceed with Phase 3.
```

The dry-run output is the only artifact produced. No Final Execution Report is emitted in dry-run mode.

---

## Strict Write Safety Rules

These rules apply to every Phase 3 write to Monday and Linear AIP.

**Never change** Status, Owner, Timeline, or Group **unless one of the following is true:**
- The change is explicitly stated in the transcript
- There is clear completion evidence
- The owner directly confirmed it during the standup
- The change is required by Linear AIP ↔ Monday reconciliation **and the transcript or completed Monday execution authorises it** (see AIP Conflict Safety, Step 4)
- The change is the documented operational return of a subagent dispatch — specifically `monday_task_required.required == true`
- The change is a **user-directed bulk reorganisation** (e.g. "move all department-specific tasks out of Planned Automations") — in which case Step 3E.1 move-rationale Updates are mandatory on every moved item

**If uncertain → DO NOT WRITE → ASK USER.**

This rule overrides the confidence rubric. Confidence answers "is this the right item?", not "is this the right write?". Both must hold.

**Low confidence (<60%) does NOT automatically create.** Create only if all four hold:
- The action is specific (concrete imperative)
- The owner is clear (named person, "Both", or external)
- It has a clear project/task context
- It is genuinely standalone

Otherwise add to **Requires User Confirmation**; do not create a Monday item.

Touch-only writes (Source column updates) are exempt from confidence gating but **do trigger Step 3H backfill** if the touched item lacks a Description Update.

**Description Updates are mandatory on every touched item** — Step 3G covers creates, Step 3H covers existing items, Step 3E.1 covers moves. Skip only if the idempotency header check confirms one is already present.

**Chained evaluation dispatches (Step 3.7D.1) are exempt** from explicit user-confirmation requirements at write time.

---

## Owner Assignment Rules

**If owner is "Both":** assign both Jehad and Michael if both Monday IDs exist.

**If owner is external or has no Monday ID** (Andrew, Bonaventure, Ann, Joyce, Lisandro, Andre, Euclid, etc.): leave the Monday Owner column blank; mention the external owner narratively in the Description Update and the Monday Update post.

**If owner is unclear:** do not assign anyone; add to the Final Report under "Missing / unclear owners".

**Never invent Monday user IDs.**

---

## Action Sub-Item Naming Convention

Use **Verb + object + context**.

✅ Good: "Send Monday API token to Lisandro" / "Schedule Bonaventure finance dashboard follow-up" / "Review Fireflies custom vocabulary gaps" / "Draft scope doc for Executive Management System"

❌ Bad: "Follow up" / "Check this" / "Discuss" / "Update task" / "Action item"

Production stage sub-items use Plan / Build / Test / Deploy / Monitor.

---

## Architecture

```
Fireflies raw transcript  ◄── canonical
        │
        ▼
  Meeting Intelligence Digest (Phase 1)
        │
        ▼
  Obsidian idempotency check ──── ask user if today's file exists
        │
        ▼
  Match + duplicate-detect + parent-route ── confidence scoring
        │
        ▼
  Step 2B.1 — Pre-Create Name-Similarity Scan ── blocks/flags duplicates before plan is finalised
        │
        ▼
  Subagent Dispatch Gate (register every tool — drop only zero-context market references)
        │
        ▼
  Execution Plan (Phase 2 — predicted Context Coverage counts + dedup scan results attached)
        │
        ▼
  Execution Control Mode check ── if large/ambiguous → wait for "Approve execution"
        │
        ▼
  Phase 3 — strict priority order
        ├── Step 3.0: Pre-Create Guard ── re-checks live board state before every create call
        ├── Monday Automations writes
        │     ├── Step 3G: Description Update on every create
        │     ├── Step 3H: Backfill Description Update on every touched-but-undocumented item
        │     └── Step 3E.1: Move-rationale Update on every group change
        ├── No-orphan next-step pass
        ├── Subagent dispatch (gated, validated, volume-controlled, chained)
        ├── Linear AIP reconciliation (with Conflict Safety)
        ├── Step 3I: Context Coverage Check (mandatory; gates Step 5/6)
        ├── Obsidian / Prime Radiant write (Step 5 — sources/meetings/YYYY-MM-DD-<slug>.md; Obsidian Git handles commit/push)
        └── Final Execution Report (incl. coverage line, dedup results, failures)
```

---

# PHASE 1 — ANALYSE

## Step 1 — Retrieve the Fireflies Transcript

Search Fireflies (broad keyword + ±1 day window) and fetch the **raw transcript only**.

```
Tool: Fireflies:fireflies_search
Query: keyword:"AIO" scope:title from:<day-before> to:<day-after>

Tool: Fireflies:fireflies_get_transcript
transcriptId: <id>
```

> ⛔ **Never call `fireflies_get_summary`.** The Fireflies AI summary is unreliable and must never be used as input to the Digest or any downstream phase — only the raw transcript sentences are authoritative (Step 1.5 reinforces this).
>
> ℹ️ **If the transcript output is too large for inline display** (the tool response shows "Output too large… Full output saved to: `<path>`"), use the `Read` tool on that exact persisted file path to load the full transcript before building the Digest.

If zero results, retry with `keyword:"standup"`. If multiple, confirm with user.

---

## Step 1.5 — Build the Meeting Intelligence Digest

**The Fireflies summary is unreliable.** The raw transcript is the only source of truth.

Construct a structured Digest with: Attendees, Topics discussed, Decisions made, Open questions, Action items, Blockers, Tool mentions, Project/task references, Implied next steps.

The Digest is the input to every downstream phase.

---

## Step 1.6 — Obsidian / Prime Radiant Idempotency Check

Resolve the target file path for today's standup:

```
{{PRIME_RADIANT_VAULT}}/sources/meetings/YYYY-MM-DD-aio-standup.md
```

(default: `~/janus/prime-radiant/sources/meetings/2026-05-18-aio-standup.md` for today)

Check whether the file already exists using bash:

```bash
stat ~/janus/prime-radiant/sources/meetings/YYYY-MM-DD-aio-standup.md
```

If the file exists, stop and ask the user: **(a)** skip (do not reprocess — default) / **(b)** rerun new findings only (delete the existing file first, then continue) / **(c)** abort.

Default (a). **No Monday, Linear, or subagent writes occur until the user chooses.**

**If the user chooses (c) abort:**
- Stop the run immediately
- Do not perform Phase 2 or Phase 3
- Emit only a brief abort notice — no Final Report.

---

## Step 2 — Parse the Digest into Typed Items

Categories: A. Status Updates / B. Decisions / C. New Action Items / D.1 Production Stage sub-items / D.2 Action sub-items / E. Tool Mentions (ALL tools — SaaS, AI, infrastructure, analytics, creative, email, hosting, etc.) / F. Items Completed / G. Cancellations / H. Next-Step Actions.

Every category E item flows to a Dispatch Gate check at Step 2D.1. The default outcome of the gate is to dispatch — the gate drops only zero-context market references.

Valid Monday Automations status transitions: Backlog → In Definition → In Development → In Testing → In Production. Postponed and Deprecated are off-cycle.

Every next-step (H) must carry Action / Owner / Time horizon / Due date / Linked Monday item — no exceptions.

---

## Step 2A — Confidence Scoring for Matching

Additive rubric (max 100): exact name +50, owner overlap +20, topic match +15, explicit verbal reference +20, AIP link match +25, recency +5, sub-item references +10, meaningful Updates-body match +15, recent Source tag +5, ambiguous overlap −15.

Buckets: ≥85% silent / 60–84% ask / <60% does not auto-create.

---

# PHASE 2 — PLAN

## Step 2B — Duplicate Detection Layer

Search across: parent names, sub-item names, Updates body (last 30 days), Link column, Source column (last 5 standup tags).

**Refined Updates-body match rules.** A match counts as duplicate evidence only when at least one of these holds:
- **At least 2 meaningful keywords** match
- **An AIP/AIR reference** matches (regex `/AI[PR]-\d+/`)
- **Same owner + project/tool name** both appear

Generic words contribute zero on their own: `next step`, `follow up`, `AIO`, `standup`, `update`, `tool`, `task`, `action`, `meeting`, `discuss`, `review`, `check`.

Buckets: ≥85% reuse / 60–84% ask / <60% new only if Strict Write Safety four-criterion gate passes.

---

## Step 2B.1 — Pre-Create Name-Similarity Scan (NEW in v3.22)

Runs **immediately after Step 2B**, for every candidate item or sub-item in the execution plan — before the plan is finalised and presented to the user.

**Purpose:** Step 2B detects duplicates via Updates-body keyword matching. This step adds a direct name-similarity scan against the live sub-items board (`5095012849`) and main board (`5095012818`), which Step 2B alone does not cover. Root cause of prior duplicate accumulation: sub-items are stored on a separate board and are not returned in a standard parent-item board fetch — so they were invisible to Step 2B.

**Algorithm:**

For each candidate item name in the plan:

1. **Tokenise the candidate name.**
   - Lowercase, strip punctuation.
   - Remove stop words: `the`, `a`, `an`, `for`, `and`, `or`, `to`, `with`, `via`, `on`, `of`, `in`, `from`, `by`, `at`, `as`, `is`, `it`, `its`, `be`, `not`, `this`, `that`, `we`, `our`, `all`, `up`, `get`, `set`, `run`, `build`, `add`, `create`, `new`, `use`, `make`, `into`, `out`, `how`, `when`.
   - Remaining tokens are **meaningful tokens**.

2. **Search the relevant board(s).**
   - For sub-item candidates: call `get_board_items_page(boardId: 5095012849, searchTerm: <first meaningful token>, limit: 50)`.
   - For parent-item candidates: call `get_board_items_page(boardId: 5095012818, searchTerm: <first meaningful token>, limit: 50)`.
   - Also search the main board for sub-item candidates (some sub-items may be promoted to parents in future). One search per candidate is sufficient.

3. **Score each result.**
   - Count how many of the candidate's meaningful tokens appear in the existing item's name (case-insensitive, partial match on ≥4-character tokens).
   - Use the highest-scoring existing item as the match candidate.

4. **Apply match thresholds:**

   | Token overlap | Confidence | Action |
   |---|---|---|
   | ≥3 meaningful tokens | HIGH — duplicate | Remove candidate from plan. Log in Final Report under "Deduplication — Blocked." |
   | 2 meaningful tokens | MEDIUM — possible duplicate | Flag in plan. Add to "Requires User Confirmation" at Step 2E — do not create until user confirms. |
   | 0–1 meaningful tokens | LOW — likely distinct | Proceed with creation as planned. |

5. **Log the scan results** in the Phase 2 plan output — a "Deduplication Scan Results" block listing: candidates scanned / blocked (with existing item name + id) / flagged for confirmation / cleared to create. This block is also included in the Dry-Run output.

**What this step does NOT replace:**
- Step 2B still runs first — Updates-body matching catches semantic duplicates even when names differ.
- Step 3.0 re-runs this scan at execution time against live board state.
- Step 2B.1 is about name similarity; Step 2B is about content similarity. Both are needed.

**Performance note:** search calls are read-only and count toward Phase 2 (no-write phase). If a single standup has >10 candidate creates, batch the searches — one search per first meaningful token covers multiple candidates sharing the same lead token.

---

## Step 2C — Parent Project Routing

**Default preference: attach over create.** ≥85% attach as Action sub-item / 60–84% ask / <60% new parent only if all four new-parent criteria hold.

---

## Step 2D — Generate the Execution Plan

Plan sections: Items to update / Items to create / Sub-items to create / Updates to post / **Description Updates to post — Step 3G (creates) + Step 3H (backfills) + Step 3E.1 (moves), with predicted counts** / **Deduplication Scan Results (Step 2B.1)** / Subagent hand-off packages / Linear AIP reconciliation candidates / Obsidian entry draft / Requires User Confirmation.

**Coverage prediction:** for every item that will be touched in Phase 3, predict whether it already has a Description Update header. The plan's Predicted Context Coverage block lists creates / backfills / moves / already-covered counts so the user sees the full per-create *and* per-touch context cost.

### 2D.1 Subagent Dispatch Gate — Every Tool Gets Registered (v3.18)

**The rule: every tool mentioned in any meeting must be checked against Linear AIR.** There is no category of tool that is exempt — not web hosting, not transactional email, not analytics, not creative tools, not AI platforms. All of it. The registry exists so Janus has a complete picture of every tool in use or under consideration, and that purpose only works if every tool makes it in.

**The only things that do NOT trigger a dispatch:**
- A tool mentioned purely as an abstract industry/market reference with zero operational context — e.g., "I read that Google launched X" with no indication of intent to use, trial, compare, or evaluate it.
- A tool that was immediately and explicitly dismissed — e.g., "We looked at Y briefly but it's definitely not for us" (and no further discussion followed).

Everything else passes: tools being adopted, trialled, compared, already in production but not yet registered, or mentioned as a solution to a problem — all of these require a dispatch.

**Algorithm for every tool mention (category E items from Step 2):**

1. **Extract the tool name** from the transcript. Include the vendor name if known (e.g., "Recent.io" not just "Recent").

2. **Check Linear AIR** — search for an existing entry before deciding on any action. Do not assume something is or isn't registered.

3. **Route based on what you find:**

   | Situation | Action |
   |---|---|
   | Entry **does not exist** | Dispatch `/ai-registry` to create a Backlog entry. Chain `/ai-tool-evaluation` Gate 1 automatically (v3.10 default-true rule). |
   | Entry **exists** AND meeting discussed new information (new decision, cost data, adoption outcome, use case, comparison result) | Dispatch `/ai-registry` for enrichment. Chain `/ai-tool-evaluation` if the new information changes the evaluation picture (e.g., a production adoption warrants Gate 2/3 reassessment). |
   | Entry **exists** AND no new information discussed (tool mentioned in passing, already fully documented) | Log as "already registered — no new information, skipped" in the Final Report. No dispatch needed. |

4. **Set urgency from the transcript context:**
   - Tool was adopted as an explicit decision in this meeting → `by-next-standup`
   - Tool is being actively trialled or evaluated → `this-week`
   - Tool was mentioned as a future consideration or passing reference → `longer`

5. **Populate the hand-off package** (Subagent Hand-Off JSON Schema below). The `transcript_evidence` array must contain at least one verbatim or near-verbatim excerpt that mentions the tool and its context.

**Don't classify the tool type before dispatching.** If you're unsure whether something is an "AI tool" vs "SaaS" vs "infrastructure," do not use that uncertainty to skip it. The `/ai-registry` skill handles classification. Your job is to ensure every tool exits a meeting with a Linear AIR check completed.

**Volume control:** if a meeting mentions more than 5 distinct tools, batch the dispatches — run all `/ai-registry` checks first in the plan, then chain evaluations. Do not let evaluation wait times block Monday writes. Evaluations run async; Monday writes cannot.

**This gate's job is to let tools through, not to stop them.** Under-registration is the failure mode, not over-registration. When in doubt, register.

---

## Step 2E — Plan Presentation & Approval

Present the plan and wait for approval if any ambiguity exists or if Execution Control Mode triggers fire (incl. ≥15 actions counting predicted Step 3H backfills + Step 3E.1 moves toward the threshold). The plan **must include** the Deduplication Scan Results block from Step 2B.1 — items blocked and items flagged for user confirmation are listed here and require explicit user response before Phase 3 proceeds.

---

# PHASE 3 — EXECUTE

**Run the Execution Control Mode check first.** If any of its four conditions hold, wait for `Approve execution` before proceeding.

Apply writes in the strict priority order. Every write below assumes Phase 2 produced an approved plan.

## Step 3.0 — Pre-Create Guard (NEW in v3.22)

Runs **immediately before every `create_item` or sub-item creation call** in Phase 3. This is the execution-time layer of the Deduplication Gate — it catches duplicates that were missed in Phase 2 (e.g. because the item was created by another run or manually between Phase 2 scan time and Phase 3 execution time).

**Algorithm:**

1. Before executing any create call for a candidate item or sub-item, re-run the Step 2B.1 name-similarity scan against the **live current board state**.
2. Apply the same token-overlap thresholds:
   - ≥3 meaningful tokens → **BLOCK**: do not create. Log under Issues/Warnings: `"<candidate name>" blocked at Step 3.0 — duplicate of existing item "<existing name>" (id: XXXXXXX)`. Continue to the next item.
   - 2 meaningful tokens → **BLOCK and surface**: same as above, but surface prominently in the Final Report under "Deduplication — Blocked at Execution Time". Do not create.
   - 0–1 tokens → **PROCEED**: execute the create call as planned.

3. **If a candidate is blocked at Step 3.0** (not caught in Phase 2):
   - Skip the creation.
   - Skip the corresponding Step 3G Description Update (nothing was created).
   - Log the match in the Final Report under "Issues / Warnings — Deduplication" with the candidate name, existing item name, and existing item id.
   - **Do not block other Phase 3 creates.** One blocked item does not halt the execution run.

4. **Idempotency:** this check is live-state, not plan-state. The search call is read-only. It adds at most one `get_board_items_page` call per candidate — acceptable overhead.

**What Step 3.0 does NOT do:**
- It does not replace Step 2B.1. Phase 2 blocking prevents wasted plan-presentation and user-confirmation cycles. Both layers are needed.
- It does not retroactively block items already created in earlier Phase 3 steps within the same run. The guard applies before each new creation, not to items already written.

---

## Step 3 — Update Monday Automations Board

Board `5095012818`. Sub-steps:

- **3A. Update existing item** via `change_item_column_values` with Source column populated as `<meeting tag> DD Mon YYYY` (`AIO 6 May 2026`, `AI/IT Mtg 6 May 2026`, `Bonaventure 4 May 2026`, etc.). Status / Owner / Timeline subject to Strict Write Safety. **Touching an item triggers Step 3H if it has no Description Update.**
- **3B. Add a sub-item** — 3B.1 Production Stage (Plan / Build / Test / Deploy / Monitor) or 3B.2 Action (Verb + object + context). **Each sub-item triggers Step 3G. Step 3.0 runs immediately before each sub-item creation call.**
- **3C. Post an Update** via `create_update` — HTML only. (For substantive decision / findings posts on existing items. Does NOT replace Step 3H — substantive Updates and Description Updates serve different purposes.)
- **3D. Create a new parent item** — only when Step 2C parent routing yielded "create new parent" AND Strict Write Safety low-confidence rule passes. **Each new parent triggers Step 3G. Step 3.0 runs immediately before the creation call.**
- **3E. Move completed items to Done group** when shipped. Deprecated stays in place. **Each move triggers Step 3E.1.**
- **3E.1. Group-move rationale Update (NEW in v3.13).** Every time the skill moves an item between groups — Step 3E completion-move, Step 3.7 routing decision, or any user-directed bulk reorganisation — post a one-paragraph Update on the moved item explaining *why* the move happened. Format:

  ```html
  <p><strong>Group move — DD Mon YYYY</strong></p>
  <p>Moved from <em>&lt;old group&gt;</em> to <em>&lt;new group&gt;</em>.</p>
  <p><strong>Reason:</strong> &lt;transcript-derived rationale OR routing-table reasoning OR user-directed reorganisation rationale&gt;</p>
  <p><strong>Source:</strong> &lt;meeting tag DD Mon YYYY&gt; (or "User-directed bulk reorganisation DD Mon YYYY" if no meeting)</p>
  ```

  Idempotency: skip if a `<strong>Group move — DD Mon YYYY</strong>` block for the same date is already present in the item's Updates timeline.

- **3F. Verify** — re-fetch the board; spot-check items touched.

- **3G. MANDATORY Description Update on every newly created item / sub-item.** Format template (HTML, no Markdown):

  ```html
  <h2>Description (from meeting notes)</h2>
  <p><strong>Source:</strong> <meeting + date> — <a href="<fireflies-url>">Fireflies recording</a></p>
  <p><strong>Why:</strong> <transcript-derived rationale, 1–2 sentences></p>
  <p><strong>Definition of done:</strong> <one-sentence outcome></p>
  <p><strong>Depends on / Related:</strong> <ids or names></p>
  <p><strong>Quote:</strong> <optional direction-setting line></p>
  <p><em>Note: this content lives in Updates because Monday's set_item_description_content mutation is currently broken for newly created items (HTTP 500 against null description docs at API version 2026-07).</em></p>
  ```

  **Idempotency:** before posting, fetch the item's Updates and search for `<h2>Description (from meeting notes)</h2>`. If present, skip — never post a second Description Update.

  **Failure handling:** if the post fails, retry once. If it still fails, log under "Issues / Warnings"; do not block Phase 3 on a single failure.

- **3H. MANDATORY Backfill Description Update on every touched existing item that lacks one (NEW in v3.13).** When the skill touches an existing item via 3A (source bump), 3C (substantive Update), 3.5 (next-step stub), 3.7E (subagent-driven follow-up task linked to existing parent), and the item has *no* `<h2>Description (from meeting notes)</h2>` block in its Updates timeline yet, post one. Same template as Step 3G with three modifications:

  - **Source** field — the meeting that touched this item in this run (or "Best-effort backfill — DD Mon YYYY" if the touch was a user-directed reorganisation with no meeting).
  - **Why** field — derived in priority order: (1) current-meeting transcript evidence if the touch is meeting-driven; (2) the most informative existing Update body via the Step 2B Updates-body grep; (3) the item name + group routing as a last-resort one-liner.
  - **Backfill disclaimer** — append a single-line note: `<p><em>Backfilled context — item predates the v3.11 / v3.12 Description Update convention or was created without one. Best-effort reconstruction from current standup + prior Updates.</em></p>`

  Same idempotency check as Step 3G — never post a second one.

  **Failure handling:** retry once. If it still fails, log under "Issues / Warnings" with the item id; **the Step 3I Context Coverage Check will catch the miss and surface it in the Final Report**.

  **Optional escalation path (Option A — seed-and-fill):** If the user has manually opened the item in the UI to seed the description doc, the skill MAY attempt `set_item_description_content(item_id, markdown)` after the Step 3H Update succeeds. Same fallback policy as Step 3G.

---

## Step 3.5 — No-Orphan Next-Step Pass (STRICT)

Each next-step needs all four required fields. Match → ≥85% silent / 60–84% ask / <60% Strict Write Safety four-criterion gate.

If creating new, prefer Action sub-item via Step 2C parent routing. Defaults: new Automations parent `In Definition`; Action sub-item `Working on it`.

**Newly created items / sub-items in this pass also get a Step 3G Description Update. Step 3.0 runs before each creation call.**
**Existing items touched in this pass also get Step 3H if uncovered.**

Idempotency: before posting `Next step from <meeting tag> DD Mon YYYY` stub on a Monday item, fetch the item's Updates and search for the literal string. Skip if present.

---

## Step 3.7 — Subagent Dispatch (gated, validated, volume-controlled, chained)

Execute every hand-off package authorised in Step 2D.1. Process in the order: all `/ai-registry` dispatches first, then chain `/ai-tool-evaluation` based on their returns.

**3.7A — Dispatch `/ai-registry`** via the Task/Agent tool (never the `Skill` tool — loading sibling skills co-resident in this conversation causes instruction collisions). Pass the full hand-off JSON schema. One subagent per tool.

**3.7B — Validate the return.** Expect structured JSON per the Subagent Return Schema. Check for: valid JSON, `action_completed` field, `linear_air_issue` (AIR-N). If malformed or missing required fields, retry the dispatch once with the same package. If still failing, log under "Subagent Failures" in the Final Report and continue — do not block other dispatches.

**3.7C — Chain `/ai-tool-evaluation` Gate 1** when ANY of the following is true:
- `evaluation_required.required == true` in the return
- The original hand-off had `air_id: "new"` and `evaluation_required` is absent or null (v3.10 default-true rule)
- A previously existing entry was enriched with information that materially changes the evaluation picture (e.g., production adoption, new cost data, changed vendor terms)

Dispatch `/ai-tool-evaluation` as a second Task/Agent call with the evaluation hand-off package. Include the `linear_air_issue` (AIR-N) returned from `/ai-registry` so the evaluator writes its Gate 1 output to the correct Linear issue.

**3.7D — Create Monday Automations follow-up task** if `monday_task_required.required == true` in the return. Examples: "Test Canva in sandbox," "Review Hostinger pricing against existing AWS spend," "Schedule vendor demo for Recent transactional email." **Step 3.0 runs before the creation call. Apply Step 3G Description Update to the new task immediately after creation.**

**Subagent Task Volume Control:** if a single tool generates more than 3 follow-up Monday tasks, consolidate them under one parent with sub-items. Both the consolidated parent and each sub-item receive Step 3G Description Updates.

**3.7E — Log all outcomes** for the Final Report → "AI Registry / Tool Evaluation Subagents" section:
- Tool name
- AIR-N created or enriched (link)
- Evaluation outcome: Gate 1 pass / fail / pending / skipped (if entry already fully evaluated)
- Monday follow-up task created (if any, with item id)
- Any enrichment added to an existing entry
- Any subagent failures

---

## Step 3I — Context Coverage Check (NEW in v3.13, MANDATORY)

After Phase 3 has applied all writes (Steps 3 / 3.5 / 3.7) and before Linear AIP reconciliation (Step 4), run the Context Coverage Check.

**Algorithm:**

1. Build the **touched-items set**: every Monday item id that received any write in this run — Source bumps, status / owner / timeline / group changes, sub-item additions, Updates posts, subagent-driven follow-ups, completion moves to Done, bulk reorganisation moves.
2. For each touched item, fetch its current Updates timeline.
3. Search for `<h2>Description (from meeting notes)</h2>` in the Updates body.
4. **If present:** ✅ counted as covered. Continue.
5. **If absent:** ❌ run Step 3H backfill *now*. Re-check.
6. **If post-backfill the header is still absent (post failed twice):** ❌ flagged as a coverage failure. Logged under Final Report Issues/Warnings with the item id and a "manual recovery" recommendation.
7. **For every item moved between groups in this run:** also verify a `<strong>Group move — <today's date></strong>` block is present. If absent, post it via Step 3E.1 *now*.
8. Emit the coverage tally for the Final Report — `X/X items covered (A direct creates Step 3G, B backfills Step 3H, C move-rationales Step 3E.1, D failures)`.

The check is **idempotent** — running it twice in a row produces no additional posts. It is also safe across re-runs of the same standup.

**Failure handling:** Step 3I never blocks Phase 3 from continuing to Step 5 or Step 6 (Final Report). Coverage failures are surfaced loudly so they can be fixed manually.

---

## Step 4 — Linear AIP Reconciliation (with Conflict Safety)

(Unchanged from v3.12 — see "Linear AIP Conflict Safety" below.)

---

## Step 5 — Write the Forward-Looking Entry to Prime Radiant / Obsidian

Write the standup entry as a meeting-parser-compatible markdown file directly into the single-vault Prime Radiant at `sources/meetings/`. This is the **sole journal write** — there is no Notion write. The entry is first-class Prime Radiant content: searchable in Obsidian, immediately consumable by `/janus-brain`'s downstream tooling, and correctly filed alongside all other meeting sources. The `parser_version: 3` field prevents re-processing by the applier.

**Sequencing:**

1. Runs **after** Step 3I (Context Coverage Check) — coverage tally is included in the entry body.
2. Runs **before** the Final Execution Report — the write result is included in Summary + Issues / Warnings if it failed.
3. **Does NOT block any Phase 3 step upstream.** Failures here never re-trigger Monday writes or block the Final Report.

**Target:**

`{{PRIME_RADIANT_VAULT}}/sources/meetings/YYYY-MM-DD-<slug>.md`

where `YYYY-MM-DD` is the standup date and `<slug>` is the meeting slug (e.g. `aio-standup`, `aio-mktg-it-meeting`).

Default `{{PRIME_RADIANT_VAULT}}`: `~/janus/prime-radiant/` (single-repo root).

**Algorithm:**

1. **Resolve `{{PRIME_RADIANT_VAULT}}` and `{{CAPTURED_BY_SLUG}}`.** Read the configured vault root (Reference section). If unset, fall back to `~/janus/prime-radiant/`. Derive `{{CAPTURED_BY_SLUG}}` by: (a) matching `git config --global user.email` against `people/*/` directory names in the vault, or (b) using the single `people/*/` directory if only one exists, or (c) defaulting to `jehad-altoutou`. If the vault root does not resolve to an existing directory with a `.git/` subdirectory, log `obsidian_write: skipped (vault not found)` and continue.
2. **Pre-write freshness check (no git ops).** Do NOT run `git pull` from the sandbox — this can also conflict with Obsidian Git's auto-pull and leave lock files. The vault on disk is Obsidian Git's responsibility; assume it is reasonably current. Proceed directly to the directory check.
3. **Directory check.** Ensure `<vault>/sources/meetings/` exists; create with `mkdir -p` if not.
4. **Idempotency check.** Stat the target path `<vault>/sources/meetings/YYYY-MM-DD-<slug>.md`. If it already exists, skip the write and log `obsidian_write: skipped (file already present at <full path>)`. Do not overwrite.
5. **Compose front-matter** per the meeting-parser schema in `Reference: Prime Radiant Write`:
   - `type: source`
   - `source_type: meeting`
   - `title`: `AIO Standup DD Mon YYYY`
   - `slug`: `YYYY-MM-DD-aio-standup`
   - `created`: standup date in `YYYY-MM-DD` form
   - `captured_by`: vault owner's slug (default `jehad-altoutou`; override via `{{CAPTURED_BY_SLUG}}`)
   - `fireflies_id`: Fireflies transcript id from Step 1
   - `fireflies_url`: full Fireflies recording URL from Step 1
   - `attendees`: YAML list of attendee real names from the Digest (e.g. `[Michael Bruck, Jehad Altoutou]`)
   - `duration_min`: rounded meeting duration in minutes
   - `audience`: `department`
   - `departments`: `[ai-office]`
   - `standup_skill_version`: `v3.22` (lets `/janus-brain` identify standup-written files)
   - `parser_version`: `3` (matches `/janus-brain` 2026-05-14 applier; prevents re-processing)
   - `related`: YAML list of every Monday item id touched in Phase 3 (from the Step 3I touched-items set) plus any `AIR-N` / `AIP-N` references touched by subagents
6. **Compose body.** The body is the full forward-looking standup entry — the same content that previously went to Notion. Sections:
   - **Clean Meeting Summary** (3–5 sentences, past tense, no jargon)
   - **🎯 Next steps — by next standup** (actions due before tomorrow's standup)
   - **📅 Next steps — this week** (actions due within the current week)
   - **🏔️ Next steps — longer horizon** (anything beyond this week)
   - **Decisions made** (bullet list)
   - **Findings / context** (supporting detail, blockers, open questions)
   - **Monday items touched** — list with Monday item links and coverage line: `✅ X items, ⚠️ Y backfilled, ➡️ Z move-rationales, ❌ W coverage failures`
   - **Linear AIP reconciliation** — changes applied, conflicts logged
   - **AI Registry / Tool Evaluation outcomes** — per-tool registry + Gate 1 results
   - Every next-step bullet carries: Action / Owner / Time horizon / Due date / Monday item link
7. **Write.** Concatenate front-matter + `\n\n` + body and write atomically (write-to-temp + rename) to the target path. UTF-8, LF line endings.
8. **Verify.** Re-read the first 14 lines to confirm the front-matter wrote intact. If verification fails, log under Issues / Warnings.

**Step 5.1 — Git: do NOT run any git commands from the sandbox.**

⛔ **Never run `git add`, `git commit`, or `git push` from the bash sandbox for this vault.**

The Obsidian Git plugin runs on the host machine on a 5-minute auto-commit + push cycle. Running git from the sandbox simultaneously creates a race condition for `.git/HEAD.lock` — whichever process runs second fails to acquire the lock and leaves a stale lock file that blocks all future git operations until manually cleared.

The file written in Step 5 is already on disk at the correct path. Obsidian Git will detect the new file on its next cycle and commit + push it automatically. No further action is needed.

Log in the Final Report: `obsidian_git: skipped — Obsidian Git handles commit/push on next 5-min cycle`.

**Step 5.2 — Local fallback (if vault write failed):**

If the vault root cannot be found or the file write fails, fall back to writing the entry to `outputs/standup-AIO-<DD-Mon-YYYY>.md` in the Cowork outputs folder. Log `obsidian_write: failed — fallback written to outputs/standup-AIO-<DD-Mon-YYYY>.md` under Issues / Warnings. The Final Report links to the fallback file.

**Idempotency notes:**

- The file-write idempotency check is purely path-based. If the user reruns the standup with the `(b) rerun new findings only` option from Step 1.6, the write will skip on the second run — delete the old file first if a clean overwrite is wanted.
- Git is not run from the sandbox — no git idempotency concern. File-existence check (step 4) prevents double-writes.

**Failure handling:**

| Failure mode | Logged as | Continues? |
|---|---|---|
| Vault root not found / no `.git/` | `obsidian_write: skipped (vault not found at <path>)` | Yes — fallback to outputs/ |
| Target file already exists | `obsidian_write: skipped (file already present at <path>)` | Yes |
| Pre-write `git pull` failed | `obsidian_write: warning — pull failed: <reason>; proceeding with local write` | Yes |
| `sources/meetings/` directory could not be created | `obsidian_write: failed — cannot create <path>: <reason>` | Yes — fallback to outputs/ |
| Permission denied | `obsidian_write: failed — permission denied at <path>` | Yes — fallback to outputs/ |
| Write threw (disk full, IO error, etc.) | `obsidian_write: failed — <error string>` | Yes — fallback to outputs/ |
| Front-matter verification failed | `obsidian_write: failed — front-matter verification mismatch` | Yes — fallback to outputs/ |
| (git ops not run from sandbox — no git failure modes apply) | `obsidian_git: skipped — Obsidian Git handles commit/push` | n/a |

Every outcome is surfaced in the Final Report Summary line (`Obsidian write (Step 5): ✅ written (Obsidian Git will commit) | ⏭️ skipped (file already present) | ❌ failed + fallback written to outputs/`).

**Single-vault visibility:**

The file lands in `sources/meetings/` within the single `~/janus/prime-radiant/` git repo — the CLAUDE.md §3 canonical path for all meeting sources. It is immediately visible in Obsidian alongside all other ingested meeting transcripts. The `departments: [ai-office]` field is retained for search and filtering.

---

## Step 6 — Final Execution Report

```markdown
## Standup Processing Report — <meeting tag> DD Mon YYYY

### Summary
- Transcript processed: ✅
- Monday items updated: X
- Monday items created: X (Y new parents, Z action sub-items, W production-stage sub-items)
- Description Updates posted (Step 3G — creates): X
- Backfill Description Updates posted (Step 3H — touches): X
- Group-move rationales posted (Step 3E.1): X
- Context Coverage: X/X covered (Y backfilled, Z move-rationales, W failures)
- Deduplication (Step 2B.1 + Step 3.0): X candidates scanned, Y blocked, Z flagged/confirmed, W blocked at execution time
- Subagent dispatches: X total
- Subagent failures: X
- AIP conflicts unresolved: X
- Obsidian entry (Step 5): ✅ written + pushed | ✅ written + push warning | ⏭️ skipped (already present | vault not found) | ❌ failed + fallback to outputs/standup-AIO-<DD-Mon-YYYY>.md
- Linear AIP changes: X applied, Y unmatched, Z conflicts unresolved
- Execution Control Mode: <auto / controlled — user approved>

### Items Updated
- [<Monday item link>] — <field>: <old> → <new> — Coverage: ✅ existing | ⚠️ backfilled | ❌ failed

### Items Created
- [<Monday item link>] — <group> / <status> / <owner> / <labels> — Description Update: ✅

### Items Moved (Step 3E and 3E.1)
- [<Monday item link>] — <old group> → <new group> — Reason: <rationale> — Move-rationale Update: ✅

### Sub-items Created
- <stage or action name> under [<parent name>](monday-link) — <owner>, due <date> — Description Update: ✅

### Updates Posted
- Substantive: <one-line summary> on [<item name>](monday-link)
- Description Updates (Step 3G — creates): <count>
- Backfill Description Updates (Step 3H — touches): <count>
- Group-move rationales (Step 3E.1): <count>
- Per-meeting next-step stubs: <count>

### Context Coverage
- Total items touched: X
- Already covered (no action): A
- Step 3G creates: B
- Step 3H backfills: C
- Step 3E.1 move-rationales: D
- Coverage failures: E (item ids + retry result + manual-recovery note)

### Deduplication
- Step 2B.1 scan (planning time):
  - Candidates scanned: X
  - Blocked (high-confidence ≥3 tokens): A — list: "<candidate>" matched "<existing>" (id: XXXXXXX)
  - Flagged for user confirmation (2 tokens): B — list with user's response
  - Cleared to create: C
- Step 3.0 guard (execution time):
  - Checks run: X
  - Blocked at execution: Y — list: "<candidate>" matched "<existing>" (id: XXXXXXX)

### AI Registry / Tool Evaluation Subagents
(unchanged from v3.10)

### Monday Follow-Up Tasks Created from Registry / Evaluation Work
(unchanged)

### Subagent Failures / Subagent Blockers / AIP Conflicts Unresolved / Requires User Confirmation / Missing or Unclear Owners
(unchanged)

### Issues / Warnings
- Duplicate risks
- Unmatched AIP issues
- Ambiguous transcript references resolved by guess
- Strict Write Safety rule triggered
- Subagent Dispatch Gate excluded
- Chained evaluation skipped
- Description Update failures (Step 3G / 3H / 3E.1 — list with item id)
- Context Coverage failures
- Deduplication blocks (Step 2B.1 — planning) and (Step 3.0 — execution)
- set_item_description_content attempts
- Obsidian write failures (Step 5 — vault not found / permission denied / write threw — with file target + fallback path)
- Obsidian git: skipped line (Step 5.1 — no git ops run from sandbox; Obsidian Git handles commit/push)

### Plan summary
- Phase 1 digest size
- Phase 2 plan: predicted vs. actual coverage counts
- Phase 2 dedup scan: blocked / flagged / cleared
- Phase 3 writes: executed vs. planned
```

If a section has no content, write `_None._`.

---

## Reference: Monday Automations Board Schema

(Unchanged from v3.12.)

### Board (`5095012818`)
URL: https://janusd-company.monday.com/boards/5095012818

**Columns:** Name, Task Owner (`multiple_person_mm2mxqy7`), Status (`color_mm2mfrpd`), Timeline (`timerange_mm2mbggm`), Priority (`color_mm2mbt5n`), Automation Type (`dropdown_mm2mkr0y`), Source (`text_mm2x5d54` — `<meeting tag> DD Mon YYYY`), Labels (`dropdown_mm2xe0sn`), Link (`link_mm2xexj3` — AIP-N URL), Subitems (`subtasks_mm2mszsh`).

**Status labels:** Backlog (`5`), In Definition (`6`), In Development (`0`), In Testing (`2`), In Production (`1`), Postponed (`4`), Deprecated (`3`).

**Groups (departments):**
| Group | ID |
|---|---|
| Planned Automations (default top group; cross-cutting only — see v3.13 Coverage Invariant) | `topics` |
| Office of CEO | `group_mm32zmaq` |
| Marketing Department | `group_mm2xfh38` |
| Operations Department | `group_mm2xtzbj` |
| ISO Department | `group_mm2xjkm2` |
| HR Department | `group_mm2m796p` |
| IT Department (added 6 May 2026) | `group_mm33y6xe` |
| Done | `group_mm2mbjs3` |

**Labels:** Office of CEO, AI Policy, Technology, Finance, Marketing, Commercial, Legal, Training, Country.

**Sub-item columns:** Name (`name`), Owner (`person`), Status (`status` — Working on it / Done / Stuck), Date (`date0`).

**Item description body API note:** `set_item_description_content(item_id, markdown)` returns HTTP 500 on freshly created items. Use Step 3G/3H Description Updates as the canonical context surface until Monday fixes the API.

### Sub-items Board (`5095012849`)
URL: https://janusd-company.monday.com/boards/5095012849

This board stores all sub-items created from the main Automations board. It is **the primary deduplication search target** for Step 2B.1 and Step 3.0 — every sub-item candidate must be checked against this board before creation. Use `get_board_items_page(boardId: 5095012849, searchTerm: <first meaningful token>)` for the name-similarity scan.

---

## Reference: Monday Person IDs

| Name | Monday User ID |
|---|---|
| Michael Bruck | `102517374` |
| Jehad Altoutou | `102517376` |
| Andrey Timokhov | `102587659` |
| Lysander | `102587655` |

People-column value format:
```json
{"<column_id>": {"personsAndTeams": [{"id": 102517374, "kind": "person"}]}}
```

**Names without Monday accounts:** Andrew, Bonaventure Wong, Ann, Joyce, Lisandro, Andre, Euclid, Tia / Dhya. Apply Owner Assignment Rules — leave blank, mention narratively in the Description Update / Update post.

---

## Reference: Linear IDs (orchestrator-side only)

### Teams
| Team | ID | Issue Prefix | Owning skill |
|---|---|---|---|
| AI Registry | `598dd614-dce5-4ede-98ef-207f3bdff33c` | `AIR-N` | `/ai-registry` |
| AI Projects | `2d1b5c04-94fd-4087-8e95-a5a7aa244a16` | `AIP-N` | reconciled by Step 4 |

### AIP Workflow Status UUIDs (Step 4)
(Unchanged.)

---

## Reference: Prime Radiant Write (Step 5 — v3.21)

**Purpose.** Canonical destination for daily standup content in the single Prime Radiant vault. The file lands as first-class meeting source content — searchable in Obsidian, immediately visible in the curator's personal meeting log, and consumable by `/janus-brain`'s meeting-digest applier. The `parser_version: 3` field prevents re-processing by the applier.

**Substrate.** Single git repo at `~/janus/prime-radiant/` (one `.git/` root covering the whole vault). Established by the `/janus-brain` 2026-05-14 rewrite.

**Path variable.** `{{PRIME_RADIANT_VAULT}}`

**Default (macOS, all employees):**

```
~/janus/prime-radiant/
```

**`{{CAPTURED_BY_SLUG}}` derivation (runtime):**

1. Run `git config --global user.email` inside the vault.
2. Match the email domain-part against `people/*/` directory names (e.g. `jehad-altoutou` for `jehada@janusd.io`).
3. If step 2 is ambiguous, check if only one `people/*/` directory exists — use it.
4. Default to `jehad-altoutou` if all else fails.

**Full target path:**

```
{{PRIME_RADIANT_VAULT}}/sources/meetings/YYYY-MM-DD-<slug>.md
```

**Filename convention.** `YYYY-MM-DD-<slug>.md` — date-first per CLAUDE.md §3 naming rules. The slug describes the meeting type (e.g. `aio-standup`, `aio-mktg-it-meeting`). Multiple meetings on the same day each get their own file with distinct slugs.

**Front-matter schema (meeting-parser compatible — matches `/janus-brain` Phase 3.5 output):**

```yaml
---
type: source
source_type: meeting
title: AIO Standup DD Mon YYYY
slug: YYYY-MM-DD-aio-standup
created: YYYY-MM-DD
captured_by: <person-slug>          # default jehad-altoutou; override via {{CAPTURED_BY_SLUG}}
fireflies_id: <id>
fireflies_url: <Fireflies recording URL>
attendees: [Name1, Name2, ...]      # YAML list of real names from the Digest
duration_min: <int>                 # rounded meeting duration
audience: department
departments: [ai-office]
standup_skill_version: v3.22           # skill version that wrote this file
parser_version: 3                      # /janus-brain applier version (prevents re-processing)
related: [<Monday item ids>, <AIR-N>, <AIP-N>]   # YAML list; cross-refs touched in Phase 3
---
```

**Idempotency.** Path-based. If `YYYY-MM-DD-<slug>.md` already exists at the target path, skip the write and log `obsidian_write: skipped (file already present)` under Final Report Issues. Never overwrite. No git ops are run from the sandbox.

**Non-blocking failure policy.** If the vault root cannot be resolved, the `sources/meetings/` directory cannot be created, permission is denied, or the write or git steps throw for any reason, log under Final Report Issues and attempt the local fallback write to `outputs/standup-AIO-<DD-Mon-YYYY>.md`. The write NEVER blocks the Final Report.

**Migration (from v3.17).** Move existing standup files from `people/jehad-altoutou/meetings/` to `sources/meetings/`:
```bash
git -C ~/janus/prime-radiant mv people/jehad-altoutou/meetings/*-standup.md sources/meetings/
git -C ~/janus/prime-radiant commit -m "migrate: standup files people/jehad-altoutou/meetings → sources/meetings (v3.19)"
git -C ~/janus/prime-radiant push
```

---

## Reference: Deprecated Surface — Monday AI Tools Registry Board

Board `5095577150` is **deprecated as an active execution surface** (since v3.7). Retained for historical reference.

**Do not write to it from this skill.**

---

## Department Group Routing (for new parent tasks on the Automations board)

| Transcript signal | Target group |
|---|---|
| HR forms, hiring, onboarding, training new staff | HR Department (`group_mm2m796p`) |
| Marketing, CRM, brand, content, lead gen | Marketing Department (`group_mm2xfh38`) |
| ISO compliance, audit, policy enforcement | ISO Department (`group_mm2xjkm2`) |
| Finance ops, invoice, expense, finance dashboards | Operations Department (`group_mm2xtzbj`) — no Finance group exists |
| Operations, post-prod support, infra-ops, vendor mgmt | Operations Department (`group_mm2xtzbj`) |
| IT support, IT helpdesk, IAM, SSO, IT handoff, sandbox→production for IT-deployed tools, Monday/Slack/Workspace admin | IT Department (`group_mm33y6xe`) |
| CEO-driven initiatives, Bonaventure-asked tasks, EMS, finance dashboard for CEO | Office of CEO (`group_mm32zmaq`) |
| Cross-cutting AI Office tech, registry / AI / policy / R&D work, anything not above | Planned Automations (`topics`) |

The Labels column captures cross-cutting concerns. <70% routing confidence → ask the user before creating.

**Bulk reorganisation rule (v3.13):** if the user requests a bulk reorganisation of items from `topics` into department groups, every moved item must receive a Step 3E.1 move-rationale Update *and* a Step 3H backfill Description Update if it doesn't already have one. Both posts use Source `Bulk reorganisation DD Mon YYYY` if no meeting drove the move.

---

## Conventions

- British English throughout
- Costs in USD (rare — costs owned by `/ai-registry`)
- Dates: `DD Mon YYYY`
- Issue identifiers: `AIR-N` (managed by `/ai-registry`), `AIP-N` (reconciled by Step 4)
- Standup log entries headed `## AIO DD Mon YYYY` — date-titled, no sequence numbers
- Source column: `<meeting tag> DD Mon YYYY` for the most recent touching meeting (`AIO`, `AI/IT Mtg`, `Bonaventure`, `Andrew Weekly`, `Bulk reorganisation`, etc.)
- Monday item names stable — append context via Updates rather than renaming
- HTML, not markdown, in Monday Update bodies
- **Three-phase execution mandatory** — no writes during Phase 1 or Phase 2
- **Obsidian idempotency check is in Phase 1** — check file existence at `{{PRIME_RADIANT_VAULT}}/sources/meetings/YYYY-MM-DD-<slug>.md`
- **Strict Write Safety** — Status / Owner / Timeline / Group changes require explicit transcript evidence, completion proof, owner confirmation, authorised reconciliation, or user-directed bulk reorganisation. When uncertain, ask
- **Low-confidence (<60%) does not auto-create**
- **Duplicate detection mandatory** before any new item creation — Step 2B (Updates-body match) AND Step 2B.1 (name-similarity scan against live boards)
- **Parent project routing — attach over create** is the default
- **Owner Assignment Rules** — Both = both IDs; external = blank + narrative mention; unclear = blank + Final Report; never invent IDs
- **Action sub-item naming** — Verb + object + context
- **Context Coverage Invariant (v3.13)** — every Monday item the skill *touches* (created, source-bumped, status-changed, group-moved, sub-item-added) is guaranteed to have a `<h2>Description (from meeting notes)</h2>` block in its Updates timeline by the end of Phase 3. Step 3G covers creates; Step 3H backfills existing items; Step 3E.1 posts move-rationale Updates; Step 3I verifies coverage at end of Phase 3 and surfaces failures in the Final Report. The pipeline does not consider Phase 3 complete until coverage is verified.
- **Mandatory Description Update on creates (Step 3G v3.12)** — every new parent / sub-item / subagent-driven follow-up task gets one immediately after creation.
- **Mandatory Backfill Description Update on touches (Step 3H v3.13)** — every touched-but-undocumented existing item gets one. Best-effort context derivation (current meeting → prior Updates → item name + routing). Backfill disclaimer included.
- **Mandatory Group-move rationale Update (Step 3E.1 v3.13)** — every group change posts a "why we moved this" Update. Idempotent on date.
- **Deduplication Gate (v3.22)** — two-layer: (1) Step 2B.1 name-similarity scan in Phase 2 (blocks high-confidence duplicates from the plan; flags medium for user confirmation); (2) Step 3.0 pre-create guard in Phase 3 (re-checks live board state immediately before every creation call). Token-overlap thresholds: ≥3 tokens = HIGH block; 2 tokens = MEDIUM flag; 0–1 = proceed. Dedup scan targets sub-items board (`5095012849`) and main board (`5095012818`). Under-detection is the failure mode — when in doubt, flag.
- **Sub-skill orchestration via subagent dispatch** — Task/Agent only; never the `Skill` tool from within this skill
- **Subagent Dispatch Gate (v3.18)** — every tool mentioned (any category: SaaS, AI, infrastructure, analytics, creative, email, hosting) triggers a Linear AIR check; new tools are registered and Gate 1 evaluation is chained automatically; existing entries with new information are enriched; the only items dropped are zero-context market references and tools the speaker immediately dismissed with no further discussion
- **Subagent Return Validation** — JSON validate (including `evaluation_required` boolean check); one retry; on failure log under Subagent Failures
- **Chained Evaluation Dispatch (v3.10)** — when `/ai-registry` returns `evaluation_required.required == true` (or new-tool default), automatically dispatch `/ai-tool-evaluation` Gate 1
- **Subagent Task Volume Control** — >3 follow-ups per tool consolidate under one parent with sub-items. Both consolidated parent and each sub-item receive Step 3G Description Updates.
- **Execution Control Mode** — large/ambiguous runs (>15 actions counting Step 3H backfills + Step 3E.1 moves toward the threshold) require explicit "Approve execution"
- **Linear AIP Conflict Safety** — never silently reconcile drift; log conflict and require manual review
- **Output Compression** — 5–7 bullet summaries; no transcript quotes; no duplication
- **AI Registry source of truth is Linear AIR**
- **Context Separation Rule** — never copy reference docs from `/ai-registry` or `/ai-tool-evaluation`
- **No-orphan invariant** — every Obsidian next-step bullet has Action, Owner, Time horizon, Due date, Monday item link
- **Forward-looking journal** — Obsidian entries lead with Clean Meeting Summary, then 🎯 / 📅 / 🏔️ next steps
- **Idempotency** — file existence check in Phase 1; per-standup Monday Update stub guarded by date-string check; chained Gate 1 skipped if AIR-N already has same-day Gate 1 comment; Description Update skipped if header already present; group-move rationale skipped if same-date stub already present
- **Step 3I Context Coverage Check** runs before Obsidian write / Final Report — coverage tally appears in both surfaces
- **Final Execution Report is emitted on every run that reaches Phase 3** — including coverage results, backfills, move-rationales, dedup results, failures
- **Obsidian write (Step 5 v3.21)** — forward-looking entry written as `YYYY-MM-DD-<slug>.md` with meeting-parser-compatible front-matter (incl. `parser_version: 3`, `standup_skill_version: v3.22`) to `{{PRIME_RADIANT_VAULT}}/sources/meetings/` (default `~/janus/prime-radiant/sources/meetings/` — CLAUDE.md §3 canonical path), then `git add && commit && push` (Step 5.1, non-blocking). Path-based idempotency (skip if file exists); non-blocking on failure with local fallback to `outputs/`. See `Reference: Prime Radiant Write`.

### Defensive Execution Principle

When in doubt:
- Do not write
- Do not create
- Do not dispatch (or chain)
- **Do not skip a Description Update** — if you can't derive Why / DoD confidently, post a backfill with a placeholder and surface it in Issues / Warnings rather than skip.
- **Do not skip a deduplication check** — if you're unsure whether a candidate is a duplicate, flag it for user confirmation rather than create blindly.

Instead:
- Ask the user
- Surface ambiguity in the Final Report

**Accuracy > automation. Context > silence.**

---

## Execution Checklist

**Phase 1 — Analyse**
- [ ] Fireflies transcript retrieved (raw transcript, not summary)
- [ ] Meeting Intelligence Digest constructed
- [ ] Obsidian idempotency check completed in Phase 1 (file existence check at `{{PRIME_RADIANT_VAULT}}/sources/meetings/YYYY-MM-DD-<slug>.md`)
- [ ] Digest contains all nine fields

**Phase 2 — Plan**
- [ ] Monday Automations board fetched and cached
- [ ] Confidence scoring applied
- [ ] Duplicate detection run (Step 2B — Updates-body match)
- [ ] **Step 2B.1 — Pre-Create Name-Similarity Scan run on every candidate item and sub-item** — boards `5095012849` and `5095012818` searched; high-confidence duplicates removed from plan; medium-confidence flagged for user confirmation
- [ ] Parent Project Routing applied — attach preferred over create
- [ ] Owner Assignment Rules applied — no invented IDs
- [ ] Action sub-item names follow Verb + object + context
- [ ] Subagent Dispatch Gate applied
- [ ] Chained Gate 1 evaluations noted
- [ ] **Predicted Context Coverage counted** — creates / backfills / moves / already-covered, with totals
- [ ] **Deduplication Scan Results block included in plan** — blocked / flagged / cleared counts with item names and ids
- [ ] Execution plan generated with all sections
- [ ] Plan presented to user when ambiguities exist; approval received

**Phase 3 entry**
- [ ] **Execution Control Mode check completed** — counting Step 3H backfills + Step 3E.1 moves toward the 15-action threshold; user gave "Approve execution" if triggered

**Phase 3 — Execute (in priority order)**
- [ ] **Step 3.0 Pre-Create Guard applied immediately before every create call** — live board re-checked; any duplicate not caught in Phase 2 is blocked and logged; no-create does not halt the run
- [ ] **(1) Monday Automations** updates applied (Strict Write Safety enforced)
- [ ] Sub-items added — production stages AND action sub-items
- [ ] Updates posted for decisions, findings, AIP linkage, blockers
- [ ] **(3G) Description Update posted on every newly created parent + sub-item** — idempotency-checked, failures logged
- [ ] **(3H) Backfill Description Update posted on every touched-but-undocumented existing item** — same template, with backfill disclaimer; idempotency-checked
- [ ] **(3E.1) Group-move rationale Update posted on every moved item** — idempotency-checked on date
- [ ] Completed items moved to Done; Deprecated annotated
- [ ] **(2) No-orphan pass** — every next-step has all four fields and a Monday item id; new items receive Step 3G (with Step 3.0 guard applied); existing items receive Step 3H if uncovered
- [ ] Per-standup `Next step from <meeting tag> DD Mon YYYY` Update stub posted (idempotency-checked)
- [ ] **(3) Subagent dispatch** — gated, validated, volume-controlled
- [ ] Subagent returns validated against JSON schema
- [ ] Chained Gate 1 evaluation dispatched per Default-true rule; chained returns validated; no third-level chains
- [ ] Subagent Task Volume Control applied (consolidated parent + sub-items receive Step 3G, with Step 3.0 guard)
- [ ] No Monday AI Tools Registry writes
- [ ] No `Skill`-tool invocation of `/ai-registry` or `/ai-tool-evaluation` from within this skill
- [ ] **(4) Linear AIP** map built and reconciliation pass completed with Conflict Safety
- [ ] Linear AIR was not modified by this skill
- [ ] **(5) Step 3I Context Coverage Check passed** — every touched item verified covered; failures backfilled or surfaced; tally captured for Obsidian entry + Final Report
- [ ] **(6) Obsidian / Prime Radiant entry written** (Step 5) — `{{PRIME_RADIANT_VAULT}}/sources/meetings/YYYY-MM-DD-<slug>.md` with meeting-parser-compatible front-matter (incl. `parser_version: 3`, `standup_skill_version: v3.22`); outcome surfaced in Summary + Issues
- [ ] **(5.1) Git commit + push completed** (or non-blocking warning logged if pull/commit/push failed); file is on disk regardless and Obsidian Git plugin's auto-backup is the safety net
- [ ] **Local fallback honoured** if vault write failed — `outputs/standup-AIO-<DD-Mon-YYYY>.md` written and linked in Final Report
- [ ] Every next-step bullet in the Obsidian entry includes a Monday hyperlink
- [ ] **(7) Final Execution Report** emitted, including Subagent Failures, Subagent Blockers, AIP Conflicts Unresolved, Missing/Unclear Owners, gated-out subagent mentions, chained-evaluation outcomes, **Context Coverage results (covered / backfilled / move-rationales / failures)**, **Deduplication results (Step 2B.1 blocked/flagged + Step 3.0 execution-time blocks)**, **set_item_description_content seed-and-fill results**
- [ ] No speculative writes — only transcript-warranted, plan-approved, subagent-validated, reconciliation-confirmed, chained-Gate-1, dedup-cleared, Description-Update-completed, Coverage-verified changes
- [ ] **Defensive Execution Principle** honoured throughout
