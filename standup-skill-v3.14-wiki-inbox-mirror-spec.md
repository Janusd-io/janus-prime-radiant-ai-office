# Standup Skill v3.14 — Wiki Inbox Mirror (Spec)

**For:** Jehad Altoutou (skill maintainer)
**From:** Michael Bruck
**Date:** 2026-05-08
**Skill version target:** v3.13 → v3.14
**Status:** proposed change; awaiting Jehad's review/integration

---

## Background

The Janus Prime Radiant wiki (currently the AI Office instance, soon shared with HR / Marketing / Finance / IT-Ops as separate domain instances) ingests sources from `inbox/` per its `CLAUDE.md` schema. The standup skill already produces the highest-signal artifact for that ingest — the daily `## AIO DD Mon YYYY` Notion entry — but the wiki only learns about it when a human (today: Michael) manually drops a copy into the wiki inbox.

This proposes a Step 5.1 that mirrors the same content the skill writes to Notion into the wiki inbox folder, so the wiki picks it up automatically on the next ingest session. **Notion remains load-bearing; the wiki drop is best-effort.**

This change is also what unblocks the wiki becoming a shared AI Office tool rather than Michael's personal one — Jehad's standup runs become a first-class wiki-write surface.

---

## Change summary

1. **New Step 5.1 — Mirror to Wiki Inbox.** Inserted between Step 5 (Notion entry) and Step 6 (Final Execution Report).
2. **New skill configuration:** `wiki_inbox_path` (absolute path) and `wiki_dept` (short tag, e.g. `aio`).
3. **Step 6 Final Report:** add a `Wiki inbox drop:` line so failures are visible.
4. **Changelog entry** at top of `SKILL.md` ("What's new in v3.14").

No changes to Phases 1–3 or to the Context Coverage Invariant. Step 5.1 is purely additive and runs after Step 5 (Notion) regardless of Phase 3 outcome.

---

## Step 5.1 — Mirror to Wiki Inbox

**Trigger:** runs after Step 5 (Notion entry) succeeds. If `wiki_inbox_path` is unset, skip silently and note `skipped (no config)` in the Final Report.

**Inputs (already produced by the time Step 5.1 runs):**

- The compressed Notion entry body (the same Markdown the skill writes to Notion in Step 5).
- The Fireflies transcript URL (already known from Step 1).
- The Notion entry URL (returned by Step 5).
- Meeting date (already in skill scope).
- Attendees list (already parsed in Phase 1).
- `wiki_dept` and `wiki_inbox_path` from skill config.

**Output file:**

```
<wiki_inbox_path>/<YYYY-MM-DD>-<wiki_dept>-standup.md
```

Examples: `2026-05-08-aio-standup.md`, `2026-05-08-marketing-standup.md`.

**File contents:**

```markdown
---
notion_url: <full Notion URL of the entry written in Step 5>
notion_section: <meeting tag> DD Mon YYYY
fetched: YYYY-MM-DD
source_type: notion-standup-entry
fireflies_transcript: <Fireflies URL>
attendees: [firstname-lastname, firstname-lastname, ...]
---

# <meeting tag> DD Mon YYYY

**Attendees:** Firstname Lastname, Firstname Lastname
**Source transcript:** [Fireflies — <meeting tag> DD Mon](<fireflies URL>)

## Clean meeting summary

<same compressed bullet body the skill wrote to Notion in Step 5>

## 🎯 Next steps — by next standup (DD Mon)

<same as Notion>

## 📅 This week

<same as Notion>

## 🏔️ Longer horizon

<same as Notion>

## Decisions made

<same as Notion>

## Key findings / discussions

<same as Notion>

## Monday items touched

<same as Notion, including the v3.13 coverage line>

## Linear AIP reconciliation

<same as Notion>

## AI Registry / Tool Evaluation Outcomes

<same as Notion>
```

The body MUST be plain Markdown — no Notion-specific blocks (toggle, callout, database mentions). The skill already produces a plain-Markdown rendering for Notion's content; the same string is reused verbatim.

The `attendees:` list MUST use kebab-case `firstname-lastname` slugs (matching the wiki's `entities/internal/<slug>.md` filenames), not display names. Maintain a small mapping table in skill config or derive deterministically from the Fireflies attendee list.

**Idempotency:**

Piggyback on Step 1.6's existing Notion idempotency check.

- If Step 1.6 found the Notion entry already exists and the user chose `skip`, also skip Step 5.1.
- If the user chose `rerun`, Step 5.1 overwrites the wiki file (atomic rename: write to `<file>.tmp`, then `mv`).
- If the user chose `abort`, Phase 3 doesn't run, so Step 5.1 doesn't run either.
- Independent check: if `<wiki_inbox_path>/<YYYY-MM-DD>-<wiki_dept>-standup.md` already exists at Step 5.1 time but Notion idempotency was clear (rare — implies wiki and Notion drifted), log a warning to the Final Report and skip the wiki write to avoid clobbering. Surface this as `wiki_drift` in the report.

**Failure semantics (best-effort):**

| Condition | Behaviour |
|---|---|
| `wiki_inbox_path` unset | Skip silently. Final Report: `skipped (no config)`. |
| Path does not exist or not writable | Skip with warning. Final Report: `❌ <error message>`. Do NOT abort the standup run. |
| File already exists + Notion idempotency was clear | Skip. Final Report: `⚠️ wiki_drift — file already present`. |
| Write succeeds | Final Report: `✅ <relative path>`. |

The wiki drop never blocks Phase 3 completion or Step 6. Notion is the load-bearing surface; wiki mirroring is incremental.

**Concurrency:** the wiki may be on Google Drive or another sync layer. To minimise sync conflicts, write to a temp file then atomically rename. Do not hold the file open longer than needed. If the user runs the skill twice the same day from different machines (e.g. Michael's laptop + Jehad's laptop), Notion idempotency catches it before Step 5.1 runs.

---

## Step 6 — Final Execution Report (addition)

Add one line to the Summary block:

```
- Wiki inbox drop: ✅ <relative path> | ⏭ skipped (no config) | ⚠️ wiki_drift | ❌ <error>
```

No other changes to Step 6.

---

## Configuration

Two new keys in skill config (wherever `/standup` reads its environment-specific config today):

```yaml
# Required for Step 5.1 to fire. Absolute path to the wiki's inbox/ folder.
# Unset = Step 5.1 is skipped.
wiki_inbox_path: "/Users/<user>/<google-drive-mount>/<shared-folder>/Janus Prime Radiant — AI Office/inbox"

# Filename suffix tag identifying the domain wiki. Default: "aio".
# Per-domain wikis (Marketing, HR, etc.) override this.
wiki_dept: "aio"
```

Per-machine config — Michael and Jehad each set their own path, since their Google Drive mount points differ.

When the Marketing-domain wiki ships, the marketing standup variant of `/standup` (or the same skill with a per-meeting override) sets `wiki_inbox_path` to the Marketing wiki and `wiki_dept: "marketing"`.

---

## Changelog block to add at the top of `SKILL.md`

```markdown
## What's new in v3.14

- **Step 5.1 — Mirror to Wiki Inbox.** After Step 5 writes the Notion journal entry, the same compressed content is mirrored as a Markdown file into the configured wiki inbox folder. The wiki ingests the file on its next session, creating decision pages, updating project hubs, and escalating new entities per its own schema (see the wiki's `CLAUDE.md` §5.1). Notion remains load-bearing; the wiki mirror is best-effort and does not block Phase 3 completion.
- **New configuration:** `wiki_inbox_path` (absolute path; unset = Step 5.1 is skipped) and `wiki_dept` (filename tag, default `"aio"`). Per-machine config — values differ between maintainers because Google Drive mount points differ.
- **Step 6 Final Report** gains a `Wiki inbox drop:` line so wiki-write outcomes surface alongside Notion / Linear / Monday.
- **Idempotency** piggybacks on Step 1.6's Notion check; the user's `skip / rerun / abort` choice cascades to the wiki write.
```

---

## What this enables

- **The wiki becomes a shared AI Office tool.** Jehad's standup runs feed the wiki without a Michael-in-the-loop manual step. Both maintainers' work shows up in the same knowledge surface.
- **Per-domain wiki rollout becomes mechanical.** When the Marketing or HR wiki comes online (each is a separate domain instance per the wiki's `CLAUDE.md` §1 "Domain generalisability"), point `wiki_inbox_path` at it and standup → wiki ingest is automatic.
- **No new Notion coupling.** The skill keeps writing to Notion identically; the wiki gets the same content via a side channel. If the wiki goes away, the standup skill is unaffected.

---

## Out of scope for v3.14

- Triggering the wiki ingest itself. The wiki ingest still requires an LLM session (Cowork or otherwise) to actually move the file from `inbox/` to `sources/notion/` and update wiki pages. The standup skill just deposits the file; the wiki picks it up on next session. A scheduled wiki ingest job is a separate question for later.
- Bidirectional sync. The wiki never writes back to Notion / Linear / Monday from this path. Wiki edits stay in the wiki.
- Cross-vault sync. If we eventually have multiple wiki instances (Marketing + HR + AIO) and want a standup to fan out into more than one, we add a list config (`wiki_inbox_paths: [...]`) — not in this revision.

---

## Open questions for Jehad

1. Where does `/standup` currently read environment config from? (To know where to add `wiki_inbox_path` cleanly.)
2. Is there an existing attendee-name → kebab-slug mapping in the skill, or does Step 5.1 need to introduce one?
3. Anything in the v3.13 testing harness that would be invalidated by adding a write-after-Step-5? (My read: no, but you'd know.)
