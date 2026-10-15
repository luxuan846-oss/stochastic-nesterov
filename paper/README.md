# Stochastic Fast KM 初稿

主文件：`main.tex`。参考文献：`references.bib`。编译结果：`main.pdf`。

```bash
cd paper
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

## 当前范围

问题定位：通过条件无偏的随机算子查询，寻找一个固定非扩张算子的不动点。

- 正文采用英文，已有 Introduction、Problem formulation and stochastic oracle、Stochastic Fast KM iteration。
- 采用 Yang 等人 arXiv:2609.28543v1 源码中的 `article`、10pt、单栏、1 inch 页边距作为版式基础。
- 使用按节编号的公式和定理环境、数字引用，按 SIOPT 理论论文方式组织章节；当前没有使用官方 `siamart` 投稿类。
- 源文件末尾以注释预留 Almost-sure convergence analysis、Noise conditions and sample costs、Numerical experiments、Conclusions、Auxiliary results。后续有结果后再启用，PDF 不显示无内容的章节。
- 作者和单位尚未填写；标题为暂定标题。摘要明确标明当前只完成问题、模型和算法设定。

## 已固定的数学设定

1. 实可分 Hilbert space，固定非扩张算子，非空不动点集合。
2. 查询点为当前迭代点，误差关于查询前的信息条件零均值；不引入偏差项 $b_k$。
3. 与 Yang 等人模型的关系仅为其式 (6) 中 $b_k=0$ 的特例；没有宣称两个随机算法相同。
4. 固定参数 $\alpha>2$、$0<s\le1$，一次初始化查询，之后每步一次新的随机算子评估。
5. 上一步返回值直接保存后使用，误差组合明确写出；组合误差的条件均值未必为零。
6. N2 表示条件方差一致有界；这里的 N6 专指固定步长下的加权二阶矩预算可和。N6 被列为待研究的充分条件，没有写成已证明定理。

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
