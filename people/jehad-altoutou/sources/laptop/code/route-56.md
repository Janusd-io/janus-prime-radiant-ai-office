---
type: source
source_type: laptop
title: Assessify — route
slug: route-56
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/api/admin/invites/route.ts
original_size: 4236
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# route

_Extracted from `[[assessify|assessify]]/src/app/api/admin/invites/route.ts` on 2026-05-14._

```typescript
import { NextRequest, NextResponse } from "next/server";
import { prisma } from "@/lib/db";
import { nanoid } from "nanoid";
import { sendInviteEmail } from "@/lib/email";
import { getSession } from "@/lib/auth";

export async function GET() {
  const session = await getSession();
  if (!session) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });

  try {
    const invites = await prisma.candidateInvite.findMany({
      orderBy: { createdAt: "desc" },
      include: {
        template: {
          include: {
            jobRole: { include: { department: true } },
          },
        },
      },
    });

    return Response.json({ invites });
  } catch (error) {
    console.error("GET /api/admin/invites error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

export async function POST(req: NextRequest) {
  const session = await getSession();
  if (!session) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });

  try {
    const body = await req.json();
    const { candidateName, candidateEmail, templateId, expiresInDays } = body as {
      candidateName: string;
      candidateEmail: string;
      templateId: string;
      expiresInDays?: number;
    };

    if (!candidateName || !candidateEmail || !templateId) {
      return Response.json(
        { error: "candidateName, candidateEmail, and templateId are required" },
        { status: 400 }
      );
    }

    const template = await prisma.assessmentTemplate.findUnique({
      where: { id: templateId },
      include: { jobRole: { include: { department: true } } },
    });

    if (!template) {
      return Response.json({ error: "Assessment template not found" }, { status: 404 });
    }

    const code = nanoid(12);
    const expiresAt = expiresInDays
      ? new Date(Date.now() + expiresInDays * 24 * 60 * 60 * 1000)
      : null;

    const invite = await prisma.candidateInvite.create({
      data: {
        code,
        candidateName,
        candidateEmail,
        templateId,
        expiresAt,
      },
    });

    // Send invite email
    const origin = req.headers.get("origin");
    const host = req.headers.get("host") ?? "localhost:3000";
    const isLocalhost = host.includes("localhost") || host.includes("127.0.0.1");
    const baseUrl = origin ?? `${isLocalhost ? "http" : "https"}://${host}`;
    const inviteLink = `${baseUrl}/assess/invite/${invite.code}`;

    let emailSent = false;
    try {
      await sendInviteEmail({
        to: candidateEmail,
        candidateName,
        assessmentTitle: template.title,
        department: template.jobRole.department.name,
        jobRole: template.jobRole.title,
        inviteLink,
        expiresAt: invite.expiresAt,
      });
      emailSent = true;
    } catch (emailError) {
      console.error("Email send failed (invite still created):", emailError);
    }

    return Response.json(
      {
        invite: {
          id: invite.id,
          code: invite.code,
          candidateName: invite.candidateName,
          candidateEmail: invite.candidateEmail,
          status: invite.status,
          expiresAt: invite.expiresAt,
          link: `/assess/invite/${invite.code}`,
          template: {
            title: template.title,
            jobRole: template.jobRole.title,
            department: template.jobRole.department.name,
          },
        },
        emailSent,
      },
      { status: 201 }
    );
  } catch (error) {
    console.error("POST /api/admin/invites error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

export async function DELETE(req: NextRequest) {
  const session = await getSession();
  if (!session) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });

  try {
    const id = new URL(req.url).searchParams.get("id");
    if (!id) {
      return Response.json({ error: "id is required" }, { status: 400 });
    }

    await prisma.candidateInvite.delete({ where: { id } });
    return Response.json({ ok: true });
  } catch (error) {
    console.error("DELETE /api/admin/invites error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

```