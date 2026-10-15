---
type: paper
node_id: paper:salzo2025_iterates_fista_converge
title: "The iterates of FISTA converge even under inexact computations and stochastic gradients"
authors: ["Saverio Salzo"]
year: 2025
venue: "arXiv；正式版见roadmap书目"
external_ids:
  arxiv: "2511.12665"
  doi: null
  s2: null
tags: ["fixed-point", "stochastic", "core"]
added: 2026-10-14T13:52:52Z
---

# The iterates of FISTA converge even under inexact computations and stochastic gradients

## One-line thesis
随机FISTA在衰减梯度步长下有a.s.弱点极限。

## Problem / Gap
同一无限随机轨道的末次残差与点极限；以roadmap的精确问题类为准。

## Method
随机FISTA在衰减梯度步长下有a.s.弱点极限。

## Key Results
v3 Thm.3.10、Remark3.11。 原文位置：`roadmap_20261014/sources/salzo.txt`。

## Assumptions
Hilbert；有界条件方差；gamma_k约k^-1.5 log^-r，r>0.5。

## Limitations / Failure Modes
对应O(log^r/sqrt(k))目标差是期望界，不是a.s.o(k^-2)。

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

> Very recently, the papers "Point Convergence of Nesterov's Accelerated Gradient Method: An AI-Assisted Proof" by Jang and Ryu, and "The Iterates of Nesterov's Accelerated Algorithm Converge in the Critical Regimes" by Bot, Fadili, and Nguyen have simultaneously resolved a long-standing open problem concerning Nesterov's accelerated gradient method. These works show that the iterates of the algorithm (known in its composite form as FISTA) indeed converge to an optimal solution. In this work, we extend these results and prove that, in infinite dimensional Hilbert spaces, the iterates of such an algorithm still converge (in the weak sense) even when the proximity operator and the gradient are computed inexactly, with the latter possibly stochastic.

