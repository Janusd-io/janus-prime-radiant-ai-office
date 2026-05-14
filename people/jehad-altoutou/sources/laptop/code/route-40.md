---
type: source
source_type: laptop
title: route
slug: route-40
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/api/admin/sessions/route.ts
original_size: 2218
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# route

_Extracted from `[[assessify|assessify]]/src/app/api/admin/sessions/route.ts` on 2026-05-14._

```typescript
import { NextResponse } from "next/server";
import { prisma } from "@/lib/db";
import { getSession } from "@/lib/auth";

export async function GET() {
  const session = await getSession();
  if (!session) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });

  try {
    const sessions = await prisma.candidateSession.findMany({
      orderBy: { createdAt: "desc" },
      include: {
        version: {
          include: {
            template: { select: { id: true, title: true, slug: true } },
          },
        },
        result: {
          select: {
            recommendation: true,
            normalizedScore: true,
            totalScore: true,
            maxScore: true,
            confidenceRating: true,
            automationLabels: true,
            createdAt: true,
          },
        },
        _count: {
          select: { responses: true },
        },
      },
    });

    return Response.json({
      sessions: sessions.map((s) => ({
        id: s.id,
        status: s.status,
        candidateName: s.candidateName,
        candidateEmail: s.candidateEmail,
        startedAt: s.startedAt,
        completedAt: s.completedAt,
        lastActiveAt: s.lastActiveAt,
        createdAt: s.createdAt,
        assessment: {
          title: s.version.template.title,
          slug: s.version.template.slug,
          versionId: s.version.id,
          versionNumber: s.version.versionNumber,
        },
        responseCount: s._count.responses,
        result: s.result
          ? {
              recommendation: s.result.recommendation,
              normalizedScore: s.result.normalizedScore,
              totalScore: s.result.totalScore,
              maxScore: s.result.maxScore,
              confidenceRating: s.result.confidenceRating,
              automationLabels: s.result.automationLabels
                ? JSON.parse(s.result.automationLabels)
                : [],
              completedAt: s.result.createdAt,
            }
          : null,
      })),
      total: sessions.length,
    });
  } catch (error) {
    console.error("GET /api/admin/sessions error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

```