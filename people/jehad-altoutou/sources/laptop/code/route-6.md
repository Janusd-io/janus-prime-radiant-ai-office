---
type: source
source_type: laptop
title: route
slug: route-6
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/api/easter/claim/route.ts
original_size: 2562
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---

# route

_Extracted from `[[assessify|assessify]]/src/app/api/easter/claim/route.ts` on 2026-05-14._

```typescript
import { NextRequest } from "next/server";
import { prisma } from "@/lib/db";
import { validateEgg, EGGS } from "@/lib/easter-eggs";

export async function GET(req: NextRequest) {
  const email = new URL(req.url).searchParams.get("email");
  if (!email) {
    return Response.json({ error: "email query param is required" }, { status: 400 });
  }

  const claims = await prisma.easterEggClaim.findMany({
    where: { candidateEmail: email },
    select: { eggId: true, claimedAt: true },
  });

  return Response.json({ claims });
}

export async function POST(req: NextRequest) {
  try {
    const body = await req.json();
    const { egg, candidateName, candidateEmail, sessionId } = body as {
      egg: string;
      candidateName: string;
      candidateEmail: string;
      sessionId?: string;
    };

    if (!egg || !candidateName || !candidateEmail) {
      return Response.json(
        { error: "egg, candidateName, and candidateEmail are required" },
        { status: 400 }
      );
    }

    const eggId = validateEgg(egg);
    if (!eggId) {
      return Response.json(
        { "❌": "That's not a valid egg. Keep searching." },
        { status: 400 }
      );
    }

    // Check if already claimed
    const existing = await prisma.easterEggClaim.findUnique({
      where: { candidateEmail_eggId: { candidateEmail, eggId } },
    });

    if (existing) {
      return Response.json({
        "🥚": "You've already claimed this egg!",
        egg: eggId,
        name: EGGS[eggId].name,
        claimedAt: existing.claimedAt,
      });
    }

    const claim = await prisma.easterEggClaim.create({
      data: {
        sessionId: sessionId ?? null,
        candidateName,
        candidateEmail,
        eggId,
        eggValue: egg,
        ipAddress:
          req.headers.get("x-forwarded-for") ??
          req.headers.get("x-real-ip") ??
          null,
        userAgent: req.headers.get("user-agent") ?? null,
      },
    });

    const eggDef = EGGS[eggId];

    return Response.json({
      "🎉": `Congratulations! You found "${eggDef.name}"!`,
      egg: eggId,
      difficulty: eggDef.difficulty,
      claimedAt: claim.claimedAt,
      message:
        eggId === "egg_4"
          ? "You found the impossible egg. You are truly one of a kind. The hiring team has been notified."
          : "Your discovery has been recorded. Can you find them all?",
    });
  } catch (error) {
    console.error("POST /api/easter/claim error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

```