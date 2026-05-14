---
type: source
source_type: laptop
title: Desktop Captures — route
slug: route-80
created: 2026-04-23
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: "/Users/jehad/Desktop/Claude Projects/Dubai-Property-Leads/src/app/api/admin/proposals/[id]/route.ts"
original_size: 3746
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

_Extracted from `Desktop/Claude Projects/Dubai-Property-Leads/src/app/api/admin/proposals/[id]/route.ts` on 2026-05-14._

```typescript
import { NextResponse } from 'next/server';
import { cookies } from 'next/headers';
import { prisma } from '@/lib/prisma';
import { verifyAdminToken } from '@/lib/proposals-auth';

async function requireAdmin() {
  const jar = await cookies();
  const token = jar.get('admin_session')?.value;
  if (!token) throw new Error('Unauthorized');
  await verifyAdminToken(token);
}

// GET /api/admin/proposals/[id] — fetch single proposal
export async function GET(_req: Request, { params }: { params: Promise<{ id: string }> }) {
  try {
    await requireAdmin();
  } catch {
    return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
  }

  const { id } = await params;
  const client = await prisma.proposalClient.findUnique({
    where: { id },
    include: { proposal: true },
  });

  if (!client) return NextResponse.json({ error: 'Not found' }, { status: 404 });
  return NextResponse.json(client);
}

// PUT /api/admin/proposals/[id] — update proposal
export async function PUT(request: Request, { params }: { params: Promise<{ id: string }> }) {
  try {
    await requireAdmin();
  } catch {
    return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
  }

  const { id } = await params;

  let body: Record<string, unknown>;
  try {
    body = await request.json();
  } catch {
    return NextResponse.json({ error: 'Invalid JSON' }, { status: 400 });
  }

  const existing = await prisma.proposalClient.findUnique({ where: { id }, include: { proposal: true } });
  if (!existing) return NextResponse.json({ error: 'Not found' }, { status: 404 });

  const clientUpdate: Record<string, unknown> = {};
  if (body.companyName !== undefined) clientUpdate.companyName = (body.companyName as string).trim();
  if (body.contactName !== undefined) clientUpdate.contactName = (body.contactName as string).trim();
  if (body.email !== undefined) clientUpdate.email = (body.email as string).trim().toLowerCase();
  if (body.role !== undefined) clientUpdate.role = (body.role as string)?.trim() || null;
  if (body.phone !== undefined) clientUpdate.phone = (body.phone as string)?.trim() || null;
  if (body.website !== undefined) clientUpdate.website = (body.website as string)?.trim() || null;
  if (body.officeAddress !== undefined) clientUpdate.officeAddress = (body.officeAddress as string)?.trim() || null;
  if (body.notes !== undefined) clientUpdate.notes = (body.notes as string)?.trim() || null;
  if (body.status !== undefined) clientUpdate.status = body.status;
  if (body.meetingDate !== undefined) clientUpdate.meetingDate = body.meetingDate ? new Date(body.meetingDate as string) : null;

  const proposalUpdate: Record<string, unknown> = {};
  if (body.packageVolume !== undefined) proposalUpdate.packageVolume = body.packageVolume ? Number(body.packageVolume) : null;
  if (body.pricingNotes !== undefined) proposalUpdate.pricingNotes = (body.pricingNotes as string)?.trim() || null;
  if (body.pricingDisplay !== undefined) proposalUpdate.pricingDisplay = (body.pricingDisplay as string)?.trim() || null;
  if (body.discoveryNotes !== undefined) proposalUpdate.discoveryNotes = (body.discoveryNotes as string)?.trim() || null;
  if (body.ctaMessage !== undefined) proposalUpdate.ctaMessage = (body.ctaMessage as string)?.trim() || null;
  if (body.proposalStatus !== undefined) proposalUpdate.status = body.proposalStatus;

  const [updatedClient] = await prisma.$transaction([
    prisma.proposalClient.update({ where: { id }, data: clientUpdate, include: { proposal: true } }),
    ...(Object.keys(proposalUpdate).length > 0 && existing.proposal
      ? [prisma.proposalData.update({ where: { clientId: id }, data: proposalUpdate })]
      : []),
  ]);

  return NextResponse.json(updatedClient);
}

```