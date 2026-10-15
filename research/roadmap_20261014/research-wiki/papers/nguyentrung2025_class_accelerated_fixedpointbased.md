---
type: paper
node_id: paper:nguyentrung2025_class_accelerated_fixedpointbased
title: "A Class of Accelerated Fixed-Point-Based Methods with Delayed Inexact Oracles and Its Applications"
authors: ["Nghia Nguyen-Trung", "Quoc Tran-Dinh"]
year: 2025
venue: "arXiv；正式版见roadmap书目"
external_ids:
  arxiv: "2512.13547"
  doi: null
  s2: null
tags: ["fixed-point", "stochastic", "core"]
added: 2026-10-14T13:52:43Z
---

# A Class of Accelerated Fixed-Point-Based Methods with Delayed Inexact Oracles and Its Applications

## One-line thesis
AFP 已覆盖一般随机 oracle 加递增批量的 a.s. 快速率。

## Problem / Gap
同一无限随机轨道的末次残差与点极限；以roadmap的精确问题类为准。

## Method
AFP 已覆盖一般随机 oracle 加递增批量的 a.s. 快速率。

## Key Results
Thm. 2 在 y_k 上的残差 o(1/k)；Cor. 2。 原文位置：`memory/readings/sources/delayed.txt`。

## Assumptions
有限维余强制；递推误差条件(7)与可和delta。

## Limitations / Failure Modes
与原始缓存 Fast KM 的全部系数、初始化和随机过程等价性待核对。

## Reusable Ingredients
按原文定理的误差权重、输出点和filtration组织证明。

## Open Questions
原始Fast KM/Fast OGDA的随机过程覆盖判定仍需逐式证明。

## Claims
这里只记录论文报告的结论；未进行逐行形式证明审核。

## Connections
自动由 graph/edges.jsonl 生成。
- paper:nguyentrung2025_class_accelerated_fixedpointbased —extends→ paper:trandinh2024_variancereduced_fast_krasnoselkiimann：AFP一般递推误差模型覆盖有限和之外的随机oracle。
- paper:nguyentrung2025_class_accelerated_fixedpointbased —invalidates→ idea:001：原文已明示a.s.残差小o与点极限，否定宽泛首次性。
- paper:nguyentrung2025_class_accelerated_fixedpointbased —addresses_gap→ gap:raw_equivalence：提供覆盖判定所需原始递推；关系不代表判定已经完成。

## Relevance to This Project
核心邻近文献；参见主报告四组速率表与第5–7节。

## Abstract (original)

> In this paper, we develop a novel accelerated fixed-point-based framework using delayed inexact oracles to approximate a fixed point of a nonexpansive operator (or equivalently, a root of a co-coercive operator), a central problem in scientific computing. Our approach leverages both Nesterov's acceleration technique and the Krasnosel'skii-Mann (KM) iteration, while accounting for delayed inexact oracles, a key mechanism in asynchronous algorithms. We also introduce a unified approximate error condition for delayed inexact oracles, which can cover various practical scenarios. Under mild conditions and appropriate parameter updates, we establish both $\mathcal{O}(1/k^2)$ non-asymptotic and $o(1/k^2)$ asymptotic convergence rates in expectation for the squared norm of residual. Our rate significantly improves the $\mathcal{O}(1/k)$ rates in classical KM-type methods, including their asynchronous variants. We also establish $o(1/k^2)$ almost sure convergence rates and the almost sure convergence of iterates to a solution of the problem. Within our framework, we instantiate three settings for the underlying operator: (i) a deterministic universal delayed oracle; (ii) a stochastic delayed oracle; and (iii) a finite-sum structure with asynchronous updates. For each case, we instantiate our framework to obtain a concrete algorithmic variant for which our convergence results still apply, and whose iteration complexity depends linearly on the maximum delay. Finally, we verify our algorithms and theoretical results through two numerical examples on both matrix game and shallow neural network training problems.

