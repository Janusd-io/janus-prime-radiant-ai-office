---
type: source
source_type: laptop
title: page
slug: page-62
created: 2026-04-23
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: "/Users/jehad/Desktop/Claude Projects/Dubai-Property-Leads/src/app/proposals/[slug]/page.tsx"
original_size: 2579
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---
<!-- jb:project-callout -->
> Part of [[desktop-captures|Desktop Captures]] — automatically linked by /janus-brain.


# page

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Claude Projects/Dubai-Property-Leads/src/app/proposals/[slug]/page.tsx` on 2026-05-14._

```tsx
import { cookies } from 'next/headers';
import { notFound, redirect } from 'next/navigation';
import { prisma } from '@/lib/prisma';
import { verifyProposalToken } from '@/lib/proposals-auth';
import ProposalContent from '@/components/proposals/ProposalContent';
import type { ProposalClientRecord } from '@/types/proposals';

interface PageProps {
  params: Promise<{ slug: string }>;
}

export const dynamic = 'force-dynamic';

export default async function ProposalPage({ params }: PageProps) {
  const { slug } = await params;

  // Verify session — middleware already checked, but we validate here too
  const jar = await cookies();
  const token = jar.get('proposal_session')?.value;

  if (!token) {
    redirect('/proposals/login');
  }

  let tokenPayload: { slug: string; clientId: string };
  try {
    tokenPayload = await verifyProposalToken(token);
  } catch {
    redirect('/proposals/login');
  }

  // Enforce that the token slug matches the requested slug
  if (tokenPayload.slug !== slug) {
    redirect('/proposals/login');
  }

  const client = await prisma.proposalClient.findUnique({
    where: { slug },
    include: { proposal: true },
  });

  if (!client || client.status !== 'active') {
    notFound();
  }

  // Verify token clientId matches db record (defense in depth)
  if (client.id !== tokenPayload.clientId) {
    redirect('/proposals/login');
  }

  // Strip passwordHash before passing to client component
  const safeClient: ProposalClientRecord = {
    id: client.id,
    companyName: client.companyName,
    contactName: client.contactName,
    email: client.email,
    role: client.role,
    phone: client.phone,
    website: client.website,
    officeAddress: client.officeAddress,
    slug: client.slug,
    status: client.status,
    notes: client.notes,
    meetingDate: client.meetingDate,
    createdAt: client.createdAt,
    proposal: client.proposal
      ? {
          id: client.proposal.id,
          clientId: client.proposal.clientId,
          packageVolume: client.proposal.packageVolume,
          pricingNotes: client.proposal.pricingNotes,
          pricingDisplay: client.proposal.pricingDisplay,
          customSections: client.proposal.customSections as Record<string, unknown> | null,
          discoveryNotes: client.proposal.discoveryNotes,
          ctaMessage: client.proposal.ctaMessage,
          status: client.proposal.status,
          createdAt: client.proposal.createdAt,
          updatedAt: client.proposal.updatedAt,
        }
      : null,
  };

  return <ProposalContent client={safeClient} />;
}

```