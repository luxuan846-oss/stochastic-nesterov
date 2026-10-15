---
type: paper
node_id: paper:hermant2024_gradient_correlation_key
title: "Gradient correlation is a key ingredient to accelerate SGD with momentum"
authors: ["Julien Hermant", "Marien Renaud", "Jean-François Aujol", "Charles Dossal", "Aude Rondepierre"]
year: 2024
venue: "arXiv；正式版见roadmap书目"
external_ids:
  arxiv: "2410.07870"
  doi: null
  s2: null
tags: ["fixed-point", "stochastic", "core"]
added: 2026-10-14T13:52:51Z
---

# Gradient correlation is a key ingredient to accelerate SGD with momentum

## One-line thesis
SGC可使SNAG保留加速目标差的a.s.小o速率。

## Problem / Gap
同一无限随机轨道的末次残差与点极限；以roadmap的精确问题类为准。

## Method
SGC可使SNAG保留加速目标差的a.s.小o速率。

## Key Results
ICLR2025正式版Thms. 3–4。 原文位置：`roadmap_20261014/sources/hermant.txt`。

## Assumptions
光滑凸有限和；SGC；双步长参数。

## Limitations / Failure Modes
不是持续加性方差界；目标差不能直接代替一般算子残差。

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

> Empirically, it has been observed that adding momentum to Stochastic Gradient Descent (SGD) accelerates the convergence of the algorithm. However, the literature has been rather pessimistic, even in the case of convex functions, about the possibility of theoretically proving this observation. We investigate the possibility of obtaining accelerated convergence of the Stochastic Nesterov Accelerated Gradient (SNAG), a momentum-based version of SGD, when minimizing a sum of functions in a convex setting. We demonstrate that the average correlation between gradients allows to verify the strong growth condition, which is the key ingredient to obtain acceleration with SNAG. Numerical experiments, both in linear regression and deep neural network optimization, confirm in practice our theoretical results.

