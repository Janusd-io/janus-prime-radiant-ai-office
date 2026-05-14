---
type: source
source_type: laptop
title: route
slug: route-59
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/api/admin/analytics/route.ts
original_size: 4158
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# route

_Extracted from `assessify/src/app/api/admin/analytics/route.ts` on 2026-05-14._

```typescript
import { NextRequest } from "next/server";
import { prisma } from "@/lib/db";
import { getSession } from "@/lib/auth";
import {
  getAssessmentFunnel,
  getQuestionAnalytics,
  getCompetencyHeatmap,
  getResultDistribution,
} from "@/lib/analytics";

export async function GET(req: NextRequest) {
  try {
    const session = await getSession();
    if (!session) return Response.json({ error: "Unauthorized" }, { status: 401 });

    const { searchParams } = new URL(req.url);
    const versionId = searchParams.get("versionId");
    const type = searchParams.get("type") ?? "funnel";

    // Overview mode: return cross-assessment stats
    if (type === "overview") {
      const templates = await prisma.assessmentTemplate.findMany({
        where: { isActive: true, slug: { not: { startsWith: "library-" } } },
        include: {
          jobRole: { include: { department: true } },
          versions: {
            orderBy: { versionNumber: "desc" },
            include: {
              sections: { select: { id: true, _count: { select: { questions: true } } } },
              _count: { select: { candidateSessions: true } },
            },
          },
        },
      });

      // Global stats
      const totalSessions = await prisma.candidateSession.count();
      const completedSessions = await prisma.candidateSession.count({ where: { status: "completed" } });
      const totalInvites = await prisma.candidateInvite.count();
      const pendingInvites = await prisma.candidateInvite.count({ where: { status: "pending" } });
      const totalResults = await prisma.candidateResult.count();
      const allResults = await prisma.candidateResult.findMany({ select: { normalizedScore: true, recommendation: true } });

      const avgScore = allResults.length > 0
        ? allResults.reduce((s, r) => s + r.normalizedScore, 0) / allResults.length
        : 0;

      const recDist: Record<string, number> = { strong_hire: 0, hire: 0, consider: 0, weak_fit: 0, reject: 0 };
      for (const r of allResults) recDist[r.recommendation] = (recDist[r.recommendation] ?? 0) + 1;

      const assessments = templates.map((t) => {
        // Prefer version with candidates, else published, else latest
        const v = t.versions.find((v) => v._count.candidateSessions > 0)
          ?? t.versions.find((v) => v.status === "published")
          ?? t.versions[0];
        return {
          id: t.id,
          title: t.title,
          department: t.jobRole.department.name,
          departmentSlug: t.jobRole.department.slug,
          jobRole: t.jobRole.title,
          versionId: v?.id,
          status: v?.status ?? "draft",
          candidates: v?._count.candidateSessions ?? 0,
          questions: v?.sections.reduce((s, sec) => s + sec._count.questions, 0) ?? 0,
        };
      });

      return Response.json({
        type: "overview",
        data: {
          totalSessions,
          completedSessions,
          completionRate: totalSessions > 0 ? completedSessions / totalSessions : 0,
          totalInvites,
          pendingInvites,
          totalResults,
          avgScore,
          recommendationDistribution: recDist,
          assessments,
        },
      });
    }

    if (!versionId) {
      return Response.json({ error: "versionId query param is required" }, { status: 400 });
    }

    let data: unknown;

    switch (type) {
      case "funnel":
        data = await getAssessmentFunnel(versionId);
        break;
      case "questions":
        data = await getQuestionAnalytics(versionId);
        break;
      case "competencies":
        data = await getCompetencyHeatmap(versionId);
        break;
      case "distribution":
        data = await getResultDistribution(versionId);
        break;
      default:
        return Response.json(
          { error: "type must be one of: overview, funnel, questions, competencies, distribution" },
          { status: 400 }
        );
    }

    return Response.json({ type, versionId, data });
  } catch (error) {
    console.error("GET /api/admin/analytics error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

```