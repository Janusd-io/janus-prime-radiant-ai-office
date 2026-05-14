---
type: source
source_type: laptop
title: rate-limit
slug: rate-limit
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/lib/rate-limit.ts
original_size: 2072
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---

# rate-limit

_Extracted from `[[assessify|assessify]]/src/lib/rate-limit.ts` on 2026-05-14._

```typescript
// Simple in-memory sliding-window rate limiter.
// No external dependencies — works for single-instance Docker deployments.

const store = new Map<string, number[]>();

// Clean old entries every 5 minutes
setInterval(() => {
  const now = Date.now();
  for (const [key, timestamps] of store) {
    const valid = timestamps.filter((t) => now - t < 60_000);
    if (valid.length === 0) store.delete(key);
    else store.set(key, valid);
  }
}, 300_000);

/**
 * Check if a request should be rate-limited.
 * @param key   Unique identifier (e.g. IP + route)
 * @param limit Max requests allowed in the window
 * @param windowMs Window size in milliseconds (default 60s)
 * @returns { limited: boolean, remaining: number, retryAfterMs: number }
 */
export function rateLimit(
  key: string,
  limit: number,
  windowMs = 60_000
): { limited: boolean; remaining: number; retryAfterMs: number } {
  const now = Date.now();
  const timestamps = (store.get(key) ?? []).filter((t) => now - t < windowMs);

  if (timestamps.length >= limit) {
    const oldest = timestamps[0];
    return { limited: true, remaining: 0, retryAfterMs: windowMs - (now - oldest) };
  }

  timestamps.push(now);
  store.set(key, timestamps);
  return { limited: false, remaining: limit - timestamps.length, retryAfterMs: 0 };
}

/** Helper to get client IP from request headers */
export function getClientIp(req: Request): string {
  const forwarded = req.headers.get("x-forwarded-for");
  if (forwarded) return forwarded.split(",")[0].trim();
  return "unknown";
}

/** Returns a 429 Response if limited, or null if allowed */
export function checkRateLimit(req: Request, route: string, limit = 10, windowMs = 60_000): Response | null {
  const ip = getClientIp(req);
  const { limited, retryAfterMs } = rateLimit(`${ip}:${route}`, limit, windowMs);
  if (limited) {
    return Response.json(
      { error: "Too many requests. Please try again later." },
      {
        status: 429,
        headers: { "Retry-After": String(Math.ceil(retryAfterMs / 1000)) },
      }
    );
  }
  return null;
}

```