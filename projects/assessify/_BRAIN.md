---
type: project-brain
project: Assessify
last_updated: 2026-05-12
maintainer: Claude (Opus 4.7) + Jehad
purpose: Curated, canonical summary of Assessify. Read THIS first instead of grepping the codebase.
---

# Assessify — Project Brain

> Canonical, hand-curated context for Assessify. The 614 `*().md` files in this folder are auto-graphified noise — ignore them. **Only this file is authoritative.**
>
> Always read this before exploring the codebase. Update it at the end of any non-trivial change.

---

## What is Assessify

A self-hosted HR + recruitment platform for **Janus Digital** (Dubai-based property-AI fund). It runs the candidate intake → pre-screening → interview → scoring → offer pipeline, plus HR onboarding forms.

- **Code:** `/Users/jehad/assessify/`
- **Repo:** [Jehada-Janusd/HR-Assessment-Platform](https://github.com/Jehada-Janusd/HR-Assessment-Platform), `main` branch
- **Production:** `https://assessify.janusd.io` — Hostinger Ubuntu VPS, Caddy + Docker
- **Stack:** Next.js 16.2.4 (App Router, **breaking changes vs. training data — read `node_modules/next/dist/docs/`**), React 19, Prisma 7 (SQLite via libsql adapter), Tailwind v4, shadcn/ui, Resend (email), `@react-pdf/renderer` (server-side PDFs)

---

## Current state — what's shipped and what's next

### Phase 1.A — Foundation ✅
Pipeline data model, agency + direct intake forms, candidate dashboard, role/scoping, MCP recruitment tools.

### Phase 1.B — Pre-interview scoring ✅ (multiple iterations)
- v1: scoring agent + Slack alert + send-invite button
- v2: full HR-equivalent pre-screening report (10+ sections — career arc, weighted scorecard, structural gaps, why-to-hire, risk register, interview Qs, decision framework, compensation, onboarding plan, final assessment)
- v3 (May 2026): extended candidate intake fields (employment, visa, AI tools, license, location, CV received), email template variants per form type, country dropdown, candidate PDF export, MCP rubric CRUD

### Phase 1.C — Post-interview scoring ✅ (May 7–8, 2026, shipped via Codex)
- `post-scoring-agent.ts` (450L) mirrors the pre-scoring agent
- `PostInterviewReport.tsx` + `PostInterviewScoringButton.tsx` UI on the candidate detail page
- `post-score/route.ts` API endpoint + extracted `post-score-service.ts` (shared between manual and webhook paths)
- REIB-specific post-interview rubric seeded via `scripts/seed-ib-post-rubric.ts`
- **Fireflies webhook** at `/api/recruitment/fireflies-callback` auto-imports transcripts → matches to Application by candidate name/role → triggers post-scoring without manual action
- Vitest tests for the post-scoring agent, the post-score service, and the leave calendar

### Phase 1.D — Interview scheduling ✅ (May 12, 2026, MOCK mode pending provisioning)
- Replaced the misleading "Send Interview Invite" button (which actually sent an online assessment) with a real **Schedule Interview** modal on the candidate detail page. HR picks date + time + duration (defaults 60 min, Mon–Fri 09:00–18:00 Asia/Dubai). Submitting books a Google Calendar event with Meet link + Fireflies notetaker, advances the Application to `interview_scheduled`, and Resend-emails both the candidate and the interviewer.
- **Free/busy conflict check** before booking. If the interviewer is busy, the modal shows the next 3 open slots as one-click buttons.
- **Interviewer resolution** via COALESCE: `JobRole.interviewerEmail` (per-role override) → `Department.defaultInterviewer` → null. Both editable in admin UI (`DepartmentInterviewerCard` on the department slug page; new field at the bottom of the JobRoles edit form).
- **MOCK mode** (`GOOGLE_MOCK=1` in prod env, default until provisioned): no real Google calls. "Open in Calendar" link is a Google Calendar **prefill URL** with title, time, attendees, and description pre-filled, so the interviewer can save it to their own calendar with one click. The Resend emails still fire normally.
- **Real Google OAuth**: routes built at `/api/google/oauth/{start,callback}`. Once Workspace mailbox `interview@janusd.com` + GCP OAuth client are provisioned and the refresh token is captured (via `/start`), flip `GOOGLE_MOCK=0` and bookings call the real Calendar API.
- Slack pre-score message keeps "Open candidate" deep-link only; the earlier Slack "Schedule interview" button was removed (consolidated into the platform on user request).

### Phase 1.D — Provisioning ⏳ PENDING (Jehad owns)
- A. Google Workspace mailbox `interview@janusd.com` with 2FA
- B. GCP project + OAuth client (Calendar API enabled; redirect URI = `https://assessify.janusd.io/api/google/oauth/callback`; scopes `calendar.events` + `calendar.freebusy`)
- C. Hit `/api/google/oauth/start` while signed in as `interview@janusd.com` to capture the refresh token (persists to `GoogleToken` row)
- D. Each interviewer shares free/busy with `interview@janusd.com` from Google Calendar settings
- E. Paste `GOOGLE_OAUTH_CLIENT_ID/SECRET/REDIRECT_URI` into prod `.env` and flip `GOOGLE_MOCK=0`

### Phase 1.E — Offer & decision workflow ⏳
Empty. Stages `offer / hired / rejected` defined. Compensation block in pre-screening report is the starting point.

### Phase 2 — Funnel analytics, multi-stakeholder feedback ⏳
`ApplicationStage` history table is ready for time-in-stage analytics. `ApplicationFeedback` is HR-only — needs interviewer-facing flow.

### Cross-cutting (not phased)
- **Leave management** ✅ (May 2026) — Web React leave form (`/leave/new`, signature canvas + balance check), 2-step approval flow runs in Slack (line manager DM → HR DM → employee DM with signed PDF), CEO auto-approval + HR acknowledgement, 8 leave types, balance tracking with HR reset/correction, **team leave calendar with department-colored continuous bars** (`TeamLeaveCalendar.tsx`). Outstanding: Deel.com sync, UAE public holiday auto-fetch (designed, not built).
- **Team onboarding** ✅ (May 7, 2026) — `/admin/team` page lets HR create/edit `Employee` + `LineManager` rows and link each employee to a line manager (drives Slack DM routing for leave approvals). `Employee.lineManagerId` FK added. 9 new MCP `team_*` tools. Sidebar refactored: Leave Requests + Balances + Team collapsed into one "Leave" expandable group.

---

## Key file paths (memorize, don't grep)

### Recruitment pipeline
| What | Path |
|---|---|
| Pipeline list | `src/app/admin/recruitment/page.tsx` |
| Candidate detail | `src/app/admin/recruitment/[id]/page.tsx` |
| Pre-screening report | `src/app/admin/recruitment/[id]/PreScreeningReport.tsx` |
| **Schedule interview** button + modal (formerly "Send Interview Invite") | `src/app/admin/recruitment/[id]/SendInviteButton.tsx` |
| Export PDF button | `src/app/admin/recruitment/[id]/ExportPdfButton.tsx` |
| Post-interview report | `src/app/admin/recruitment/[id]/PostInterviewReport.tsx` |
| Post-interview scoring button | `src/app/admin/recruitment/[id]/PostInterviewScoringButton.tsx` |
| Rubric editor | `src/app/admin/recruitment/rubrics/RubricForm.tsx` |
| Candidate-centric view | `src/app/admin/recruitment/candidates/[id]/page.tsx` |

### Phase 1.D — Interview scheduling
| What | Path |
|---|---|
| Google Calendar client (free/busy, create event, mock prefill URL) | `src/lib/google-calendar.ts` |
| Schedule interview endpoint | `src/app/api/admin/recruitment/applications/[id]/schedule-interview/route.ts` |
| Google OAuth bootstrap (start refresh-token capture flow) | `src/app/api/google/oauth/start/route.ts` |
| Google OAuth callback (persists refresh token to `GoogleToken`) | `src/app/api/google/oauth/callback/route.ts` |
| Department default interviewer card | `src/components/admin/DepartmentInterviewerCard.tsx` |
| Per-JobRole interviewer override field | `src/components/admin/JobRolesManager.tsx` (Interview scheduling block at bottom of edit form) |
| Department PATCH endpoint (for defaultInterviewer) | `src/app/api/admin/departments/[id]/route.ts` |
| Interview confirmation + interviewer notification email templates | `src/lib/email.ts` (`sendInterviewConfirmationEmail`, `sendInterviewerNotificationEmail`) |

### APIs & agents
| What | Path |
|---|---|
| Agency/direct form submission | `src/app/api/forms/[submissionId]/route.ts` |
| Pre-scoring agent | `src/lib/recruitment/pre-scoring-agent.ts` |
| Post-scoring agent | `src/lib/recruitment/post-scoring-agent.ts` |
| Post-score service (shared) | `src/lib/recruitment/post-score-service.ts` |
| Manual post-score API | `src/app/api/admin/recruitment/applications/[id]/post-score/route.ts` |
| Fireflies webhook (auto post-score) | `src/app/api/recruitment/fireflies-callback/route.ts` |
| Profile PDF | `src/app/api/admin/recruitment/applications/[id]/profile.pdf/route.ts` |
| Rubric CRUD (REST) | `src/app/api/admin/recruitment/rubrics/route.ts` + `[id]/route.ts` |
| HR forms invite | `src/app/api/admin/hr-forms/route.ts` |

> **Removed (May 12, 2026):** `src/app/api/admin/recruitment/applications/[id]/send-invite/route.ts` — that endpoint sent an *online assessment* despite its misleading name. The candidate-detail button is now the interview scheduler; assessment invites are sent from `/admin/invites`.

### Leave & team management
| What | Path |
|---|---|
| Admin leave requests page | `src/app/admin/leave-requests/page.tsx` |
| Team leave calendar (department-colored bars, overlap detection) | `src/app/admin/leave-requests/TeamLeaveCalendar.tsx` |
| Leave request form (web React, not Slack) | `src/app/leave/new/page.tsx` |
| **Team page** (Employee + LineManager directory) | `src/app/admin/team/page.tsx` + `TeamManager.tsx` |
| Leave domain lib | `src/lib/leave.ts` |
| Slack interactive handler (leave approvals only — interview scheduling moved to platform) | `src/app/api/slack/interactive/route.ts` |

### Libs & domain
| What | Path |
|---|---|
| Domain constants (stages, sources, score tiers, recommendations, `FullPreScreeningReport`, `PostInterviewReport`) | `src/lib/recruitment.ts` |
| Email templates (per formType variants) | `src/lib/email.ts` |
| PDF document | `src/lib/pdf/CandidateProfilePdf.tsx` |
| Country list (197) | `src/lib/countries.ts` |
| MCP tools | `src/lib/mcp/tools.ts` (~3300 lines, ~100 tools) |
| MCP auth/scoping | `src/lib/mcp/auth.ts`, `src/lib/auth-scope.ts` |
| Prisma client | `src/lib/db.ts` (output: `src/generated/prisma/`) |

### Schema & migrations
| What | Path |
|---|---|
| Prisma schema | `prisma/schema.prisma` |
| Idempotent ALTER TABLEs | `Dockerfile` entrypoint (lines ~470+) — **prod has no Prisma migrations applied; entrypoint is the source of truth** |
| Seed scripts | `scripts/seed-recruitment.ts`, `scripts/seed-ib-rubric.ts`, `scripts/seed-ib-post-rubric.ts` (REIB post-interview), `scripts/seed-recruitment-webhook.ts` |

---

## Data model — quick reference

### `Candidate` (cross-application person)
```
firstName, lastName, email (unique), phoneNumber, nationality, noticePeriod,
office, source ("agency"|"career_page"|"direct"|"referral"), agencyName,
linkedinUrl, cvDriveUrl, cvDriveFolderUrl, cvFileName, cvUploadedAt,
currentlyEmployed ("employed"|"not_working"|"freelancing"),
visaStatus (free text), aiToolsProficiency (free text),
hasDriversLicense (Boolean?), locationStatus ("in_uae"|"outside_uae"),
externalId, archivedAt
```

### `Application` (one row per candidate × role)
```
candidateId, jobRoleId, intakeSubmissionId, office, source, agencyName,
currentStage, status, closeReason, assignedAdminId,
preScore, preScoreTier, postScore, postScoreTier,
appliedAt (auto), cvReceivedAt (set on form submission), closedAt,
externalId
```

Pipeline stages (in order):
`intake_received → cv_review → pre_scored → interview_invited → interview_scheduled → interview_completed → post_scored → offer → hired | rejected | withdrawn`

### `RecruitmentRubric`
```
name, kind ("pre_interview"|"post_interview"), jobRoleId (null = global),
version, isActive, criteria (JSON array of criterion),
thresholdStrong (default 0.85), thresholdMatch (0.7), thresholdConsider (0.55)
```

Criterion shape: `{ key (snake_case, auto-derived from label), label, weight (0..1, sum=1.0), scoringPrompt, commentaryGuidance?, redFlagSignals? }`

### `ApplicationScore`
```
applicationId, rubricId, kind, score (0..1), tier, breakdown (JSON),
sourceRef, computedBy ("claude"|"manual"), computedAt
```

For pre-interview: breakdown is the `FullPreScreeningReport` JSON (defined in `src/lib/recruitment.ts`).

### `Department` (interviewer fields)
```
defaultInterviewer (email, fallback when JobRole.interviewerEmail is null)
```

### `JobRole` (interviewer override + JD fields)
```
interviewerEmail (override; wins over Department.defaultInterviewer),
jdSummary, jdResponsibilities, jdRequirements, jdNiceToHaves, jdYearsExperience
```

### `Interview` (Phase 1.D)
```
applicationId, scheduledAt (UTC), durationMin (default 60), timezone (default "Asia/Dubai"),
interviewerEmail, interviewerName, candidateEmail (snapshots taken at booking time),
meetUrl, calendarEventId, calendarHtmlLink,
status ("scheduled"|"cancelled"|"completed"|"no_show"),
scheduledBySlackUserId (legacy nullable, no longer used), cancellationReason, cancelledAt
```

### `GoogleToken` (Phase 1.D OAuth)
```
email (unique, e.g. "interview@janusd.com"),
refreshToken (long-lived; access tokens minted on demand),
scopes (CSV), lastRefreshAt
```

---

## Production deploy workflow

Production runs as docker compose stack at `/opt/stacks/assessify/` on Hostinger VPS. Code is pushed via **rsync over SSH**, not git pull.

```bash
# 1. Backup (uses sqlite3 .backup, online-safe)
ssh -i ~/.ssh/hostinger_janusd janusd@187.127.98.40 \
  'cd /opt/stacks/assessify && bash backup.sh'

# 2. Rsync changed files (NEVER rsync .env, dev.db, node_modules, .next, src/generated/prisma/*)
rsync -avz --relative -e "ssh -i ~/.ssh/hostinger_janusd" \
  <changed-files> \
  janusd@187.127.98.40:/opt/stacks/assessify/

# 3. Rebuild + restart (entrypoint runs idempotent ALTER TABLEs on boot)
ssh -i ~/.ssh/hostinger_janusd janusd@187.127.98.40 \
  'cd /opt/stacks/assessify && docker compose build app && docker compose up -d app'

# 4. Smoke-test
curl -s -o /dev/null -w "%{http_code}\n" https://assessify.janusd.io/
```

**Hard rules:**

- ALWAYS run `backup.sh` before deploy — takes ~1s.
- NEVER `docker compose down -v` on prod (wipes the volume).
- NEVER rsync `dev.db` from local (clobbers prod data).
- Schema changes go in the Dockerfile entrypoint as idempotent `if ! ... grep -q ...; then ALTER TABLE ...; fi` blocks. There are NO Prisma migrations on prod.
- DB volume: `assessify_assessify_data` → `/app/data/dev.db` inside container.
- Container name on prod: `assessify-app` (different from local `assessify-app-1`).

---

## Conventions & gotchas

- **Vitest tests now exist** in `src/lib/__tests__/` (post-scoring-agent, post-score-service, leave-calendar — added May 2026). Run with `npx vitest`. Most surfaces still rely on type-check + manual deploy + curl smoke.
- **`tsc --noEmit` is the primary correctness gate**. Run it once at the end of a change set, not per-edit. Add a `vitest run` for any change touching tested surfaces.
- **MCP server** lives at `src/app/api/mcp/route.ts`. Tools registered in `src/lib/mcp/tools.ts` `TOOL_DEFINITIONS` array; dispatched via the `switch (name)` block; handlers below.
- **Auth**: admin sessions via cookie (`getSession` from `@/lib/auth`); MCP via Bearer token.
- **Email**: Resend, branded templates in `src/lib/email.ts`. Form-invite email branches by `FormTemplate.formType` (HR onboarding vs. recruitment).
- **PDF rendering pitfalls** (`@react-pdf/renderer`):
  - Don't use `wrap={false}` on tall content — triggers `unsupported number: -1.84e+21` overflow.
  - Don't use `fontStyle: "italic"` with Helvetica — use `fontFamily: "Helvetica-Oblique"`.
  - Don't use `fixed` on nested layouts — only on Page-level absolute footers, and even then prefer in-flow.
  - `borderRadius` ≤ half the element's height, or arc paths overflow.
- **SQLite + Prisma**: never `UPDATE ... = readfile(...)` without `CAST(... AS TEXT)` — `readfile()` produces a BLOB and Prisma rejects it with "Expected a string in column ... got object". Use `CAST(readfile('...') AS TEXT)` or write via Prisma.
- **Form submissions**: dynamic FormTemplate JSON (no static schema). The submission handler at `src/app/api/forms/[submissionId]/route.ts` reads `formatted.<field_name>` and maps to Candidate/Application columns. To add a form field: edit `scripts/seed-recruitment.ts` AND the submission handler AND re-seed prod.
- **Phase 1.D env vars** (production `.env`):
  - `GOOGLE_MOCK=1` while provisioning is pending → mock free/busy + mock event ID + Google Calendar **prefill URL** for "Open in Calendar". Flip to `0` after OAuth tokens are captured.
  - `GOOGLE_OAUTH_CLIENT_ID` / `GOOGLE_OAUTH_CLIENT_SECRET` / `GOOGLE_OAUTH_REDIRECT_URI` for real mode.
  - `INTERVIEW_MAILBOX_EMAIL` (default `interview@janusd.com`), `INTERVIEW_TIMEZONE` (default `Asia/Dubai`), `INTERVIEW_BUSINESS_HOURS_START` / `_END` (default 9 / 18), `INTERVIEW_DEFAULT_DURATION_MIN` (default 60), `FIREFLIES_INVITE_EMAIL` (default `fred@fireflies.ai`).
- **Dubai timezone**: UTC+4 year-round, no DST. The schedule-interview endpoint builds UTC `Date` from `(date, time)` strings as `new Date(Date.UTC(y, mo-1, d, h - 4, mi))`. Don't try to be clever with `Intl.DateTimeFormat` for *parsing* — it's display-only.
- **Resend sender**: prod uses `RESEND_FROM_EMAIL=Assessify <noreply@janusd.io>` (verified domain in Resend). Don't fall back to the default `onboarding@resend.dev` sandbox sender — it can only deliver to the account owner.

---

## Linked context

- Auto-memory (Claude's persistent feedback/project memories): `~/.claude/projects/-Users-jehad-assessify/memory/`
- Detailed deploy notes: see auto-memory `reference_production_deploy.md`
- External services (Resend, GitHub, Slack, n8n, UptimeRobot, MCP): auto-memory `reference_external_services.md`

---

## How to update this brain

When you finish a non-trivial change:

1. Move features between "shipped" and "next" sections.
2. Update file paths if anything moved.
3. Add new gotchas under **Conventions & gotchas** when you discover them.
4. Bump `last_updated` in frontmatter.

Keep this file ≤ ~500 lines. If a topic grows, link to a sibling note instead of inlining.
