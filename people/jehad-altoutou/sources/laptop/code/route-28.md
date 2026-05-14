---
type: source
source_type: laptop
title: route
slug: route-28
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/api/admin/verify-otp/route.ts
original_size: 1446
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---

# route

_Extracted from `[[assessify|assessify]]/src/app/api/admin/verify-otp/route.ts` on 2026-05-14._

```typescript
import { NextRequest } from "next/server";
import { prisma } from "@/lib/db";
import { checkRateLimit } from "@/lib/rate-limit";

export async function POST(req: NextRequest) {
  try {
    const rl = checkRateLimit(req, "verify-otp", 5, 60_000);
    if (rl) return rl;

    const { email, code } = await req.json();

    if (!email || !code) {
      return Response.json({ error: "Email and code are required" }, { status: 400 });
    }

    const user = await prisma.adminUser.findUnique({
      where: { email, isActive: true },
    });

    if (!user) {
      return Response.json({ error: "Invalid code" }, { status: 403 });
    }

    const otp = await prisma.passwordOtp.findFirst({
      where: {
        userId: user.id,
        code,
        used: false,
        expiresAt: { gt: new Date() },
      },
      orderBy: { createdAt: "desc" },
    });

    if (!otp) {
      return Response.json(
        { error: "Invalid or expired code. Please request a new one." },
        { status: 403 }
      );
    }

    // Mark OTP as used
    await prisma.passwordOtp.update({
      where: { id: otp.id },
      data: { used: true },
    });

    // Return a reset token (the OTP id serves as a one-time reset token)
    return Response.json({ ok: true, resetToken: otp.id });
  } catch (error) {
    console.error("POST /api/admin/verify-otp error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

```