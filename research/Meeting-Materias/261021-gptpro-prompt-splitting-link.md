# 给 GPT Pro 的调研指令：Boţ 系列加速 fixed-point 方法与 splitting 算法的对应关系

2026-10-21

使用方法：把第 1 节到第 5 节的全文粘贴到 GPT Pro 对话框，打开联网搜索。可附上手头已有的 PDF。

---

## 1. 背景

我的研究方向是结构化的非光滑 composite optimization，包括不仅限于：问题具有 $f+g$、$f+g+h$、$f+g\circ L$ 等结构时，利用结构设计 splitting 算法，并且给出依托 fixed-point / monotone operator 理论的收敛分析，而非只给一个 standard 的 convergence rate。

我关心 Radu Ioan Boţ 及合作者的加速 fixed-point 方法**怎样落到具体的优化算法上**：论文把哪个 splitting 写成了哪个算子 $T$ 的 fixed-point iteration，加速后的 rate 在原优化问题上意味着什么。论文本身研究的抽象问题只作为背景。

参照例子：reflected forward-backward 类论文把算法用到 forward-backward splitting 等具体问题上。我需要的是这类对应关系的完整清单。

## 2. 论文清单

先逐篇确认身份，给出准确标题、作者、年份、期刊和 arXiv 编号。我的描述可能不准确，按描述无法确定的标「待确认」并列出候选。

1. Boţ, Nguyen, *Fast Krasnosel'skiĭ–Mann algorithm with a convergence rate of the fixed point iteration of o(1/k)*, SINUM 2023。
2. Boţ, Csetnek, Nguyen, Fast OGDA（*Fast Optimistic Gradient Descent Ascent method in continuous and discrete time*）。
3. Boţ 的一篇 Fast KM 推广文章，我记作「siopt」，可能涉及算子和或多算子结构。待确认。
4. Boţ, Chenchene, Fadili 等，带 preconditioner 的 generalized Fast KM。
5. Boţ 与合作者的 Fast Inertial 类文章。待确认。
6. 你检索到的 Boţ 及合作者 2022–2026 年其他加速 fixed-point、Halpern、Tikhonov、Fast OGDA 类文章，凡是包含具体 splitting 应用的都收录。
7. 对照文献：「reflected forward-backward」论文，我记得约 2016 年。候选包括 Malitsky 的 projected reflected gradient、Malitsky–Tam 的 forward-reflected-backward、Cevher–Vũ 的 reflected forward-backward。确认最符合的一篇，并说明它与 Boţ 系列的关系。

## 3. 任务

### 3.1 逐篇提取对应关系

对每篇论文，找出原文中**所有**把加速方法与具体算法建立联系的地方，包括应用章节、Corollary、Remark、Example 和数值实验。每一条对应关系写成表格中的一行：

| 列 | 内容 |
|---|---|
| 位置 | 节号、定理 / Corollary / Remark 编号、式号 |
| 原优化问题 | 例如 $\min f+g$、$\min f+g+h$、$\min f(x)+g(Lx)$、saddle-point、monotone inclusion $0\in A+B$ |
| 对应的 splitting | 例如 forward-backward、Douglas–Rachford、Davis–Yin、Chambolle–Pock / PDHG、ADMM、Tseng FBF、forward-reflected-backward、extragradient、OGDA |
| 算子 $T$ 或 $V$ | 写出显式公式，例如 $T=J_{\gamma A}\circ(\mathrm{Id}-\gamma B)$ |
| 算子性质 | averaged 及常数、nonexpansive、cocoercive、monotone + Lipschitz；在哪个 metric 或 preconditioner 下成立 |
| 加速后的 rate | 对哪个量，例如 $\lVert x_k-Tx_k\rVert=o(1/k)$，迭代点是否弱收敛 |
| 回到原问题的量 | 原文是否把 residual 换算成 objective gap、gradient mapping、KKT residual、primal-dual gap 或可行性误差；给出换算式与位置。原文没有换算的标「原文未换算」 |
| 参数条件 | 步长、松弛参数、cocoercivity / Lipschitz 常数的约束 |

### 3.2 反向汇总表

以 splitting 为行，以论文为列。格子中填写：该论文是否覆盖这个 splitting、对应的定理编号、得到的 rate。没有覆盖的格子留空，并在表下说明原因：算子类别不符（例如不是 averaged），还是原文没有讨论。

至少包含的行：proximal point、forward-backward、Douglas–Rachford、Peaceman–Rachford、Davis–Yin、Chambolle–Pock / PDHG、ADMM、Tseng FBF、forward-reflected-backward、extragradient、OGDA、Halpern 型 splitting。

### 3.3 算子类别与方法分支

整理一张短表说明：哪些 splitting 落在 averaged / nonexpansive 的 Fast KM 分支，哪些落在 monotone + Lipschitz 的 Fast OGDA 分支，哪些需要 preconditioned 或 degenerate metric 才能纳入。每条判断给出文献依据，例如 He–Yuan 关于 PDHG 的 proximal point 解释、Gabay 关于 ADMM 与 Douglas–Rachford 对偶关系的结果、Davis–Yin 从 fixed-point residual 到 objective rate 的结果。

### 3.4 随机版本

对 3.2 中每个 splitting，检索已有的 stochastic 或 inexact 加速版本，并说明随机误差进入的位置：

- 噪声在 resolvent / prox 外部，例如随机梯度前向步，此时加性零均值模型 $\widehat T_k(x)=T(x)+e_k$ 是否精确成立；
- 噪声进入 resolvent / prox 内部，此时样本算子的均值是否仍等于 $T$，偏差如何处理。

### 3.5 结构带来的缺口

列出 3–5 类问题结构：对这类结构直接套用现有 Fast KM / Fast OGDA 会失效，或者需要新的分析。失效的原因可以是算子不再 averaged、只在 degenerate metric 下 nonexpansive、随机采样导致有偏，或者 residual 无法换算回原问题。每类结构给出具体例子、现有最近的文献和剩余空白。这一节是你的推断，与原文结论分开写。

## 4. 要求

1. 中文行文；专业术语、人名、方法名、期刊名保留英文。
2. 每条对应关系必须给出原文位置。无法从原文确认的，标「待核实」，禁止编造定理编号或公式。
3. 每篇文献给出作者、标题、年份、期刊或会议，以及 arXiv 编号或 DOI，并通过联网检索确认。
4. 区分「论文原文结论」与「你的推断」。
5. 凡是「覆盖 / 等价 / 特例」类判断，写明算法、算子和参数条件。例如「Douglas–Rachford 是 Fast KM 的特例」要写清楚取哪个 $T$、averaged 常数是多少、参数取什么值。

## 5. 输出顺序

1. 论文清单确认结果；
2. 3.1 逐篇对应表；
3. 3.2 反向汇总表；
4. 3.3 算子类别表；
5. 3.4 随机版本；
6. 3.5 结构缺口；
7. 待核实事项汇总。
