---
type: source
source_type: laptop
title: route
slug: route-5
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/api/easter/hints/route.ts
original_size: 1340
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# route

_Extracted from `assessify/src/app/api/easter/hints/route.ts` on 2026-05-14._

```typescript
import { NextRequest } from "next/server";
import { prisma } from "@/lib/db";
import { EGGS, getHint, type EggId } from "@/lib/easter-eggs";

export async function GET(req: NextRequest) {
  const url = new URL(req.url);
  const eggId = url.searchParams.get("egg") as EggId | null;
  const email = url.searchParams.get("email");

  if (!eggId) {
    return Response.json(
      { error: "egg query param is required" },
      { status: 400 }
    );
  }

  if (!(eggId in EGGS)) {
    return Response.json({ error: "Unknown egg" }, { status: 404 });
  }

  const egg = EGGS[eggId];

  // Egg 4 gets no hints
  if (eggId === "egg_4") {
    return Response.json({
      egg: eggId,
      difficulty: egg.difficulty,
      hint: null,
      message: "No hints available for this challenge.",
    });
  }

  // Determine hint level based on how many eggs the candidate has already found
  const claimedCount = email
    ? await prisma.easterEggClaim.count({ where: { candidateEmail: email } })
    : 0;

  // More eggs found = harder hints (start at level 0, max at hints.length-1)
  const hintLevel = Math.min(claimedCount, egg.hints.length - 1);
  const hint = getHint(eggId, hintLevel);

  return Response.json({
    egg: eggId,
    difficulty: egg.difficulty,
    hintLevel: hintLevel + 1,
    totalHints: egg.hints.length,
    hint,
  });
}

```