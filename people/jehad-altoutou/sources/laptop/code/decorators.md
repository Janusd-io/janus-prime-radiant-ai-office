---
type: source
source_type: laptop
title: decorators
slug: decorators
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/apps/client_portal/decorators.py
original_size: 1634
original_ext: .py
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:41Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# decorators

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/apps/client_portal/decorators.py` on 2026-05-14._

```python
"""Portal authentication decorator."""

import functools

from django.shortcuts import redirect

from apps.members.models import WorkspaceMembership
from apps.workspaces.models import Workspace


def portal_auth_required(view_func):
    """Decorator that enforces portal session authentication.

    Checks that the user is authenticated, has an active portal session,
    and resolves the portal workspace onto the request.
    """

    @functools.wraps(view_func)
    def _wrapped(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("client_portal:magic_link_expired")

        if not request.session.get("is_portal_session"):
            return redirect("client_portal:magic_link_expired")

        workspace_id = request.session.get("portal_workspace_id")
        if not workspace_id:
            return redirect("client_portal:magic_link_expired")

        try:
            workspace = Workspace.objects.get(id=workspace_id)
        except Workspace.DoesNotExist:
            return redirect("client_portal:magic_link_expired")

        # Verify user has client membership in this workspace
        membership = (
            WorkspaceMembership.objects.filter(
                user=request.user,
                workspace=workspace,
            )
            .select_related("custom_role")
            .first()
        )

        if not membership:
            return redirect("client_portal:magic_link_expired")

        request.portal_workspace = workspace
        request.portal_membership = membership

        return view_func(request, *args, **kwargs)

    return _wrapped

```