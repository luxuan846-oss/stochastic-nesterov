---
type: paper
node_id: paper:attouch2024_stochastic_ravine_accelerated
title: "The stochastic Ravine accelerated gradient method with general extrapolation coefficients"
authors: ["Hedy Attouch", "Jalal Fadili", "Vyacheslav Kungurtsev"]
year: 2024
venue: "arXiv；正式版见roadmap书目"
external_ids:
  arxiv: "2403.04860"
  doi: null
  s2: null
tags: ["fixed-point", "stochastic", "core"]
added: 2026-10-14T13:52:53Z
---

# The stochastic Ravine accelerated gradient method with general extrapolation coefficients

## One-line thesis
随机Ravine区分目标差快率与点极限所需的噪声权重。

## Problem / Gap
同一无限随机轨道的末次残差与点极限；以roadmap的精确问题类为准。

## Method
随机Ravine区分目标差快率与点极限所需的噪声权重。

## Key Results
JOTA2026 Thm.3.1、Cor.4.1。 原文位置：`roadmap_20261014/sources/ravine.txt`。

## Assumptions
条件无偏；目标值用加权平方可和；点极限需更强加权一阶可和。

## Limitations / Failure Modes
不能把目标值条件直接用作点极限条件。

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

> In a real Hilbert space domain setting, we study the convergence properties of the stochastic Ravine accelerated gradient method for convex differentiable optimization. We consider the general form of this algorithm where the extrapolation coefficients can vary with each iteration, and where the evaluation of the gradient is subject to random errors. This general treatment models a breadth of practical algorithms and numerical implementations. We show that, under a proper tuning of the extrapolation parameters, and when the error variance associated with the gradient evaluations or the step-size sequences vanish sufficiently fast, the Ravine method provides fast convergence of the values both in expectation and almost surely. We also improve the convergence rates from O(.) to o(.). Moreover, we show almost sure summability property of the gradients, which implies the fast convergence of the gradients towards zero. This property reflects the fact that the high-resolution ODE of the Ravine method includes a Hessian-driven damping term. When the space is also separable, our analysis allows also to establish almost sure weak convergence of the sequence of iterates provided by the algorithm. We finally specialize the analysis to consider different parameter choices, including vanishing and constant (heavy ball method with friction) damping parameter, and present a comprehensive landscape of the tradeoffs in speed and accuracy associated with these parameter choices and statistical properties on the sequence of errors in the gradient computations. We provide a thorough discussion of the similarities and differences with the Nesterov accelerated gradient which satisfies similar asymptotic convergence rates.

