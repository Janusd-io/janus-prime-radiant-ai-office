---
type: source
source_type: laptop
title: route
slug: route-37
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/api/admin/setup/route.ts
original_size: 2727
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# route

_Extracted from `[[assessify|assessify]]/src/app/api/admin/setup/route.ts` on 2026-05-14._

```typescript
import { NextRequest } from "next/server";
import { prisma } from "@/lib/db";
import { createSession } from "@/lib/auth";
import bcrypt from "bcryptjs";
import { checkRateLimit } from "@/lib/rate-limit";

// GET: validate invite token (public — no auth)
export async function GET(req: NextRequest) {
  try {
    const token = new URL(req.url).searchParams.get("token");
    if (!token) return Response.json({ valid: false, reason: "No token provided" });

    const otp = await prisma.passwordOtp.findFirst({
      where: { code: token, used: false, expiresAt: { gt: new Date() } },
      include: { user: { select: { email: true, isActive: true } } },
    });

    if (!otp) return Response.json({ valid: false, reason: "This invite has expired or is invalid" });
    if (otp.user.isActive) return Response.json({ valid: false, reason: "This account has already been set up" });

    return Response.json({ valid: true, email: otp.user.email });
  } catch (error) {
    console.error("GET /api/admin/setup error:", error);
    return Response.json({ valid: false, reason: "Internal server error" });
  }
}

// POST: activate account (public — no auth)
export async function POST(req: NextRequest) {
  try {
    // 5 setup attempts per minute per IP
    const rl = checkRateLimit(req, "setup", 5, 60_000);
    if (rl) return rl;

    const { token, name, password } = (await req.json()) as {
      token?: string;
      name?: string;
      password?: string;
    };

    if (!token || !name?.trim() || !password) {
      return Response.json({ error: "Token, name, and password are required" }, { status: 400 });
    }
    if (password.length < 8) {
      return Response.json({ error: "Password must be at least 8 characters" }, { status: 400 });
    }

    const otp = await prisma.passwordOtp.findFirst({
      where: { code: token, used: false, expiresAt: { gt: new Date() } },
      include: { user: true },
    });

    if (!otp) {
      return Response.json({ error: "This invite has expired or is invalid" }, { status: 400 });
    }
    if (otp.user.isActive) {
      return Response.json({ error: "This account has already been set up" }, { status: 400 });
    }

    const passwordHash = await bcrypt.hash(password, 12);

    await prisma.adminUser.update({
      where: { id: otp.user.id },
      data: { name: name.trim(), passwordHash, isActive: true },
    });

    await prisma.passwordOtp.update({
      where: { id: otp.id },
      data: { used: true },
    });

    await createSession(otp.user.id);

    return Response.json({ ok: true });
  } catch (error) {
    console.error("POST /api/admin/setup error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

```