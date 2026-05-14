---
type: source
source_type: laptop
title: route
slug: route-83
created: 2026-04-23
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Dubai-Property-Leads/src/app/api/proposals/auth/login/route.ts
original_size: 2140
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---

# route

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Claude Projects/Dubai-Property-Leads/src/app/api/proposals/auth/login/route.ts` on 2026-05-14._

```typescript
import { NextResponse } from 'next/server';
import { prisma } from '@/lib/prisma';
import { signProposalToken } from '@/lib/proposals-auth';
import bcrypt from 'bcryptjs';

// In-memory rate limiter: max 8 attempts per IP per 10 minutes
const loginAttempts = new Map<string, { count: number; resetAt: number }>();

function isRateLimited(ip: string): boolean {
  const now = Date.now();
  const record = loginAttempts.get(ip);
  if (!record || now > record.resetAt) {
    loginAttempts.set(ip, { count: 1, resetAt: now + 10 * 60 * 1000 });
    return false;
  }
  record.count++;
  return record.count > 8;
}

export async function POST(request: Request) {
  const ip = request.headers.get('x-forwarded-for') ?? 'unknown';

  if (isRateLimited(ip)) {
    return NextResponse.json({ error: 'Too many attempts. Try again in 10 minutes.' }, { status: 429 });
  }

  let body: { email?: string; password?: string };
  try {
    body = await request.json();
  } catch {
    return NextResponse.json({ error: 'Invalid request' }, { status: 400 });
  }

  const email = (body.email ?? '').trim().toLowerCase();
  const password = (body.password ?? '').trim();

  if (!email || !password) {
    return NextResponse.json({ error: 'Email and password are required' }, { status: 400 });
  }

  const client = await prisma.proposalClient.findUnique({ where: { email } });

  // Always run bcrypt to prevent timing-based enumeration
  const dummyHash = '$2a$12$00000000000000000000000000000000000000000000000000000u';
  const hashToCompare = client?.passwordHash ?? dummyHash;
  const passwordValid = await bcrypt.compare(password, hashToCompare);

  if (!client || !passwordValid || client.status !== 'active') {
    return NextResponse.json({ error: 'Invalid credentials' }, { status: 401 });
  }

  const token = await signProposalToken(client.slug, client.id);

  const response = NextResponse.json({ slug: client.slug });
  response.cookies.set('proposal_session', token, {
    httpOnly: true,
    secure: process.env.NODE_ENV === 'production',
    sameSite: 'lax',
    path: '/',
    maxAge: 60 * 60 * 24 * 7, // 7 days
  });
  return response;
}

```