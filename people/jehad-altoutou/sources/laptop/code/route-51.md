---
type: source
source_type: laptop
title: route
slug: route-51
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: "/Users/jehad/assessify/src/app/api/admin/users/[id]/resend/route.ts"
original_size: 1966
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# route

_Extracted from `[[assessify|assessify]]/src/app/api/admin/users/[id]/resend/route.ts` on 2026-05-14._

```typescript
import { NextRequest } from "next/server";
import { prisma } from "@/lib/db";
import { getSession } from "@/lib/auth";
import { sendAdminInviteEmail } from "@/lib/email";
import { nanoid } from "nanoid";

// POST: resend invite for a pending user — admin only
export async function POST(
  _req: NextRequest,
  ctx: { params: Promise<{ id: string }> }
) {
  try {
    const session = await getSession();
    if (!session) return Response.json({ error: "Unauthorized" }, { status: 401 });
    if (session.role !== "admin") return Response.json({ error: "Only admins can resend invites" }, { status: 403 });

    const { id } = await ctx.params;
    const user = await prisma.adminUser.findUnique({ where: { id } });
    if (!user) return Response.json({ error: "User not found" }, { status: 404 });
    if (user.isActive) return Response.json({ error: "User is already active" }, { status: 400 });

    // Expire old tokens
    await prisma.passwordOtp.updateMany({
      where: { userId: id, used: false },
      data: { used: true },
    });

    const token = nanoid(32);
    await prisma.passwordOtp.create({
      data: {
        userId: id,
        code: token,
        expiresAt: new Date(Date.now() + 7 * 24 * 60 * 60 * 1000),
      },
    });

    const baseUrl =
      process.env.PUBLIC_APP_URL ??
      process.env.APP_URL ??
      "http://localhost:3000";
    const inviteLink = `${baseUrl}/admin/setup?token=${token}`;

    let emailSent = false;
    try {
      await sendAdminInviteEmail({
        to: user.email,
        inviterName: session.name,
        role: user.role,
        inviteLink,
      });
      emailSent = true;
    } catch (e) {
      console.error("Failed to resend admin invite:", e);
    }

    return Response.json({ ok: true, emailSent, inviteLink });
  } catch (error) {
    console.error("POST /api/admin/users/[id]/resend error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

```