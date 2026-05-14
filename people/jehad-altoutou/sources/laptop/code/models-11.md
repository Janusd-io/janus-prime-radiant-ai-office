---
type: source
source_type: laptop
title: models
slug: models-11
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/apps/settings_manager/models.py
original_size: 1305
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:41Z"
project: brightbean-studio

---

# models

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/apps/settings_manager/models.py` on 2026-05-14._

```python
import uuid

from django.db import models

from apps.common.managers import OrgScopedManager


class OrgSetting(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    organization = models.ForeignKey(
        "organizations.Organization",
        on_delete=models.CASCADE,
        related_name="settings",
    )
    key = models.CharField(max_length=255)
    value = models.JSONField()
    updated_at = models.DateTimeField(auto_now=True)

    objects = OrgScopedManager()

    class Meta:
        db_table = "settings_org_setting"
        unique_together = [("organization", "key")]

    def __str__(self):
        return f"{self.organization.name}: {self.key}"


class WorkspaceSetting(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    workspace = models.ForeignKey(
        "workspaces.Workspace",
        on_delete=models.CASCADE,
        related_name="settings",
    )
    key = models.CharField(max_length=255)
    value = models.JSONField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "settings_workspace_setting"
        unique_together = [("workspace", "key")]

    def __str__(self):
        return f"{self.workspace.name}: {self.key}"

```