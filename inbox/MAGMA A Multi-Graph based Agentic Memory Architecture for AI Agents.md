---
title: "MAGMA: A Multi-Graph based Agentic Memory Architecture for AI Agents"
source: "https://arxiv.org/html/2601.03236v2"
author:
published:
created: 2026-05-13
description:
tags:
  - "clippings"
---
Dongming Jiang <sup>α</sup>, Yi Li <sup>α</sup>, Guanpeng Li <sup>β</sup>, Bingzhe Li <sup>α</sup>  
<sup>α</sup> Department of Computer Science, The University of Texas at Dallas  
<sup>β</sup> Department of Electrical and Computer Engineering, University of Florida  
{dongming.jiang, yi.li3, bingzhe.li}@utdallas.edu  
liguanpeng@ufl.edu Corresponding author

###### Abstract

Memory-Augmented Generation (MAG) extends Large Language Models with external memory to support long-context reasoning, but existing approaches largely rely on semantic similarity over monolithic memory stores, entangling temporal, causal, and entity information. This design limits interpretability and alignment between query intent and retrieved evidence, leading to suboptimal reasoning accuracy. In this paper, we propose MAGMA, a multi-graph agentic memory architecture that represents each memory item across orthogonal semantic, temporal, causal, and entity graphs. MAGMA formulates retrieval as policy-guided traversal over these relational views, enabling query-adaptive selection and structured context construction. By decoupling memory representation from retrieval logic, MAGMA provides transparent reasoning paths and fine-grained control over retrieval. Experiments on LoCoMo and LongMemEval demonstrate that MAGMA consistently outperforms state-of-the-art agentic memory systems in long-horizon reasoning tasks. The open-source code is available at: [https://github.com/FredJiang0324/MAGMA](https://github.com/FredJiang0324/MAGMA).

MAGMA: A Multi-Graph based Agentic Memory Architecture for AI Agents

Dongming Jiang <sup>α</sup>, Yi Li <sup>α</sup>, Guanpeng Li <sup>β</sup>, Bingzhe Li <sup>α</sup> <sup>†</sup> <sup>α</sup> Department of Computer Science, The University of Texas at Dallas <sup>β</sup> Department of Electrical and Computer Engineering, University of Florida {dongming.jiang, yi.li3, bingzhe.li}@utdallas.edu liguanpeng@ufl.edu

## 1 Introduction

Large Language Models (LLMs) have demonstrated remarkable capabilities across a wide range of tasks [^4] [^1] [^42], yet they remain limited in their ability to maintain and reason over long-term context. These models process information within a finite attention window, and their internal representations do not persist across interactions, causing earlier details to be forgotten once they fall outside the active context [^4] [^2]. Even within a single long sequence, attention effectiveness degrades with distance due to attention dilution, positional encoding limitations, and token interference, leading to the well-known “lost-in-the-middle” and context-decay phenomena [^28] [^35]. Moreover, LLMs lack native mechanisms for stable and structured memory, resulting in inconsistent recall, degraded long-horizon reasoning, and limited support for tasks requiring persistent and organized memory [^20] [^29].

To address these inherent limitations, Memory-Augmented Generation (MAG) systems have emerged as a promising direction for enabling LLMs to operate beyond the boundaries of their fixed context windows. MAG equips an agent with an external memory continuously recording interaction histories and allowing the agents to retrieve and reintegrate past experiences when generating new responses. By offloading long-term context to an explicit memory module, MAG systems provide a means for agents to accumulate knowledge over time, support multi-session coherence, and adapt to evolving conversational or task contexts. In this paradigm, memory is no longer implicit in internal activations but becomes a persistent, queryable resource that substantially enhances long-horizon reasoning, personalized behavior, and stable agent identity.

Despite their promise, current MAG systems exhibit structural and operational limitations that constrain their effectiveness in long-term reasoning [^25] [^5] [^46] [^31] [^38] [^40] [^17]. Most existing approaches store past interactions in monolithic repositories or minimally structured memory buffers, relying primarily on semantic similarity, recency, or heuristic scoring to retrieve relevant content. For example, A-Mem [^46] organizes past interactions into Zettelkasten-like memory units that are incrementally linked and refined, yet their retrieval pipelines rely primarily on semantic embedding similarity, missing the relations such as temporal or causal relationships. Cognitive-inspired frameworks like Nemori [^30] introduce principled episodic segmentation and representation alignment, enabling agents to detect event boundaries and construct higher-level semantic summaries. However, their memory structures are still narrative and undifferentiated, with no explicit modeling of distinct relational dimensions.

To address the structural limitations of existing MAG systems, we propose MAGMA, a multi-graph agentic memory architecture that explicitly models heterogeneous relational structure in an agent’s experience. MAGMA represents each memory item across four orthogonal relational graphs (i.e., semantic, temporal, causal, and entity), yielding a disentangled representation of how events, concepts, and participants are related.

Built on this unified multi-graph substrate, MAGMA introduces a hierarchical, intent-aware query mechanism that selects relevant relational views, traverses them independently, and fuses the resulting subgraphs into a compact, type-aligned context for generation. By decoupling memory representation from retrieval logic, MAGMA enables transparent reasoning paths, fine-grained control over memory selection, and improved alignment between query intent and retrieved evidence. This relational formulation provides a principled and extensible foundation for agentic memory, improving both long-term coherence and interpretability.

Our contributions are summarized as follows:

1. We propose MAGMA, a multi-graph agentic memory architecture that explicitly models semantic, temporal, causal, and entity relations essential for long-horizon reasoning.
2. We introduce an Adaptive Traversal Policy that routes retrieval based on query intent, enabling efficient pruning of irrelevant graph regions and achieving lower latency and reduced token usage.
3. We design a dual-stream memory evolution mechanism that decouples latency-sensitive event ingestion from asynchronous structural consolidation, preserving responsiveness while refining relational structure.
4. We demonstrate that MAGMA consistently outperforms state-of-the-art agentic memory systems on long-context benchmarks including LoCoMo and LongMemEval, while reducing retrieval latency and token consumption relative to prior systems. The code is open-sourced <sup>1</sup>.

![Refer to caption](https://arxiv.org/html/2601.03236v2/x1.png)

Figure 1: High-Level Architecture of Memory-Augmented Generation (MAG).

![Refer to caption](https://arxiv.org/html/2601.03236v2/x2.png)

Figure 2: Architectural Overview of MAGMA. The system is composed of three layers: (1) A Query Process that routes and synthesizes context; (2) A Data Structure Layer organizing memory into Relation Graphs and a Vector Database; and (3) A Write/Update Process utilizing a dual-stream mechanism for fast ingestion and asynchronous consolidation.

## 2 Background

Existing Large Language Models (LLMs) face fundamental challenges in handling long-term agentic interactions. These challenges stem from the inherent limitations of fixed-length contexts, which result in fragmented memory and an inability to maintain narrative coherence over time. The evolution of long-term consistency in LLMs is shifted from Context-Window Extension [^2] [^35] [^19] [^37], Retrieval-Augmented Generation (RAG) [^23] [^13] [^41] [^14] [^9] [^26] to Memory-Augmented Generation (MAG).

Retrieval-oriented approaches enrich the model with an external, dynamic memory library, giving rise to the paradigm of Memory-Augmented Generation (MAG) [^50] [^34] [^11]. Formally, unlike static RAG, MAG maintains a time-variant memory $\mathcal{M}_{t}$ that evolves via a feedback loop:

$$
o_{t}=\text{LLM}(q_{t},\text{Retrieve}(q_{t},\mathcal{M}_{t}))
$$
 
$$
\mathcal{M}_{t+1}=\text{Update}(\mathcal{M}_{t},q_{t},o_{t})
$$

As shown in Figure 1, this feedback loop enables the memory module to evolve over time: the user query is combined with retrieved information to form an augmented prompt, and the model’s output is subsequently written back to refine $\mathcal{M}_{t}$.

Some prior schemes focused on structuring the intermediate states or relationships of memory to enable better reasoning. Think-in-Memory (TiM) [^27] stores evolving chains-of-thought to maintain consistency. A-MEM [^46] draws inspiration from the Zettelkasten method, organizing knowledge into an interconnected note network. More recently, graph-based approaches like GraphRAG [^7] and Zep [^38] structure memory into knowledge graphs to capture cross-document dependencies. We provide a detailed discussion of related work in Appendix A.

However, prior work typically organizes memory around associative proximity (e.g., semantic similarity) rather than mechanistic dependency [^21]. As a result, such methods can retrieve what occurred but struggle to reason about why, since they lack explicit representations of causal structure, leading to reduced accuracy in complex reasoning tasks [^15] [^48].

## 3 MAGMA Design

In this section, we introduce the proposed Multi-Graph based Agentic Memory (MAGMA) design and its components in detail.

### 3.1 Architectural Overview

MAGMA architecture is organized into the following three logical layers, orchestrating the interaction between control logic and the memory substrate as illustrated in Figure 2.

Query Process: The inference engine responsible for retrieving and synthesizing information. It comprises the Intent-Aware Router for dispatching tasks, the Adaptive Topological Retrieval module for executing graph traversals, and the Context Synthesizer for generating the final narrative response.

Data Structure ($\mathcal{G}$): The unified storage substrate that fuses disparate modalities. As shown in the center of Figure 2, it maintains a Vector Database for semantic search alongside four distinct Relation Graphs (i.e., Semantic, Temporal, Causal and Entity). This layer provides the topological foundation for cross-view reasoning.

Write/Update Process: A dual-stream pipeline manages memory evolution. It decouples latency-sensitive operations via Synaptic Ingestion (Fast Path) from compute-intensive reasoning via Asynchronous Consolidation (Slow Path), ensuring the system remains responsive while continuously deepening its memory structure.

Functionally, the Query Layer interacts with the Data Structure Layer to execute the synchronous Query Process (Section 3.3), while the Write/Update Layer manages the continuous Memory Evolution (Section 3.4).

### 3.2 Data Structure Layer

As the core component of Memory-Augmented Generation (MAG), the data structure layer is responsible for storing, organizing, and evolving past information to support future retrieval and updates. In MAGMA, we formalize this layer as a time-variant directed multigraph $\mathcal{G}_{t}=(\mathcal{N}_{t},\mathcal{E}_{t})$, where nodes represent events and edges encode heterogeneous relational structures. This unified manifold enables structured reasoning across multiple logical dimensions(i.e., semantic, temporal, causal, and entity) while preserving their orthogonality.

Unified node representation: The node set $\mathcal{N}$ is hierarchically organized to represent experience at multiple granularities, ranging from fine-grained atomic events to higher-level episodic groupings. Each Event-Node $n_{i}\in\mathcal{N}_{\text{event}}$ is defined as:

$$
n_{i}=\langle c_{i},\tau_{i},\mathbf{v}_{i},\mathcal{A}_{i}\rangle
$$

where $c_{i}$ denotes the event content (e.g., observations, actions, or state changes), $\tau_{i}$ is a discrete timestamp anchoring the event in time, and $\mathbf{v}_{i}\in\mathbb{R}^{d}$ is a dense representation indexed in the vector database [^16]. The attribute set $\mathcal{A}_{i}$ captures structured metadata such as entity references, temporal cues, or contextual descriptors, enabling hybrid retrieval that integrates semantic similarity with symbolic and structural constraints.

Relation graphs (edge space): The edge set $\mathcal{E}$ is partitioned into four semantic subspaces, corresponding to the relation graphs:

- Temporal Graph ($\mathcal{E}_{temp}$): Defined as strictly ordered pairs $(n_{i},n_{j})$ where $\tau_{i}<\tau_{j}$. This immutable chain provides the ground truth for chronological reasoning.
- Causal Graph ($\mathcal{E}_{causal}$): Directed edges representing logical entailment. An edge $e_{ij}\in\mathcal{E}_{causal}$ exists if $S(n_{j}|n_{i},q)>\delta$, explicitly inferred by the consolidation module to support "Why" queries.
- Semantic Graph ($\mathcal{E}_{sem}$): Undirected edges connecting conceptually similar events, formally defined by $\cos(\mathbf{v}_{i},\mathbf{v}_{j})>\theta_{sim}$.
- Entity Graph ($\mathcal{E}_{ent}$): Edges connecting events to abstract entity nodes, solving the object permanence problem across disjoint timeline segments.

![Refer to caption](https://arxiv.org/html/2601.03236v2/x3.png)

Figure 3: Query process with adaptive hybrid retrieval pipeline. (1) Query Analysis detects intent and fuses signals to find Anchors. (2) Adaptive Traversal navigates specific graph views (Causal, Temporal) based on the policy weights.

### 3.3 Query Process: Adaptive Hierarchical Retrieval

As illustrated in Figure 3, retrieval in MAGMA is formulated as a policy-guided graph traversal rather than a static lookup operation. The query process is orchestrated by a Router $\mathcal{R}$, which decomposes the user query into structured control signals and executes a multi-stage retrieval pipeline (Algorithm 1) that dynamically selects, traverses, and fuses relevant relational views. Four main stages in the query process is introduced below:

Stage 1 - Query Analysis & Decomposition: The process begins by decomposing the raw user query $q$ into structured control signals, including semantic, lexical, and temporal cues. MAGMA then extracts three complementary representations to guide the retrieval process:

- Intent Classification ($T_{q}$): A lightweight classifier maps $q$ to a specific intent type $T_{q}\in\{\textsc{Why},\textsc{When},\textsc{Entity}\}$. This acts as the "steering wheel," determining which graph edges will later be prioritized (e.g., "Why" queries trigger a bias for Causal edges).
- Temporal Parsing ($[\tau_{s},\tau_{e}]$): A temporal tagger resolves relative expressions (e.g., "last Friday") into absolute timestamps, defining a hard time window for filtering.
- Representation Extraction: The system simultaneously generates a dense embedding $\vec{q}$ for semantic search and extracts sparse keywords $q_{key}$ for exact lexical matching.

Stage 2 - Multi-Signal Anchor Identification: Before initiating graph traversal, the system first identifies a set of anchor nodes that serve as entry points into the memory graph. To ensure robustness across query modalities, we fuse signals from dense semantic retrieval, lexical keyword matching, and temporal filtering using Reciprocal Rank Fusion (RRF) [^6]:

$$
S_{anchor}=\text{Top}_{K}\left(\sum_{m\in\{vec,key,time\}}\frac{1}{k+r_{m}(n)}\right)
$$

This ensures robust starting points regardless of query modality.

Stage 3 - Adaptive Traversal Policy: Starting from the anchor set $\mathcal{S}_{anchor}$, the system expands the context using a Heuristic Beam Search. Unlike rigid rule-based traversals, MAGMA calculates a dynamic transition score $S(n_{j}|n_{i},q)$ for moving from node $n_{i}$ to neighbor $n_{j}$ via edge $e_{ij}$. This score fuses structural alignment with semantic relevance:

$$
\begin{split}S(n_{j}|n_{i},q)=\exp\bigg(&\lambda_{1}\cdot\underbrace{\phi(type(e_{ij}),T_{q})}_{\begin{subarray}{c}\text{Structural}\\
\text{Alignment}\end{subarray}}\\
&+\lambda_{2}\cdot\underbrace{\text{sim}(\vec{n}_{j},\vec{q})}_{\begin{subarray}{c}\text{Semantic}\\
\text{Affinity}\end{subarray}}\bigg)\end{split}
$$

Here, $\text{sim}(\cdot)$ denotes the cosine similarity between the neighbor’s embedding and the query embedding. The structural alignment function $\phi$ dynamically rewards edge types based on the detected query intent $T_{q}$:

$$
\phi(r,T_{q})=\mathbf{w}_{T_{q}}^{\top}\cdot\mathbf{1}_{r}
$$

where $\mathbf{w}_{T_{q}}$ is an adaptive weight vector specific to intent $T_{q}$ (e.g., assigning high weights to CAUSAL edges for "Why" queries), and $\mathbf{1}_{r}$ is the one-hot encoding of the edge relation.

At each step, the algorithm retains the top- $k$ nodes with the highest cumulative scores. This ensures the traversal is guided by a dual signal: strictly following the logical structure (via $\phi$) while maintaining contextual focus (via sim).

Algorithm 1 Adaptive Hybrid Retrieval (Heuristic Beam Search)

Query $q$, Graph $G$, VectorDB $V$, Intent $T_{q}$

Narrative Context $C_{out}$

// Phase 1: Initialization

$S_{anchor}\leftarrow\textsc{RRF}(V.\textsc{Search}(\vec{q}),K.\textsc{Search}(q_{key}))$ // Hybrid Retrieval

 $CurrentFrontier,Visited\leftarrow S_{anchor}$ $\mathbf{w}_{T_{q}}\leftarrow\textsc{GetAttentionWeights}(T_{q})$

for $d\leftarrow 1$ to $MaxDepth$ do

   $Candidates\leftarrow\textsc{PriorityQueue}()$

  for $u\in CurrentFrontier$ do

   for $v\in G.\textsc{Neighbors}(u)$ do

     if $v\notin Visited$ then

      // Calculate transition score via Eq. 5

       $s_{uv}\leftarrow\exp(\lambda_{1}(\mathbf{w}_{T_{q}}^{\top}\cdot\mathbf{1}_{e_{uv}})+\lambda_{2}\text{sim}(\vec{v},\vec{q}))$

       $score_{v}\leftarrow\text{score}_{u}\cdot\gamma+s_{uv}$ // Apply Decay $\gamma$

       $Candidates.\textsc{Push}(v,score_{v})$

     end if

   end for

  end for

   $CurrentFrontier\leftarrow Candidates.\textsc{TopK}(BeamWidth)$    $Visited.\textsc{AddAll}(CurrentFrontier)$

  if $Visited.\textsc{Size}()\geq Budget$ then break

  end if

end for

 $C_{sorted}\leftarrow\textsc{TopologicalSort}(Visited,T_{q})$

return $\textsc{Serialize}(C_{sorted})$

Stage 4: Narrative Synthesis via Graph Linearization: The final phase transforms the retrieved subgraph $\mathcal{G}_{sub}$ into a coherent narrative context. MAGMA employs a structure-aware linearization protocol that preserves the relational dependencies encoded in the graph with the following three phases.

1\. Topological Ordering: Raw nodes are reorganized to reflect the logic of the query. For temporal queries ($T_{q}=\textsc{When}$), nodes are sorted by timestamp $\tau_{i}$. For causal queries ($T_{q}=\textsc{Why}$), we apply a topological sort on the causal edges $\mathcal{E}_{causal}$ to ensure causes precede effects in the prompt context.

2\. Context Scaffolding with Provenance: To mitigate hallucination, each node is serialized into a structured block containing its timestamp, content, and explicit reference ID. We define the linearized context $C_{prompt}$ as:

$$
C_{prompt}=\bigoplus_{n_{i}\in\text{Sort}(\mathcal{G}_{sub})}\left[\texttt{<t:}\tau_{i}\texttt{> }n_{i}.content\texttt{ <ref:}n_{i}.id\texttt{>}\right]
$$

where $\bigoplus$ denotes string concatenation.

3\. Salience-Based Token Budgeting: Given a fixed LLM context window, we cannot include all retrieved nodes. We utilize the relevance scores $S(n_{j}|n_{i},q)$ computed in Eq. (5) to enforce a dynamic budget. Low-probability nodes are summarized into brevity codes (e.g., "…3 intermediate events…"), while high-salience nodes retain full semantic detail.

This structured scaffold forces the LLM to act as an interpreter of evidence rather than a creative writer, significantly reducing grounding errors.

### 3.4 Memory Evolution (Write and Update)

Long-term reasoning requires not only effective retrieval, but also a memory substrate that can adapt and reorganize as experience accumulates. MAGMA addresses this requirement through a structured memory evolution scheme that incrementally refines its multi-relational graph over time. Specifically, the transition from $\mathcal{G}_{t}$ to $\mathcal{G}_{t+1}$ is governed by a dual-stream process that decouples latency-sensitive ingestion from compute-intensive consolidation [^22], balancing short-term responsiveness with long-term reasoning fidelity.

Fast path ( synaptic ingestion): The Fast Path operates on the critical path of interaction, constrained by strict latency requirements. It performs non-blocking operations: event segmentation, vector indexing, and updating the immutable temporal backbone ($n_{t-1}\rightarrow n_{t}$). As detailed in Algorithm 2, no blocking LLM reasoning occurs here, ensuring the agent remains responsive regardless of memory size.

Algorithm 2 Fast Path: Synaptic Ingestion

User Interaction $I$, Current Graph $\mathcal{G}_{t}$

Updated Graph $\mathcal{G}_{t+1}$

 $n_{t}\leftarrow\textsc{SegmentEvent}(I)$ $n_{prev}\leftarrow\textsc{GetLastNode}(\mathcal{G}_{t})$

// Update Temporal Backbone

 $\mathcal{G}.\textsc{AddEdge}(n_{prev},n_{t},\text{type}=\textsc{Temp})$

// Indexing

 $\mathbf{v}_{t}\leftarrow\textsc{Encoder}(n_{t}.c)$ $VDB.\textsc{Add}(\mathbf{v}_{t},n_{t}.id)$

$Queue.\textsc{Enqueue}(n_{t}.id)$ // Trigger Slow Path

return $n_{t}$

Slow path (structural consolidation): Asynchronously, the slow path performs Memory Consolidation (Algorithm 3). It functions as a background worker that dequeues events and densifies the graph structure. By analyzing the local neighborhood $\mathcal{N}(n_{t})$ of recent events, the system employs an LLM $\Phi$ to infer latent connections:

$$
\mathcal{E}_{new}=\Phi_{reason}(\mathcal{N}(n_{t}),\mathcal{H}_{history})
$$

This process constructs high-value $\mathcal{E}_{causal}$ and $\mathcal{E}_{ent}$ links, effectively trading off compute time for relational depth.

Algorithm 3 Slow Path: Structural Consolidation

Worker Process:

loop

   $id\leftarrow Queue.\textsc{Dequeue}()$

  if $id$ is null then continue

  end if

   $n_{t}\leftarrow\mathcal{G}.\textsc{GetNode}(id)$    $\mathcal{N}_{local}\leftarrow\mathcal{G}.\textsc{GetNeighborhood}(n_{t},\text{hops}=2)$

  // Infer latent Causal and Entity structures

   $Prompt\leftarrow\textsc{Format}(\mathcal{N}_{local})$    $\mathcal{E}_{new}\leftarrow\Phi_{LLM}(Prompt)$    $\mathcal{G}.\textsc{AddEdges}(\mathcal{E}_{new})$

end loop

### 3.5 Implementation

We implement MAGMA as a modular three-layer architecture designed for extensibility, scalability, and deployment flexibility. The storage layer abstracts over heterogeneous physical backends, providing unified interfaces for managing the typed memory graph, dense vector indices, and sparse keyword indices. This abstraction cleanly separates the logical memory model from its physical realization, enabling seamless substitution of storage backends (e.g., in-memory data structures versus production-grade graph or vector databases) with minimal engineering effort.

The retrieval layer coordinates the core algorithmic components, including memory construction, multi-stage ranking, and policy-guided graph traversal. It is supported by specialized utility modules for episodic segmentation and temporal normalization, which provide structured signals to downstream retrieval and traversal policies. The application layer manages the interaction loop, evaluation harnesses, and prompt construction, serving as the interface between the agent and the underlying memory system.

Table 1: Performance on the LoCoMo benchmark evaluated using the LLM-as-a-Judge metric. Higher scores indicate better performance. LLM model is based on gpt-4o-mini.

| Method | Multi-Hop | Temporal | Open-Domain | Single-Hop | Adversarial | Overall |
| --- | --- | --- | --- | --- | --- | --- |
| Full Context | 0.468 | 0.562 | 0.486 | 0.630 | 0.205 | 0.481 |
| A-MEM | 0.495 | 0.474 | 0.385 | 0.653 | 0.616 | 0.580 |
| MemoryOS | 0.552 | 0.422 | 0.504 | 0.674 | 0.428 | 0.553 |
| Nemori | 0.569 | 0.649 | 0.485 | 0.764 | 0.325 | 0.590 |
| MAGMA (ours) | 0.528 | 0.650 | 0.517 | 0.776 | 0.742 | 0.700 |

## 4 Experiments

We conduct comprehensive experiments to evaluate both the reasoning effectiveness and systems properties of the proposed MAGMA architecture over state-of-the-art baselines.

### 4.1 Experimental Setup

Datasets. We evaluate long-term conversational capability using two widely adopted benchmarks: (1) LoCoMo [^29]: which contains ultra-long conversations (average length of 9K tokens) designed to assess long-range temporal and causal retrieval. (2) LongMemEval [^43]: a large-scale stress-test benchmark with an average context length exceeding 100K tokens, used to evaluate scalability and memory retention stability over extended interaction horizons..

Baselines. We compare MAGMA against four state-of-the-art memory architectures. For fair comparison, all methods employ the same backbone LLMs.

- Full Context: Feeds the entire conversation history into the LLM.
- A-MEM [^46]: A biological-inspired, self-evolving memory system that dynamically organizes agent experiences.
- Nemori [^30]: A graph-based memory utilizing a "predict-calibrate" mechanism for episodic segmentation.
- MemoryOS [^17]: A semantic-focused memory operating system employing a hierarchical storage strategy.

Metrics. Following standard evaluation protocols, we primarily use the LLM-as-a-Judge score [^49] to assess the accuracy of different methods. The detailed evaluation prompt used for the judge model is provided in the appendix. For completeness, we also report token-level F1 and BLEU-1 [^33].

### 4.2 Overall Comparison

This section introduces the accuracy performance comparison between all methods on the LoCoMo benchmark based on LLM-as-a-judge. As shown in Table 1, MAGMA achieves the highest overall judge score of 0.7, substantially outperforming the other baselines: Full Context (0.481), A-MEM (0.58), MemoryOS (0.553) and Nemori (0.59) by relative margins of 18.6% to 45.5%. This result demonstrates that explicitly modeling multi-relational structure enables more accurate long-horizon reasoning than flat or purely semantic memory architectures.

A closer analysis reveals that MAGMA’s advantage is particularly pronounced in reasoning-intensive settings. In the Temporal category, MAGMA slightly but consistently outperforms others (Judge: 0.650 for MAGMA vs. 0.422 - 0.649 for others), validating the effectiveness of our Temporal Inference Engine in resolving relative temporal expressions into grounded chronological representations. The performance gap further widens under adversarial conditions, where MAGMA attains a judge score of 0.742. This robustness stems from the Adaptive Traversal Policy, which prioritizes causal and entity-consistent paths and avoids semantically similar yet structurally irrelevant distractors that often mislead vector-based retrieval systems. Additional results and analyzes, including case studies and evaluations under alternative metrics, are provided in the appendix.

Table 2: Performance comparison on LongMemEval dataset across different question types. We compare our MAGMA method against the Full-context baseline and the Nemori system.

<table><thead><tr><th></th><th>Question Type</th><th>Full-context</th><th>Nemori</th><th>MAGMA</th></tr><tr><th></th><th></th><th>(101K tokens)</th><th>(3.7–4.8K tokens)</th><th>(0.7–4.2K tokens)</th></tr></thead><tbody><tr><th rowspan="7">gpt-4o-mini</th><th>single-session-preference</th><td>6.7%</td><td>62.7%</td><td>73.3%</td></tr><tr><th>single-session-assistant</th><td>89.3%</td><td>73.2%</td><td>83.9%</td></tr><tr><th>temporal-reasoning</th><td>42.1%</td><td>43.0%</td><td>45.1%</td></tr><tr><th>multi-session</th><td>38.3%</td><td>51.4%</td><td>50.4%</td></tr><tr><th>knowledge-update</th><td>78.2%</td><td>52.6%</td><td>66.7%</td></tr><tr><th>single-session-user</th><td>78.6%</td><td>77.7%</td><td>72.9%</td></tr><tr><th>Average</th><td>55.0%</td><td>56.2%</td><td>61.2%</td></tr></tbody></table>

### 4.3 Generalization Study

To evaluate generalization under extreme context lengths, we compare MAGMA against prior methods on the LongMemEval benchmark. LongMemEval poses a substantial scalability challenge, with an average context length exceeding 100k tokens, and therefore serves as a rigorous stress test for long-term memory retention and retrieval under strict computational constraints.

As summarized in Table 2, MAGMA achieves the highest average accuracy (61.2%), outperforming both the Full-context baseline (55.0%) and the Nemori system (56.2%). These results indicate that MAGMA generalizes effectively to ultra-long interaction histories while maintaining strong retrieval precision.

At the same time, the results highlight a favorable efficiency–granularity trade-off. Although the Full-context baseline performs strongly on single-session-assistant tasks (89.3%), this performance comes at a prohibitive computational cost, requiring over 100k tokens per query. MAGMA achieves competitive accuracy (83.9%) while using only 0.7k–4.2k tokens per query, representing a reduction of more than 95%. This demonstrates that MAGMA effectively compresses long interaction histories into compact, reasoning-dense subgraphs, preserving essential information while substantially reducing inference-time overhead.

### 4.4 System Efficiency Analysis

To evaluate the system efficiency of MAGMA, two metrics are focused: (1) memory build time (the time required to construct the memory graph) and (2) token cost (the average tokens processed per query).

Table 3 reports the comparative results. While A-MEM achieves the lowest token consumption (2.62k) due to its aggressive summarization, it sacrifices reasoning depth (see Table 1). In contrast, MAGMA achieves the lowest query latency (1.47s) about 40% faster than the next best retrieval baseline (A-MEM) while maintaining a competitive token cost (3.37k). This efficiency stems from our Adaptive Traversal Policy, which prunes irrelevant subgraphs early, and the dual-stream architecture that offloads complex indexing to the background.

Table 3: System efficiency comparison with total memory build time (in hours), average token consumption per query (in k tokens), and average query latency (in seconds).

| Method | Build Time (h) | Tokens/Query (k) | Latency (s) |
| --- | --- | --- | --- |
| Full Context | N/A | 8.53 | 1.74 |
| A-MEM | 1.01 | 2.62 | 2.26 |
| MemoryOS | 0.91 | 4.76 | 32.68 |
| Nemori | 0.29 | 3.46 | 2.59 |
| MAGMA | 0.39 | 3.37 | 1.47 |

Table 4: Breakdown analysis on the performance impact of different schemes in MAGMA.

| MAGMA schemes | Judge | F1 | BLEU-1 |
| --- | --- | --- | --- |
| w/o Adaptive Policy | 0.637 | 0.413 | 0.357 |
| w/o Causal Links | 0.644 | 0.439 | 0.354 |
| w/o Temporal Backbone | 0.647 | 0.438 | 0.349 |
| w/o Entity Links | 0.666 | 0.451 | 0.363 |
| MAGMA (Full) | 0.700 | 0.467 | 0.378 |

Table 5: Single-graph ablation study on LoCoMo.

| Graph Configuration | Multi-Hop | Temporal | Open-Domain | Single-Hop | Adversarial | Overall |
| --- | --- | --- | --- | --- | --- | --- |
| Causal Only | 0.470 | 0.460 | 0.430 | 0.650 | 0.680 | 0.590 |
| Temporal Only | 0.440 | 0.620 | 0.450 | 0.650 | 0.520 | 0.577 |
| Entity Only | 0.485 | 0.420 | 0.460 | 0.640 | 0.450 | 0.531 |
| Full MAGMA | 0.528 | 0.650 | 0.517 | 0.776 | 0.742 | 0.700 |

### 4.5 Ablation Study

In this subsection, we conduct a systematic ablation study to assess the contribution of individual components in MAGMA. By selectively disabling edge types and traversal mechanisms, we isolate the sources of its reasoning capability. The results in Table 4 reveal three main findings.

First, removing the Adaptive Policy results in the largest performance drop, with the Judge score decreasing from 0.700 to 0.637. This confirms that intent-aware routing is critical: without it, retrieval degenerates into a static graph walk that introduces structurally irrelevant information and degrades reasoning quality. Second, removing either Causal Links or the Temporal Backbone leads to comparable and substantial performance losses (0.644 and 0.647, respectively), indicating that causal structure and temporal ordering provide complementary, non-substitutable axes of reasoning. Finally, removing Entity Links causes a smaller but consistent decline (0.700 to 0.666), highlighting their role in maintaining entity permanence and reducing hallucinations in entity-centric queries.

To further isolate the contribution of each relation type, we additionally conducted a single-graph-only ablation on LoCoMo, shown in Table 5. The results are consistent with the leave-one-out findings in Table 4. Among single-graph variants, Causal Only achieves the highest overall score (0.590), suggesting that causal relations provide strong logical filtering and robustness against distractor noise. Temporal Only performs best on temporal questions (0.620), confirming that explicit temporal structure is particularly important for sequential reasoning. In contrast, Entity Only obtains the lowest overall score (0.531): while it remains helpful for concept bridging in multi-hop reasoning, it lacks both timeline awareness and logical filtering, which explains why removing entity links causes the smallest drop in the full-system ablation.

Overall, these results show that no single relation type is sufficient to recover MAGMA’s full reasoning capability, as all single-graph variants remain below 0.60 overall. By explicitly decoupling causal, temporal, and entity relations and combining them with adaptive traversal, MAGMA leverages their complementary strengths to achieve the best overall performance.

## 5 Conclusion

We introduced MAGMA, a multi-graph agentic memory architecture that models semantic, temporal, causal, and entity relations within a unified yet disentangled memory substrate. By formulating retrieval as a policy-guided graph traversal and decoupling memory ingestion from asynchronous structural consolidation, MAGMA enables effective long-horizon reasoning while maintaining low inference-time latency. Empirical results on LoCoMo and LongMemEval demonstrate that MAGMA consistently outperforms state-of-the-art memory systems while achieving substantial efficiency gains under ultra-long contexts.

## 6 Limitations

While MAGMA demonstrates strong empirical performance, it has several limitations. First, the quality of the constructed memory graph depends on the reasoning fidelity of the underlying Large Language Models used during asynchronous consolidation. This dependency is a shared limitation of agentic memory systems that rely on LLM-based structural inference, as they are susceptible to extraction errors and hallucinations [^32] [^44] [^39]. Although MAGMA employs structured prompts and conservative inference thresholds to reduce spurious links, erroneous or missing relations may still arise and propagate to downstream retrieval. Nevertheless, our experimental results indicate that, even under these constraints, agentic memory systems such as MAGMA substantially outperform traditional baselines, including full-context approaches, in long-horizon reasoning tasks.

Second, multi-graph substrate may introduce additional storage and engineering complexity compared to flat, vector-only memory systems. Maintaining multiple relational views and dual-stream processing incurs a little higher implementation and memory overhead, which may limit applicability in highly resource-constrained environments.

Finally, most existing agentic memory systems, including MAGMA, are primarily evaluated on long-context conversational and agentic benchmarks such as LoCoMo and LongMemEval. While these benchmarks effectively stress temporal and causal reasoning, they do not cover the full range of settings in which agentic memory may be required [^10] [^12]. Extending MAGMA to other scenarios, such as multimodal agents or environments with heterogeneous observation streams, may require additional adaptation and calibration. Addressing these broader evaluation settings remains an important research direction for future work.

## 7 Acknowledgment

This work was partially supported by NSF 2343863, 2413520, 2417747 and 2440611. Any opinions, conclusions, or recommendations expressed in this material are those of the authors and do not necessarily reflect the views of the NSF.

## References

## Appendix A Related Work

Following the framing in main text, we organize related work along the same progression: from context window extension to retrieval augmented generation (RAG) and finally to memory augmented generation (MAG), and then discuss structured/graph memories and causal reasoning, which are central to long-horizon agentic interactions.  
Context-window Extension. A direct line of work extends the effective context length of Transformers by modifying attention or positional extrapolation. Longformer [^3] introduces sparse attention patterns to scale to long documents, reducing quadratic cost while retaining locality and selected global connectivity. ALiBi [^36] (Attention with Linear Biases) enables length extrapolation by injecting distance-aware linear biases into attention scores, improving robustness when testing on longer sequences than those seen in training. Recent efforts also add explicit memory modules or hybrid mechanisms to push beyond pure attention-window scaling. For example, LM2 [^19] proposes a decoder-only architecture augmented with an auxiliary memory to mitigate long-context limitations. MemoRAG [^37] similarly emphasizes global-memory-enhanced retrieval to boost long-context processing when raw context is insufficient or inefficient. While these approaches improve long-range coverage, they do not, by themselves, address the continual, evolving, and write-back nature of agent memory required for multi-session interactions.  
Retrieval Augmented Generation. RAG [^23] augments an LLM with external retrieval over a fixed corpus, classically retrieving supporting passages and conditioning generation on them. Subsequent work explores better integration with long-context models and more scalable retrieval pipelines. LongRAG [^14] studies how to exploit long-context LLMs together with retrieval, improving the ability to incorporate larger retrieved evidence sets. Other systems focus on structuring the retrieved memory space or optimizing the RAG serving stack: M-RAG [^41] uses multiple partitions to encourage fine-grained retrieval focus, while RAGO [^13] provides a systematic framework for performance optimization in RAG serving. Furthermore, to improve the reliability of retrieved context, approaches like Self-Correcting RAG [^45] enhance generation faithfulness via selective context filtering and inference-guided search. However, standard RAG typically assumes a static knowledge base. In contrast, agentic settings require memory that is continuously updated (the feedback loop described in the main text). This motivates the shift to MAG systems, where memory is dynamic and evolves with interaction histories.  
Memory Augmented Generation and Agent Memory Systems. MAG systems maintain and update an external memory over time, enabling agents to accumulate knowledge, preserve identity, and remain coherent across sessions. Early and representative directions include memory construction and write-back strategies for long-term agent behavior, such as MemoryBank [^50] and generative agents style architectures that emphasize persistent profiles and evolving state grounded in past interactions [^30] [^29] [^47]. A growing body of work adopts systems metaphors and designs: MemGPT [^31] frames LLM agents with an operating-system-like memory hierarchy, emphasizing paging and controlled context management. More recent memory OS systems propose explicit storage hierarchies, efficient memory modules, and controllers (e.g., MemoryOS [^18], MemOS [^25], and Hippocampus [^24]) to manage persistence, scalability, and retrieval policies at scale. In addition, practical agent-memory stacks (e.g., Zep [^38]) offer temporal knowledge-graph-based memory services aimed at real-world deployment constraints.  
Structured memory: chains-of-thought and graph-based representations. Beyond flat text buffers or vector stores, several methods explicitly structure memory to support reasoning. Think-in-Memory (TiM) stores evolving chains-of-thought to improve consistency across long-horizon reasoning, while A-MEM [^46] is inspired by Zettelkasten-style linking of notes/experiences. These methods highlight the value of representing intermediate reasoning traces or explicit links, but many retrieval pipelines still predominantly rely on semantic similarity as the primary access mechanism. Graph-based approaches have recently gained traction as a way to capture cross-document and cross-episode dependencies. GraphRAG [^8] builds entity-centric graphs and community summaries to answer more global questions over large corpora. Zep proposes a temporally-aware knowledge-graph engine (Graphiti) that synthesizes conversational and structured business data while preserving historical relations. The main text notes these graph-based lines explicitly and motivates a key gap: many systems organize memory around associative proximity (semantic relatedness) rather than mechanistic dependency.  
Causal reasoning and long-horizon evaluation. Causal reasoning has been highlighted as both important and challenging for LLMs. The work [^21] study LLMs’ ability to generate causal arguments across multiple causal tasks and emphasize robustness/failure modes, reinforcing that what happened retrieval is not sufficient for why reasoning in many settings. Benchmarking efforts such as LoCoMo [^29] stress long-range temporal and causal dynamics in multi-session conversations and provide evaluation tasks that expose long-horizon memory deficits. The paper’s experimental setup also uses LongMemEval [^43] as an ultra-long context stress test, and evaluates via LLM-as-a-Judge protocols standard in modern instruction-following evaluation. Overall, prior work demonstrates steady progress in (i) scaling context length, (ii) improving retrieval pipelines, and (iii) building structured, evolving memories for agents. The main text positions MAGMA within this trajectory by explicitly targeting multi-relational structure (semantic/temporal/causal/entity) and intent-aware retrieval control.

## Appendix B System Implementation Details

### B.1 Hyperparameter Configuration

Table 6 presents the comprehensive configuration used in our experiments. These parameters were empirically optimized on the LoCoMo benchmark. Notably, MAGMA employs an Adaptive Scoring mechanism where weights ($\lambda$) shift dynamically based on the detected query intent.

Table 6: Hyperparameter settings for MAGMA. "Traversal Weights" correspond to the intent-specific vector $\mathbf{w}_{T_{q}}$, while $\lambda_{1}$ and $\lambda_{2}$ control the global balance between structural alignment and semantic affinity (Eq. 5).

<table><tbody><tr><td>Module</td><td>Parameter</td><td>Value/Range</td></tr><tr><td rowspan="3">Embedding</td><td>Model (Default)</td><td>all-MiniLM-L6-v2</td></tr><tr><td>Model (Optional)</td><td>text-embedding-3-small</td></tr><tr><td>Dimension</td><td>384 / 1536</td></tr><tr><td rowspan="2">Inference</td><td>LLM Backbone</td><td>gpt-4o-mini</td></tr><tr><td>Temperature</td><td>0.0</td></tr><tr><td rowspan="4">Retrieval (Phase 1)</td><td>RRF Constant (<math><semantics><mi>k</mi> <annotation>k</annotation></semantics></math>)</td><td>60</td></tr><tr><td>Vector Top-K</td><td>20</td></tr><tr><td><math><semantics><msub><mi>w</mi> <mrow><mi>k</mi> <mo></mo><mi>e</mi> <mo></mo><mi>y</mi> <mo></mo><mi>w</mi> <mo></mo><mi>o</mi> <mo></mo><mi>r</mi> <mo></mo><mi>d</mi></mrow></msub> <annotation>w_{keyword}</annotation></semantics></math> (Fusion)</td><td>2.0 – 5.0</td></tr><tr><td>Sim. Threshold</td><td>0.10–0.30</td></tr><tr><td rowspan="3">Traversal (Phase 2)</td><td>Max Depth</td><td>5 hops</td></tr><tr><td>Max Nodes</td><td>200</td></tr><tr><td>Drop Threshold</td><td>0.15</td></tr><tr><td rowspan="6">Adaptive Weights</td><td><math><semantics><msub><mi>λ</mi> <mn>1</mn></msub> <annotation>\lambda_{1}</annotation></semantics></math> (Structure Coef.)</td><td>1.0 (Base)</td></tr><tr><td><math><semantics><msub><mi>λ</mi> <mn>2</mn></msub> <annotation>\lambda_{2}</annotation></semantics></math> (Semantic Coef.)</td><td>0.3 – 0.7</td></tr><tr><td><math><semantics><msub><mi>w</mi> <mrow><mi>e</mi> <mo></mo><mi>n</mi> <mo></mo><mi>t</mi> <mo></mo><mi>i</mi> <mo></mo><mi>t</mi> <mo></mo><mi>y</mi></mrow></msub> <annotation>w_{entity}</annotation></semantics></math> (in <math><semantics><msub><mi>𝐰</mi> <msub><mi>T</mi> <mi>q</mi></msub></msub> <annotation>\mathbf{w}_{T_{q}}</annotation></semantics></math>)</td><td>2.5 – 6.0</td></tr><tr><td><math><semantics><msub><mi>w</mi> <mrow><mi>t</mi> <mo></mo><mi>e</mi> <mo></mo><mi>m</mi> <mo></mo><mi>p</mi> <mo></mo><mi>o</mi> <mo></mo><mi>r</mi> <mo></mo><mi>a</mi> <mo></mo><mi>l</mi></mrow></msub> <annotation>w_{temporal}</annotation></semantics></math> (in <math><semantics><msub><mi>𝐰</mi> <msub><mi>T</mi> <mi>q</mi></msub></msub> <annotation>\mathbf{w}_{T_{q}}</annotation></semantics></math>)</td><td>0.5 – 4.0</td></tr><tr><td><math><semantics><msub><mi>w</mi> <mrow><mi>c</mi> <mo></mo><mi>a</mi> <mo></mo><mi>u</mi> <mo></mo><mi>s</mi> <mo></mo><mi>a</mi> <mo></mo><mi>l</mi></mrow></msub> <annotation>w_{causal}</annotation></semantics></math> (in <math><semantics><msub><mi>𝐰</mi> <msub><mi>T</mi> <mi>q</mi></msub></msub> <annotation>\mathbf{w}_{T_{q}}</annotation></semantics></math>)</td><td>3.0 – 5.0</td></tr><tr><td><math><semantics><msub><mi>w</mi> <mrow><mi>p</mi> <mo></mo><mi>h</mi> <mo></mo><mi>r</mi> <mo></mo><mi>a</mi> <mo></mo><mi>s</mi> <mo></mo><mi>e</mi></mrow></msub> <annotation>w_{phrase}</annotation></semantics></math> (in <math><semantics><msub><mi>𝐰</mi> <msub><mi>T</mi> <mi>q</mi></msub></msub> <annotation>\mathbf{w}_{T_{q}}</annotation></semantics></math>)</td><td>2.5 – 5.0</td></tr></tbody></table>

## Appendix C Prompt Library

MAGMA employs a sophisticated prompt strategy with three distinct types, each optimized for specific cognitive tasks within the memory pipeline.

### C.1 Event Extraction Prompt (JSON-Structured)

To ensure robustness against hallucination and parsing errors, this module employs a strict JSON schema enforcement strategy. The prompt explicitly defines the extraction targets to ensure downstream graph integrity, capturing not just entities but also semantic relationships and temporal markers.

<svg id="A3.SS1.p2.pic1" height="1676.55" overflow="visible" version="1.1" viewBox="0 0 600 1676.55" width="600"><g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" transform="translate(0,1676.55) matrix(1 0 0 -1 0 0)" fill="#000000" stroke="#000000" stroke-width="0.4pt"><g style="--ltx-fill-color:#000000;" fill="#000000" fill-opacity="1.0"><path style="stroke:none" d="M 0 5.91 L 0 1670.64 C 0 1673.9 2.64 1676.55 5.91 1676.55 L 594.09 1676.55 C 597.36 1676.55 600 1673.9 600 1670.64 L 600 5.91 C 600 2.64 597.36 0 594.09 0 L 5.91 0 C 2.64 0 0 2.64 0 5.91 Z"></path></g><g style="--ltx-fill-color:#F2F2F2;" fill="#F2F2F2" fill-opacity="1.0"><path style="stroke:none" d="M 1.97 5.91 L 1.97 1173.72 L 598.03 1173.72 L 598.03 5.91 C 598.03 3.73 596.27 1.97 594.09 1.97 L 5.91 1.97 C 3.73 1.97 1.97 3.73 1.97 5.91 Z"></path></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 21.65 1661.15)"><foreignObject style="--ltx-fg-color:#FFFFFF;--ltx-fo-width:40.23em;--ltx-fo-height:0.69em;--ltx-fo-depth:34.8em;" width="556.69" height="491.02" transform="matrix(1 0 0 -1 0 9.49)" overflow="visible" color="#FFFFFF"><span id="A3.SS1.p2.pic1.1.1.1.1.1" style="width:34.98em;"><span id="A3.SS1.p2.pic1.1.1.1.1.1.1"><span id="A3.SS1.p2.pic1.1.1.1.1.1.1.1">System Prompt: Event Extractor</span></span> </span></foreignObject></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 21.65 247.62)"><foreignObject style="--ltx-fg-color:#000000;--ltx-fo-width:40.23em;--ltx-fo-height:66.07em;--ltx-fo-depth:16.9em;" width="556.69" height="1148.13" transform="matrix(1 0 0 -1 0 914.28)" overflow="visible" color="#000000"><span id="A3.SS1.p2.pic1.2.2.2.1.1" style="width:40.23em;"><span id="A3.SS1.p2.pic1.2.2.2.1.1.1"><span id="A3.SS1.p2.pic1.2.2.2.1.1.1.1">System Role:</span> You are an automated Graph Memory Parser. Your task is to extract structured metadata from raw conversational logs to build a knowledge graph.</span> <span id="A3.SS1.p2.pic1.2.2.2.1.1.2"><span id="A3.SS1.p2.pic1.2.2.2.1.1.2.1">Input Data:</span></span> <span id="A3.I1"><span id="A3.I1.i1" style="list-style-type:none;">• <span id="A3.I1.i1.p1"><span id="A3.I1.i1.p1.1">Speaker: {speaker}</span> </span></span><span id="A3.I1.i2" style="list-style-type:none;">• <span id="A3.I1.i2.p1"><span id="A3.I1.i2.p1.1">Text: {text}</span> </span></span><span id="A3.I1.i3" style="list-style-type:none;">• <span id="A3.I1.i3.p1"><span id="A3.I1.i3.p1.1">Context: {prev_summary}</span> </span></span></span><span id="A3.SS1.p2.pic1.2.2.2.1.1.3"><span id="A3.SS1.p2.pic1.2.2.2.1.1.3.1">Instructions:</span> Analyze the input and return <span id="A3.SS1.p2.pic1.2.2.2.1.1.3.2">ONLY</span> a valid JSON object matching the specific schema below. Do not include markdown formatting.</span> <span id="A3.SS1.p2.pic1.2.2.2.1.1.4"><span id="A3.SS1.p2.pic1.2.2.2.1.1.4.1">Target Schema:</span></span> <span id="A3.I2"><span id="A3.I2.i1" style="list-style-type:none;">• <span id="A3.I2.i1.p1"><span id="A3.I2.i1.p1.1"><span id="A3.I2.i1.p1.1.1">"entities"</span>: List of proper nouns (People, Locations, Organizations).</span></span></span> <span id="A3.I2.i2" style="list-style-type:none;">• <span id="A3.I2.i2.p1"><span id="A3.I2.i2.p1.1"><span id="A3.I2.i2.p1.1.1">"topic"</span>: String (1–3 words representing the main theme).</span></span></span> <span id="A3.I2.i3" style="list-style-type:none;">• <span id="A3.I2.i3.p1"><span id="A3.I2.i3.p1.1"><span id="A3.I2.i3.p1.1.1">"relationships"</span>: List of strings describing interactions (e.g., "X researches Y").</span></span></span> <span id="A3.I2.i4" style="list-style-type:none;">• <span id="A3.I2.i4.p1"><span id="A3.I2.i4.p1.1"><span id="A3.I2.i4.p1.1.1">"semantic_facts"</span>: List of atomic facts preserving key information.</span></span></span> <span id="A3.I2.i5" style="list-style-type:none;">• <span id="A3.I2.i5.p1"><span id="A3.I2.i5.p1.1"><span id="A3.I2.i5.p1.1.1">"dates_mentioned"</span>: List of temporal strings (e.g., "next Friday", "2024-01-01").</span></span></span> <span id="A3.I2.i6" style="list-style-type:none;">• <span id="A3.I2.i6.p1"><span id="A3.I2.i6.p1.1"><span id="A3.I2.i6.p1.1.1">"summary"</span>: One-sentence summary preserving speaker attribution.</span></span></span></span></span></foreignObject></g></g></svg>

### C.2 Query-Adaptive QA Prompt

The generation prompt begins with a strict persona definition and appends specific reasoning instructions dynamically based on the Router’s classification (e.g., Multi-hop, Temporal, Open-domain).

<svg id="A3.SS2.p2.pic1" height="3434.52" overflow="visible" version="1.1" viewBox="0 0 600 3434.52" width="600"><g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" transform="translate(0,3434.52) matrix(1 0 0 -1 0 0)" fill="#000000" stroke="#000000" stroke-width="0.4pt"><g style="--ltx-fill-color:#000000;" fill="#000000" fill-opacity="1.0"><path style="stroke:none" d="M 0 5.91 L 0 3428.62 C 0 3431.88 2.64 3434.52 5.91 3434.52 L 594.09 3434.52 C 597.36 3434.52 600 3431.88 600 3428.62 L 600 5.91 C 600 2.64 597.36 0 594.09 0 L 5.91 0 C 2.64 0 0 2.64 0 5.91 Z"></path></g><g style="--ltx-fill-color:#F2F2F2;" fill="#F2F2F2" fill-opacity="1.0"><path style="stroke:none" d="M 1.97 5.91 L 1.97 2998.11 L 598.03 2998.11 L 598.03 5.91 C 598.03 3.73 596.27 1.97 594.09 1.97 L 5.91 1.97 C 3.73 1.97 1.97 3.73 1.97 5.91 Z"></path></g><g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;--ltx-fg-color:#000000;" stroke-dasharray="2.84528pt,2.84528pt" stroke-dashoffset="1.42264pt" fill="#000000" stroke="#000000" stroke-opacity="1.0" color="#000000"><path style="fill:none" d="M 1.97 1962.08 L 598.03 1962.08"></path></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 21.65 3419.12)"><foreignObject style="--ltx-fg-color:#FFFFFF;--ltx-fo-width:40.23em;--ltx-fo-height:0.69em;--ltx-fo-depth:30em;" width="556.69" height="424.6" transform="matrix(1 0 0 -1 0 9.49)" overflow="visible" color="#FFFFFF"><span id="A3.SS2.p2.pic1.1.1.1.1.1" style="width:34.98em;"><span id="A3.SS2.p2.pic1.1.1.1.1.1.1"><span id="A3.SS2.p2.pic1.1.1.1.1.1.1.1">System Prompt: Adaptive QA</span></span> </span></foreignObject></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 21.65 2073.52)"><foreignObject style="--ltx-fg-color:#000000;--ltx-fo-width:40.23em;--ltx-fo-height:65.97em;--ltx-fo-depth:7.2em;" width="556.69" height="1012.41" transform="matrix(1 0 0 -1 0 912.78)" overflow="visible" color="#000000"><span id="A3.SS2.p2.pic1.2.2.2.1.1" style="width:40.23em;"><span id="A3.SS2.p2.pic1.2.2.2.1.1.1"><span id="A3.SS2.p2.pic1.2.2.2.1.1.1.1">System Role:</span> You are a precision QA assistant operating on retrieved memory contexts. Your goal is to answer the user’s question accurately using <span id="A3.SS2.p2.pic1.2.2.2.1.1.1.2">only</span> the provided information.</span> <span id="A3.SS2.p2.pic1.2.2.2.1.1.2"><span id="A3.SS2.p2.pic1.2.2.2.1.1.2.1">Context:</span> {context}</span> <span id="A3.SS2.p2.pic1.2.2.2.1.1.3"><span id="A3.SS2.p2.pic1.2.2.2.1.1.3.1">Current Query:</span></span> <span id="A3.I3"><span id="A3.I3.i1" style="list-style-type:none;">• <span id="A3.I3.i1.p1"><span id="A3.I3.i1.p1.1">Question: {question}</span> </span></span><span id="A3.I3.i2" style="list-style-type:none;">• <span id="A3.I3.i2.p1"><span id="A3.I3.i2.p1.1">Constraints: {category_specific_constraints}</span> </span></span></span><span id="A3.SS2.p2.pic1.2.2.2.1.1.4"><span id="A3.SS2.p2.pic1.2.2.2.1.1.4.1">Instructions:</span></span> <span id="A3.I4"><span id="A3.I4.i1" style="list-style-type:none;">1. <span id="A3.I4.i1.p1"><span id="A3.I4.i1.p1.1">Use ONLY information explicitly stated in the context.</span></span></span> <span id="A3.I4.i2" style="list-style-type:none;">2. <span id="A3.I4.i2.p1"><span id="A3.I4.i2.p1.1">If the answer is not present, respond exactly with "Information not found".</span></span></span> <span id="A3.I4.i3" style="list-style-type:none;">3. <span id="A3.I4.i3.p1"><span id="A3.I4.i3.p1.1">Be concise (typically 1–10 words) unless detailed reasoning is required.</span></span></span> <span id="A3.I4.i4" style="list-style-type:none;">4. <span id="A3.I4.i4.p1"><span id="A3.I4.i4.p1.1"><span id="A3.I4.i4.p1.1.1">{dynamic_instruction}</span> <span id="A3.I4.i4.p1.1.2" style="--ltx-fg-color:#999999;">// Automatically generated by our engine’s query classifier/router (no oracle labels)</span></span> </span></span></span><span id="A3.SS2.p2.pic1.2.2.2.1.1.5"><span id="A3.SS2.p2.pic1.2.2.2.1.1.5.1">Answer:</span></span></span> </foreignObject></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 21.65 1241.12)"><foreignObject style="--ltx-fg-color:#000000;--ltx-fo-width:40.23em;--ltx-fo-height:51.25em;--ltx-fo-depth:88.7em;" width="556.69" height="1936.49" transform="matrix(1 0 0 -1 0 709.15)" overflow="visible" color="#000000"><span id="A3.SS2.p2.pic1.3.3.3.1.1" style="width:40.23em;"><span id="A3.SS2.p2.pic1.3.3.3.1.1.1"><span id="A3.SS2.p2.pic1.3.3.3.1.1.1.1">*Dynamic Instruction Injection Candidates:</span></span> <span id="A3.I5"><span id="A3.I5.i1" style="list-style-type:none;">• <span id="A3.I5.i1.p1"><span id="A3.I5.i1.p1.1"><span id="A3.I5.i1.p1.1.1">[Multi-hop]:</span> "Connect related facts across different nodes. For comparison queries (e.g., ’both/all’), identify commonalities between entities rather than listing individual details."</span> </span></span><span id="A3.I5.i2" style="list-style-type:none;">• <span id="A3.I5.i2.p1"><span id="A3.I5.i2.p1.1"><span id="A3.I5.i2.p1.1.1">[Temporal]:</span> "Resolve relative dates (e.g., ’yesterday’) using the event timestamps. Output dates strictly in ’D Month YYYY’ format. Calculate durations if asked."</span> </span></span><span id="A3.I5.i3" style="list-style-type:none;">• <span id="A3.I5.i3.p1"><span id="A3.I5.i3.p1.1"><span id="A3.I5.i3.p1.1.1">[Open-Domain/Inference]:</span> "Make reasonable inferences based on the user’s personality traits, interests, and past behaviors. Support hypothetical (’would/could’) reasoning with evidence."</span> </span></span><span id="A3.I5.i4" style="list-style-type:none;">• <span id="A3.I5.i4.p1"><span id="A3.I5.i4.p1.1"><span id="A3.I5.i4.p1.1.1">[Single-hop/Factual]:</span> "Extract the specific entity, name, or method requested. Do not add explanations. Return the exact fact matching the query intent."</span></span></span></span></span></foreignObject></g></g></svg>

### C.3 Evaluation Prompt (LLM-as-a-Judge)

To ensure rigorous evaluation beyond simple n-gram overlapping, we employ a semantic scoring mechanism. The Judge LLM evaluates the alignment between the generated response and the ground truth using the following schema.

<svg id="A3.SS3.p2.pic1" height="2213.85" overflow="visible" version="1.1" viewBox="0 0 600 2213.85" width="600"><g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" transform="translate(0,2213.85) matrix(1 0 0 -1 0 0)" fill="#000000" stroke="#000000" stroke-width="0.4pt"><g style="--ltx-fill-color:#000000;" fill="#000000" fill-opacity="1.0"><path style="stroke:none" d="M 0 5.91 L 0 2207.94 C 0 2211.2 2.64 2213.85 5.91 2213.85 L 594.09 2213.85 C 597.36 2213.85 600 2211.2 600 2207.94 L 600 5.91 C 600 2.64 597.36 0 594.09 0 L 5.91 0 C 2.64 0 0 2.64 0 5.91 Z"></path></g><g style="--ltx-fill-color:#F2F2F2;" fill="#F2F2F2" fill-opacity="1.0"><path style="stroke:none" d="M 1.97 5.91 L 1.97 1711.01 L 598.03 1711.01 L 598.03 5.91 C 598.03 3.73 596.27 1.97 594.09 1.97 L 5.91 1.97 C 3.73 1.97 1.97 3.73 1.97 5.91 Z"></path></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 21.65 2198.45)"><foreignObject style="--ltx-fg-color:#FFFFFF;--ltx-fo-width:40.23em;--ltx-fo-height:0.69em;--ltx-fo-depth:34.8em;" width="556.69" height="491.02" transform="matrix(1 0 0 -1 0 9.49)" overflow="visible" color="#FFFFFF"><span id="A3.SS3.p2.pic1.1.1.1.1.1" style="width:34.98em;"><span id="A3.SS3.p2.pic1.1.1.1.1.1.1"><span id="A3.SS3.p2.pic1.1.1.1.1.1.1.1">System Prompt: Semantic Grader</span></span> </span></foreignObject></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 21.65 17.24)"><foreignObject style="--ltx-fg-color:#000000;--ltx-fo-width:40.23em;--ltx-fo-height:121.56em;--ltx-fo-depth:0.25em;" width="556.69" height="1685.42" transform="matrix(1 0 0 -1 0 1681.96)" overflow="visible" color="#000000"><span id="A3.SS3.p2.pic1.2.2.2.1.1" style="width:40.23em;"><span id="A3.SS3.p2.pic1.2.2.2.1.1.1">You are an expert evaluator assessing the semantic fidelity of a memory retrieval system. Score the <span id="A3.SS3.p2.pic1.2.2.2.1.1.1.1">Candidate Answer</span> against the <span id="A3.SS3.p2.pic1.2.2.2.1.1.1.2">Gold Reference</span> on a continuous scale [0.0, 1.0].</span> <span id="A3.SS3.p2.pic1.2.2.2.1.1.2"><span id="A3.SS3.p2.pic1.2.2.2.1.1.2.1">Scoring Rubric:</span></span> <span id="A3.I6"><span id="A3.I6.i1" style="list-style-type:none;">• <span id="A3.I6.i1.p1"><span id="A3.I6.i1.p1.1"><span id="A3.I6.i1.p1.1.1">1.0 (Exact Alignment):</span> Captures all key entities, temporal markers, and causal relationships. Semantically equivalent.</span></span></span> <span id="A3.I6.i2" style="list-style-type:none;">• <span id="A3.I6.i2.p1"><span id="A3.I6.i2.p1.1"><span id="A3.I6.i2.p1.1.1">0.8 (Substantially Correct):</span> Main point is accurate but lacks minor nuances or secondary details.</span></span></span> <span id="A3.I6.i3" style="list-style-type:none;">• <span id="A3.I6.i3.p1"><span id="A3.I6.i3.p1.1"><span id="A3.I6.i3.p1.1.1">0.6 (Partial Match):</span> Contains valid information but misses key constraints (e.g., wrong date but correct event).</span></span></span> <span id="A3.I6.i4" style="list-style-type:none;">• <span id="A3.I6.i4.p1"><span id="A3.I6.i4.p1.1"><span id="A3.I6.i4.p1.1.1">0.4 (Tangential):</span> Touches on the topic but misses the core information requirement.</span></span></span> <span id="A3.I6.i5" style="list-style-type:none;">• <span id="A3.I6.i5.p1"><span id="A3.I6.i5.p1.1"><span id="A3.I6.i5.p1.1.1">0.2 (Incoherent):</span> Factually incorrect with only minimal topical overlap.</span></span></span> <span id="A3.I6.i6" style="list-style-type:none;">• <span id="A3.I6.i6.p1"><span id="A3.I6.i6.p1.1"><span id="A3.I6.i6.p1.1.1">0.0 (Contradiction/Hallucination):</span> Completely unrelated or contradicts the ground truth.</span></span></span></span> <span id="A3.SS3.p2.pic1.2.2.2.1.1.3"><span id="A3.SS3.p2.pic1.2.2.2.1.1.3.1">Evaluation Constraints:</span></span> <span id="A3.I7"><span id="A3.I7.i1" style="list-style-type:none;">1. <span id="A3.I7.i1.p1"><span id="A3.I7.i1.p1.1"><span id="A3.I7.i1.p1.1.1">Temporal Flexibility:</span> Accept relative time references (e.g., "next Tuesday") if they resolve to the same period as the Gold Reference.</span></span></span> <span id="A3.I7.i2" style="list-style-type:none;">2. <span id="A3.I7.i2.p1"><span id="A3.I7.i2.p1.1"><span id="A3.I7.i2.p1.1.1">Semantic Equivalence:</span> Prioritize informational content over lexical matching.</span></span></span> <span id="A3.I7.i3" style="list-style-type:none;">3. <span id="A3.I7.i3.p1"><span id="A3.I7.i3.p1.1"><span id="A3.I7.i3.p1.1.1">Adversarial Handling:</span> If the Gold Reference states "Unanswerable", the Candidate MUST explicitly state lack of information. Any hallucinated fact results in 0.0.</span></span></span></span> <span id="A3.SS3.p2.pic1.2.2.2.1.1.4"><span id="A3.SS3.p2.pic1.2.2.2.1.1.4.1">Input:</span> Question: {question} | Gold: {gold} | Candidate: {generated}</span> <span id="A3.SS3.p2.pic1.2.2.2.1.1.5"><span id="A3.SS3.p2.pic1.2.2.2.1.1.5.1">Output:</span> JSON <span id="A3.SS3.p2.pic1.2.2.2.1.1.5.2">{"score": float, "reasoning": "concise explanation"}</span></span></span></foreignObject></g></g></svg>

## Appendix D Baseline Configurations

To ensure a fair and rigorous comparison, we standardized the experimental environment across all systems. Specifically, we adhered to the following protocols:

- Full Context Baseline: We implemented a "Full Context" baseline where the entire available conversation history is fed directly into the LLM’s context window (up to the 128k token limit of gpt-4o-mini). This serves as a "brute-force" reference to evaluate the model’s native long-context capabilities without external retrieval mechanisms.
- Retrieval-Based Baselines: For all baseline systems (e.g., AMem, Nemori, MemoryOS), we applied their official default hyperparameters and storage settings to reflect their standard out-of-the-box performance.
- Unified Backbone Model: To eliminate performance variance caused by different foundation models, all systems utilized OpenAI’s gpt-4o-mini for both retrieval reasoning and response generation.
- Unified Evaluation: All system outputs were evaluated using the identical LLM-as-a-Judge framework (also powered by gpt-4o-mini with temperature=0.0), as detailed in Appendix C.

#### Dataset Statistics.

We conducted a comprehensive evaluation on the full LoCoMo benchmark, testing across all five cognitive categories to assess varying levels of retrieval complexity. The detailed distribution of query types is presented in Table 7.

Table 7: Distribution of query categories in the LoCoMo benchmark used for evaluation.

| Query Category | Count |
| --- | --- |
| Single-Hop Retrieval | 841 |
| Adversarial | 446 |
| Temporal Reasoning | 321 |
| Multi-Hop Reasoning | 282 |
| Open Domain | 96 |
| Total Samples | 1,986 |

## Appendix E Case Study

To demonstrate MAGMA’s reasoning capabilities across different cognitive modalities, we analyze three real-world scenarios from the LoCoMo benchmark. Table 8 provides a side-by-side comparison of MAGMA against key baselines (A-MEM, Nemori, MemoryOS).

Table 8: Case study for failure analysis comparing MAGMA against baselines across three reasoning types. Red text indicates hallucinations or partial failures; Teal text indicates correct reasoning derived from graph traversal.

|  | Query & Type | Baseline Failure Mode | MAGMA Graph Reasoning (Success) |
| --- | --- | --- | --- |
| Fact | Q1: Fact Retrieval   "What instruments does Melanie play?" | A-MEM: "Memories do not explicitly state…"   MemoryOS: "Clarinet"   Failure: Baselines relying on top-k vector search missed the distant memory of the "violin" (D2:5) because it appeared in a context about "me-time" rather than explicitly about music. | "Clarinet and Violin."   Mechanism: MAGMA utilized the entity-centric subgraph around "Melanie". By traversing dynamic semantic edges (e.g., "playing", "enjoy") to connected event nodes, it aggregated all mentions of musical activities regardless of the specific relation label or distance. |
| Logic | Q2: Logical Inference   "How many children does Melanie have?" | Nemori: "At least two…"   MemoryOS: "Two"   Failure: Baselines performed surface-level extraction from a photo description showing "two children" (D18:5), failing to account for the "son" mentioned in a separate accident event. | "At least three."   Mechanism: MAGMA executed multi-hop inference focused on Entity Resolution: 1. Node A (Photo): Identified "two kids" entity. 2. Node B (Accident): Linked "son" (D18:1) via a dynamic relationship edge. 3. Node C (Dialogue): Confirmed "brother" (D18:7) is distinct from the two in the photo. $\rightarrow$ Logic: $2\text{ (Photo)}+1\text{ (Son/Brother)}=3$. |
| Time | Q3: Temporal Res.   "When did she hike after the roadtrip?" | A-MEM: "20 October 2023"   MemoryOS: "29 December 2025"   Failure: A-MEM simply copied the session timestamp. MemoryOS hallucinated a future date. Both failed to resolve the relative time expression. | "19 October 2023"   Mechanism: MAGMA’s Temporal Parser identified the relative marker "yesterday" in D18:17. Calculation: $T_{\text{session}}(Oct20)-1\text{ day}=Oct19$. This exact date was anchored to the Event Node, allowing precise retrieval. |

### E.1 Illustrative Walkthrough: From Memory Construction to Retrieval

To make the case study more concrete, we briefly illustrate how MAGMA processes the Melanie example end to end. Consider three representative facts from the conversation history: (1) Melanie mentions playing the violin in an earlier session, (2) she later says that she also plays the clarinet, and (3) in a later family-trip session, she refers to her son, two children in a photo, and a hike done yesterday.

During memory construction, MAGMA first segments these utterances into event nodes and places them along a temporal backbone. The system then incrementally enriches this memory with additional structure, such as semantic connections between related musical events, entity-centric links for recurring references to Melanie and her family members, and normalized temporal attributes for relative expressions such as yesterday. As a result, the memory is not stored as a flat list of text snippets, but as a small multi-view graph in which the same history can be accessed through different relational paths.

At query time, MAGMA first identifies the dominant retrieval intent and then selects anchor events before traversing the most relevant graph views. For example, for “What instruments does Melanie play?”, retrieval focuses on the entity and semantic views, allowing MAGMA to aggregate both the earlier violin mention and the later clarinet mention. For “How many children does Melanie have?”, retrieval centers on the local entity neighborhood, combining the references to a son, two children, and brother into a single evidence set. For “When did she hike?”, MAGMA relies primarily on the temporal view, using the normalized representation of yesterday to recover the grounded date.

This example highlights the key intuition behind MAGMA: memory construction organizes conversational history into complementary relational views, and query-time retrieval activates different parts of this structure depending on the reasoning need.

### E.2 Detailed Analysis

#### Case 1: Overcoming Information Loss (Recall).

For the query regarding instruments, A-MEM failed completely due to its summarization process abstracting away specific details ("violin") from early sessions. Other RAG baselines only retrieved the "clarinet" due to surface-level semantic matching. MAGMA, however, maintains an entity-centric graph structure. Instead of relying on rigid schemas, MAGMA queries the local neighborhood of the \[Entity: Melanie\] node. This allows it to capture diverse natural language predicates (e.g., "playing my violin", "started clarinet") and aggregate disjoint facts into a comprehensive answer, demonstrating robustness against information loss.

#### Case 2: Multi-Hop Reasoning vs. Surface Extraction.

The query "How many children?" exposes a critical weakness in standard RAG: the inability to perform arithmetic across contexts. Baselines simply extracted the explicit mention of "two children" from a photo caption. In contrast, MAGMA treated this as a graph traversal problem focused on entity resolution. It queried the neighborhood of \[Entity: Melanie\] for connected nodes of type Person. By analyzing the semantic edges, specifically distinguishing the "two kids" entity in the canyon photo from the "son" entity involved in the car accident, MAGMA synthesized these distinct nodes. It correctly deduced that the "son" (referenced later as "brother") was an additional individual, summing up to a count of "at least three," a logical leap impossible for systems relying solely on vector similarity.

#### Case 3: Temporal Grounding.

When asked "When did she hike?", baselines either hallucinated or defaulted to the conversation timestamp (Oct 20). This ignores the semantic meaning of the user’s statement: "we just did it yesterday." MAGMA’s structured ingestion pipeline normalizes relative dates during graph construction. The event was stored with the resolved attribute date="2023-10-19", making the retrieval trivial and exact, completely bypassing the ambiguity that confused the LLM-based baselines.

Table 9: LoCoMo evaluation with F1 and BLEU-1 metrics

<table><thead><tr><th></th><th colspan="2">Multi-Hop</th><th colspan="2">Temporal</th><th colspan="2">Open-Domain</th><th colspan="2">Single-Hop</th><th colspan="2">Overall</th></tr><tr><th>Method</th><th>F1</th><th>BLEU-1</th><th>F1</th><th>BLEU-1</th><th>F1</th><th>BLEU-1</th><th>F1</th><th>BLEU-1</th><th>F1</th><th>BLEU-1</th></tr></thead><tbody><tr><td>Full Context</td><td>0.182</td><td>0.128</td><td>0.079</td><td>0.055</td><td>0.042</td><td>0.030</td><td>0.229</td><td>0.156</td><td>0.140</td><td>0.096</td></tr><tr><td>A-MEM</td><td>0.128</td><td>0.088</td><td>0.128</td><td>0.079</td><td>0.076</td><td>0.051</td><td>0.174</td><td>0.110</td><td>0.116</td><td>0.074</td></tr><tr><td>MemoryOS</td><td>0.365</td><td>0.276</td><td>0.434</td><td>0.369</td><td>0.246</td><td>0.191</td><td>0.493</td><td>0.437</td><td>0.413</td><td>0.355</td></tr><tr><td>Nemori</td><td>0.363</td><td>0.249</td><td>0.569</td><td>0.479</td><td>0.247</td><td>0.189</td><td>0.548</td><td>0.439</td><td>0.502</td><td>0.403</td></tr><tr><td>MAGMA (ours)</td><td>0.264</td><td>0.172</td><td>0.509</td><td>0.370</td><td>0.180</td><td>0.136</td><td>0.551</td><td>0.477</td><td>0.467</td><td>0.378</td></tr></tbody></table>

## Appendix F Metric Validation Analysis

To validate our choice of using an LLM-based Judge over traditional lexical metrics, we conducted a granular failure analysis on seven representative test cases. Table 10 details the quantitative breakdown.

### F.1 Rationale for Semantic Scoring

Our empirical results reveal two critical failure modes where standard metrics (F1, BLEU-1) directly contradict human judgment:

1. False Rewards (The “Hallucination” Problem): Lexical metrics heavily reward incorrect answers that share surface-level tokens.
	- In Case 3, a direct negation (“compatible” vs. “not compatible”) yields a remarkably high F1 of 0.857, treating a fatal contradiction as a near-perfect match.
	- In Case 6, substituting the wrong entity (“John” vs. “Sarah”) still achieves F1 0.750, rewarding the hallucinatory output.
2. False Penalties (The “Phrasing” Problem): Valid answers with different formatting or synonyms are unfairly penalized.
	- In Case 4 (Time Notation) and Case 5 (Synonyms), F1 and BLEU scores drop to 0.000 despite the answers being semantically identical.

As shown in Table 10, the LLM-Judge correctly assigns a score of 0.0 to factual errors and 1.0 to semantic matches, aligning perfectly with reasoning requirements.

Table 10: Quantitative Failure Analysis of Lexical Metrics. We present seven controlled cases with their calculated F1 and BLEU-1 scores. The data demonstrates that lexical metrics frequently assign high scores to fatal errors (False Rewards) and zero scores to correct variations (False Penalties), whereas the LLM-Judge correctly assesses semantic validity.

<svg id="A6.T10.pic1" height="937.8" overflow="visible" version="1.1" viewBox="0 0 600 937.8" width="600"><g style="--ltx-stroke-color:#000000;--ltx-fill-color:#000000;" transform="translate(0,937.8) matrix(1 0 0 -1 0 0)" fill="#000000" stroke="#000000" stroke-width="0.4pt"><g style="--ltx-fill-color:#B3B3B3;" fill="#B3B3B3" fill-opacity="1.0"><path style="stroke:none" d="M 0 8.98 L 0 928.82 C 0 933.78 4.02 937.8 8.98 937.8 L 591.02 937.8 C 595.98 937.8 600 933.78 600 928.82 L 600 8.98 C 600 4.02 595.98 0 591.02 0 L 8.98 0 C 4.02 0 0 4.02 0 8.98 Z"></path></g><g style="--ltx-fill-color:#F9F9F9;" fill="#F9F9F9" fill-opacity="1.0"><path style="stroke:none" d="M 1.11 8.98 L 1.11 928.82 C 1.11 933.17 4.63 936.69 8.98 936.69 L 591.02 936.69 C 595.37 936.69 598.89 933.17 598.89 928.82 L 598.89 8.98 C 598.89 4.63 595.37 1.11 591.02 1.11 L 8.98 1.11 C 4.63 1.11 1.11 4.63 1.11 8.98 Z"></path></g><g fill-opacity="1.0" transform="matrix(1.0 0.0 0.0 1.0 20.79 465.44)"><foreignObject style="--ltx-fg-color:#000000;--ltx-fo-width:40.36em;--ltx-fo-height:33.2em;--ltx-fo-depth:32.7em;" width="40.36em" height="911.97" transform="matrix(1 0 0 -1 0 459.44)" overflow="visible" color="#000000"><table id="A6.T10.pic1.1.1.1.1.1"><thead><tr id="A6.T10.pic1.1.1.1.1.1.1.1" style="--ltx-bg-color:#E6E6E6;"><th id="A6.T10.pic1.1.1.1.1.1.1.1.1" style="padding-top:3pt;padding-bottom:3pt;"><span id="A6.T10.pic1.1.1.1.1.1.1.1.1.1" style="--ltx-bg-color:#E6E6E6;"><span id="A6.T10.pic1.1.1.1.1.1.1.1.1.1.1" style="width:100.9pt;"><span id="A6.T10.pic1.1.1.1.1.1.1.1.1.1.1.1">Failure Mode</span></span></span></th><th id="A6.T10.pic1.1.1.1.1.1.1.1.2" style="padding-top:3pt;padding-bottom:3pt;"><span id="A6.T10.pic1.1.1.1.1.1.1.1.2.1" style="--ltx-bg-color:#E6E6E6;"><span id="A6.T10.pic1.1.1.1.1.1.1.1.2.1.1"><span id="A6.T10.pic1.1.1.1.1.1.1.1.2.1.1.1">Case Detail (Gold / Predicted)</span></span></span></th><th id="A6.T10.pic1.1.1.1.1.1.1.1.3" style="padding-top:3pt;padding-bottom:3pt;"><span id="A6.T10.pic1.1.1.1.1.1.1.1.3.1" style="--ltx-bg-color:#E6E6E6;"><span id="A6.T10.pic1.1.1.1.1.1.1.1.3.1.1" style="width:48.4pt;"><span id="A6.T10.pic1.1.1.1.1.1.1.1.3.1.1.1">Lexical Metrics</span><br><span id="A6.T10.pic1.1.1.1.1.1.1.1.3.1.1.2">(F1 / BLEU-1)</span></span></span></th><th id="A6.T10.pic1.1.1.1.1.1.1.1.4" style="padding-top:3pt;padding-bottom:3pt;"><span id="A6.T10.pic1.1.1.1.1.1.1.1.4.1" style="--ltx-bg-color:#E6E6E6;"><span id="A6.T10.pic1.1.1.1.1.1.1.1.4.1.1" style="width:48.4pt;"><span id="A6.T10.pic1.1.1.1.1.1.1.1.4.1.1.1">LLM Judge</span><br><span id="A6.T10.pic1.1.1.1.1.1.1.1.4.1.1.2">(Semantic)</span></span></span></th></tr></thead><tbody><tr id="A6.T10.pic1.1.1.1.1.1.2.1"><td id="A6.T10.pic1.1.1.1.1.1.2.1.1" style="padding-top:3pt;padding-bottom:3pt;"><span id="A6.T10.pic1.1.1.1.1.1.2.1.1.1"><span id="A6.T10.pic1.1.1.1.1.1.2.1.1.1.1" style="width:100.9pt;"><span id="A6.T10.pic1.1.1.1.1.1.2.1.1.1.1.1">Case 1: False Reward</span><br><span id="A6.T10.pic1.1.1.1.1.1.2.1.1.1.1.2">(Wrong Fact, High Overlap)</span></span></span></td><td id="A6.T10.pic1.1.1.1.1.1.2.1.2" style="padding-top:3pt;padding-bottom:3pt;"><span id="A6.T10.pic1.1.1.1.1.1.2.1.2.1"><span id="A6.T10.pic1.1.1.1.1.1.2.1.2.1.1"><span id="A6.T10.pic1.1.1.1.1.1.2.1.2.1.1.1">Gold:</span> “three items”<br><span id="A6.T10.pic1.1.1.1.1.1.2.1.2.1.1.2">Pred:</span> “five items”<br><span id="A6.T10.pic1.1.1.1.1.1.2.1.2.1.1.3">Analysis:</span> Factually wrong count, but rewarded for sharing the noun “items”.</span></span></td><td id="A6.T10.pic1.1.1.1.1.1.2.1.3" style="padding-top:3pt;padding-bottom:3pt;"><span id="A6.T10.pic1.1.1.1.1.1.2.1.3.1"><span id="A6.T10.pic1.1.1.1.1.1.2.1.3.1.1" style="width:48.4pt;"><span id="A6.T10.pic1.1.1.1.1.1.2.1.3.1.1.1" style="--ltx-fg-color:#FF0000;">High</span><br>0.500 / 0.500</span></span></td><td id="A6.T10.pic1.1.1.1.1.1.2.1.4" style="padding-top:3pt;padding-bottom:3pt;"><span id="A6.T10.pic1.1.1.1.1.1.2.1.4.1"><span id="A6.T10.pic1.1.1.1.1.1.2.1.4.1.1" style="width:48.4pt;"><span id="A6.T10.pic1.1.1.1.1.1.2.1.4.1.1.1" style="--ltx-fg-color:#008080;">0.0</span><br>(Reject)</span></span></td></tr><tr id="A6.T10.pic1.1.1.1.1.1.3.2"><td id="A6.T10.pic1.1.1.1.1.1.3.2.1" style="padding-top:3pt;padding-bottom:3pt;"><span id="A6.T10.pic1.1.1.1.1.1.3.2.1.1"><span id="A6.T10.pic1.1.1.1.1.1.3.2.1.1.1" style="width:100.9pt;"><span id="A6.T10.pic1.1.1.1.1.1.3.2.1.1.1.1">Case 2: False Penalty</span><br><span id="A6.T10.pic1.1.1.1.1.1.3.2.1.1.1.2">(Verbose Phrasing)</span></span></span></td><td id="A6.T10.pic1.1.1.1.1.1.3.2.2" style="padding-top:3pt;padding-bottom:3pt;"><span id="A6.T10.pic1.1.1.1.1.1.3.2.2.1"><span id="A6.T10.pic1.1.1.1.1.1.3.2.2.1.1"><span id="A6.T10.pic1.1.1.1.1.1.3.2.2.1.1.1">Gold:</span> “18 days”<br><span id="A6.T10.pic1.1.1.1.1.1.3.2.2.1.1.2">Pred:</span> “The total duration was 18 days”<br><span id="A6.T10.pic1.1.1.1.1.1.3.2.2.1.1.3">Analysis:</span> Correct answer penalized for low precision due to extra words.</span></span></td><td id="A6.T10.pic1.1.1.1.1.1.3.2.3" style="padding-top:3pt;padding-bottom:3pt;"><span id="A6.T10.pic1.1.1.1.1.1.3.2.3.1"><span id="A6.T10.pic1.1.1.1.1.1.3.2.3.1.1" style="width:48.4pt;"><span id="A6.T10.pic1.1.1.1.1.1.3.2.3.1.1.1" style="--ltx-fg-color:#FF0000;">Low</span><br>0.500 / 0.333</span></span></td><td id="A6.T10.pic1.1.1.1.1.1.3.2.4" style="padding-top:3pt;padding-bottom:3pt;"><span id="A6.T10.pic1.1.1.1.1.1.3.2.4.1"><span id="A6.T10.pic1.1.1.1.1.1.3.2.4.1.1" style="width:48.4pt;"><span id="A6.T10.pic1.1.1.1.1.1.3.2.4.1.1.1" style="--ltx-fg-color:#008080;">1.0</span><br>(Accept)</span></span></td></tr><tr id="A6.T10.pic1.1.1.1.1.1.4.3"><td id="A6.T10.pic1.1.1.1.1.1.4.3.1" style="padding-top:3pt;padding-bottom:3pt;"><span id="A6.T10.pic1.1.1.1.1.1.4.3.1.1"><span id="A6.T10.pic1.1.1.1.1.1.4.3.1.1.1" style="width:100.9pt;"><span id="A6.T10.pic1.1.1.1.1.1.4.3.1.1.1.1">Case 3: False Reward</span><br><span id="A6.T10.pic1.1.1.1.1.1.4.3.1.1.1.2">(Negation/Contradiction)</span></span></span></td><td id="A6.T10.pic1.1.1.1.1.1.4.3.2" style="padding-top:3pt;padding-bottom:3pt;"><span id="A6.T10.pic1.1.1.1.1.1.4.3.2.1"><span id="A6.T10.pic1.1.1.1.1.1.4.3.2.1.1"><span id="A6.T10.pic1.1.1.1.1.1.4.3.2.1.1.1">Gold:</span> “compatible with Mac”<br><span id="A6.T10.pic1.1.1.1.1.1.4.3.2.1.1.2">Pred:</span> “ <span id="A6.T10.pic1.1.1.1.1.1.4.3.2.1.1.3">not</span> compatible with Mac”<br><span id="A6.T10.pic1.1.1.1.1.1.4.3.2.1.1.4">Analysis:</span> Fatal contradiction receives near-perfect scores due to high token overlap.</span></span></td><td id="A6.T10.pic1.1.1.1.1.1.4.3.3" style="padding-top:3pt;padding-bottom:3pt;"><span id="A6.T10.pic1.1.1.1.1.1.4.3.3.1"><span id="A6.T10.pic1.1.1.1.1.1.4.3.3.1.1" style="width:48.4pt;"><span id="A6.T10.pic1.1.1.1.1.1.4.3.3.1.1.1" style="--ltx-fg-color:#FF0000;">Very High</span><br>0.857 / 0.750</span></span></td><td id="A6.T10.pic1.1.1.1.1.1.4.3.4" style="padding-top:3pt;padding-bottom:3pt;"><span id="A6.T10.pic1.1.1.1.1.1.4.3.4.1"><span id="A6.T10.pic1.1.1.1.1.1.4.3.4.1.1" style="width:48.4pt;"><span id="A6.T10.pic1.1.1.1.1.1.4.3.4.1.1.1" style="--ltx-fg-color:#008080;">0.0</span><br>(Reject)</span></span></td></tr><tr id="A6.T10.pic1.1.1.1.1.1.5.4"><td id="A6.T10.pic1.1.1.1.1.1.5.4.1" style="padding-top:3pt;padding-bottom:3pt;"><span id="A6.T10.pic1.1.1.1.1.1.5.4.1.1"><span id="A6.T10.pic1.1.1.1.1.1.5.4.1.1.1" style="width:100.9pt;"><span id="A6.T10.pic1.1.1.1.1.1.5.4.1.1.1.1">Case 4: False Penalty</span><br><span id="A6.T10.pic1.1.1.1.1.1.5.4.1.1.1.2">(Time Notation)</span></span></span></td><td id="A6.T10.pic1.1.1.1.1.1.5.4.2" style="padding-top:3pt;padding-bottom:3pt;"><span id="A6.T10.pic1.1.1.1.1.1.5.4.2.1"><span id="A6.T10.pic1.1.1.1.1.1.5.4.2.1.1"><span id="A6.T10.pic1.1.1.1.1.1.5.4.2.1.1.1">Gold:</span> “14:00”<br><span id="A6.T10.pic1.1.1.1.1.1.5.4.2.1.1.2">Pred:</span> “2 PM”<br><span id="A6.T10.pic1.1.1.1.1.1.5.4.2.1.1.3">Analysis:</span> Different formats result in zero overlap despite identical meaning.</span></span></td><td id="A6.T10.pic1.1.1.1.1.1.5.4.3" style="padding-top:3pt;padding-bottom:3pt;"><span id="A6.T10.pic1.1.1.1.1.1.5.4.3.1"><span id="A6.T10.pic1.1.1.1.1.1.5.4.3.1.1" style="width:48.4pt;"><span id="A6.T10.pic1.1.1.1.1.1.5.4.3.1.1.1" style="--ltx-fg-color:#FF0000;">Zero</span><br>0.000 / 0.000</span></span></td><td id="A6.T10.pic1.1.1.1.1.1.5.4.4" style="padding-top:3pt;padding-bottom:3pt;"><span id="A6.T10.pic1.1.1.1.1.1.5.4.4.1"><span id="A6.T10.pic1.1.1.1.1.1.5.4.4.1.1" style="width:48.4pt;"><span id="A6.T10.pic1.1.1.1.1.1.5.4.4.1.1.1" style="--ltx-fg-color:#008080;">1.0</span><br>(Accept)</span></span></td></tr><tr id="A6.T10.pic1.1.1.1.1.1.6.5"><td id="A6.T10.pic1.1.1.1.1.1.6.5.1" style="padding-top:3pt;padding-bottom:3pt;"><span id="A6.T10.pic1.1.1.1.1.1.6.5.1.1"><span id="A6.T10.pic1.1.1.1.1.1.6.5.1.1.1" style="width:100.9pt;"><span id="A6.T10.pic1.1.1.1.1.1.6.5.1.1.1.1">Case 5: False Penalty</span><br><span id="A6.T10.pic1.1.1.1.1.1.6.5.1.1.1.2">(Synonyms)</span></span></span></td><td id="A6.T10.pic1.1.1.1.1.1.6.5.2" style="padding-top:3pt;padding-bottom:3pt;"><span id="A6.T10.pic1.1.1.1.1.1.6.5.2.1"><span id="A6.T10.pic1.1.1.1.1.1.6.5.2.1.1"><span id="A6.T10.pic1.1.1.1.1.1.6.5.2.1.1.1">Gold:</span> “cheap”<br><span id="A6.T10.pic1.1.1.1.1.1.6.5.2.1.1.2">Pred:</span> “inexpensive”<br><span id="A6.T10.pic1.1.1.1.1.1.6.5.2.1.1.3">Analysis:</span> Standard metrics cannot handle synonym matching without external resources.</span></span></td><td id="A6.T10.pic1.1.1.1.1.1.6.5.3" style="padding-top:3pt;padding-bottom:3pt;"><span id="A6.T10.pic1.1.1.1.1.1.6.5.3.1"><span id="A6.T10.pic1.1.1.1.1.1.6.5.3.1.1" style="width:48.4pt;"><span id="A6.T10.pic1.1.1.1.1.1.6.5.3.1.1.1" style="--ltx-fg-color:#FF0000;">Zero</span><br>0.000 / 0.000</span></span></td><td id="A6.T10.pic1.1.1.1.1.1.6.5.4" style="padding-top:3pt;padding-bottom:3pt;"><span id="A6.T10.pic1.1.1.1.1.1.6.5.4.1"><span id="A6.T10.pic1.1.1.1.1.1.6.5.4.1.1" style="width:48.4pt;"><span id="A6.T10.pic1.1.1.1.1.1.6.5.4.1.1.1" style="--ltx-fg-color:#008080;">1.0</span><br>(Accept)</span></span></td></tr><tr id="A6.T10.pic1.1.1.1.1.1.7.6"><td id="A6.T10.pic1.1.1.1.1.1.7.6.1" style="padding-top:3pt;padding-bottom:3pt;"><span id="A6.T10.pic1.1.1.1.1.1.7.6.1.1"><span id="A6.T10.pic1.1.1.1.1.1.7.6.1.1.1" style="width:100.9pt;"><span id="A6.T10.pic1.1.1.1.1.1.7.6.1.1.1.1">Case 6: False Reward</span><br><span id="A6.T10.pic1.1.1.1.1.1.7.6.1.1.1.2">(Entity Hallucination)</span></span></span></td><td id="A6.T10.pic1.1.1.1.1.1.7.6.2" style="padding-top:3pt;padding-bottom:3pt;"><span id="A6.T10.pic1.1.1.1.1.1.7.6.2.1"><span id="A6.T10.pic1.1.1.1.1.1.7.6.2.1.1"><span id="A6.T10.pic1.1.1.1.1.1.7.6.2.1.1.1">Gold:</span> “John completed the project”<br><span id="A6.T10.pic1.1.1.1.1.1.7.6.2.1.1.2">Pred:</span> “Sarah completed the project”<br><span id="A6.T10.pic1.1.1.1.1.1.7.6.2.1.1.3">Analysis:</span> Wrong entity (Sarah vs John), yet high metrics due to shared sentence structure.</span></span></td><td id="A6.T10.pic1.1.1.1.1.1.7.6.3" style="padding-top:3pt;padding-bottom:3pt;"><span id="A6.T10.pic1.1.1.1.1.1.7.6.3.1"><span id="A6.T10.pic1.1.1.1.1.1.7.6.3.1.1" style="width:48.4pt;"><span id="A6.T10.pic1.1.1.1.1.1.7.6.3.1.1.1" style="--ltx-fg-color:#FF0000;">High</span><br>0.750 / 0.750</span></span></td><td id="A6.T10.pic1.1.1.1.1.1.7.6.4" style="padding-top:3pt;padding-bottom:3pt;"><span id="A6.T10.pic1.1.1.1.1.1.7.6.4.1"><span id="A6.T10.pic1.1.1.1.1.1.7.6.4.1.1" style="width:48.4pt;"><span id="A6.T10.pic1.1.1.1.1.1.7.6.4.1.1.1" style="--ltx-fg-color:#008080;">0.0</span><br>(Reject)</span></span></td></tr><tr id="A6.T10.pic1.1.1.1.1.1.8.7"><td id="A6.T10.pic1.1.1.1.1.1.8.7.1" style="padding-top:3pt;padding-bottom:3pt;"><span id="A6.T10.pic1.1.1.1.1.1.8.7.1.1"><span id="A6.T10.pic1.1.1.1.1.1.8.7.1.1.1" style="width:100.9pt;"><span id="A6.T10.pic1.1.1.1.1.1.8.7.1.1.1.1">Case 7: False Penalty</span><br><span id="A6.T10.pic1.1.1.1.1.1.8.7.1.1.1.2">(Format Noise)</span></span></span></td><td id="A6.T10.pic1.1.1.1.1.1.8.7.2" style="padding-top:3pt;padding-bottom:3pt;"><span id="A6.T10.pic1.1.1.1.1.1.8.7.2.1"><span id="A6.T10.pic1.1.1.1.1.1.8.7.2.1.1"><span id="A6.T10.pic1.1.1.1.1.1.8.7.2.1.1.1">Gold:</span> “5”<br><span id="A6.T10.pic1.1.1.1.1.1.8.7.2.1.1.2">Pred:</span> “5 (extracted from JSON…)”<br><span id="A6.T10.pic1.1.1.1.1.1.8.7.2.1.1.3">Analysis:</span> Correct value embedded in noise results in poor precision metrics.</span></span></td><td id="A6.T10.pic1.1.1.1.1.1.8.7.3" style="padding-top:3pt;padding-bottom:3pt;"><span id="A6.T10.pic1.1.1.1.1.1.8.7.3.1"><span id="A6.T10.pic1.1.1.1.1.1.8.7.3.1.1" style="width:48.4pt;"><span id="A6.T10.pic1.1.1.1.1.1.8.7.3.1.1.1" style="--ltx-fg-color:#FF0000;">Low</span><br>0.286 / 0.167</span></span></td><td id="A6.T10.pic1.1.1.1.1.1.8.7.4" style="padding-top:3pt;padding-bottom:3pt;"><span id="A6.T10.pic1.1.1.1.1.1.8.7.4.1"><span id="A6.T10.pic1.1.1.1.1.1.8.7.4.1.1" style="width:48.4pt;"><span id="A6.T10.pic1.1.1.1.1.1.8.7.4.1.1.1" style="--ltx-fg-color:#008080;">1.0</span><br>(Accept)</span></span></td></tr></tbody></table></foreignObject></g></g></svg>

[^1]: Gpt-4 technical report. arXiv preprint arXiv:2303.08774. Cited by: §1.

[^2]: Longformer: the long-document transformer. arXiv preprint arXiv:2004.05150. Cited by: §1, §2.

[^3]: Longformer: the long-document transformer. arXiv preprint arXiv:2004.05150. Cited by: Appendix A.

[^4]: Language models are few-shot learners. Advances in neural information processing systems 33, pp. 1877–1901. Cited by: §1.

[^5]: Mem0: building production-ready ai agents with scalable long-term memory. arXiv preprint arXiv:2504.19413. Cited by: §1.

[^6]: Reciprocal rank fusion outperforms condorcet and individual rank learning methods. In Proceedings of the 32nd International ACM SIGIR Conference on Research and Development in Information Retrieval, SIGIR ’09, New York, NY, USA, pp. 758–759. External Links: ISBN 9781605584836, [Link](https://doi.org/10.1145/1571941.1572114), [Document](https://dx.doi.org/10.1145/1571941.1572114) Cited by: §3.3.

[^7]: From local to global: a graph rag approach to query-focused summarization. arXiv preprint arXiv:2404.16130. Cited by: §2.

[^8]: From local to global: a graph rag approach to query-focused summarization. arXiv preprint arXiv:2404.16130. Cited by: Appendix A.

[^9]: From rag to memory: non-parametric continual learning for large language models. arXiv preprint arXiv:2502.14802. Cited by: §2.

[^10]: Memory in the age of ai agents. arXiv preprint arXiv:2512.13564. Cited by: §6.

[^11]: Emotional rag: enhancing role-playing agents through emotional retrieval. In 2024 IEEE International Conference on Knowledge Graph (ICKG), pp. 120–127. Cited by: §2.

[^12]: Anatomy of agentic memory: taxonomy and empirical analysis of evaluation and system limitations. arXiv preprint arXiv:2602.19320. Cited by: §6.

[^13]: Rago: systematic performance optimization for retrieval-augmented generation serving. In Proceedings of the 52nd Annual International Symposium on Computer Architecture, pp. 974–989. Cited by: Appendix A, §2.

[^14]: Longrag: enhancing retrieval-augmented generation with long-context llms. arXiv preprint arXiv:2406.15319. Cited by: Appendix A, §2.

[^15]: Cladder: assessing causal reasoning in language models. Advances in Neural Information Processing Systems 36, pp. 31038–31065. Cited by: §2.

[^16]: Billion-scale similarity search with gpus. IEEE Transactions on Big Data 7 (3), pp. 535–547. Cited by: §3.2.

[^17]: Memory os of ai agent. arXiv preprint arXiv:2506.06326. Cited by: §1, 4th item.

[^18]: Memory os of ai agent. arXiv preprint arXiv:2506.06326. Cited by: Appendix A.

[^19]: Lm2: large memory models. arXiv preprint arXiv:2502.06049. Cited by: Appendix A, §2.

[^20]: Sharp nearby, fuzzy far away: how neural language models use context. arXiv preprint arXiv:1805.04623. Cited by: §1.

[^21]: Causal reasoning and large language models: opening a new frontier for causality. Transactions on Machine Learning Research. Cited by: Appendix A, §2.

[^22]: What learning systems do intelligent agents need? complementary learning systems theory updated. Trends in cognitive sciences 20 (7), pp. 512–534. Cited by: §3.4.

[^23]: Retrieval-augmented generation for knowledge-intensive nlp tasks. Advances in neural information processing systems 33, pp. 9459–9474. Cited by: Appendix A, §2.

[^24]: Hippocampus: an efficient and scalable memory module for agentic ai. arXiv preprint arXiv:2602.13594. Cited by: Appendix A.

[^25]: MemOS: a memory os for ai system. arXiv preprint arXiv:2507.03724. Cited by: Appendix A, §1.

[^26]: Cache mechanism for agent rag systems. arXiv preprint arXiv:2511.02919. Cited by: §2.

[^27]: Think-in-memory: recalling and post-thinking enable llms with long-term memory. arXiv preprint arXiv:2311.08719. Cited by: §2.

[^28]: Lost in the middle: how language models use long contexts. Transactions of the Association for Computational Linguistics 12, pp. 157–173. Cited by: §1.

[^29]: Evaluating very long-term conversational memory of llm agents. arXiv preprint arXiv:2402.17753. Cited by: Appendix A, §1, §4.1.

[^30]: Nemori: self-organizing agent memory inspired by cognitive science. arXiv preprint arXiv:2508.03341. Cited by: Appendix A, §1, 3rd item.

[^31]: MemGPT: towards llms as operating systems.. Cited by: Appendix A, §1.

[^32]: Unifying large language models and knowledge graphs: a roadmap. IEEE Transactions on Knowledge and Data Engineering 36 (7), pp. 3580–3599. Cited by: §6.

[^33]: Bleu: a method for automatic evaluation of machine translation. In Proceedings of the 40th Annual Meeting of the Association for Computational Linguistics, P. Isabelle, E. Charniak, and D. Lin (Eds.), Philadelphia, Pennsylvania, USA, pp. 311–318. External Links: [Link](https://aclanthology.org/P02-1040/), [Document](https://dx.doi.org/10.3115/1073083.1073135) Cited by: §4.1.

[^34]: Generative agents: interactive simulacra of human behavior. In Proceedings of the 36th annual acm symposium on user interface software and technology, pp. 1–22. Cited by: §2.

[^35]: Train short, test long: attention with linear biases enables input length extrapolation. arXiv preprint arXiv:2108.12409. Cited by: §1, §2.

[^36]: Train short, test long: attention with linear biases enables input length extrapolation. arXiv preprint arXiv:2108.12409. Cited by: Appendix A.

[^37]: Memorag: boosting long context processing with global memory-enhanced retrieval augmentation. In Proceedings of the ACM on Web Conference 2025, pp. 2366–2377. Cited by: Appendix A, §2.

[^38]: Zep: a temporal knowledge graph architecture for agent memory. arXiv preprint arXiv:2501.13956. Cited by: Appendix A, §1, §2.

[^39]: Revisiting relation extraction in the era of large language models. In Proceedings of the conference. association for computational linguistics. meeting, Vol. 2023, pp. 15566. Cited by: §6.

[^40]: Mirix: multi-agent memory system for llm-based agents. arXiv preprint arXiv:2507.07957. Cited by: §1.

[^41]: M-rag: reinforcing large language model performance through retrieval-augmented generation with multiple partitions. In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pp. 1966–1978. Cited by: Appendix A, §2.

[^42]: Chain-of-thought prompting elicits reasoning in large language models. Advances in neural information processing systems 35, pp. 24824–24837. Cited by: §1.

[^43]: Longmemeval: benchmarking chat assistants on long-term interactive memory. arXiv preprint arXiv:2410.10813. Cited by: Appendix A, §4.1.

[^44]: The rise and potential of large language model based agents: a survey. Science China Information Sciences 68 (2), pp. 121101. Cited by: §6.

[^45]: Self-correcting rag: enhancing faithfulness via mmkp context selection and nli-guided mcts. External Links: 2604.10734, [Link](https://arxiv.org/abs/2604.10734) Cited by: Appendix A.

[^46]: A-mem: agentic memory for llm agents. arXiv preprint arXiv:2502.12110. Cited by: Appendix A, §1, §2, 2nd item.

[^47]: Bridging the editing gap in llms: fineedit for precise and targeted text modifications. Findings of the Association for Computational Linguistics: EMNLP 2025, pp. 2193–2206. Cited by: Appendix A.

[^48]: Igniting language intelligence: the hitchhiker’s guide from chain-of-thought reasoning to language agents. ACM Computing Surveys 57 (8), pp. 1–39. Cited by: §2.

[^49]: Judging llm-as-a-judge with mt-bench and chatbot arena. Advances in neural information processing systems 36, pp. 46595–46623. Cited by: §4.1.

[^50]: Memorybank: enhancing large language models with long-term memory. In Proceedings of the AAAI Conference on Artificial Intelligence, Vol. 38, pp. 19724–19731. Cited by: Appendix A, §2.