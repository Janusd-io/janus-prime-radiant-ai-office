---
type: project
title: Assessify — HR Assessment Platform
slug: assessify-hr-assessment-platform
created: 2026-04-13
updated: 2026-05-13
departments: [ai-office, hr]
status: active
owner: jehad-altoutou
sources: [pr-backup-2026-05-11-project-assessify-hr-assessment-platform]
related: [assessify, hr-recruitment-pipeline, recruitment-automation-pipeline, theresa-wong, mariam-mahmood, hostinger, n8n]
audience: [department]
captured_by: jehad-altoutou
---

# Assessify — HR Assessment Platform

Production-grade hiring assessment platform with scoring engine, analytics, HR onboarding forms, and n8n automation. Backs the [[recruitment-automation-pipeline]] for the HR department; primary engineering owner is [[jehad-altoutou]]; HR stakeholders are [[theresa-wong]] and [[mariam-mahmood]].

The Assessify SaaS itself is tracked as a vendor entity at [[assessify]] — this page is the **project hub** for the Janus-side implementation work (the repo Jehad maintains, the n8n workflows that integrate it with HR processes, the deployment story).

## Stack (snapshot)

- Next.js 16 (App Router, Turbopack, async params)
- Prisma v7 + SQLite (via `@prisma/adapter-libsql`)
- Tailwind v4 + shadcn/ui (on `@base-ui/react`, not Radix) + Framer Motion
- Resend (email — free tier limited to owner email)
- Docker (`docker-compose.yml`), named volume `/app/data`
- Hosted via [[hostinger]] + n8n at `https://n8n.srv1086109.hstgr.cloud`

## Goal

Replace boring hiring assessments with a premium, data-rich, automation-ready product. Serves candidates (immersive UX) and internal teams (scoring, analytics, webhooks, n8n integration).

## Key decisions

- **2026-04-10** — Library templates (`library-{deptSlug}`, `isActive=false`) hold standalone bank questions, hidden from candidate picker.
- **2026-04-13** — Question Bank section grouping: Cultural Fit / AI Awareness / Department-Specific / General.
- **2026-04-13** — Versioning concept removed from UI (assessments edit in place; `versionNumber` still in schema for session integrity but invisible).
- **2026-04-10** — HR forms send files as base64 in webhook payload (not server storage) so n8n can attach directly.
- **standing** — Never wipe Docker volume (`docker compose down -v`) unless schema changed.

## n8n automation workflows

Hosted at `n8n.srv1086109.hstgr.cloud`. Webhook endpoint: `/webhook/2f1599d5-732f-4ab2-bde1-c879f2265451`.

**HR Document Processor (main):** Webhook → Switch on `formType` → Bank Details / Personal Data branch → GDrive folder check + create → file upload → HTML doc → GDoc conversion → Slack notification.

**Error Handler:** Error Trigger → Google Sheets log + Slack DM. Each monitored workflow must set this as its Error Workflow.

## Open

- Custom domain + HTTPS setup (waiting on IT).
- Build assessments for Operations, HR, Finance departments (content work).
- Cron for `scripts/backup.sh` on production host.
- Verify Resend with custom domain for external candidate delivery.

## Related

- [[recruitment-automation-pipeline]] — the parent department-level pipeline.
- [[assessify]] — the SaaS vendor entity.
- [[hostinger]] — hosting provider.
