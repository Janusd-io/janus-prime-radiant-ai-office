---
type: project
title: Brightbean Studio
slug: brightbean-studio
created: 2026-05-14
updated: 2026-06-09
departments: [ai-office]
status: active
owner: jehad-altoutou
captured_by: jehad-altoutou
audience: [personal]
sources: [connection-page, connection-success, connection-expired, notification, digest, drawer, history, history-list, preferences, platform-icon-2, post-row, post-list, comment-list, comment-form, queue, org-queue, version-diff, version-diff-2, signup, logout]
related: [jehad-altoutou]
path: /Users/jehad/brightbean-studio
repo: https://github.com/brightbeanxyz/brightbean-studio
migrated_from: personal-obsidian-vault
---

# BrightBean Studio

**One-line description**: Open-source, self-hostable social media management platform for creators, agencies, and SMBs — schedule, publish, approve, and monitor content across 12+ platforms.

**Status**: 🟢 Active

---

## Stack
- **Framework**: Django 5.1 / Python 3.12
- **Frontend**: Django templates + Alpine.js 3 + HTMX 1.9 + Tailwind CSS 3
- **Database**: PostgreSQL (production) / SQLite (local dev)
- **Background tasks**: django-background-tasks (`python manage.py process_tasks`)
- **Storage**: S3Boto3 (production) / FileSystemStorage (local)
- **Auth**: django-allauth (Google/GitHub SSO + email/password), custom 2FA (TOTP)
- **Encryption**: AES-256-GCM via `apps/common/encryption.py` for credentials & tokens
- **HTTP Client**: httpx (async, for provider API calls)
- **Image Processing**: Pillow (thumbnails, platform variants)
- **Monitoring**: Sentry SDK
- **Skills used**: [[debug|/debug]], [[code-review|/code-review]]

---

## Architecture Overview

Multi-tenant SaaS: **Organization → Workspaces → Members** with granular RBAC.

Content pipeline: **Composer → Calendar/Queue → Approval → Publisher → Inbox**

Provider system: Abstract `SocialProvider` base class in `providers/base.py`, 11 platform implementations. Each provider implements OAuth, publish, inbox, and metrics interfaces.

---

## Django Apps (17 apps)

| App | Purpose |
|-----|---------|
| `accounts` | User auth, 2FA, OAuth, sessions, ToS acceptance |
| `organizations` | Multi-tenant org management, soft-deletion with grace period |
| `workspaces` | Workspace container per org, approval workflow settings, branding |
| `members` | RBAC: org/workspace memberships, custom roles, permissions, invitations |
| `credentials` | Platform API credentials per org (encrypted), setup UI |
| `social_accounts` | User-connected social accounts per workspace, OAuth tokens, health checks |
| `composer` | Post editor, content categories, tags, templates, Kanban idea board, CSV import |
| `calendar` | Visual scheduling, recurring posting slots, queues, custom events |
| `publisher` | Publishing engine, retry logic, rate limit tracking, publish audit logs |
| `inbox` | Unified social inbox (comments/DMs/mentions), sentiment, SLA config |
| `approvals` | Multi-stage approval workflows, threaded comments, reminders, audit trail |
| `media_library` | Org/workspace media, folders, platform-optimized variants, versioning |
| `notifications` | In-app/email/webhook notifications, per-user preferences, quiet hours |
| `client_portal` | Passwordless 30-day magic-link access for external client approval |
| `onboarding` | Connection links for bulk social account setup, checklists |
| `settings_manager` | Org/workspace-level key-value settings |
| `common` | Encryption utilities, OrgScoped/WorkspaceScoped managers, validators |

---

## Key Models (per app)

### accounts
- `User` — email (unique), name, avatar, totp_secret, totp_enabled, last_workspace_id
- `OAuthConnection` — user, provider (google/github), provider_user_id
- `Session` — user, token_hash, device_info, ip_address, expires_at

### organizations
- `Organization` — name, logo_url, default_timezone, deletion_requested_at

### workspaces
- `Workspace` — organization, name, timezone, approval_workflow_mode, default_hashtags, is_archived

### members
- `OrgMembership` — user, organization, org_role (owner/admin/member)
- `WorkspaceMembership` — user, workspace, workspace_role (owner/manager/editor/contributor/client/viewer), custom_role
- `CustomRole` — organization, name, permissions (JSONField)
- `Invitation` — organization, email, org_role, workspace_assignments (JSON), token, expires_at

### credentials
- `PlatformCredential` — organization, platform (12 choices), credentials (EncryptedJSONField), is_configured, test_result

### social_accounts
- `SocialAccount` — workspace, platform, account_platform_id, account_name, oauth_access_token (encrypted), oauth_refresh_token (encrypted), token_expires_at, connection_status
- `MastodonAppRegistration` — instance_url, client_id (encrypted), client_secret (encrypted)

### composer
- `Post` — workspace, author, title, caption, first_comment, internal_notes, tags (JSON), category, scheduled_at
- `PlatformPost` — post, social_account, status (draft→published/failed), platform_specific overrides, platform_post_id, retry_count
- `Idea` — workspace, author, title, description, tags (JSON), status, group, position
- `IdeaGroup` — workspace, name, position (Kanban columns)
- `Tag` — workspace, name (unique per workspace)
- `PostTemplate` — workspace, name, template_data (JSON) — UUID PKs
- `PostMedia` — post, media_asset, position, alt_text
- `PostVersion` — post, version_number, snapshot (JSON)
- `ContentCategory` — workspace, name, color
- `Feed` — workspace, name, url

### calendar
- `PostingSlot` — social_account, day_of_week, time, is_active
- `Queue` — workspace, name, category, social_account, is_active
- `QueueEntry` — queue, post, position, assigned_slot_datetime
- `RecurrenceRule` — post (one-to-one), frequency, interval, end_date
- `CustomCalendarEvent` — workspace, title, start_date, end_date, color

### publisher
- `PublishLog` — platform_post, attempt_number, status_code, response_body, error_message
- `RateLimitState` — social_account, platform, requests_remaining, window_resets_at

### inbox
- `InboxMessage` — workspace, social_account, message_type, sender_name, body, sentiment, status (unread/open/resolved/archived), assigned_to
- `InboxReply` — inbox_message, author, body, platform_reply_id
- `InternalNote` — inbox_message, author, body
- `SavedReply` — workspace, title, body (variable substitution)
- `InboxSLAConfig` — workspace (one-to-one), target_response_minutes, auto_resolve_on_reply

### approvals
- `ApprovalAction` — post, user, action (submitted/approved/changes_requested/rejected)
- `PostComment` — post, author, body, visibility (internal/external), parent_comment
- `ApprovalReminder` — post, stage, reminder_count, escalated

### media_library
- `MediaFolder` — organization, workspace, parent_folder, name (max 3 levels)
- `MediaAsset` — organization, workspace, folder, file, media_type, thumbnail, tags (JSON), processing_status
- `MediaAssetVersion` — media_asset, version_number, file, change_description

### notifications
- `Notification` — user, event_type (17 types), title, body, data (JSON), is_read
- `NotificationPreference` — user, event_type, channel (in_app/email/webhook), is_enabled
- `NotificationDelivery` — notification, channel, status (pending/delivered/failed), attempts
- `QuietHours` — user (one-to-one), start_time, end_time, timezone, digest_mode

### client_portal
- `MagicLinkToken` — user, workspace, token, expires_at (30 days)

---

## Provider System (`providers/`)

Abstract `SocialProvider` in `base.py`. Registry in `__init__.py` maps platform strings → classes.

| Provider | File | API |
|----------|------|-----|
| Facebook | `facebook.py` | Facebook Pages API |
| Instagram | `instagram.py` | Instagram Business Graph API |
| Instagram Personal | `instagram_personal.py` | Instagram Login API |
| LinkedIn Personal | `linkedin_personal.py` | LinkedIn v2 API |
| LinkedIn Company | `linkedin_company.py` | LinkedIn v2 API (inherits from personal) |
| TikTok | `tiktok.py` | TikTok Content Posting API |
| YouTube | `youtube.py` | YouTube Data API v3 |
| Pinterest | `pinterest.py` | Pinterest API |
| Threads | `threads.py` | Threads API (Meta) |
| Bluesky | `bluesky.py` | AT Protocol (session-based, no app credentials) |
| Google Business | `google_business.py` | Google My Business API |
| Mastodon | `mastodon.py` | Mastodon API (instance-specific) |

**Provider interface**: `get_auth_url()`, `exchange_code()`, `refresh_token()`, `publish_post()`, `delete_post()`, `fetch_comments()`, `reply_to_comment()`, `get_account_metrics()`, `health_check()`

**Credential flow**: App-level credentials in `PlatformCredential` (encrypted) → per-user tokens in `SocialAccount` (encrypted) → `get_provider(platform, credentials)` instantiates provider.

---

## Background Tasks

| Task | Schedule | Purpose |
|------|----------|---------|
| `run_publish_cycle()` | Every 15s | Publish due posts, handle retries |
| `generate_recurrences()` | Daily | Expand recurring posts 90 days ahead |
| `send_email_notifications()` | Hourly | Batch email delivery with quiet hours |
| `retry_failed_deliveries()` | Every 5min | Retry webhook/email failures |
| `fetch_inbox_messages()` | Every 5min | Poll platforms for new comments/DMs |
| `process_media_variants()` | On demand | Generate platform-optimized media |
| `send_approval_reminders()` | Hourly | Escalate stalled approvals |
| `health_check_accounts()` | Every 30min | Verify token validity, detect disconnections |

---

## Custom Middleware

| Middleware | Purpose |
|-----------|---------|
| `AuthRateLimitMiddleware` | Rate limit auth POST endpoints (10/min per IP) |
| `TosAcceptanceMiddleware` | Redirect to ToS page if not accepted |
| `RBACMiddleware` | Resolve `request.org`, `request.org_membership`, `request.workspace`, `request.workspace_membership` on every request |

---

## Frontend Architecture

- **Alpine.js 3** — Reactive UI: sidebar toggle (localStorage), modals, dropdowns, Kanban drag-and-drop
- **HTMX 1.9** — Partial page swaps: tab switching, infinite scroll, filter updates, autosave
- **Tailwind CSS 3** — Utility-first styling, compiled via `django-tailwind`
- **CSS Variables** — Design tokens: `--primary`, `--border`, `--text-primary`, `--surface-0`, etc.
- **Flatpickr** — Date picker (CDN)
- **Cropper.js** — Image cropping in media library

Static files: `/static/js/alpine.min.js`, `/static/js/htmx.min.js`
Tailwind source: `/theme/static_src/src/styles.css` → compiled to `/theme/static/css/dist/styles.css`
Dev watch: `cd theme/static_src && npm run start`

---

## Config/Settings

| File | Purpose |
|------|---------|
| `config/settings/base.py` | All core settings, INSTALLED_APPS, middleware, encryption, platform credentials |
| `config/settings/development.py` | DEBUG=True, ALLOWED_HOSTS=*, CSP report-only, console email |
| `config/settings/production.py` | DEBUG=False, CSRF_COOKIE_SECURE, Sentry, compressed static |
| `config/settings/test.py` | Test overrides, ALLOWED_HOSTS=*, SQLite |

Settings module selected by `DJANGO_SETTINGS_MODULE` (default: `config.settings.development` from `manage.py`).

---

## Local Dev Setup

```bash
# Python 3.12 required (brew install python@3.12)
python3.12 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cd theme/static_src && npm install && cd ../..

# .env: DATABASE_URL=sqlite:///db.sqlite3, STORAGE_BACKEND=local, MEDIA_ROOT=media
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver          # Tab 1
cd theme/static_src && npm run start # Tab 2 (Tailwind watch)
python manage.py process_tasks      # Tab 3 (background worker)
```

---

## Key Decisions
- *(2026-04-16)* Set up locally with SQLite instead of Docker/PostgreSQL for faster iteration
- *(2026-04-17)* Created `apps/utils.py` with `json_tag_contains()` for SQLite-compatible JSON tag filtering — avoids duplicating DB-engine checks at every call site
- *(2026-04-17)* Used `x-teleport="body"` with `position: fixed` + `getBoundingClientRect()` for custom dropdowns — tried `overflow: visible` chain first but it broke page scroll layout
- *(2026-04-17)* Built Platform Credentials UI as expandable inline forms rather than modals — better UX for multi-field input with help text
- *(2026-04-17)* Pushed PR from HappyLife2 GitHub account (personal), not Jehada-Janusd (work)

## Bugs Fixed
1. **Use Template ValidationError** — Built-in templates have integer IDs but compose view only queried UUID-based PostTemplate. Added fallback to `builtin_templates.py` + caption pre-fill from template body.
2. **Inbox tab active state** — HTMX swaps only message list, not tab bar. Added Alpine.js client-side toggling.
3. **Tag filtering crash on SQLite** — `tags__contains` uses PostgreSQL JSON `@>` operator. Created `apps/utils.py:json_tag_contains()` with `__icontains` fallback. Updated 6 call sites.
4. **File upload crash** — Missing `STORAGES["default"]` for local dev. Added `FileSystemStorage` in `config/settings/base.py`.
5. **MEDIA_ROOT=/app/media** — Docker path in `.env`, invalid on macOS. Changed to `media`.
6. **Stale last_workspace_id** — User redirect to deleted workspace causing 403. Fixed in DB.

## Features Added
1. **Profile vs Preferences separation** — `templates/accounts/settings.html` conditionally renders. Preferences shows notification matrix (17 event types × 3 channels).
2. **Platform Credentials UI** — `apps/credentials/views.py` CRUD + `templates/credentials/list.html`. Guided setup per platform with help text and developer console links.
3. **Upgraded dropdown menus** — Custom Alpine.js dropdowns with teleport, search, transitions across calendar, inbox, and org settings.

## Progress Log
- *(2026-04-16)* Cloned repo, installed Python 3.12, set up local dev with SQLite
- *(2026-04-17)* Fixed 6 bugs, built 3 features, submitted PR #24 from HappyLife2 account
- *(2026-04-17)* PR status: MERGEABLE, no conflicts with upstream (7 commits behind)

---

## Knowledge Graph

Full Graphify analysis: **2336 nodes, 8779 edges, 112 communities**. Graph data in `03 Projects/BrightBean Studio/graph.json`.

### Key Communities
- [[_COMMUNITY_Community 0|Providers (LinkedIn, YouTube, Social)]] — 318 nodes
- [[_COMMUNITY_Community 1|Org Settings & Calendar Views]] — 309 nodes
- [[_COMMUNITY_Community 2|Approval Workflows & Tests]] — 161 nodes
- [[_COMMUNITY_Community 3|Holidays & Calendar Overlay]] — 154 nodes
- [[_COMMUNITY_Community 4|Notifications & Publishing Tasks]] — 152 nodes
- [[_COMMUNITY_Community 5|Alpine.js Frontend]] — 143 nodes
- [[_COMMUNITY_Community 6|LinkedIn & YouTube Providers]] — 118 nodes
- [[_COMMUNITY_Community 7|Validators & Security]] — 116 nodes
- [[_COMMUNITY_Community 9|Organization Models & Admin]] — 104 nodes
- [[_COMMUNITY_Community 10|Social Account Health Checks]] — 100 nodes
- [[_COMMUNITY_Community 12|Inbox Sync Engine]] — 63 nodes
- [[_COMMUNITY_Community 14|Client Portal Views]] — 32 nodes
- [[_COMMUNITY_Community 17|Queue & Slot Services]] — 20 nodes
- [[_COMMUNITY_Community 20|Social Account OAuth Views]] — 15 nodes
- [[_COMMUNITY_Community 22|Custom Middleware]] — 10 nodes
- [[_COMMUNITY_Community 23|Built-in Templates]] — 6 nodes

## Related
- [[jehad-altoutou]]
- [[index|Home]]

## Code graph
Full node index: [[brightbean-studio-graph-index|brightbean-studio code graph index]] (all graphify nodes). Clustered views in the `_COMMUNITY_*` notes; visual map in `graph.canvas`.
