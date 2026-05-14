---
type: source
source_type: laptop
title: Assessify — route
slug: route-29
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/api/admin/auth/route.ts
original_size: 1875
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# route

_Extracted from `[[assessify|assessify]]/src/app/api/admin/auth/route.ts` on 2026-05-14._

```typescript
import { NextRequest } from "next/server";
import { prisma } from "@/lib/db";
import bcrypt from "bcryptjs";
import { createSession, destroySession } from "@/lib/auth";
import { checkRateLimit, getClientIp } from "@/lib/rate-limit";
import { auditLog } from "@/lib/audit";

export async function GET() {
  try {
    const { getSession } = await import("@/lib/auth");
    const session = await getSession();
    if (!session) return Response.json({ user: null });
    return Response.json({ user: session });
  } catch {
    return Response.json({ user: null });
  }
}

export async function POST(req: NextRequest) {
  try {
    // 5 login attempts per minute per IP
    const rl = checkRateLimit(req, "login", 5, 60_000);
    if (rl) return rl;

    const { email, password } = await req.json();

    if (!email || !password) {
      return Response.json(
        { error: "Email and password are required" },
        { status: 400 }
      );
    }

    const user = await prisma.adminUser.findUnique({
      where: { email, isActive: true },
    });

    if (!user) {
      return Response.json({ error: "Invalid credentials" }, { status: 401 });
    }

    const valid = await bcrypt.compare(password, user.passwordHash);
    if (!valid) {
      return Response.json({ error: "Invalid credentials" }, { status: 401 });
    }

    await createSession(user.id);

    await auditLog({
      userId: user.id, userEmail: user.email, action: "auth.login",
      ipAddress: getClientIp(req),
    });

    return Response.json({
      user: { id: user.id, email: user.email, name: user.name, role: user.role },
    });
  } catch (error) {
    console.error("POST /api/admin/auth error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

export async function DELETE() {
  await destroySession();
  return Response.json({ ok: true });
}

```