---
type: source
source_type: laptop
title: leads
slug: leads
created: 2026-04-23
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Dubai-Property-Leads/src/lib/leads.ts
original_size: 2009
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---
<!-- jb:project-callout -->
> Part of [[desktop-captures|Desktop Captures]] — automatically linked by /janus-brain.


# leads

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Claude Projects/Dubai-Property-Leads/src/lib/leads.ts` on 2026-05-14._

```typescript
import { prisma } from './prisma';
import Papa from 'papaparse';

/**
 * Allocates leads from the database for a purchase.
 * Strategy: Newest available leads first.
 */
export const allocateLeads = async (count: number) => {
  // Use a transaction to ensure we don't over-allocate or have race conditions
  return await prisma.$transaction(async (tx: any) => {
    // 1. Select available leads
    // Note: In a production system with high concurrency, you might use 
    // SELECT FOR UPDATE or a more complex queueing system.
    const leads = await tx.lead.findMany({
      where: {
        status: 'available',
      },
      orderBy: {
        timestamp: 'desc',
      },
      take: count,
    });

    if (leads.length < count) {
      // Log warning or throw error if not enough leads
      await tx.systemLog.create({
        data: {
          level: 'warning',
          message: `Attempted to allocate ${count} leads but only ${leads.length} available.`,
        },
      });
      // We might still deliver what we have, or stop. Requirement says 
      // "If a lead contains invalid contact information, it will be replaced."
      // For now, we'll deliver what we have and notify.
    }

    // 2. Update delivered_count and status
    const leadIds = leads.map((l: any) => l.id);
    
    await tx.lead.updateMany({
      where: {
        id: { in: leadIds },
      },
      data: {
        deliveredCount: { increment: 1 },
        lastDeliveredAt: new Date(),
        status: 'delivered', // For this simple MVP, we mark as delivered once.
      },
    });

    return leads;
  });
};

export const generateLeadsCsv = (leads: any[]) => {
  const data = leads.map((l: any) => ({
    'Full Name': l.name,
    'Phone Number': l.phone,
    'Email': l.email,
    'Nationality': l.nationality,
    'Buyer Budget': l.budget,
    'Property Type Interest': l.propertyType,
    'Inquiry Message': l.inquiryMessage,
    'Timestamp': l.timestamp.toISOString(),
  }));

  return Papa.unparse(data);
};

```