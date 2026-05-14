---
type: source
source_type: laptop
title: route
slug: route-78
created: 2026-04-23
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Dubai-Property-Leads/src/app/api/admin/auth/login/route.ts
original_size: 1966
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
---

# route

_Extracted from `Desktop/Claude Projects/Dubai-Property-Leads/src/app/api/admin/auth/login/route.ts` on 2026-05-14._

```typescript
import { NextResponse } from 'next/server';
import crypto from 'crypto';
import { signAdminToken } from '@/lib/proposals-auth';

// Simple in-memory rate limiter: max 10 attempts per IP per 15 minutes
const loginAttempts = new Map<string, { count: number; resetAt: number }>();

function isRateLimited(ip: string): boolean {
  const now = Date.now();
  const record = loginAttempts.get(ip);
  if (!record || now > record.resetAt) {
    loginAttempts.set(ip, { count: 1, resetAt: now + 15 * 60 * 1000 });
    return false;
  }
  record.count++;
  return record.count > 10;
}

export async function POST(request: Request) {
  const ip = request.headers.get('x-forwarded-for') ?? 'unknown';

  if (isRateLimited(ip)) {
    return NextResponse.json({ error: 'Too many attempts. Try again later.' }, { status: 429 });
  }

  let body: { password?: string };
  try {
    body = await request.json();
  } catch {
    return NextResponse.json({ error: 'Invalid request' }, { status: 400 });
  }

  const adminPassword = process.env.PROPOSALS_ADMIN_PASSWORD;
  if (!adminPassword) {
    return NextResponse.json({ error: 'Admin not configured' }, { status: 503 });
  }

  const inputPassword = (body.password ?? '').trim();
  if (!inputPassword) {
    return NextResponse.json({ error: 'Password required' }, { status: 400 });
  }

  // Constant-time comparison
  const inputBuf = Buffer.from(inputPassword);
  const adminBuf = Buffer.from(adminPassword);
  const equal =
    inputBuf.length === adminBuf.length &&
    crypto.timingSafeEqual(inputBuf, adminBuf);

  if (!equal) {
    return NextResponse.json({ error: 'Invalid password' }, { status: 401 });
  }

  const token = await signAdminToken();

  const response = NextResponse.json({ ok: true });
  response.cookies.set('admin_session', token, {
    httpOnly: true,
    secure: process.env.NODE_ENV === 'production',
    sameSite: 'lax',
    path: '/',
    maxAge: 60 * 60 * 8, // 8 hours
  });
  return response;
}

```