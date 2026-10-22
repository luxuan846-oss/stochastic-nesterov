# Stochastic Fast KM 初稿

主文件：`main.tex`。参考文献：`references.bib`。编译结果：`main.pdf`。

```bash
cd paper
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

## 当前进展（2026-10-22）

暂定标题：*Last-Iterate Rates of Stochastic Fast Krasnosel'skiĭ–Mann Iterations: Momentum, Implicit Variance Reduction, and Decaying Noise*。正文英文，`article` 10pt，SIOPT 式章节。作者未填写。

**主线**：Table 1 列出已知 last-iterate 速率，三行之间的差距对应三个问题。

| 节 | 标题 | 问题 | 状态 |
|---|---|---|---|
| §1 | Introduction | 背景、两种实现（same-sample re-query / reuse）、Table 1、Q1–Q3 | 已写 |
| §2 | Preliminaries | (FP)、Assumption 2.1 非扩张、oracle (H1) | 已写 |
| §3 | The last iterate of stochastic KM | Q1：last iterate $O(\log k/k^{1/6})$ 与 random iterate $O(k^{-1/4})$ | 已写，Answer to (Q1) 引用 BC Thm 2.10、4.4、Rem 5.3 |
| §4 | Implicit variance reduction in Fast KM | Q2：动量能否隐式降低方差并加速 last iterate | 已写 |
| §5 | Fast KM under decaying noise | Q3：方差衰减多快才有 $o(1/k)$ | 只有问题与已知条件，待讨论 |
| §6 | Applications to stochastic optimization | SGD、prox gradient（有偏）、backward–forward（无偏） | 已写 |

**§4 结构**：4.1 Fast KM iteration（$s=1$ 不失一般性）→ 4.2 reuse 实现（Algorithm 1 + 两句动机 + Q2）→ 4.3 Noise propagation under reuse（Lemma：stored noise 系数 $b_k=O(1/k^2)$，new noise 权重 $a_k\to1$；Prop：$T=0$ 且方差有下界时 $\mathbb E\lVert x_{k+1}-Tx_{k+1}\rVert^2\ge\sigma^2/4$）→ 4.4 Horizon-dependent parameters（Yang et al. Thm 1：$O(D/K+\sigma\log K/\sqrt K)$，Answer to (Q2)）。

**本文新增的数学内容**：Lemma 4.x 的噪声分解与二阶矩递推；Prop 4.x 的 $T=0$ 反例；§6 的 $\operatorname{Fix}T_{BF}$ 刻画与 prox 有偏反例。其余定理均为引用。

## 待办

1. **Q3 门槛**：下界只要求 $q>1$，已知 a.s. 充分条件 N6-$\ell^2$ 要求 $q>3$（N6-$\ell^1$：$q>4$）。计划用 $t_k^2$ 加权能量，对照 $T=0$（mean-square 只需 $q>2$）与 $T=-\mathrm{Id}$（$q>3$）。
2. §5 补一句明确写出 $q>1$ 与 $q>3$ 的差距。
3. Table 1 之后补定位段，可并入 intro 的 "We thus study the reuse implementation."
4. 待定：Table 1 动量列是否改成 iKM 参数 $(\alpha_k,\beta_k,\lambda_k)$；iKM 外推参数 $\alpha_k$ 与 Fast KM 的 $\alpha$ 记号冲突，候选改为 $\mu_k$。
5. 未提交 git。

## 已固定的数学设定

1. $\mathbb R^d$，Euclidean 范数，固定非扩张算子，非空不动点集合。
2. 查询点为当前迭代点，误差条件无偏，$\sigma_k^2:=\mathbb E[\lVert e_k\rVert^2\mid\mathcal F_k]$；有界方差作为 Assumption 3.2 在 §3 用到时引入。
3. 固定 $\alpha>2$，$s=1$；一次初始化查询，之后每步一次新查询，上一步返回值保存后复用。
4. 组合误差 $\eta_k=a_ke_k-d_ke_{k-1}$，条件均值 $-d_ke_{k-1}$。
5. N6 为 Attouch–Fadili–Kungurtsev Thm 3.1 的 $(K_2)$/$(K_2^+)$ 在 Fast KM 下的特例，只作为候选充分条件，未写成本文定理。

## 补充材料的采用边界

- 采用：目标算子固定、随机性来自查询、期望梯度例子、完整 prox 估计未必无偏。
- 不采用“所有近端/PDHG 随机实现都满足无偏算子模型”。引言只给有明确依据的采样梯度例子。
- 不采用“已有文献都没有使用过去的估计”。本地 AFP 比较笔记已经说明其消元式也含前一步估计，不能把这种结构本身写成新贡献。
- 不采用“一致有界方差必然导致残差不趋零”。有界方差上界也允许实际误差为零；失效结论必须说明具体噪声和算子。
- 不把 $q>2$、$q>3$ 写成一般非线性算子的精确门槛。当前材料中的标量例子不能替代一般定理。
- 不把几乎必然 little-o 直接换算为期望样本复杂度；还需要可量化的有限时域界。
- 不把历史误差的条件均值非零写成“Robbins–Siegmund 失效”；它说明需要处理额外项或选择合适的能量。

## 术语与固定表达对照

| 本稿采用表达 | 核对出处 | 用途 |
|---|---|---|
| nonexpansive operator; fixed-point residual | Yang 等人 §2.1、Theorem 1；Boţ–Nguyen §1 | 问题与指标 |
| stochastic oracle; conditionally centered stochastic noise | Yang 等人 §2.2，式 (6)–(8) | 随机查询模型 |
| all information available immediately before the oracle call | Yang 等人 §2.2 | filtration 的时间约定 |
| strongly measurable | Yang 等人 §2.2 | Hilbert 值随机变量 |
| last-iterate; root-mean-square | Yang 等人 §1.1、Theorem 1 | 有限时域结果的比较 |
| weak convergence of the iterates | Boţ–Nguyen Theorem 3.4 | 确定性结论和研究目标 |
| almost sure convergence of iterates | AFP §3.2(d)、Theorem 2；Bravo–Cominetti 摘要 | 随机目标 |
| extrapolation term; operator evaluations at the previous iterates | Boţ–Nguyen Remark 2.1 | 更新中的历史算子值 |

全文统一采用 `fixed-point`、`cocoercivity`、`almost-sure` 作定语，`almost surely` 作副词。引用文献标题保留导出写法。

没有作为原文固定表达引用的内容：`retains the preceding evaluation` 和关于 `stored response` 的句子是对式 (3.1) 实现方式的描述；N6 的候选地位、研究目标、噪声组合恒等式和 prox 反例是本稿的数学说明，不作为已有文献定理归因。

已核对表达同步保存于 `../notes/writing-phrasebook.md`。

## 文献来源

- Boţ–Nguyen：Crossref DOI `10.1137/22M1504305` 导出 BibTeX；结论核对本地 arXiv v2 原文 Algorithm 2.1、Theorems 3.4–3.5。
- Bravo–Cominetti：Crossref DOI `10.1137/22M1515550` 导出 BibTeX；采样梯度例子核对本地期刊文本 §4.3。
- Yang 等人：arXiv `2609.28543` 官方 BibTeX 与源码；模型核对 §2.2，RMS 界核对 Theorem 1。
- Nguyen-Trung–Tran-Dinh：arXiv `2512.13547` 官方 BibTeX；已有几乎必然结果核对 v1 Theorem 2。这里只陈述原文提供的结果，不声称其全部证明已经独立验证。

参考文献仅规范化 citation key、TeX 重音和数学标题标记，没有自行补造书目字段。
