---
type: source
source_type: laptop
title: Desktop Captures — route
slug: route-79
created: 2026-04-23
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Dubai-Property-Leads/src/app/api/admin/proposals/route.ts
original_size: 3425
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---
<!-- jb:project-callout -->
> Part of [[desktop-captures|Desktop Captures]] — automatically linked by /janus-brain.


# route

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Claude Projects/Dubai-Property-Leads/src/app/api/admin/proposals/route.ts` on 2026-05-14._

```typescript
import { NextResponse } from 'next/server';
import { cookies } from 'next/headers';
import { prisma } from '@/lib/prisma';
import { verifyAdminToken } from '@/lib/proposals-auth';
import bcrypt from 'bcryptjs';
import crypto from 'crypto';

async function requireAdmin() {
  const jar = await cookies();
  const token = jar.get('admin_session')?.value;
  if (!token) throw new Error('Unauthorized');
  await verifyAdminToken(token);
}

function generatePassword(length = 16): string {
  return crypto.randomBytes(length).toString('base64url').slice(0, length);
}

function slugify(text: string): string {
  return text
    .toLowerCase()
    .replace(/[^a-z0-9\s-]/g, '')
    .trim()
    .replace(/\s+/g, '-')
    .replace(/-+/g, '-');
}

// GET /api/admin/proposals — list all proposal clients
export async function GET() {
  try {
    await requireAdmin();
  } catch {
    return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
  }

  const clients = await prisma.proposalClient.findMany({
    orderBy: { createdAt: 'desc' },
    include: { proposal: true },
  });

  return NextResponse.json(clients);
}

// POST /api/admin/proposals — create a new proposal client
export async function POST(request: Request) {
  try {
    await requireAdmin();
  } catch {
    return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
  }

  let body: Record<string, unknown>;
  try {
    body = await request.json();
  } catch {
    return NextResponse.json({ error: 'Invalid JSON' }, { status: 400 });
  }

  const companyName = (body.companyName as string)?.trim();
  const contactName = (body.contactName as string)?.trim();
  const email = (body.email as string)?.trim().toLowerCase();

  if (!companyName || !contactName || !email) {
    return NextResponse.json({ error: 'companyName, contactName, and email are required' }, { status: 400 });
  }

  // Generate slug from company name, make unique
  const baseSlug = slugify(companyName);
  let slug = baseSlug;
  let suffix = 1;
  while (await prisma.proposalClient.findUnique({ where: { slug } })) {
    slug = `${baseSlug}-${suffix++}`;
  }

  const plainPassword = generatePassword();
  const passwordHash = await bcrypt.hash(plainPassword, 12);

  const meetingDate = body.meetingDate ? new Date(body.meetingDate as string) : null;

  const client = await prisma.proposalClient.create({
    data: {
      companyName,
      contactName,
      email,
      passwordHash,
      role: (body.role as string)?.trim() || null,
      phone: (body.phone as string)?.trim() || null,
      website: (body.website as string)?.trim() || null,
      officeAddress: (body.officeAddress as string)?.trim() || null,
      slug,
      notes: (body.notes as string)?.trim() || null,
      meetingDate,
      status: 'active',
      proposal: {
        create: {
          packageVolume: body.packageVolume ? Number(body.packageVolume) : null,
          pricingNotes: (body.pricingNotes as string)?.trim() || null,
          pricingDisplay: (body.pricingDisplay as string)?.trim() || null,
          discoveryNotes: (body.discoveryNotes as string)?.trim() || null,
          ctaMessage: (body.ctaMessage as string)?.trim() || null,
          status: 'published',
        },
      },
    },
    include: { proposal: true },
  });

  // Return the plain password once — it is never stored
  return NextResponse.json({ client, plainPassword }, { status: 201 });
}

```