---
type: source
source_type: laptop
title: route
slug: route-55
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/api/admin/webhooks/route.ts
original_size: 2631
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# route

_Extracted from `assessify/src/app/api/admin/webhooks/route.ts` on 2026-05-14._

```typescript
import { NextRequest, NextResponse } from "next/server";
import { prisma } from "@/lib/db";
import { nanoid } from "nanoid";
import { getSession } from "@/lib/auth";

export async function GET() {
  const session = await getSession();
  if (!session) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });

  try {
    const endpoints = await prisma.webhookEndpoint.findMany({
      orderBy: { createdAt: "desc" },
      include: { _count: { select: { deliveries: true } } },
    });
    return Response.json({ endpoints });
  } catch (error) {
    console.error("GET /api/admin/webhooks error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

export async function POST(req: NextRequest) {
  const session = await getSession();
  if (!session) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });

  try {
    const { url, events } = await req.json() as {
      url: string;
      events: string[];
    };

    if (!url?.trim()) {
      return Response.json({ error: "URL is required" }, { status: 400 });
    }

    if (!events || events.length === 0) {
      return Response.json({ error: "At least one event is required" }, { status: 400 });
    }

    // Generate a signing secret
    const secret = `whsec_${nanoid(32)}`;

    const endpoint = await prisma.webhookEndpoint.create({
      data: {
        url: url.trim(),
        secret,
        events: JSON.stringify(events),
        isActive: true,
      },
    });

    return Response.json({
      endpoint: {
        id: endpoint.id,
        url: endpoint.url,
        secret: endpoint.secret,
        events: JSON.parse(endpoint.events),
        isActive: endpoint.isActive,
      },
    }, { status: 201 });
  } catch (error) {
    console.error("POST /api/admin/webhooks error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

export async function DELETE(req: NextRequest) {
  const session = await getSession();
  if (!session) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });

  try {
    const id = new URL(req.url).searchParams.get("id");
    if (!id) return Response.json({ error: "id is required" }, { status: 400 });

    // Delete deliveries first, then the endpoint
    await prisma.webhookDelivery.deleteMany({ where: { endpointId: id } });
    await prisma.webhookEndpoint.delete({ where: { id } });
    return Response.json({ ok: true });
  } catch (error) {
    console.error("DELETE /api/admin/webhooks error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

```