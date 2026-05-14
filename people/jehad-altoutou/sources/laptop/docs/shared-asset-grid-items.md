---
type: source
source_type: laptop
title: _shared_asset_grid_items
slug: shared-asset-grid-items
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/media_library/_shared_asset_grid_items.html
original_size: 195
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:40Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# _shared_asset_grid_items

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/media_library/_shared_asset_grid_items.html` on 2026-05-14._

{% comment %}Rendered after shared upload - individual asset cards.
Expects: assets{% endcomment %} {% for asset in assets %} {% include
"media_library/\_shared_asset_card.html" %} {% endfor %}
