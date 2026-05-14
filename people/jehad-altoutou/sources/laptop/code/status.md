---
type: source
source_type: laptop
title: status
slug: status
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/apps/composer/status.py
original_size: 2291
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:41Z"
project: brightbean-studio

---

# status

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/apps/composer/status.py` on 2026-05-14._

```python
"""Post status aggregation helpers.

Editorial status lives on ``PlatformPost`` — each social account flows through
the workflow independently. ``Post.status`` is a *derived* property computed
from its children. This module holds the pure aggregation function so it can
be reused by model properties, views, and tests.
"""

# Canonical workflow order from least- to most-advanced. "Lower" states win
# when a post has mixed children in non-terminal states so the UI reflects the
# most conservative / action-required state.
_WORKFLOW_ORDER = [
    "draft",
    "changes_requested",
    "rejected",
    "pending_review",
    "pending_client",
    "approved",
    "scheduled",
    "publishing",
    "partially_published",
    "published",
]

# Statuses considered "terminal publishing outcomes".
_TERMINAL = {"published", "failed"}


def derive_post_status(statuses):
    """Return an aggregate post-level status from an iterable of child statuses.

    Rules:
      - empty → "draft"
      - all children share the same value → that value
      - all terminal, all published → "published"
      - all terminal, all failed → "failed"
      - all terminal, mix of published/failed → "partially_published"
      - any child failed + any non-terminal → "publishing" (still in flight)
      - otherwise → the "lowest" (earliest in _WORKFLOW_ORDER) child status.
        This means e.g. (draft, scheduled) → "draft", (scheduled, publishing) →
        "scheduled", (pending_review, approved) → "pending_review".
    """
    values = [s for s in statuses if s]
    if not values:
        return "draft"

    unique = set(values)
    if len(unique) == 1:
        return values[0]

    # All terminal: combine by outcome.
    if unique <= (_TERMINAL | {"failed"}):
        if "published" in unique and "failed" in unique:
            return "partially_published"
        if unique == {"published"}:
            return "published"
        return "failed"

    # Otherwise return the "lowest" state by workflow order. Unknown values fall
    # to the end so a weird stray status doesn't shadow real ones.
    def _rank(s):
        try:
            return _WORKFLOW_ORDER.index(s)
        except ValueError:
            return len(_WORKFLOW_ORDER)

    return min(unique, key=_rank)

```