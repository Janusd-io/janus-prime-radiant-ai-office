---
type: integration
tags:
  - email
  - resend
---

# Resend Email

Email delivery via Resend (`src/lib/email.ts`).

## Templates
- **Assessment Invite** — `sendAssessmentInviteEmail()` — candidate assessment invitation
- **Onboarding Form** — `sendOnboardingFormEmail()` — HR form invitation (welcome aboard theme)
- **Admin Invite** — `sendAdminInviteEmail()` — platform user invitation with role

## Configuration
- **API Key:** `RESEND_API_KEY` in `.env`
- **From:** `RESEND_FROM_EMAIL` — defaults to `Assessify <onboarding@resend.dev>`
- **Free tier limitation:** `onboarding@resend.dev` only delivers to the Resend account owner's verified email. Custom domain needed for external recipients.

## Known Issues (Resolved)
- *(2026-04-16)* `.env` had `RESEND_API_KEY` concatenated with `SESSION_SECRET` on same line (missing newline separator). Resend rejected the key as invalid. Invites were still created in DB but email silently failed. Fixed by splitting the line + deploying new key.
- *(2026-04-16)* `docker compose restart` does NOT reload `env_file` — must use `docker compose up -d --force-recreate` to pick up `.env` changes.

## Related
- [[_COMMUNITY_Email Sending|Email Sending community]]
- [[assessify|Assessify]]
- [[references|References]]
