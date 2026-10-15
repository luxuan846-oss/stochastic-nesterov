---
type: paper
node_id: paper:cortild2026_stochastic_krasnoselskiimann_iterations
title: "Stochastic Krasnoselskii-Mann Iterations: Convergence without Uniformly Bounded Variance"
authors: ["Daniel Cortild", "Coralia Cartis", "Juan Peypouquet"]
year: 2026
venue: "arXiv；正式版见roadmap书目"
external_ids:
  arxiv: "2604.22581"
  doi: null
  s2: null
tags: ["fixed-point", "stochastic", "core"]
added: 2026-10-14T13:52:49Z
---

# Stochastic Krasnoselskii-Mann Iterations: Convergence without Uniformly Bounded Variance

## One-line thesis
随机KM在解处有限方差及样本映射结构下有弱点极限。

## Problem / Gap
同一无限随机轨道的末次残差与点极限；以roadmap的精确问题类为准。

## Method
随机KM在解处有限方差及样本映射结构下有弱点极限。

## Key Results
Thm. 2.13；Cor. 2.12 区分末次与running minimum。 原文位置：`memory/readings/sources/cortild.txt`。

## Assumptions
可分Hilbert；非扩张样本映射；RM步长。

## Limitations / Failure Modes
不能忽略样本映射条件；running minimum率不是末次率。

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

> We investigate the Stochastic Krasnoselskii-Mann iterations for expected nonexpansive fixed-point problems in a real separable Hilbert space. We establish convergence guarantees under significantly weaker assumptions on the variance than those typically used in the literature. In particular, instead of a uniform bound on the variance of the stochastic oracle, we only assume finite variance at a single fixed point. Under this assumption, we prove almost sure weak convergence of the iterates, derive convergence rates for the expected residual and the last-iterate residual, and obtain almost sure convergence rates for the running minimum residual. Notably, we recover the best-known stochastic oracle complexity without imposing uniformly bounded variance. We illustrate the applicability of our results to Stochastic Gradient Descent, where we recover known guarantees, to Stochastic Three-Operator Splitting and Stochastic Backward-Forward Splitting, for which we obtain the first results that avoid uniform variance bounds, and to a novel Stochastic Lifted Three-Operator Splitting.

