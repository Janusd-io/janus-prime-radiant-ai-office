---
type: source
source_type: laptop
title: context_processors
slug: context-processors-2
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/apps/notifications/context_processors.py
original_size: 397
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:41Z"
---

# context_processors

_Extracted from `brightbean-studio/apps/notifications/context_processors.py` on 2026-05-14._

```python
def unread_notification_count(request):
    """Add unread notification count to all template contexts."""
    if hasattr(request, "user") and request.user.is_authenticated:
        from .models import Notification

        count = Notification.objects.filter(user=request.user, is_read=False).count()
        return {"unread_notification_count": count}
    return {"unread_notification_count": 0}

```