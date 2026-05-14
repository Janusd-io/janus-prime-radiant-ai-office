---
type: source
source_type: laptop
title: proxy
slug: proxy
created: 2026-04-23
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Dubai-Property-Leads/src/proxy.ts
original_size: 1832
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
---

# proxy

_Extracted from `Desktop/Claude Projects/Dubai-Property-Leads/src/proxy.ts` on 2026-05-14._

```typescript
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';
import { jwtVerify } from 'jose';

function getSecret() {
  const secret = process.env.PROPOSALS_JWT_SECRET;
  if (!secret) return null;
  return new TextEncoder().encode(secret);
}

export async function proxy(request: NextRequest) {
  const { pathname } = request.nextUrl;
  const secret = getSecret();

  // Protect admin routes — exempt /admin/login
  if (pathname.startsWith('/admin') && pathname !== '/admin/login') {
    const token = request.cookies.get('admin_session')?.value;
    if (!token || !secret) {
      return NextResponse.redirect(new URL('/admin/login', request.url));
    }
    try {
      const { payload } = await jwtVerify(token, secret);
      if (payload.type !== 'admin') throw new Error();
    } catch {
      const res = NextResponse.redirect(new URL('/admin/login', request.url));
      res.cookies.delete('admin_session');
      return res;
    }
  }

  // Protect /proposals/[slug] — exempt /proposals/login
  if (pathname.startsWith('/proposals/') && pathname !== '/proposals/login') {
    const slug = pathname.split('/')[2];
    if (!slug) return NextResponse.next();

    const token = request.cookies.get('proposal_session')?.value;
    if (!token || !secret) {
      return NextResponse.redirect(new URL('/proposals/login', request.url));
    }
    try {
      const { payload } = await jwtVerify(token, secret);
      if (payload.type !== 'proposal' || payload.slug !== slug) {
        throw new Error();
      }
    } catch {
      const res = NextResponse.redirect(new URL('/proposals/login', request.url));
      res.cookies.delete('proposal_session');
      return res;
    }
  }

  return NextResponse.next();
}

export const config = {
  matcher: ['/admin/:path*', '/proposals/:path*'],
};

```