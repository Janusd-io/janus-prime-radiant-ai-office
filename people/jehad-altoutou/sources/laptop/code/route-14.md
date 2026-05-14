---
type: source
source_type: laptop
title: route
slug: route-14
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: "/Users/jehad/assessify/src/app/api/forms/invite/[code]/start/route.ts"
original_size: 1727
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# route

_Extracted from `[[assessify|assessify]]/src/app/api/forms/invite/[code]/start/route.ts` on 2026-05-14._

```typescript
import { NextRequest } from "next/server";
import { prisma } from "@/lib/db";

export async function POST(
  req: NextRequest,
  ctx: { params: Promise<{ code: string }> }
) {
  try {
    const { code } = await ctx.params;

    const invite = await prisma.formInvite.findUnique({
      where: { code },
      include: { template: true },
    });

    if (!invite) {
      return Response.json({ error: "Invite not found." }, { status: 404 });
    }

    if (invite.expiresAt && invite.expiresAt < new Date()) {
      return Response.json({ error: "This invite has expired." }, { status: 410 });
    }

    // If already started, return existing submission
    if (invite.submissionId) {
      return Response.json({ submissionId: invite.submissionId });
    }

    // Create submission
    const submission = await prisma.formSubmission.create({
      data: {
        templateId: invite.templateId,
        employeeName: invite.employeeName,
        employeeEmail: invite.employeeEmail,
        region: invite.region,
        formData: "{}",
        status: "draft",
        inviteCode: invite.code,
        startedAt: new Date(),
        ipAddress:
          req.headers.get("x-forwarded-for") ??
          req.headers.get("x-real-ip") ??
          null,
        userAgent: req.headers.get("user-agent") ?? null,
      },
    });

    await prisma.formInvite.update({
      where: { id: invite.id },
      data: { status: "started", submissionId: submission.id },
    });

    return Response.json({ submissionId: submission.id }, { status: 201 });
  } catch (error) {
    console.error("POST /api/forms/invite/[code]/start error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

```