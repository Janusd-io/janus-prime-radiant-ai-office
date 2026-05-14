---
type: source
source_type: laptop
title: style-guide-whitelabel
slug: style-guide-whitelabel
created: 2026-04-16
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/brightbean-studio/development_specs/style-guide-whitelabel.html
original_size: 71944
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:36Z"
project: brightbean-studio

---
<!-- jb:project-callout -->
> Part of [[brightbean-studio|Brightbean Studio]] — automatically linked by /janus-brain.


# style-guide-whitelabel

> Part of [[brightbean-studio|Brightbean Studio]] — captured by /janus-brain.

_Extracted from `brightbean-studio/development_specs/style-guide-whitelabel.html` on 2026-05-14._

<div class="hero">

<div class="hero-inner">

<div class="hero-badge">

<span class="dot"></span> White-Label Design System v1.0

</div>

# A style guide built to be *yours*

Every brand token is swappable. Change 10 CSS variables and the entire
system rebrands - colors, fonts, shadows, everything downstream cascades
automatically.

Display Font  
Georgia (system)

Body Font  
system-ui stack

Mono Font  
ui-monospace stack

Primary  
BrightBean Orange

CSS Framework  
Tailwind CSS

<div class="wl-callout">

<span class="wl-icon">🏷️</span>

**White-label ready.** Every brand-dependent value flows from the
`--brand-*` CSS variable block. To rebrand, swap only those tokens - all
semantic and component tokens inherit automatically. Fonts are also
brand tokens.

</div>

</div>

</div>

<div class="container">

<div class="section">

<div class="section-label">

00 - Architecture

</div>

<div class="section-title">

Token Layering

</div>

<div class="section-desc">

Three-layer token architecture. White-label clients only touch Layer 1.
Everything else cascades.

</div>

<div class="arch-diagram">

<div class="arch-box brand">

#### Brand Tokens

--brand-500, --brand-font-body\
**Swap these to rebrand**

</div>

<div class="arch-arrow">

→

</div>

<div class="arch-box semantic">

#### Semantic Tokens

--primary, --text-primary\
Reference brand tokens

</div>

<div class="arch-arrow">

→

</div>

<div class="arch-box component">

#### Component Tokens

btn-primary, card hover\
Reference semantic tokens

</div>

</div>

<div class="sub-label">

Example: Rebranding to a blue theme

</div>

<div class="code-block">

<span class="comment">/\* Only change this block to rebrand the entire
app \*/</span> <span class="key">--brand-50</span>:
<span class="val">\#EFF6FF</span>; <span class="comment">/\* tw: blue-50
\*/</span> <span class="key">--brand-100</span>:
<span class="val">\#DBEAFE</span>; <span class="comment">/\* tw:
blue-100 \*/</span> <span class="key">--brand-200</span>:
<span class="val">\#BFDBFE</span>; <span class="comment">/\* tw:
blue-200 \*/</span> <span class="key">--brand-500</span>:
<span class="val">\#3B82F6</span>; <span class="comment">/\* tw:
blue-500 - new PRIMARY \*/</span> <span class="key">--brand-600</span>:
<span class="val">\#2563EB</span>; <span class="comment">/\* tw:
blue-600 \*/</span> <span class="key">--brand-700</span>:
<span class="val">\#1D4ED8</span>; <span class="comment">/\* tw:
blue-700 \*/</span> <span class="key">--brand-font-display</span>:
<span class="val">'Palatino Linotype', Palatino, serif</span>;

</div>

</div>

<div class="section">

<div class="section-label">

01 - Color

</div>

<div class="section-title">

Palette

</div>

<div class="section-desc">

Warm stone neutrals paired with BrightBean orange. Accent colors are
fixed across white-label instances - they serve status and data viz, not
brand identity.

</div>

<div style="margin-bottom:28px">

<div class="sub-label">

Brand Scale (white-label swappable)

</div>

<div class="color-grid">

<div class="color-card">

<div class="color-swatch" style="background:var(--brand-50)"
hex="#FFF7ED">

</div>

<div class="color-info">

<div class="color-name">

50

</div>

<div class="color-tw">

orange-50

</div>

</div>

</div>

<div class="color-card">

<div class="color-swatch" style="background:var(--brand-100)"
hex="#FFEDD5">

</div>

<div class="color-info">

<div class="color-name">

100

</div>

<div class="color-tw">

orange-100

</div>

</div>

</div>

<div class="color-card">

<div class="color-swatch" style="background:var(--brand-200)"
hex="#FED7AA">

</div>

<div class="color-info">

<div class="color-name">

200

</div>

<div class="color-tw">

orange-200

</div>

</div>

</div>

<div class="color-card">

<div class="color-swatch" style="background:var(--brand-300)"
hex="#FDBA74">

</div>

<div class="color-info">

<div class="color-name">

300

</div>

<div class="color-tw">

orange-300

</div>

</div>

</div>

<div class="color-card">

<div class="color-swatch" style="background:var(--brand-400)"
hex="#FB923C">

</div>

<div class="color-info">

<div class="color-name">

400

</div>

<div class="color-tw">

orange-400

</div>

</div>

</div>

<div class="color-card">

<div class="color-swatch" style="background:var(--brand-500)"
hex="#F97316">

</div>

<div class="color-info">

<div class="color-name">

500 ★

</div>

<div class="color-tw">

orange-500

</div>

</div>

</div>

<div class="color-card">

<div class="color-swatch" style="background:var(--brand-600)"
hex="#EA580C">

</div>

<div class="color-info">

<div class="color-name">

600

</div>

<div class="color-tw">

orange-600

</div>

</div>

</div>

<div class="color-card">

<div class="color-swatch" style="background:var(--brand-700)"
hex="#C2410C">

</div>

<div class="color-info">

<div class="color-name">

700

</div>

<div class="color-tw">

orange-700

</div>

</div>

</div>

<div class="color-card">

<div class="color-swatch" style="background:var(--brand-800)"
hex="#9A3412">

</div>

<div class="color-info">

<div class="color-name">

800

</div>

<div class="color-tw">

orange-800

</div>

</div>

</div>

<div class="color-card">

<div class="color-swatch" style="background:var(--brand-900)"
hex="#7C2D12">

</div>

<div class="color-info">

<div class="color-name">

900

</div>

<div class="color-tw">

orange-900

</div>

</div>

</div>

</div>

</div>

<div style="margin-bottom:28px">

<div class="sub-label">

Neutrals (stone - warm-tinted grays)

</div>

<div class="color-grid">

<div class="color-card">

<div class="color-swatch" style="background:var(--neutral-950)"
hex="#171412">

</div>

<div class="color-info">

<div class="color-name">

950

</div>

<div class="color-tw">

stone-950

</div>

</div>

</div>

<div class="color-card">

<div class="color-swatch" style="background:var(--neutral-900)"
hex="#1C1917">

</div>

<div class="color-info">

<div class="color-name">

900

</div>

<div class="color-tw">

stone-900

</div>

</div>

</div>

<div class="color-card">

<div class="color-swatch" style="background:var(--neutral-700)"
hex="#44403C">

</div>

<div class="color-info">

<div class="color-name">

700

</div>

<div class="color-tw">

stone-700

</div>

</div>

</div>

<div class="color-card">

<div class="color-swatch" style="background:var(--neutral-500)"
hex="#78716C">

</div>

<div class="color-info">

<div class="color-name">

500

</div>

<div class="color-tw">

stone-500

</div>

</div>

</div>

<div class="color-card">

<div class="color-swatch" style="background:var(--neutral-300)"
hex="#D6D3D1">

</div>

<div class="color-info">

<div class="color-name">

300

</div>

<div class="color-tw">

stone-300

</div>

</div>

</div>

<div class="color-card">

<div class="color-swatch"
style="background:var(--neutral-200);border:1px solid var(--neutral-300)"
hex="#E7E5E4">

</div>

<div class="color-info">

<div class="color-name">

200

</div>

<div class="color-tw">

stone-200

</div>

</div>

</div>

<div class="color-card">

<div class="color-swatch"
style="background:var(--neutral-100);border:1px solid var(--neutral-200)"
hex="#F5F5F4">

</div>

<div class="color-info">

<div class="color-name">

100

</div>

<div class="color-tw">

stone-100

</div>

</div>

</div>

<div class="color-card">

<div class="color-swatch"
style="background:var(--neutral-50);border:1px solid var(--neutral-200)"
hex="#FAFAF9">

</div>

<div class="color-info">

<div class="color-name">

50

</div>

<div class="color-tw">

stone-50

</div>

</div>

</div>

</div>

</div>

<div>

<div class="sub-label">

Status & Accents (fixed across white-label)

</div>

<div class="color-grid">

<div class="color-card">

<div class="color-swatch" style="background:var(--success-500)"
hex="#22C55E">

</div>

<div class="color-info">

<div class="color-name">

Success

</div>

<div class="color-tw">

green-500

</div>

</div>

</div>

<div class="color-card">

<div class="color-swatch" style="background:var(--warning-500)"
hex="#EAB308">

</div>

<div class="color-info">

<div class="color-name">

Warning

</div>

<div class="color-tw">

yellow-500

</div>

</div>

</div>

<div class="color-card">

<div class="color-swatch" style="background:var(--error-500)"
hex="#EF4444">

</div>

<div class="color-info">

<div class="color-name">

Error

</div>

<div class="color-tw">

red-500

</div>

</div>

</div>

<div class="color-card">

<div class="color-swatch" style="background:var(--info-500)"
hex="#3B82F6">

</div>

<div class="color-info">

<div class="color-name">

Info

</div>

<div class="color-tw">

blue-500

</div>

</div>

</div>

<div class="color-card">

<div class="color-swatch" style="background:var(--accent-teal)"
hex="#14B8A6">

</div>

<div class="color-info">

<div class="color-name">

Teal

</div>

<div class="color-tw">

teal-500

</div>

</div>

</div>

<div class="color-card">

<div class="color-swatch" style="background:var(--accent-indigo)"
hex="#6366F1">

</div>

<div class="color-info">

<div class="color-name">

Indigo

</div>

<div class="color-tw">

indigo-500

</div>

</div>

</div>

<div class="color-card">

<div class="color-swatch" style="background:var(--accent-rose)"
hex="#F43F5E">

</div>

<div class="color-info">

<div class="color-name">

Rose

</div>

<div class="color-tw">

rose-500

</div>

</div>

</div>

</div>

</div>

</div>

<div class="section">

<div class="section-label">

02 - Typography

</div>

<div class="section-title">

Type System

</div>

<div class="section-desc">

Zero external downloads. Georgia provides serif warmth for display text.
The system-ui stack handles all UI and body text. ui-monospace covers
data and code. All are white-label swappable via brand tokens.

</div>

<div class="type-specimen">

<div class="type-row">

<div class="type-meta">

<div class="font-name">

Georgia

</div>

<div class="font-stack">

Georgia, 'Times New Roman', serif

</div>

<div class="font-usage">

Page titles, hero headings, metric callouts. Swappable via
--brand-font-display.

</div>

</div>

<div class="type-preview-display">

Schedule your story, *beautifully.*

</div>

</div>

<div class="type-row">

<div class="type-meta">

<div class="font-name">

system-ui

</div>

<div class="font-stack">

system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif

</div>

<div class="font-usage">

Body text, buttons, labels, nav, forms. Renders as SF Pro on macOS,
Segoe UI on Windows, Roboto on Android.

</div>

</div>

<div class="type-preview-body">

Create, schedule, and publish content across all your platforms from a
single dashboard. Track engagement in real-time and let AI suggest the
perfect posting window for your audience.

</div>

</div>

<div class="type-row">

<div class="type-meta">

<div class="font-name">

ui-monospace

</div>

<div class="font-stack">

ui-monospace, SFMono-Regular, Consolas, monospace

</div>

<div class="font-usage">

Data tables, timestamps, metrics, tokens, code. Renders as SF Mono on
macOS, Cascadia/Consolas on Windows.

</div>

</div>

<div class="type-preview-mono">

engagement_rate: 4.8% impressions: 12,847 scheduled: 2026-03-25T14:00Z

</div>

</div>

</div>

<div class="type-scale">

<div class="ts-row" style="background:var(--surface-1)">

<span class="ts-name">Token</span><span class="ts-size"
style="color:var(--text-tertiary)">Size</span><span class="ts-tw"
style="color:var(--text-tertiary)">Tailwind</span><span class="ts-sample"
style="font-weight:600;font-size:0.8125rem;color:var(--text-tertiary)">Usage</span>

</div>

<div class="ts-row">

<span class="ts-name">xs</span><span class="ts-size">12px</span><span class="ts-tw">text-xs</span><span class="ts-sample"
style="font-size:12px">Overlines, hints, fine print</span>

</div>

<div class="ts-row">

<span class="ts-name">sm</span><span class="ts-size">14px</span><span class="ts-tw">text-sm</span><span class="ts-sample"
style="font-size:14px">Labels, secondary text, compact UI</span>

</div>

<div class="ts-row">

<span class="ts-name">base</span><span class="ts-size">15px</span><span class="ts-tw">text-base</span><span class="ts-sample"
style="font-size:15px">Default body, paragraphs</span>

</div>

<div class="ts-row">

<span class="ts-name">lg</span><span class="ts-size">18px</span><span class="ts-tw">text-lg</span><span class="ts-sample"
style="font-size:18px">Lead text, card titles</span>

</div>

<div class="ts-row">

<span class="ts-name">xl</span><span class="ts-size">20px</span><span class="ts-tw">text-xl</span><span class="ts-sample"
style="font-size:20px">Sub-headings, drawer titles</span>

</div>

<div class="ts-row">

<span class="ts-name">2xl</span><span class="ts-size">24px</span><span class="ts-tw">text-2xl</span><span class="ts-sample"
style="font-size:24px">Section headings</span>

</div>

<div class="ts-row">

<span class="ts-name">3xl</span><span class="ts-size">30px</span><span class="ts-tw">text-3xl</span><span class="ts-sample"
style="font-size:30px;font-family:var(--font-display)">Page
titles</span>

</div>

<div class="ts-row">

<span class="ts-name">4xl+</span><span class="ts-size">36–48px</span><span class="ts-tw">text-4xl</span><span class="ts-sample"
style="font-size:36px;font-family:var(--font-display);letter-spacing:-0.025em">Hero
display</span>

</div>

</div>

</div>

<div class="section">

<div class="section-label">

03 - Foundations

</div>

<div class="section-title">

Spacing, Radius & Elevation

</div>

<div class="section-desc">

4px base grid. Tailwind's native spacing scale. Pill radii for actions,
softer rounding for containers. Shadows use warm-tinted blacks.

</div>

<div class="foundations-grid">

<div>

<div class="sub-label">

Spacing Scale

</div>

<div class="spacing-visual">

<div class="sp-row">

<span class="sp-label">1</span>

<div class="sp-bar" style="width:16px">

</div>

<span class="sp-value">4px</span><span class="sp-tw">p-1</span>

</div>

<div class="sp-row">

<span class="sp-label">2</span>

<div class="sp-bar" style="width:32px">

</div>

<span class="sp-value">8px</span><span class="sp-tw">p-2</span>

</div>

<div class="sp-row">

<span class="sp-label">3</span>

<div class="sp-bar" style="width:48px">

</div>

<span class="sp-value">12px</span><span class="sp-tw">p-3</span>

</div>

<div class="sp-row">

<span class="sp-label">4</span>

<div class="sp-bar" style="width:64px">

</div>

<span class="sp-value">16px</span><span class="sp-tw">p-4</span>

</div>

<div class="sp-row">

<span class="sp-label">6</span>

<div class="sp-bar" style="width:96px">

</div>

<span class="sp-value">24px</span><span class="sp-tw">p-6</span>

</div>

<div class="sp-row">

<span class="sp-label">8</span>

<div class="sp-bar" style="width:128px">

</div>

<span class="sp-value">32px</span><span class="sp-tw">p-8</span>

</div>

<div class="sp-row">

<span class="sp-label">12</span>

<div class="sp-bar" style="width:192px">

</div>

<span class="sp-value">48px</span><span class="sp-tw">p-12</span>

</div>

<div class="sp-row">

<span class="sp-label">16</span>

<div class="sp-bar" style="width:256px">

</div>

<span class="sp-value">64px</span><span class="sp-tw">p-16</span>

</div>

</div>

</div>

<div>

<div class="sub-label">

Border Radius

</div>

<div class="radius-grid" style="margin-bottom:32px">

<div class="radius-item">

<div class="radius-box" style="border-radius:var(--radius-sm)">

</div>

4px\
rounded

</div>

<div class="radius-item">

<div class="radius-box" style="border-radius:var(--radius-md)">

</div>

6px\
rounded-md

</div>

<div class="radius-item">

<div class="radius-box" style="border-radius:var(--radius-lg)">

</div>

8px\
rounded-lg

</div>

<div class="radius-item">

<div class="radius-box" style="border-radius:var(--radius-xl)">

</div>

12px\
rounded-xl

</div>

<div class="radius-item">

<div class="radius-box" style="border-radius:var(--radius-2xl)">

</div>

16px\
rounded-2xl

</div>

<div class="radius-item">

<div class="radius-box" style="border-radius:var(--radius-full)">

</div>

pill\
rounded-full

</div>

</div>

<div class="sub-label">

Elevation

</div>

<div class="shadow-row">

<div class="shadow-card" style="box-shadow:var(--shadow-xs)">

xs\
shadow-xs

</div>

<div class="shadow-card" style="box-shadow:var(--shadow-sm)">

sm\
shadow-sm

</div>

<div class="shadow-card" style="box-shadow:var(--shadow-md)">

md\
shadow-md

</div>

<div class="shadow-card" style="box-shadow:var(--shadow-lg)">

lg\
shadow-lg

</div>

</div>

</div>

</div>

</div>

<div class="section">

<div class="section-label">

04 - Components

</div>

<div class="section-title">

Buttons

</div>

<div class="section-desc">

Pill-shaped with generous horizontal padding. Primary gets a
brand-colored glow shadow. All transitions use the ease-out curve.

</div>

<div class="btn-grid">

<div>

<div class="btn-row-label">

Variants

</div>

<div class="btn-row">

Schedule Post

Save Draft

Learn More

Delete

</div>

<div class="tw-hint">

bg-orange-500 text-white rounded-full px-6 py-2.5 font-semibold
shadow-\[0_4px_14px_rgba(249,115,22,0.28)\]

</div>

</div>

<div>

<div class="btn-row-label">

Sizes

</div>

<div class="btn-row">

Small

Default

Large

</div>

</div>

<div>

<div class="btn-row-label">

With Icons

</div>

<div class="btn-row">

⚡ Publish Now

📅 Pick Date

＋

⚙

🔔

</div>

</div>

</div>

</div>

<div class="section">

<div class="section-label">

05 - Components

</div>

<div class="section-title">

Forms, Badges & Avatars

</div>

<div class="section-desc">

Inputs use the brand color for focus rings - this automatically
rebrands. Error states always use the fixed red-500 regardless of brand.

</div>

<div class="component-grid">

<div class="input-showcase">

<div class="form-group">

Post caption

<span class="form-hint">Supports hashtags and @mentions</span>

</div>

<div class="form-group">

Schedule time

</div>

<div class="form-group">

Campaign tag <span class="form-error">⚠ Tags cannot contain special
characters</span>

</div>

<div class="tw-hint">

focus:ring-2 focus:ring-orange-200 focus:border-orange-500

</div>

</div>

<div>

<div class="component-block-title">

Badges

</div>

<div class="badge-grid" style="margin-bottom:24px;">

<span class="badge"
style="background:var(--primary-soft);color:var(--brand-700)">Scheduled</span>
<span class="badge"
style="background:var(--success-50);color:var(--success-700)">Published</span>
<span class="badge"
style="background:var(--warning-50);color:var(--warning-700)">Draft</span>
<span class="badge"
style="background:var(--error-50);color:var(--error-700)">Failed</span>
<span class="badge"
style="background:var(--info-50);color:var(--info-700)">In Review</span>
<span class="badge"
style="background:var(--accent-rose-soft);color:#9F1239">Trending</span>

</div>

<div class="component-block-title">

Avatars

</div>

<div class="avatar-row" style="margin-bottom:16px;">

<div class="avatar avatar-xs" style="background:var(--error-500)">

J

</div>

<div class="avatar avatar-sm" style="background:var(--accent-teal)">

E

</div>

<div class="avatar avatar-md" style="background:var(--primary)">

M

</div>

<div class="avatar avatar-lg" style="background:var(--accent-sky)">

A

</div>

</div>

<div class="component-block-title">

Avatar Stack

</div>

<div class="avatar-stack">

<div class="avatar avatar-md" style="background:var(--primary)">

J

</div>

<div class="avatar avatar-md" style="background:var(--error-500)">

E

</div>

<div class="avatar avatar-md" style="background:var(--accent-teal)">

M

</div>

<div class="avatar avatar-md" style="background:var(--accent-sky)">

+3

</div>

</div>

</div>

</div>

</div>

<div class="section">

<div class="section-label">

06 - Patterns

</div>

<div class="section-title">

Cards & Post Preview

</div>

<div class="section-desc">

Cards lift on hover with a shadow bloom and transparent border - the
same "reveal" interaction used by Sprout Social and [[linear|Linear]]. Metric
callouts use the display serif for editorial weight.

</div>

<div class="card-showcase" style="margin-bottom:36px;">

<div class="card">

<div class="card-header">

<div class="card-icon"
style="background:var(--primary-soft); color:var(--primary);">

📊

</div>

<span class="card-tag"
style="background:var(--success-50);color:var(--success-700)">+12%</span>

</div>

### Total Reach

<div class="card-metric">

148.2K

</div>

<span class="card-change up">↑ 12.4% from last week</span>

</div>

<div class="card">

<div class="card-header">

<div class="card-icon"
style="background:var(--accent-rose-soft); color:var(--accent-rose);">

🔥

</div>

<span class="card-tag"
style="background:var(--accent-rose-soft);color:#9F1239">Hot</span>

</div>

### Engagement Rate

<div class="card-metric">

4.82%

</div>

<span class="card-change up">↑ 0.7% from last week</span>

</div>

<div class="card">

<div class="card-header">

<div class="card-icon"
style="background:var(--accent-sky-soft); color:var(--accent-sky);">

📅

</div>

<span class="card-tag"
style="background:var(--warning-50);color:var(--warning-700)">Pending</span>

</div>

### Scheduled Posts

<div class="card-metric">

23

</div>

Next up in 2 hours

</div>

</div>

<div class="component-block-title">

Post Preview Card

</div>

<div class="post-card">

<div class="post-header">

<div class="avatar avatar-md" style="background:var(--primary)">

S

</div>

<div>

<div class="post-author">

Social Suite

</div>

<div class="post-handle">

@socialsuite · Scheduled for 2:00 PM

</div>

</div>

<div class="post-platforms">

<div class="platform-dot" style="background:#000000" title="X">

𝕏

</div>

<div class="platform-dot" style="background:#0A66C2" title="[[linkedin|LinkedIn]]">

in

</div>

<div class="platform-dot" style="background:#E4405F" title="Instagram">

ig

</div>

</div>

</div>

<div class="post-body">

Just shipped our new AI-powered scheduling engine - it learns your
audience's habits and finds the perfect window. 🚀\
\
Early results: 23% more engagement on average.

</div>

<div class="post-image">

📸 Image preview

</div>

<div class="post-actions">

<span class="post-action">♡ 0</span> <span class="post-action">↻
0</span> <span class="post-action">💬 0</span> <span class="post-action"
style="margin-left:auto">✏️ Edit</span>

</div>

</div>

</div>

<div class="section">

<div class="section-label">

07 - Feedback

</div>

<div class="section-title">

Toasts

</div>

<div class="section-desc">

Status-colored tinted backgrounds with matching borders. These use the
fixed semantic palette - they never change with white-label branding.

</div>

<div class="toast-showcase">

<div class="toast success">

<span class="toast-icon">✓</span> Post published to 3 platforms

</div>

<div class="toast warning">

<span class="toast-icon">⚠</span> Image exceeds Twitter's recommended
size

</div>

<div class="toast error">

<span class="toast-icon">✕</span> Failed to connect Instagram - re-auth
required

</div>

<div class="toast info">

<span class="toast-icon">ℹ</span> Best posting time today: 2:00 PM

</div>

</div>

</div>

<div class="section">

<div class="section-label">

08 - Navigation

</div>

<div class="section-title">

Sidebar Pattern

</div>

<div class="section-desc">

Vertical nav with icon + label. Active state uses the brand-soft
background with brand-700 text - this auto-rebrands. Notification badges
always use error red.

</div>

<div class="nav-sample">

<div class="nav-logo">

<div class="nav-logo-mark">

S

</div>

<div class="nav-logo-text">

Social Suite

</div>

</div>

<div class="nav-item active">

<span class="nav-icon">🏠</span> Dashboard

</div>

<div class="nav-item">

<span class="nav-icon">✏️</span> Compose

</div>

<div class="nav-item">

<span class="nav-icon">📅</span> Calendar

</div>

<div class="nav-item">

<span class="nav-icon">📥</span> Inbox <span class="nav-badge">5</span>

</div>

<div class="nav-section-label">

Analytics

</div>

<div class="nav-item">

<span class="nav-icon">📊</span> Performance

</div>

<div class="nav-item">

<span class="nav-icon">👥</span> Audience

</div>

<div class="nav-section-label">

Settings

</div>

<div class="nav-item">

<span class="nav-icon">🔗</span> Connections

</div>

<div class="nav-item">

<span class="nav-icon">⚙️</span> Preferences

</div>

</div>

</div>

<div class="section">

<div class="section-label">

09 - Motion

</div>

<div class="section-title">

Transitions & Curves

</div>

<div class="section-desc">

Two curves: ease-out for standard interactions, spring for playful
moments. Hover these boxes.

</div>

<div class="motion-demo">

<div class="motion-box m-ease-out">

↑\
ease-out

</div>

<div class="motion-box m-spring">

⊕\
spring

</div>

<div class="motion-box m-rotate">

↻\
rotate

</div>

</div>

<div class="timing-card">

<div class="tc-title">

Timing Tokens

</div>

<div class="tc-row">

--dur-fast : 150ms - focus rings, color swaps

</div>

<div class="tc-row">

--dur-base : 200ms - card hovers, buttons   *tw: duration-200*

</div>

<div class="tc-row">

--dur-slow : 350ms - page transitions, modals

</div>

<div class="tc-row">

--ease-out : cubic-bezier(0.16, 1, 0.3, 1)

</div>

<div class="tc-row">

--ease-spring : cubic-bezier(0.34, 1.56, 0.64, 1)

</div>

</div>

</div>

<div class="section">

<div class="section-label">

10 - Reference

</div>

<div class="section-title">

Tailwind Class Mapping

</div>

<div class="section-desc">

How CSS variable tokens map to Tailwind utility classes. Extend your
tailwind.config.js to expose the brand tokens as custom colors.

</div>

<div class="code-block" style="margin-bottom:24px">

<span class="comment">// tailwind.config.js</span>
<span class="fn">module</span>.<span class="fn">exports</span> = {
<span class="key">theme</span>: { <span class="key">extend</span>: {
<span class="key">colors</span>: { <span class="key">brand</span>: {
<span class="val">50</span>: <span class="val">'var(--brand-50)'</span>,
<span class="val">100</span>:
<span class="val">'var(--brand-100)'</span>,
<span class="val">200</span>:
<span class="val">'var(--brand-200)'</span>,
<span class="val">500</span>:
<span class="val">'var(--brand-500)'</span>,
<span class="val">600</span>:
<span class="val">'var(--brand-600)'</span>,
<span class="val">700</span>:
<span class="val">'var(--brand-700)'</span>, }, },
<span class="key">fontFamily</span>: { <span class="val">display</span>:
<span class="val">'var(--font-display)'</span>,
<span class="val">body</span>:
<span class="val">'var(--font-body)'</span>,
<span class="val">mono</span>:
<span class="val">'var(--font-mono)'</span>, }, }, }, }

</div>

| Purpose | CSS Variable | Tailwind Class | Preview |
|----|----|----|----|
| Primary button bg | var(--primary) | bg-brand-500 | <span class="swatch" style="background:var(--primary)"></span> |
| Primary hover | var(--primary-hover) | hover:bg-brand-600 | <span class="swatch" style="background:var(--primary-hover)"></span> |
| Soft background | var(--primary-soft) | bg-brand-50 | <span class="swatch" style="background:var(--primary-soft)"></span> |
| Focus ring | var(--primary-ring) | ring-brand-200 | <span class="swatch" style="background:var(--primary-ring)"></span> |
| Text on brand bg | var(--text-inverse) | text-white | <span class="swatch" style="background:white;border-color:var(--neutral-300)"></span> |
| Body text | var(--text-primary) | text-stone-900 | <span class="swatch" style="background:var(--text-primary)"></span> |
| Secondary text | var(--text-secondary) | text-stone-600 | <span class="swatch" style="background:var(--text-secondary)"></span> |
| Muted text | var(--text-tertiary) | text-stone-500 | <span class="swatch" style="background:var(--text-tertiary)"></span> |
| Page background | var(--surface-1) | bg-stone-50 | <span class="swatch" style="background:var(--surface-1);border-color:var(--neutral-300)"></span> |
| Card background | var(--surface-0) | bg-white | <span class="swatch" style="background:white;border-color:var(--neutral-300)"></span> |
| Border | var(--border) | border-stone-200 | <span class="swatch" style="background:var(--border)"></span> |

</div>

<div class="section">

<div class="section-label">

11 - Principles

</div>

<div class="section-title">

Design Guidelines

</div>

<div class="section-desc">

Rules that keep the system coherent across white-label instances.

</div>

<div class="guidelines">

<div class="guideline-card">

#### <span class="do">✓</span> Brand tokens only for identity

Only use --brand-\* for elements that represent the client's identity:
primary buttons, active nav states, logo marks, focus rings. Status
colors (red/green/yellow/blue) are fixed.

</div>

<div class="guideline-card">

#### <span class="dont">✕</span> Don't brand status indicators

Error states, success messages, and warnings must always use the fixed
semantic palette. A red brand should never produce red success badges -
confusion over interaction matters more than consistency.

</div>

<div class="guideline-card">

#### <span class="do">✓</span> Test every rebrand at extremes

Every white-label theme must be tested with very dark brands (navy,
black) and very light brands (yellow, lime). Check contrast ratios:
text-on-brand must pass WCAG AA (4.5:1 for body, 3:1 for large text).

</div>

<div class="guideline-card">

#### <span class="dont">✕</span> Don't use pure gray neutrals

All neutrals use the stone scale (warm undertone). Pure grays feel cold
and clinical. Stone keeps the interface approachable regardless of brand
color.

</div>

<div class="guideline-card">

#### <span class="do">✓</span> Keep serif in display only

The display font (Georgia by default) is for heroes, page titles, and
metric callouts only. Never use it in buttons, labels, nav, or form
fields - those always use the body font.

</div>

<div class="guideline-card">

#### <span class="dont">✕</span> Don't assume font availability

White-label clients can set custom display fonts via
--brand-font-display, but body and mono stacks should remain system
fonts for reliability. If a client needs a custom body font, use
@font-face with fallbacks.

</div>

</div>

</div>

</div>

<div class="footer">

White-label design system for **Social Suite** - powered by BrightBean
Orange, system fonts, and Tailwind CSS.

</div>
