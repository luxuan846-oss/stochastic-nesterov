---
type: paper
node_id: paper:yang2026_stochastic_inertial_krasnoselskiimann
title: "Stochastic Inertial Krasnosel'skii-Mann Iteration Achieves Near-Optimal Sample Complexity"
authors: ["Tong Yang", "Tao Jiang", "Yuejie Chi", "Ashok Cutkosky", "Lin Xiao"]
year: 2026
venue: "arXiv；正式版见roadmap书目"
external_ids:
  arxiv: "2609.28543"
  doi: null
  s2: null
tags: ["fixed-point", "stochastic", "core"]
added: 2026-10-14T13:52:49Z
---

# Stochastic Inertial Krasnosel'skii-Mann Iteration Achieves Near-Optimal Sample Complexity

## One-line thesis
stochastic iKM 给预设时域的近最优 RMS 残差。

## Problem / Gap
同一无限随机轨道的末次残差与点极限；以roadmap的精确问题类为准。

## Method
stochastic iKM 给预设时域的近最优 RMS 残差。

## Key Results
Thm. 1；Appendix A Proposition 1。 原文位置：`roadmap_20261014/sources/ikm_zotero.txt`。

## Assumptions
实Hilbert；N2；时域依赖参数；每步一次新oracle。

## Limitations / Failure Modes
确定性Fast KM等价参数与随机主定理schedule不同；无直接无限轨道a.s.结论。

## Reusable Ingredients
按原文定理的误差权重、输出点和filtration组织证明。

## Open Questions
原始Fast KM/Fast OGDA的随机过程覆盖判定仍需逐式证明。

## Claims
这里只记录论文报告的结论；未进行逐行形式证明审核。

## Connections
自动由 graph/edges.jsonl 生成。
- paper:yang2026_stochastic_inertial_krasnoselskiimann —supports→ paper:bot2022_fast_krasnoselskiimann_algorithm：Appendix A Proposition 1给确定性特殊参数下等价，不是随机主定理的自动覆盖。

## Relevance to This Project
核心邻近文献；参见主报告四组速率表与第5–7节。

## Abstract (original)

> We analyze a simple stochastic inertial Krasnosel'skii--Mann (iKM) method for finding a fixed point of a nonexpansive operator in a real Hilbert space. Our method is obtained simply by adding two inertial extrapolations to stochastic KM [Bravo and Cominetti, 2024], and it retains one call to a possibly biased stochastic oracle per update and achieves sharp rates in both the stochastic and deterministic regimes. Specifically, with our proposed parameter schedule, we prove the following last-iterate fixed-point residual bound: \[ {O}\!\left(\frac{1}{K} +\frac{σ\log K}{\sqrt K} +\frac{B_K\log K}{K}\right), \] where $K$ is the horizon, $σ$ is the noise level and $B_K$ is the accumulated root-mean-square bias. When $B_K=O(\sqrt K)$, this yields $\widetilde O(ε^{-2})$ sample complexity that matches, up to a logarithmic factor, the stochastic-oracle lower bound given under the unbiased subclass of our model [Foster et al., 2019, Theorem 2]. It also improves the best-known $O(ε^{-4})$ random-iterate guarantee for stochastic KM [Bravo and Cominetti, 2024, Corollary 5.4]. To our knowledge, this is the first single-loop method for general nonexpansive fixed-point problems to attain this near-optimal sample complexity without variance reduction or batching. When the oracle is exact, the same method attains the worst-case-optimal $O(K^{-1})$ last-iterate residual rate [Park and Ryu, 2022, Theorem 4.6], improving the $O(K^{-1/2})$ rate of classical KM [Cominetti et al., 2014; Bravo and Cominetti, 2018].

