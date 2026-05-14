---
type: source
source_type: laptop
title: managers
slug: managers-2
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/apps/media_library/managers.py
original_size: 2046
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:41Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# managers

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/apps/media_library/managers.py` on 2026-05-14._

```python
"""Custom managers for media library models."""

from django.db import connection, models
from django.db.models import Q


class MediaAssetManager(models.Manager):
    def for_workspace(self, workspace_id):
        return self.get_queryset().filter(workspace_id=workspace_id)

    def for_org(self, organization_id):
        return self.get_queryset().filter(organization_id=organization_id)

    def for_workspace_with_shared(self, workspace_id, organization_id):
        """Return workspace-scoped assets plus shared org-level assets."""
        return self.get_queryset().filter(
            Q(workspace_id=workspace_id) | Q(workspace__isnull=True, organization_id=organization_id)
        )

    def shared_only(self, organization_id):
        """Return only shared org-level assets (workspace is null)."""
        return self.get_queryset().filter(
            organization_id=organization_id,
            workspace__isnull=True,
        )

    def search(self, query, queryset=None):
        """Full-text search on filename and tags.

        Uses PostgreSQL full-text search when available, falls back to
        case-insensitive LIKE queries on SQLite.
        """
        qs = queryset if queryset is not None else self.get_queryset()
        if not query:
            return qs

        if connection.vendor == "postgresql":
            from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

            search_vector = SearchVector("filename", weight="A")
            search_query = SearchQuery(query, search_type="websearch")

            qs = (
                qs.annotate(
                    search=search_vector,
                    rank=SearchRank(search_vector, search_query),
                )
                .filter(Q(search=search_query) | Q(tags__contains=[query]))
                .order_by("-rank")
            )
        else:
            # SQLite fallback: simple case-insensitive contains
            qs = qs.filter(Q(filename__icontains=query) | Q(tags__icontains=query))

        return qs

```