---
type: source
source_type: laptop
title: Assessify — route
slug: route-64
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: "/Users/jehad/assessify/src/app/api/assess/invite/[code]/start/route.ts"
original_size: 2424
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# route

_Extracted from `[[assessify|assessify]]/src/app/api/assess/invite/[code]/start/route.ts` on 2026-05-14._

```typescript
import { NextRequest } from "next/server";
import { prisma } from "@/lib/db";
import { trackEvent } from "@/lib/analytics";

export async function POST(
  req: NextRequest,
  ctx: { params: Promise<{ code: string }> }
) {
  try {
    const { code } = await ctx.params;

    const invite = await prisma.candidateInvite.findUnique({
      where: { code },
      include: {
        template: {
          include: {
            versions: {
              where: { status: "published" },
              orderBy: { versionNumber: "desc" },
              take: 1,
            },
          },
        },
      },
    });

    if (!invite) {
      return Response.json({ error: "Invite not found." }, { status: 404 });
    }

    if (invite.expiresAt && invite.expiresAt < new Date()) {
      return Response.json({ error: "This invite has expired." }, { status: 410 });
    }

    // If already started, return existing session
    if (invite.sessionId) {
      return Response.json({ sessionId: invite.sessionId });
    }

    const version = invite.template.versions[0];
    if (!version) {
      return Response.json({ error: "No published assessment available." }, { status: 404 });
    }

    // Create session
    const session = await prisma.candidateSession.create({
      data: {
        versionId: version.id,
        candidateName: invite.candidateName,
        candidateEmail: invite.candidateEmail,
        status: "in_progress",
        startedAt: new Date(),
        lastActiveAt: new Date(),
        ipAddress:
          req.headers.get("x-forwarded-for") ??
          req.headers.get("x-real-ip") ??
          null,
        userAgent: req.headers.get("user-agent") ?? null,
      },
    });

    // Link invite to session
    await prisma.candidateInvite.update({
      where: { id: invite.id },
      data: { status: "started", sessionId: session.id },
    });

    await trackEvent("assessment_started", {
      sessionId: session.id,
      eventData: {
        inviteCode: invite.code,
        templateId: invite.templateId,
        versionId: version.id,
        candidateName: invite.candidateName,
        candidateEmail: invite.candidateEmail,
      },
    });

    return Response.json({ sessionId: session.id }, { status: 201 });
  } catch (error) {
    console.error("POST /api/assess/invite/[code]/start error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

```