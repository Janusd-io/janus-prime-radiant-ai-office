---
type: source
source_type: laptop
title: services
slug: services-3
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/apps/composer/services.py
original_size: 718
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:41Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# services

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/apps/composer/services.py` on 2026-05-14._

```python
"""Composer service helpers."""

from __future__ import annotations


def sync_post_scheduled_at(post):
    """Set ``post.scheduled_at`` to ``min(children scheduled_at)``.

    Keeps the legacy ``Post.scheduled_at`` column in sync with the earliest
    per-platform scheduled time so listings, grouping and Coalesce fallbacks
    remain consistent. No-op when no PlatformPost has a scheduled_at set.
    """
    times = list(post.platform_posts.exclude(scheduled_at__isnull=True).values_list("scheduled_at", flat=True))
    if not times:
        return
    earliest = min(times)
    if post.scheduled_at != earliest:
        post.scheduled_at = earliest
        post.save(update_fields=["scheduled_at", "updated_at"])

```