---
type: paper
node_id: paper:bot2022_fast_optimistic_gradient
title: "Fast Optimistic Gradient Descent Ascent (OGDA) method in continuous and discrete time"
authors: ["Radu Ioan Bot", "Ernö Robert Csetnek", "Dang-Khoa Nguyen"]
year: 2022
venue: "arXiv；正式版见roadmap书目"
external_ids:
  arxiv: "2203.10947"
  doi: null
  s2: null
tags: ["fixed-point", "stochastic", "core"]
added: 2026-10-14T13:52:42Z
---

# Fast Optimistic Gradient Descent Ascent (OGDA) method in continuous and discrete time

## One-line thesis
Fast OGDA 给单调 Lipschitz 末次 o(1/k) 与弱点极限。

## Problem / Gap
同一无限随机轨道的末次残差与点极限；以roadmap的精确问题类为准。

## Method
Fast OGDA 给单调 Lipschitz 末次 o(1/k) 与弱点极限。

## Key Results
期刊版 Thms. 16–17，Algorithm 2。 原文位置：`roadmap_20261014/sources/fast_ogda.txt`。

## Assumptions
Hilbert；单调 L-Lipschitz；s<1/(2L)。

## Limitations / Failure Modes
这是确定性定理；预测点相关误差需另证。

## Reusable Ingredients
按原文定理的误差权重、输出点和filtration组织证明。

## Open Questions
原始Fast KM/Fast OGDA的随机过程覆盖判定仍需逐式证明。

## Claims
这里只记录论文报告的结论；未进行逐行形式证明审核。

## Connections
自动由 graph/edges.jsonl 生成。
- paper:trandinh2025_new_accelerated_pastextragradient —inspired_by→ paper:bot2022_fast_optimistic_gradient：VAPEG使用加速past-gradient机制；与Fast OGDA完全等价尚未核实。
- paper:bot2022_fast_optimistic_gradient —addresses_gap→ gap:raw_equivalence：提供覆盖判定所需原始递推；关系不代表判定已经完成。

## Relevance to This Project
核心邻近文献；参见主报告四组速率表与第5–7节。

## Abstract (original)

> In the framework of real Hilbert spaces we study continuous in time dynamics as well as numerical algorithms for the problem of approaching the set of zeros of a single-valued monotone and continuous operator $V$. The starting poin is a second order dynamical system that combines a vanishing damping term with the time derivative of $V$ along the trajectory. Our method exhibits fast convergence rates of order $o \left( \frac{1}{tβ(t)} \right)$ for $\|V(z(t))\|$, wher $β(\cdot)$ is a positive nondecreasing function satisfying a growth condition, and also for the restricted gap function. We also prove the weak convergence of the trajectory to a zero of $V$. Temporal discretizations of the dynamical system generate implicit and explicit numerical algorithms, which can be both seen as accelerated versions of the Optimistic Gradient Descent Ascent (OGDA) method, for which we prove that the generated sequence of iterates shares the asymptotic features of the continuous dynamics. In particular we show for the implicit numerical algorithm convergence rates of order $o \left( \frac{1}{kβ_k} \right)$ for $\|V(z^k)\|$ and the restricted gap function, where $(β_k)_{k \geq 0}$ is a positive nondecreasing sequence satisfying a growth condition. For the explicit numerical algorithm we show by additionally assuming that the operator $V$ is Lipschitz continuous convergence rates of order $o \left( \frac{1}{k} \right)$ for $\|V(z^k)\|$ and the restricted gap function. All convergence rate statements are last iterate convergence results; in addition we prove for both algorithms the convergence of the iterates to a zero of $V$. To our knowledge, our study exhibits the best known convergence rate results for monotone equations. Numerical experiments indicate the overwhelming superiority of our explicit numerical algorithm over other methods for monotone equations.

