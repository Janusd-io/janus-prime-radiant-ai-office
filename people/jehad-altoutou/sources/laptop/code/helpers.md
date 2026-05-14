---
type: source
source_type: laptop
title: helpers
slug: helpers
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/apps/settings_manager/helpers.py
original_size: 1440
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:41Z"
---

# helpers

_Extracted from `brightbean-studio/apps/settings_manager/helpers.py` on 2026-05-14._

```python
"""Settings cascade helper: workspace -> org -> app default."""

from .defaults import APP_DEFAULTS
from .models import OrgSetting, WorkspaceSetting


def get_setting(workspace_id, key, workspace_org_id=None):
    """Return the setting value following the cascade:
    workspace override -> org override -> application default.

    Args:
        workspace_id: UUID of the workspace
        key: Setting key (e.g., "approval.internal_reminder_hours")
        workspace_org_id: Optional org ID to avoid an extra query.
                         If not provided, it will be looked up.
    """
    # 1. Check workspace-level override
    try:
        ws_setting = WorkspaceSetting.objects.get(workspace_id=workspace_id, key=key)
        if ws_setting.value is not None:
            return ws_setting.value
    except WorkspaceSetting.DoesNotExist:
        pass

    # 2. Check org-level override
    if workspace_org_id is None:
        from apps.workspaces.models import Workspace

        try:
            workspace_org_id = Workspace.objects.values_list("organization_id", flat=True).get(id=workspace_id)
        except Workspace.DoesNotExist:
            return APP_DEFAULTS.get(key)

    try:
        org_setting = OrgSetting.objects.get(organization_id=workspace_org_id, key=key)
        return org_setting.value
    except OrgSetting.DoesNotExist:
        pass

    # 3. Fall back to application default
    return APP_DEFAULTS.get(key)

```