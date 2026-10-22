---
type: paper
node_id: paper:bravo2024_stochastic_halpern_iteration
title: "Stochastic Halpern iteration in normed spaces and applications to reinforcement learning"
authors: ["Mario Bravo", "Juan Pablo Contreras"]
year: 2024
venue: "arXiv；正式版见roadmap书目"
external_ids:
  arxiv: "2403.12338"
  doi: null
  s2: null
tags: ["fixed-point", "stochastic", "core"]
added: 2026-10-14T13:52:50Z
---

# Stochastic Halpern iteration in normed spaces and applications to reinforcement learning

## One-line thesis
随机Halpern在一般范数中有期望误差界及轨道极限。

## Problem / Gap
同一无限随机轨道的末次残差与点极限；以roadmap的精确问题类为准。

## Method
随机Halpern在一般范数中有期望误差界及轨道极限。

## Key Results
Thm. 3.3、Cor. 3.5、Thm. 3.7、Thm. 3.10。 原文位置：`memory/readings/sources/bravo_contreras.txt`。

## Assumptions
有限维一般范数；点极限需要光滑范数及误差可和。

## Limitations / Failure Modes
epsilon^-3下界使用特定范数及算法访问模型，不否定Hilbert epsilon^-2。

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

> We analyze the oracle complexity of the stochastic Halpern iteration with minibatch, where we aim to approximate fixed-points of nonexpansive and contractive operators in a normed finite-dimensional space. We show that if the underlying stochastic oracle has uniformly bounded variance, our method exhibits an overall oracle complexity of $\tilde{O}(\varepsilon^{-5})$, to obtain $\varepsilon$ expected fixed-point residual for nonexpansive operators, improving recent rates established for the stochastic Krasnoselskii-Mann iteration. Also, we establish a lower bound of $Ω(\varepsilon^{-3})$ which applies to a wide range of algorithms, including all averaged iterations even with minibatching. Using a suitable modification of our approach, we derive a $O(\varepsilon^{-2}(1-γ)^{-3})$ complexity bound in the case in which the operator is a $γ$-contraction to obtain an approximation of the fixed-point. As an application, we propose new model-free algorithms for average and discounted reward MDPs. For the average reward case, our method applies to weakly communicating MDPs without requiring prior parameter knowledge.

