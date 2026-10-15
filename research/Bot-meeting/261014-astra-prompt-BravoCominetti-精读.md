# 给 Astra 的精读指令：Bravo–Cominetti 2024 随机 KM 论文详细拆解

2026-10-14

## 1. 任务

精读并逐节拆解下面这篇论文，产出一份我能对照原文自学的中文精读笔记。

- 论文：Mario Bravo, Roberto Cominetti, *Stochastic Fixed-Point Iterations for Nonexpansive Maps: Convergence and Error Bounds*, SIAM J. Control Optim., 2024, DOI 10.1137/22M1515550。
- PDF：`/Users/liluxuan/Zoterodb/storage/6PUG34I4/Bravo and Cominetti - 2024 - 2024_SIAM_Stochastic Fixed-Point Iterations for Nonexpansive Maps Convergence and Error Bounds.pdf`，共 29 页。

读者：刚进入不动点方向的优化研究者，熟悉随机梯度法、Robbins–Siegmund 引理和 Nesterov 加速的 Lyapunov 分析，对 KM 迭代和非扩张算子理论较陌生。

读完后我要能做到三件事：

1. 不看原文复述每个主要定理的假设、结论和证明主线；
2. 说清噪声在证明的哪一步进入、带什么权重、靠什么条件被控制；
3. 判断哪些结论与技巧能移植到带动量的随机 Fast KM，哪些不能。

## 2. 拆解内容

按论文结构逐节写，覆盖以下内容。

### 2.1 论文定位

用两三句话写出：论文研究什么迭代、解决什么问题、主要结论是什么。再写出它相对 Combettes–Pesquet 随机拟 Fejér 框架和经典随机逼近理论的增量。

### 2.2 设定、记号与假设

1. 写出迭代 (SKM)、噪声 $U_n$ 的定义，以及原范数与欧氏范数的区分。
2. 对假设 (H0)–(H4)、(BVAR)、(UNI) 逐条给出：公式、含义、一个满足它的例子、一个违反它的例子。
3. 画一张表，列出每个定理用到哪些假设。

### 2.3 核心工具：Theorem 2.1

1. 写出定理陈述，说明它来自 Bravo–Cominetti–Pavez-Signé 2019 的含误差 KM 估计。
2. 说明函数 $\kappa$、$\tau_n$、$\pi_{kn}$ 等量的定义与作用。
3. 说明 2.1 节的 reduction trick 如何把 (SKM) 化归到 Theorem 2.1。

### 2.4 主要定理逐个拆解

覆盖 Lemma 2.4、Theorem 2.5、Theorem 2.8、Corollary 2.9、Theorem 2.10、Theorem 2.11、Corollary 2.12、Theorem 4.1、Theorem 4.4、Corollary 4.5、Proposition 5.1、Corollary 5.4、Corollary 5.5。对每一个都写出：

1. **陈述**：用 LaTeX 写出假设与结论；
2. **结论类型**：从下面五类中标注：有限时域界、期望界、残差几乎必然趋零或几乎必然速率、迭代点几乎必然收敛、样本复杂度；
3. **证明步骤**：编号写出主线，关键不等式单独列出，并标原文公式编号；
4. **噪声处理**：噪声项的形式、权重、所需可和性（$\ell^1$ 或 $\ell^2$）、用到的鞅或概率工具；
5. **检查点**：一个我能自己验证的小问题，例如代入 $\alpha_n = 1/(n+1)^a$ 算出速率指数。

Theorem 2.5 和 Theorem 2.11 写到能逐行对照原文的程度，其余定理写清主线即可。Theorem 2.8 要与 Combettes–Pesquet 的 Corollary 2.7 对比。

### 2.5 第 3 节应用

简要写出 Q-learning 如何写成 (SKM)、Theorem 3.1 与 3.2 用了哪些一般定理、数值例子验证了什么。这一节不展开证明。

### 2.6 总表

列为：定理编号 | 假设 | 步长条件 | 结论 | 结论类型 | 速率。

### 2.7 通往随机 Fast KM 的接口

1. 论文中哪些量和不等式在加入动量后会改变；
2. 论文缺少哪一类结论，例如残差的几乎必然速率、不依赖预设迭代总数的最优速率、加速；
3. 哪些证明技巧能直接借用，哪些需要替换，并说明理由。

### 2.8 练习与疑问

1. 3–5 道推导练习，难度从代入计算到补全一个证明步骤，附简要答案；
2. 读原文时发现的疑点、记号不清或可能的笔误，标明页码与公式编号。

## 3. 写作要求

1. 中文行文，技术术语保留英文原名。
2. 所有定理、引理、公式都标原文编号与页码。原文没有写明而由你补出的推导，标「补充推导」。
3. 记号与原文保持一致；需要新记号时先说明。

## 4. 输出文件

产出两个文件，放在 `/Users/liluxuan/Documents/Obsidian/My_Paper/6_stochastic_acclerate/Bot-meeting/`：

1. **Markdown**：`261014-BravoCominetti2024-精读.md`，供 Obsidian 阅读。
   - 文件开头写 YAML front matter：`title`、`date: 2026-10-14`、`tags: [stochastic-KM, fixed-point, paper-reading]`、`source` 填 DOI。
   - 行内公式用 `$...$`；独立公式用单独成行的 `$$` 包围，前后各留一行空行。
   - 不使用 `\label`、`\eqref`、`\tag`、`aligned`、`cases` 等环境与命令；表格内公式用 `\lvert`、`\rVert` 代替竖线。
   - 用二级、三级标题组织，使 Obsidian 大纲视图可导航。
2. **PDF**：`261014-BravoCominetti2024-精读.pdf`，由上述 Markdown 转换生成，命令如下：

```bash
cd "/Users/liluxuan/Documents/Obsidian/My_Paper/6_stochastic_acclerate/Bot-meeting/" && pandoc "261014-BravoCominetti2024-精读.md" -o "261014-BravoCominetti2024-精读.pdf" --pdf-engine=xelatex -V mainfont="Times New Roman" -V CJKmainfont="PingFang SC" -V geometry:margin=2.5cm --toc
```

生成后打开 PDF 检查：中文正常显示，公式全部渲染，没有残留的美元符号或 LaTeX 源码。转换报错时修正 Markdown 后重新生成。
