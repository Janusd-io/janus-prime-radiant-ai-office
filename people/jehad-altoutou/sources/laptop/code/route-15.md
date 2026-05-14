---
type: source
source_type: laptop
title: route
slug: route-15
created: 2026-05-12
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/api/google/oauth/start/route.ts
original_size: 1916
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# route

_Extracted from `assessify/src/app/api/google/oauth/start/route.ts` on 2026-05-14._

```typescript
/**
 * Phase 1.D OAuth bootstrap (start).
 *
 * Hit this route logged in as an admin and signed into Google as the
 * INTERVIEW_MAILBOX_EMAIL account in the SAME browser. Redirects to Google's
 * consent screen with offline access so we get a refresh token. The callback
 * route persists the refresh_token into GoogleToken.
 *
 * Required env:
 *   - GOOGLE_OAUTH_CLIENT_ID
 *   - GOOGLE_OAUTH_CLIENT_SECRET
 *   - GOOGLE_OAUTH_REDIRECT_URI  (e.g. https://assessify.janusd.io/api/google/oauth/callback)
 *   - INTERVIEW_MAILBOX_EMAIL    (optional; used as login_hint)
 */
import { NextResponse } from "next/server";
import { getSession } from "@/lib/auth";

const SCOPES = [
  "https://www.googleapis.com/auth/calendar.events",
  "https://www.googleapis.com/auth/calendar.freebusy",
].join(" ");

export async function GET() {
  const user = await getSession();
  if (!user) {
    return NextResponse.json({ error: "admin login required" }, { status: 401 });
  }

  const clientId = process.env.GOOGLE_OAUTH_CLIENT_ID;
  const redirectUri = process.env.GOOGLE_OAUTH_REDIRECT_URI;
  if (!clientId || !redirectUri) {
    return NextResponse.json(
      {
        error:
          "GOOGLE_OAUTH_CLIENT_ID / GOOGLE_OAUTH_REDIRECT_URI not set. Complete provisioning first.",
      },
      { status: 500 },
    );
  }

  const url = new URL("https://accounts.google.com/o/oauth2/v2/auth");
  url.searchParams.set("client_id", clientId);
  url.searchParams.set("redirect_uri", redirectUri);
  url.searchParams.set("response_type", "code");
  url.searchParams.set("scope", SCOPES);
  url.searchParams.set("access_type", "offline");
  url.searchParams.set("prompt", "consent"); // force refresh_token return
  url.searchParams.set("include_granted_scopes", "true");
  const hint = process.env.INTERVIEW_MAILBOX_EMAIL;
  if (hint) url.searchParams.set("login_hint", hint);

  return NextResponse.redirect(url.toString());
}

```