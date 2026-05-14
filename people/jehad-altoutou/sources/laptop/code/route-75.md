---
type: source
source_type: laptop
title: route
slug: route-75
created: 2026-04-23
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Dubai-Property-Leads/src/app/api/webhook/stripe/route.ts
original_size: 2960
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
---

# route

_Extracted from `Desktop/Claude Projects/Dubai-Property-Leads/src/app/api/webhook/stripe/route.ts` on 2026-05-14._

```typescript
import { NextRequest, NextResponse } from 'next/server';
import { stripe } from '@/lib/stripe';
import { prisma } from '@/lib/prisma';
import { allocateLeads, generateLeadsCsv } from '@/lib/leads';
import { sendLeadEmail } from '@/lib/email';
import Stripe from 'stripe';

const endpointSecret = process.env.STRIPE_WEBHOOK_SECRET;

export async function POST(req: NextRequest) {
  const payload = await req.text();
  const sig = req.headers.get('stripe-signature');

  let event: Stripe.Event;

  try {
    if (!sig || !endpointSecret) {
      throw new Error('Missing stripe signature or endpoint secret');
    }
    event = stripe.webhooks.constructEvent(payload, sig, endpointSecret);
  } catch (err: any) {
    console.error('Webhook signature verification failed:', err.message);
    return NextResponse.json({ error: `Webhook Error: ${err.message}` }, { status: 400 });
  }

  // Handle the event
  if (event.type === 'checkout.session.completed') {
    const session = event.data.object as Stripe.Checkout.Session;
    
    const customerEmail = session.customer_details?.email;
    const packageId = session.metadata?.packageId;
    const leadsCount = parseInt(session.metadata?.leadsCount || '0');

    if (!customerEmail || !packageId || leadsCount === 0) {
      console.error('Missing required metadata in stripe session', session.id);
      return NextResponse.json({ error: 'Missing metadata' }, { status: 400 });
    }

    try {
      // 1. Log the purchase
      const purchase = await prisma.purchase.create({
        data: {
          stripeSessionId: session.id,
          customerEmail,
          packageId,
          leadsCount,
          amountTotal: session.amount_total || 0,
          currency: session.currency || 'aed',
          status: 'completed',
        },
      });

      // 2. Allocate Leads
      const leads = await allocateLeads(leadsCount);

      // 3. Generate CSV
      const csvContent = generateLeadsCsv(leads);

      // 4. Send Email
      await sendLeadEmail(customerEmail, csvContent, packageId.charAt(0).toUpperCase() + packageId.slice(1));

      // 5. Update purchase with CSV status (optional, here we just finish)
      await prisma.systemLog.create({
        data: {
          level: 'info',
          message: `Successfully processed purchase ${purchase.id} for ${customerEmail}. Delivered ${leads.length} leads.`,
        },
      });

    } catch (error: any) {
      console.error('Error processing successful payment:', error);
      await prisma.systemLog.create({
        data: {
          level: 'error',
          message: `Failed to process successful payment for session ${session.id}: ${error.message}`,
          payload: { error: error.stack },
        },
      });
      // We return 200 anyway to Stripe to avoid retries if the payment was successful 
      // but our delivery failed (we'll handle delivery manually from logs)
    }
  }

  return NextResponse.json({ received: true });
}

```