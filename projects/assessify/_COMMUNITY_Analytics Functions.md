---
type: community
cohesion: 0.29
members: 7
---

# Analytics Functions

**Cohesion:** 0.29 - loosely connected
**Members:** 7 nodes

## Members
- [[analytics.ts]] - code - src/lib/analytics.ts
- [[getAssessmentFunnel()]] - code - src/lib/analytics.ts
- [[getCompetencyHeatmap()]] - code - src/lib/analytics.ts
- [[getQuestionAnalytics()]] - code - src/lib/analytics.ts
- [[getResultDistribution()]] - code - src/lib/analytics.ts
- [[getSessionAnalytics()]] - code - src/lib/analytics.ts
- [[trackEvent()]] - code - src/lib/analytics.ts

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Analytics_Functions
SORT file.name ASC
```
