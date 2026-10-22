# 给 GPT Pro 的调研指令：随机快速不动点方法的领域 roadmap

2026-10-14

使用方法：把第 1 节到第 5 节的全文粘贴到 GPT Pro 对话框，打开联网搜索。

---

## 1. 背景

我是优化方向的研究者，之前精读并讨论过 Attouch–Fadili–Kungurtsev 的随机 Ravine / Nesterov 论文（JOTA 2026）：在随机梯度噪声下，函数值误差几乎必然达到 $o(1/k^2)$，迭代点几乎必然弱收敛，工具是 Lyapunov 能量与 Robbins–Siegmund 引理。

现在我和 Radu Ioan Boţ 合作，课题为：**随机 Fast KM 与随机 Fast OGDA 的几乎必然速率。**

1. 随机 Fast KM：问题 $x = Tx$，$T$ 非扩张，算子只能带噪声地计算，$\widehat{T}_k(x) = T(x) + e_k$，$\mathbb{E}[e_k \mid \mathcal{F}_k] = 0$。确定性 Fast KM 的残差为 $o(1/k)$。
2. 随机 Fast OGDA：问题 $V(z) = 0$，$V$ 单调且 Lipschitz 连续。确定性 Fast OGDA 的残差为 $o(1/k)$。

噪声假设有两条：N2，条件方差一致有界 $\mathbb{E}[\lVert e_k\rVert^2 \mid \mathcal{F}_k] \le \sigma^2$；N6，加权噪声可和 $\sum_k s_k^2 t_k^2 \sigma_k^2 < \infty$，其中 $s_k$ 为步长，$t_k$ 为动量参数。

我已经在读的三篇：

1. Bravo, Cominetti, *Stochastic Fixed-Point Iterations for Nonexpansive Maps: Convergence and Error Bounds*, SICON 2024；
2. Yang, Jiang, Chi, Cutkosky, Xiao, *Stochastic Inertial Krasnosel'skii–Mann Iteration Achieves Near-Optimal Sample Complexity*, arXiv 2026；
3. Boţ, Nguyen, Fast Krasnosel'skii–Mann 算法，残差 $o(1/k)$。

## 2. 任务

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

## 3. 内容

### 3.1 速率总表

这是 roadmap 的主体，按 A∩B、A∩C、B∩C、A∩B∩C 分成四张表。行为方法，列为问题类、噪声模型、结论类型、速率、论文与定理编号。

A∩B 表的方法包括随机 Nesterov 的各类变体（单步长 $\alpha/k$ 型、双步长型、递增批量型），问题类为光滑凸优化。其余三张表的方法至少包括：KM、Halpern、Fast KM、惯性 KM、EAG、Fast OGDA，以及各自的随机版本。问题类区分非扩张不动点、余强制算子求零、单调 Lipschitz 算子求零。结论类型区分确定性末次迭代、随机期望界、随机几乎必然速率、迭代点几乎必然收敛、样本复杂度。

速率写成具体阶，并注明度量的是残差还是残差平方。已知下界单独列一行。尚无结果的格子标「空白」，并写明检索过的来源。

### 3.2 发展时间线

只写直接通向总表结果的节点，15–20 个。每个节点写出年份、作者、论文、结论，以及它推进了总表中的哪一格。

### 3.3 研究人员

只收录在这个窄领域有代表作的人，15–20 人。表格列为：姓名、机构、主页链接、本领域代表作两篇、研究线。研究线标注为 A∩B、A∩C、B∩C 中的一个或多个。经典人物另列一张短表，最多 8 人。

初步线索，核实后保留符合标准的人并补充遗漏：Hermant、Aujol、Dossal、Rondepierre、Salzo、Attouch、Sebbouh、Cominetti、Bravo、Contreras、Boţ、Csetnek、Dang-Khoa Nguyen、Combettes、Ernest Ryu、Donghwan Kim、TaeHo Yoon、Lieder、Diakonikolas、Tran-Dinh、Loizou、Gorbunov、Alacaoglu、Lin Xiao、Yuejie Chi、Cutkosky、Tong Yang、Yekini Shehu。

### 3.4 当前课题

5–7 个课题，每个具体到问题类、噪声模型和目标速率。每个课题写出：精确陈述、已知最好结果与定理编号、剩余空白、2024–2026 年代表论文、与我的课题的关系（直接竞争、可借用技巧，或背景）。

### 3.5 我的课题的位置

在总表中标出我的课题对应的格子。列出 3–5 篇最近邻论文，逐篇写出：它证明了什么、没证明什么、我的课题与它的区别。重点检索：**是否已有人给出随机 Fast KM 或随机 Fast OGDA 的几乎必然速率**。

## 4. 要求

1. 中文行文，人名、方法名、期刊名保留英文。
2. 每篇文献给出作者、标题、年份、期刊或会议，以及 arXiv 编号或 DOI；所有速率标定理编号。
3. 主页链接和文献都要通过联网检索确认；无法确认的标「待核实」，禁止编造。
4. 区分「论文原文结论」与「你的推断」。

## 5. 输出格式

1. 先在对话中输出完整的 Markdown 正文，用于粘贴进 Obsidian：
   - 开头写 YAML front matter：`title`、`date: 2026-10-14`、`tags: [roadmap, fixed-point, monotone-operator, stochastic]`；
   - 行内公式用 `$...$`，独立公式用单独成行的 `$$` 包围；表格内公式用 `\lVert`、`\rVert` 代替竖线；
   - 链接用 `[文字](URL)` 格式，用二级、三级标题组织。
2. 再用代码工具生成两个可下载文件：`261014-领域roadmap-随机快速不动点.md` 与 `261014-领域roadmap-随机快速不动点.pdf`。PDF 要能正常显示中文与公式，表格不溢出页面。
