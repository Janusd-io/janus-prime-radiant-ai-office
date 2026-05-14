---
type: source
source_type: laptop
title: route
slug: route-21
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: "/Users/jehad/assessify/src/app/api/admin/assessments/[id]/route.ts"
original_size: 5232
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# route

_Extracted from `assessify/src/app/api/admin/assessments/[id]/route.ts` on 2026-05-14._

```typescript
import { NextRequest, NextResponse } from "next/server";
import { prisma } from "@/lib/db";
import { getSession } from "@/lib/auth";

// GET full template with all nested data (for editor)
export async function GET(
  _req: NextRequest,
  ctx: { params: Promise<{ id: string }> }
) {
  const session = await getSession();
  if (!session) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });

  try {
    const { id } = await ctx.params;

    const template = await prisma.assessmentTemplate.findUnique({
      where: { id },
      include: {
        jobRole: { include: { department: true } },
        versions: {
          include: {
            sections: {
              orderBy: { sortOrder: "asc" },
              include: {
                questions: {
                  orderBy: { sortOrder: "asc" },
                  include: {
                    options: { orderBy: { sortOrder: "asc" } },
                    competencies: { include: { competency: true } },
                  },
                },
              },
            },
          },
          orderBy: { versionNumber: "desc" },
        },
      },
    });

    if (!template) {
      return Response.json({ error: "Template not found" }, { status: 404 });
    }

    return Response.json({ template });
  } catch (error) {
    console.error("GET /api/admin/assessments/[id] error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

// PATCH update template fields or version fields (title, desc, passingScore, timeLimit)
export async function PATCH(
  req: NextRequest,
  ctx: { params: Promise<{ id: string }> }
) {
  const session = await getSession();
  if (!session) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });

  try {
    const { id } = await ctx.params;
    const body = await req.json();
    const { title, description, passingScore, timeLimit, recommendationThresholds, eggHuntEnabled } = body;

    if (title || description !== undefined || eggHuntEnabled !== undefined) {
      await prisma.assessmentTemplate.update({
        where: { id },
        data: {
          ...(title && { title }),
          ...(description !== undefined && { description }),
          ...(eggHuntEnabled !== undefined && { eggHuntEnabled }),
        },
      });
    }

    // Update latest version's settings
    if (passingScore !== undefined || timeLimit !== undefined || recommendationThresholds !== undefined) {
      const latestVersion = await prisma.assessmentVersion.findFirst({
        where: { templateId: id },
        orderBy: { versionNumber: "desc" },
      });
      if (latestVersion) {
        await prisma.assessmentVersion.update({
          where: { id: latestVersion.id },
          data: {
            ...(passingScore !== undefined && { passingScore }),
            ...(timeLimit !== undefined && { timeLimit }),
            ...(recommendationThresholds !== undefined && {
              recommendationThresholds: typeof recommendationThresholds === "string"
                ? recommendationThresholds
                : JSON.stringify(recommendationThresholds),
            }),
          },
        });
      }
    }

    return Response.json({ ok: true });
  } catch (error) {
    console.error("PATCH /api/admin/assessments/[id] error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

export async function DELETE(
  _req: NextRequest,
  ctx: { params: Promise<{ id: string }> }
) {
  const session = await getSession();
  if (!session) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });

  try {
    const { id } = await ctx.params;

    // Check if any sessions exist — prevent deletion if so
    const sessionCount = await prisma.candidateSession.count({
      where: { version: { templateId: id } },
    });
    if (sessionCount > 0) {
      return Response.json(
        { error: `Cannot delete assessment with ${sessionCount} candidate sessions. Archive it instead.` },
        { status: 400 }
      );
    }

    // Delete in proper order
    const versions = await prisma.assessmentVersion.findMany({ where: { templateId: id } });
    for (const v of versions) {
      const sections = await prisma.section.findMany({ where: { versionId: v.id } });
      for (const s of sections) {
        const questions = await prisma.question.findMany({ where: { sectionId: s.id } });
        for (const q of questions) {
          await prisma.questionCompetency.deleteMany({ where: { questionId: q.id } });
          await prisma.answerOption.deleteMany({ where: { questionId: q.id } });
        }
        await prisma.question.deleteMany({ where: { sectionId: s.id } });
      }
      await prisma.section.deleteMany({ where: { versionId: v.id } });
    }
    await prisma.candidateInvite.deleteMany({ where: { templateId: id } });
    await prisma.assessmentVersion.deleteMany({ where: { templateId: id } });
    await prisma.assessmentTemplate.delete({ where: { id } });

    return Response.json({ ok: true });
  } catch (error) {
    console.error("DELETE /api/admin/assessments/[id] error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

```