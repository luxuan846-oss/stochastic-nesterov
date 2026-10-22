# Stochastic Fast KM 初稿

主文件：`main.tex`。参考文献：`references.bib`。编译结果：`main.pdf`。

```bash
cd paper
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

## 当前进展（2026-10-22）

基准：`d75c431` 的进展记录；§4.2 的 reuse 段落和算法调整已在 `5d783d1` 推送。以下状态按当前 `main.tex` 核对；§4.3、Q2–Q3 和文档更新随本次提交同步。

暂定标题：*Last-Iterate Rates of Stochastic Fast Krasnosel'skiĭ–Mann Iterations: Momentum, Implicit Variance Reduction, and Decaying Noise*。

## 主线

**Q1 立基准 → Q2 给出反例 → Q3 留作开放问题。**

1. **Q1**：以 Bravo–Cominetti Theorem 4.4 给出的 stochastic KM last-iterate expectation bound $O(\log k/k^{1/6})$ 为基准。该 upper bound 不证明其他速率不可能。
2. **Q2**：pure Fast KM 的固定参数不能普遍保证 residual 的 mean-square convergence。具体地，$T=0$ 且 noise variance 有正下界时，residual 的二阶矩不趋于零。这是反例结论，不是所有 bounded-variance 实例的共同性质，也不直接给出 expectation 或 almost-sure 的不可能性。
3. **Q3**：研究 decaying noise 下的 almost-sure residual rate 与迭代点收敛。当前只列目标和候选条件，充分性尚未证明。

## 范围约定

1. 讨论渐近与 almost-sure 结果；保留 Q1 的 expectation 基准和 Q2 的 mean-square 反例，不展开 horizon-dependent 参数、finite-horizon bound 或 sample complexity。
2. 算法固定为 pure Fast KM：$s=1$、$\alpha>2$ 固定；初始化查询一次，之后每步一次新 oracle 调用，复用上一步的 response。
3. §4.3 使用 $\rho_k=\alpha/(k+\alpha)$，momentum 系数为 $1-\rho_k$。N6 只是候选充分条件。

## 已完成的修改

| 位置 | 当前内容 | 状态 |
|---|---|---|
| §1 与 Table 1 | Q1–Q3 主线；区分 expectation、mean-square 和 almost-sure 目标；删除 stochastic iKM 的 horizon-dependent 比较行和 $q>1$ 的样本数论证 | 已写入 |
| §1 开头与 §2 | 问题 (FP) 与 nonexpansive 条件在引言首段以文字给出，不设 assumption 环境；§2 给出 filtration 与条件无偏 oracle | 已写 |
| §3 | Q1 与 stochastic KM 已有结果，引用 BC Theorems 2.10、4.4 和 Remark 5.3 | 已写；保留 Q1 |
| §4.2 | 显式 stored response 与更新式；算法不依赖 $a_k,d_k$ | 已推送 `5d783d1`；后续局部编辑以当前源码为准 |
| §4.3 | 直接 perturbation 分析的限制 → auxiliary-state reduction → Lemma 4.1 → Proposition 4.2 → 对照 BC Remark 2.3 → Answer to Q2 | 已写入 `main.tex` |
| §4.4 | 原 horizon-dependent parameters 及其 Q2 回答 | 已从正文删除 |
| §5 | almost-sure 目标；以 $T=0$ 反例引出 decaying noise；区分 $q>2$ 必要性与 $q>3$ 候选充分性 | 已写入；尚未压缩为一段展望 |
| 记号 | §4.3 统一为 $\rho_k$；VR 比较使用 “a tunable weight” 的无符号表述；§5 使用 $\alpha_k=1-\rho_k$ | 已处理 |
| Applications | $\operatorname{Fix}T_{BF}$ 刻画、prox 有偏反例等 | 源码注释保留，当前 PDF 不显示 |
| 给 Boţ 的邮件 | 中英文定稿 | 据作者提供的进展，待发送；本次未核对邮件稿，未发送 |

最近一次完整编译通过，未发现未定义引用或公式溢出；编译结果不替代数学证明核查。

## 核心数学内容

本文的推导见 `lem:noise` 和 `prop:fixed`；来源与结构对照见 `../notes/writing-phrasebook.md`。

新噪声同时进入 relaxation step 与 momentum term：

$$
\eta_k=\frac{\rho_k}{2}e_k+(1-\rho_k)(e_k-e_{k-1}).
$$

Lemma 4.1 将 auxiliary sequence 写成

$$
u_{k+1}=\Bigl(1-\frac{\rho_k}{2}\Bigr)e_k+v_{k+1},\qquad
v_{k+1}=\Bigl(1-\frac{\rho_k}{2}\Bigr)v_k+b_ke_{k-1},
$$

其中

$$
b_k=\frac{\alpha(\alpha-2)}{4(k+\alpha)(k+\alpha-1)}=O(k^{-2}).
$$

stored error 的净系数为 $O(k^{-2})$，new error 的系数 $1-\rho_k/2\to1$。关于 $v_k$ 的衰减仍须结合 noise 条件分析。

Proposition 4.2：对 $T=0$ 和 $\mathbb E\sigma_k^2\geq\sigma^2>0$，

$$
\mathbb E\lVert x_{k+1}-Tx_{k+1}\rVert^2\geq\frac{\sigma^2}{4},\qquad k\geq1.
$$

Q3 涉及两个不同结论：

- **mean-square 必要条件**：由同一反例的逐步下界，root-mean-square residual 为 $o(1/k)$ 要求 $k^2\mathbb E\sigma_k^2\to0$。对 deterministic profiles $\sigma_k^2\asymp k^{-q}$，这要求 $q>2$。
- **almost-sure 候选充分条件**：N6-$\ell^2$ 为 $\sum_k(k+1)^2\sigma_k^2<\infty$ almost surely；对上述 deterministic profiles，当且仅当 $q>3$ 成立。它是否足以保证当前算法的 almost-sure 目标尚待证明。

两者涉及相同的加权 variance 量，但收敛意义不同，不能直接作为同一门槛的上下界。

## 待办

1. 将 §5 压缩为一段展望，保留 almost-sure 目标及候选条件的待验证地位。
2. 按最新拟议格式，将 `cor:skm` 的引用放入标题可选参数 `[{\cite[...]{...}}]`；当前仍为正文开头的引用写法。
3. 核对 Table 1、Q2 回答与 Proposition 的指标是否始终一致，避免由 mean-square 反例推断 expectation 或 almost-sure 不可能性。
4. 给 Boţ 的邮件待作者发送。

## 待验证

1. **N6-$\ell^2$ 的适用性**：Attouch–Fadili–Kungurtsev Theorem 3.1 针对 Ravine 方法；当前 pure Fast KM 的 almost-sure 能量分析尚未建立。
2. **确定性 perturbation 定理的出处**：尚未核实一条可直接用于当前递推的 inexact Fast KM 定理。§4.3 的文献概述不作为这种定理的替代。
3. **随机 Fast KM 与 iKM 的等价关系**：杨等人 Appendix A 中的确定性对应关系不直接作为随机等价证明；当前主线不使用这一推断。

## 已固定的数学设定

1. $\mathbb R^d$，Euclidean 范数，固定非扩张算子，非空不动点集合。
2. 查询点为当前迭代点，误差条件无偏，$\sigma_k^2:=\mathbb E[\lVert e_k\rVert^2\mid\mathcal F_k]$；有界方差作为 Assumption 3.2 在 §3 用到时引入。
3. 固定 $\alpha>2$，$s=1$；一次初始化查询，之后每步一次新查询，上一步返回值保存后复用。
4. 令 $\rho_k=\alpha/(k+\alpha)$；组合误差 $\eta_k=(1-\rho_k/2)e_k-(1-\rho_k)e_{k-1}$，条件均值 $-(1-\rho_k)e_{k-1}$。
5. N6 采用 Attouch–Fadili–Kungurtsev Thm 3.1 中条件的加权可和形式；该定理针对 Ravine 方法，对当前 Fast KM recursion 的适用性待验证。

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
