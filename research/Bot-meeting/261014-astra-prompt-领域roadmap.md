# 给 Astra 的调研指令：随机快速不动点方法的领域 roadmap

2026-10-14

## 1. 任务

为下面这个窄领域整理一份 roadmap。领域由三条线的交集界定：

- **A. 随机算法的渐近收敛理论**：同一条随机轨道无限运行时的几乎必然收敛、末次迭代速率；工具为 Robbins–Siegmund 引理、随机拟 Fejér 单调性、鞅收敛定理。
- **B. Nesterov 型加速在随机噪声下的性质**：动量在噪声下能保住什么速率，噪声如何被动量放大，需要什么步长、批量或噪声可和条件。
- **C. 不动点迭代与单调算子求零**：KM、Halpern、Fast KM、惯性 KM、EAG、OGDA、Fast OGDA。

roadmap 按交集组织：

| 交集 | 内容 | 代表线索 |
|---|---|---|
| A∩B | 随机 Nesterov 的几乎必然速率与迭代点收敛 | Hermant 等 2025、Salzo 2025、Liu–Yuan、Sebbouh 等 |
| A∩C | 随机 KM、随机 Halpern 的几乎必然收敛与误差界 | Combettes–Pesquet 2015、Bravo–Cominetti 2024、Bravo–Contreras |
| B∩C | 确定性 Fast KM、Fast OGDA、锚点化方法的快速末次迭代速率，以及随机惯性 KM 的样本复杂度 | Boţ–Nguyen、Boţ–Csetnek–Nguyen、Yoon–Ryu、Yang 等 2026 |
| A∩B∩C | 随机 Fast KM、随机 Fast OGDA 的几乎必然速率 | 我的课题，检索是否已有结果 |

三条线各自的一般内容只写到支撑上述交集所需的程度。非单调变分不等式、分布式与联邦设定不写。

上述划分由我初步拟定，你检索后发现更准确的划分方式时，直接改用并说明理由。

读者：刚进入这一方向的优化研究者，背景是随机 Nesterov 加速的几乎必然收敛分析。

读完后我要能做到三件事：

1. 用一张表说清：每种加速机制在确定性、随机期望、随机几乎必然三种意义下的已知最好速率，以及对应论文；
2. 知道这个窄领域里谁在做、做到哪一步，能找到他们的主页；
3. 判断我的课题「随机 Fast KM 与随机 Fast OGDA 的几乎必然速率」与哪几篇论文最近，空白在哪里。

本地参考材料，先读：

- `与 Boţ 教授第二次讨论笔记：随机快速 fixed-point 与单调算子方法.md`
- `261014-astra-prompt-stochastic-KM.md` 第 3.1 节的文献线索
- Zotero 中 fixed-point 一栏的 PDF，路径在 `/Users/liluxuan/Zoterodb/storage/`

## 2. 内容

### 2.1 速率总表

这是 roadmap 的主体，按 A∩B、A∩C、B∩C、A∩B∩C 分成四张表。行为方法，列为问题类、噪声模型、结论类型、速率、论文与定理编号。

A∩B 表的方法包括随机 Nesterov 的各类变体（单步长 $\alpha/k$ 型、双步长型、递增批量型），问题类为光滑凸优化。其余三张表的方法至少包括：KM、Halpern、Fast KM、惯性 KM、EAG、Fast OGDA，以及各自的随机版本。问题类区分非扩张不动点、余强制算子求零、单调 Lipschitz 算子求零。结论类型区分确定性末次迭代、随机期望界、随机几乎必然速率、迭代点几乎必然收敛、样本复杂度。

表中速率写成具体阶，例如 $O(1/k)$、$o(1/k)$、$\tilde{O}(\varepsilon^{-2})$，并注明是 $\lVert x_k - Tx_k\rVert$ 还是其平方。已知下界单独列一行。尚无结果的格子标「空白」，并写明你检索了哪些来源。

### 2.2 发展时间线

只写直接通向 2.1 节结果的节点，控制在 15–20 个。每个节点写出年份、作者、论文、结论，以及它推进了总表中的哪一格。

### 2.3 研究人员

只收录在这个窄领域有代表作的人，控制在 15–20 人。表格列为：姓名、机构、主页、本领域代表作两篇、研究线。研究线标注为 A∩B、A∩C、B∩C 中的一个或多个。

经典人物另列一张短表，最多 8 人，只写与本领域直接相关的贡献。

下列名单是初步线索，核实后保留符合标准的人，并补充遗漏的人：

- Baptiste Hermant、Jean-François Aujol、Charles Dossal、Aude Rondepierre、Saverio Salzo、Hedy Attouch、Othmane Sebbouh；
- Roberto Cominetti、Mario Bravo、Juan Pablo Contreras、Radu Ioan Boţ、Ernö Robert Csetnek、Dang-Khoa Nguyen、Patrick Combettes；
- Ernest Ryu、Donghwan Kim、TaeHo Yoon、Felix Lieder、Jelena Diakonikolas、Quoc Tran-Dinh；
- Nicolas Loizou、Eduard Gorbunov、Ahmet Alacaoglu、Lin Xiao、Yuejie Chi、Ashok Cutkosky、Tong Yang、Yekini Shehu。

### 2.4 当前课题

列出 5–7 个课题，每个都要具体到问题类、噪声模型和目标速率。不收录「推广到更一般设定」一类泛化课题。每个课题写出：

1. 精确的问题陈述；
2. 已知最好结果，附论文与定理编号；
3. 剩余空白；
4. 2024–2026 年的代表论文；
5. 与我的课题的关系：直接竞争、可借用技巧，或背景。

### 2.5 我的课题的位置

在 2.1 节总表中标出我的课题对应的格子。列出 3–5 篇最近邻论文，逐篇写出：它证明了什么、没证明什么、我的课题与它的区别。

## 3. 要求

1. 中文行文，人名、方法名、期刊名保留英文。
2. 每个主页链接都要实际打开确认可访问，并写明确认日期；失败的标「待核实」。
3. 每篇文献给出作者、标题、年份、期刊或会议，以及 arXiv 编号或 DOI。所有速率都标定理编号；无法核实的标「待核实」。

## 4. 输出文件

产出两个文件，放在 `/Users/liluxuan/Documents/Obsidian/My_Paper/6_stochastic_acclerate/Bot-meeting/`：

1. **Markdown**：`261014-领域roadmap-随机快速不动点.md`，供 Obsidian 阅读。
   - 文件开头写 YAML front matter：`title`、`date: 2026-10-14`、`tags: [roadmap, fixed-point, monotone-operator, stochastic]`。
   - 行内公式用 `$...$`；独立公式用单独成行的 `$$` 包围，前后各留一行空行；表格内公式用 `\lVert`、`\rVert` 代替竖线。
   - 链接用 `[文字](URL)` 格式；用二级、三级标题组织。
2. **PDF**：`261014-领域roadmap-随机快速不动点.pdf`，由上述 Markdown 转换生成：

```bash
cd "/Users/liluxuan/Documents/Obsidian/My_Paper/6_stochastic_acclerate/Bot-meeting/" && pandoc "261014-领域roadmap-随机快速不动点.md" -o "261014-领域roadmap-随机快速不动点.pdf" --pdf-engine=xelatex -V mainfont="Times New Roman" -V CJKmainfont="PingFang SC" -V geometry:margin=2cm -V colorlinks=true --toc
```

生成后打开 PDF 检查：中文与公式正常显示，表格没有溢出页面。表格过宽时拆成多张表。
