---
type: source
source_type: laptop
title: README
slug: readme
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
original_path: /Users/jehad/assessify/README.md
original_size: 11545
original_ext: .md
category: notes
extracted_with: text-copy
extracted_at: "2026-05-14T09:51:32Z"
sensitivity: dept
sensitivity_confidence: 0.90
sensitivity_reason: "Internal project README — operational"
project: assessify

---

# README

_Extracted from `[[assessify|assessify]]/README.md` on 2026-05-14._

# Assessify

A production-grade hiring assessment platform built for Janusd. Delivers immersive, scored assessments to candidates while giving HR teams a full admin suite with analytics, scoring engines, webhooks, and n8n automation.

> **Docs:** [📖 README](README.md) · [📘 SOP (full operations manual)](SOP.md)

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Framework | Next.js 16 (App Router, Turbopack) |
| Language | TypeScript (strict) |
| Database | SQLite via Prisma v7 + `@prisma/adapter-libsql` |
| UI | Tailwind CSS v4 + shadcn/ui (`@base-ui/react`) + Framer Motion |
| Email | Resend API |
| Auth | Custom session tokens (bcryptjs + HMAC) |
| Runtime | Docker (multi-stage, named volume) |
| Automation | Webhooks (HMAC-signed) + n8n integration |

## Features

### Admin Dashboard
- Department-organized overview with per-department stats
- Assessment builder (sections, questions, options, competency mapping, scoring rules)
- Duplicate assessments across job roles
- Question Bank with section grouping (Cultural Fit / AI Awareness / Department-Specific / General)
- Import questions from bank with department + section filtering
- Job role management per department
- Candidate invite system with email delivery
- Team member management (invite admins/users, deactivate, reset passwords, change roles)
- Role-based access control (Admin / User) with role badge in sidebar
- Session monitoring and PDF export of candidate results
- Webhook endpoint management
- Password management with OTP reset flow
- Full API documentation with cURL examples

### Assessment Engine
- 7 question types: Single Select, Multi Select, Ranking, Scenario, Situational Judgment, Short Text, Confidence Rating
- 4 scoring strategies: Weighted Options, Exact Match, Partial Credit, Scenario-Based
- Per-template recommendation thresholds (Strong Hire / Hire / Consider / Weak Fit / Reject)
- Versioned assessments — drafts vs published; in-flight sessions stay on their original version
- Competency-level scoring and aggregation
- Risk indicators and hiring summary generation
- Score calculator with quick-fill (best/worst/random)
- Live assessment preview

### Candidate Experience
- Invite-based access (unique codes via email)
- Section-by-section progression with progress tracking
- Timer support
- Completion screen with immediate feedback
- Easter egg hunt system (IT department, 4 challenges)

### HR Forms
- Built-in templates: Personal Data Onboarding, Bank Details
- Custom form template builder (8 field types: text, email, phone, date, textarea, dropdown, file upload, section heading)
- Template preview — see the form exactly as employees will
- Template management: create, edit, activate/deactivate, delete
- Region-aware file validation (UAE: JPEG only, SWIFT mandatory)
- File attachments as base64 in webhook payload for n8n processing
- Date formatting (DD/MM/YYYY)
- Dynamic field rendering for custom forms with validation

### Analytics
- Platform-wide overview dashboard (6 KPIs: invites, sessions, completed, completion rate, avg score, pass rate)
- Global recommendation distribution (Strong Hire → Reject)
- Per-assessment drill-down with funnel, competency heatmap, question performance, result distribution
- Assessment selector — click any assessment from the overview to see its detailed analytics

### Security & Production Hardening
- HMAC-signed admin session tokens (`SESSION_SECRET`)
- All `/api/admin/*` write endpoints gated by `getSession()` — unauthenticated requests return 401
- In-memory sliding-window rate limiting:
  - login: 5/min, forgot-password: 3/min, setup: 5/min
  - reset-password: 5/min, verify-otp: 5/min
  - `/api/mcp`: 60/min per IP (token-authenticated, defense-in-depth)
- Audit logging for all admin + MCP write actions (login, user mgmt, MCP tool calls, with IP + user-agent)
- Server-side assessment time-limit enforcement (auto-expires sessions)
- Automated database backup with 30-day rotation (`backup.sh`, runs nightly via cron on prod)
- [[github|GitHub]] Actions CI runs typecheck + lint + full vitest suite on every push and PR

### PDF Export
- Print-ready HTML report for any candidate session
- Includes: summary cards, hiring recommendation, section scores, competency scores, full question responses
- Accessible from session detail page → "Export PDF" button → browser print-to-PDF

### Claude Connector (MCP)

- Expose Assessify tools to Claude Desktop / Mobile via MCP over HTTPS at `/api/mcp`
- OAuth 2.1 flow with PKCE + Dynamic Client Registration (RFC 7591)
- Two token paths: OAuth (auto-minted when Claude connects) or manual bearer tokens from `/admin/settings`
- Per-user scoping — each admin only sees their own tokens; only admins can create manual tokens
- Origin tracking — IP address + device (macOS/Windows/iOS/...) captured at consent and shown on each token card
- Auto-generated names use the approving admin's email (e.g. `Claude · jehada@janusd.io`)
- Trash icon fully revokes **and** deletes the record; audit log preserves the evidence
- **57 tools** (Round 3, 2026-04):
  - **Read / search (9):** list_departments, list_competencies, search_assessments, search_job_roles, search_candidates, search_questions, get_assessment, get_session, get_session_results
  - **Authoring (11):** create_assessment, create_job_role, create_question, add_question, add_section, attach_question_to_section, set_section_weights, update_thresholds, create_competency, create_department, create_candidate_invite
  - **Editing (8):** update_assessment, update_question, update_section, update_competency, update_department, update_job_role, reorder_sections, reorder_questions
  - **Versioning (5):** create_new_version, publish_version, list_assessment_versions, get_assessment_version, revert_to_version
  - **Sessions / analytics (5):** list_sessions, get_assessment_analytics, get_question_analytics, export_sessions, toggle_assessment_active
  - **Invite management (7):** get_invite, list_invites, revoke_invite, resend_invite, extend_invite_expiry, update_candidate, bulk_create_candidate_invites
  - **Duplicate / clone (2):** duplicate_assessment, duplicate_question
  - **Admin archive (3):** archive_competency, archive_department, archive_job_role
  - **Automation (4):** lookup_by_external_id, bulk_tag_questions, bulk_delete_questions, bulk_toggle_assessment_active
  - **Destructive (3):** delete_question, detach_question_from_section, remove_section
- Idempotency via optional `externalId` on every `create_*` tool — duplicate calls return the existing record (`idempotent: true`) instead of creating a duplicate

## Project Structure

```
src/
  app/
    admin/           # 21 admin pages (dashboard, assessments, invites, analytics, settings, api-docs, etc.)
    assess/          # Candidate assessment flow
    forms/           # HR onboarding forms
    api/             # 67 API routes
      admin/         # Admin CRUD APIs
      sessions/      # Candidate session APIs
      assess/        # Invite validation + start
      forms/         # Form submission APIs
      easter/        # Easter egg APIs
      uploads/       # File upload APIs
  components/
    ui/              # 28 shadcn/ui components
    assessment/      # 7 assessment-specific components
    admin/           # 3 admin components
  lib/
    auth.ts          # Session management
    db.ts            # Prisma client singleton
    scoring-engine.ts# Full scoring pipeline
    analytics.ts     # Event tracking + queries
    email.ts         # Resend templates
    webhooks.ts      # HMAC-signed dispatch
    easter-eggs.ts   # Easter egg logic
    file-validation.ts# Region-aware file rules
    utils.ts         # Tailwind class merging
prisma/
    schema.prisma    # 25 models
    seed.ts          # 4 departments, 6 roles, 15 competencies, 1 full assessment
```

## Data Model (33 Models)

**Core:** Department, JobRole, Competency

**Assessments:** AssessmentTemplate, AssessmentVersion, Section, Question, AnswerOption, QuestionCompetency

**Candidates:** CandidateSession, CandidateResponse, CandidateInvite, CandidateResult, CandidateSectionScore, CandidateCompetencyScore

**Analytics:** AnalyticsEvent

**Webhooks:** WebhookEndpoint, WebhookDelivery

**Admin:** AdminUser, PasswordOtp, AuditLog

**HR Forms:** FormTemplate, FormInvite, FormSubmission, FormFile

**Easter Eggs:** EasterEggClaim

**Leave Management:** Employee, LineManager, LeaveRequest, LeaveBalance

**Claude Connector (MCP):** McpToken, OAuthClient, OAuthAuthorizationCode

## Getting Started

### Prerequisites
- Docker and Docker Compose
- Node.js 22+ (for local dev)

### Docker (Recommended)

```bash
# Clone and configure
git clone https://github.com/Jehada-Janusd/HR-Assessment-Platform.git
cd HR-Assessment-Platform
cp .env.example .env   # Add your Resend API key

# Build and run
docker compose build
docker compose up -d

# Access
open http://localhost:3000/admin
```

The entrypoint script automatically initializes the database from seed data on first run and applies idempotent migrations on subsequent starts.

### Local Development

```bash
npm install
npx prisma generate
npx prisma db push
npx ts-node --compiler-options '{"module":"commonjs"}' prisma/seed.ts
npm run dev
```

### Environment Variables

| Variable | Description |
|----------|-------------|
| `DATABASE_URL` | SQLite path (default: `file:./dev.db`) |
| `RESEND_API_KEY` | Resend API key for email delivery |
| `APP_URL` | Base URL (default: `http://localhost:3000`) |
| `JWT_SECRET` | Secret for session tokens |

## API Overview

Full API documentation is available at `/admin/api-docs` with cURL examples for every endpoint.

| Area | Endpoints | Description |
|------|-----------|-------------|
| Auth | 6 | Login, logout, password management, OTP, account setup |
| Assessments | 7 | CRUD, publish, duplicate |
| Sections / Questions | 4 | CRUD within assessments |
| Question Bank | 1 | Cross-department question reuse |
| Sessions | 5 | Candidate assessment flow |
| Invites | 2 | Create and validate invites |
| Job Roles | 3 | CRUD per department |
| Departments | 1 | List departments |
| Competencies | 3 | CRUD competencies |
| HR Forms | 4 | Form invites, submissions, files |
| Analytics | 1 | Aggregated stats |
| Webhooks | 1 | Endpoint management |
| MCP / OAuth | 6 | JSON-RPC MCP server + OAuth 2.1 (DCR, authorize, token, consent) |
| MCP Token Mgmt | 2 | Manual bearer token CRUD in `/admin/settings` |
| Leave Mgmt | ~4 | Leave requests, balances, reset (employees + line managers) |
| Easter Eggs | 6 | Hidden gamification |
| Uploads | 2 | File upload + retrieval |
| Health | 1 | `/api/health` for liveness / proxy probes |

## Seeded Data

The seed script provisions:
- **4 departments:** Information Technology, Operations, Human Resources, Finance
- **6 job roles** across departments
- **15 competencies** (Communication, Troubleshooting, AI Readiness, etc.)
- **1 complete assessment** (IT Support Specialist) with 3 sections, 21 questions, full scoring rules
- **2 HR form templates** (Personal Data Onboarding, Bank Details)

## Docker Volume

Data persists in a named Docker volume (`assessify_data` mounted at `/app/data`). The entrypoint script:
1. Checks if `dev.db` exists in the volume
2. Copies `seed.db` if not (first run)
3. Applies additive column migrations idempotently via `sqlite3`

**Important:** Never run `docker compose down -v` unless the schema has changed. This wipes all data.

## License

Private repository. All rights reserved.
