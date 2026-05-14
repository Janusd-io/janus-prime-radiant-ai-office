---
type: source
source_type: laptop
title: HANDOFF
slug: handoff
created: 2026-05-12
captured_by: jehad-altoutou
audience: personal
original_path: /Users/jehad/assessify/HANDOFF.md
original_size: 11852
original_ext: .md
category: notes
extracted_with: text-copy
extracted_at: "2026-05-14T09:51:32Z"
sensitivity: dept
sensitivity_confidence: 0.85
sensitivity_reason: "Session-handoff note for engineering — operational, no PII"
---

# HANDOFF

_Extracted from `[[assessify|assessify]]/HANDOFF.md` on 2026-05-14._

# Handoff — Assessify

> Single-file summary for the next Claude session. Read this first. Then read
> `AGENTS.md` (token-efficiency rules + brain pointer) and
> `/Users/jehad/Documents/[[obsidian|Obsidian]] Vault/03 Projects/Assessify/_BRAIN.md`
> (canonical project brain). Ignore the 614 auto-graphified `*().md` files in
> the same Obsidian folder.

---

## TL;DR — where we are (May 12, 2026 — late session)

Pipeline scoring is fully shipped pre- and post-interview. **Phase 1.D —
interview scheduling — also shipped today in MOCK mode** (`GOOGLE_MOCK=1`
on prod). The Slack pre-score DM keeps the "Open candidate" button only;
the actual interview booking happens entirely on the candidate detail
page now ("Schedule Interview" modal). Up next: provisioning Google
Workspace + GCP OAuth so the bot creates real calendar events.

- Repo: `/Users/jehad/assessify/` · branch: `main` · **many uncommitted changes from today's session — see `git status`**
- Prod: `https://assessify.janusd.io` ([[hostinger|Hostinger]] Docker, rsync deploy)
- Last commit: `239d765` (pre-session); rsync deploys since then are on prod but uncommitted locally
- Monday board: 8 existing items moved to Done + 2 new items created (Phase 1.D, Team onboarding)

---

## What just shipped (today's session — May 12, 2026)

**Phase 1.D — Interview scheduling (rsync'd to prod, not yet committed):**

| Area | Files |
|---|---|
| Schema | `prisma/schema.prisma` + idempotent ALTERs in `Dockerfile`. New: `Department.defaultInterviewer`, `JobRole.interviewerEmail`, `Interview` table, `GoogleToken` table. |
| Google Calendar client | `src/lib/google-calendar.ts` — getFreeBusy, findNextOpenSlots, createInterviewEvent, isWithinBusinessHours, resolveInterviewerEmail. `GOOGLE_MOCK=1` returns deterministic free/busy + a real **Google Calendar prefill URL** (title/time/attendees/description) so "Open in Calendar" works without real OAuth. |
| OAuth bootstrap | `src/app/api/google/oauth/{start,callback}/route.ts` — admin hits `/start` while signed into `interview@janusd.com`, callback persists refresh token to `GoogleToken`. |
| Endpoint | `src/app/api/admin/recruitment/applications/[id]/schedule-interview/route.ts` — POST. Validates business hours + 30-min lead time, checks free/busy, books, persists Interview, advances Application.currentStage, audit-logs, sends two Resend emails. |
| Candidate-page UI | `src/app/admin/recruitment/[id]/SendInviteButton.tsx` rewritten — was "Send Interview Invite" (assessment sender, misleading) → now **Schedule Interview** modal (date/time/duration/notes; conflict suggestions as one-click alternative buttons). |
| Admin UI for interviewer fields | `src/components/admin/DepartmentInterviewerCard.tsx` (department slug page) + new field at bottom of `JobRolesManager.tsx` edit form + `src/app/api/admin/departments/[id]/route.ts` PATCH. |
| Email templates | `src/lib/email.ts` — `sendInterviewConfirmationEmail` (to candidate) + `sendInterviewerNotificationEmail` (to interviewer). Both branded. |
| **Deleted** | `src/app/api/admin/recruitment/applications/[id]/send-invite/route.ts` (old assessment-invite-from-candidate-page endpoint — replaced by schedule-interview). |
| Slack cleanup | Removed the earlier "Schedule interview" Block Kit button + handlers from `src/lib/slack.ts` + `/api/slack/interactive/route.ts`. Pre-score DM now shows only "Open candidate" + a context line pointing HR to the platform. |

**Earlier session today (already committed):**

| Commit | Change |
|---|---|
| `239d765` | fix(leave): uniform day cells + separate month header row |
| `89961fb` | feat(leave): continuous department-colored leave bars |
| `0802863` | fix(leave): "Upcoming Leaves" list above day-strip |
| `4b22b96` | fix(leave): calendar window auto-extends to cover furthest upcoming leave |
| `f108eb4` | refactor(sidebar): collapse Leave Requests + Balances + Team into single "Leave" group |
| `8424762` | feat(team): `/admin/team` + Employee↔LineManager FK + 9 MCP `team_*` tools |
| `9e56e70` | fix(leave): HR full name in signature |

Prod `.env` was updated with: `GOOGLE_MOCK=1`, `INTERVIEW_MAILBOX_EMAIL`, `INTERVIEW_TIMEZONE=Asia/Dubai`, `INTERVIEW_BUSINESS_HOURS_START=9`, `_END=18`, `INTERVIEW_DEFAULT_DURATION_MIN=60`, `FIREFLIES_INVITE_EMAIL=fred@[[fireflies|fireflies]].ai`.

---

## Open threads — what's queued in the user's head

### 1. [[google-workspace|Google Workspace]] + GCP provisioning (Jehad owns; unblocks flipping `GOOGLE_MOCK=0`)

The Phase 1.D code is complete and live in mock mode. To go live:

- **A. Workspace mailbox** `interview@janusd.com` (create seat, 2FA, log in once)
- **B. GCP project** `assessify-scheduler` (or reuse). Enable Calendar API. Create OAuth 2.0 web client with redirect URI `https://assessify.janusd.io/api/google/oauth/callback`. Internal consent screen. Scopes: `calendar.events` + `calendar.freebusy`.
- **C. Refresh-token capture**: while signed into `interview@janusd.com` in a browser, hit `https://assessify.janusd.io/api/google/oauth/start`. The callback persists the refresh token into `GoogleToken`.
- **D. Free/busy sharing**: each interviewer shares free/busy with `interview@janusd.com` from their Calendar settings (Share with specific people → "See only free/busy (hide details)").
- **E. Env**: paste `GOOGLE_OAUTH_CLIENT_ID/SECRET/REDIRECT_URI` into prod `.env`, flip `GOOGLE_MOCK=0`, restart.

After this, the "Open in Calendar" link points to the **real** event on `interview@janusd.com`'s calendar (not the prefill URL), and the interviewer gets a real `.ics` invite via Google.

### 2. UAE public holidays — auto-fetch + skip in leave-day calc (DESIGNED, NOT STARTED)

User confirmed Nager.Date doesn't cover UAE. Best fit: **Google's public holiday calendar** `en.ae#holiday@group.v.calendar.google.com` read via Calendar API with an API key (no OAuth, public calendar). Daily cron via existing n8n upserts into a new `PublicHoliday` table. Then `calculateBusinessDays` in `src/lib/leave.ts` skips those dates.

**On the Monday board:** there's a paused item `2884090805 — "HR: Provide complete leave policy (categories, max days, public holidays)"`. The auto-fetch approach makes that item obsolete; can repurpose to engineering or close it.

User said "I hope that makes sense" — no green light yet to build. Confirm before scaffolding.

### 3. Leave form is NOT in `/admin/forms`

This caused confusion last session. The leave form is custom React at `src/app/leave/new/page.tsx`, **not** a `FormTemplate` row. Different architecture — needs custom date math + balance check + signature. Don't try to "find the leave form template"; it doesn't exist.

If the user asks to "edit the leave form fields", changes are made in the React component, not a UI.

### 4. Sidebar refactored

Leave Requests, Leave Balances, and the new Team page now live under a single **Leave** expandable group. Don't add new top-level entries casually — sidebar real estate is precious.

---

## Production deploy — the only safe path

Project is self-hosted on Hostinger VPS Docker, NOT Vercel. The Vercel plugin
is disabled for this project in `.claude/settings.local.json`. Ignore any
Vercel-related suggestions in tool-output.

```bash
# 1. Backup
ssh -i ~/.ssh/hostinger_janusd janusd@187.127.98.40 \
  'cd /opt/stacks/assessify && bash backup.sh'

# 2. Rsync only the files you touched (NEVER .env, dev.db, node_modules, .next, src/generated/prisma/*)
rsync -avz --relative -e "ssh -i ~/.ssh/hostinger_janusd" \
  <files...> \
  janusd@187.127.98.40:/opt/stacks/assessify/

# 3. Rebuild + restart (entrypoint runs idempotent ALTER TABLE on boot)
ssh -i ~/.ssh/hostinger_janusd janusd@187.127.98.40 \
  'cd /opt/stacks/assessify && docker compose build app && docker compose up -d app'

# 4. Smoke
curl -s -o /dev/null -w "%{http_code}\n" https://assessify.janusd.io/
```

**Hard rules:**

- ALWAYS `backup.sh` before deploy.
- NEVER `docker compose down -v` on prod (wipes the volume).
- NEVER rsync `dev.db` from local to prod (clobbers data).
- Schema changes go in the Dockerfile entrypoint as **idempotent** `if ! grep -q ...; then ALTER TABLE ...; fi` blocks. There are NO Prisma migrations on prod.

---

## Gotchas worth remembering

- **`@react-pdf/renderer`**: don't use `wrap={false}` on tall content, don't use `fontStyle: "italic"` with Helvetica (use `fontFamily: "Helvetica-Oblique"`), don't put `fixed` on nested layouts. We've already been bitten by all three.
- **SQLite + Prisma**: `readfile()` returns a BLOB, not TEXT. If you write JSON to a TEXT column via sqlite3, wrap in `CAST(readfile(...) AS TEXT)` or Prisma will throw on the next `findMany`.
- **FormTemplate edits**: rows live in DB. The seed script (`scripts/seed-recruitment.ts`) won't run in the prod container (the standalone build doesn't ship `scripts/` or `tsx`). To update prod FormTemplate JSON: build the JSON locally, scp to prod, then `docker exec ... sqlite3 ... UPDATE ... = CAST(readfile('/tmp/...') AS TEXT)`.
- **Department-colored leave bars** use a hash-based palette in `TeamLeaveCalendar.tsx`. New departments need no code change.
- **Phase 1.D `GOOGLE_MOCK=1`**: in mock mode, `createInterviewEvent` returns a deterministic fake event ID **plus** a real Google Calendar **prefill URL** (title, time, attendees, description all populated). Clicking "Open in Calendar" in the modal or in the interviewer email opens a brand-new event editor with everything filled — interviewer just hits Save in their own calendar. After provisioning, the prefill URL is replaced by the real event's `htmlLink`.
- **Dubai timezone**: UTC+4 year-round, no DST. The schedule-interview endpoint converts (date, time) inputs to UTC via `new Date(Date.UTC(y, mo-1, d, h - 4, mi))`. Don't try to be clever with `Intl.DateTimeFormat` for parsing — it's display-only.
- **Resend sender**: prod uses `RESEND_FROM_EMAIL=Assessify <noreply@janusd.io>` (verified domain). The default `onboarding@resend.dev` is sandbox-only and can ONLY deliver to the account owner.
- **Email-to-fake-domains silently fails**: Resend accepts the API call but the email never lands. Test candidates with `@calibration.demo` etc. won't receive confirmation emails — replace with a real address for end-to-end testing.

---

## Conventions I'm now enforcing (these live in `AGENTS.md`)

1. Read **sections**, not whole files. Use `offset`/`limit` on Read for files >100 lines.
2. `tsc --noEmit` once **per change set**, not per edit.
3. Bundle parallel Bash/Read calls in one message.
4. **2-sentence** end-of-turn summaries. The diff is the source of truth.
5. No preamble before action.
6. Don't re-read files I just edited.
7. Suggest `/clear` when the user switches workstreams.
8. Use Sonnet/Haiku for routine edits; reserve Opus for plans and debugging.

Earlier sessions burned tokens on whole-file reads, per-edit `tsc`, verbose recaps, and the Vercel-plugin injecting ~12K tokens per session for a non-Vercel project. The plugin is now disabled for this repo.

---

## Pointers

- **Curated brain** (read before exploring): `/Users/jehad/Documents/Obsidian Vault/03 Projects/Assessify/_BRAIN.md`
- **Auto-memory** (persistent feedback/project notes): `/Users/jehad/.claude/projects/-Users-jehad-assessify/memory/MEMORY.md`
- **Project instructions** (efficiency rules + breaking-changes warning): `/Users/jehad/assessify/AGENTS.md` (loaded via `CLAUDE.md`)
- **Monday board** (HR Dashboard — Recruitment & Leave Management): https://janusd-company.monday.com/boards/5095636727
- **[[github|GitHub]] repo**: https://github.com/Jehada-Janusd/HR-Assessment-Platform

---

## If the user asks something unrelated to current threads

Suggest `/clear` first. Long sessions in this codebase get expensive fast
because of the conversation length + tool-output accumulation. Fresh
session + this handoff = much cheaper.
