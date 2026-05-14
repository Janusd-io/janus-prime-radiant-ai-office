---
type: source
source_type: laptop
title: _asset_grid_items
slug: asset-grid-items
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/media_library/_asset_grid_items.html
original_size: 210
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:40Z"
---

# _asset_grid_items

_Extracted from `brightbean-studio/templates/media_library/_asset_grid_items.html` on 2026-05-14._

{% comment %}Rendered after upload - individual asset cards to append to
grid. Expects: assets, workspace{% endcomment %} {% for asset in assets
%} {% include "media_library/\_asset_card.html" %} {% endfor %}
