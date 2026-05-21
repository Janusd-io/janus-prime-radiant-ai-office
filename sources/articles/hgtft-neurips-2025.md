---
type: source
source_type: article
title: Heterogeneous Graph Temporal Fusion Transformer for Time Series Forecasting in Multiphysics Systems (HGTFT — NeurIPS 2025 submission)
slug: hgtft-neurips-2025
created: 2026-05-21
captured_by: michael-bruck
author: anonymous-neurips-2025-submission
audience: ai-office
departments: [ai-office, engineering]
status: active
confidence: high
related: [hgtft, coordination-leverage-model, organisational-digital-twin, digital-twin]
---

# Heterogeneous Graph Temporal Fusion Transformer (HGTFT) — NeurIPS 2025

Markdown twin of `hgtft-neurips-2025.pdf` (41 pages, NeurIPS 2025 submission, anonymous review). The PDF is the primary source of truth for equations, figures, tables, and appendices; this twin captures the abstract, claims, architecture, and results in indexable form. The acronym **HGTFT** aligns with Janus Digital's customer-facing platform name as used in the [[coordination-leverage-model|Coordination Leverage Model]] (Michael, April 2026) — the paper is presumed to be Janus / Janus-affiliated research backing the product, anonymized per NeurIPS double-blind review.

## Abstract (verbatim from the paper)

> Existing Transformer-based methods effectively capture multivariate time series dependencies, while pre-trained large models excel in generalizing across forecasting tasks, albeit typically in single-physics fields. Spatial-temporal approaches integrate graph structures to enhance forecasting, but often fall short in modeling the complexity of heterogeneous fields with diverse inter-variable interactions. These models also lack a comprehensive understanding of the underlying physical mechanisms in multiphysics fields, leading to dimensional inconsistencies.
>
> To address these challenges, we propose a pre-training and fine-tuning paradigm tailored for spatially and temporally structured physical environments. By tokenizing observation points and generating embeddings that capture temporal patterns and spatial correlations, our model, the **heterogeneous graph temporal fusion transformer (HGTFT)**, effectively integrates multivariable dependencies and relational semantics. We also design a task pipeline with specialized loss functions and training strategies. Applied to temperature, flow, and energy-related field data in building environments, our method demonstrates strong zero-shot generalization and achieves substantial accuracy improvements through few-shot fine-tuning with domain-specific data.

## Three contributions

1. **Problem definition** — *Heterogeneous Graph Forecasting in Multiphysics Systems*, applicable to a broader range of real-world physical systems (nuclear reactors, aerospace vehicles, biomedical devices, combined heat and power systems, smart buildings).
2. **HGTFT framework + multi-stage training pipeline** — designed to capture physical dynamics and improve generalization across diverse forecasting tasks. Encoder learns generalizable physical patterns; decoder adapts flexibly to diverse downstream tasks.
3. **Performance** — strong performance on a self-constructed **MBS (Multiphysics Building System)** dataset and other public benchmarks.

## Architecture (§4, Figure 1)

Three stacked layers, processed per-node and per-timestep:

- **Fusion Layer** — converts heterogeneous data into unified-dimensional vectors. Static Variable Selection + Dynamic Variable Selection → BILSTM → Mean Pooling. Colored bars in Figure 1 indicate different object types.
- **Temporal Layer** — Self-Transformer Layer + Transformer Layer, processed per-object, shared across all objects.
- **Graph Layer** — Graph Attention Network across K relation types, Cross-temporal Aggregation for all connected node types, replicated across all time steps. Outputs node embeddings.

Subtask Model Layer takes node embeddings and produces forecasting dynamic data for all nodes.

## Problem formulation

Heterogeneous graph forecasting in multiphysics systems involves multiple node types and relationships. Each node `v_i` has static attributes `s_i` and time-variant features split into: (1) variables known for both past and future `x_i`, (2) variables known only for the past `z_i`, (3) the prediction variable `y_i`.

```
ŷ_{i, t+1:t+T_future} = F(s_i, x_{i, t-T_past+1:t+T_future}, z_{i, t-T_past+1:t}, y_{i, t-T_past+1:t}, N(v_i))
N(v_i) = ⋃_{r_l ∈ R} N_l(v_i)
```

`N(v_i)` aggregates neighborhood information for node `v_i` across relation types `r_l`.

## Training paradigm (§5)

Multi-task self-supervised learning (MTSL) pipeline with shared encoder + task-specific decoders (hard parameter sharing). Three pre-training stages with progressive specialization (detail in Appendix F.7).

**Loss function** combines four terms:

```
L_task,i = a1·L_MSE + a2·L_RCS + a3·L_CRS + a4·L_FDS
```

- **MSE** — standard mean squared error.
- **RCS (Reasonableness Checks Score)** — discourages predictions that contradict domain-specific operational constraints or physical laws (Appendix F.4).
- **CRS (Correlation-Based Score)** — promotes consistency with correlation patterns in real-world multivariate time-series data (Appendix F.5).
- **FDS (Frequency Domain Similarity)** — aligns spectral characteristics of predictions with ground truth using Fourier-based analysis (Appendix F.6).

**Subtask fine-tuning** — two stages:

- Task fine-tuning — shared encoder frozen; only task-specific parameters updated.
- Project-specific fine-tuning — only lightweight components (e.g., dense projection layer) updated; aligns with new data distributions while retaining general representations.

## Experimental results (§6)

Evaluated on three dataset families:

- **Standard time-series benchmarks** — ETT (4 subsets), Weather, Electricity, Traffic, Exchange, ILI.
- **Graph-structured spatiotemporal** — PeMSD4, PeMSD8, COVID-19 (JHU: 83 Michigan counties; NYT: 50 US states).
- **MBS (Multiphysics Building System) dataset** — self-constructed; time-series from diverse building operation scenarios; 7-day look-back (672 steps) → 1-day forecast (96 steps) at 15-minute intervals.

**Baselines:** LSTM, Autoformer, TFT, HTGNN, STD-MAE, TimesFM, MOIRAI, LLMTime, Time-LLM.

### Table 1 — standard benchmarks (best in bold, second-best underlined; trained or fine-tuned on 10% of each dataset)

HGTFT wins or ties best on most metrics. Selected wins:

- Weather MAE: HGTFT 0.334 (second-best after Time-LLM 0.264).
- Electricity MSE: HGTFT 0.219 (second-best after Time-LLM 0.163).
- COVID-19 (JHU) MAE: HGTFT 41.54 (best).
- COVID-19 (JHU) RMSE: HGTFT 94.38 (best).
- COVID-19 (NYT) MAE: HGTFT 25.69 (best).
- COVID-19 (NYT) RMSE: HGTFT 65.64 (best).

### Table 2 — MBS dataset (10-run average, 50 randomly selected building cases)

HGTFT zero-shot and few-shot both outperform every baseline on every metric. Sample (best in bold):

- MSE: HGTFT few-shot 0.0023 (best); HGTFT zero-shot 0.0027 (second).
- RCS: HGTFT zero-shot 0.0012 (best); HGTFT few-shot 0.0029 (second).
- (CRS and FDS partial in source extraction; check PDF for complete numbers.)

### Table 3 — Ablation study

Removing or simplifying components confirms each contributes to performance. Notable degradations:

- `Fusion: dense` (VSN → dense): MSE 0.0027 → 0.0053 (≈2× worse).
- `Graph: removed`: MSE 0.0027 → 0.0065 (≈2.4× worse).
- `Temporal: removed`: MSE 0.0027 → 0.0072 (≈2.7× worse).

## Application to building digital twins

The paper's experimental focus is *temperature, flow, and energy-related field data in building environments* — directly aligned with the use case Janus's customer-facing HGTFT product addresses ([[coordination-leverage-model]] §4.1 describes the product as *"a structured, continuously updated digital twin of a building: its geometry, its mechanical systems, their relationships, their physics"*). The Reasonableness Checks Score (RCS) loss term operationalises the physics-consistency requirement that the product needs (predictions can't violate physical laws of HVAC operation, energy conservation, etc.).

## Provenance + status notes

- **PDF metadata.** Author / Title / Subject / Keywords are blank (anonymous NeurIPS submission). Created via pdfTeX 1.40.26 / TeX Live 2024 on 2025-05-16.
- **Submission status.** NeurIPS 2025 (under review or proceedings — to verify when blind-review window closes).
- **Janus attribution.** The product name HGTFT in the Coordination Leverage Model precedes this paper in the wiki. Reasonable inference: Janus or Janus-affiliated researchers authored this paper; the product builds on the same architecture. Direct attribution is *unconfirmed* per the v0.12 attribution rule — the paper itself is anonymized and no other source has confirmed authorship.
- **Filed via:** PDF kept at `sources/articles/hgtft-neurips-2025.pdf`; this markdown twin lives alongside per CLAUDE.md §5.1 PDF-handling pattern.

## Related

- [[hgtft]] — Janus product project hub (resolves the [[ingest-2026-05-21-1015-create-hgtft-entity-page]] escalation).
- [[coordination-leverage-model]] — uses HGTFT as the architectural precedent for the [[organisational-digital-twin]].
- [[organisational-digital-twin]] — the AIO-side application of the same engineering pattern.
- [[digital-twin]] — parent concept.
