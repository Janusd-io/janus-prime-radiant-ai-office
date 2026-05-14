---
type: source
source_type: laptop
title: route
slug: route-11
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/api/oauth/authorize/consent/route.ts
original_size: 3010
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# route

_Extracted from `[[assessify|assessify]]/src/app/api/oauth/authorize/consent/route.ts` on 2026-05-14._

```typescript
import { NextRequest, NextResponse } from "next/server";
import { prisma } from "@/lib/db";
import { getSession } from "@/lib/auth";
import { mintAuthCode } from "@/lib/mcp/oauth";
import { auditLog } from "@/lib/audit";
import { getClientIp } from "@/lib/rate-limit";

export const dynamic = "force-dynamic";

/**
 * Called by the consent page when the admin approves (or denies) access.
 * Returns the URL the browser should navigate to (either the client's redirect_uri with code,
 * or the same URI with error=access_denied).
 */
export async function POST(req: NextRequest) {
  const session = await getSession();
  if (!session) return NextResponse.json({ error: "Not signed in" }, { status: 401 });

  const body = await req.json();
  const decision = body?.decision as "approve" | "deny";
  const clientId = body?.clientId as string;
  const redirectUri = body?.redirectUri as string;
  const codeChallenge = body?.codeChallenge as string;
  const codeChallengeMethod = body?.codeChallengeMethod as string;
  const state = (body?.state as string) || "";
  const scope = (body?.scope as string) || "read,write";

  if (!clientId || !redirectUri || !decision) {
    return NextResponse.json({ error: "invalid_request" }, { status: 400 });
  }

  const client = await prisma.oAuthClient.findUnique({ where: { clientId } });
  if (!client) return NextResponse.json({ error: "unknown client" }, { status: 400 });

  const allowed: string[] = JSON.parse(client.redirectUris);
  if (!allowed.includes(redirectUri)) {
    return NextResponse.json({ error: "redirect_uri not registered" }, { status: 400 });
  }

  const target = new URL(redirectUri);
  if (state) target.searchParams.set("state", state);

  if (decision === "deny") {
    target.searchParams.set("error", "access_denied");
    target.searchParams.set("error_description", "User denied access");
    await auditLog({
      userId: session.id,
      userEmail: session.email,
      action: "mcp_oauth.denied",
      targetType: "OAuthClient",
      targetId: clientId,
      details: { clientName: client.clientName },
      ipAddress: getClientIp(req) ?? undefined,
    });
    return NextResponse.json({ redirect: target.toString() });
  }

  // Approve → mint code
  if (codeChallengeMethod !== "S256" || !codeChallenge) {
    return NextResponse.json({ error: "PKCE S256 required" }, { status: 400 });
  }

  const code = await mintAuthCode({
    clientId,
    userId: session.id,
    redirectUri,
    codeChallenge,
    codeChallengeMethod,
    scope,
    createdIp: getClientIp(req) ?? null,
    createdUserAgent: req.headers.get("user-agent") ?? null,
  });

  target.searchParams.set("code", code);

  await auditLog({
    userId: session.id,
    userEmail: session.email,
    action: "mcp_oauth.authorized",
    targetType: "OAuthClient",
    targetId: clientId,
    details: { clientName: client.clientName, scope },
    ipAddress: getClientIp(req) ?? undefined,
  });

  return NextResponse.json({ redirect: target.toString() });
}

```