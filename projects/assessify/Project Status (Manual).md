---
type: status
maintained: manual
note: "Manually maintained. Graphify auto-extracts in this folder will not overwrite this file."
last_updated: 2026-04-27
---

# Assessify — Project Status

> **One-line:** Production HR + hiring assessment platform for Janus Digital. Drives candidate assessments, leave management, HR forms, and Claude-driven admin work via MCP.

**Live:** https://assessify.janusd.io · **Repo:** https://github.com/Jehada-Janusd/HR-Assessment-Platform · **Host:** Hostinger VPS (Caddy + Docker)

---

## What's shipped

### Core platform
- Next.js 16 App Router + TypeScript strict + Prisma v7 / SQLite (libsql adapter) + Tailwind v4 + shadcn (base-ui primitives)
- Docker (multi-stage) with named volume `assessify_data` → `/app/data/dev.db`
- Schema: 33 Prisma models with additive nullable migrations applied via Dockerfile entrypoint (never wipe the volume)
- Custom auth: HMAC session tokens + bcryptjs + rate limiting + audit log

### Assessment engine
- Department → JobRole → AssessmentTemplate → AssessmentVersion → Section → Question → AnswerOption
- Question Bank with section grouping (Cultural Fit / AI Awareness / Department-Specific / General)
- Scoring strategies: weighted_options / exact / partial / scenario_based / ranking
- Per-template recommendation thresholds (Strong Hire / Hire / Consider / Reject)
- 15+ competencies, per-section + per-competency aggregation
- PDF export for sessions
- **Real versioning live (Wave 2a):** draft / published / archived with hard refusal of edits to a published version that has in-flight sessions

### Leave management
- `/leave/new` public form → balance check → Slack DM workflow
- Manager Approve/Reject buttons → HR escalation on drained balance
- **CEO auto-approval (Bonaventure Wong)** — single-step with HR Acknowledge button (audit trail in `hrAcknowledgedAt` / `hrAcknowledgedBy`)
- Admin views at `/admin/leave-requests` and `/admin/leave-balances`
- PDF document generation (CEO layout simplified to single signature)

### HR forms
- Onboarding + Bank Details + custom form template builder
- Region-aware file validation (UAE = JPEG-only, etc.)
- Webhook to n8n at `https://n8n.janusd.io/webhook/2f1599d5-732f-4ab2-bde1-c879f2265451` (active workflow)

### Claude Connector (MCP)
- `/api/mcp` — JSON-RPC over HTTPS, OAuth 2.1 + PKCE + RFC 7591 Dynamic Client Registration
- **36 tools live** (was 12 originally — see [tool growth log](#mcp-tool-growth-log) below)
- Token rotation in-place on refresh; 24h access TTL; 60-day refresh TTL
- Origin tracking on each token (IP + device captured at consent)
- Skill at `skills/assessify-hr/` — installable in Claude Desktop as a Project for HR

### Easter egg hunt
- 4 difficulty tiers (easy → impossible)
- ROT13-encoded hints, admin leaderboard
- **Per-assessment toggle** (`AssessmentTemplate.eggHuntEnabled`) — was hardcoded to IT department, now flippable per assessment via portal or MCP

### Monitoring & alerts
- `slackAlert(...)` DMs Jehad (Nomi bot in `janus-digital.slack.com`) on prod errors with 5-min dedupe
- Wired into webhook dispatcher, email sends, MCP catch block, leave route, slack interactive route
- `/api/health` endpoint pings DB; Docker healthcheck uses it
- UptimeRobot polls `/api/health` every 5 min externally (covers VPS-down scenarios)

### Other
- 4 seeded departments: IT, Operations, HR, Finance
- 17 employees, 4 line managers
- Audit log for admin + MCP actions
- Branding: Janus Digital favicon + sidebar logo

---

## MCP tool growth log

| Round | Date | Tools | Notes |
|---|---|---|---|
| Bootstrap | Apr 2026 | 12 | 7 read + 5 write — basic create_assessment, search_*, list_departments, etc. |
| **Wave 1 (P1)** | Apr 2026 | +13 → 25 | Authoring surface — update_assessment, update_thresholds, add/update/remove/reorder sections, set_section_weights, add/update/reorder questions, create_question (Bank), attach/detach_question_to_section, competencyIds + thresholds extension on create_assessment |
| Egg hunt toggle | Apr 2026 | =25 | `eggHuntEnabled` field added to update_assessment input |
| **Wave 2a (P1.1 + P1.2)** | Apr 2026 | +11 → **36** | Read: get_session, list_sessions, get_session_results, get_assessment_analytics, get_question_analytics, export_sessions. Versioning: create_new_version, publish_version, list_assessment_versions, get_assessment_version, revert_to_version. Plus the in-flight session refusal gate on 11 existing mutators. |
| Wave 2b (planned) | — | +9 | Invite mgmt: get_invite, list_invites, revoke_invite, resend_invite, extend_invite_expiry, update_candidate, bulk_create_candidate_invites. Duplicate: duplicate_assessment, duplicate_question. |
| Wave 2c (planned) | — | +11+ | Admin CRUD (Department, Competency, JobRole), externalId idempotency, lookup_by_external_id, bulk_tag_questions, bulk_delete_questions, bulk_toggle_assessment_active. Schema columns already migrated. |

---

## Architecture decisions worth remembering

- **Operations layer at `src/lib/operations/`** — pure async functions wrapped by both portal API routes and MCP tool handlers. Single source of truth for business logic; portal and MCP never drift.
- **Validation layer at `src/lib/mcp/validation.ts`** — `requireAdmin`, `assertVersionEditable` (the in-flight gate), `assertWeightsSumToOne`, `assertCompetencyIdsExist`, etc. Throws `McpValidationError` / `McpPermissionError` with clean error envelopes.
- **Cursor pagination via `src/lib/mcp/pagination.ts`** — opaque base64 over `(createdAt DESC, id DESC)`. Default limit 25, max 100.
- **Audit log on every MCP write + every PII read** with `mcp.<entity>.<verb>` action. Filters captured, never row contents.
- **Idempotent ALTER TABLE in Dockerfile entrypoint** — schema migrations live in the `entrypoint.sh` heredoc. Never apply via `prisma migrate` on prod.
- **Vitest + ephemeral SQLite per test process** — `prisma db push` once at suite start, truncate-between-tests for isolation. 81 tests as of 2026-04-27.

---

## Production deploy procedure (summary)

```bash
# 1. Snapshot prod DB (every deploy)
ssh -i ~/.ssh/hostinger_janusd janusd@187.127.98.40 \
  'cd /opt/stacks/assessify && bash backup.sh'

# 2. Rsync changed files only — never sync .env / dev.db / node_modules / .next / src/generated/prisma
rsync -avz -e "ssh -i ~/.ssh/hostinger_janusd" <changed files> \
  janusd@187.127.98.40:/opt/stacks/assessify/

# 3. Rebuild + restart
ssh -i ~/.ssh/hostinger_janusd janusd@187.127.98.40 \
  'cd /opt/stacks/assessify && docker compose build app && docker compose up -d app'

# 4. Verify
curl -s https://assessify.janusd.io/api/health
```

Schema changes: add idempotent `ALTER TABLE` to the Dockerfile entrypoint **and** apply via `docker exec assessify-app sqlite3 ...` so the change is live before the rebuild.

---

## Known constraints

- **Resend free tier** only delivers to `jehada@janusd.io`. Custom domain not yet configured at resend.com/domains.
- **GitHub `gh` auth gotcha**: the user has two GitHub accounts cached in keyring (`HappyLife2`, `Jehada-Janusd`). HappyLife2 is often active by default and 403s on push. Fix: `gh auth switch --user Jehada-Janusd && gh auth setup-git`.
- **Slack bot scope**: Nomi needs `im:write` to start fresh DMs with users who haven't messaged the bot. If you add a new HR admin and they haven't pinged Nomi, the first DM uses `conversations.open` + retry to bootstrap the channel.
- **Versioning UI hidden in portal**: AssessmentVersion model exists and is now exercised by MCP, but the admin editor still shows "version 1" only. UI work to expose draft/published switch is out of scope for current waves.

---

## Pending workstreams

- **Wave 2b** — invite management (revoke / resend / extend / bulk) + duplicate (assessment / question)
- **Wave 2c** — admin CRUD for Department / Competency / JobRole + externalId idempotency on creates + bulk operations
- Custom Resend domain so candidate invite emails reach non-`@janusd.io` addresses
- Optional Database dashboard: Prisma Studio over SSH tunnel, or build `/admin/db` read-only browser in the portal (parked)

---

## Cross-links

- README + SOP live in the repo and are kept in sync with each release: `README.md` and `SOP.md`
- HR-facing skill: `skills/assessify-hr/SKILL.md` — paste into a Claude Desktop Project's instructions
- Memory (machine-readable): `~/.claude/projects/-Users-jehad-assessify/memory/`
