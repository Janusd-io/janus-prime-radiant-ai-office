---
type: source
source_type: laptop
title: workspace_settings
slug: workspace-settings
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/layouts/workspace_settings.html
original_size: 3904
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:40Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# workspace_settings

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/layouts/workspace_settings.html` on 2026-05-14._

{% extends "base.html" %} {% block page_header %}{% endblock %} {% block
sidebar_nav %} <a
href="%7B%%20url%20&#39;calendar:calendar&#39;%20workspace_id=request.workspace.id%20%%7D"
class="sidebar-nav-item mb-2"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iZmxleC1zaHJpbmstMCIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0IiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PGxpbmUgeDE9IjE5IiB5MT0iMTIiIHgyPSI1IiB5Mj0iMTIiPjwvbGluZT48cG9seWxpbmUgcG9pbnRzPSIxMiAxOSA1IDEyIDEyIDUiPjwvcG9seWxpbmU+PC9zdmc+"
class="flex-shrink-0" /> <span class="sidebar-nav-label">Workspace
Settings</span></a>

<div class="sidebar-section-label">

{{ request.workspace.name }}

</div>

<a
href="%7B%%20url%20&#39;workspaces:settings&#39;%20workspace_id=request.workspace.id%20%%7D"
class="sidebar-nav-item mb-1 {% if settings_active == &#39;general&#39; %}active{% endif %}"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iZmxleC1zaHJpbmstMCIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0IiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PGNpcmNsZSBjeD0iMTIiIGN5PSIxMiIgcj0iMyI+PC9jaXJjbGU+PHBhdGggZD0iTTE5LjQgMTVhMS42NSAxLjY1IDAgMDAuMzMgMS44MmwuMDYuMDZhMiAyIDAgMDEwIDIuODMgMiAyIDAgMDEtMi44MyAwbC0uMDYtLjA2YTEuNjUgMS42NSAwIDAwLTEuODItLjMzIDEuNjUgMS42NSAwIDAwLTEgMS41MVYyMWEyIDIgMCAwMS00IDB2LS4wOUExLjY1IDEuNjUgMCAwMDkgMTkuNGExLjY1IDEuNjUgMCAwMC0xLjgyLjMzbC0uMDYuMDZhMiAyIDAgMDEtMi44My0yLjgzbC4wNi0uMDZBMS42NSAxLjY1IDAgMDA0LjY4IDE1YTEuNjUgMS42NSAwIDAwLTEuNTEtMUgzYTIgMiAwIDAxMC00aC4wOUExLjY1IDEuNjUgMCAwMDQuNiA5YTEuNjUgMS42NSAwIDAwLS4zMy0xLjgybC0uMDYtLjA2YTIgMiAwIDAxMi44My0yLjgzbC4wNi4wNkExLjY1IDEuNjUgMCAwMDkgNC42OGExLjY1IDEuNjUgMCAwMDEtMS41MVYzYTIgMiAwIDAxNCAwdi4wOWExLjY1IDEuNjUgMCAwMDEgMS41MSAxLjY1IDEuNjUgMCAwMDEuODItLjMzbC4wNi0uMDZhMiAyIDAgMDEyLjgzIDIuODNsLS4wNi4wNkExLjY1IDEuNjUgMCAwMDE5LjMyIDlhMS42NSAxLjY1IDAgMDAxLjUxIDFIMjFhMiAyIDAgMDEwIDRoLS4wOWExLjY1IDEuNjUgMCAwMC0xLjUxIDF6IiAvPjwvc3ZnPg=="
class="flex-shrink-0" /> <span
class="sidebar-nav-label">General</span></a> <a
href="%7B%%20url%20&#39;social_accounts:list&#39;%20workspace_id=request.workspace.id%20%%7D"
class="sidebar-nav-item mb-1 {% if settings_active == &#39;social_accounts&#39; %}active{% endif %}"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iZmxleC1zaHJpbmstMCIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0IiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PGNpcmNsZSBjeD0iMTgiIGN5PSI1IiByPSIzIj48L2NpcmNsZT48Y2lyY2xlIGN4PSI2IiBjeT0iMTIiIHI9IjMiPjwvY2lyY2xlPjxjaXJjbGUgY3g9IjE4IiBjeT0iMTkiIHI9IjMiPjwvY2lyY2xlPjxsaW5lIHgxPSI4LjU5IiB5MT0iMTMuNTEiIHgyPSIxNS40MiIgeTI9IjE3LjQ5Ij48L2xpbmU+PGxpbmUgeDE9IjE1LjQxIiB5MT0iNi41MSIgeDI9IjguNTkiIHkyPSIxMC40OSI+PC9saW5lPjwvc3ZnPg=="
class="flex-shrink-0" /> <span class="sidebar-nav-label">Social
Accounts</span></a> <a
href="%7B%%20url%20&#39;media_library:index&#39;%20workspace_id=request.workspace.id%20%%7D"
class="sidebar-nav-item mb-1 {% if settings_active == &#39;media&#39; %}active{% endif %}"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iZmxleC1zaHJpbmstMCIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0IiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PHJlY3QgeD0iMyIgeT0iMyIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiByeD0iMiIgcnk9IjIiIC8+PGNpcmNsZSBjeD0iOC41IiBjeT0iOC41IiByPSIxLjUiPjwvY2lyY2xlPjxwb2x5bGluZSBwb2ludHM9IjIxIDE1IDE2IDEwIDUgMjEiPjwvcG9seWxpbmU+PC9zdmc+"
class="flex-shrink-0" /> <span class="sidebar-nav-label">Media
Library</span></a> <a
href="%7B%%20url%20&#39;workspaces:approvals_settings&#39;%20workspace_id=request.workspace.id%20%%7D"
class="sidebar-nav-item mb-1 {% if settings_active == &#39;approvals&#39; %}active{% endif %}"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iZmxleC1zaHJpbmstMCIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0IiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PHBhdGggZD0iTTEyIDIyczgtNCA4LTEwVjVsLTgtMy04IDN2N2MwIDYgOCAxMCA4IDEweiIgLz48cG9seWxpbmUgcG9pbnRzPSI5IDEyIDExIDE0IDE1IDEwIj48L3BvbHlsaW5lPjwvc3ZnPg=="
class="flex-shrink-0" /> <span
class="sidebar-nav-label">Approvals</span></a> <a
href="%7B%%20url%20&#39;client_portal_admin:client_list&#39;%20workspace_id=request.workspace.id%20%%7D"
class="sidebar-nav-item mb-1 {% if settings_active == &#39;clients&#39; %}active{% endif %}"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iZmxleC1zaHJpbmstMCIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0IiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PHBhdGggZD0iTTE3IDIxdi0yYTQgNCAwIDAwLTQtNEg1YTQgNCAwIDAwLTQtNHYyIiAvPjxjaXJjbGUgY3g9IjkiIGN5PSI3IiByPSI0Ij48L2NpcmNsZT48cGF0aCBkPSJNMjMgMjF2LTJhNCA0IDAgMDAtMy0zLjg3IiAvPjxwYXRoIGQ9Ik0xNiAzLjEzYTQgNCAwIDAxMCA3Ljc1IiAvPjwvc3ZnPg=="
class="flex-shrink-0" /> <span class="sidebar-nav-label">Client
Portal</span></a> {% endblock %} {% block content %} {% endblock %}
