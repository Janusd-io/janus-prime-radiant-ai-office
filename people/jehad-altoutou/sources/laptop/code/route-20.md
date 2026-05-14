---
type: source
source_type: laptop
title: route
slug: route-20
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/api/admin/assessments/route.ts
original_size: 2618
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# route

_Extracted from `assessify/src/app/api/admin/assessments/route.ts` on 2026-05-14._

```typescript
import { NextRequest, NextResponse } from "next/server";
import { prisma } from "@/lib/db";
import { getSession } from "@/lib/auth";

export async function GET() {
  const session = await getSession();
  if (!session) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });

  try {
    const templates = await prisma.assessmentTemplate.findMany({
      include: {
        jobRole: { include: { department: true } },
        versions: {
          include: {
            sections: {
              include: { _count: { select: { questions: true } } },
              orderBy: { sortOrder: "asc" },
            },
            _count: { select: { candidateSessions: true } },
          },
          orderBy: { versionNumber: "desc" },
        },
      },
      orderBy: { createdAt: "desc" },
    });

    return Response.json({ templates });
  } catch (error) {
    console.error("GET /api/admin/assessments error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

export async function POST(req: NextRequest) {
  const session = await getSession();
  if (!session) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });

  try {
    const { title, slug, description, jobRoleId, passingScore, timeLimit } = await req.json() as {
      title: string;
      slug?: string;
      description?: string;
      jobRoleId: string;
      passingScore?: number;
      timeLimit?: number | null;
    };

    if (!title || !jobRoleId) {
      return Response.json({ error: "title and jobRoleId are required" }, { status: 400 });
    }

    const finalSlug = slug?.trim() || title.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/(^-|-$)/g, "");

    const existing = await prisma.assessmentTemplate.findUnique({ where: { slug: finalSlug } });
    if (existing) {
      return Response.json({ error: "An assessment with this slug already exists" }, { status: 409 });
    }

    const template = await prisma.assessmentTemplate.create({
      data: {
        title,
        slug: finalSlug,
        description: description ?? null,
        jobRoleId,
        versions: {
          create: {
            versionNumber: 1,
            status: "draft",
            passingScore: passingScore ?? 0.6,
            timeLimit: timeLimit ?? null,
          },
        },
      },
      include: {
        versions: true,
      },
    });

    return Response.json({ template }, { status: 201 });
  } catch (error) {
    console.error("POST /api/admin/assessments error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

```