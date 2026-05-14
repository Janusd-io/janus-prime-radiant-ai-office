---
type: source
source_type: laptop
title: route
slug: route-53
created: 2026-05-12
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/api/admin/job-roles/route.ts
original_size: 2732
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# route

_Extracted from `[[assessify|assessify]]/src/app/api/admin/job-roles/route.ts` on 2026-05-14._

```typescript
import { NextRequest, NextResponse } from "next/server";
import { prisma } from "@/lib/db";
import { getSession } from "@/lib/auth";

export async function GET() {
  const session = await getSession();
  if (!session) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });

  try {
    const jobRoles = await prisma.jobRole.findMany({
      where: { isActive: true },
      include: { department: true },
      orderBy: [{ department: { name: "asc" } }, { title: "asc" }],
    });
    return Response.json({ jobRoles });
  } catch (error) {
    console.error("GET /api/admin/job-roles error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

export async function POST(req: NextRequest) {
  const session = await getSession();
  if (!session) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });

  try {
    const body = await req.json() as {
      title: string;
      slug?: string;
      description?: string;
      departmentId: string;
      jdSummary?: string;
      jdResponsibilities?: string;
      jdRequirements?: string;
      jdNiceToHaves?: string;
      jdYearsExperience?: string;
      interviewerEmail?: string;
    };
    const { title, slug, description, departmentId } = body;

    if (!title?.trim() || !departmentId) {
      return Response.json(
        { error: "title and departmentId are required" },
        { status: 400 }
      );
    }

    const finalSlug = slug?.trim() || title.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/(^-|-$)/g, "");

    const existing = await prisma.jobRole.findUnique({ where: { slug: finalSlug } });
    if (existing) {
      return Response.json({ error: "A job role with this slug already exists" }, { status: 409 });
    }

    const trimOrNull = (v: string | undefined) => {
      const t = v?.trim();
      return t && t.length > 0 ? t : null;
    };

    const role = await prisma.jobRole.create({
      data: {
        title: title.trim(),
        slug: finalSlug,
        description: trimOrNull(description),
        departmentId,
        isActive: true,
        jdSummary: trimOrNull(body.jdSummary),
        jdResponsibilities: trimOrNull(body.jdResponsibilities),
        jdRequirements: trimOrNull(body.jdRequirements),
        jdNiceToHaves: trimOrNull(body.jdNiceToHaves),
        jdYearsExperience: trimOrNull(body.jdYearsExperience),
        interviewerEmail: trimOrNull(body.interviewerEmail),
      },
      include: { department: true },
    });

    return Response.json({ role }, { status: 201 });
  } catch (error) {
    console.error("POST /api/admin/job-roles error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

```