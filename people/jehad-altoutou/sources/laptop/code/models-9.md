---
type: source
source_type: laptop
title: models
slug: models-9
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/apps/workspaces/models.py
original_size: 1797
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:41Z"
---

# models

_Extracted from `brightbean-studio/apps/workspaces/models.py` on 2026-05-14._

```python
import uuid

from django.db import models

from apps.common.managers import OrgScopedManager


class Workspace(models.Model):
    class ApprovalWorkflowMode(models.TextChoices):
        NONE = "none", "None"
        OPTIONAL = "optional", "Optional"
        REQUIRED_INTERNAL = "required_internal", "Required (Internal)"
        REQUIRED_INTERNAL_AND_CLIENT = "required_internal_and_client", "Required (Internal + Client)"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    organization = models.ForeignKey(
        "organizations.Organization",
        on_delete=models.CASCADE,
        related_name="workspaces",
    )
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to="workspaces/icons/%Y/%m/", blank=True)
    description = models.CharField(max_length=500, blank=True, default="")
    timezone = models.CharField(max_length=63, blank=True, default="")
    primary_color = models.CharField(max_length=7, blank=True, default="")
    secondary_color = models.CharField(max_length=7, blank=True, default="")
    default_hashtags = models.JSONField(default=list, blank=True)
    default_first_comment = models.TextField(blank=True, default="")
    approval_workflow_mode = models.CharField(
        max_length=40,
        choices=ApprovalWorkflowMode.choices,
        default=ApprovalWorkflowMode.NONE,
    )
    is_archived = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = OrgScopedManager()

    class Meta:
        db_table = "workspaces_workspace"

    def __str__(self):
        return self.name

    @property
    def effective_timezone(self):
        return self.timezone or self.organization.default_timezone

```