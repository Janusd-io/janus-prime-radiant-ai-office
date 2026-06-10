---
type: project
title: Assessify
slug: assessify
created: 2026-05-14
updated: 2026-06-09
captured_by: jehad-altoutou
status: live
owner: jehad-altoutou
departments: [hr]
confidence: working
audience: department
path: /Users/jehad/assessify
repo: https://github.com/Jehada-Janusd/HR-Assessment-Platform
migrated_from: personal-obsidian-vault
---

# Assessify

**One-line description:** Production-grade hiring assessment platform with scoring engine, analytics, HR onboarding forms, and n8n automation.

**Status:** 🟢 Active

## Stack
- **Framework:** Next.js 16 (App Router, Turbopack, async params) — ⚠️ breaking changes from training data, read `node_modules/next/dist/docs/` before writing Next code
- **DB:** Prisma v7 + SQLite via `@prisma/adapter-libsql`
- **UI:** Tailwind v4 + shadcn/ui (on `@base-ui/react`, NOT Radix) + Framer Motion
- **Email:** Resend (free tier → only sends to `jehada@janusd.io`)
- **Runtime:** Docker (`docker-compose.yml`), named volume `/app/data`, entrypoint does idempotent SQL migrations via `sqlite3`
- **Tech stack profile:** [[saas-default-stack]]

## Goal
Replace boring hiring assessments with a premium, data-rich, automation-ready product. Serves candidates (immersive UX) and internal teams (scoring, analytics, webhooks, n8n).

## Key Decisions
- *(2026-04-10)* Library templates (`library-{deptSlug}`, `isActive=false`) hold standalone bank questions — hidden from candidate picker
- *(2026-04-13)* Question Bank section grouping: Cultural Fit / AI Awareness / Department-Specific / General (normalized per section slug)
- *(2026-04-13)* **Versioning concept removed from UI** — assessments edit in place. `versionNumber` still exists in schema for candidate-session integrity but is invisible
- *(2026-04-10)* HR forms send files as base64 in webhook payload (not server storage) so n8n can attach them directly
- *(ongoing)* Never wipe Docker volume (`docker compose down -v`) unless schema changed — see [[jehad-altoutou]] standing rule

## Live Credentials / URLs (local)
- Admin: `http://localhost:3000/admin` — `jehada@janusd.com`
- Candidate: `/assess/invite/[code]`
- HR form: `/forms/[code]`
- API docs: `/admin/api-docs`

## Architecture Quick-Map
Use the graph dump in [[_COMMUNITY_Assessment Editor Page|graph communities]] instead of re-reading source. Key communities:

- [[_COMMUNITY_API Routes (AdminForms)|API Routes (Admin/Forms)]] — 50 nodes, all `GET/POST/PATCH/DELETE` handlers (god nodes: `GET()` 31 edges, `POST()` 22)
- [[_COMMUNITY_Assessment Editor Page|Assessment Editor]] — the big edit page (`src/app/admin/assessments/[id]/edit/page.tsx`) — cohesion 0.14, candidate for future split
- [[_COMMUNITY_Scoring Engine|Scoring Engine]] — `src/lib/scoring-engine.ts` — `scoreQuestion`, `scoreWeightedOptions`, `scoreExact`, `scorePartial`, `calculateRecommendation`, `parseThresholds`
- [[_COMMUNITY_Analytics Functions|Analytics]] — `src/lib/analytics.ts` — funnel, competency heatmap, question analytics, result distribution
- [[_COMMUNITY_Auth & Sessions|Auth]] — `src/lib/auth.ts` — `createSession`, `destroySession`, `generateToken`, `parseToken`, `requireAuth`
- [[_COMMUNITY_Email Sending|Email]] — `src/lib/email.ts` — separate templates for invite vs onboarding
- [[_COMMUNITY_Webhook Dispatcher|Webhooks]] — `src/lib/webhooks.ts` — HMAC-signed
- [[_COMMUNITY_File Validation Rules|File Validation]] — `src/lib/file-validation.ts` — region-aware rules (UAE: JPEG only, SWIFT mandatory in bank form)
- [[_COMMUNITY_Easter Egg Logic|Easter Eggs]] — `src/lib/easter-eggs.ts` — IT-only, 4 eggs, rot13 hints

## How Claude Should Use This Graph
Before grepping source for "where is X":
1. Check [[_COMMUNITY_API Routes (AdminForms)|relevant community note]] — it lists every node with source path + line
2. Check the individual node note (e.g. `scoreQuestion().md`) — has `source_file`, `source_location`, and outgoing edges
3. Open the source file only for the specific line range

This cuts token usage ~2400× vs reading the whole corpus (benchmarked).

Re-run `/graphify /Users/jehad/assessify --update --obsidian --obsidian-dir "/Users/jehad/Documents/Obsidian Vault/03 Projects/Assessify"` after any significant code change.

## Progress Log
- *(2026-04-10)* Phase 1-2D complete — CRUD, preview, recommendation thresholds, score calculator, duplicate, job-role management
- *(2026-04-13)* Question Bank section grouping + filtered import picker (department + section)
- *(2026-04-13)* Version UI removed — assessments directly editable
- *(2026-04-13)* New Assessment description field → textarea (was unclickable)
- *(2026-04-13)* Graphify dump → 451 notes imported into this vault
- *(2026-04-14)* Admin user invite system — invite via email, role picker (Admin/User), account setup page with password strength bar
- *(2026-04-14)* Role-based access control — Admin can manage users (deactivate, reset password, change role, delete); User role view-only
- *(2026-04-14)* Role badge in sidebar (next to user name) and team members list
- *(2026-04-14)* Full README rewrite + SOP document added
- *(2026-04-14)* Graph updated → 480 notes, 364 nodes, 303 edges, 116 communities
- *(2026-04-14)* Production hardening: HMAC-signed tokens, rate limiting, audit logging, session expiry enforcement, PDF export, backup script
- *(2026-04-14)* Analytics dashboard revamped — platform-wide overview with 6 KPIs, per-assessment drill-down
- *(2026-04-14)* README updated with security/PDF/team sections; SOP v1.1 with 3 new sections
- *(2026-04-14)* Custom form template builder — 8 field types, preview, dynamic candidate rendering
- *(2026-04-14)* PDF report redesigned — compact layout, header first page only, no confidence text
- *(2026-04-14)* Confidence (i) tooltip on session detail page
- *(2026-04-14)* Graph updated → 481 notes, 363 nodes, 298 edges, 118 communities
- *(2026-04-16)* Database cleaned for demo — all transactional data purged, structure preserved (1 admin, 4 depts, 6 roles, 4 templates, 3 form templates)
- *(2026-04-16)* Resend `.env` fix — API key was concatenated with SESSION_SECRET (missing newline). New key deployed, container recreated.
- *(2026-04-16)* n8n Bank Details workflow completed — full pipeline: folder check → create → HTML doc → Google Doc conversion → Slack notification
- *(2026-04-16)* n8n Error Handler workflow built — Error Trigger → Google Sheets log + Slack DM. Requires Error Workflow setting on each monitored workflow.
- *(2026-04-17)* Docker + ngrok verified live. Graph notes: 611 in vault.

## n8n Automation Workflows
Hosted at `https://n8n.srv1086109.hstgr.cloud`. Webhook endpoint: `/webhook/2f1599d5-732f-4ab2-bde1-c879f2265451`

### HR Document Processor (main workflow)
- **Trigger:** Webhook `POST` from Assessify form submissions
- **Router:** Switch node on `formType` / `formName`
  - `bank_details` → Bank Details branch
  - `Personal Data Form` → Personal Data branch
- **Both branches share the same pattern:**
  1. Check if employee folder exists in [[Google Drive Integration|Google Drive]] (`HR Documents/`)
  2. Create folder if missing
  3. Upload file attachments (base64 → binary → Google Drive)
  4. Generate styled HTML table from form data (Code node)
  5. Upload HTML → Google Drive → Copy as native Google Doc → Delete temp HTML
  6. Send Slack notification to `jehada` with folder link
- **Credentials:** Janus GDrive OAuth2, Janus Slack API
- **Google Drive parent folder:** `1V2LhE-_eyqNsMSFySq9mMWU7u51DAtkz` (HR Documents)

### Error Handler Workflow
- **Trigger:** Error Trigger node (n8n built-in)
- **Actions:** Log to Google Sheets ("Error Logs") + Slack DM
- **Fields:** Workflow name, error message, last node executed, execution URL, timestamp
- **Setup required:** Each monitored workflow must set this as its Error Workflow in Settings
- **Important:** Only triggers on production executions (webhook/schedule), NOT manual test runs

## Deployment & Access
- **Docker:** `assessify-app-1` container, volume `assessify_data` at `/app/data`
- **DB:** SQLite at `/app/data/dev.db` inside container
- **ngrok:** `https://disseminative-indistinctive-roseanne.ngrok-free.dev` → `localhost:3000`
- **Demo reset:** Backup + truncate transactional tables (sessions, responses, results, invites, submissions, analytics, audit logs) — keep admin/templates/departments/roles

## Open / Next
- [ ] Custom domain + HTTPS setup (waiting on IT for hosting decision)
- [x] ~~Resend domain verification~~ — Fixed: `.env` had RESEND_API_KEY and SESSION_SECRET on same line (no newline). New key deployed `re_GwM...`. Free tier still only delivers to account owner email.
- [x] ~~n8n production workflow wiring~~ — Bank Details + Personal Data branches complete
- [x] ~~Error handler workflow~~ — Logging to Google Sheets + Slack
- [ ] Build assessments for Operations, HR, Finance departments (content work)
- [ ] Set up cron for `scripts/backup.sh` on production host
- [ ] Verify Resend with custom domain for sending to external candidates

## Related
- [[jehad-altoutou]]
- [[saas-default-stack]]
- [[n8n-workflow|/n8n-workflow]]
- [[n8n-code|/n8n-code]]
- [[n8n-debug|/n8n-debug]]
- [[docker-build|/docker-build]]
- [[deploy|/deploy]]
- [[database-optimize|/database-optimize]]
- [[api-security|/api-security]]
- [[graphify|Graphify skill]]
- [[index|Home]]

## Auto-Memory
Also tracked in `/Users/jehad/.claude/projects/-Users-jehad-assessify/memory/` — those memories survive across all conversations; this note is for human + semantic-graph access.

---

## Notes — assessify-hr skill

_Migrated from the personal-vault 'AI Office Brain' base, 2026-06-09._

# /assessify-hr — Assessify platform driver

Drives the Assessify HR platform via its MCP connector for Janus Digital HR. Single skill the user invokes directly when working on assessments, candidate invites, or HR taxonomy.

## When to use

Trigger phrases include:
- *"Create a new assessment on Assessify"* / *"Show me the assessments"*
- *"Add a question to the IT Support assessment"*
- *"Set the section weights"* / *"Update thresholds"*
- *"Invite [candidate] to take [assessment]"*
- *"On Assessify, [...]"* / *"[...] on Assessify"*
- *"New job role"* / *"Add a competency"* / *"Create a department"*

## What it does

Drives the full Assessify domain model:

- **Assessments** — create, edit, duplicate, version (publish / revert), activate / deactivate, search, analytics
- **Sections** — add to assessment, set weights, set thresholds, reorder, remove
- **Questions** — create, update, delete, duplicate, attach/detach to sections, bulk delete, bulk tag, reorder, search, analytics
- **Job roles** — create, update, archive, search
- **Departments** — create, update, archive, list
- **Competencies** — create, update, archive, list
- **Candidate invites** — create, bulk create, list, get, resend, revoke, extend expiry
- **Sessions** — list, get, get results, export
- **Candidates** — search, update
- **Lookup** — by external ID

## Where Assessify fits

Assessify is one of the platforms supporting Janus's recruitment workflow. The broader recruitment work is tracked on [[monday]] — that board has items for the centralised recruitment tracker, AI-driven CV scoring, Fireflies post-interview analysis, leave management, etc. Assessify itself is the assessment engine within that pipeline.

The current operational state: SSFI/Assessify HR platform is in **In Testing** on [[monday]] (item `2881310536`); active expansion work tracked on [[monday]].

## Source of truth

The Assessify SaaS platform itself. This skill is the only writer.

Every `*_create` / `*_update` / `*_delete` operation hits Assessify directly. There is no caching layer between this skill and the platform.

## Not orchestrated by [[standup]]

[[assessify]] is a peer skill, not a subagent of [[standup]]. The standup may surface a Monday task (e.g., "build CV intake form on Assessify") that the user later actions by invoking [[assessify]] manually.

## Naming conventions

- **British English** in all assessment text, question wording, and documentation
- **Job role names** match what HR uses in Deel and elsewhere
- **Competency names** are stable across roles where possible (e.g., "Critical Thinking" rather than "Critical Thinking — Engineering" if the same skill is shared)

## Related

- Operational item: [[monday]] → Assessify HR platform (id `2881310536`)
- Recruitment pipeline: [[monday]] (board `5095636727`)
- Orchestrator (indirect): [[standup]] surfaces Assessify-related tasks but does not dispatch this skill

## Code graph
Full node index: [[assessify-graph-index|assessify code graph index]] (all graphify nodes). Clustered views in the `_COMMUNITY_*` notes; visual map in `graph.canvas`.
