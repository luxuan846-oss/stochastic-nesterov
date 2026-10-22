---
type: paper
node_id: paper:yoon2026_dualanchor_acceleration_nearoptimal
title: "Dual-Anchor Acceleration Is Near-Optimal for Stochastic Monotone Root-Finding"
authors: ["TaeHo Yoon", "Nicolas Loizou"]
year: 2026
venue: "arXiv；正式版见roadmap书目"
external_ids:
  arxiv: "2609.36033"
  doi: null
  s2: null
tags: ["fixed-point", "stochastic", "core"]
added: 2026-10-14T13:52:54Z
---

# Dual-Anchor Acceleration Is Near-Optimal for Stochastic Monotone Root-Finding

## One-line thesis
dual-anchor结合内层resolvent近似给近最优随机求零复杂度。

## Problem / Gap
同一无限随机轨道的末次残差与点极限；以roadmap的精确问题类为准。

## Method
dual-anchor结合内层resolvent近似给近最优随机求零复杂度。

## Key Results
Cor.3.6。 原文位置：`memory/readings/sources/dual_anchor.txt`。

## Assumptions
单调Lipschitz样本算子；无偏有界方差。

## Limitations / Failure Modes
有限精度复杂度，非原始Fast OGDA的无限轨道定理。

## Reusable Ingredients
按原文定理的误差权重、输出点和filtration组织证明。

## Open Questions
原始Fast KM/Fast OGDA的随机过程覆盖判定仍需逐式证明。

## Claims
这里只记录论文报告的结论；未进行逐行形式证明审核。

## Connections
自动由 graph/edges.jsonl 生成。
本轮没有添加显式关系。

## Relevance to This Project
核心邻近文献；参见主报告四组速率表与第5–7节。

## Abstract (original)

> Among distinct optimal acceleration mechanisms for deterministic monotone root-finding problems and fixed-point problems, dual-anchoring has recently been shown to admit a more robust direct stochastic extension than standard anchor acceleration. However, without additional strong monotonicity, the existing stochastic dual-anchoring guarantee has two limitations: first, it requires cocoercivity in expectation, and second, it attains only $O(ε^{-3})$ oracle complexity, leaving a gap to the near-optimal $\tilde{O}(ε^{-2})$ complexity achieved by other methods. In this work, we address both of these limitations by combining dual-anchoring with stochastic resolvent approximation and optimized variance control. For unbiased stochastic oracles with variance bounded by $σ^2$, where sample operators are monotone and uniformly $L$-Lipschitz, our algorithm finds a point with $ε$-residual with a near-optimal oracle complexity of $O ( (LD / ε) \ell + (σ^2 / ε^2) \ell^2)$, where $\ell = \log (1 + LD / ε)$ and $D$ is the initial distance to a solution. This result improves the best known oracle complexity in the noise-dominated regime under these samplewise assumptions, reducing the poly-logarithmic factor from cubic to quadratic.

