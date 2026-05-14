---
type: source
source_type: laptop
title: Assessify — route
slug: route-17
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/api/health/route.ts
original_size: 750
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# route

_Extracted from `[[assessify|assessify]]/src/app/api/health/route.ts` on 2026-05-14._

```typescript
import { prisma } from "@/lib/db";

export const dynamic = "force-dynamic";

/**
 * Liveness + DB readiness probe. Used by:
 *  - Docker healthcheck (container marked unhealthy if this fails)
 *  - External uptime monitors (UptimeRobot, BetterStack, etc.)
 *
 * Returns 200 only if the DB responds. Never leaks internals.
 */
export async function GET() {
  const start = Date.now();
  try {
    await prisma.$queryRaw`SELECT 1`;
    return Response.json(
      { ok: true, uptime: process.uptime(), db_ms: Date.now() - start },
      { headers: { "Cache-Control": "no-store" } }
    );
  } catch {
    return Response.json(
      { ok: false, db_ms: Date.now() - start },
      { status: 503, headers: { "Cache-Control": "no-store" } }
    );
  }
}

```