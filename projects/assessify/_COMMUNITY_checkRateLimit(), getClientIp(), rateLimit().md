---
type: community
cohesion: 0.83
members: 4
---

# checkRateLimit(), getClientIp(), rateLimit()

**Cohesion:** 0.83 - tightly connected
**Members:** 4 nodes

## Members
- [[checkRateLimit()]] - code - src/lib/rate-limit.ts
- [[getClientIp()]] - code - src/lib/rate-limit.ts
- [[rate-limit.ts]] - code - src/lib/rate-limit.ts
- [[rateLimit()]] - code - src/lib/rate-limit.ts

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/checkRateLimit(),_getClientIp(),_rateLimit()
SORT file.name ASC
```
