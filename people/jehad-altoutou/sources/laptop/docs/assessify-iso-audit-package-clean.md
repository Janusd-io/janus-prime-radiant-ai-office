---
type: source
source_type: laptop
title: Assessify-ISO-Audit-Package-CLEAN
slug: assessify-iso-audit-package-clean
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/docs/Assessify-ISO-Audit-Package-CLEAN.docx
original_size: 96923
original_ext: .docx
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:32Z"
---

# Assessify-ISO-Audit-Package-CLEAN

_Extracted from `assessify/docs/Assessify-ISO-Audit-Package-CLEAN.docx` on 2026-05-14._

# Table of Contents

# Assessify — ISO/IEC 27001:2022 Audit Package

**Document Owner:** Jehad Altoutou, Janus Digital **System Owner /
Technical Lead:** Jehad Altoutou **Document Version:** 1.0 **Effective
Date:** 28 April 2026 **Review Cycle:** Annual (next review: April 2027)
**Classification:** Internal — for authorised auditors

------------------------------------------------------------------------

> **Note for the auditor:** This package is written against ISO/IEC
> 27001:2022 Annex A. If your engagement is scoped to ISO/IEC 27017
> (cloud) or 27018 (cloud PII), Sections 9 (Suppliers) and 12
> (Compliance) are written to extend cleanly. If your engagement is SOC
> 2 instead, the same controls map to the Trust Services Criteria — call
> out where you'd like cross-references.

------------------------------------------------------------------------

## 1. Executive Summary

**Assessify** is a self-hosted hiring assessment and HR onboarding
platform operated by Janus Digital. It enables HR teams to administer
scored assessments to candidates, capture personal data and bank-details
forms during onboarding, and deliver structured results to downstream
systems.

The platform processes **candidate personal data (name, email, IP,
assessment responses, scores)** and **employee personal data (full name,
date of birth, address, family information, bank details, scanned
documents)**. As such it is in scope for an Information Security
Management System (ISMS) under ISO/IEC 27001:2022 and for personal-data
protection obligations under any applicable national PII regulation.

This document describes the controls implemented to protect the
confidentiality, integrity, and availability of data processed by
Assessify, and provides evidence pointers for each control.

------------------------------------------------------------------------

## 2. Scope of the ISMS

### 2.1 In scope

| Asset | Type | Location | Data classification |
|----|----|----|----|
| Assessify production application | Software | Hostinger VPS (Malaysia, Kuala Lumpur) | Internal |
| Production database | SQLite file in Docker volume | Hostinger VPS, encrypted at rest by VPS provider | **Confidential** (PII) |
| Source code repository | GitHub private repo | github.com (SaaS) | Internal |
| Email-delivery service | Resend API | SaaS provider | Internal (transit only) |
| Reverse proxy | Caddy 2 | Hostinger VPS | Internal |
| Workflow automation | n8n | Adjacent Hostinger container | Internal |
| Backups | SQLite snapshots, 30-day retention | Hostinger VPS local disk | **Confidential** (PII) |
| MCP integration endpoint (Claude AI) | HTTPS API | Same VPS | Internal |

### 2.2 Out of scope

- Candidate / employee personal devices (used to fill in assessments and
  forms).
- Janus Digital corporate IT estate (laptops, email, identity provider).
- Hostinger's underlying hypervisor and physical data centre — covered
  by the supplier's own attestations (see § 9).

### 2.3 Roles & responsibilities

| Role | Person / Function | Responsibility |
|----|----|----|
| System owner | Jehad Altoutou | Day-to-day operation, deploys, incident response |
| Data controller | Janus Digital HR | Decides what assessments / forms to deploy, retains results |
| Data processor | Assessify (this system) | Stores and processes data on behalf of HR |
| Hosting provider | Hostinger International Ltd. | VPS infrastructure |
| Email provider | Resend | Transactional email delivery |
| Code-quality reviewer | GitHub Actions CI | Automated checks on every change |

------------------------------------------------------------------------

## 3. System Architecture (data flow + trust boundaries)

The diagram below shows every data flow and the trust boundary each
crosses. Render with [mermaid.live](https://mermaid.live) for a PNG /
SVG export, or view directly on GitHub which renders Mermaid natively.

<img src="media/rId15.png" style="width:5.83333in;height:5.76742in"
alt="Assessify — system architecture, data flows, and trust boundaries" />

**Connection legend.** Numbers correspond to the labelled arrows in the
diagram.

| \# | Direction | Protocol | Authentication |
|----|----|----|----|
| 1 | Candidate → Caddy | HTTPS (TLS 1.2+) | Single-use invite code (time-limited) |
| 2 | Employee → Caddy | HTTPS (TLS 1.2+) | Single-use form code (time-limited) |
| 3 | HR Admin → Caddy | HTTPS (TLS 1.2+) | Email + bcrypt password → HMAC-signed session cookie |
| 4 | Claude (MCP) → Caddy | HTTPS (TLS 1.2+) | OAuth 2.1 + PKCE (S256) bearer token |
| 5 | Application ↔ Database | Local Docker volume mount | Filesystem permissions (root-only) |
| 6 | Database → Backups | Local filesystem (cron) | Nightly snapshot via SQLite online `.backup` |
| 7 | Application → Resend | HTTPS API | API key from `.env`, never logged |
| 8 | Application → n8n | HTTPS | HMAC-SHA256 signed webhook payloads |
| 9 | GitHub → Application | SSH (rsync) | Key-based SSH (no password auth); CI must pass first |

**Zone definitions.** "External access — public network" refers to the
**network medium** (the public internet) that all four user types
traverse to reach the system; it is outside the ISMS perimeter because
we cannot enforce controls on the user's device or their network path.
**Authentication trust differs per user type** (single-use invite code,
password + HMAC-signed session cookie, OAuth 2.1 + PKCE) and is enforced
at Caddy plus the application layer, regardless of which network the
user is connecting from. HR admins and Janus Digital staff are trusted
personnel — only the network medium they reach the system over is
outside the perimeter.

**Trust boundaries crossed:**

1.  Public network → Caddy: TLS terminated at Caddy, certificate
    auto-renewed by Let's Encrypt.
2.  Caddy → application: localhost network on the VPS; not accessible
    from the public internet.
3.  Application → data zone: Docker named volume, root-only filesystem
    permissions.
4.  Application → external SaaS: HTTPS, with API keys held in
    environment variables that are never logged.
5.  GitHub → VPS: pushes deploy via authenticated `rsync` over SSH
    (key-based, no password authentication).

------------------------------------------------------------------------

## 4. Data Inventory & Classification

| Data category | Examples | Classification | Storage | Retention |
|----|----|----|----|----|
| Candidate identity | Name, email | **Confidential / PII** | SQLite | Indefinite (configurable per assessment) |
| Candidate behaviour | Assessment responses, IP at session, time spent | **Confidential / PII** | SQLite | Indefinite |
| Employee identity | Full name, DOB, nationality, marital status, religion | **Confidential / PII** | SQLite | Indefinite |
| Employee family data | Spouse, children, parents | **Confidential / PII** | SQLite | Indefinite |
| Employee bank details | Account, IBAN, SWIFT, scanned IDs | **Confidential / PII** | SQLite + base64 in webhook payload | Indefinite |
| Admin user accounts | Name, email, bcrypt password hash, role | **Confidential** | SQLite | Until offboarding |
| Audit log | Who did what, when, from which IP | **Internal** | SQLite | Indefinite |
| MCP tokens | SHA-256 hash, prefix, IP + UA at consent | **Confidential** | SQLite | Until revoked or expired (1h access / 60d refresh) |
| Operational telemetry | Container logs (capped 20 MB × 3) | **Internal** | Docker logs | ~1–2 days rolling |

> **Action for the data controller (HR):** define an explicit retention
> policy per data category (e.g. *"candidate sessions deleted 24 months
> after completion unless the candidate is hired"*). Assessify supports
> retention through a future maintenance task; the auditor may flag this
> as a gap to be closed.

------------------------------------------------------------------------

## 5. Access Control (Annex A.5.15 – A.5.18, A.8.2 – A.8.5)

### 5.1 User identification & authentication

- **HR admins** authenticate with email + password. Passwords are hashed
  using bcrypt (12 rounds, industry standard). Sessions are issued as
  HMAC-SHA256-signed tokens stored in `httpOnly`, `Secure`,
  `SameSite=Lax` cookies, expiring after 24 hours.
- **Candidates** access assessments via a single-use, time-limited
  invite code emailed to them. No password is ever set for candidates.
- **AI integration clients** (Claude Desktop / Mobile) authenticate via
  OAuth 2.1 with PKCE (S256 challenge). Access tokens expire after 1
  hour; refresh tokens are rotated and expire after 60 days.

### 5.2 Authorisation

- The application enforces `getSession()` on every `/api/admin/*` write
  endpoint. Unauthenticated calls receive HTTP 401. *(Verified by
  automated probe against production.)*
- Two roles exist: `admin` (full control) and `user` (read-only
  dashboards). Backend enforces `session.role === "admin"` on management
  operations.
- MCP tokens are scoped per user; an admin only sees and revokes their
  own tokens.

### 5.3 Account lifecycle

- New admin invites are sent via OTP-validated invite link. The invite
  expires after 24 hours and is single-use.
- Password reset flow uses a 6-digit OTP, valid 10 minutes. Rate-limited
  at 3 requests / minute per IP.
- Deactivation: admin record sets `isActive = false`, which immediately
  invalidates session lookups even if the cookie hasn't expired.

### 5.4 Privileged access

- Operating-system root on the VPS is held by the System Owner only.
  Root SSH login is **disabled**; access is via a non-root `janusd` user
  with key-based SSH (no password auth). Public-key fingerprint is held
  by the System Owner in `~/.ssh/`.
- No shared accounts exist.

------------------------------------------------------------------------

## 6. Cryptography (Annex A.8.24)

| Use case | Algorithm | Key management |
|----|----|----|
| Web traffic in transit | TLS 1.2+ | Certificate auto-issued and renewed by Let's Encrypt via Caddy ACME |
| Admin session tokens | HMAC-SHA256 | `SESSION_SECRET` 48-character random, stored only in `.env` on the VPS |
| Password storage | bcrypt (12 rounds) | Per-password salt; never logged |
| Webhook payloads | HMAC-SHA256 signature | Per-endpoint shared secret generated server-side |
| MCP token storage | SHA-256 of raw token | Raw value shown to user once at creation; never persisted, never logged |
| Backups | None at application layer | At-rest disk encryption is the responsibility of the VPS provider |

> **Auditor note:** disk encryption on the Hostinger VPS is the
> provider's responsibility; their attestation should be referenced
> under § 9.

------------------------------------------------------------------------

## 7. Operational Security (Annex A.5.30 – A.5.32, A.8.6 – A.8.16)

### 7.1 Logging & monitoring (A.8.15, A.8.16)

- **Audit log** (`AuditLog` table): every administrative action and
  every MCP tool call captures `userId`, `userEmail`, `action`,
  `targetType`, `targetId`, `details` (JSON), `ipAddress`, `createdAt`.
  Log entries are append-only at the application layer.
- **Container logs** (Docker JSON-file driver): capped at 20 MB × 3
  files per container to prevent disk exhaustion.
- **Container health**: `/api/health` is probed every 30 seconds by
  Docker's healthcheck. Unhealthy state is visible via `docker inspect`
  and the operations team.
- **Application errors**: caught at the route level and reported via
  `slackAlert()` to the engineering Slack channel for awareness.

### 7.2 Capacity & vulnerability management (A.8.6, A.8.8)

- VPS resource thresholds are tracked through Hostinger's panel and
  `df`/`free` checks during operational reviews.
- `npm audit` is reviewed monthly. Current state: 0 critical, 0 high, 8
  moderate vulnerabilities — each documented as non-exploitable in the
  runtime path (full analysis in the relevant commit message).
- All HIGH-severity advisories are patched as soon as a vendor fix is
  available.

### 7.3 Backup (A.8.13)

- Nightly backup at 03:00 UTC via `backup.sh`, executed by `cron` on the
  VPS. Uses SQLite's online `.backup` API so the application is never
  paused.
- 30-day rotation; older backups are deleted automatically.
- Backups are stored on the same VPS local disk (gap: no off-site backup
  at present — see § 11.1).

### 7.4 Change management (A.8.32)

- All code changes are made on a feature branch and merged to `main`
  only after passing GitHub Actions CI: TypeScript type-check, ESLint,
  and the full automated test suite (124 tests).
- Production deploys follow a documented runbook: pre-deploy backup →
  rsync of changed files only → image rebuild → container restart →
  smoke test. *(Documented in Section 17 of the technical SOP.)*
- Schema changes are encoded as idempotent `ALTER TABLE` statements in
  the Docker entrypoint — the only source of truth for production
  migrations — so they apply identically to fresh installs and existing
  volumes.

### 7.5 Secure development (A.8.25 – A.8.28)

- TypeScript strict mode is enforced.
- ESLint blocks merges on real correctness rules (React purity /
  immutability / hook dependencies, unused declarations).
- All web routes that handle administrative data require an
  authenticated session. This is verified both by code review (every new
  admin route) and by automated testing.

------------------------------------------------------------------------

## 8. Communications Security (Annex A.8.20 – A.8.23)

- All public traffic is encrypted in transit (TLS 1.2 minimum, enforced
  by Caddy).
- HTTP requests redirect to HTTPS automatically.
- Outbound traffic to external services (Resend, n8n webhooks) is HTTPS
  only.
- Internal traffic between Caddy and the application is on the localhost
  loopback inside the VPS — not reachable from the public internet.

------------------------------------------------------------------------

## 9. Supplier & Third-Party Relationships (Annex A.5.19 – A.5.23)

| Supplier | Service | Compliance posture | Risk mitigation |
|----|----|----|----|
| Hostinger International Ltd. | Virtual Private Server | Public-facing security policy; KVM virtualisation; ISO 27001 not formally claimed by Hostinger but they publish security commitments | Own all data on a named Docker volume; daily backups; can migrate to another VPS provider in \<1 day |
| Resend | Transactional email API | Resend is SOC 2 Type II audited (verify currency at audit time) | Only candidate names + email addresses + invite links are sent; no scores or PII details transit Resend |
| Let's Encrypt (via Caddy) | TLS certificate authority | Long-standing CA, free, automated | Certificate auto-renewal monitored by Caddy itself |
| GitHub (Microsoft) | Source code hosting + CI | SOC 1, SOC 2, ISO 27001, ISO 27018 (verify) | Repository is private; deploy keys rotated on team change |
| n8n | Workflow automation (self-hosted on the same VPS) | Self-hosted, no external trust | Same trust zone as the app |

The data controller (Janus Digital HR) is responsible for confirming
that current contracts with Hostinger and Resend remain in force and
that their published compliance attestations have not lapsed.

------------------------------------------------------------------------

## 10. Information Security Incident Management (Annex A.5.24 – A.5.28)

### 10.1 Detection sources

- Health-check failures (Docker reports container as `unhealthy`).
- Audit-log anomalies (e.g. unexpected MCP token creations).
- Slack alerts on uncaught application errors.
- GitHub Actions CI failures on `main` (indicates regressions slipping
  through review).
- External reports (candidate / HR feedback).

### 10.2 Response procedure

1.  **Triage** — System Owner determines severity (info / minor / major
    / critical) within 1 hour of detection.
2.  **Contain** — for credential exposure, immediately revoke the
    affected MCP token / admin session via `/admin/settings`. For active
    exploit, take container offline (`docker compose down`) — public
    traffic 503's.
3.  **Eradicate** — apply the fix on a feature branch, run CI, deploy.
4.  **Recover** — restore from the most recent clean backup if data
    integrity was compromised.
5.  **Document** — incident note in the operations log (audit log entry
    plus Slack post-mortem thread).

### 10.3 Notification

If candidate or employee personal data is confirmed exposed, the data
controller (HR) is notified within 24 hours of confirmation. Onward
notification of data subjects and any supervisory authority is the data
controller's decision and is governed by applicable national PII law.

------------------------------------------------------------------------

## 11. Business Continuity (Annex A.5.29 – A.5.30)

### 11.1 Recovery objectives

| Objective | Target | Current capability |
|----|----|----|
| Recovery Point Objective (RPO) | ≤ 24 hours of data loss | Met by nightly backup at 03:00 UTC |
| Recovery Time Objective (RTO) | ≤ 4 hours | Met — full rebuild from latest backup completes in \<30 minutes given a fresh VPS |

**Known gap:** all backups currently reside on the same VPS as the live
data. A loss of the VPS itself (catastrophic provider failure,
ransomware on the host) would lose both. This is the auditor's most
likely finding-to-close. **Remediation plan:** add weekly off-site
backup transfer (e.g. to an S3-compatible object store or to the System
Owner's controlled storage) before the next audit cycle.

### 11.2 Disaster scenarios covered

- **Container crash** → Docker `restart: unless-stopped` policy +
  healthcheck → automatic restart.
- **Bad deploy** → previous Docker image is preserved on the VPS;
  rollback by re-tagging and `docker compose up -d`.
- **Database corruption** → restore latest nightly backup, lose at most
  24 hours of data.
- **VPS loss** → rebuild on new VPS from GitHub source + most recent
  off-site backup. (Pending the gap above.)

------------------------------------------------------------------------

## 12. Compliance & Personal Data (Annex A.5.34 – A.5.36)

- The data controller (Janus Digital HR) is responsible for the lawful
  basis under which candidate and employee data is processed.
- The platform supports the data controller's obligations by:
  - Providing complete logs of who accessed what (§ 7.1).
  - Allowing per-record deletion via the admin UI (right to erasure).
  - Allowing data export per assessment in JSON or CSV (right to
    portability).
  - Enforcing role-based access so processing is on a need-to-know
    basis.
- The platform itself does **not** transfer data to third countries
  unless the data controller configures a webhook to an external
  recipient. Such transfers are the controller's responsibility.

------------------------------------------------------------------------

## 13. Statement of Applicability — quick reference

The complete SoA is maintained as a separate document. Below is the
summary of which Annex A 2022 controls apply to Assessify:

| Theme | Applicable | Notes |
|----|----|----|
| 5\. Organisational | A.5.1, .8, .9, .10, .15–.18, .19–.23, .24–.28, .29–.30, .34, .37 | Core ISMS scope |
| 6\. People | A.6.3 (training) | System Owner trained on Next.js, Prisma, Docker; HR admins onboarded with first-login walkthrough |
| 7\. Physical | A.7.5–.7.7 | Inherited from Hostinger; no Janus Digital physical estate in scope |
| 8\. Technological | A.8.2–.8, .12–.16, .20–.24, .25–.28, .32 | Most controls land here — see § 5–8 above |

------------------------------------------------------------------------

## 14. Evidence Pointers

For each control the auditor will request evidence. The evidence below
is reproducible from a logged-in admin session or by the System Owner on
request:

| Control | Evidence | How to obtain |
|----|----|----|
| Authentication enforced on admin endpoints | HTTP 401 from `curl https://assessify.janusd.io/api/admin/assessments` (no cookie) | Live demonstration |
| Audit log captures admin actions | `AuditLog` table query for any 24-hour window | Admin session → SQL view (read-only) |
| Backups are recent | `ls -la /opt/stacks/assessify/backups/` shows ≥ 28 nightly snapshots | SSH session demonstration |
| TLS in force | SSL Labs scan of `assessify.janusd.io`, A grade | Public scan |
| CI runs on every change | GitHub Actions tab on the repository, last 30 builds | GitHub UI |
| Vulnerability review | `npm audit` output and corresponding commit messages | Commit `8994491` and forward |
| Schema migrations are version-controlled and idempotent | Dockerfile entrypoint script, git history | `git log -- Dockerfile` |
| Incident response was tested | Latest dry-run of restore-from-backup | Run scheduled by System Owner |

------------------------------------------------------------------------

## 15. Open Items & Roadmap

These are the gaps the auditor is most likely to flag. They are tracked
and accepted by the System Owner.

| Item | Severity | Target close |
|----|----|----|
| No off-site backup | High | +30 days from audit |
| Per-data-category retention policy not yet documented in HR's data-protection policy | Medium | +60 days |
| CSP / X-Frame-Options not yet set at the application layer (relying on Caddy defaults) | Low | +60 days |
| Annual access-review process not yet scheduled | Low | Add to maintenance calendar at next quarterly review |

------------------------------------------------------------------------

## Appendix A — Where the technical detail lives

Auditors who want to drill in past the control narrative can look at:

- `README.md` — system overview and architecture summary.
- `SOP.md` — full operations manual (deployment, runbook,
  troubleshooting, maintenance).
- `prisma/schema.prisma` — complete data model.
- `src/lib/audit.ts` and `src/lib/mcp/tools.ts` — audit-logging
  implementation.
- `.github/workflows/test.yml` — CI definition.
- `Dockerfile` — production container image and entrypoint migrations.

------------------------------------------------------------------------

*End of audit package.*
