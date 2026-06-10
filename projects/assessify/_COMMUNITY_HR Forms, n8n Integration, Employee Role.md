---
type: community
cohesion: 0.50
members: 4
---

# HR Forms, n8n Integration, Employee Role

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Members
- [[Employee Role]] - document - SOP.md
- [[HR Forms]] - document - SOP.md
- [[Webhooks & Automation]] - document - SOP.md
- [[n8n Integration]] - document - SOP.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/HR_Forms,_n8n_Integration,_Employee_Role
SORT file.name ASC
```
