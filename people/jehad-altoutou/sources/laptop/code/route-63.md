---
type: source
source_type: laptop
title: route
slug: route-63
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: "/Users/jehad/assessify/src/app/api/assess/invite/[code]/route.ts"
original_size: 2418
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# route

_Extracted from `[[assessify|assessify]]/src/app/api/assess/invite/[code]/route.ts` on 2026-05-14._

```typescript
import { NextRequest } from "next/server";
import { prisma } from "@/lib/db";

export async function GET(
  _req: NextRequest,
  ctx: { params: Promise<{ code: string }> }
) {
  try {
    const { code } = await ctx.params;

    const invite = await prisma.candidateInvite.findUnique({
      where: { code },
      include: {
        template: {
          include: {
            jobRole: { include: { department: true } },
            versions: {
              where: { status: "published" },
              orderBy: { versionNumber: "desc" },
              take: 1,
              include: {
                sections: {
                  where: { isActive: true },
                  include: {
                    _count: { select: { questions: { where: { isActive: true } } } },
                  },
                },
              },
            },
          },
        },
      },
    });

    if (!invite) {
      return Response.json({ error: "Invite not found or invalid link." }, { status: 404 });
    }

    if (invite.expiresAt && invite.expiresAt < new Date()) {
      return Response.json({ error: "This invite has expired. Please contact the hiring team for a new link." }, { status: 410 });
    }

    const version = invite.template.versions[0];
    if (!version) {
      return Response.json({ error: "No published assessment available for this role." }, { status: 404 });
    }

    const questionCount = version.sections.reduce(
      (sum, s) => sum + s._count.questions,
      0
    );

    return Response.json({
      invite: {
        id: invite.id,
        code: invite.code,
        candidateName: invite.candidateName,
        candidateEmail: invite.candidateEmail,
        status: invite.status,
        sessionId: invite.sessionId,
        expiresAt: invite.expiresAt,
      },
      assessment: {
        title: invite.template.title,
        slug: invite.template.slug,
        description: invite.template.description,
        department: invite.template.jobRole.department.name,
        departmentSlug: invite.template.jobRole.department.slug,
        jobRole: invite.template.jobRole.title,
        timeLimit: version.timeLimit,
        sectionCount: version.sections.length,
        questionCount,
      },
    });
  } catch (error) {
    console.error("GET /api/assess/invite/[code] error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

```