---
type: source
source_type: laptop
title: route
slug: route-65
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/api/sessions/route.ts
original_size: 3942
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---

# route

_Extracted from `[[assessify|assessify]]/src/app/api/sessions/route.ts` on 2026-05-14._

```typescript
import { NextRequest } from "next/server";
import { prisma } from "@/lib/db";
import { trackEvent } from "@/lib/analytics";

export async function POST(req: NextRequest) {
  try {
    const body = await req.json();
    const { assessmentSlug, candidateName, candidateEmail } = body;

    if (!assessmentSlug || !candidateName || !candidateEmail) {
      return Response.json(
        { error: "assessmentSlug, candidateName, and candidateEmail are required" },
        { status: 400 }
      );
    }

    const template = await prisma.assessmentTemplate.findUnique({
      where: { slug: assessmentSlug, isActive: true },
      include: {
        versions: {
          where: { status: "published" },
          orderBy: { versionNumber: "desc" },
          take: 1,
          include: {
            sections: {
              where: { isActive: true },
              orderBy: { sortOrder: "asc" },
              include: {
                questions: {
                  where: { isActive: true },
                  orderBy: { sortOrder: "asc" },
                  include: {
                    options: {
                      orderBy: { sortOrder: "asc" },
                      select: {
                        id: true,
                        key: true,
                        label: true,
                        value: true,
                        sortOrder: true,
                        metadata: true,
                      },
                    },
                  },
                },
              },
            },
          },
        },
      },
    });

    if (!template || template.versions.length === 0) {
      return Response.json({ error: "Assessment not found or not published" }, { status: 404 });
    }

    const version = template.versions[0];

    const session = await prisma.candidateSession.create({
      data: {
        versionId: version.id,
        candidateName,
        candidateEmail,
        status: "in_progress",
        startedAt: new Date(),
        lastActiveAt: new Date(),
        ipAddress: req.headers.get("x-forwarded-for") ?? req.headers.get("x-real-ip") ?? null,
        userAgent: req.headers.get("user-agent") ?? null,
      },
    });

    await trackEvent("assessment_started", {
      sessionId: session.id,
      eventData: {
        assessmentSlug,
        templateId: template.id,
        versionId: version.id,
        candidateName,
        candidateEmail,
      },
    });

    return Response.json(
      {
        session: {
          id: session.id,
          status: session.status,
          startedAt: session.startedAt,
          candidateName: session.candidateName,
          candidateEmail: session.candidateEmail,
        },
        assessment: {
          id: template.id,
          title: template.title,
          slug: template.slug,
          version: {
            id: version.id,
            versionNumber: version.versionNumber,
            passingScore: version.passingScore,
            timeLimit: version.timeLimit,
          },
          sections: version.sections.map((section) => ({
            id: section.id,
            title: section.title,
            slug: section.slug,
            description: section.description,
            introText: section.introText,
            iconName: section.iconName,
            sortOrder: section.sortOrder,
            weight: section.weight,
            questions: section.questions.map((q) => ({
              id: q.id,
              slug: q.slug,
              title: q.title,
              prompt: q.prompt,
              questionType: q.questionType,
              difficulty: q.difficulty,
              sortOrder: q.sortOrder,
              options: q.options,
            })),
          })),
        },
      },
      { status: 201 }
    );
  } catch (error) {
    console.error("POST /api/sessions error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

```