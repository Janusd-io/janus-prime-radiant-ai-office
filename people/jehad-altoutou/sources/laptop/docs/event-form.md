---
type: source
source_type: laptop
title: event_form
slug: event-form
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/calendar/partials/event_form.html
original_size: 4110
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:37Z"
---

# event_form

_Extracted from `brightbean-studio/templates/calendar/partials/event_form.html` on 2026-05-14._

<div class="p-5">

### {% if event %}Edit Event{% else %}Add Custom Event{% endif %}

{% csrf_token %}

<div>

Title

</div>

<div class="grid grid-cols-2 gap-3">

<div>

Start Date

</div>

<div>

End Date

</div>

</div>

<div>

Color

<div class="flex items-center gap-2">

<div class="flex gap-1.5"
x-data="{ presets: ['#3B82F6','#22C55E','#EAB308','#F97316','#EF4444','#8B5CF6','#EC4899','#14B8A6'] }">

</div>

</div>

</div>

<div>

Description (optional)

</div>

<div class="flex items-center justify-between pt-2">

{% if event %}

{% csrf_token %}

Delete Event

{% else %}

<div>

</div>

{% endif %}

<div class="flex items-center gap-2">

Cancel

{% if event %}Save Changes{% else %}Add Event{% endif %}

</div>

</div>

</div>
