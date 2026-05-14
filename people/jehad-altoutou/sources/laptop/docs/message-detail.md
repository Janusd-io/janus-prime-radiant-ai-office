---
type: source
source_type: laptop
title: message_detail
slug: message-detail
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/inbox/message_detail.html
original_size: 3093
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:37Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# message_detail

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/inbox/message_detail.html` on 2026-05-14._

{% extends "base.html" %} {% load humanize %} {% block title %}{{
message.sender_name }} - Inbox - {{ workspace.name }} - Brightbean{%
endblock %} {% block extra_head %} <style>
    .inbox-detail-full { margin: -1.5rem; height: calc(100% + 3rem); }
    .badge-pill {
        display: inline-flex; align-items: center; gap: 3px;
        font-size: 10px; font-weight: 600; padding: 2px 7px;
        border-radius: 9999px; letter-spacing: 0.01em; white-space: nowrap;
    }
    .badge-sentiment-positive { background: var(--success-50); color: var(--success-700); }
    .badge-sentiment-neutral  { background: var(--surface-2); color: var(--text-tertiary); }
    .badge-sentiment-negative { background: var(--error-50); color: var(--error-700); }
    .badge-type { background: var(--surface-2); color: var(--text-secondary); }
    .badge-status-unread  { background: var(--info-50); color: var(--info-700); }
    .badge-status-open    { background: var(--warning-50); color: var(--warning-700); }
    .badge-status-resolved { background: var(--success-50); color: var(--success-700); }
    .badge-status-archived { background: var(--surface-2); color: var(--text-ghost); }
    .sla-countdown { font-family: var(--font-mono); font-size: 11px; font-weight: 600; }
    .sla-ok { color: var(--text-tertiary); }
    .sla-warn { color: var(--warning-700); }
    .sla-overdue { color: var(--error-700); }
</style> {% endblock %} {% block content %}

<div class="inbox-detail-full" x-data="{
    slaTarget: {{ sla_config.target_response_minutes|default:'0' }},
    getSlaClass(receivedAt) {
        if (!this.slaTarget) return '';
        const deadline = new Date(new Date(receivedAt).getTime() + this.slaTarget * 60000);
        const remaining = deadline - new Date();
        if (remaining &lt; 0) return 'sla-overdue';
        if (remaining &lt; this.slaTarget * 60000 * 0.25) return 'sla-warn';
        return 'sla-ok';
    },
    formatSla(receivedAt) {
        if (!this.slaTarget) return '';
        const deadline = new Date(new Date(receivedAt).getTime() + this.slaTarget * 60000);
        const diff = deadline - new Date();
        const mins = Math.floor(Math.abs(diff) / 60000);
        if (diff &lt; 0) return mins &lt; 60 ? mins + 'm overdue' : Math.floor(mins/60) + 'h overdue';
        return mins &lt; 60 ? mins + 'm left' : Math.floor(mins/60) + 'h ' + (mins%60) + 'm left';
    }
}">

<div class="px-5 py-2.5 border-b border-stone-100 flex-shrink-0">

<a
href="%7B%%20url%20&#39;inbox:feed&#39;%20workspace_id=workspace.id%20%%7D"
class="inline-flex items-center gap-1.5 text-[13px] font-medium text-stone-500 hover:text-stone-700 transition-colors"><img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjxwb2x5bGluZSBwb2ludHM9IjE1IDE4IDkgMTIgMTUgNiI+PC9wb2x5bGluZT48L3N2Zz4="
class="w-4 h-4" /> Back to Inbox</a>

</div>

<div id="inbox-detail-panel" class="flex-1"
style="height: calc(100% - 41px);">

{% include "inbox/partials/\_message_panel.html" %}

</div>

</div>

{% endblock %}
