---
type: paper
node_id: paper:bot2022_fast_krasnoselskiimann_algorithm
title: "Fast Krasnosel'skii-Mann algorithm with a convergence rate of the fixed point iteration of $o\\left(\\frac{1}{k}\\right)$"
authors: ["Radu Ioan Bot", "Dang-Khoa Nguyen"]
year: 2022
venue: "arXiv；正式版见roadmap书目"
external_ids:
  arxiv: "2206.09462"
  doi: null
  s2: null
tags: ["fixed-point", "stochastic", "core"]
added: 2026-10-14T13:52:41Z
---

# Fast Krasnosel'skii-Mann algorithm with a convergence rate of the fixed point iteration of $o\left(\frac{1}{k}\right)$

## One-line thesis
Fast KM 原始递推给 o(1/k) 残差与弱点极限。

## Problem / Gap
同一无限随机轨道的末次残差与点极限；以roadmap的精确问题类为准。

## Method
Fast KM 原始递推给 o(1/k) 残差与弱点极限。

## Key Results
Thms. 3.4–3.5；Remark 2.2。 原文位置：`memory/readings/sources/fast_km.txt`。

## Assumptions
Hilbert；theta-averaged，含 theta=1；alpha>2。

## Limitations / Failure Modes
无噪声结果；不能把随机化和确定性等价混同。

## Reusable Ingredients
按原文定理的误差权重、输出点和filtration组织证明。

## Open Questions
原始Fast KM/Fast OGDA的随机过程覆盖判定仍需逐式证明。

## Claims
这里只记录论文报告的结论；未进行逐行形式证明审核。

## Connections
自动由 graph/edges.jsonl 生成。
- paper:trandinh2024_variancereduced_fast_krasnoselkiimann —extends→ paper:bot2022_fast_krasnoselskiimann_algorithm：VR-FKM采用Fast KM结构并加入VR；不声称所有噪声过程等价。
- paper:yang2026_stochastic_inertial_krasnoselskiimann —supports→ paper:bot2022_fast_krasnoselskiimann_algorithm：Appendix A Proposition 1给确定性特殊参数下等价，不是随机主定理的自动覆盖。
- paper:bot2022_fast_krasnoselskiimann_algorithm —addresses_gap→ gap:raw_equivalence：提供覆盖判定所需原始递推；关系不代表判定已经完成。

## Relevance to This Project
核心邻近文献；参见主报告四组速率表与第5–7节。

## Abstract (original)

> The Krasnosel'skii-Mann (KM) algorithm is the most fundamental iterative scheme designed to find a fixed point of an averaged operator in the framework of a real Hilbert space, since it lies at the heart of various numerical algorithms for solving monotone inclusions and convex optimization problems. We enhance the Krasnosel'skii-Mann algorithm with Nesterov's momentum updates and show that the resulting numerical method exhibits a convergence rate for the fixed point residual of $o(1/k)$ while preserving the weak convergence of the iterates to a fixed point of the operator. Numerical experiments illustrate the superiority of the resulting so-called Fast KM algorithm over various fixed point iterative schemes, and also its oscillatory behavior, which is a specific of Nesterov's momentum optimization algorithms.

