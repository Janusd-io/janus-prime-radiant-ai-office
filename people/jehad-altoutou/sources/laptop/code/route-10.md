---
type: source
source_type: laptop
title: Assessify — route
slug: route-10
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/api/oauth/register/route.ts
original_size: 1702
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# route

_Extracted from `[[assessify|assessify]]/src/app/api/oauth/register/route.ts` on 2026-05-14._

```typescript
import { NextRequest, NextResponse } from "next/server";
import { registerClient } from "@/lib/mcp/oauth";

export const dynamic = "force-dynamic";

/**
 * RFC 7591 Dynamic Client Registration.
 * Claude Desktop POSTs here with { client_name, redirect_uris, ... }
 */
export async function POST(req: NextRequest) {
  try {
    const body = await req.json();
    const clientName =
      (body?.client_name as string | undefined)?.trim() || "MCP Client";
    const redirectUris = (body?.redirect_uris as string[] | undefined) ?? [];

    if (!Array.isArray(redirectUris) || redirectUris.length === 0) {
      return NextResponse.json(
        { error: "invalid_redirect_uri", error_description: "redirect_uris required" },
        { status: 400 }
      );
    }
    for (const u of redirectUris) {
      try {
        new URL(u);
      } catch {
        return NextResponse.json(
          { error: "invalid_redirect_uri", error_description: `bad URI: ${u}` },
          { status: 400 }
        );
      }
    }

    const client = await registerClient({ clientName, redirectUris });

    // Per spec, return a full registration response
    return NextResponse.json(
      {
        client_id: client.clientId,
        client_name: client.clientName,
        redirect_uris: client.redirectUris,
        grant_types: ["authorization_code", "refresh_token"],
        response_types: ["code"],
        token_endpoint_auth_method: "none", // public client with PKCE
      },
      { status: 201 }
    );
  } catch (err) {
    console.error("[oauth/register]", err);
    return NextResponse.json(
      { error: "server_error", error_description: "registration failed" },
      { status: 500 }
    );
  }
}

```