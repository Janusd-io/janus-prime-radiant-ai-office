---
type: source
source_type: laptop
title: route
slug: route-49
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/api/admin/users/route.ts
original_size: 3167
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---

# route

_Extracted from `[[assessify|assessify]]/src/app/api/admin/users/route.ts` on 2026-05-14._

```typescript
import { NextRequest } from "next/server";
import { prisma } from "@/lib/db";
import { getSession } from "@/lib/auth";
import { sendAdminInviteEmail } from "@/lib/email";
import { nanoid } from "nanoid";
import { auditLog } from "@/lib/audit";
import { getClientIp } from "@/lib/rate-limit";

// GET: list all admin users
export async function GET() {
  try {
    const session = await getSession();
    if (!session) return Response.json({ error: "Unauthorized" }, { status: 401 });

    const users = await prisma.adminUser.findMany({
      select: { id: true, email: true, name: true, role: true, isActive: true, createdAt: true },
      orderBy: { createdAt: "asc" },
    });

    return Response.json({ users });
  } catch (error) {
    console.error("GET /api/admin/users error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

// POST: invite a new admin user (admin only)
export async function POST(req: NextRequest) {
  try {
    const session = await getSession();
    if (!session) return Response.json({ error: "Unauthorized" }, { status: 401 });
    if (session.role !== "admin") return Response.json({ error: "Only admins can invite users" }, { status: 403 });

    const { email, role } = (await req.json()) as { email?: string; role?: string };

    if (!email?.trim()) return Response.json({ error: "Email is required" }, { status: 400 });
    if (!role || !["admin", "user"].includes(role)) {
      return Response.json({ error: "Role must be 'admin' or 'user'" }, { status: 400 });
    }

    const existing = await prisma.adminUser.findUnique({ where: { email: email.trim().toLowerCase() } });
    if (existing) {
      return Response.json({ error: "A user with this email already exists" }, { status: 409 });
    }

    const user = await prisma.adminUser.create({
      data: {
        email: email.trim().toLowerCase(),
        name: "Pending",
        passwordHash: "",
        role,
        isActive: false,
      },
    });

    const token = nanoid(32);
    await prisma.passwordOtp.create({
      data: {
        userId: user.id,
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
        to: email.trim().toLowerCase(),
        inviterName: session.name,
        role,
        inviteLink,
      });
      emailSent = true;
    } catch (e) {
      console.error("Failed to send admin invite email:", e);
    }

    await auditLog({
      userId: session.id, userEmail: session.email, action: "user.invited",
      targetType: "AdminUser", targetId: user.id,
      details: { email: user.email, role }, ipAddress: getClientIp(req),
    });

    return Response.json({ ok: true, emailSent, inviteLink }, { status: 201 });
  } catch (error) {
    console.error("POST /api/admin/users error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

```