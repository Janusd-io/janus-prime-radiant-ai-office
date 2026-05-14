---
type: source
source_type: laptop
title: route
slug: route-47
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/api/admin/competencies/route.ts
original_size: 1709
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# route

_Extracted from `assessify/src/app/api/admin/competencies/route.ts` on 2026-05-14._

```typescript
import { NextRequest, NextResponse } from "next/server";
import { prisma } from "@/lib/db";
import { getSession } from "@/lib/auth";

export async function GET() {
  const session = await getSession();
  if (!session) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });

  try {
    const competencies = await prisma.competency.findMany({
      orderBy: { name: "asc" },
    });
    return Response.json({ competencies });
  } catch (error) {
    console.error("GET /api/admin/competencies error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

export async function POST(req: NextRequest) {
  const session = await getSession();
  if (!session) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });

  try {
    const { name, slug, description, category } = await req.json();

    if (!name) return Response.json({ error: "name is required" }, { status: 400 });

    const finalSlug = slug?.trim() || name.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/(^-|-$)/g, "");

    const existing = await prisma.competency.findUnique({ where: { slug: finalSlug } });
    if (existing) {
      return Response.json({ error: "A competency with this slug already exists" }, { status: 409 });
    }

    const competency = await prisma.competency.create({
      data: {
        name,
        slug: finalSlug,
        description: description ?? null,
        category: category ?? null,
      },
    });

    return Response.json({ competency }, { status: 201 });
  } catch (error) {
    console.error("POST /api/admin/competencies error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

```