---
type: source
source_type: laptop
title: publish_list_shell
slug: publish-list-shell
created: 2026-04-20
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/templates/calendar/partials/publish_list_shell.html
original_size: 13098
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:37Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# publish_list_shell

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/templates/calendar/partials/publish_list_shell.html` on 2026-05-14._

{% comment %} List mode shell for the Publish page. Contains tabs
(Queue, Drafts, Approvals, Sent), filter dropdowns, and tab content
area. Tab switching is HTMX partial swaps only - no full page reload. {%
endcomment %}

<div class="flex-1 flex flex-col min-h-0" x-data="publishList()">

<div class="flex flex-wrap items-center justify-between border-b border-stone-200 pb-0 -mx-3 sm:-mx-4 lg:-mx-6 px-3 sm:px-4 lg:px-6 gap-y-2">

<div class="flex items-center gap-1 -mb-px overflow-x-auto flex-nowrap">

Queue {% if queue_count
%}<span class="inline-flex items-center justify-center min-w-[20px] h-5 px-1.5 text-[11px] font-medium text-stone-500 bg-stone-100 rounded-full">{{
queue_count }}</span>{% endif %}

Drafts {% if drafts_count
%}<span class="inline-flex items-center justify-center min-w-[20px] h-5 px-1.5 text-[11px] font-medium text-stone-500 bg-stone-100 rounded-full">{{
drafts_count }}</span>{% endif %}

Approvals {% if approvals_count
%}<span class="inline-flex items-center justify-center min-w-[20px] h-5 px-1.5 text-[11px] font-medium text-stone-500 bg-stone-100 rounded-full">{{
approvals_count }}</span>{% endif %}

Sent {% if sent_count
%}<span class="inline-flex items-center justify-center min-w-[20px] h-5 px-1.5 text-[11px] font-medium text-stone-500 bg-stone-100 rounded-full">{{
sent_count }}</span>{% endif %}

</div>

<div class="flex items-center gap-2 pb-2 flex-shrink-0">

<div x-data="{
                    open: false,
                    pos: { top: 0, left: 0 },
                    updatePos() {
                        const r = this.$refs.btn.getBoundingClientRect();
                        this.pos = { top: r.bottom + 4 + 'px', left: (r.right - 224) + 'px' };
                    },
                    toggle() { this.open = !this.open; if (this.open) this.updatePos(); }
                 }" @click.away="open = false">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUgZmxleC1zaHJpbmstMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIyIj48Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSI0Ij48L2NpcmNsZT48cGF0aCBkPSJNMTYgOHY1YTMgMyAwIDAwNiAwdi0xYTEwIDEwIDAgMTAtMy45MiA3Ljk0IiAvPjwvc3ZnPg=="
class="w-3.5 h-3.5 flex-shrink-0" />
<span x-text="activeChannel ? (document.querySelector('[data-channel-id=\'' + activeChannel + '\']')?.textContent || 'Channel') : 'All Channels'"></span>
<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zIGgtMyBtbC0wLjUgdHJhbnNpdGlvbi10cmFuc2Zvcm0iIDpjbGFzcz0ib3BlbiAmYW1wOyZhbXA7ICYjMzk7cm90YXRlLTE4MCYjMzk7IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0IiBzdHJva2Utd2lkdGg9IjIuNSI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBkPSJNMTkgOWwtNyA3LTctNyIgLz48L3N2Zz4="
class="w-3 h-3 ml-0.5 transition-transform" />

<div class="w-56 bg-white rounded-xl shadow-lg ring-1 ring-stone-200 overflow-hidden"
x-show="open" x-transition:enter="transition ease-out duration-100"
x-transition:enter-start="opacity-0 scale-95"
x-transition:enter-end="opacity-100 scale-100"
x-transition:leave="transition ease-in duration-75"
x-transition:leave-start="opacity-100 scale-100"
x-transition:leave-end="opacity-0 scale-95"
:style="'position:fixed; top:' + pos.top + '; left:' + pos.left + '; z-index:9999;'"
x-cloak="">

<div class="p-2">

All Channels

{% for channel in channels_with_posts %}

{{ channel.account_name\|default:channel.account_handle }} ({{
channel.get_platform_display }})

{% endfor %}

</div>

</div>

</div>

<div x-data="{
                    open: false,
                    pos: { top: 0, left: 0 },
                    updatePos() {
                        const r = this.$refs.btn.getBoundingClientRect();
                        this.pos = { top: r.bottom + 4 + 'px', left: (r.right - 192) + 'px' };
                    },
                    toggle() { this.open = !this.open; if (this.open) this.updatePos(); }
                 }" @click.away="open = false">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUgZmxleC1zaHJpbmstMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIyIj48cGF0aCBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik03IDdoLjAxTTcgM2g1Yy41MTIgMCAxLjAyNC4xOTUgMS40MTQuNTg2bDcgN2EyIDIgMCAwMTAgMi44MjhsLTcgN2EyIDIgMCAwMS0yLjgyOCAwbC03LTdBMS45OTQgMS45OTQgMCAwMTMgMTJWN2E0IDQgMCAwMTQtNHoiIC8+PC9zdmc+"
class="w-3.5 h-3.5 flex-shrink-0" />
<span x-text="activeTag ? '#' + activeTag : 'All Tags'"></span> <img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zIGgtMyBtbC0wLjUgdHJhbnNpdGlvbi10cmFuc2Zvcm0iIDpjbGFzcz0ib3BlbiAmYW1wOyZhbXA7ICYjMzk7cm90YXRlLTE4MCYjMzk7IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0IiBzdHJva2Utd2lkdGg9IjIuNSI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBkPSJNMTkgOWwtNyA3LTctNyIgLz48L3N2Zz4="
class="w-3 h-3 ml-0.5 transition-transform" />

<div class="w-48 bg-white rounded-xl shadow-lg ring-1 ring-stone-200 overflow-hidden"
x-show="open" x-transition:enter="transition ease-out duration-100"
x-transition:enter-start="opacity-0 scale-95"
x-transition:enter-end="opacity-100 scale-100"
x-transition:leave="transition ease-in duration-75"
x-transition:leave-start="opacity-100 scale-100"
x-transition:leave-end="opacity-0 scale-95"
:style="'position:fixed; top:' + pos.top + '; left:' + pos.left + '; z-index:9999;'"
x-cloak="">

<div class="p-2 max-h-56 overflow-y-auto">

All Tags

{% for tag in all_tags %}

\#{{ tag }}

{% endfor %}

</div>

</div>

</div>

<div x-data="{
                    open: false,
                    search: '',
                    pos: { top: 0, left: 0 },
                    updatePos() {
                        const r = this.$refs.btn.getBoundingClientRect();
                        this.pos = { top: r.bottom + 4 + 'px', left: (r.right - 224) + 'px' };
                    },
                    toggle() { this.open = !this.open; if (this.open) { this.updatePos(); this.$nextTick(() =&gt; this.$refs.tzSearch?.focus()); } else { this.search = ''; } }
                 }" @click.away="open = false; search = ''">

<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zLjUgaC0zLjUgZmxleC1zaHJpbmstMCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIyIj48Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSIxMCI+PC9jaXJjbGU+PHBhdGggZD0iTTEyIDZ2Nmw0IDIiIC8+PC9zdmc+"
class="w-3.5 h-3.5 flex-shrink-0" />
<span x-text="displayTimezone.replace(/^(America|Europe|Asia|US|Pacific|Australia)\//, '') + (displayTimezone === '{{ workspace_timezone }}' ? ' (workspace)' : '')"></span>
<img
src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy0zIGgtMyBtbC0wLjUgdHJhbnNpdGlvbi10cmFuc2Zvcm0iIDpjbGFzcz0ib3BlbiAmYW1wOyZhbXA7ICYjMzk7cm90YXRlLTE4MCYjMzk7IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgdmlld2JveD0iMCAwIDI0IDI0IiBzdHJva2Utd2lkdGg9IjIuNSI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBkPSJNMTkgOWwtNyA3LTctNyIgLz48L3N2Zz4="
class="w-3 h-3 ml-0.5 transition-transform" />

<div class="w-56 bg-white rounded-xl shadow-lg ring-1 ring-stone-200 overflow-hidden"
x-show="open" x-transition:enter="transition ease-out duration-100"
x-transition:enter-start="opacity-0 scale-95"
x-transition:enter-end="opacity-100 scale-100"
x-transition:leave="transition ease-in duration-75"
x-transition:leave-start="opacity-100 scale-100"
x-transition:leave-end="opacity-0 scale-95"
:style="'position:fixed; top:' + pos.top + '; left:' + pos.left + '; z-index:9999;'"
x-cloak="">

<div class="p-2 border-b border-stone-100">

</div>

<div class="p-2 max-h-56 overflow-y-auto">

{% for tz in timezone_choices %}

{{
tz\|cut:"America/"\|cut:"Europe/"\|cut:"Asia/"\|cut:"US/"\|cut:"Pacific/"\|cut:"Australia/"
}}{% if tz == workspace_timezone %}
<span class="text-stone-400">(workspace)</span>{% endif %}

{% endfor %}

</div>

</div>

</div>

</div>

</div>

<div id="tab-content"
class="mt-4 flex-1 min-h-0 overflow-y-auto flex justify-center [&>*]:w-full [&>*]:max-w-4xl"
x-init="$nextTick(() =&gt; reloadTab())">

<div class="flex items-center justify-center py-12">

<div class="w-5 h-5 border-2 border-stone-300 border-t-orange-500 rounded-full animate-spin">

</div>

</div>

</div>

</div>
