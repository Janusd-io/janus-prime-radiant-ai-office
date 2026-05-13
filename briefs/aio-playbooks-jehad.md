---
type: brief
title: AIO operational playbooks (Jehad's view)
slug: aio-playbooks-jehad
created: 2026-05-04
updated: 2026-05-12
departments: [ai-office]
confidence: medium
status: active
sources: [2026-05-11-aio-standup-with-jehad]
related: [standup, ai-registry, ai-tool-evaluation, linear, monday, notion, jehad-altoutou, aio-skills-sor-architecture-jehad]
audience: [department]
captured_by: jehad-altoutou
---

# AIO operational playbooks (Jehad's view)

Federated from Jehad's personal vault. Step-by-step recipes for the work that runs through the AI Office, written from the skill owner's perspective. Each playbook names the skill, the trigger, and the expected outcome.

## 1. Process today's standup (the daily flow)

**Skill:** [[standup|/standup]]
**Trigger phrase:** *"Process today's standup"* or *"Log the standup from [date]"*
**Expected outcome:** Monday Automations updated, Linear AIP reconciled, Notion entry appended, Final Execution Report emitted, AI Registry / Tool Evaluation work dispatched as subagents.

Steps the skill executes (you don't need to drive these manually — just trigger):

1. **Fireflies search** for the meeting (broad keyword + ±1 day window)
2. **Build Meeting Intelligence Digest** from the raw transcript (Fireflies summary is a weak hint, never canonical)
3. **Notion idempotency check** — if today's entry exists, ask skip / rerun / abort
4. **Parse digest** into typed items (status updates, decisions, action items, sub-items, next steps, tool mentions)
5. **Apply confidence scoring** + **duplicate detection** + **parent-project routing**
6. **Apply Subagent Dispatch Gate** — drop casual tool mentions, keep explicit decisions/actions/comparisons
7. **Generate execution plan** + **Execution Control Mode check** (large runs need explicit "Approve execution")
8. **Execute Phase 3** in strict priority order: Monday → no-orphan → subagent dispatch → Linear AIP → Notion → Final Report

Confirmations during the run:

- Medium-confidence (60–84%) matches between transcript items and Monday tasks
- Borderline subagent dispatches (e.g., a comparison that could go either way)
- Strict Write Safety triggers (status changes without explicit transcript evidence)
- Attach-vs-create decisions on new sub-items

## 2. Add a new AI tool to the registry

**Skill:** [[ai-registry|/ai-registry]]
**Trigger phrase:** *"Add Harvey AI to the backlog"*, *"Add Whisper Flow to the registry"*, etc.
**Expected outcome:** New AIR-N issue in Linear AI Registry team, populated with description per the template schema, labels (department + tier), priority, requestor noted.

1. **Research the tool via Chrome** — homepage, pricing, integrations (especially Google Workspace + Slack), API docs, ToS (training-data clauses), DPA, security/compliance.
2. **Read** the [[ai-registry|/ai-registry]] description template (`/ai-registry/references/template.md`).
3. **Create the Linear issue** in the AI Registry team with the standard schema.
4. **Apply labels** based on requestor's department + tier classification.
5. **Note the requester** at the bottom of the description (e.g., "Requested by: Jehad Altoutou via 1 May standup").

When triggered automatically by [[standup|/standup]], the dispatch package contains the transcript evidence and decision context — the subagent does its own research and creation.

## 3. Run a Gate 1 evaluation on a tool

**Skill:** [[ai-tool-evaluation|/ai-tool-evaluation]]
**Trigger phrase:** *"Do a Stage 1 on AIR-N"*, *"Triage Stitch"*, *"Run Gate 1 on Whisper Flow"*
**Expected outcome:** Gate 1 Assessment comment posted on the Linear AIR issue with PASS / FAIL / BLOCKED decision; status updated to Evaluating (PASS), Rejected (FAIL), or unchanged with flag (BLOCKED).

1. **Fetch the existing AIR issue** to see what's known.
2. **Classify the candidate** — Tool (user-facing) or Infrastructure (platform/library).
3. **Research via Chrome** — homepage, integrations, pricing, API, ToS (search for "train"), DPA, security trust page.
4. **Assess each Gate 1 criterion:**
   - **G1.1** — Google Workspace / Cloud integration or export
   - **G1.2** — Slack integration (app, webhook, or MCP)
   - **G1.3** — Data portability (standard export formats)
   - **G1.4** — Data training exclusion (contractual guarantee)
   - **G1.5** — Documented API
5. **Determine outcome** — all PASS = proceed to Stage 2, any FAIL = rejected, conditional = BLOCKED with flag.
6. **Update the issue description** with full enriched research.
7. **Post the Gate 1 comment** with structured table + decision + recommended actions.
8. **Update issue status** if appropriate.

Stages 2, 3, 4 follow the same pattern but with deeper criteria — see [[ai-tool-evaluation|/ai-tool-evaluation]] for the full framework.

## 4. Invite a candidate via Assessify

**Skill:** `/assessify-hr`
**Trigger phrase:** *"Invite Sarah for the Software Engineer assessment"*, *"Send the IT Support test to candidate@example.com"*
**Expected outcome:** Candidate invitation created on the Assessify platform, email sent automatically, invite ID captured.

1. **Identify the candidate** (name + email) and the **assessment** (job role or specific assessment ID).
2. **Use** `/assessify-hr` to look up the assessment by name or job role and create the invite.
3. **Confirm** the invite link / ID; share with HR.

For bulk invites: `/assessify-hr` supports `bulk_create_candidate_invites` — pass an array of `{candidate, assessment}` pairs.

## 5. Reconcile Linear AIP drift after a standup

**Automatic** — Step 4 of [[standup|/standup]] runs this every standup.

If you're investigating manually:

1. **Pull all AIP issues** from Linear (`team: 2d1b5c04-94fd-4087-8e95-a5a7aa244a16`).
2. **Build the AIP-N → Monday map** from:
   - Source 1 (canonical): every Monday Automations item's Link column (`link_mm2xexj3`)
   - Source 2 (incidental): regex `/AIP-(\d+)/g` over board-level Updates
   - Fallback: name similarity ≥ 85 %
3. **For each AIP issue** — check current Linear state vs the Monday status mapping.
4. **Apply Conflict Safety** — only reconcile when the transcript or completed Monday execution authorises the change. Otherwise log under "AIP Conflicts Unresolved" for manual review.

Status mapping (Monday → Linear AIP):

- Backlog → Backlog
- In Definition → Planned
- In Development / In Testing → In Progress
- In Production → Done
- Postponed → Backlog
- Deprecated → Cancelled

## 6. Clean up the Notion notebook when it's too large

**Trigger:** [[standup|/standup]] Step 5A.1 flags the page above 60 KB, OR you notice slowness/timeouts on Notion writes.

1. **Run the Archival Trigger** (Step 5F of [[standup|/standup]]): identify entries older than 14 days; group by month; create / reuse `Standup Log Archive — <Month YYYY>` child page; move full entry content; replace each entry on the master page with a one-line summary linking to the archive.
2. **Verify** with a fresh fetch.
3. **If still oversized** — escalate to user. Possibly the retention window needs to shrink (default 14 → 7 days).

**Manual one-off cleanup** (what we did on 4 May 2026):

1. Save a durable backup of the current page content to outputs.
2. Use `replace_content` with a clean rebuilt page.
3. Preserve every existing `<page url="...">` reference in the new content.
4. Verify the new page loads cleanly.

## 7. Set up the morning before a standup

Pre-standup hygiene that helps the [[standup|/standup]] skill run cleanly:

- **Verify Fireflies recorded the meeting.** Title should be "AIO DD Mon" pattern. If not, edit the title to match — the skill's search relies on it.
- **Glance at Monday Automations** — make sure the parent items most likely to be discussed have current Source columns and aren't in unexpected statuses.
- **If a tool will be added/evaluated** — pre-populate the discussion topic name in your head so the transcript is unambiguous about which tool you mean.

## 8. Deliberate use of the Subagent Confirmation queue

When [[standup|/standup]] runs and a borderline tool comparison appears (e.g. "Stitch vs Lovable"), the Defensive Execution Principle holds the dispatch in **Subagent Confirmation** — it does not auto-fire even if you said "Approve execution". Replying with an explicit yes/no on the borderline item is what unblocks it.

This is by design. Don't fight it.
