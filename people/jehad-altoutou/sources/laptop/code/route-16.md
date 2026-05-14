---
type: source
source_type: laptop
title: route
slug: route-16
created: 2026-05-12
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/api/google/oauth/callback/route.ts
original_size: 3896
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# route

_Extracted from `assessify/src/app/api/google/oauth/callback/route.ts` on 2026-05-14._

```typescript
/**
 * Phase 1.D OAuth bootstrap (callback).
 *
 * Google redirects here with ?code=... — we exchange it for an access token
 * + refresh_token. The refresh_token is persisted into GoogleToken keyed by
 * the resolved email (from the access token's userinfo endpoint). Subsequent
 * Calendar calls in lib/google-calendar.ts mint short-lived access tokens
 * from this refresh_token.
 */
import { NextRequest, NextResponse } from "next/server";
import { prisma } from "@/lib/db";
import { getSession } from "@/lib/auth";

const SCOPES = [
  "https://www.googleapis.com/auth/calendar.events",
  "https://www.googleapis.com/auth/calendar.freebusy",
];

export async function GET(req: NextRequest) {
  const user = await getSession();
  if (!user) {
    return NextResponse.json({ error: "admin login required" }, { status: 401 });
  }

  const url = new URL(req.url);
  const code = url.searchParams.get("code");
  const errorParam = url.searchParams.get("error");
  if (errorParam) {
    return new Response(`OAuth error: ${errorParam}`, { status: 400 });
  }
  if (!code) {
    return new Response("Missing ?code", { status: 400 });
  }

  const clientId = process.env.GOOGLE_OAUTH_CLIENT_ID;
  const clientSecret = process.env.GOOGLE_OAUTH_CLIENT_SECRET;
  const redirectUri = process.env.GOOGLE_OAUTH_REDIRECT_URI;
  if (!clientId || !clientSecret || !redirectUri) {
    return new Response(
      "GOOGLE_OAUTH_CLIENT_ID / SECRET / REDIRECT_URI not configured.",
      { status: 500 },
    );
  }

  // Exchange code → tokens.
  const tokenRes = await fetch("https://oauth2.googleapis.com/token", {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({
      code,
      client_id: clientId,
      client_secret: clientSecret,
      redirect_uri: redirectUri,
      grant_type: "authorization_code",
    }),
  });
  if (!tokenRes.ok) {
    const body = await tokenRes.text();
    return new Response(`Token exchange failed: ${tokenRes.status} ${body}`, {
      status: 502,
    });
  }
  const tokens = (await tokenRes.json()) as {
    access_token: string;
    refresh_token?: string;
    expires_in: number;
    scope: string;
  };

  if (!tokens.refresh_token) {
    return new Response(
      "No refresh_token returned. This usually means the account previously " +
        "granted access — revoke at https://myaccount.google.com/permissions and retry.",
      { status: 400 },
    );
  }

  // Identify which Google account just granted access.
  const userinfoRes = await fetch("https://openidconnect.googleapis.com/v1/userinfo", {
    headers: { Authorization: `Bearer ${tokens.access_token}` },
  });
  if (!userinfoRes.ok) {
    const body = await userinfoRes.text();
    return new Response(`Userinfo failed: ${userinfoRes.status} ${body}`, {
      status: 502,
    });
  }
  const userinfo = (await userinfoRes.json()) as { email?: string };
  const email = userinfo.email;
  if (!email) {
    return new Response("Userinfo did not include an email.", { status: 502 });
  }

  const expected = process.env.INTERVIEW_MAILBOX_EMAIL;
  if (expected && email.toLowerCase() !== expected.toLowerCase()) {
    return new Response(
      `Signed in as ${email}, expected ${expected}. Sign out of Google, sign in as ${expected}, and retry /api/google/oauth/start.`,
      { status: 400 },
    );
  }

  const now = new Date();
  await prisma.googleToken.upsert({
    where: { email },
    create: {
      email,
      refreshToken: tokens.refresh_token,
      scopes: SCOPES.join(","),
      lastRefreshAt: now,
    },
    update: {
      refreshToken: tokens.refresh_token,
      scopes: SCOPES.join(","),
      lastRefreshAt: now,
    },
  });

  return new Response(
    `Google refresh token captured for ${email}. You can close this tab.`,
    { status: 200, headers: { "content-type": "text/plain" } },
  );
}

```