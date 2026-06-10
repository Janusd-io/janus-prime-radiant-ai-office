---
type: community
cohesion: 0.70
members: 5
---

# getResend(), sendAdminInviteEmail(), sendAssessmentInviteEmail()

**Cohesion:** 0.70 - tightly connected
**Members:** 5 nodes

## Members
- [[email.ts]] - code - src/lib/email.ts
- [[getResend()]] - code - src/lib/email.ts
- [[sendAdminInviteEmail()]] - code - src/lib/email.ts
- [[sendAssessmentInviteEmail()]] - code - src/lib/email.ts
- [[sendOnboardingFormEmail()]] - code - src/lib/email.ts

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/getResend(),_sendAdminInviteEmail(),_sendAssessmentInviteEmail()
SORT file.name ASC
```
