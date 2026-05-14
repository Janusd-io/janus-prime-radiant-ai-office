---
type: source
source_type: laptop
title: route
slug: route-81
created: 2026-04-23
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Dubai-Property-Leads/src/app/api/checkout/route.ts
original_size: 1581
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
---

# route

_Extracted from `Desktop/Claude Projects/Dubai-Property-Leads/src/app/api/checkout/route.ts` on 2026-05-14._

```typescript
import { NextRequest, NextResponse } from 'next/server';
import { stripe, LEAD_PACKAGES } from '@/lib/stripe';
import { sendErrorReport } from '@/lib/email';

export async function POST(req: NextRequest) {
  let packageContext = 'unknown package';
  try {
    const { packageId } = await req.json();
    packageContext = packageId;
    const pkg = LEAD_PACKAGES.find((p) => p.id === packageId);

    if (!pkg || pkg.isEnterprise) {
      return NextResponse.json({ error: 'Invalid package' }, { status: 400 });
    }

    const session = await stripe.checkout.sessions.create({
      payment_method_types: ['card'],
      line_items: [
        {
          price_data: {
            currency: 'aed',
            product_data: {
              name: `${pkg.name} - ${pkg.leads} Verified Leads`,
              description: pkg.description,
            },
            unit_amount: pkg.price * 100, // Stripe expects amounts in fils/cents
          },
          quantity: 1,
        },
      ],
      mode: 'payment',
      success_url: `${req.nextUrl.origin}/success?session_id={CHECKOUT_SESSION_ID}`,
      cancel_url: `${req.nextUrl.origin}/#pricing`,
      metadata: {
        packageId: pkg.id,
        leadsCount: pkg.leads.toString(),
      },
    });

    return NextResponse.json({ url: session.url });
  } catch (err: any) {
    console.error('Stripe error:', err);
    
    // Trigger automated error report email to developer
    await sendErrorReport(err, `Checkout Attempt: ${packageContext}`);

    return NextResponse.json({ error: err.message }, { status: 500 });
  }
}

```