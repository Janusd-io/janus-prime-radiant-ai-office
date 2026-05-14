---
type: source
source_type: laptop
title: route
slug: route-27
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: "/Users/jehad/assessify/src/app/api/admin/assessments/[id]/publish/route.ts"
original_size: 2248
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---

# route

_Extracted from `[[assessify|assessify]]/src/app/api/admin/assessments/[id]/publish/route.ts` on 2026-05-14._

```typescript
import { NextRequest, NextResponse } from "next/server";
import { prisma } from "@/lib/db";
import { getSession } from "@/lib/auth";

export async function POST(
  req: NextRequest,
  ctx: { params: Promise<{ id: string }> }
) {
  const session = await getSession();
  if (!session) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });

  try {
    const { id } = await ctx.params;
    const { action } = await req.json() as { action: "publish" | "unpublish" };

    const latestVersion = await prisma.assessmentVersion.findFirst({
      where: { templateId: id },
      orderBy: { versionNumber: "desc" },
      include: { sections: { include: { _count: { select: { questions: true } } } } },
    });

    if (!latestVersion) {
      return Response.json({ error: "No version found" }, { status: 404 });
    }

    if (action === "publish") {
      // Validate: must have at least one section with at least one question
      if (latestVersion.sections.length === 0) {
        return Response.json(
          { error: "Cannot publish: assessment has no sections" },
          { status: 400 }
        );
      }
      const totalQuestions = latestVersion.sections.reduce(
        (sum, s) => sum + s._count.questions,
        0
      );
      if (totalQuestions === 0) {
        return Response.json(
          { error: "Cannot publish: assessment has no questions" },
          { status: 400 }
        );
      }

      // Archive any currently published version (except this one)
      await prisma.assessmentVersion.updateMany({
        where: { templateId: id, status: "published", NOT: { id: latestVersion.id } },
        data: { status: "archived" },
      });

      await prisma.assessmentVersion.update({
        where: { id: latestVersion.id },
        data: { status: "published", publishedAt: new Date() },
      });
    } else if (action === "unpublish") {
      await prisma.assessmentVersion.update({
        where: { id: latestVersion.id },
        data: { status: "draft" },
      });
    }

    return Response.json({ ok: true });
  } catch (error) {
    console.error("POST /api/admin/assessments/[id]/publish error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

```