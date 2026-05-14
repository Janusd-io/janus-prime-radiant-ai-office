---
type: source
source_type: laptop
title: route
slug: route-31
created: 2026-05-07
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/api/admin/hr-forms/route.ts
original_size: 4439
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---

# route

_Extracted from `[[assessify|assessify]]/src/app/api/admin/hr-forms/route.ts` on 2026-05-14._

```typescript
import { NextRequest, NextResponse } from "next/server";
import { prisma } from "@/lib/db";
import { nanoid } from "nanoid";
import { sendOnboardingFormEmail } from "@/lib/email";
import { getSession } from "@/lib/auth";

// GET: List all form submissions + form invites
export async function GET() {
  const session = await getSession();
  if (!session) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });

  try {
    const [submissions, invites, templates] = await Promise.all([
      prisma.formSubmission.findMany({
        orderBy: { createdAt: "desc" },
        include: {
          template: true,
          files: true,
        },
      }),
      prisma.formInvite.findMany({
        orderBy: { createdAt: "desc" },
        include: { template: true },
      }),
      prisma.formTemplate.findMany({ where: { isActive: true } }),
    ]);

    return Response.json({ submissions, invites, templates });
  } catch (error) {
    console.error("GET /api/admin/hr-forms error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

// POST: Create a form invite and send email
export async function POST(req: NextRequest) {
  const session = await getSession();
  if (!session) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });

  try {
    const body = await req.json();
    const { employeeName, employeeEmail, templateId, region, expiresInDays } = body as {
      employeeName: string;
      employeeEmail: string;
      templateId: string;
      region?: string;
      expiresInDays?: number;
    };

    const cleanEmail = employeeEmail?.trim();
    const cleanName = employeeName?.trim();

    if (!cleanName || !cleanEmail || !templateId) {
      return Response.json(
        { error: "employeeName, employeeEmail, and templateId are required" },
        { status: 400 }
      );
    }

    const template = await prisma.formTemplate.findUnique({
      where: { id: templateId },
    });

    if (!template) {
      return Response.json({ error: "Form template not found" }, { status: 404 });
    }

    const code = nanoid(12);
    const expiresAt = expiresInDays
      ? new Date(Date.now() + expiresInDays * 24 * 60 * 60 * 1000)
      : null;

    const invite = await prisma.formInvite.create({
      data: {
        code,
        employeeName: cleanName,
        employeeEmail: cleanEmail,
        templateId,
        region: region ?? "global",
        expiresAt,
      },
    });

    // Send email
    const origin = req.headers.get("origin");
    const host = req.headers.get("host") ?? "localhost:3000";
    const isLocalhost = host.includes("localhost") || host.includes("127.0.0.1");
    const baseUrl = origin ?? `${isLocalhost ? "http" : "https"}://${host}`;
    const inviteLink = `${baseUrl}/forms/${invite.code}`;

    let emailSent = false;
    try {
      await sendOnboardingFormEmail({
        to: cleanEmail,
        employeeName: cleanName,
        formName: template.name,
        formType: template.formType,
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
          employeeName: invite.employeeName,
          employeeEmail: invite.employeeEmail,
          region: invite.region,
          status: invite.status,
          link: `/forms/${invite.code}`,
          template: { name: template.name, formType: template.formType },
        },
        emailSent,
      },
      { status: 201 }
    );
  } catch (error) {
    console.error("POST /api/admin/hr-forms error:", error);
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

    await prisma.formInvite.delete({ where: { id } });
    return Response.json({ ok: true });
  } catch (error) {
    console.error("DELETE /api/admin/hr-forms error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

```