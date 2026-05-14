---
type: source
source_type: laptop
title: settings
slug: settings-3
created: 2026-04-20
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/layouts/settings.html
original_size: 4991
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:40Z"
project: brightbean-studio

---

# settings

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/layouts/settings.html` on 2026-05-14._

{% extends "base.html" %} {% block page_header %}{% endblock %} {% block
sidebar_nav %} <a
href="%7B%%20if%20request.workspace%20%%7D%7B%%20url%20&#39;calendar:calendar&#39;%20workspace_id=request.workspace.id%20%%7D%7B%%20else%20%%7D/%7B%%20endif%20%%7D"
class="sidebar-nav-item mb-2"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iZmxleC1zaHJpbmstMCIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0IiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PGxpbmUgeDE9IjE5IiB5MT0iMTIiIHgyPSI1IiB5Mj0iMTIiPjwvbGluZT48cG9seWxpbmUgcG9pbnRzPSIxMiAxOSA1IDEyIDEyIDUiPjwvcG9seWxpbmU+PC9zdmc+"
class="flex-shrink-0" /> <span
class="sidebar-nav-label">Settings</span></a>

<div class="sidebar-section-label">

Account

</div>

<a href="%7B%%20url%20&#39;accounts:settings&#39;%20%%7D"
class="sidebar-nav-item mb-1 {% if settings_active == &#39;profile&#39; %}active{% endif %}"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iZmxleC1zaHJpbmstMCIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0IiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PHBhdGggZD0iTTIwIDIxdi0yYTQgNCAwIDAwLTQtNEg4YTQgNCAwIDAwLTQgNHYyIiAvPjxjaXJjbGUgY3g9IjEyIiBjeT0iNyIgcj0iNCI+PC9jaXJjbGU+PC9zdmc+"
class="flex-shrink-0" /> <span
class="sidebar-nav-label">Profile</span></a> <a
href="%7B%%20url%20&#39;accounts:settings&#39;%20%%7D?tab=preferences"
class="sidebar-nav-item mb-1 {% if settings_active == &#39;preferences&#39; %}active{% endif %}"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iZmxleC1zaHJpbmstMCIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0IiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PGxpbmUgeDE9IjQiIHkxPSIyMSIgeDI9IjQiIHkyPSIxNCI+PC9saW5lPjxsaW5lIHgxPSI0IiB5MT0iMTAiIHgyPSI0IiB5Mj0iMyI+PC9saW5lPjxsaW5lIHgxPSIxMiIgeTE9IjIxIiB4Mj0iMTIiIHkyPSIxMiI+PC9saW5lPjxsaW5lIHgxPSIxMiIgeTE9IjgiIHgyPSIxMiIgeTI9IjMiPjwvbGluZT48bGluZSB4MT0iMjAiIHkxPSIyMSIgeDI9IjIwIiB5Mj0iMTYiPjwvbGluZT48bGluZSB4MT0iMjAiIHkxPSIxMiIgeDI9IjIwIiB5Mj0iMyI+PC9saW5lPjxsaW5lIHgxPSIxIiB5MT0iMTQiIHgyPSI3IiB5Mj0iMTQiPjwvbGluZT48bGluZSB4MT0iOSIgeTE9IjgiIHgyPSIxNSIgeTI9IjgiPjwvbGluZT48bGluZSB4MT0iMTciIHkxPSIxNiIgeDI9IjIzIiB5Mj0iMTYiPjwvbGluZT48L3N2Zz4="
class="flex-shrink-0" /> <span
class="sidebar-nav-label">Preferences</span></a>

<div class="sidebar-section-label">

Organization

</div>

<a href="%7B%%20url%20&#39;organizations:settings&#39;%20%%7D"
class="sidebar-nav-item mb-1 {% if settings_active == &#39;general&#39; %}active{% endif %}"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iZmxleC1zaHJpbmstMCIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0IiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PHJlY3QgeD0iMiIgeT0iMyIgd2lkdGg9IjIwIiBoZWlnaHQ9IjE0IiByeD0iMiIgcnk9IjIiIC8+PGxpbmUgeDE9IjgiIHkxPSIyMSIgeDI9IjE2IiB5Mj0iMjEiPjwvbGluZT48bGluZSB4MT0iMTIiIHkxPSIxNyIgeDI9IjEyIiB5Mj0iMjEiPjwvbGluZT48L3N2Zz4="
class="flex-shrink-0" /> <span
class="sidebar-nav-label">General</span></a>
<a href="%7B%%20url%20&#39;organizations:workspaces&#39;%20%%7D"
class="sidebar-nav-item mb-1 {% if settings_active == &#39;workspaces&#39; %}active{% endif %}"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iZmxleC1zaHJpbmstMCIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0IiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PHJlY3QgeD0iMyIgeT0iMyIgd2lkdGg9IjciIGhlaWdodD0iNyIgLz48cmVjdCB4PSIxNCIgeT0iMyIgd2lkdGg9IjciIGhlaWdodD0iNyIgLz48cmVjdCB4PSIzIiB5PSIxNCIgd2lkdGg9IjciIGhlaWdodD0iNyIgLz48cmVjdCB4PSIxNCIgeT0iMTQiIHdpZHRoPSI3IiBoZWlnaHQ9IjciIC8+PC9zdmc+"
class="flex-shrink-0" /> <span
class="sidebar-nav-label">Workspaces</span></a>
<a href="%7B%%20url%20&#39;members:list&#39;%20%%7D"
class="sidebar-nav-item mb-1 {% if settings_active == &#39;members&#39; %}active{% endif %}"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iZmxleC1zaHJpbmstMCIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0IiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PHBhdGggZD0iTTE3IDIxdi0yYTQgNCAwIDAwLTQtNEg1YTQgNCAwIDAwLTQgNHYyIiAvPjxjaXJjbGUgY3g9IjkiIGN5PSI3IiByPSI0Ij48L2NpcmNsZT48cGF0aCBkPSJNMjMgMjF2LTJhNCA0IDAgMDAtMy0zLjg3TTE2IDMuMTNhNCA0IDAgMDEwIDcuNzUiIC8+PC9zdmc+"
class="flex-shrink-0" /> <span class="sidebar-nav-label">Team
Members</span></a> <a
href="%7B%%20url%20&#39;organizations:cross_workspace_calendar&#39;%20%%7D"
class="sidebar-nav-item mb-1 {% if settings_active == &#39;calendars&#39; %}active{% endif %}"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iZmxleC1zaHJpbmstMCIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0IiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PHJlY3QgeD0iMyIgeT0iNCIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiByeD0iMiIgcnk9IjIiIC8+PGxpbmUgeDE9IjE2IiB5MT0iMiIgeDI9IjE2IiB5Mj0iNiI+PC9saW5lPjxsaW5lIHgxPSI4IiB5MT0iMiIgeDI9IjgiIHkyPSI2Ij48L2xpbmU+PGxpbmUgeDE9IjMiIHkxPSIxMCIgeDI9IjIxIiB5Mj0iMTAiPjwvbGluZT48L3N2Zz4="
class="flex-shrink-0" /> <span class="sidebar-nav-label">All
Calendars</span></a>
<a href="%7B%%20url%20&#39;media_library_org:shared_index&#39;%20%%7D"
class="sidebar-nav-item mb-1 {% if settings_active == &#39;media&#39; %}active{% endif %}"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iZmxleC1zaHJpbmstMCIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0IiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PHJlY3QgeD0iMyIgeT0iMyIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiByeD0iMiIgcnk9IjIiIC8+PGNpcmNsZSBjeD0iOC41IiBjeT0iOC41IiByPSIxLjUiPjwvY2lyY2xlPjxwb2x5bGluZSBwb2ludHM9IjIxIDE1IDE2IDEwIDUgMjEiPjwvcG9seWxpbmU+PC9zdmc+"
class="flex-shrink-0" /> <span class="sidebar-nav-label">Media
Library</span></a>
<a href="%7B%%20url%20&#39;credentials:list&#39;%20%%7D"
class="sidebar-nav-item mb-1 {% if settings_active == &#39;credentials&#39; %}active{% endif %}"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iZmxleC1zaHJpbmstMCIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0IiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PHBhdGggZD0iTTE1IDdoM2E1IDUgMCAwMTAgMTBoLTNtLTYgMEg2QTUgNSAwIDAxNiA3aDMiIC8+PGxpbmUgeDE9IjgiIHkxPSIxMiIgeDI9IjE2IiB5Mj0iMTIiPjwvbGluZT48L3N2Zz4="
class="flex-shrink-0" /> <span class="sidebar-nav-label">Platform
Credentials</span></a> {% endblock %} {% block content %} {% endblock %}
