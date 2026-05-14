---
type: source
source_type: laptop
title: Assessify — auth
slug: auth
created: 2026-05-01
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/lib/auth.ts
original_size: 2734
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# auth

_Extracted from `[[assessify|assessify]]/src/lib/auth.ts` on 2026-05-14._

```typescript
import { cookies } from "next/headers";
import { createHmac } from "crypto";
import { prisma } from "@/lib/db";
import { redirect } from "next/navigation";

const SESSION_COOKIE = "assessify_admin_session";
const SESSION_MAX_AGE = 60 * 60 * 24; // 24 hours

// Secret for HMAC signing — falls back to a generated one on first boot
function getSecret(): string {
  if (process.env.SESSION_SECRET) return process.env.SESSION_SECRET;
  // Deterministic fallback so existing sessions survive restarts
  return "assessify_default_secret_change_in_production_" + (process.env.DATABASE_URL ?? "");
}

// HMAC-signed token: base64url(userId:timestamp:random).signature
function generateToken(userId: string): string {
  const payload = `${userId}:${Date.now()}:${Math.random().toString(36).slice(2)}`;
  const encoded = Buffer.from(payload).toString("base64url");
  const sig = createHmac("sha256", getSecret()).update(encoded).digest("base64url");
  return `${encoded}.${sig}`;
}

function parseToken(token: string): { userId: string; timestamp: number } | null {
  try {
    const [encoded, sig] = token.split(".");
    if (!encoded || !sig) return null;

    // Verify HMAC signature
    const expected = createHmac("sha256", getSecret()).update(encoded).digest("base64url");
    if (sig !== expected) return null;

    const decoded = Buffer.from(encoded, "base64url").toString();
    const [userId, ts] = decoded.split(":");
    const timestamp = parseInt(ts, 10);
    if (!userId || isNaN(timestamp)) return null;
    if (Date.now() - timestamp > SESSION_MAX_AGE * 1000) return null;
    return { userId, timestamp };
  } catch {
    return null;
  }
}

export async function createSession(userId: string) {
  const token = generateToken(userId);
  const cookieStore = await cookies();
  cookieStore.set(SESSION_COOKIE, token, {
    httpOnly: true,
    secure: process.env.NODE_ENV === "production",
    sameSite: "lax",
    maxAge: SESSION_MAX_AGE,
    path: "/",
  });
  return token;
}

export async function destroySession() {
  const cookieStore = await cookies();
  cookieStore.delete(SESSION_COOKIE);
}

export async function getSession() {
  const cookieStore = await cookies();
  const token = cookieStore.get(SESSION_COOKIE)?.value;
  if (!token) return null;

  const parsed = parseToken(token);
  if (!parsed) return null;

  const user = await prisma.adminUser.findUnique({
    where: { id: parsed.userId, isActive: true },
    select: {
      id: true,
      email: true,
      name: true,
      role: true,
      office: true,
      scopedDepartments: true,
    },
  });

  return user;
}

export async function requireAuth() {
  const user = await getSession();
  if (!user) redirect("/admin/login");
  return user;
}

```