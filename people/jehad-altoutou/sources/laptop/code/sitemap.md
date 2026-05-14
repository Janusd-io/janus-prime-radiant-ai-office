---
type: source
source_type: laptop
title: sitemap
slug: sitemap
created: 2026-04-23
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Dubai-Property-Leads/src/app/sitemap.ts
original_size: 1033
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---
<!-- jb:project-callout -->
> Part of [[desktop-captures|Desktop Captures]] — automatically linked by /janus-brain.


# sitemap

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Claude Projects/Dubai-Property-Leads/src/app/sitemap.ts` on 2026-05-14._

```typescript
import { MetadataRoute } from 'next';

export default function sitemap(): MetadataRoute.Sitemap {
  const baseUrl = 'https://dubaipropertyleads.ae';
  
  const routes = [
    '',
    '/about',
    '/dubai-investor-leads',
    '/dubai-real-estate-leads',
    '/off-plan-leads-dubai',
    '/property-buyer-leads-dubai',
    '/where-to-buy-dubai-property-leads',
    '/blog/how-real-estate-agents-get-leads-in-dubai',
    '/blog/cost-of-real-estate-leads-dubai',
    '/blog/off-plan-property-leads-guide',
    '/blog/best-lead-generation-for-dubai-brokers',
    '/blog/top-new-off-plan-projects-dubai-2026',
    '/blog/best-dubai-property-leads-providers-2026',
    '/blog/are-paid-real-estate-leads-worth-it-dubai',
    '/blog/how-to-generate-leads-cheaper-than-property-finder-bayut',
    '/real-estate-api',
    '/real-estate-api/documentation',
  ];

  return routes.map((route) => ({
    url: `${baseUrl}${route}`,
    lastModified: new Date(),
    changeFrequency: 'daily' as const,
    priority: route === '' ? 1 : 0.8,
  }));
}

```