---
type: paper
node_id: paper:trandinh2024_variancereduced_fast_krasnoselkiimann
title: "Variance-Reduced Fast Krasnoselkii-Mann Methods for Finite-Sum Root-Finding Problems"
authors: ["Quoc Tran-Dinh"]
year: 2024
venue: "arXiv；正式版见roadmap书目"
external_ids:
  arxiv: "2406.02413"
  doi: null
  s2: null
tags: ["fixed-point", "stochastic", "core"]
added: 2026-10-14T13:52:43Z
---

# Variance-Reduced Fast Krasnoselkii-Mann Methods for Finite-Sum Root-Finding Problems

## One-line thesis
VR-FKM v4 已有 a.s. o(1/k) 残差和点极限。

## Problem / Gap
同一无限随机轨道的末次残差与点极限；以roadmap的精确问题类为准。

## Method
VR-FKM v4 已有 a.s. o(1/k) 残差和点极限。

## Key Results
Thm. 2；Cors. 1–2：O(n+n^(2/3)/epsilon)。 原文位置：`memory/readings/sources/vr_fast_km.txt`。

## Assumptions
有限维有限和；平均分量余强制型条件；SVRG/SAGA。

## Limitations / Failure Modes
不能只保留均值算子余强制；MOR模板不等于正式发表。

## Reusable Ingredients
按原文定理的误差权重、输出点和filtration组织证明。

## Open Questions
原始Fast KM/Fast OGDA的随机过程覆盖判定仍需逐式证明。

## Claims
这里只记录论文报告的结论；未进行逐行形式证明审核。

## Connections
自动由 graph/edges.jsonl 生成。
- paper:trandinh2024_variancereduced_fast_krasnoselkiimann —extends→ paper:bot2022_fast_krasnoselskiimann_algorithm：VR-FKM采用Fast KM结构并加入VR；不声称所有噪声过程等价。
- paper:nguyentrung2025_class_accelerated_fixedpointbased —extends→ paper:trandinh2024_variancereduced_fast_krasnoselkiimann：AFP一般递推误差模型覆盖有限和之外的随机oracle。
- paper:trandinh2024_variancereduced_fast_krasnoselkiimann —invalidates→ idea:001：原文已明示a.s.残差小o与点极限，否定宽泛首次性。

## Relevance to This Project
核心邻近文献；参见主报告四组速率表与第5–7节。

## Abstract (original)

> We propose a new class of fast Krasnoselkii--Mann methods with variance reduction to solve a finite-sum co-coercive equation $Gx = 0$. Our algorithm is single-loop and leverages a new family of unbiased variance-reduced estimators specifically designed for a wider class of root-finding algorithms. Our method achieves both $\mathcal{O}(1/k^2)$ and $o(1/k^2)$ last-iterate convergence rates in terms of $\mathbb{E}[\| Gx^k\|^2]$, where $k$ is the iteration counter and $\mathbb{E}[\cdot]$ is the total expectation. We also establish almost sure $o(1/k^2)$ convergence rates and the almost sure convergence of iterates $\{x^k\}$ to a solution of $Gx=0$. We instantiate our framework for two prominent estimators: SVRG and SAGA. By an appropriate choice of parameters, both variants attain an oracle complexity of $\mathcal{O}(n + n^{2/3}ε^{-1})$ to reach an $ε$-solution, where $n$ represents the number of summands in the finite-sum operator $G$. Furthermore, under $σ$-strong quasi-monotonicity, our method achieves a linear convergence rate and an oracle complexity of $\mathcal{O}(n+ \max\{n, n^{2/3}κ\} \log(\frac{1}ε))$, where $κ:= L/σ$. We extend our approach to solve a class of finite-sum inclusions (possibly nonmonotone), demonstrating that our schemes retain the same theoretical guarantees as in the equation setting. Finally, numerical experiments validate our algorithms and demonstrate their promising performance compared to state-of-the-art methods.

