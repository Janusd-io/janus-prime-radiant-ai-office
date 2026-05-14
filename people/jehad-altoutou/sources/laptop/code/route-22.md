---
type: source
source_type: laptop
title: route
slug: route-22
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: "/Users/jehad/assessify/src/app/api/admin/assessments/[id]/sections/route.ts"
original_size: 1901
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# route

_Extracted from `assessify/src/app/api/admin/assessments/[id]/sections/route.ts` on 2026-05-14._

```typescript
import { NextRequest, NextResponse } from "next/server";
import { prisma } from "@/lib/db";
import { getSession } from "@/lib/auth";

// POST: Create new section in the latest version
export async function POST(
  req: NextRequest,
  ctx: { params: Promise<{ id: string }> }
) {
  const session = await getSession();
  if (!session) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });

  try {
    const { id } = await ctx.params;
    const { title, slug, description, introText, iconName, weight } = await req.json();

    if (!title) {
      return Response.json({ error: "title is required" }, { status: 400 });
    }

    const latestVersion = await prisma.assessmentVersion.findFirst({
      where: { templateId: id },
      orderBy: { versionNumber: "desc" },
    });
    if (!latestVersion) {
      return Response.json({ error: "No version found for this template" }, { status: 404 });
    }

    if (latestVersion.status === "published") {
      return Response.json({ error: "Cannot modify published version. Unpublish first." }, { status: 400 });
    }

    const existingCount = await prisma.section.count({ where: { versionId: latestVersion.id } });
    const finalSlug = slug?.trim() || title.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/(^-|-$)/g, "");

    const section = await prisma.section.create({
      data: {
        versionId: latestVersion.id,
        title,
        slug: finalSlug,
        description: description ?? null,
        introText: introText ?? null,
        iconName: iconName ?? null,
        sortOrder: existingCount + 1,
        weight: weight ?? 0.33,
        isActive: true,
      },
    });

    return Response.json({ section }, { status: 201 });
  } catch (error) {
    console.error("POST /api/admin/assessments/[id]/sections error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

```