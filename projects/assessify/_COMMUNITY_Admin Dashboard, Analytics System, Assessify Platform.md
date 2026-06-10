---
type: community
cohesion: 0.12
members: 20
---

# Admin Dashboard, Analytics System, Assessify Platform

**Cohesion:** 0.12 - loosely connected
**Members:** 20 nodes

## Members
- [[Admin  HR Role]] - document - SOP.md
- [[Admin Dashboard]] - document - README.md
- [[Analytics System]] - document - SOP.md
- [[assessify]] - document - README.md
- [[Assessment Engine]] - document - README.md
- [[Candidate Invite System]] - document - SOP.md
- [[Candidate Role]] - document - SOP.md
- [[Custom Auth (bcryptjs + HMAC JWT)]] - document - SOP.md
- [[Docker Volume (assessify_data)]] - document - README.md
- [[Easter Egg System]] - document - SOP.md
- [[Email Delivery (Resend)]] - document - SOP.md
- [[Question Bank]] - document - SOP.md
- [[Recommendation Bands (Strong Hire to Reject)]] - document - SOP.md
- [[Scoring Engine]] - document - SOP.md
- [[page.tsx_18]] - code - src/app/admin/analytics/page.tsx
- [[route.ts_39]] - code - src/app/api/admin/analytics/route.ts
- [[route.ts_43]] - code - src/app/api/assess/invite/[code]/start/route.ts
- [[route.ts_44]] - code - src/app/api/sessions/route.ts
- [[route.ts_47]] - code - src/app/api/sessions/[sessionId]/answers/route.ts
- [[route.ts_48]] - code - src/app/api/sessions/[sessionId]/complete/route.ts

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Admin_Dashboard,_Analytics_System,_Assessify_Platform
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_DELETE(), GET(), normalizeSectionCategory()]]

## Top bridge nodes
- [[route.ts_47]] - degree 3, connects to 1 community
- [[route.ts_48]] - degree 3, connects to 1 community
- [[route.ts_39]] - degree 2, connects to 1 community
- [[route.ts_43]] - degree 2, connects to 1 community
- [[route.ts_44]] - degree 2, connects to 1 community