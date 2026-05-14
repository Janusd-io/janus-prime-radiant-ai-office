---
type: source
source_type: laptop
title: _folder_form
slug: folder-form
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/media_library/_folder_form.html
original_size: 2092
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:40Z"
---

# _folder_form

_Extracted from `brightbean-studio/templates/media_library/_folder_form.html` on 2026-05-14._

{% comment %}Modal for creating a new folder. Expects: workspace{%
endcomment %}

<div class="fixed inset-0 z-50 flex items-center justify-center"
@keydown.escape.window="showNewFolder = false">

<div class="absolute inset-0 bg-black/30 backdrop-blur-sm"
@click="showNewFolder = false">

</div>

<div class="relative bg-white rounded-2xl shadow-xl w-full max-w-sm mx-4 p-6"
@click.stop="">

### New Folder

<div class="flex justify-end gap-2">

Cancel

Create Folder

</div>

</div>

</div>
