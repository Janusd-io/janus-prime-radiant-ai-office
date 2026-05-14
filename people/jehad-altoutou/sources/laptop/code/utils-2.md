---
type: source
source_type: laptop
title: utils
slug: utils-2
created: 2026-04-20
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/apps/utils.py
original_size: 837
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:41Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# utils

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/apps/utils.py` on 2026-05-14._

```python
"""Shared utilities across apps."""

import json

from django.conf import settings
from django.db.models import Q


def json_tag_contains(field, tag):
    """Return a Q object that filters a JSONField array containing the given tag.

    Works on both PostgreSQL (__contains) and SQLite (__icontains fallback).
    """
    db_engine = settings.DATABASES["default"]["ENGINE"]
    if "sqlite" in db_engine:
        # SQLite doesn't support __contains on JSON fields at all.
        # Use __icontains on the raw text representation instead.
        # A JSON array like ["test", "foo"] is stored as text, so we search
        # for the JSON-encoded string value (e.g. '"test"') within it.
        json_str = json.dumps(tag)  # e.g. '"test"'
        return Q(**{f"{field}__icontains": json_str})
    return Q(**{f"{field}__contains": [tag]})

```