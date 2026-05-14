---
type: source
source_type: laptop
title: Brightbean Studio — context_processors
slug: context-processors-3
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/apps/onboarding/context_processors.py
original_size: 1229
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:41Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# context_processors

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/apps/onboarding/context_processors.py` on 2026-05-14._

```python
"""Context processor for onboarding checklist popup."""

from apps.onboarding.checklist import get_checklist_items
from apps.onboarding.models import OnboardingChecklist


def onboarding_checklist(request):
    """Inject onboarding checklist data into every template context."""
    if not hasattr(request, "user") or not request.user.is_authenticated:
        return {}

    workspace = getattr(request, "workspace", None)
    if not workspace:
        return {}

    checklist_dismissed = OnboardingChecklist.objects.filter(
        user=request.user, workspace=workspace, is_dismissed=True
    ).exists()

    if checklist_dismissed:
        return {"checklist_dismissed": True, "checklist_items": []}

    checklist_items = get_checklist_items(workspace)
    completed_count = sum(1 for item in checklist_items if item["completed"])
    total_count = len(checklist_items)

    # Don't show if all items are complete
    if completed_count == total_count:
        return {"checklist_dismissed": True, "checklist_items": []}

    return {
        "checklist_items": checklist_items,
        "checklist_dismissed": False,
        "checklist_completed_count": completed_count,
        "checklist_total_count": total_count,
    }

```