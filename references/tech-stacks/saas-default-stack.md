---
type: stack
tags: [stack, saas, backend]
---

# SaaS Default Stack

Used by [[scaffold|/scaffold]] and [[saas-architect|/saas-architect]].

## Core
- **Framework**: Next.js 15+ App Router + TypeScript
- **Styling**: Tailwind CSS + [[design-systems|shadcn/ui]]
- **Database**: Neon Postgres + Drizzle ORM
- **Auth**: Clerk (Vercel Marketplace)
- **Payments**: Stripe
- **Email**: Resend
- **Cache**: Upstash Redis
- **Workflows**: n8n (webhook-connected) → see [[n8n-workflow|/n8n-workflow]]
- **Hosting**: Vercel

## Related Skills
- [[scaffold|/scaffold]]
- [[saas-architect|/saas-architect]]
- [[api-design|/api-design]]
- [[database-optimize|/database-optimize]]
- [[deploy|/deploy]]

## Patterns
See [[saas-engineering-patterns|SaaS Engineering Patterns]] for stack-agnostic architecture/UI patterns (metadata-driven objects, multi-tenancy, token theme, RBAC) distilled from [[twenty-crm|Twenty CRM]].

## Build Kit
To actually build a high-end SaaS on this stack, follow [[saas-blueprint-guide|🏗️ SaaS Blueprint]] — paste-ready tokens, folder skeleton, and code recipes (multi-tenancy, RBAC, event backbone, metadata objects, pagination) distilled from [[twenty-crm|Twenty CRM]].
