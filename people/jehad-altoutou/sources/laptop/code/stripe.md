---
type: source
source_type: laptop
title: stripe
slug: stripe
created: 2026-04-23
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Dubai-Property-Leads/src/lib/stripe.ts
original_size: 1381
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
---

# stripe

_Extracted from `Desktop/Claude Projects/Dubai-Property-Leads/src/lib/stripe.ts` on 2026-05-14._

```typescript
import Stripe from 'stripe';

if (!process.env.STRIPE_SECRET_KEY && process.env.NODE_ENV === 'production') {
  console.warn('Warning: STRIPE_SECRET_KEY is missing during production build.');
}

const stripeKey = process.env.STRIPE_SECRET_KEY || 'sk_test_mock_key';
export const stripe = new Stripe(stripeKey);

export const LEAD_PACKAGES = [
  {
    id: 'starter',
    name: 'Starter',
    leads: 25,
    price: 3750,
    pricePerLead: 150,
    description: 'Best for testing lead quality.',
    cta: 'Get Leads Now',
  },
  {
    id: 'growth',
    name: 'Growth',
    leads: 100,
    price: 13500,
    pricePerLead: 135,
    description: 'Save 1,500 AED compared to buying Starter packages.',
    cta: 'Reserve Leads Today',
    popular: true,
  },
  {
    id: 'pro',
    name: 'Pro',
    leads: 250,
    price: 31250,
    pricePerLead: 125,
    description: 'Best value for active brokers and serious agents.',
    cta: 'Start Receiving Leads',
  },
  {
    id: 'agency',
    name: 'Agency',
    leads: 600,
    price: 69000,
    pricePerLead: 115,
    description: 'Ideal for brokerages with larger sales teams.',
    cta: 'Start Receiving Leads',
  },
  {
    id: 'enterprise',
    name: 'Enterprise',
    leads: 2000,
    price: 0, // Custom
    pricePerLead: 0,
    description: 'Custom pricing for bulk enquiries.',
    cta: 'Contact Sales',
    isEnterprise: true,
  },
];

```