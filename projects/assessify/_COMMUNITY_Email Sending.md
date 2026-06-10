---
type: community
cohesion: 0.83
members: 4
---

# Email Sending

**Cohesion:** 0.83 - tightly connected
**Members:** 4 nodes

## Members
- [[email.ts]] - code - src/lib/email.ts
- [[getResend()]] - code - src/lib/email.ts
- [[sendAssessmentInviteEmail()]] - code - src/lib/email.ts
- [[sendOnboardingFormEmail()]] - code - src/lib/email.ts

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Email_Sending
SORT file.name ASC
```
