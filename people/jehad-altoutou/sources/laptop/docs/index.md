---
type: source
source_type: laptop
title: index
slug: index
created: 2026-03-31
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/VibeVoice/demo/web/index.html
original_size: 27379
original_ext: .html
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:33Z"
project: vibevoice

---
<!-- jb:project-callout -->
> Part of [[vibevoice|VibeVoice]] — automatically linked by /janus-brain.


# index

_Extracted from `[[vibevoice|VibeVoice]]/demo/web/index.html` on 2026-05-14._

VibeVoice-Realtime TTS Demo

<style>
  :root {
    --bg: #f5f7fc;
    --surface: #ffffff;
    --accent: #5562ff;
    --accent-strong: #3f4dff;
    --text-primary: #1f2742;
    --text-muted: #5d6789;
    --border: rgba(85, 98, 255, 0.18);
    --shadow: 0 18px 45px rgba(31, 39, 66, 0.08);
  }

  .helper-text {
    font-size: 12px;
    color: #8a93b5;
  }

  * {
    box-sizing: border-box;
  }

  body {
    margin: 0;
    background: var(--bg);
    font-family: 'Inter', 'Segoe UI', Roboto, Helvetica, sans-serif;
    color: var(--text-primary);
    display: flex;
    justify-content: center;
    padding: 48px 20px;
  }

  .app-shell {
    width: min(960px, 100%);
    background: var(--surface);
    border-radius: 20px;
    padding: 36px 40px 44px;
    box-shadow: var(--shadow);
    display: flex;
    flex-direction: column;
    gap: 28px;
  }

  h1 {
    margin: 0;
    text-align: center;
    font-size: 30px;
    font-weight: 700;
    letter-spacing: 0.01em;
  }

  .panel {
    display: flex;
    flex-direction: column;
    gap: 10px;
  }

  .field {
    display: flex;
    flex-direction: column;
    gap: 8px;
  }

  .field-label {
    font-weight: 600;
    font-size: 15px;
    color: var(--text-primary);
  }

  .text-input {
    width: 100%;
    min-height: 140px;
    max-height: 240px;
    border: 1px solid rgba(31, 39, 66, 0.14);
    border-radius: 12px;
    padding: 14px 16px;
    font-size: 15px;
    line-height: 1.6;
    font-family: inherit;
    background: #f9faff;
    transition: border-color 0.2s, box-shadow 0.2s;
    resize: vertical;
  }

  .text-input:focus {
    outline: none;
    border-color: var(--accent);
    box-shadow: 0 0 0 3px rgba(85, 98, 255, 0.18);
    background: #fff;
  }

  #streamingPreviewContainer {
    border-radius: 14px;
    border: 1px solid var(--border);
    background: [[linear|linear]]-gradient(135deg, #eef2ff 0%, #f7f9ff 100%);
    padding: 18px 20px;
    box-shadow: inset 0 1px 2px rgba(85, 98, 255, 0.12);
  }

  #streamingPreviewHeader {
    font-weight: 600;
    color: var(--text-primary);
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 14px;
    margin-bottom: 8px;
  }

  #streamingPreviewNote {
    font-weight: 400;
    font-size: 12px;
    color: var(--text-muted);
  }

  #streamingPreview {
    min-height: 70px;
    padding: 10px 12px;
    border-radius: 10px;
    background: rgba(255, 255, 255, 0.9);
    border: 1px solid rgba(85, 98, 255, 0.25);
    font-family: 'Courier New', Courier, monospace;
    font-size: 14px;
    line-height: 1.5;
    color: var(--text-primary);
    white-space: pre-wrap;
  }

  #streamingPreview.streaming-active::after {
    content: "";
    display: inline-block;
    width: 2px;
    height: 1.1em;
    background: var(--accent);
    margin-left: 2px;
    animation: previewCaret 0.9s steps(1) infinite;
    vertical-align: bottom;
  }

  @keyframes previewCaret {
    0%, 50% {
      opacity: 1;
    }
    51%, 100% {
      opacity: 0;
    }
  }

  .control-panel {
    display: flex;
    flex-direction: column;
    gap: 18px;
  }

  .inline-field {
    display: flex;
    flex-direction: column;
    gap: 6px;
  }

  .select-control {
    width: 220px;
    border: 1px solid rgba(31, 39, 66, 0.14);
    border-radius: 10px;
    padding: 8px 12px;
    font-size: 14px;
    font-family: inherit;
    background: #fbfcff;
    color: var(--text-primary);
    transition: border-color 0.2s, box-shadow 0.2s;
  }

  .select-control:focus {
    outline: none;
    border-color: var(--accent);
    box-shadow: 0 0 0 3px rgba(85, 98, 255, 0.18);
    background: #fff;
  }

  .control-row {
    display: flex;
    align-items: center;
    flex-wrap: wrap;
    gap: 20px 28px;
  }

  .range-control {
    display: flex;
    align-items: center;
    gap: 12px;
    font-size: 14px;
    color: var(--text-primary);
  }

  .range-control input[type="range"] {
    width: 200px;
    accent-color: var(--accent);
  }

  .range-value {
    font-weight: 600;
    color: var(--text-primary);
    min-width: 42px;
    text-align: right;
  }

  #playback {
    background: var(--accent);
    color: #fff;
    border: none;
    padding: 10px 24px;
    border-radius: 999px;
    cursor: pointer;
    font-weight: 600;
    font-size: 14px;
    box-shadow: 0 8px 16px rgba(85, 98, 255, 0.25);
    transition: transform 0.15s, box-shadow 0.15s, background 0.15s;
  }

  #playback:hover {
    transform: translateY(-1px);
    box-shadow: 0 10px 20px rgba(85, 98, 255, 0.28);
  }

  #playback:active {
    transform: translateY(0);
  }

  #playback.playing {
    background: var(--accent-strong);
  }

  .secondary-btn {
    border: 1px solid rgba(31, 39, 66, 0.18);
    background: #f1f3ff;
    color: var(--text-primary);
    padding: 8px 18px;
    border-radius: 999px;
    cursor: pointer;
    font-size: 13px;
    font-weight: 500;
    transition: background 0.15s, border-color 0.15s;
  }

  .secondary-btn:hover {
    background: #e6e9ff;
    border-color: rgba(31, 39, 66, 0.26);
  }

  .secondary-btn:disabled {
    opacity: 0.55;
    cursor: not-allowed;
  }

  .metrics {
    display: flex;
    flex-wrap: wrap;
    gap: 16px 32px;
    font-size: 14px;
    color: var(--text-muted);
  }

  .metrics span {
    display: flex;
    align-items: baseline;
    gap: 6px;
  }

  .metrics span strong {
    color: var(--text-primary);
    font-weight: 600;
  }

  .metric-unit {
    color: var(--text-muted);
    font-size: 13px;
  }

  #logOutput {
    max-height: 260px;
    overflow-y: auto;
    background: #f7f9ff;
    color: var(--text-primary);
    padding: 16px 18px;
    border: 1px solid rgba(31, 39, 66, 0.12);
    border-radius: 12px;
    font-size: 13px;
    line-height: 1.6;
    box-shadow: inset 0 1px 2px rgba(15, 23, 42, 0.06);
    font-family: 'Fira Code', 'Courier New', Courier, monospace;
    margin-top: 0px;
  }

  @media (max-width: 720px) {
    .app-shell {
      padding: 28px 20px 36px;
      gap: 24px;
    }

    .select-control {
      width: 100%;
    }

    .control-row {
      flex-direction: column;
      align-items: flex-start;
      gap: 16px;
    }

    #playback {
      width: 100%;
      text-align: center;
    }
  }
</style>

<div class="app-shell">

# VibeVoice-Realtime TTS Demo

<div class="section panel">

<span class="field-label">Text</span>

<div id="streamingPreviewContainer">

<div id="streamingPreviewHeader">

Streaming Input Text

</div>

<div id="streamingPreview" aria-live="polite">

This area will display the streaming input text in real time.

</div>

</div>

</div>

<span class="helper-text">This demo requires the full text to be
provided upfront. The model then receives the text via streaming input
during synthesis.\
For non-punctuation special characters, applying text normalization
before processing often yields better results.</span>

<div class="section panel control-panel">

<div class="inline-field">

<span class="field-label">Speaker</span> Loading...

</div>

<div class="control-row">

CFG <span id="cfgValue" class="range-value">1.5</span> Inference Steps
<span id="stepsValue" class="range-value">5</span>

Reset Controls

</div>

<div class="control-row">

Start

Save

</div>

</div>

<div class="section panel">

<div class="metrics">

Model Generated Audio**0.00**<span class="metric-unit">s</span> Audio
Played**0.00**<span class="metric-unit">s</span>

</div>

</div>

<div class="section panel">

<span class="field-label">Runtime Logs</span>

```
```

</div>

</div>
