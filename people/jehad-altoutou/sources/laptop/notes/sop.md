---
type: source
source_type: laptop
title: SOP
slug: sop
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
original_path: /Users/jehad/assessify/SOP.md
original_size: 40552
original_ext: .md
category: notes
extracted_with: text-copy
extracted_at: "2026-05-14T09:51:32Z"
sensitivity: dept
sensitivity_confidence: 0.85
sensitivity_reason: "Internal operations manual — no PII, operational only"
project: assessify

---

# SOP

_Extracted from `[[assessify|assessify]]/SOP.md` on 2026-05-14._

# Assessify — Standard Operating Procedure (SOP)

**Version:** 1.3
**Last Updated:** 28 April 2026
**Owner:** [[jehad-altoutou|Jehad Altoutou]] — Janusd

> **Recent:** v1.3 (28 Apr 2026) — MCP up to 57 tools (Round 3); admin auth gate on every `/api/admin/*` endpoint; rate limit on `/api/mcp`; Next.js 16.2.4 (HIGH advisory patched); [[github|GitHub]] Actions CI; Dockerfile entrypoint now runs migrations on fresh-install path too.

> **Docs:** [📖 README](README.md) · [📘 SOP (full operations manual)](SOP.md)

---

## Table of Contents

1. [System Overview](#1-system-overview)
2. [Architecture](#2-architecture)
3. [Deployment & Infrastructure](#3-deployment--infrastructure)
4. [Admin Operations](#4-admin-operations)
5. [Assessment Lifecycle](#5-assessment-lifecycle)
6. [Candidate Flow](#6-candidate-flow)
7. [HR Forms Flow](#7-hr-forms-flow)
8. [Question Bank Management](#8-question-bank-management)
9. [Scoring Engine](#9-scoring-engine)
10. [Webhooks & Automation](#10-webhooks--automation)
11. [Email Delivery](#11-email-delivery)
12. [Analytics](#12-analytics)
12a. [Team Member Management](#12a-team-member-management)
12b. [PDF Export](#12b-pdf-export)
12c. [Audit Logging](#12c-audit-logging)
12d. [Claude Connector (MCP)](#12d-claude-connector-mcp)
13. [Easter Egg System](#13-easter-egg-system)
14. [Backup & Recovery](#14-backup--recovery)
15. [Troubleshooting](#15-troubleshooting)
16. [Security Considerations](#16-security-considerations)
17. [Maintenance Runbook](#17-maintenance-runbook)

---

## 1. System Overview

Assessify is a self-hosted hiring assessment platform. It enables HR teams to:

- Create multi-section assessments with weighted scoring
- Invite candidates via unique, time-limited links
- Score responses automatically against competency frameworks
- Generate hiring recommendations (Strong Hire → Reject)
- Collect HR onboarding forms with region-specific validation
- Push results to external systems via webhooks and n8n

**Primary users:**

| Role | Access Point | Purpose |
| --- | --- | --- |
| Admin / HR | `/admin` | Build assessments, send invites, review results |
| Candidate | `/assess/invite/[code]` | Take assessments |
| Employee | `/forms/[code]` | Fill onboarding / bank details forms |

---

## 2. Architecture

### Stack

- **Frontend + Backend:** Next.js 16 (App Router) — single deployable
- **Database:** SQLite via Prisma v7 + `@prisma/adapter-libsql`
- **UI:** Tailwind CSS v4, shadcn/ui (built on `@base-ui/react`), Framer Motion
- **Email:** Resend API
- **Container:** Docker multi-stage build, Alpine Linux, Node 22
- **Automation:** HMAC-signed webhooks, n8n integration

### Data Model (33 tables)

```
Department → JobRole → AssessmentTemplate → AssessmentVersion → Section → Question → AnswerOption
                                                                    ↓
                                                              QuestionCompetency → Competency
                                                                    ↓
CandidateInvite → CandidateSession → CandidateResponse
                                   → CandidateResult
                                   → CandidateSectionScore
                                   → CandidateCompetencyScore

AdminUser → PasswordOtp → AuditLog
WebhookEndpoint → WebhookDelivery
FormTemplate → FormInvite → FormSubmission → FormFile
AnalyticsEvent
EasterEggClaim

Employee → LeaveRequest ← LineManager
        → LeaveBalance

AdminUser → McpToken ← OAuthClient ← OAuthAuthorizationCode
```

### File Layout

```
src/app/api/        67 API routes (admin, sessions, forms, easter eggs, MCP, OAuth, leave, health)
src/app/admin/      21 admin pages
src/app/assess/     Candidate assessment UI
src/app/forms/      HR form UI
src/lib/            Core logic (auth, scoring, analytics, email, webhooks)
src/components/     28 shadcn + 10 custom components
prisma/             Schema (33 models) + seed script
```

---

## 3. Deployment & Infrastructure

### Initial Deployment

```bash
git clone https://github.com/Jehada-Janusd/HR-Assessment-Platform.git
cd HR-Assessment-Platform
cp .env.example .env
# Edit .env: set RESEND_API_KEY, JWT_SECRET, APP_URL
docker compose build
docker compose up -d
```

### Environment Variables

| Variable | Required | Description |
| --- | --- | --- |
| `DATABASE_URL` | Yes | `file:/app/data/dev.db` (Docker default) |
| `RESEND_API_KEY` | Yes | Resend API key for email |
| `JWT_SECRET` | Yes | HMAC secret for session tokens |
| `APP_URL` | Yes | Public base URL (e.g. `https://assess.janusd.io`) |

### Docker Volume

Data persists in a named volume `assessify_data` → `/app/data/dev.db`.

**Critical rule:** NEVER run `docker compose down -v` unless a schema migration requires it. This deletes all data — assessments, candidates, results, everything.

### Entrypoint Script Behavior

On every container start:

1. If `/app/data/dev.db` does not exist → copy from `seed.db` (first run)
2. Apply additive column migrations idempotently via `sqlite3` ALTER TABLE
3. Start Next.js server

### Rebuilding After Code Changes

```bash
docker compose build app
docker compose up -d app
# Data is preserved — only the app code is replaced
```

### Production Deploy ([[hostinger|Hostinger]] VPS)

Production runs at `https://assessify.janusd.io` on a Hostinger Ubuntu VPS behind Caddy. The stack lives at `/opt/stacks/assessify/` and is **not** a git clone — files are synced manually via `rsync` over SSH.

**Deploy steps (from local repo):**

```bash
# 1. Snapshot the prod DB
ssh janusd@<host> 'cd /opt/stacks/assessify && bash backup.sh'

# 2. Sync changed files (example: a single page)
rsync -avz -e "ssh -i ~/.ssh/hostinger_janusd" \
  src/app/admin/settings/McpTokensCard.tsx \
  janusd@<host>:/opt/stacks/assessify/src/app/admin/settings/

# 3. Rebuild and restart the container
ssh janusd@<host> '
  cd /opt/stacks/assessify
  docker compose build app
  docker compose up -d app
'

# 4. Smoke-test
curl -s -o /dev/null -w "%{http_code}\n" https://assessify.janusd.io/
```

**Rules:**

- Always run `backup.sh` before a deploy — backups land in `/opt/stacks/assessify/backups/` (30-day rotation).
- Never rsync the DB, `.env`, `node_modules`, `.next`, or `src/generated/prisma/*` — the Dockerfile build regenerates the Prisma client inside the image.
- Schema changes: add a matching idempotent `ALTER TABLE` block to the Dockerfile entrypoint (see `McpToken` / `OAuthAuthorizationCode` as patterns). The entrypoint runs on every container start and is the only source of truth for prod migrations.
- Volume `assessify_data` survives `docker compose up -d`. Never run `docker compose down -v` on prod.

---

## 4. Admin Operations

### First Login

- URL: `http://localhost:3000/admin`
- Default credentials are set during seed (update via Settings page)
- Current admin: `jehada@janusd.com`

### Admin Pages

| Page | Path | Purpose |
| --- | --- | --- |
| Dashboard | `/admin` | Department overview, stats, recent activity |
| Assessments | `/admin/assessments` | List, create, edit, duplicate, delete |
| Assessment Editor | `/admin/assessments/[id]/edit` | Sections, questions, settings, preview, calculator |
| Invites | `/admin/invites` | Send candidate invites, view status |
| Sessions | `/admin/sessions` | Monitor active/completed sessions |
| Session Detail | `/admin/sessions/[id]` | Individual candidate scoring breakdown |
| Question Bank | `/admin/question-bank` | Cross-department question library |
| HR Forms | `/admin/hr-forms` | View form submissions and invite status |
| Analytics | `/admin/analytics` | Assessment funnel, competency heatmaps |
| Departments | `/admin/departments/[slug]` | Department details, job role management |
| Settings | `/admin/settings` | Webhook endpoints, admin profile |
| API Docs | `/admin/api-docs` | Full API reference with cURL examples |
| Easter Eggs | `/admin/easter-eggs` | Leaderboard and claim tracking |

### Password Management

- **Change password:** Click profile icon → Change Password
- **Forgot password:** Login page → "Forgot your password?" → OTP sent via Resend → Enter OTP → Set new password

---

## 5. Assessment Lifecycle

### Step 1: Create Assessment

1. Go to `/admin/assessments` → **+ New Assessment**
2. Fill in: Title, Description, Job Role (grouped by department), Passing Score, Time Limit
3. Click **Create Assessment** → redirected to editor

### Step 2: Add Sections

1. In the editor, go to **Sections & Questions** tab
2. Click **+ Add Section** → Title, Description, Intro Text, Icon, Weight
3. Section weights should sum to 1.0 (warning shown if not)

### Step 3: Add Questions

For each section, two methods:

**Method A — Manual:**
Click **+ Add Question** → fill in title, prompt, type, difficulty, max points, scoring strategy, answer options (key/label/points/isCorrect), competency mapping.

**Method B — From Question Bank:**
Click **Add from Bank** → filters pre-set to current department + section type → search, select, import.

### Step 4: Configure Scoring

In the **Settings** tab:

- **Passing Score:** percentage threshold (e.g. 60%)
- **Time Limit:** minutes (optional)
- **Recommendation Thresholds:** Strong Hire / Hire / Consider / Weak Fit cutoffs (each a percentage, must be descending)

### Step 5: Test with Calculator

Go to **Score Calculator** tab:

- Quick-fill: Best Case / Worst Case / Random
- Manually set answers per question
- See total score, per-section breakdown, per-competency scores, recommendation band
- Verify scoring makes sense before publishing

### Step 6: Publish

Click **Publish** in the header. Validation runs:

- Must have at least 1 section
- Must have at least 1 question
- If validation fails, error message shown

Published assessments are directly editable — no versioning workflow needed. Changes take effect immediately for new invites.

### Step 7: Send Invites

Go to `/admin/invites` → **+ Send Invite** → select assessment, enter candidate name + email → sends email with unique link.

### Step 8: Monitor

- `/admin/sessions` — track who started, completed, or is in progress
- `/admin/sessions/[id]` — full scoring breakdown per candidate
- `/admin/analytics` — aggregate funnel, competency heatmaps

---

## 6. Candidate Flow

1. Candidate receives email with invite link (`/assess/invite/[code]`)
2. Validates code → shows assessment title, description, time limit
3. Clicks **Start** → creates session, redirects to `/assess/[sessionId]`
4. Presented section-by-section:
   - Section intro screen (title, description, question count)
   - Questions one at a time (SingleSelect, MultiSelect, Ranking, Scenario, Situational)
   - Timer counts down if time limit set
5. On last question → **Complete** → session locked
6. Redirected to `/assess/[sessionId]/result` — immediate feedback
7. Scoring engine runs: question scores → section scores → competency scores → recommendation

---

## 7. HR Forms Flow

### Form Templates

Two built-in templates are seeded. Admins can create unlimited custom templates.

| Template | Type | Fields |
| --- | --- | --- |
| Personal Data Onboarding | `personal_data` (built-in) | Full name, nationality, ID/passport, emergency contact, etc. |
| Bank Details | `bank_details` (built-in) | Bank name, account number, IBAN, SWIFT code (mandatory) |
| *(Custom)* | `custom` | Admin-defined via template builder |

### Creating Custom Form Templates

1. Go to HR Forms → **Templates** button (top-right)
2. Click **+ New Template**
3. Enter template name and description
4. Add fields: Text, Email, Phone, Date, Text Area, Dropdown, File Upload, Section Heading
5. Configure each field: label, placeholder, required toggle, dropdown options
6. Reorder fields with up/down arrows
7. Click **Create Template** → template appears in the form type dropdown when sending invites
8. Use the **eye icon** to preview the form as the employee will see it

### Sending Form Invites

1. Admin goes to `/admin/hr-forms` → **Send Form**
2. Creates invite → selects form template (built-in or custom), enters employee name + email, selects region
3. Email sent with link to `/forms/[code]`

### Employee Filling Form

1. Opens link → validates code → shows form
2. Fills fields, attaches files (region-aware validation):
   - **UAE:** JPEG only (no PNG), max 1MB
   - **Global:** JPEG + PNG, max 1MB
3. Submits → data saved to `FormSubmission`, files to `FormFile`
4. Webhook fires with full submission data + file attachments as base64

### n8n Integration

The webhook payload includes:

```json
{
  "event": "form.submitted",
  "submission": {
    "id": "...",
    "formType": "personal_data",
    "data": { "field": "value" },
    "files": [
      {
        "filename": "passport.jpg",
        "mimeType": "image/jpeg",
        "content": "<base64>"
      }
    ]
  }
}
```

n8n receives this, parses the JSON, and can:

- Extract base64 files as binary
- Build formatted tables/PDFs
- Route to [[google-drive|Google Drive]], SharePoint, etc.
- Send notifications

---

## 8. Question Bank Management

### Concept

The Question Bank is a cross-department library. Every question in every assessment is visible in the bank, grouped by:

- **Department** (tabs: All, IT, Operations, HR, Finance)
- **Section** (sub-tabs: All Sections, Cultural Fit, AI Awareness, Department-Specific, General)

### Adding to the Bank

Two methods:

1. **Directly:** Question Bank page → **+ Add Question** → select department, bank section, fill details
2. **Automatically:** Any question created in an assessment appears in the bank

### Importing from Bank

When editing an assessment section:

1. Click **Add from Bank**
2. Modal filters default to current assessment's department + section type
3. Search, adjust filters, select questions
4. Click **Add N Questions** → copies question data into the section

### Bank Section Logic

Questions are categorized by their source section slug:

| Section slug contains | Bank category |
| --- | --- |
| `cultur` | Cultural Fit |
| `ai-aware` / `ai readiness` | AI Awareness |
| `library` / `library-*` | General |
| Anything else | Department-Specific |

### Standalone Questions

When adding directly to the bank, a hidden Library template (`library-{deptSlug}`, `isActive=false`) stores the question. These templates never appear in candidate assessment lists.

---

## 9. Scoring Engine

### Question-Level Scoring

| Strategy | Behavior |
| --- | --- |
| `weighted_options` | Each option has points; candidate gets the points of their selection(s) |
| `exact` | All-or-nothing: correct answer = max points, else 0 |
| `partial` | Partial credit for partially correct multi-select |
| `scenario_based` | Points mapped per option for complex scenarios |

**Ranking questions:** Scored by comparing candidate's order to `correctAnswerKey` order. Each position match gets proportional points.

### Aggregation Pipeline

```
Question scores
  → Section scores (weighted by question weight within section)
    → Overall score (weighted by section weight)
      → Competency scores (aggregated across all questions mapped to that competency)
        → Recommendation (compared to per-template thresholds)
```

### Recommendation Bands

| Band | Default threshold |
| --- | --- |
| Strong Hire | >= 85% |
| Hire | >= 70% |
| Consider | >= 55% |
| Weak Fit | >= 40% |
| Reject | < 40% |

Thresholds are configurable per assessment in Settings tab.

### Additional Outputs

- **Confidence score:** How certain the scoring is (based on answer consistency)
- **Risk indicators:** Flags like "rushed answers", "low competency X"
- **Hiring summary:** Text-based summary for hiring managers
- **Automation labels:** Machine-readable tags for webhook consumers

---

## 10. Webhooks & Automation

### Configuration

Admin → Settings → Webhooks:

- Add endpoint URL
- System generates HMAC secret
- Select events to subscribe to

### Security

Every webhook delivery includes:

- `X-Webhook-Signature` header: HMAC-SHA256 of the payload body using the endpoint secret
- `X-Webhook-Timestamp` header: ISO timestamp

Verify on the receiving end:

```
expected = HMAC-SHA256(secret, timestamp + "." + body)
if expected !== signature → reject
```

### Events

| Event | Trigger |
| --- | --- |
| `session.completed` | Candidate finishes assessment |
| `form.submitted` | Employee submits HR form |
| `invite.created` | New candidate invite sent |

### Retry Logic

Failed deliveries (non-2xx response) are logged in `WebhookDelivery` with status and response body for debugging.

---

## 11. Email Delivery

### Provider

Resend API. Current constraint: free tier only delivers to the account owner's email (`jehada@janusd.io`).

### Templates

Two HTML email templates:

1. **Assessment Invite:** Subject: "You're invited to take an assessment" — includes assessment title, link, time limit
2. **Onboarding Form Invite:** Subject: "Please complete your onboarding form" — includes form type, link

### URL Detection

The email helper detects `localhost` / `127.0.0.1` and uses `http://` instead of `https://` to avoid SSL errors in development.

### Upgrading

To send to any email:

1. Verify a custom domain in Resend dashboard
2. Update `RESEND_API_KEY` with a production key
3. Update the `from` address in `src/lib/email.ts`

---

## 12. Analytics

### Overview Dashboard

Accessible at `/admin/analytics`. Two-level view:

**Level 1 — Platform Overview (default):**

- 6 global KPI cards: Total Invites, Sessions, Completed, Completion Rate, Avg Score, Pass Rate
- Overall Recommendation Distribution (Strong Hire → Reject) with color-coded bars
- Assessment list with department, job role, candidate count, question count
- Pending invites notification
- Click any assessment to drill down

**Level 2 — Assessment Drill-Down:**

| Report | What it shows |
| --- | --- |
| Funnel | 5 cards: Total Sessions, Started, Completed, Completion Rate, Drop-off Rate |
| Result Distribution | Horizontal bars per recommendation band with candidate counts |
| Competency Heatmap | Average scores per competency with color-coded progress bars |
| Question Performance | Table: avg score, avg time, fail rate, attempts per question |

Back button returns to the overview.

### Event Tracking

The `AnalyticsEvent` table logs:

- `assessment_started`, `assessment_completed`
- `section_entered`, `section_completed`
- `question_viewed`, `question_answered`
- Custom events via `trackEvent()` in `src/lib/analytics.ts`

---

## 12a. Team Member Management

### Inviting New Members

1. Go to Settings → Team Members → **+ Invite Member**
2. Enter work email, select role (Admin / User)
3. Click Send Invite → email sent with setup link
4. Invitee clicks link → `/admin/setup?token=xxx` → sets name + password → auto-logged in

### Role-Based Access

| Action | Admin | User |
| --- | --- | --- |
| View team members list | Yes | Yes |
| Invite new members | Yes | No |
| Deactivate / reactivate | Yes | No |
| Reset another's password | Yes | No |
| Change another's role | Yes | No |
| Delete users | Yes | No |

### Offboarding (Revoking Access)

1. Settings → Team Members → find the user
2. Click the deactivate icon (user-x) → user's status changes to "Deactivated"
3. Deactivated users cannot log in — the login endpoint checks `isActive: true`
4. Optionally: reset their password first (key icon) for security, then deactivate

### Role Badge

Each user sees their role badge (Admin / User) in the sidebar bottom-left, next to their name.

---

## 12b. PDF Export

### Exporting a Candidate Report

1. Go to `/admin/sessions` → click a completed session
2. Click **Export PDF** (top-right button)
3. A print-ready HTML report opens in a new tab
4. Click **Download PDF** on the report → browser print dialog → Save as PDF

### Report Contents

- Candidate name, email, assessment title, department, job role
- Summary cards: overall score, recommendation, confidence, status
- Hiring summary text and flags
- Section scores with progress bars
- Competency scores (color-coded)
- Full question responses table (section, question, answer, score, time)
- Footer: "Confidential — generated by [admin name]"

---

## 12c. Audit Logging

### What Gets Logged

Every admin action is recorded in the `AuditLog` table:

| Action | Trigger |
| --- | --- |
| `auth.login` | Admin logs in |
| `user.invited` | New team member invited |
| `user.deactivated` | User access revoked |
| `user.reactivated` | User access restored |
| `user.role_changed` | Role changed (Admin ↔ User) |
| `user.password_reset` | Admin resets another user's password |
| `user.deleted` | User permanently deleted |
| `mcp_token.created` | Manual MCP bearer token generated in Settings |
| `mcp_token.revoked` | (Legacy) MCP token soft-revoked — no longer emitted |
| `mcp_token.deleted` | MCP token revoked and permanently deleted |
| `mcp_oauth.authorized` | Admin approved a Claude OAuth consent request |
| `mcp_oauth.denied` | Admin denied a Claude OAuth consent request |

### Fields Captured

- `userId` / `userEmail` — who performed the action
- `targetType` / `targetId` — what was affected
- `details` — JSON context (e.g. new role, email of invited user)
- `ipAddress` — client IP from request headers
- `createdAt` — timestamp

### Querying Audit Logs

```bash
docker compose exec app sqlite3 /app/data/dev.db \
  "SELECT createdAt, userEmail, action, targetId, details FROM AuditLog ORDER BY createdAt DESC LIMIT 20;"
```

---

## 12d. Claude Connector (MCP)

Assessify exposes a Model Context Protocol server so admins can drive the platform from Claude Desktop / Mobile / Web.

### Endpoints

| Path | Purpose |
| --- | --- |
| `POST /api/mcp` | JSON-RPC MCP endpoint (requires `Authorization: Bearer <token>`) |
| `POST /api/oauth/register` | RFC 7591 Dynamic Client Registration |
| `GET  /api/oauth/authorize` | OAuth consent screen (admin must be signed in) |
| `POST /api/oauth/authorize/consent` | Approve/deny — mints auth code |
| `POST /api/oauth/token` | Exchange code for access + refresh token (PKCE S256) |

Access tokens live 1 hour; refresh tokens 60 days (rotated on use).

### Token Types

1. **OAuth-minted** — created automatically when an admin signs in to Claude and approves the consent screen. Auto-named as `${clientName} · ${admin-email}`.
2. **Manual bearer** — generated from `/admin/settings` → "New Token". 90-day expiry by default. Admin-only. Shown once; SHA-256 hashed at rest.

Both flows persist to the `McpToken` table. The hash is stored; the raw token is never logged.

### Origin Tracking

Every token row captures, at consent/creation:

- `createdIp` — client IP from the `X-Forwarded-For` chain
- `createdUserAgent` — raw UA string (UI renders it as `macOS` / `Windows` / `iOS` / etc.)

This is how you verify no outsider obtained a token on your admin account. Check the "Approved from …" line under each token card against your known devices.

### Revoke & Delete

Clicking the trash icon in `/admin/settings` performs a **hard delete** — the row is removed from `McpToken` and the token is invalidated immediately. The audit log row (`mcp_token.deleted`) keeps the name, prefix, and clientId for compliance.

Legacy soft-revoked rows (`revokedAt` set) from before April 2026 can also be removed via the same trash icon — the confirm copy adapts to say "Delete revoked token?" for those.

### Available Tools (MCP)

**57 tools** total as of Round 3 (Apr 2026). Grouped by category:

| Category | Count | Examples |
| --- | --- | --- |
| Read / search | 9 | `list_departments`, `search_assessments`, `get_assessment`, `get_session`, `get_session_results` |
| Authoring | 11 | `create_assessment`, `create_job_role`, `create_question`, `add_section`, `add_question`, `attach_question_to_section`, `create_competency`, `create_department`, `create_candidate_invite` |
| Editing | 8 | `update_assessment`, `update_question`, `update_section`, `update_competency`, `update_department`, `update_job_role`, `reorder_*`, `set_section_weights`, `update_thresholds` |
| Versioning | 5 | `create_new_version`, `publish_version`, `list_assessment_versions`, `get_assessment_version`, `revert_to_version` |
| Sessions / analytics | 5 | `list_sessions`, `get_assessment_analytics`, `get_question_analytics`, `export_sessions`, `toggle_assessment_active` |
| Invite management | 7 | `get_invite`, `list_invites`, `revoke_invite`, `resend_invite`, `extend_invite_expiry`, `update_candidate`, `bulk_create_candidate_invites` |
| Duplicate / clone | 2 | `duplicate_assessment`, `duplicate_question` |
| Admin archive | 3 | `archive_competency`, `archive_department`, `archive_job_role` |
| Automation | 4 | `lookup_by_external_id`, `bulk_tag_questions`, `bulk_delete_questions`, `bulk_toggle_assessment_active` |
| Destructive | 3 | `delete_question`, `detach_question_from_section`, `remove_section` |

Idempotency: every `create_*` tool accepts an optional `externalId`. A second call with the same `externalId` returns the existing record (`idempotent: true`) instead of creating a duplicate. `lookup_by_external_id` exposes the same map for reads.

Refusal contracts (a sample):
- `revoke_invite` refuses on `started` or `completed` invites.
- `update_candidate` refuses if any session for that candidate is `completed` / `expired` / `disqualified` (audit integrity).
- `bulk_delete_questions` refuses the **whole batch** if any target has candidate responses.
- `archive_*` refuses if a child still depends on the parent (active questions on a competency, active roles in a department, active assessments tied to a role).

Tool implementations: [src/lib/mcp/tools.ts](src/lib/mcp/tools.ts). Per-domain operations live in [src/lib/operations/](src/lib/operations/) and are reused by both MCP handlers and portal API routes.

### Setup in Claude

1. Admin opens `/admin/settings` → copy the MCP Connector URL (`https://assessify.janusd.io/api/mcp`).
2. In Claude → Settings → Connectors → Add Custom → paste URL.
3. Claude begins Dynamic Client Registration, redirects to Assessify, admin approves consent.
4. Token appears in Settings as `Claude · <admin-email>` with IP + device.

### Troubleshooting

| Symptom | Cause / Fix |
| --- | --- |
| 401 on `/api/mcp` | Token expired (1h) — Claude should auto-refresh. If refresh also 401s, reconnect from Claude. |
| Consent page 500 | Admin not signed in to Assessify. Open `/admin` first. |
| Token missing IP/device | Row predates the April 2026 origin-tracking migration. Revoke + reconnect to repopulate. |

---

## 13. Easter Egg System

Hidden gamification layer for IT department assessments.

- **4 eggs** defined in `src/lib/easter-eggs.ts`
- Each has a challenge, hint (ROT13 encoded), and validation
- Accessible during assessment at `/assess/[sessionId]/eggs`
- Claims tracked in `EasterEggClaim` with email, session, IP, timestamp
- Admin leaderboard at `/admin/easter-eggs`

---

## 14. Backup & Recovery

### Automated Backup (Recommended)

```bash
# Run manually
./scripts/backup.sh

# Or set up daily cron (2 AM)
crontab -e
# Add: 0 2 * * * /path/to/assessify/scripts/backup.sh
```

The script copies the SQLite database from the Docker container, saves it as `backups/assessify_YYYYMMDD_HHMMSS.db`, and rotates to keep the last 30 backups.

### Manual Backup

```bash
docker compose cp app:/app/data/dev.db ./backup-$(date +%Y%m%d).db
```

### Restore from Backup

```bash
# Stop the app
docker compose stop app

# Replace the database
docker compose cp ./backup-YYYYMMDD.db app:/app/data/dev.db

# Restart
docker compose start app
```

### Full Export

For migration to another system, use the API endpoints at `/admin/api-docs` to export:

- Assessments: `GET /api/admin/assessments`
- Questions: `GET /api/admin/question-bank`
- Sessions: `GET /api/admin/sessions`
- Competencies: `GET /api/admin/competencies`

---

## 15. Troubleshooting

### Container won't start

```bash
docker compose logs app --tail 50
```

Common causes:

- Missing `.env` file → copy `.env.example`
- Port 3000 already in use → change port in `docker-compose.yml`
- Corrupted database → restore from backup

### Emails not sending

- Check `RESEND_API_KEY` is set in `.env`
- Free tier: can only send to the account owner email
- Check Resend dashboard for delivery logs

### Invite link gives SSL error

- On localhost, links should use `http://` — if not, check `APP_URL` in `.env`

### Assessment won't publish

- Must have at least 1 section with at least 1 question
- Check for error message in the red banner

### Webhook not firing

- Check Settings → Webhooks — endpoint must be active
- Check `WebhookDelivery` table for failed attempts
- Verify the receiving server returns 2xx

### Score Calculator shows 0 for ranking questions

- Ensure `correctAnswerKey` is set on ranking questions (JSON string of the correct order, e.g. `["a","c","b","d"]`)

---

## 16. Security Considerations

### Authentication

- Admin sessions use HMAC-signed tokens (`SESSION_SECRET` in `.env`) stored in httpOnly cookies
- Token format: `base64url(payload).hmac_sha256_signature` — cannot be forged without the secret
- Passwords hashed with bcryptjs (12 rounds)
- OTP for password reset (6-digit, 10-minute expiry)

### Rate Limiting

In-memory sliding-window rate limiter (no external dependencies):

| Endpoint | Limit | Window |
| --- | --- | --- |
| Login (`POST /api/admin/auth`) | 5 requests | 60 seconds |
| Forgot Password (`POST /api/admin/forgot-password`) | 3 requests | 60 seconds |
| Account Setup (`POST /api/admin/setup`) | 5 requests | 60 seconds |
| Reset Password (`POST /api/admin/reset-password`) | 5 requests | 60 seconds |
| Verify OTP (`POST /api/admin/verify-otp`) | 5 requests | 60 seconds |
| MCP (`POST /api/mcp`) | 60 requests | 60 seconds |

Returns 429 with `Retry-After` header when exceeded. The MCP limit is per-IP defense-in-depth on top of bearer-token auth — protects against a leaked or misbehaving token hammering the server until manual revocation.

### Role-Based Access Control

- Admin role: full access to all management endpoints
- User role: read access to dashboards, no user management
- Backend enforces `session.role === "admin"` on all write operations

### Audit Trail

All admin actions logged to `AuditLog` table with userId, action, target, details, IP, and timestamp. See [Section 12c](#12c-audit-logging).

### Data Access

- All admin APIs require authentication
- Candidate APIs validate invite codes (single-use, optionally time-limited)
- Assessment time limits enforced server-side (auto-expire sessions)
- Form APIs validate invite codes

### Webhooks

- HMAC-SHA256 signatures on every delivery
- Secrets generated server-side, never exposed in logs

### File Uploads

- Max 1MB per file
- MIME type validation (region-aware)
- Files stored as base64 in webhook payload, not on public file system

### Remaining for Production

- [ ] Enable CSP / security headers (X-Frame-Options, X-Content-Type-Options) — currently relying on Caddy defaults
- [ ] Set up custom Resend domain + no-reply email
- [ ] Configure firewall rules for webhook endpoints
- [x] ~~Enable HTTPS~~ (done — Caddy on the Hostinger VPS, auto-renewing Let's Encrypt)
- [x] ~~Auth gate on every `/api/admin/*` endpoint~~ (done Apr 2026 — `getSession()` required)
- [x] ~~Rate limit on `/api/mcp` and password-reset endpoints~~ (done Apr 2026)
- [x] ~~Set strong SESSION_SECRET~~ (done — 48-char random in `.env`)
- [x] ~~Rate limiting on login/invite~~ (done — in-memory sliding window)
- [x] ~~Automated backups~~ (done — `backup.sh`, nightly cron @ 03:00 UTC, 30-day rotation)
- [x] ~~Audit logging~~ (done — AuditLog table, also covers MCP tool calls)
- [x] ~~CI~~ (done — GitHub Actions runs typecheck + lint + tests on every push and PR)
- [x] ~~Healthcheck~~ (done — `/api/health` probed every 30s; uses 127.0.0.1 to avoid IPv6/IPv4 mismatch)

---

## 17. Maintenance Runbook

### Weekly

- [ ] Check `/admin/analytics` for assessment completion rates
- [ ] Review webhook delivery logs for failures
- [ ] Glance at GitHub Actions runs — investigate any red CI

### Monthly

- [ ] Verify nightly backups landed (`ls -la /opt/stacks/assessify/backups/` — should see ~30 files, each ~600 KB)
- [ ] Review and prune old test data (sessions, form submissions)
- [ ] Check Resend email delivery stats
- [ ] `npm audit` review — investigate any new HIGH/CRITICAL findings (8 moderates as of Apr 2026 are documented as non-exploitable)
- [ ] Prune Docker build cache on the VPS: `docker builder prune -af` (frees several GB after a busy deploy month)
- [ ] Spot-check `/admin/settings` MCP token list — revoke anything you don't recognize

### On Schema Change

1. Update `prisma/schema.prisma`
2. Add idempotent `ALTER TABLE` (or `CREATE TABLE`) block to the Dockerfile entrypoint — guard with a `PRAGMA table_info` / `sqlite_master` check
3. Rebuild: `docker compose build app`
4. Restart: `docker compose up -d app` (no `-v` — volume is preserved)
5. Verify migration applied: `docker compose exec app sqlite3 /app/data/dev.db ".schema TableName"`

The entrypoint runs migrations on **both** fresh-install and existing-volume paths (since v1.3), so a brand-new VPS provisioned from the seed will land on the current schema automatically.

### On Code Change

```bash
docker compose build app && docker compose up -d app
# No -v flag. Data is preserved.
```

### CI / GitHub Actions

[.github/workflows/test.yml](.github/workflows/test.yml) runs on every push to `main` and every PR:

1. `npm ci`
2. `npx prisma generate`
3. `npx tsc --noEmit` (typecheck)
4. `npx eslint src` (lint — must be 0 errors; warnings are policy-driven)
5. `npx vitest run` (full test suite, 124 tests as of Apr 2026)

Failure on any step blocks the merge by default. The lint policy is documented in [eslint.config.mjs](eslint.config.mjs): real correctness rules (purity, immutability, exhaustive-deps, unused-vars/expressions) are errors; over-strict React Compiler rules (`set-state-in-effect`, `static-components`) and `no-explicit-any` in legacy code are demoted to warnings.

### When tools change (MCP)

The MCP tool list is loaded once per Claude session at connector handshake time. After deploying new MCP tools:

1. The bundle inside the running container will reflect the change after `docker compose build && up -d`.
2. Existing Claude clients keep their cached tool list until they reconnect — toggle the connector off/on in Claude Settings, then start a new chat.
3. Verify with an authenticated `tools/list` call to confirm prod is serving the expected count.

---

## Appendix: Complete API Route Map

```
POST   /api/admin/auth                          Login
DELETE /api/admin/auth                          Logout
POST   /api/admin/change-password               Change password
POST   /api/admin/forgot-password               Request OTP
POST   /api/admin/verify-otp                    Verify OTP
POST   /api/admin/reset-password                Reset password

GET    /api/admin/assessments                   List assessments
POST   /api/admin/assessments                   Create assessment
GET    /api/admin/assessments/[id]              Get assessment
PATCH  /api/admin/assessments/[id]              Update assessment
DELETE /api/admin/assessments/[id]              Delete assessment
POST   /api/admin/assessments/[id]/publish      Publish/unpublish
POST   /api/admin/assessments/[id]/duplicate    Duplicate assessment

GET    /api/admin/assessments/[id]/sections              List sections
POST   /api/admin/assessments/[id]/sections              Create section
PATCH  /api/admin/assessments/[id]/sections/[sId]        Update section
DELETE /api/admin/assessments/[id]/sections/[sId]        Delete section

GET    /api/admin/assessments/[id]/sections/[sId]/questions              List questions
POST   /api/admin/assessments/[id]/sections/[sId]/questions              Create question
PATCH  /api/admin/assessments/[id]/sections/[sId]/questions/[qId]        Update question
DELETE /api/admin/assessments/[id]/sections/[sId]/questions/[qId]        Delete question

GET    /api/admin/question-bank                 List bank questions
POST   /api/admin/question-bank                 Add to bank
DELETE /api/admin/question-bank?id=...          Delete from bank

GET    /api/admin/invites                       List invites
POST   /api/admin/invites                       Create invite

GET    /api/admin/departments                   List departments
GET    /api/admin/job-roles                     List job roles
POST   /api/admin/job-roles                     Create job role
PATCH  /api/admin/job-roles/[id]                Update job role
DELETE /api/admin/job-roles/[id]                Delete job role

GET    /api/admin/competencies                  List competencies
POST   /api/admin/competencies                  Create competency
PATCH  /api/admin/competencies/[id]             Update competency
DELETE /api/admin/competencies/[id]             Delete competency

GET    /api/admin/sessions                      List sessions
GET    /api/admin/sessions/[id]                 Session detail
GET    /api/admin/analytics                     Analytics data
GET    /api/admin/webhooks                      List webhooks
POST   /api/admin/webhooks                      Create webhook
GET    /api/admin/hr-forms                      List form data
GET    /api/admin/hr-forms/[id]                 Form submission detail

GET    /api/assessments                         Public: list published
GET    /api/assessments/[slug]                  Public: get by slug
GET    /api/assess/invite/[code]                Validate invite
POST   /api/assess/invite/[code]/start          Start from invite

POST   /api/sessions                            Create session
GET    /api/sessions/[id]                       Get session
POST   /api/sessions/[id]/answers               Submit answers
POST   /api/sessions/[id]/complete              Complete session
GET    /api/sessions/[id]/result                Get result

GET    /api/forms/invite/[code]                 Validate form invite
POST   /api/forms/invite/[code]/start           Start form
GET    /api/forms/[submissionId]                Get submission
PUT    /api/forms/[submissionId]                Update submission

POST   /api/uploads                             Upload file
GET    /api/uploads/[filename]                  Get file

GET    /api/easter/route                        Get eggs
GET    /api/easter/hints                        Get hints
POST   /api/easter/claim                        Claim egg
POST   /api/easter/vault                        Vault unlock
POST   /api/easter/challenge-2                  Challenge 2
POST   /api/easter/track                        Track activity
GET    /api/easter/resume                       Resume state

# Health
GET    /api/health                              Liveness probe (used by Docker healthcheck)

# MCP / OAuth (Round 3)
POST   /api/mcp                                 JSON-RPC MCP — bearer token required, 60 req/min/IP
GET    /api/mcp                                 Server info (no auth)
POST   /api/oauth/register                      RFC 7591 Dynamic Client Registration
GET    /api/oauth/authorize                     OAuth consent screen (admin must be signed in)
POST   /api/oauth/authorize/consent             Approve / deny — mints auth code
POST   /api/oauth/token                         Exchange code for access + refresh tokens (PKCE S256)

# MCP token management (admin-only)
GET    /api/admin/mcp/tokens                    List own tokens
POST   /api/admin/mcp/tokens                    Mint manual bearer token
DELETE /api/admin/mcp/tokens/[id]               Revoke + permanently delete

# Leave management
GET    /api/leave                               List leave requests (filtered by role)
POST   /api/leave                               Create leave request
GET    /api/leave/[id]                          Request detail
PATCH  /api/admin/leave-balances/[employeeId]/reset  Reset balance (admin)
```

**Auth gate:** Every `/api/admin/*` endpoint above requires a valid admin session cookie (returns 401 otherwise) — except the explicitly public auth-flow endpoints (`auth`, `setup`, `forgot-password`, `reset-password`, `verify-otp`, all rate-limited).
