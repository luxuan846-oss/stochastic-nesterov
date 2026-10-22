# 论文写作固定表达

文献整理的分组、核对流程与固定用词见 `notes/literature-route-map.md`。

## 2026-10-15 随机 Fast KM 初稿

适用稿件：`paper/main.tex`。本表记录核对过的术语和短表达，不授权扩大相应定理的适用条件。

| 表达 | 原文位置 | 本稿约定 |
|---|---|---|
| nonexpansive operator | Yang 等人 2026 §2.1 式 (3)；Boţ–Nguyen 2023 §1 | 作用在 Hilbert space 上的固定算子 |
| fixed-point residual | Yang 等人 Theorem 1；Boţ–Nguyen Theorem 3.5 | 范数 $\lVert x-Tx\rVert$，与平方区分 |
| stochastic oracle model | Yang 等人 §2.2 | 只采用其条件无偏特例 |
| conditionally centered stochastic noise | Yang 等人 §2.2，式 (6)–(8) | 查询前 filtration 下均值为零 |
| immediately before the oracle call | Yang 等人 §2.2 | $\mathcal F_k$ 为第 $k$ 次查询前的信息 |
| strongly measurable | Yang 等人 §2.2 | Hilbert 值随机变量 |
| last-iterate | Yang 等人 §1.1、Theorem 1 | 确定索引输出，不是随机选点或历史最小值 |
| root-mean-square | Yang 等人 §1.1 与 Theorem 1 的公式 | $(\mathbb E r_K^2)^{1/2}$ |
| weak convergence of the iterates | Boţ–Nguyen Theorem 3.4 | 无限维的点列结论 |
| almost sure convergence | Bravo–Cominetti 摘要；AFP Theorem 2 | 写成副词时采用 almost surely |
| extrapolation term | Boţ–Nguyen Remark 2.1 | 特定更新中的算子值差分项 |
| operator evaluations at the previous iterates | Boţ–Nguyen Remark 2.1 | 不将其扩写为已证明的随机噪声门槛 |

来源路径：

- `research/memory/readings/sources/ikm.txt`
- `research/memory/readings/sources/fast_km.txt`
- `research/roadmap_20261014/sources/bravo_cominetti.txt`
- `research/memory/readings/sources/delayed.txt`

统一写法：`fixed-point`、`cocoercivity`、`almost-sure` 作定语，`almost surely` 作副词。

本稿自己的描述而非原文固定术语：`retains the preceding evaluation`、`stored response`。它们仅指保存上一轮返回的向量，不用于命名新算法或宣称新颖性。

## Fast KM 章节修订

| 采用的叙述或格式 | 原文位置 | 本稿处理 |
|---|---|---|
| 先给 KM 更新、松弛参数和残差速率，再引入 Fast KM | Boţ–Nguyen §1，式 (1.3) 及后续速率讨论 | KM 使用固定 $\lambda\in(0,1)$ 陈述保证 |
| Nesterov's momentum updates | Boţ–Nguyen 摘要、§1 | 用于介绍 Fast KM 的加速机制 |
| 参数和初值在更新式之前给出 | Boţ–Nguyen Algorithm 2.1，式 (2.7) | 非扩张算子情形固定 $\alpha>2$、$0<s\le1$ |
| KM iteration with an additional extrapolation term | Boţ–Nguyen Remark 2.1，式 (2.8) | 解释 $s=1$ 时的算子值差分项 |
| 精确查询到随机查询的转接 | Yang 等人 §1、§2.1–2.2；Bravo–Cominetti (SKM) | 保持 $T$ 形式，将精确评估替换为条件无偏返回值 |

本次统一使用 fixed-point 的 $T$ 形式。随机误差差分和总误差的系数由本稿递推直接展开；保留总误差中的单独 $e_k$ 项，不将总扰动简化成纯噪声差。正文只陈述这些恒等式，不由符号相反直接宣称噪声门槛已经改善。

## 2026-10-22 Introduction 改写

| 采用的叙述或格式 | 原文位置 | 本稿处理 |
|---|---|---|
| 用 quote 环境单独陈述研究问题 | Yang 等人 §1 第 3 段后 | 问题按本文递推重写，只借格式 |
| Related work 用加粗段首分组 | Yang 等人 §1.2 | 四组：stochastic KM、fast deterministic、stochastic accelerated、lower bounds |
| "replacing the exact operator evaluations … with stochastic oracle responses" | Yang 等人 §1 第 3 段 | 改写为统一递推 $(1-\lambda_k)x_k+\lambda_k(Tx_k+e_k)$ |
| "exact evaluations or summable perturbations" | Yang 等人 §1.2 | 用于概括确定性 Fast KM 分析的范围 |
| 速率综述按 KM → Fast KM 顺序 | Boţ–Nguyen §1 | $o(1/\sqrt{k})$ 到 $o(1/k)$ |

对照表与出处：`notes/intro-draft-20261022.md`。

## 2026-10-22 Applications 章节

| 采用的叙述或格式 | 原文位置 | 本稿处理 |
|---|---|---|
| 应用章节放在主体分析之后，逐个给出 $T$、averaged 常数与 $\operatorname{Fix}T$ | Boţ–Nguyen §4；BC §4.3；Cortild 等 §3.2 | §4 按 SGD、FB、BF 三小节 |
| "The operator $T_{DY}$ is $\frac{2\beta}{4\beta-\gamma}$-averaged" | Boţ–Nguyen §4，Corollary 4.1 前 | $B=0$ 得 $T_{FB}$ 的常数 |
| Stochastic Backward-Forward splitting (SBF) | Cortild 等 §3.2，式 (SBF) | 沿用名称 |

## 2026-10-22 Reuse noise reduction

| 采用的结构或表达 | 来源 | 本稿处理 |
|---|---|---|
| 直接 perturbation 分析的限制 → auxiliary sequence → subtracting the recursion → effective errors | Bravo–Cominetti §2.1 | §4.3 按此顺序组织；递推和 Lemma 按 Fast KM 单独推导 |
| 隐式 variance reduction 的讨论 | Bravo–Cominetti Remark 2.3 | 区分 stored error 与 new error 的权重 |

Q2 的 mean-square 反例、Q3 的 almost-sure 目标及两种收敛意义的区分为本文说明；不作为参考文献已证明的 Fast KM 结果。
