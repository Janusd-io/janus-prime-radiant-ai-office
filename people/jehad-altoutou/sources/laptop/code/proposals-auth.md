---
type: source
source_type: laptop
title: proposals-auth
slug: proposals-auth
created: 2026-04-23
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Dubai-Property-Leads/src/lib/proposals-auth.ts
original_size: 1246
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---

# proposals-auth

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Claude Projects/Dubai-Property-Leads/src/lib/proposals-auth.ts` on 2026-05-14._

```typescript
import { SignJWT, jwtVerify } from 'jose';

function getSecret() {
  const secret = process.env.PROPOSALS_JWT_SECRET;
  if (!secret) throw new Error('PROPOSALS_JWT_SECRET env var is not set');
  return new TextEncoder().encode(secret);
}

export async function signProposalToken(slug: string, clientId: string): Promise<string> {
  return new SignJWT({ slug, clientId, type: 'proposal' })
    .setProtectedHeader({ alg: 'HS256' })
    .setIssuedAt()
    .setExpirationTime('7d')
    .sign(getSecret());
}

export async function verifyProposalToken(token: string): Promise<{ slug: string; clientId: string }> {
  const { payload } = await jwtVerify(token, getSecret());
  if (payload.type !== 'proposal') throw new Error('Invalid token type');
  return { slug: payload.slug as string, clientId: payload.clientId as string };
}

export async function signAdminToken(): Promise<string> {
  return new SignJWT({ type: 'admin' })
    .setProtectedHeader({ alg: 'HS256' })
    .setIssuedAt()
    .setExpirationTime('8h')
    .sign(getSecret());
}

export async function verifyAdminToken(token: string): Promise<void> {
  const { payload } = await jwtVerify(token, getSecret());
  if (payload.type !== 'admin') throw new Error('Invalid admin token');
}

```