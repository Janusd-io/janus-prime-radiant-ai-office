---
type: source
source_type: laptop
title: route
slug: route-50
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: "/Users/jehad/assessify/src/app/api/admin/users/[id]/route.ts"
original_size: 4712
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# route

_Extracted from `[[assessify|assessify]]/src/app/api/admin/users/[id]/route.ts` on 2026-05-14._

```typescript
import { NextRequest } from "next/server";
import { prisma } from "@/lib/db";
import { getSession } from "@/lib/auth";
import bcrypt from "bcryptjs";
import { auditLog } from "@/lib/audit";
import { getClientIp } from "@/lib/rate-limit";

// PATCH: update user (toggle active, change role, reset password) — admin only
export async function PATCH(
  req: NextRequest,
  ctx: { params: Promise<{ id: string }> }
) {
  try {
    const session = await getSession();
    if (!session) return Response.json({ error: "Unauthorized" }, { status: 401 });
    if (session.role !== "admin") return Response.json({ error: "Only admins can manage users" }, { status: 403 });

    const { id } = await ctx.params;
    const { isActive, role, newPassword } = (await req.json()) as {
      isActive?: boolean;
      role?: string;
      newPassword?: string;
    };

    // Prevent self-modification for dangerous actions
    if (id === session.id) {
      if (isActive === false) return Response.json({ error: "You cannot deactivate yourself" }, { status: 400 });
      if (role && role !== session.role) return Response.json({ error: "You cannot change your own role" }, { status: 400 });
    }

    // Prevent deactivating the last active admin
    if (isActive === false || (role && role !== "admin")) {
      const target = await prisma.adminUser.findUnique({ where: { id } });
      if (target?.role === "admin") {
        const adminCount = await prisma.adminUser.count({ where: { role: "admin", isActive: true } });
        if (adminCount <= 1) {
          return Response.json({ error: "Cannot remove the last active admin" }, { status: 400 });
        }
      }
    }

    const data: Record<string, unknown> = {};
    if (isActive !== undefined) data.isActive = isActive;
    if (role && ["admin", "user"].includes(role)) data.role = role;
    if (newPassword) {
      if (newPassword.length < 8) return Response.json({ error: "Password must be at least 8 characters" }, { status: 400 });
      data.passwordHash = await bcrypt.hash(newPassword, 12);
    }

    if (Object.keys(data).length === 0) {
      return Response.json({ error: "Nothing to update" }, { status: 400 });
    }

    await prisma.adminUser.update({ where: { id }, data });

    const actions: string[] = [];
    if (isActive !== undefined) actions.push(isActive ? "user.reactivated" : "user.deactivated");
    if (role) actions.push("user.role_changed");
    if (newPassword) actions.push("user.password_reset");
    for (const action of actions) {
      await auditLog({
        userId: session.id, userEmail: session.email, action,
        targetType: "AdminUser", targetId: id,
        details: { ...(role ? { newRole: role } : {}), ...(isActive !== undefined ? { isActive } : {}) },
        ipAddress: getClientIp(req),
      });
    }

    return Response.json({ ok: true });
  } catch (error) {
    console.error("PATCH /api/admin/users/[id] error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

// DELETE: permanently delete user — admin only
export async function DELETE(
  _req: NextRequest,
  ctx: { params: Promise<{ id: string }> }
) {
  try {
    const session = await getSession();
    if (!session) return Response.json({ error: "Unauthorized" }, { status: 401 });
    if (session.role !== "admin") return Response.json({ error: "Only admins can delete users" }, { status: 403 });

    const { id } = await ctx.params;

    if (id === session.id) {
      return Response.json({ error: "You cannot delete yourself" }, { status: 400 });
    }

    const target = await prisma.adminUser.findUnique({ where: { id } });
    if (!target) return Response.json({ error: "User not found" }, { status: 404 });

    // Only guard if the target is an ACTIVE admin — pending/inactive admins can always be deleted
    if (target.role === "admin" && target.isActive) {
      const adminCount = await prisma.adminUser.count({ where: { role: "admin", isActive: true } });
      if (adminCount <= 1) {
        return Response.json({ error: "Cannot delete the last active admin" }, { status: 400 });
      }
    }

    await prisma.passwordOtp.deleteMany({ where: { userId: id } });
    await prisma.adminUser.delete({ where: { id } });

    await auditLog({
      userId: session.id, userEmail: session.email, action: "user.deleted",
      targetType: "AdminUser", targetId: id,
      details: { email: target.email, name: target.name },
      ipAddress: getClientIp(_req),
    });

    return Response.json({ ok: true });
  } catch (error) {
    console.error("DELETE /api/admin/users/[id] error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

```