---
title: "Transformers are Graph Neural Networks"
source: "https://arxiv.org/html/2506.22084v1"
author:
published:
created: 2026-05-13
description:
tags:
  - "clippings"
---
Chaitanya K. Joshi  
Department of Computer Science and Technology  
University of Cambridge, UK  
[chaitanya.joshi@cl.cam.ac.uk](mailto:chaitanya.joshi@cl.cam.ac.uk)

###### Abstract

We establish connections between the Transformer architecture, originally introduced for natural language processing, and Graph Neural Networks (GNNs) for representation learning on graphs. We show how Transformers can be viewed as message passing GNNs operating on fully connected graphs of tokens, where the self-attention mechanism capture the relative importance of all tokens w.r.t. each-other, and positional encodings provide hints about sequential ordering or structure. Thus, Transformers are expressive set processing networks that *learn* relationships among input elements without being constrained by apriori graphs. Despite this mathematical connection to GNNs, Transformers are implemented via dense matrix operations that are significantly more efficient on modern hardware than sparse message passing. This leads to the perspective that Transformers are GNNs currently winning the hardware lottery.

## 1 Transformers for Natural Language Processing

Our discussion focuses on *representation learning*, which is the foundation for any machine learning task, be it predictive or generative modelling [^25].

At a high level, deep neural networks compress statistical and semantic information about data into a list of numbers, called a latent representation or embedding. Models are trained by optimizing a loss function that measures how well the model’s representations perform on a task of interest, such as predicting some properties of the input data. For example, if we give a model a dataset of sentences and train it to predict the next word in each sentence, it will learn to build representations of each word that capture its meaning and context in the sentence [^16].

When trained on diverse but interconnected data sources, models learn to build general-purpose representations that capture the underlying structure of the data. Good representations enable generalization to new tasks via knowledge transfer across related domains [^26] [^28]. For instance, training a model on mathematical tasks may also improve it for programming related tasks, as both domains require abstract problem-solving.

A key ingredient for building good representations is a highly expressive and scalable model architecture. This can be understood by studying at the transformation of architectures in the context of Natural Language Processing (NLP).

### From RNNs to Transformers

Recurrent Neural Networks (RNNs) were a class of widely used deep learning architectures for NLP [^18] [^32]. RNNs build representations of each word in a sentence in a sequential manner, i.e. one word at a time. Intuitively, we can imagine an RNN layer as a conveyor belt, with the words being processed on it autoregressively from left to right. At the end, we get a latent embedding for each word in the sentence, which we pass to the next RNN layer or use for our tasks of choice.

However, the sequential nature of RNNs means they struggle with long input contexts, as they compress the entire sentence into a single fixed-length representation at the end of the conveyor belt. This lead to the design of the *attention mechanism* [^3], which allows RNNs to focus on different parts of the input sentence when building representations at each step, rather than just the representation of the last word processed.

Transformer networks [^34], which are built on top of the attention mechanism, take this idea further by allowing the model to build representations of each word in parallel, rather than sequentially. This is done by computing the importance of each word in the sentence w.r.t. each other word, and then updating the representation of each word based on this importance. This allows the model to capture long-range dependencies and relationships between words, leading to more expressive representations.

Initially introduced for machine translation <sup>1</sup>, Transformers have replaced RNNs as the architecture of choice across NLP [^1] and wider deep learning applications [^11] [^27] due to their expressivity and scalability.

![Refer to caption](https://arxiv.org/html/2506.22084v1/x1.png)

Figure 1: Representation Learning for NLP. RNNs build representations one token at a time, which captures the sequential nature of language. Transformers build representations in parallel via attention mechanisms, which capture relative importance of words w.r.t. each-other.

### The attention mechanism

The central component of the Transformer is the attention mechanism, which allows the representations of words in sentences to capture their relative importance w.r.t. each-other; see [^36] for an intuitive introduction.

Formally, we are given a sentence $\mathcal{S}$ consisting of an ordered set of $n$ words (or tokens, more generally). For each token $i$, we initialize its representation $h_{i}^{\ell=0}\in\mathbb{R}^{d}$ as an initial token embedding [^24]. Token representations for each token $i$ are then updated via an attention mechanism from any arbitrary layer $\ell$ to layer $\ell+1$ as follows:

$$
\displaystyle h_{i}^{\ell+1}
$$
 
$$
\displaystyle=\text{Attention}\left(Q=W_{Q}^{\ell}\ h_{i}^{\ell},\ K=\{W_{K}^{%
\ell}\ h_{j}^{\ell},\ \forall j\in\mathcal{S}\},\ V=\{W_{V}^{\ell}\ h_{j}^{%
\ell},\ \forall j\in\mathcal{S}\}\right),
$$
$$
\displaystyle=\sum_{j\in\mathcal{S}}w_{ij}\cdot W_{V}^{\ell}\ h_{j}^{\ell}\ ,
$$

where $j\in\mathcal{S}$ denotes the set of all tokens in the sentence (including token $i$ itself), and $W_{Q}^{\ell},W_{K}^{\ell},W_{V}^{\ell}\in\mathbb{R}^{d\times d}$ are learnable linear transformations denoting the Query, Key and Value for the attention computation, respectively. The attention weights $w_{ij}\in\mathbb{R}$, which captures the relative importance between each pair of tokens $(i,j)$, are computed via a dot-product of the linearly transformed representations, followed by a softmax normalization across all tokens $j\in\mathcal{S}$:

$$
\displaystyle w_{ij}
$$
 
$$
\displaystyle=\text{softmax}_{j\in\mathcal{S}}\left(W_{Q}^{\ell}h_{i}^{\ell}\ %
\cdot\ W_{K}^{\ell}h_{j}^{\ell}\right),
$$
$$
\displaystyle=\frac{\text{exp}\left(W_{Q}^{\ell}h_{i}^{\ell}\ \cdot\ W_{K}^{%
\ell}h_{j}^{\ell}\right)}{\sum_{j^{\prime}\in\mathcal{S}}\text{exp}\left(W_{Q}%
^{\ell}h_{i}^{\ell}\ \cdot\ W_{K}^{\ell}h_{j^{\prime}}^{\ell}\right)}\ .
$$

Figure 2 illustrates the described attention mechanism, which is a slightly simplified version of the one used in Transformers. The attention computation in equation 1 is performed in parallel for each token in the sentence to obtain the updated representations in one shot. This is a key advantage of Transformers over RNNs, which update representations token-by-token.

![Refer to caption](https://arxiv.org/html/2506.22084v1/x2.png)

Figure 2: A simple attention mechanism. Taking as input the representations of the token h i ℓ superscript subscript ℎ 𝑖 h\_{i}^{\\ell} italic\_h start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT roman\_ℓ end\_POSTSUPERSCRIPT and the set of other tokens in the sentence { j ⁢ ∀ ∈ 𝒮 } 𝑗 for-all \\{h\_{j}^{\\ell}\\;\\ \\forall j\\in\\mathcal{S}\\} { italic\_h start\_POSTSUBSCRIPT italic\_j end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT roman\_ℓ end\_POSTSUPERSCRIPT ∀ italic\_j ∈ caligraphic\_S }, we compute the attention weights w 𝑤 w\_{ij} italic\_w start\_POSTSUBSCRIPT italic\_i italic\_j end\_POSTSUBSCRIPT denoting the relative importance for each pair (, ) (i,j) ( italic\_i, italic\_j ) through the dot-product followed by a softmax normalization. Finally, we produce the updated token representation + 1 h\_{i}^{\\ell+1} italic\_h start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT roman\_ℓ + 1 end\_POSTSUPERSCRIPT by summing over the representations of tokens \\{h\_{j}^{\\ell}\\} { italic\_h start\_POSTSUBSCRIPT italic\_j end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT roman\_ℓ end\_POSTSUPERSCRIPT } weighted by the corresponding. Each token in parallel undergoes the same pipeline to update its representation.

### Multi-head attention

In practice, using a single attention head can be limiting, as it forces the model to learn only one set of weights that capture relationships among tokens. However, tokens can interact in multiple ways, and we may want to simultaneously capture different aspects of their relationships, such as syntactic and semantic dependencies as well as contextual connections.

To improve the expressivity of the attention mechanism, Transformers introduced *multi-head attention*, which computes multiple attention weights in parallel. Each attention head learns its own set of query, key, and value transformations, allowing the model to attend to different types of relationships simultaneously and ‘hedge its bets’ on the most relevant representations for each token.

Formally, we can define $K$ attention heads, where each head $k$ computes its own set of query, key, and value transformations when updating the representation of token $i$ at layer $\ell$:

$$
\displaystyle Q^{k}=W_{Q}^{\ell,k}\ h_{i}^{\ell},\quad K^{k}=\{W_{K}^{\ell,k}%
\ h_{j}^{\ell},\ \forall j\in\mathcal{S}\},\quad V^{k,}=\{W_{V}^{\ell,k}\ h_{j%
}^{\ell},\ \forall j\in\mathcal{S}\},
$$

where $W_{Q}^{\ell,k},W_{K}^{\ell,k},W_{V}^{\ell,k}\in\mathbb{R}^{d\times\frac{d}{k}}$ are learnable linear transformations for the $k^{\text{th}}$ attention head at layer $\ell$. The output of each attention head is then computed as:

$$
\displaystyle\text{head}_{i}^{k}
$$
 
$$
\displaystyle=\sum_{j\in\mathcal{S}}w_{ij}^{k}\cdot W_{V}^{\ell,k}\ h_{j}^{%
\ell},
$$
$$
\displaystyle\text{and}\quad w_{ij}^{k}
$$
 
$$
\displaystyle=\text{softmax}_{j\in\mathcal{S}}\left(W_{Q}^{\ell,k}\ h_{i}^{%
\ell}\ \cdot\ W_{K}^{\ell,k}\ h_{j}^{\ell}\right),
$$

where $w_{ij}^{k}\in\mathbb{R}$ are the attention weights for the $k^{\text{th}}$ head, computed in the same way as before in equation 3, but using the query and key transformations specific to that head. The outputs of all attention heads are concatenated and projected to produce the updated representation for token $i$ as:

$$
\displaystyle\tilde{h}_{i}^{\ell}=\text{Concat}\left(\text{head}_{i}^{1},%
\ldots,\text{head}_{i}^{K}\right)O^{\ell},
$$

where $O^{\ell}\in\mathbb{R}^{d\times d}$ is a learnable linear transformation that projects the concatenated outputs to the original representation dimension $d$. In practice, the computation for all the heads is done in parallel via batched matrix multiplication.

After the multi-head attention operation, each token undergoes an independent token-wise operation. The updated representation $\tilde{h}_{i}^{\ell}$ for token $i$ is added to the original representation $h_{i}^{\ell}$ to form a residual connection [^17], followed by a layer normalization [^2], and further processing by a token-wise multi-layer perceptron (MLP):

$$
\displaystyle h_{i}^{\ell+1}
$$
 
$$
\displaystyle=\text{MLP}\left(\text{LayerNorm}\left(h_{i}^{\ell}+\tilde{h}_{i}%
^{\ell}\right)\right),
$$

where the MLP projects each token’s representation to a higher dimension (typically $4\times d$), applies a non-linear activation function, and then projects back to the original dimension $d$. It is worth remarking that this token-wise MLP contains significantly more learnable parameters than the attention mechanism.

All of these operations (MLP sub-networks, residual connections, layer normalization) are now standard components and best practices of deep learning architectures. They enable stacking multiple Transformer layers to build very deep networks, which has been key to the development of foundation models that learn complex relationships from large datasets [^6].

The final picture of a Transformer layer is illustrated in Figure 3.

![Refer to caption](https://arxiv.org/html/2506.22084v1/x3.png)

Figure 3: A Transformer layer. A multi-head attention sub-layer computes the relative importance of each token in a sentence w.r.t. each other token, and updates their representations accordingly. The updated representations are then processed by a token-wise multi-layer perceptron (MLP) sub-layer. Modern variants of the Transformer use SwiGLU 30 instead of ReLU 15 as the MLP’s activation function, and apply the LayerNorm operations before the multi-head attention and feed-forward sub-layers, rather than after 37.

## 2 Graph Neural Networks for Representation Learning on Graphs

Let us now turn our attention to sets with relational structure, i.e. graphs.

Graphs are used to model complex and interconnected systems in the real-world, ranging from knowledge graphs to social networks and molecular structures. Formally, an attributed graph $\mathcal{G}=({\bm{A}},{\bm{H}})$ is a set $\mathcal{V}$ of $n$ nodes connected by edges. ${\bm{A}}$ denotes an $n\times n$ adjacency matrix where each entry $a_{ij}\in\{0,1\}$ indicates the presence or absence of an edge connecting nodes $i$ and $j$. Additionally, we can define $\mathcal{N}_{i}$ as the set of neighbors of node $i$, which are the nodes connected to $i$ by an edge, i.e. $\mathcal{N}_{i}=\{j\in\mathcal{V}\mid a_{ij}=1\}$. The matrix of initial representations ${\bm{H}}\in\mathbb{R}^{n\times d}$ stores attributes ${\bm{h}}_{i}\in\mathbb{R}^{d}$ associated with each node $i$. For example, in molecular graphs, each node contains information about the atom type and edges can represent interactions among atoms.

Typically, the nodes in a graph have no canonical or fixed ordering and can be shuffled arbitrarily, resulting in an equivalent shuffling of the rows and columns of the adjacency matrix ${\bm{A}}$. Thus, accounting for permutation symmetry is a critical consideration when designing machine learning models for graphs [^7]. Formally, a permutation $\sigma$ of the nodes acts on the graph $\mathcal{G}$ by permuting the rows and columns of the adjacency matrix ${\bm{A}}$ and the representations ${\bm{H}}$:

$$
\displaystyle{\bm{P}}_{\sigma}{\mathcal{G}}
$$
 
$$
\displaystyle=({\bm{P}}_{\sigma}{\bm{A}}{\bm{P}}_{\sigma}^{\top},{\bm{P}}_{%
\sigma}{\bm{H}}),
$$

where ${\bm{P}}_{\sigma}$ is a permutation matrix corresponding to $\sigma$, and ${\bm{P}}_{\sigma}\in\mathbb{R}^{n\times n}$ has exactly one 1 in every row and column, and 0 elsewhere.

### Message Passing Graph Neural Networks

Graph Neural Networks (GNNs) are a class of deep learning architectures designed to operate on graph-structured data. GNNs leverage graph topology to propagate and aggregate information between connected nodes. They have emerged as the architecture of choice for representation learning on graph data across domains ranging from molecular modelling [^31] [^5] to recommendation systems [^39] and transportation networks [^8].

GNNs are based on the principle of *message passing*, where each node iteratively updates its representations by aggregating from its local neighbors [^4]. Formally, node representations ${\bm{h}}_{i}$ for each node $i\in\mathcal{V}$ are updated from layer $\ell$ to $\ell+1$ through a three-step process:

1. Message construction: For each node $i$ and its neighbors $j\in\mathcal{N}_{i}$, construct a message ${\bm{m}}_{ij}^{\ell}$ that captures the relationship between the representations of nodes $i$ and $j$.
	$$
	\displaystyle{\bm{m}}_{ij}^{\ell}
	$$
	 
	$$
	\displaystyle=\psi\left({\bm{h}}_{i}^{\ell},{\bm{h}}_{j}^{\ell}\right),\quad%
	\forall j\in\mathcal{N}_{i},
	$$
	where $\psi:\mathbb{R}^{2\times d}\to\mathbb{R}^{d}$ is an MLP that learns to construct the message based on the representations of nodes $i$ and $j$.
2. Aggregation: Combine all messages from the neighbors of node $i$ to produce a single aggregated message ${\bm{m}}_{i}^{\ell}$.
	$$
	\displaystyle{\bm{m}}_{i}^{\ell}
	$$
	 
	$$
	\displaystyle=\bigoplus_{j\in\mathcal{N}_{i}}{\bm{m}}_{ij}^{\ell},
	$$
	where $\bigoplus$ is a permutation-invariant operator (e.g. sum, mean, max) that aggregates messages from all neighbors $j\in\mathcal{N}_{i}$. Thus, a change in the order of neighbors does not affect the aggregated message, preserving the graph’s symmetry (equation 10).
3. Update: Update the representations of node $i$ using the aggregated message ${\bm{m}}_{i}^{\ell}$ and its previous representations ${\bm{h}}_{i}^{\ell}$.
	$$
	\displaystyle{\bm{h}}_{i}^{\ell+1}
	$$
	 
	$$
	\displaystyle=\phi\left({\bm{h}}_{i}^{\ell},{\bm{m}}_{i}^{\ell}\right),
	$$
	where $\phi:\mathbb{R}^{d}\to\mathbb{R}^{d}$ is another MLP.

This general formulation encompasses most commonly used GNN architectures including Graph Convolutional Networks [^23], Graph Isomorphism Networks [^38], and Message Passing Neural Networks [^14]. By stacking multiple message passing layers, GNNs can propagate information beyond immediate neighbors and capture complex multi-hop relationships in the graph structure (Figure 4).

![Refer to caption](https://arxiv.org/html/2506.22084v1/x4.png)

Figure 4: Representation learning on graphs with message passing. (left) Graphs model complex systems via a set of nodes connected by edges. (middle) GNNs build latent representations of graph data via message passing, where each node learns to aggregate representations from its local neighbourhood. (right) Stacking L 𝐿 italic\_L message passing layers enables GNNs to send and aggregate information from -hop subgraphs around each node.

### Graph Attention Networks

A particularly interesting class of GNNs uses attention mechanisms to weight the importance of different neighbors during aggregation [^35]. In Graph Attention Networks (GATs), the message from neighbor $j$ to node $i$ is computed as:

$$
\displaystyle\psi\left({\bm{h}}_{i}^{\ell},{\bm{h}}_{j}^{\ell}\right)
$$
 
$$
\displaystyle=\text{LocalAttention}\left(W^{\ell}_{Q}\ {\bm{h}}_{i}^{\ell}\ ,%
\ \{W^{\ell}_{K}\ {\bm{h}}_{j}^{\ell},\ \forall j\in\mathcal{N}_{i}\}\ ,\ \{W^%
{\ell}_{V}\ {\bm{h}}_{j}^{\ell},\ \forall j\in\mathcal{N}_{i}\}\right),
$$
$$
\displaystyle=\frac{\exp(W^{\ell}_{Q}\ {\bm{h}}_{i}^{\ell}\cdot W^{\ell}_{K}\ %
{\bm{h}}_{j}^{\ell})}{\sum_{j^{\prime}\in\mathcal{N}_{i}}\exp(W^{\ell}_{Q}\ {%
\bm{h}}_{i}^{\ell}\cdot W^{\ell}_{K}\ {\bm{h}}_{j^{\prime}}^{\ell})}\cdot W^{%
\ell}_{V}\ {\bm{h}}_{j}^{\ell}\ ,
$$

where $W^{\ell}_{Q},W^{\ell}_{K},W^{\ell}_{V}\in\mathbb{R}^{d\times d}$. The local attention mechanism allows allows GATs to learn which neighbors are more important for each node during the aggregation step. The updated representation for node $i$ is computed by aggregating the messages from all its neighbors:

$$
\displaystyle{\bm{h}}_{i}^{\ell+1}
$$
 
$$
\displaystyle={\bm{h}}_{i}^{\ell}\ +\ \sum_{j\in\mathcal{N}_{i}}\psi\left({\bm%
{h}}_{i}^{\ell},{\bm{h}}_{j}^{\ell}\right),
$$

In practice, GATs also use multi-head attention to compute multiple sets of attention weights in parallel, allowing the model to learn different aspects of the relationships between nodes.

These equations should look very familiar!

In fact, they are almost identical to the Transformer’s attention mechanism for computing the relative importance of words in a sentence.

## 3 Transformers are GNNs over Fully Connected Graphs

At this point, let us establish a formal equivalence between multi-head attention in Transformers and message passing in Graph Attention Networks (GATs).

Transformers can be viewed as GNNs operating on complete graphs, where self-attention models relationships between all input tokens in a sentence $\mathcal{S}$. The multi-head attention in equation 8 can be directly instantiated in the message passing framework as follows (for each head):

$$
\displaystyle\psi\left({\bm{h}}_{i}^{\ell},{\bm{h}}_{j}^{\ell}\right)
$$
 
$$
\displaystyle=\text{GlobalAttention}\left(W^{\ell}_{Q}\ {\bm{h}}_{i}^{\ell}\ ,%
\ \{W^{\ell}_{K}\ {\bm{h}}_{j}^{\ell},\ \forall j\in\mathcal{S}\}\ ,\ \{W^{%
\ell}_{V}\ {\bm{h}}_{j}^{\ell},\ \forall j\in\mathcal{S}\}\right),
$$
$$
\displaystyle=\frac{\exp(W^{\ell}_{Q}\ {\bm{h}}_{i}^{\ell}\cdot W^{\ell}_{K}\ %
{\bm{h}}_{j}^{\ell})}{\sum_{j^{\prime}\in\mathcal{S}}\exp(W^{\ell}_{Q}\ {\bm{h%
}}_{i}^{\ell}\cdot W^{\ell}_{K}\ {\bm{h}}_{j^{\prime}}^{\ell})}\cdot W^{\ell}_%
{V}\ {\bm{h}}_{j}^{\ell}\ .
$$

Here, $\psi\left({\bm{h}}_{i}^{\ell},{\bm{h}}_{j}^{\ell}\right)$ computes the message from token $j$ to token $i$, with the relative importance of each token computed via attention. Next, the weighted messages from all tokens in the sentence are aggregated via a summation, and the representation of token $i$ is updated as in equation 9 using a token-wise feedforward network $\phi$:

$$
\displaystyle{\bm{h}}_{i}^{\ell+1}\
$$
 
$$
\displaystyle=\ \phi\left({\bm{h}}_{i}^{\ell}\ ,\ {\bm{m}}_{i}^{\ell}\right)\ %
=\text{MLP}\left(\text{LayerNorm}\left(h_{i}^{\ell}+\sum_{j\in\mathcal{S}}\psi%
\left({\bm{h}}_{i}^{\ell},{\bm{h}}_{j}^{\ell}\right)\right)\right)\ .
$$

We have arrived at exactly the same set of update equations as in Section 1.

Thus, Transformers are highly expressive set processing networks. They can learn to capture both local and global context in the data via multi-head attention, without being constrained by the pathologies of pre-defined sparse graph structure as in GNNs [^9]. This is especially useful for tasks where we do not have an apriori graph structure, such as in modelling molecular structures. For instance, proteins fold into stable 3D structures through interactions between distant residues, so capturing global relationships is important for ensuring physical validity when predicting protein structures [^22].

Conversely, GATs can be viewed as Transformers with attention restricted to local neighbourhoods, where the graph structure is used to implement sparse or masked attention [^10].

This connection has inspired a new development in graph representation learning. Transformers use positional encodings as an initial feature to add information about the sequential ordering of tokens in a sentence, without strictly enforcing a sequential structure. This idea can be extended to graphs, where positional encodings can be used to softly inject information about the graph structure into Transformer blocks [^12]. This has led to a new class of *Graph Transformers* [^29] that aim to combine both local message passing and global multi-head attention. These architectures overcome the expressivity limitations of message passing GNNs while preserving the inductive bias of graph structure.

## 4 Transformers are GNNs Winning the Hardware Lottery

We will conclude with a discussion on the *hardware lottery* [^19], the marriage of architectures and hardware that determines which research ideas rise to prominence, and its connection to the *bitter lesson* in AI research [^33].

While we have established that Transformers are GNNs operating over fully connected graphs, there is an important practical difference between the two classes of architectures.

Transformers implement global multi-head attention through highly optimized *dense* matrix multiplication operations that leverage the parallel processing capabilities of modern GPUs and TPUs. Given a matrix of initial representations ${\bm{H}}\in\mathbb{R}^{n\times d}$, the self-attention mechanism for all tokens in the sentence $\mathcal{S}$ can be computed in a parallel manner as follows:

$$
\displaystyle\tilde{\bm{H}}^{\ell}
$$
 
$$
\displaystyle=\text{softmax}\left({\bm{H}}^{\ell}\ W_{Q}^{\ell}\ \left({\bm{H}%
}^{\ell}\ W_{K}^{\ell}\right)^{\top}\right)\ \left({\bm{H}}^{\ell}\ W_{V}^{%
\ell}\right),
$$

The multi-head attention mechanism can also be similarly parallelized by performing a single linear transformation for all heads in parallel, followed by reshaping the queries, keys, and values per head to tensors of dimension $n\times k\times d/k$ each. The token-wise operations which follow multi-head attention are independent of other tokens and trivially parallelizable as well.

In contrast, GNNs typically perform *sparse* message passing over locally connected structures, which is substantially less efficient on current GPUs for typical problem scales (with the exception of very sparse or billion-scale graphs). This involves maintaining an index of neighbours for each node, and performing gather and scatter operations to propogate messages [^13]. As a result, GNNs are orders of magnitude slower to train and challenging to scale compared to standard Transformers on current hardware.

Additionally, with an increasing emphasis on scaling up models and datasets, there is empirical evidence that Transformers can learn the inductive biases baked in to GNNs, such as locality, when trained at sufficient scale. This is particularly effective when models are given appropriate positional encodings as ‘hints’ about the underlying structure of their input data, without imposing them as hard constraints in the architecture [^20]. The expressivity and flexibility of Transformers makes them the go-to architecture for representation learning on structured data across diverse application domains, including graphs.

Thus, Transformers are Graph Neural Networks that are currently winning the hardware lottery.

### Acknowledgements

I am grateful to numerous colleagues for feedback on this article over the years, which has helped shape my understanding of Transformers and GNNs. I would also like to thank [The Gradient](https://thegradient.pub/) for providing a platform to share an initial version of this work.

[^1]: J. Achiam, S. Adler, S. Agarwal, L. Ahmad, I. Akkaya, F. L. Aleman, D. Almeida, J. Altenschmidt, et al. Gpt-4 technical report. *arXiv preprint arXiv:2303.08774*, 2023.

[^2]: J. L. Ba, J. R. Kiros, and G. E. Hinton. Layer normalization. *arXiv preprint arXiv:1607.06450*, 2016.

[^3]: D. Bahdanau, K. Cho, and Y. Bengio. Neural machine translation by jointly learning to align and translate. In *ICLR*, 2015.

[^4]: P. W. Battaglia, J. B. Hamrick, V. Bapst, A. Sanchez-Gonzalez, V. Zambaldi, et al. Relational inductive biases, deep learning, and graph networks. *arXiv preprint*, 2018.

[^5]: S. Batzner, A. Musaelian, L. Sun, M. Geiger, J. P. Mailoa, M. Kornbluth, N. Molinari, T. E. Smidt, and B. Kozinsky. E (3)-equivariant graph neural networks for data-efficient and accurate interatomic potentials. *Nature communications*, 2022.

[^6]: R. Bommasani, D. A. Hudson, E. Adeli, R. Altman, S. Arora, S. von Arx, M. S. Bernstein, J. Bohg, A. Bosselut, E. Brunskill, E. Brynjolfsson, et al. On the opportunities and risks of foundation models. *ArXiv*, 2021.

[^7]: M. M. Bronstein, J. Bruna, T. Cohen, and P. Veličković. Geometric deep learning: Grids, groups, graphs, geodesics, and gauges. *arXiv preprint*, 2021.

[^8]: A. Derrow-Pinion, J. She, D. Wong, O. Lange, T. Hester, L. Perez, M. Nunkesser, S. Lee, X. Guo, B. Wiltshire, et al. Eta prediction with graph neural networks in google maps. In *Proceedings of the 30th ACM international conference on information & knowledge management*, 2021.

[^9]: F. Di Giovanni, L. Giusti, F. Barbero, G. Luise, P. Lio, and M. M. Bronstein. On over-squashing in message passing neural networks: The impact of width, depth, and topology. In *International Conference on Machine Learning*. PMLR, 2023.

[^10]: J. Dong, B. Feng, D. Guessous, Y. Liang, and H. He. Flex attention: A programming model for generating optimized attention kernels. *arXiv preprint arXiv:2412.05496*, 2024.

[^11]: A. Dosovitskiy, L. Beyer, A. Kolesnikov, D. Weissenborn, X. Zhai, T. Unterthiner, M. Dehghani, M. Minderer, G. Heigold, S. Gelly, et al. An image is worth 16x16 words: Transformers for image recognition at scale. In *International Conference on Learning Representations, ICLR*, 2021.

[^12]: V. P. Dwivedi and X. Bresson. A generalization of transformer networks to graphs. *arXiv preprint arXiv:2012.09699*, 2020.

[^13]: M. Fey and J. E. Lenssen. Fast graph representation learning with PyTorch Geometric. In *ICLR Workshop on Representation Learning on Graphs and Manifolds*, 2019.

[^14]: J. Gilmer, S. S. Schoenholz, P. F. Riley, O. Vinyals, and G. E. Dahl. Neural message passing for quantum chemistry. In *ICML*, 2017.

[^15]: X. Glorot, A. Bordes, and Y. Bengio. Deep sparse rectifier neural networks. In *Proceedings of the fourteenth international conference on artificial intelligence and statistics*, 2011.

[^16]: A. Graves. Generating sequences with recurrent neural networks. *arXiv preprint arXiv:1308.0850*, 2013.

[^17]: K. He, X. Zhang, S. Ren, and J. Sun. Deep residual learning for image recognition. In *Proceedings of the IEEE conference on computer vision and pattern recognition*, pages 770–778, 2016.

[^18]: S. Hochreiter and J. Schmidhuber. Long short-term memory. *Neural computation*, 1997.

[^19]: S. Hooker. The hardware lottery. *Communications of the ACM*, 2021.

[^20]: A. Jaegle, S. Borgeaud, J.-B. Alayrac, C. Doersch, C. Ionescu, D. Ding, S. Koppula, D. Zoran, A. Brock, E. Shelhamer, et al. Perceiver io: A general architecture for structured inputs & outputs. *arXiv preprint arXiv:2107.14795*, 2021.

[^21]: C. Joshi. Transformers are graph neural networks. *The Gradient*, 2020. URL [https://thegradient.pub/transformers-are-gaph-neural-networks/](https://thegradient.pub/transformers-are-gaph-neural-networks/).

[^22]: J. Jumper, R. Evans, A. Pritzel, T. Green, M. Figurnov, O. Ronneberger, et al. Highly accurate protein structure prediction with alphafold. *Nature*, 2021.

[^23]: T. N. Kipf and M. Welling. Semi-supervised classification with graph convolutional networks. In *ICLR*, 2017.

[^24]: T. Mikolov, I. Sutskever, K. Chen, G. S. Corrado, and J. Dean. Distributed representations of words and phrases and their compositionality. *Advances in neural information processing systems*, 2013.

[^25]: C. Olah. Deep learning, NLP, and representations. *Christopher Olah’s Blog*, 2014. URL [https://colah.github.io/posts/2014-07-NLP-RNNs-Representations/](https://colah.github.io/posts/2014-07-NLP-RNNs-Representations/).

[^26]: A. Radford, J. Wu, R. Child, D. Luan, D. Amodei, and I. Sutskever. Language models are unsupervised multitask learners. *OpenAI*, 2019.

[^27]: A. Radford, J. W. Kim, T. Xu, G. Brockman, C. Mcleavey, and I. Sutskever. Robust speech recognition via large-scale weak supervision. In *International Conference on Machine Learning*, 2023.

[^28]: C. Raffel, N. Shazeer, A. Roberts, K. Lee, S. Narang, M. Matena, Y. Zhou, W. Li, and P. J. Liu. Exploring the limits of transfer learning with a unified text-to-text transformer. *Journal of machine learning research*, 2020.

[^29]: L. Rampášek, M. Galkin, V. P. Dwivedi, A. T. Luu, G. Wolf, and D. Beaini. Recipe for a general, powerful, scalable graph transformer. *Advances in Neural Information Processing Systems*, 2022.

[^30]: N. Shazeer. Glu variants improve transformer. *arXiv preprint arXiv:2002.05202*, 2020.

[^31]: J. M. Stokes, K. Yang, K. Swanson, W. Jin, A. Cubillos-Ruiz, N. M. Donghia, C. R. MacNair, S. French, L. A. Carfrae, Z. Bloom-Ackermann, et al. A deep learning approach to antibiotic discovery. *Cell*, 2020.

[^32]: I. Sutskever, O. Vinyals, and Q. V. Le. Sequence to sequence learning with neural networks. In *Advances in neural information processing systems*, 2014.

[^33]: R. Sutton. The bitter lesson. *Incomplete Ideas (blog)*, 2019.

[^34]: A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, L. Kaiser, and I. Polosukhin. Attention is all you need. In *Advances in neural information processing systems*, 2017.

[^35]: P. Veličković, G. Cucurull, A. Casanova, A. Romero, P. Liò, and Y. Bengio. Graph Attention Networks. *ICLR*, 2018.

[^36]: L. Weng. Attention? attention! *Lil’Log*, 2018. URL [http://lilianweng.github.io/lil-log/2018/06/24/attention-attention.html](http://lilianweng.github.io/lil-log/2018/06/24/attention-attention.html).

[^37]: R. Xiong, Y. Yang, D. He, K. Zheng, S. Zheng, C. Xing, H. Zhang, Y. Lan, L. Wang, and T. Liu. On layer normalization in the transformer architecture. In *International conference on machine learning*, 2020.

[^38]: K. Xu, W. Hu, J. Leskovec, and S. Jegelka. How powerful are graph neural networks? In *ICLR*, 2019.

[^39]: R. Ying, R. He, K. Chen, P. Eksombatchai, W. L. Hamilton, and J. Leskovec. Graph convolutional neural networks for web-scale recommender systems. In *Proceedings of the 24th ACM SIGKDD international conference on knowledge discovery & data mining*, 2018.