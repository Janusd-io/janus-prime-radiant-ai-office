---
type: source
source_type: laptop
title: _folder_tree
slug: folder-tree
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/media_library/_folder_tree.html
original_size: 6874
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:40Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# _folder_tree

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/media_library/_folder_tree.html` on 2026-05-14._

{% comment %}Nested folder tree for sidebar. Expects: folders,
workspace, current_folder{% endcomment %}

<div x-data="{ folderToDelete: null, folderDeleteName: '', folderDeleteUrl: '' }">

{% for folder in folders %}

<div class="ml-folder-group">

<a
href="%7B%%20url%20&#39;media_library:index&#39;%20workspace_id=workspace.id%20%%7D?folder=%7B%7B%20folder.id%20%7D%7D"
class="ml-folder-item flex items-center gap-2 px-3 py-1.5 rounded-lg text-sm cursor-pointer group {% if current_folder == folder.id|slugify %}active{% endif %}"
data-x-data="{ editing: false, expanded: true }"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUgZmxleC1zaHJpbmstMCB0cmFuc2l0aW9uLXRyYW5zZm9ybSIgOmNsYXNzPSJleHBhbmRlZCA/ICYjMzk7cm90YXRlLTkwJiMzOTsgOiAmIzM5OyYjMzk7IiBAY2xpY2sucHJldmVudD0iZXhwYW5kZWQgPSAhZXhwYW5kZWQiIHN0eWxlPSJjb2xvcjogdmFyKC0tdGV4dC1naG9zdCwgI0E4QTI5RSk7IiBmaWxsPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyMCAyMCI+CiAgICAgIDxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcuMjkzIDE0LjcwN2ExIDEgMCAwMTAtMS40MTRMMTAuNTg2IDEwIDcuMjkzIDYuNzA3YTEgMSAwIDAxMS40MTQtMS40MTRsNCA0YTEgMSAwIDAxMCAxLjQxNGwtNCA0YTEgMSAwIDAxLTEuNDE0IDB6IiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIC8+CiAgICA8L3N2Zz4="
class="w-3.5 h-3.5 flex-shrink-0 transition-transform" /> <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCBmbGV4LXNocmluay0wIiBzdHlsZT0iY29sb3I6IHZhcigtLXRleHQtZ2hvc3QsICNBOEEyOUUpOyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+CiAgICAgIDxwYXRoIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIxLjUiIGQ9Ik0zIDd2MTBhMiAyIDAgMDAyIDJoMTRhMiAyIDAgMDAyLTJWOWEyIDIgMCAwMC0yLTJoLTZsLTItMkg1YTIgMiAwIDAwLTIgMnoiIC8+CiAgICA8L3N2Zz4="
class="w-4 h-4 flex-shrink-0" /> <span class="truncate flex-1"
data-x-text="&#39;{{ folder.name }}&#39;">{{ folder.name }}</span></a>

<div class="hidden group-hover:flex items-center gap-0.5">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zIGgtMyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjIiIGQ9Ik02IDE4TDE4IDZNNiA2bDEyIDEyIiAvPjwvc3ZnPg=="
class="w-3 h-3" />

</div>

{% if folder.subfolders.all %}

<div class="pl-5 mt-0.5" x-show="expanded">

{% for subfolder in folder.subfolders.all %} <a
href="%7B%%20url%20&#39;media_library:index&#39;%20workspace_id=workspace.id%20%%7D?folder=%7B%7B%20subfolder.id%20%7D%7D"
class="ml-folder-item flex items-center gap-2 px-3 py-1.5 rounded-lg text-sm cursor-pointer group {% if current_folder == subfolder.id|slugify %}active{% endif %}"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCBmbGV4LXNocmluay0wIiBzdHlsZT0iY29sb3I6IHZhcigtLXRleHQtZ2hvc3QpOyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+CiAgICAgICAgPHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNSIgZD0iTTMgN3YxMGEyIDIgMCAwMDIgMmgxNGEyIDIgMCAwMDItMlY5YTIgMiAwIDAwLTItMmgtNmwtMi0ySDVhMiAyIDAgMDAtMiAyeiIgLz4KICAgICAgPC9zdmc+"
class="w-4 h-4 flex-shrink-0" /> <span class="truncate flex-1">{{
subfolder.name }}</span></a>

<div class="hidden group-hover:flex items-center gap-0.5">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zIGgtMyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjIiIGQ9Ik02IDE4TDE4IDZNNiA2bDEyIDEyIiAvPjwvc3ZnPg=="
class="w-3 h-3" />

</div>

{% if subfolder.subfolders.all %}

<div class="pl-5 mt-0.5">

{% for sub2 in subfolder.subfolders.all %} <a
href="%7B%%20url%20&#39;media_library:index&#39;%20workspace_id=workspace.id%20%%7D?folder=%7B%7B%20sub2.id%20%7D%7D"
class="ml-folder-item flex items-center gap-2 px-3 py-1.5 rounded-lg text-sm cursor-pointer group {% if current_folder == sub2.id|slugify %}active{% endif %}"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCBmbGV4LXNocmluay0wIiBzdHlsZT0iY29sb3I6IHZhcigtLXRleHQtZ2hvc3QpOyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+CiAgICAgICAgICA8cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIHN0cm9rZS13aWR0aD0iMS41IiBkPSJNMyA3djEwYTIgMiAwIDAwMiAyaDE0YTIgMiAwIDAwMi0yVjlhMiAyIDAgMDAtMi0yaC02bC0yLTJINWEyIDIgMCAwMC0yIDJ6IiAvPgogICAgICAgIDwvc3ZnPg=="
class="w-4 h-4 flex-shrink-0" /> <span class="truncate flex-1">{{
sub2.name }}</span></a> {% endfor %}

</div>

{% endif %} {% endfor %}

</div>

{% endif %}

</div>

{% empty %}

No folders yet

{% endfor %}

<div class="fixed inset-0 z-[60] flex items-center justify-center"
x-show="folderToDelete" x-cloak=""
@keydown.escape.window="folderToDelete = null">

<div class="absolute inset-0 bg-black/30 backdrop-blur-sm"
@click="folderToDelete = null">

</div>

<div class="relative bg-white rounded-2xl shadow-xl w-full max-w-sm mx-4 p-6"
@click.stop="">

<div class="w-10 h-10 rounded-full flex items-center justify-center mx-auto mb-3"
style="background: var(--error-50, #FEF2F2);">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy01IGgtNSIgc3R5bGU9ImNvbG9yOiB2YXIoLS1lcnJvci01MDAsICNFRjQ0NDQpOyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjIiIGQ9Ik0xOSA3bC0uODY3IDEyLjE0MkEyIDIgMCAwMTE2LjEzOCAyMUg3Ljg2MmEyIDIgMCAwMS0xLjk5NS0xLjg1OEw1IDdtNSA0djZtNC02djZtMS0xMFY0YTEgMSAwIDAwLTEtMWgtNGExIDEgMCAwMC0xIDF2M000IDdoMTYiIC8+PC9zdmc+"
class="w-5 h-5" />

</div>

### Delete folder?

Delete <span class="font-medium" x-text="folderDeleteName"></span>?
Assets will be moved to the parent folder.

<div class="flex gap-2">

Cancel

Delete

</div>

</div>

</div>

</div>
