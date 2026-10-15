---
title: "领域 roadmap：随机快速不动点与单调算子方法"
date: 2026-10-14
tags: [roadmap, fixed-point, monotone-operator, stochastic]
author: "Astra 调研版"
lang: zh-CN
fontsize: 10pt
papersize: a4
toc-title: "目录"
---

## 1. 课题判断

**“随机 Fast KM 与随机 Fast OGDA 的几乎必然快速率”已有直接近邻，三重交集不能整体标为尚无结果。** VR-FKM、AFP、VFOSA 和 VAPEG 已在各自假设下证明末次平方残差的 $o(k^{-2})$ 几乎必然速率，并证明迭代点几乎必然趋于解。最接近用户目标的证据为 [R16] Theorem 2、[R17] Theorem 2、[R18] Theorem 14 和 [R19] Theorem 3.2。

**值得继续的主线是：冻结 Boţ 系列原始递推，判明其随机过程是否已被上述框架覆盖，再研究有实质差异的噪声门槛。** 仅加入随机 oracle、递增 batch，或把期望分析换成 Robbins–Siegmund 引理，均不足以确认新颖性。原始 Fast KM 的旧噪声缓存、Hilbert 空间弱点极限、原始 Fast OGDA 的查询点与误差传播，是需要逐式比较的对象。

本文保留任务书的四个交集，但将 B 理解为“加速机制”，包括 Nesterov 动量、Halpern 锚点和 optimistic / past-extragradient 机制。它们有联系，但名称和更新式不能互换。有限时域的随机复杂度列在 B∩C，只有明确含同一无限轨道 a.s. 结论的随机加速结果列入 A∩B∩C。

本报告覆盖本地两份讨论材料、Zotero 的 fixed-point PDF、原论文正文、arXiv 版本记录、期刊或会议页面，以及研究者主页。检索截至 **2026-10-14**。“本次核实的最强界”仅指所列假设和输出指标下的结果，不代表全部 oracle 模型的统一最优界。

### 1.1 读表之前必须固定的指标

对不动点问题取 $V=I-T$，记 $r_k=\lVert x_k-Tx_k\rVert$；对求零问题记 $r_k=\lVert Vx_k\rVert$。表内 $r_k$ 总是**范数**，$r_k^2$ 是平方。优化目标差另记 $h_k=f(x_k)-\min f$。不同算法查询点不同时，单独注明。

- **a.s.** 是 almost surely，即概率为一的轨道性质。
- **末次迭代** 指确定索引 $k$ 的算法输出；running minimum 是此前最小残差；随机输出按另一个分布选取索引。三者不互换。
- **RMS 残差** 为 $(\mathbb E r_k^2)^{1/2}$。它控制 $\mathbb E r_k$，反方向不能直接推得。
- **oracle** 是一次随机梯度或随机算子查询。$k$ 次迭代若每次用 $b_k$ 个样本，总成本为 $N_k=\sum_{j\le k}b_j$。
- $\widetilde O$ 隐去对数因子；复杂度目标为范数不超过 $\varepsilon$，平方残差目标相应为 $\varepsilon^2$。
- **弱点极限** 是所有连续线性泛函意义下的点极限。有限维中弱、强点极限一致，无限维中需区分。

仅有 $\mathbb E r_k^2=O(k^{-2})$ 不能直接推出 $r_k=o(k^{-1})$ a.s.。同样，为每个终止时刻 $K$ 重新选择参数的定理，不能直接解释为一条无限轨道的定理。

### 1.2 问题类与噪声

**非扩张映射**满足 $\lVert Tx-Ty\rVert\le\lVert x-y\rVert$。在 Hilbert 空间中，$V=I-T$ 为 $1/2$-余强制算子。**$\beta$-余强制**指

$$
\langle Vx-Vy,x-y\rangle\ge\beta\lVert Vx-Vy\rVert^2.
$$

余强制蕴含单调与 Lipschitz 连续；反方向对一般算子不成立。因此，Fast KM 的问题类包含于单调 Lipschitz 求零问题类，但 Fast KM 的递推不等于任意 Fast OGDA 特例。[R10] Remark 2.2 已明确讨论两者更新式的差异。

下文用 N2 表示条件无偏且二阶误差有界：$\mathbb E[e_k\mid\mathcal F_k]=0$、$\mathbb E[\lVert e_k\rVert^2\mid\mathcal F_k]\le\sigma_k^2$。若只要求 $\sigma_k\le\sigma$，噪声不必消失。N6 必须同时写明权重，例如 $\sum k^2\sigma_k^2<\infty$；单独说“噪声平方可和”没有足够信息。SGC 是 strong growth condition，指随机梯度的二阶矩由真实梯度的平方控制，因而噪声随最优性残差消失。

## 2. 四张速率总表

### 2.1 A∩B：光滑凸优化中的随机动量

本表均考察光滑凸目标；Salzo 的复合目标定理在正则项取零时属于该类。**阻尼系数 $1-\alpha/k$ 与梯度步长 $\alpha/k$ 是两个不同参数。** 此处先记录原文能确认的参数族，不把所有随机 Nesterov 变体归于一个速率。

**条件表。** 与下方速率表按方法名称对应。

| 方法 | 问题类 | 噪声与参数 |
|---|---|---|
| SNAG，固定动量 | 光滑凸，有限维 | N2/原文 ABC 二阶矩；步长 $\Theta(k^{-2/3-\delta})$ |
| SNAG，双步长、多序列 | 光滑凸有限和 | SGC；按定理选两组参数 |
| SNAG，$1-\alpha/k$ 阻尼 | 光滑凸，Hilbert | 常梯度步长；$\alpha>3$；$\sum k^2\sigma_k^2<\infty$ |
| 同一 SNAG，点极限 | 光滑凸，可分 Hilbert | 上行并加强为 $\sum k\sigma_k<\infty$ |
| stochastic Ravine | 光滑凸，可分 Hilbert | $\alpha>3$；常步长；$\sum k\sigma_k<\infty$ |
| 上述 SNAG，递增批量 | 光滑凸 | 独立样本方差有界；$b_k\asymp k^{3+\delta}$ |
| stochastic FISTA | 光滑凸特例，Hilbert | 有界条件方差；$t_k\asymp k$；$\gamma_k\asymp k^{-3/2}(\log k)^{-r}$，$r>1/2$ |
| SHB-IMA，参照线 | 光滑凸随机优化 | 原文平滑/二阶矩条件；$\eta_k\asymp k^{-1/2-\delta}$ |

**速率表。**

| 方法 | 结论类型 | 速率或极限 | 论文与定理 |
|---|---|---|---|
| SNAG，固定动量 | 末次 a.s.；点 a.s. 极限 | $h_k=O(k^{-1/3+\delta})$，$0<\delta<1/3$ | [R3] Thm. 5 |
| SNAG，双步长、多序列 | 末次期望；末次 a.s. | $\mathbb E h_k=O(k^{-2})$；$h_k=o(k^{-2})$ a.s. | [R4] Thms. 3–4 |
| SNAG，$1-\alpha/k$ 阻尼 | 末次 a.s. | $h_k=o(k^{-2})$ | [R5] Thm. 3.1(ii) 专门化 |
| 同一 SNAG，点极限 | 点 a.s. 弱极限 | 点趋于最优解；目标差仍 $o(k^{-2})$ | [R5] Thm. 3.1(iii) |
| stochastic Ravine | 末次 a.s.；点 a.s. 弱极限 | $h_k=o(k^{-2})$ | [R5] Cor. 4.1 |
| 上述 SNAG，递增批量 | 末次 a.s. 目标差 | $h_k=o(k^{-2})$；$N_k=\Theta(k^{4+\delta})$ | [R5] Thm. 3.1(ii) 的批量推论 |
| stochastic FISTA | 末次期望；点 a.s. 弱极限 | $\mathbb E h_k=O((\log k)^r/\sqrt{k})$ | [R6] Thm. 3.10、Rem. 3.11 |
| SHB-IMA，参照线 | 末次 a.s.；点 a.s. 极限 | $h_k=o(k^{-1/2+\delta})$ | [R2] Thm. 13、Cor. 17 |

**条件说明。** [R5] 的一般权重为 $\sum s_k^2t_k^2\sigma_k^2<\infty$，大 O 到小 o 还需要加强的外推参数条件；上表取 $t_k\asymp k$、常步长。点极限定理采用更强的加权一阶可和条件，不能只凭目标值速率补上点极限。对于批量实现，$b_k\asymp k^{3+\delta}$ 保证前一平方可和条件；若套用 $\sum k\sigma_k<\infty$，足够的幂次是 $b_k\asymp k^{4+\delta}$。

[R4] 使用 SGC，不能宣称持续加性方差下仍有相同结果。[R2] 是 heavy-ball 参照，不把它记为 Nesterov 定理。Salzo 的结果支持无限轨道的点极限，但表中列出的速率是期望目标差，不能写成 a.s. $o(k^{-2})$。

**梯度步长恰为 $\alpha/k$ 的格子：空白，待核实。** 本次核查 [R2]–[R6]、本地随机 Nesterov 笔记及 arXiv 线索后，未确认适用于“任意光滑凸目标、持续 N2、原始指定 Nesterov 递推”的统一多项式末次 a.s. 速率。该标记仅表示本报告未确认，不能据此声称不存在研究。

### 2.2 A∩C：随机 KM、Halpern 与轨道理论

**条件表。** 与下方速率表按方法名称对应。

| 方法 | 问题类 | 噪声与参数 |
|---|---|---|
| stochastic KM | 非扩张；Hilbert | $\sum\lambda_k(\mathbb E_k\lVert e_k\rVert^2)^{1/2}<\infty$；$\sum\lambda_k(1-\lambda_k)=\infty$ |
| stochastic KM | 非扩张；有限维一般范数 | 鞅差；原文噪声、步长条件 |
| stochastic KM | 同上 | 有界方差；$\lambda_k\asymp k^{-2/3}$ |
| stochastic KM | Euclidean 非扩张 | 已知 $K$；常步长约 $K^{-1/2}$ |
| stochastic KM | 可分 Hilbert；随机映射非扩张等原文结构 | 仅一个解处有限方差；RM 步长 |
| 同上，running minimum | 同上 | $\lambda_k\asymp k^{-a}$，$1/2<a<1$ |
| 同上，末次期望 | 同上 | $a=2/3$；原文矩条件 |
| stochastic Halpern | 非扩张；有限维一般范数 | 累积加权误差受控；递增批量 |
| stochastic Halpern | 同上；点极限另需光滑范数 | $\sum\mathbb E\lVert U_k\rVert<\infty$ |

**速率表。**

| 方法 | 结论类型 | 速率或极限 | 论文与定理 |
|---|---|---|---|
| stochastic KM | 点 a.s. 弱极限 | $x_k$ 趋于固定点；不提供通用数值阶 | [R1] Cor. 2.7 |
| stochastic KM | 点 a.s. 极限 | 固定点极限 | [R7] Thms. 2.5、2.8 |
| stochastic KM | 末次期望范数 | $\mathbb E r_k=O(\log k/k^{1/6})$ | [R7] Thm. 4.4 |
| stochastic KM | 随机输出期望范数 | $O(K^{-1/4})$；$O(\varepsilon^{-4})$ 样本 | [R7] Cor. 5.4 |
| stochastic KM | 末次残差 a.s.；点 a.s. 弱极限 | $r_k\to0$ | [R8] Thm. 2.13 |
| 同上，running minimum | 最佳历史点 a.s. | $\min_{j\le k}r_j=o(k^{-(1-a)/2})$ | [R8] Cor. 2.12 |
| 同上，末次期望 | 末次期望范数 | $O(\sqrt{\log k}/k^{1/6})$ | [R8] Thm. 2.11、Cor. 2.12 |
| stochastic Halpern | 末次期望范数 | $\widetilde O(k^{-1})$；批量方案 $\widetilde O(\varepsilon^{-5})$ | [R9] Thm. 3.3、Cor. 3.5 |
| stochastic Halpern | 残差 a.s.；点 a.s. 极限 | $r_k\to0$；该定理未给 $o(k^{-1})$ a.s. | [R9] Thm. 3.10 |

[R8] Corollary 2.12 同时列出随机输出、running minimum 与末次期望界；表中按三种不同输出分列。[R1] Corollary 2.7 允许有偏误差，但采用加权条件标准差可和；不能把它写成仅需条件方差有界。[R8] 也不是仅把任意 oracle 的统一方差界替换成“解处方差有限”：随机映射的结构假设仍须满足。

Halpern 属于锚点加速。本表强调其轨道极限，下一表补充它的确定性速率及有限精度随机复杂度。因此，同一种方法可以出现在不同交集，但每行证明的性质不同。

### 2.3 B∩C：确定性快速率与随机样本复杂度

**条件表。** 与下方速率表按方法名称对应。

| 方法 | 问题类 | 噪声与参数 |
|---|---|---|
| KM | 非扩张；有界轨道；一般范数 | 无噪声；松弛远离 0、1 |
| Halpern | 非扩张；Hilbert | 无噪声；经典锚点权重 |
| Fast KM | $\theta$-averaged，含 $\theta=1$ 非扩张；Hilbert | 无噪声；$\alpha>2$，$0<s\le1/\theta$ |
| generalized Fast KM | 非扩张；Hilbert | 无噪声；原文 overrelaxation 参数 |
| EAG-C / EAG-V | 单调 Lipschitz；有限维 | 无噪声；原文步长 |
| G-EAG | 单调 Lipschitz；Hilbert | 无噪声；衰减 Tikhonov 锚点 |
| Fast OGDA | 单调 $L$-Lipschitz；Hilbert | 无噪声；$\alpha>2$，$0<s<1/(2L)$ |
| VR-Halpern | 余强制及单调 Lipschitz | 无偏方差界；同样本多点差分、VR 结构 |
| stochastic iKM | 非扩张；实 Hilbert 空间 | N2，可加受控有偏项；预设 $K$ |
| stochastic Dual-OHM | 期望余强制 / 平方非扩张 | 常批量 $B$；预设 $N$ |
| dual-anchor + 内层近似 | 单调 Lipschitz 求零 | 样本算子单调、Lipschitz；N2 |
| anytime stochastic anchoring | 单调 Lipschitz；约束问题亦可 | 一次新样本；原文二阶矩结构 |
| 同上，VR 版本 | 同上 | 每步两个样本；同样本多点访问 |
| VR-GHAL | 非扩张；适当 Banach 几何 | 样本映射非扩张；N2 |

**速率表。**

| 方法 | 结论类型 | 速率或极限 | 论文与定理 |
|---|---|---|---|
| KM | 确定性末次范数 | $O(k^{-1/2})$ | [R11] Thm. 1.1 无误差特例 |
| Halpern | 确定性末次范数 | $r_k\le2\lVert x_0-x_*\rVert/(k+1)$ | [R12] Thm. 2.1 |
| Fast KM | 确定性末次；弱点极限 | $r_k=o(k^{-1})$ | [R10] Thms. 3.4–3.5 |
| generalized Fast KM | 确定性末次；弱点极限 | $\alpha=2$ 为 $O(k^{-1})$；$\alpha>2$ 为 $o(k^{-1})$ | [R15] Thm. 2 |
| EAG-C / EAG-V | 确定性末次 | $r_k^2=O(k^{-2})$ | [R13] Thms. 1–2；§2.3 的算子推广 |
| G-EAG | 确定性末次；强点极限 | $r_k=O(k^{-1})$；最小范数解 | [R14] Thm. 2.4、Cor. 2.6 |
| Fast OGDA | 确定性末次；弱点极限 | $r_k=o(k^{-1})$ | [R20] Thms. 16–17 |
| VR-Halpern | 有限精度末次期望 | $\mathbb E r_k\le C/k+C'\varepsilon$；$O(\varepsilon^{-3})$ oracle | [R21] Thm. 3.1、Cor. 3.4、Thm. 4.1 |
| stochastic iKM | 末次 RMS；样本复杂度 | 无偏时 $O(K^{-1}+\sigma\log K/\sqrt K)$；$\widetilde O(\varepsilon^{-2})$ | [R22] Thm. 1 |
| stochastic Dual-OHM | 末次平方残差期望 | $O(N^{-2}+\sigma^2/B)$；$O(\varepsilon^{-3})$ oracle | [R23] Thm. 4.1 |
| dual-anchor + 内层近似 | 末次期望；样本复杂度 | 近最优 $\widetilde O(\varepsilon^{-2})$ | [R24] Cor. 3.6 |
| anytime stochastic anchoring | 末次期望范数 | $O(k^{-1/4})$ | [R25] Thm. 2.1、Cor. 2.3 |
| 同上，VR 版本 | 末次期望范数 | $O(k^{-1/2})$ | [R25] Thm. 3.2 |
| VR-GHAL | anytime 高概率残差 | $\widetilde O(\varepsilon^{-2})$ oracle | [R26] Thm. 1、Cor. 3 |

**表中若干边界。** [R22] 每步一次新 oracle 调用，但参数依赖总时域；Appendix A Proposition 1 证明的确定性 Fast KM 等价参数与主定理的参数选择不同。[R23] 的批量在一次运行内不增加，但随目标精度取 $B=\Theta(\varepsilon^{-2})$；不能说固定一个 $B$ 后无限运行得到零残差。[R24] 包含内层 resolvent 近似，不能称为原始 Fast OGDA 的一步随机化。[R25] 在约束情形采用梯度映射或原文残差；只有集合值部分为零时才能直接记成 $\lVert Vx_k\rVert$。

[R26] 的 $\widetilde O(\varepsilon^{-2})$ 使用样本映射非扩张结构。只有 N2 时，其 Corollary 1 给出一般范数模型下更昂贵的复杂度；不能去掉结构假设后保留相同指数。高概率且对时域一致的定理，也不自动给出原始 Fast KM 的 a.s. 小 o 速率和点极限。

### 2.4 A∩B∩C：已有随机快速轨道结果与用户目标格子

**条件表。** 与下方速率表按方法名称对应。

| 方法 | 问题类 | 噪声与参数 |
|---|---|---|
| VR-FKM | 有限和余强制型；有限维 | 分量平均余强制型条件；SVRG / SAGA |
| AFP | 余强制 / 非扩张；有限维 | 递推误差条件；允许有偏与延迟；$\sum\delta_k<\infty$ |
| AFP，一般随机 oracle | 同上 | N2；$b_k\gtrsim k^{3+\omega}$，$\omega>0$ |
| VFOSA | 单调复合包含的原文特例；有限维 | 余强制型结构、VR 误差递推及可和尾项 |
| VAPEG，旧称 VFOG | 单调 Lipschitz 求零特例；有限维 | 一般误差条件 (15)；可和尾项；递增 batch 可实现 |
| stochastic Fast OGDA 动力系统 | 单调算子；Hilbert | 连续时间扩散；$\int s^2\lVert\sigma_Z(s)\rVert_{HS}^2ds<\infty$ |
| **用户目标：原始 Fast KM** | 非扩张 / 余强制；Hilbert | 缓存旧 oracle；先 N6，再判定 N2 下可行目标 |
| **用户目标：原始 Fast OGDA** | 单调 Lipschitz；Hilbert | 原始查询点、缓存方式及噪声模型必须固定 |

**速率表。**

| 方法 | 结论类型 | 速率或极限 | 论文与定理 |
|---|---|---|---|
| VR-FKM | 末次期望；末次 a.s.；点 a.s. 极限 | $\mathbb E r_k^2=o(k^{-2})$；$r_k=o(k^{-1})$ a.s. | [R16] Thms. 1–2；Cors. 1–2 |
| AFP | 查询点残差 a.s.；点 a.s. 极限 | $\lVert Gy_k\rVert=o(k^{-1})$ a.s. | [R17] Thm. 2 |
| AFP，一般随机 oracle | a.s. 快速率；期望复杂度 | 范数 $o(k^{-1})$ a.s.；$O(\varepsilon^{-4-\omega})$ oracle | [R17] Thm. 2、Cor. 2 |
| VFOSA | FBS 残差 a.s.；点 a.s. 极限 | $\lVert\mathcal G_\lambda x_k\rVert=o(k^{-1})$ a.s. | [R18] Thms. 12–14 |
| VAPEG，旧称 VFOG | 末次残差 a.s.；点 a.s. 极限 | $\lVert Gx_k\rVert=o(k^{-1})$ a.s. | [R19] Thm. 3.2；Cor. 3.4 |
| stochastic Fast OGDA 动力系统 | 轨道 a.s.；弱点极限 | $\lVert VZ(s)\rVert=o(s^{-1})$ a.s. | [R27] Thm. 3.5 |
| **用户目标：原始 Fast KM** | 同一无限轨道；末次 a.s. 与弱点极限 | 目标 $o(k^{-1})$；**宽泛结论已有，原始随机递推覆盖待验证** | 对比 [R10]、[R16]、[R17]、[R22] |
| **用户目标：原始 Fast OGDA** | 同一无限轨道；末次 a.s. 与弱点极限 | 目标 $o(k^{-1})$；**宽泛结论已有，原始随机递推覆盖待验证** | 对比 [R19]、[R20]、[R27] |

VFOSA 的残差是 forward-backward splitting 残差。它包含 resolvent，不能对一般复合包含直接替换成 $\lVert Vx_k\rVert$。VAPEG 取集合值算子为零、单调参数为零，即得到本任务允许的单调 Lipschitz 求零特例；本文不展开其非单调部分。

AFP 的“查询点” $y_k$ 具有明示快速率，三个序列的点极限另由定理给出。不要只因为 $x_k$ 与 $y_k$ 有同一极限，就自动把 $o(k^{-1})$ 残差率转移到 $x_k$。

**本交集未填写无文献依据的“空白”。** 真正未解决的是覆盖判定及假设边界。本次已查本地笔记、Zotero、arXiv、期刊正文、作者主页和这些文献的相关工作部分；该范围仍不构成不存在其他定理的证明。

### 2.5 下界与比较规则

| 下界 | 适用模型 | 含义与限制 | 证据 |
|---|---|---|---|
| 范数残差 $\Omega(1/K)$ | 确定性非扩张不动点；原文 oracle 类与维度条件 | Halpern 的最坏情形阶已最优 | [R28] Thm. 4.6 |
| 平方残差 $\Omega(1/K^2)$ | 光滑凸凹、相应一阶 oracle 类 | 与 EAG 的 $O(K^{-2})$ 平方率配对 | [R13] Thm. 3、Cor. 3 |
| 随机样本 $\Omega(\sigma^2\varepsilon^{-2})$ | 含带噪均值估计的 Hilbert 求零子类 | 仅说明噪声项的精度指数；不统一覆盖一般范数 | [R22] 下界讨论；简约子类见下文 |
| 随机样本 $\Omega(\varepsilon^{-3})$ | [R9] 规定的平均化算法、batching 和一般范数模型 | 不能用于否定 Hilbert 中更强 oracle 的二次方复杂度 | [R9] Thm. 3.7 |

第一、二行的最坏情形允许困难实例随 $K$ 改变。Fast KM 的 $o(1/k)$ 是每个固定实例沿无限轨道的渐近结论，两者没有逻辑冲突。

第三行可由 $V_\mu(x)=x-\mu$、oracle $V_\mu(x)+\xi$ 的高斯均值估计子问题解释：一次查询等价于获得一个关于 $\mu$ 的带噪样本；要令均方残差不超过 $\varepsilon^2$，至少需要常数倍 $\sigma^2/\varepsilon^2$ 个样本。这里是对子类的标准下界归约，未将它冒充 [R22] 的有编号定理。

2026 年还存在 [R29] 的 Hilbert 归约与 [R30] 的一般范数 oracle 复杂度研究。它们提示**空间几何与 oracle 访问方式会改变下界**。[R30] 本次已确认元数据，未完成正文定理核验；其数值界不纳入总表。

## 3. 直接相关的发展时间线

以下 18 个节点按首次相关成果出现的年份组织；预印本年份与正式出版年份不同的，均予以注明。

| 年份 | 作者与论文 | 推进的结果及总表位置 |
|---|---|---|
| 2015 | Combettes–Pesquet，[R1] | 随机拟 Fejér 框架；随机 KM 的 a.s. 弱点极限，A∩C 的基础 |
| 2015 | Boţ–Csetnek–Hendrich，[R35] | 惯性不动点与 Douglas–Rachford 结构，为 B∩C 提供递推与点极限工具 |
| 2017 | Bravo–Cominetti–Pavez-Signé，[R11] | 不精确 KM 的显式残差误差界，连接误差累积与 A∩C |
| 2020–2021 | Lieder，[R12] | Halpern 的精确 $O(k^{-1})$ 范数界；2020 online、2021 卷期 |
| 2021 | Sebbouh–Gower–Defazio，[R2] | SHB 末次 a.s. 目标差与点极限，A∩B 的参照线 |
| 2021 | Yoon–Ryu，[R13] | EAG 把单调 Lipschitz 末次平方残差推进到 $O(k^{-2})$，B∩C |
| 2022 | Liu–Yuan，[R3] | SGD、SHB、SNAG 的统一 a.s. 分析；一般凸末次目标差结果，A∩B |
| 2022 | Park–Ryu，[R28] | 非扩张不动点的加速复杂度和匹配下界，B∩C |
| 2022 | Cai–Song–Guzmán–Diakonikolas，[R21] | 随机 Halpern 结合递归 VR，有限精度 oracle 成本 $O(\varepsilon^{-3})$，B∩C |
| 2022–2023 | Boţ–Nguyen，[R10] | Fast KM；2022 预印本、2023 SINA，$o(k^{-1})$ 残差及弱点极限 |
| 2022–2025 | Boţ–Csetnek–Nguyen，[R20] | Fast OGDA；2023 online、2025 FoCM 卷期，单调 Lipschitz 的 $o(k^{-1})$ |
| 2024 | Bravo–Cominetti，[R7] | 随机 KM 的 a.s. 点极限与可比较的期望误差界，A∩C |
| 2024–2026 | Tran-Dinh，[R16] | VR-FKM；本报告使用 2026 v4，其中含 a.s. 小 o 与点极限，三重交集 |
| 2025 | Hermant 等，[R4] | SGC 下随机 Nesterov 的加速及 a.s. 小 o 目标差，A∩B |
| 2025–2026 | Tran-Dinh、Nguyen-Trung，[R17]–[R19] | AFP、VFOSA、VAPEG 把随机快速轨道理论推进到更广 oracle 和算子结构 |
| 2025–2026 | Salzo，[R6]；Attouch–Fadili–Kungurtsev，[R5] | FISTA 的随机点极限；Ravine 的误差权重、快速目标差与点极限，A∩B |
| 2026 | Boţ–Chenchene，[R14]；Boţ–Chenchene–Fadili，[R15]；Boţ–Schindler，[R27] | 强点极限、广义 Fast KM、随机连续时间 Fast OGDA，明确离散与连续边界 |
| 2026 | Cortild–Cartis–Peypouquet，[R8]；Yang 等，[R22]；Yoon–Loizou，[R23]–[R24]；Kim–Alacaoglu，[R25]；Diakonikolas，[R26] | 解处方差、近最优样本复杂度、anytime 和高概率结果共同细化前沿；彼此 oracle 模型不相同 |

## 4. 研究人员与主页

### 4.1 当前代表研究者

选取 18 位与上述窄领域直接相关、能列出两篇代表作的研究者。文献编号对应第 8 节完整书目。所有下列链接均在 **2026-10-14 实际访问**。官方个人介绍页也可作为身份入口，但研究组名单不能冒充独立个人主页。

| 姓名 | 机构及核验状态 | 主页 | 代表作两篇 | 研究线 |
|---|---|---|---|---|
| Radu Ioan Boţ | University of Vienna | [个人主页](https://www.mat.univie.ac.at/~rabot/)，已访问 | Fast KM [R10]；Fast OGDA [R20] | B∩C；A∩B∩C |
| Ernö Robert Csetnek | University of Vienna | [个人主页](https://www.mat.univie.ac.at/~csercser/index.htm)，已访问 | 惯性 DR [R35]；Fast OGDA [R20] | B∩C |
| Dang-Khoa Nguyen | 原论文署名 Vienna；当前机构待核实 | [官方组员记录](https://www.mat.univie.ac.at/~rabot/group.html)，已访问；个人主页待核实 | Fast KM [R10]；Fast OGDA [R20] | B∩C |
| Enis Chenchene | 2026 论文署名 Vienna；当前机构待核实 | [官方组员记录](https://www.mat.univie.ac.at/~rabot/group.html)，已访问；个人主页待核实 | G-EAG [R14]；广义 Fast KM [R15] | B∩C |
| Jalal Fadili | ENSICAEN / GREYC | [个人主页](https://fadili.users.greyc.fr/)，已访问 | stochastic Ravine [R5]；广义 Fast KM [R15] | A∩B；B∩C |
| Quoc Tran-Dinh | UNC Chapel Hill | [个人主页](https://quoctd.web.unc.edu/)，已访问 | VR-FKM [R16]；VFOSA [R18] | A∩B∩C |
| Nghia Nguyen-Trung | UNC Chapel Hill，PhD candidate | [个人主页](https://nghiant01.github.io/)，已访问 | AFP [R17]；VAPEG [R19] | A∩B∩C |
| Ernest K. Ryu | UCLA；主页列示休假期间在 OpenAI | [个人主页](https://ernestryu.com/)，已访问 | EAG [R13]；精确最优不动点复杂度 [R28] | B∩C |
| TaeHo Yoon | Johns Hopkins University，Assistant Research Scientist | [个人 CV](https://tetrzim.github.io/CV/)，已访问 | EAG [R13]；直接随机 dual-anchor [R23] | B∩C |
| Nicolas Loizou | Johns Hopkins University | [个人主页](https://nicolasloizou.github.io/index.html)，已访问 | 直接随机 dual-anchor [R23]；近最优 dual-anchor [R24] | B∩C |
| Mario Bravo | Universidad de Santiago de Chile | [个人主页](https://sites.google.com/site/mbravogon/)，已访问 | stochastic KM [R7]；stochastic Halpern [R9] | A∩C |
| Roberto Cominetti | Universidad Adolfo Ibáñez | [官方个人页](https://www.uai.cl/profesores/ingenieria-y-ciencias/roberto-cominetti)，已访问 | 不精确 KM [R11]；stochastic KM [R7] | A∩C |
| Juan Pablo Contreras | Universidad Diego Portales | [官方个人页](https://citylog.udp.cl/persona/juan-pablo-contreras/)，已访问 | 最优一般范数不动点误差界 [R32]；stochastic Halpern [R9] | A∩C；B∩C |
| Patrick L. Combettes | North Carolina State University | [个人主页](https://pcombet.math.ncsu.edu/)，已访问 | 随机拟 Fejér I [R1]；II [R31] | A∩C |
| Jean-Christophe Pesquet | CentraleSupélec / Université Paris-Saclay | [主页及履历](https://jc.pesquet.eu/biography/)，已访问 | 随机拟 Fejér I [R1]；II [R31] | A∩C |
| Jelena Diakonikolas | University of Wisconsin–Madison | [个人主页](https://www.jelena-diakonikolas.com/)，已访问 | VR-Halpern [R21]；高概率不动点 [R26] | A∩C；B∩C |
| Saverio Salzo | Sapienza Università di Roma | [官方个人页](https://www.open.diag.uniroma1.it/users/saverio_salzo)，已访问 | stochastic FISTA [R6]；不精确加速 proximal point [R33] | A∩B |
| Ahmet Alacaoglu | University of British Columbia | [个人主页](https://ahmetalacaoglu.github.io/)，已访问 | stochastic VR for VI [R34]；anytime 末次界 [R25] | B∩C |

**人员核验中的修正。** 任务线索里的 “Baptiste Hermant” 应为 **Julien Hermant**。[个人主页](https://j-hermant.github.io/) 于 2026-10-14 已访问，列示 University of Bordeaux 博士生。他与 Marien Renaud、Jean-François Aujol、Charles Dossal、Aude Rondepierre 的 [R4] 是 A∩B 的直接入口。本表未为满足“两篇”要求把未核实作品加入其名下。Dang-Khoa Nguyen 与 Enis Chenchene 在 Boţ 组页列于 former members；因此不把旧署名当成当前任职。Ernest K. Ryu 的主页已是 UCLA / OpenAI 信息，不能沿用旧 SNU 任职。

### 4.2 经典基础人物

| 人物 | 与本领域直接相关的贡献 |
|---|---|
| M. A. Krasnosel’skiĭ、W. R. Mann | 松弛不动点迭代，是 KM 系列的基础；两人合列一行 |
| Benjamin Halpern | 锚点不动点迭代，支撑固定点选择和快速残差研究 |
| Yurii Nesterov | 加速动量及估计序列，支撑 A∩B 和 Fast KM 的方法来源 |
| Boris T. Polyak | heavy-ball 与随机逼近背景；不能与 Nesterov 更新式混同 |
| Herbert Robbins、David Siegmund | 非负近超鞅工具，支撑轨道极限和误差可和分析；两人合列一行 |
| Hedy Attouch | 加速动力系统、消失阻尼、渐近速率与点极限；本报告直接对应 [R5] |

此表共 8 人；只作方法来源说明，不用于填充当前研究者名额。

## 5. 六个可检验的当前课题

以下均是**候选研究问题**。除已引用定理与第 7 节的诊断推导外，本次没有证明新的算法速率。先做第一个课题的覆盖判定，再决定是否进入证明阶段。

### 5.1 原始 Fast KM 的随机等价性与误差条件

**问题。** 在可分 Hilbert 空间中固定 [R10] 的 Fast KM，取 $g_k=Vx_k+e_k$，每步只产生一个新估计并缓存 $g_{k-1}$。N2 下要求 $\sum k^2\sigma_k^2<\infty$。目标是末次 $r_k=o(k^{-1})$ a.s.，同时有 a.s. 弱点极限。

**已知最好近邻。** [R16] Theorem 2 在有限和结构下给出同阶 a.s. 结果；[R17] Theorem 2 在有限维一般误差框架下给出同阶查询点残差及点极限。其典型无延迟误差特例已容纳 $\sum k^2\sigma_k^2<\infty$。[R22] Appendix A Proposition 1 给出确定性 Fast KM 与特定 iKM 参数的联系。

**剩余判定。** 必须核对 AFP 消元后是否得到同一随机递推，包含初值、查询点、缓存误差和全部系数。若完全相同且所需假设已包含，有限维目标属于已有定理的推论。Hilbert 版本还需判断是常规弱极限论证还是实际技术障碍；不能仅凭维度变化确认贡献。

2024–2026 代表文献为 [R16]、[R17]、[R22]。与用户课题关系为**直接竞争**。适合把它作为第一阶段的覆盖审计与证明复现，不宜预先作为新颖性承诺。

### 5.2 在明确尾部假设下减少 Fast KM 的批量增长

**问题。** 保持 5.1 的原始递推。将“仅有条件二阶矩”换成明确的轻尾假设，例如有限维条件次高斯误差，或有界样本平均并具有相应浓度界。尝试在 $\sigma_k^2=O(k^{-q})$、$2<q\le3$ 下证明 $r_k=o(k^{-1})$ a.s. 与点极限。

**已知最好近邻。** [R17] Theorem 2、[R19] Theorem 3.2 的可和二阶误差框架通常可用 $q>3$ 实现。[R26] 的高概率工具表明尾部控制与 oracle 结构可以改变复杂度，但其算法并非原始 Fast KM。

**剩余问题。** 新噪声本身满足 $k e_k\to0$ 只是必要诊断，不能替代对历史累积的控制。第 7 节说明：仅有二阶矩时，$2<q\le3$ 的统一 a.s. 小 o 目标会失败。轻尾假设必须写入定理，不能在证明中隐含使用。

2024–2026 代表文献为 [R16]、[R17]、[R26]。关系为**条件化的直接候选课题**。若对应 $b_k\asymp k^q$，总样本为 $\Theta(K^{q+1})$；只有证明成立后才能把减少的批量写成贡献。

### 5.3 原始 Fast OGDA 的噪声相关性

**问题。** 对单调 $L$-Lipschitz 算子，按 [R20] Algorithm 2 固定预测点与更新点，并明确同一样本重用、独立重采样或缓存上一估计的选择。先在 N6 下检验 $\lVert Vx_k\rVert=o(k^{-1})$ a.s. 与 a.s. 弱点极限。

**已知最好近邻。** [R19] Theorem 3.2 已在有限维给出单调 Lipschitz 特例的同阶结论。[R27] Theorem 3.5 已给出对应连续时间随机动力系统的 a.s. 快速率与弱点极限。

**剩余问题。** 原始 Fast OGDA 与 VAPEG 是否只是变量重写，必须逐式验证。预测点依赖当前样本时，不能把该点的 oracle 误差直接视为条件无偏。若递推不同，仍须说明这种差异带来了什么可证明好处；不同名称不是理论增量。

2024–2026 代表文献为 [R19]、[R20]、[R27]。关系为**直接竞争**。建议在 Fast KM 阶段完成后推进，避免两个不确定证明同时展开。

### 5.4 持续 N2 下的单一 anytime 惯性轨道

**问题。** 非扩张不动点，条件无偏且方差有界，不预知终止时刻，每步一个新 oracle。目标先设为 $r_k\to0$ a.s. 和点极限，再寻找与 oracle 成本兼容的末次幂次率；不预设 $o(k^{-1})$。

**已知最好近邻。** [R22] Theorem 1 有预设时域的 $\widetilde O(K^{-1/2})$ RMS 残差。[R8] Theorem 2.13 给随机 KM 的无限轨道弱点极限。[R25] Theorem 2.1 有 anytime 末次期望 $O(k^{-1/4})$，多点 VR 下 Theorem 3.2 为 $O(k^{-1/2})$。

**剩余问题。** 不能只把固定时域参数中的 $K$ 替换成 $k$。新 schedule 必须重新证明漂移与轨道性质。候选 a.s. 速率应从真实误差权重导出，不能把期望界直接附上 a.s. 标签。

2024–2026 代表文献为 [R8]、[R22]、[R25]。关系为**可借用技巧的后续方向**，不是原始常步长 Fast KM 的直接推论。

### 5.5 从 SGC 到算子相对噪声条件

**问题。** 余强制求零，条件无偏误差满足 $\mathbb E_k\lVert e_k\rVert^2\le c\lVert Vx_k\rVert^2$。在无需预设递增 batch 的条件下，检验原始 Fast KM 或最小参数调整能否同时达到 $o(k^{-1})$ a.s. 与点极限。

**已知最好近邻。** [R4] Theorem 4 在梯度问题的 SGC 下给出 $h_k=o(k^{-2})$ a.s.。[R16] Theorem 2 已用有限和 VR 实现算子快速率；[R8] 说明解处方差模型值得单独分析。

**剩余问题。** 梯度有目标函数，普通余强制算子没有该势函数。相对噪声项能否由同一 Lyapunov 的负漂移吸收，是具体证明问题。相对噪声的常数阈值、是否隐含插值结构、以及是否已落入 [R16] 的估计器类，都必须验证。

2024–2026 代表文献为 [R4]、[R8]、[R16]。关系为**从用户随机 Nesterov 背景迁移的候选机制**，目前不声明新颖性成立。

### 5.6 快速残差与强点极限的兼容性

**问题。** 非扩张或单调 Lipschitz 问题，使用预定锚点与 N6 噪声，希望 $r_k=O(k^{-1})$ a.s.，并强趋于指定投影解。必须说明锚点与噪声权重的精确关系。

**已知最好近邻。** 确定性 [R14] Theorem 2.4、Corollary 2.6 实现强点极限和 $O(k^{-1})$ 残差。[R9] Theorem 3.10 在有限维光滑范数下给随机 Halpern 点极限；[R17] 和 [R19] 的快速随机点极限不等于指定解选择。

**剩余问题。** 证明同一无限维随机轨道强趋于选定解，同时不牺牲声明的残差阶。应先查 G-EAG 的不精确版本以及随机 Tikhonov 文献，避免把弱到强的变化直接当作缺口。

2024–2026 代表文献为 [R9]、[R14]、[R17]。关系为**背景及可借用技巧**。它改变了用户最初的算法，不列为当前主线。

## 6. 用户课题的五篇最近邻

### 6.1 VR-FKM：最直接的有限和竞争者

[R16] 是 Tran-Dinh 单作者预印本，首稿 2024，本报告使用 **arXiv:2406.02413v4，2026-09-09**。Theorem 2 已证明 $k^2\lVert Gx_k\rVert^2\to0$ a.s.、相邻点差的同阶小 o 和迭代点 a.s. 趋于解。SVRG / SAGA 实例的样本复杂度为 $O(n+n^{2/3}\varepsilon^{-1})$。

它依赖有限和及分量平均的余强制型关系，不能只凭“均值算子余强制”就套用。用户若研究一般流式 oracle，需要进一步对比 AFP。其 PDF 使用 Mathematics of Operations Research 模板，**模板不表示正式录用**；本报告仍记预印本。

### 6.2 AFP：一般随机 oracle 下更接近 N6 的覆盖者

[R17] 的 Theorem 2 直接处理递推误差条件，Corollary 2 包含一般无偏随机 oracle 的递增 batch 实现。零延迟、无递归误差项时，其充分条件可覆盖加权平方可和情形。因此，“从有限和推广到一般随机 oracle”不能直接作为用户课题的贡献。

它在查询点 $y_k$ 证明快速残差，三个迭代序列有 a.s. 点极限。当前尚未完成与原始 Fast KM 的完整消元等价证明。需要比较全部系数及初始化，不能只比较图示或动量项外观。文章明示在有限维工作，并提及向 Hilbert 推广的可能性；Hilbert 本身不是充分的新颖性证据。

### 6.3 VAPEG：Fast OGDA 方向的直接近邻

[R19] 的首稿标题含 VFOG。**本报告采用 arXiv:2508.16791v2，2026-09-09，标题为 New Accelerated Past-Extragradient Methods with Variance Reduction for Generalized Equations。** 方法名为 VAPEG，a.s. 定理为 Theorem 3.2。

取集合值部分为零、单调特例后，该定理给出原始点和前一查询点的残差范数 $o(k^{-1})$ a.s.，并有点极限。Corollary 3.4 的 $b_k\asymp k^{3+\nu}$ 实现给出 $O(\varepsilon^{-4-\nu})$ oracle 成本。其对数批量选项另给期望复杂度，不能自动宣称满足无限可和的 a.s. 条件。

用户需要证明原始 Fast OGDA 的噪声传播与该方法不同，且差异产生明确收益。仅强调使用 optimistic 或 past-gradient 项无法避开此文。

### 6.4 stochastic iKM：复杂度标杆与确定性等价线索

[R22] 的 Theorem 1 给末次 RMS 残差及近最优样本复杂度，预先确定总迭代数。它不是用户所需的无限轨道 a.s. 定理。

Appendix A Proposition 1 将确定性 Fast KM 表示为 iKM 的特定参数实例。但“存在一种等价参数”与“该参数恰好满足随机主定理”是两个命题。必须检查参数及随机更新是否同时一致，才能转用结论。此文对 oracle 成本的比较价值高，不能因为它没有 a.s. 点极限就忽略其竞争性。

### 6.5 stochastic heavy-ball dynamics：连续时间的直接背景

[R27] Theorem 3.5 给 stochastic Fast OGDA 动力系统的 $o(s^{-1})$ a.s. 残差与弱点极限，噪声满足时间加权平方可积条件。它说明连续时间随机快速轨道已有成熟结构。

它没有自动解决离散算法。离散化产生的误差、缓存 oracle 的相关性与实际采样成本仍需另证。用户可借用能量函数的组织方式，但不能将连续时间结论替代离散证明。

## 7. 建议研究入口及一个必要的反例

### 7.1 冻结原始递推

对 $V=I-T$，以同一个缓存 $g_{k-1}$ 更新原始 Fast KM：

$$
x_{k+1}=x_k+\frac{k}{k+\alpha}(x_k-x_{k-1})-\frac{s\alpha}{2(k+\alpha)}g_k-\frac{sk}{k+\alpha}(g_k-g_{k-1}),\qquad g_k=Vx_k+e_k.
$$

在抽取 $e_k$ 之前形成 $\mathcal F_k$。此时 $x_k$、$e_{k-1}$ 已可测，新误差满足条件均值为零，旧误差不再是相对于 $\mathcal F_k$ 的新鞅差。这一点必须直接进入 Lyapunov 漂移计算。

建议的实际顺序为：

1. 对 [R17] 的三序列公式消元，逐项比较状态、初值、系数和噪声。对 [R16]、[R22] 做同样核对。得到明确的覆盖或不覆盖判断。
2. 复现确定性 Fast KM 的能量不等式，再保留旧误差交叉项，确定所需可和权重。先验证能量非负与条件漂移，再使用随机极限工具。
3. 只有在得到真实差异后，才进入 5.2 或 5.5。二维线性试验用于发现错误，不能替代 a.s. 证明。

### 7.2 诊断命题：二阶矩界不能支持任意降低衰减门槛

**本报告推导，非文献新颖性主张。** 取标量 $V(x)=x$、$s=1$、$\alpha>2$。它满足余强制条件，也对应非扩张映射 $T=0$。上述递推精确化为

$$
x_{k+1}=c_kx_k-c_ke_k+d_ke_{k-1},\qquad c_k=\frac{k+\alpha/2}{k+\alpha},\quad d_k=\frac{k}{k+\alpha}.
$$

**持续方差的障碍。** 若新噪声条件方差等于 $\sigma^2>0$，则

$$
\operatorname{Var}(x_{k+1}\mid\mathcal F_k)=c_k^2\sigma^2.
$$

由于 $c_k\to1$，末次均方残差不可能趋于零。这个结论针对上述原始更新，不否定使用衰减步长、VR 或其他参数的算法。方差下界本身也不是一般 a.s. 不可能性的完整证明。

**稀有误差的 a.s. 障碍。** 固定 $2<q\le3$，令各步噪声独立，$e_k$ 分别以概率 $p_k/2$ 取 $1/k$ 与 $-1/k$，其余概率取零，其中 $p_k=k^{2-q}$。于是

$$
\mathbb E[e_k\mid\mathcal F_k]=0,\qquad \mathbb E[e_k^2\mid\mathcal F_k]=k^{-q}.
$$

给定历史，令 $m_k=c_kx_k+d_ke_{k-1}$。数 $m_k-c_k/k$ 和 $m_k+c_k/k$ 中至少一个的绝对值不小于 $c_k/k$。因此

$$
\mathbb P\!\left(k\lvert x_{k+1}\rvert\ge c_k\mid\mathcal F_k\right)\ge p_k/2.
$$

$\sum p_k=\infty$，条件 Borel–Cantelli 引理说明该事件 a.s. 发生无穷多次。由于 $c_k\ge1/2$，$k\lvert x_{k+1}\rvert$ 不能趋于零。因而，**仅有 $\sigma_k^2=O(k^{-q})$、$2<q\le3$，不足以保证这一原始递推的末次 $o(k^{-1})$ a.s. 速率。**

这排除了初步方案中“只用二阶矩将幂次门槛从 $q>3$ 直接放宽到 $q>2$”的宽泛目标。它没有证明所有算法都需要相同门槛，也没有排除轻尾或平均化样本具有额外结构时的改进。第 5.2 节因此明确加入尾部假设，并仍标为待验证。

### 7.3 本轮方案细化的状态

已完成问题锚定、最近邻核对、反例诊断及候选路线筛选。`research-refine` 所指定的外部 `gpt-5.5` 复核调用返回 403，提示模型未启用；**没有获得独立评分，也没有 READY 判定**。保留完整失败返回和自行修订记录。报告中的候选课题均不以该复核作为证明或背书。

## 8. 文献与版本

正文用短编号定位，以下保留英文标题。标为预印本的条目不推断录用状态。正式版与 arXiv 定理编号可能不同；正文明确版本时按该版本编号。

**[R1]** Patrick L. Combettes, Jean-Christophe Pesquet. *Stochastic Quasi-Fejér Block-Coordinate Fixed Point Iterations with Random Sweeping*. 2015, **SIAM Journal on Optimization**, 25(2):1221–1248. [DOI:10.1137/140971233](https://doi.org/10.1137/140971233)；[arXiv:1404.7536v4](https://arxiv.org/abs/1404.7536v4)。正文采用该版本 Corollary 2.7。

**[R2]** Othmane Sebbouh, Robert M. Gower, Aaron Defazio. *Almost sure convergence rates for Stochastic Gradient Descent and Stochastic Heavy Ball*. 2021, **COLT**, PMLR 134. [arXiv:2006.07867](https://arxiv.org/abs/2006.07867)；[会议正式页](https://proceedings.mlr.press/v134/sebbouh21a.html)。正文采用会议版 Theorem 13、Corollary 17。

**[R3]** Jun Liu, Ye Yuan. *On Almost Sure Convergence Rates of Stochastic Gradient Methods*. 2022, **COLT**, PMLR 178:2963–2983. [arXiv:2202.04295](https://arxiv.org/abs/2202.04295)；[会议正式页](https://proceedings.mlr.press/v178/liu22d.html)。

**[R4]** Julien Hermant, Marien Renaud, Jean-François Aujol, Charles Dossal, Aude Rondepierre. *Gradient correlation is a key ingredient to accelerate SGD with momentum*. 2025, **ICLR**. [arXiv:2410.07870](https://arxiv.org/abs/2410.07870)。正文使用本地 Zotero 的 ICLR 2025 正式稿 Theorems 3–4，未把 2026 v3 的可能编号变化混入。

**[R5]** Hedy Attouch, Jalal Fadili, Vyacheslav Kungurtsev. *The Stochastic Ravine Accelerated Gradient Method with General Extrapolation Coefficients*. 2026, **Journal of Optimization Theory and Applications**, 209:5；2024 预印本。 [DOI:10.1007/s10957-026-02940-4](https://doi.org/10.1007/s10957-026-02940-4)；[arXiv:2403.04860](https://arxiv.org/abs/2403.04860)。正文按期刊版编号。

**[R6]** Saverio Salzo. *The iterates of FISTA converge even under inexact computations and stochastic gradients*. 2025 首稿，2026-07-30 v3，**预印本**。[arXiv:2511.12665v3](https://arxiv.org/abs/2511.12665v3)。

**[R7]** Mario Bravo, Roberto Cominetti. *Stochastic Fixed-Point Iterations for Nonexpansive Maps: Convergence and Error Bounds*. 2024, **SIAM Journal on Control and Optimization**. [DOI:10.1137/22M1515550](https://doi.org/10.1137/22M1515550)；[arXiv:2208.04193v3](https://arxiv.org/abs/2208.04193v3)。

**[R8]** Daniel Cortild, Coralia Cartis, Juan Peypouquet. *Stochastic Krasnoselskii-Mann Iterations: Convergence without Uniformly Bounded Variance*. 2026-09-11 v3，**预印本**。[arXiv:2604.22581v3](https://arxiv.org/abs/2604.22581v3)。

**[R9]** Mario Bravo, Juan Pablo Contreras. *Stochastic Halpern iteration in normed spaces and applications to reinforcement learning*. 2026, **Mathematical Programming**；2024 首稿。 [DOI:10.1007/s10107-026-02345-1](https://doi.org/10.1007/s10107-026-02345-1)；[arXiv:2403.12338v4](https://arxiv.org/abs/2403.12338v4)。本报告定理编号按 v4 正文。

**[R10]** Radu Ioan Boţ, Dang-Khoa Nguyen. *Fast Krasnosel’skiĭ–Mann Algorithm with a Convergence Rate of the Fixed Point Iteration of $o(1/k)$*. 2023, **SIAM Journal on Numerical Analysis**. [DOI:10.1137/22M1504305](https://doi.org/10.1137/22M1504305)；[arXiv:2206.09462v2](https://arxiv.org/abs/2206.09462v2)。

**[R11]** Mario Bravo, Roberto Cominetti, Matías Pavez-Signé. *Rates of convergence for inexact Krasnosel’skii-Mann iterations in Banach spaces*. 2017 预印本，正式卷期本次未复核。[arXiv:1705.09340v2](https://arxiv.org/abs/1705.09340v2)。定理编号按此预印本。

**[R12]** Felix Lieder. *On the convergence rate of the Halpern-iteration*. 2021 卷期、2020 online，**Optimization Letters**. [DOI:10.1007/s11590-020-01617-9](https://doi.org/10.1007/s11590-020-01617-9)。

**[R13]** TaeHo Yoon, Ernest K. Ryu. *Accelerated Algorithms for Smooth Convex-Concave Minimax Problems with $O(1/k^2)$ Rate on Squared Gradient Norm*. 2021, **ICML**, PMLR 139:12098–12109. [arXiv:2102.07922](https://arxiv.org/abs/2102.07922)；[会议正式页](https://proceedings.mlr.press/v139/yoon21d.html)。

**[R14]** Radu Ioan Boţ, Enis Chenchene. *Extragradient Method with Flexible Anchoring: Strong Convergence and Fast Residual Decay*. 2026, **SIAM Journal on Optimization**, 36(3):1420–1445. [DOI:10.1137/24M1703562](https://doi.org/10.1137/24M1703562)。

**[R15]** Radu Ioan Boţ, Enis Chenchene, Jalal Fadili. *Fast Krasnoselskii–Mann Method with Overrelaxation and Preconditioners*. 2026, **IMA Journal of Numerical Analysis**, drag042. [DOI:10.1093/imanum/drag042](https://doi.org/10.1093/imanum/drag042)；[arXiv:2411.18574](https://arxiv.org/abs/2411.18574)。正文按期刊版 Theorem 2。

**[R16]** Quoc Tran-Dinh. *Variance-Reduced Fast Krasnoselkii-Mann Methods for Finite-Sum Root-Finding Problems*. 2024 首稿，2026-09-09 v4，**预印本**。[arXiv:2406.02413v4](https://arxiv.org/abs/2406.02413v4)。

**[R17]** Nghia Nguyen-Trung, Quoc Tran-Dinh. *A Class of Accelerated Fixed-Point-Based Methods with Delayed Inexact Oracles and Its Applications*. 2025-12-15 v1，**预印本**。[arXiv:2512.13547v1](https://arxiv.org/abs/2512.13547v1)。

**[R18]** Quoc Tran-Dinh. *VFOSA: Variance-Reduced Fast Operator Splitting Algorithms for Generalized Equations*. 2025, **Journal of Machine Learning Research**, 26(254):1–68. [JMLR 正式全文及元数据](https://www.jmlr.org/papers/v26/25-0500.html)。官方页未列 DOI；对应 arXiv 编号待核实。文章存在性与 Theorem 14 已从正式全文核对，自动标题匹配仍为待核验状态。

**[R19]** Quoc Tran-Dinh, Nghia Nguyen-Trung. *New Accelerated Past-Extragradient Methods with Variance Reduction for Generalized Equations*. 2025 首稿，2026-09-09 v2，**预印本**。[arXiv:2508.16791v2](https://arxiv.org/abs/2508.16791v2)。v1 的 VFOG 标题与 v2 的 VAPEG 标题属于同一条版本记录，不计为两篇独立成果。

**[R20]** Radu Ioan Boţ, Ernö Robert Csetnek, Dang-Khoa Nguyen. *Fast Optimistic Gradient Descent Ascent (OGDA) Method in Continuous and Discrete Time*. 2025 卷期、2023 online，**Foundations of Computational Mathematics**, 25:163–222. [DOI:10.1007/s10208-023-09636-5](https://doi.org/10.1007/s10208-023-09636-5)；[arXiv:2203.10947](https://arxiv.org/abs/2203.10947)。正文按期刊版 Theorems 16–17。

**[R21]** Xufeng Cai, Chaobing Song, Cristóbal Guzmán, Jelena Diakonikolas. *Stochastic Halpern Iteration with Variance Reduction for Stochastic Monotone Inclusions*. 2022, **NeurIPS**；2023 v4。[arXiv:2203.09436v4](https://arxiv.org/abs/2203.09436v4)。正文按 v4 的 Theorem 3.1、Corollary 3.4、Theorem 4.1。

**[R22]** Tong Yang, Tao Jiang, Yuejie Chi, Ashok Cutkosky, Lin Xiao. *Stochastic Inertial Krasnosel’skii-Mann Iteration Achieves Near-Optimal Sample Complexity*. 2026-09-22 v1，**预印本**。[arXiv:2609.28543v1](https://arxiv.org/abs/2609.28543v1)。

**[R23]** TaeHo Yoon, Nicolas Loizou. *Direct Acceleration of Stochastic Root-Finding Without Variance Reduction and Regularization*. 2026，**预印本；作者 CV 列为 NeurIPS 2026，会议官方状态待复核**。[arXiv:2608.12043](https://arxiv.org/abs/2608.12043)。

**[R24]** TaeHo Yoon, Nicolas Loizou. *Dual-Anchor Acceleration Is Near-Optimal for Stochastic Monotone Root-Finding*. 2026-09-28 v1，**预印本**。[arXiv:2609.36033v1](https://arxiv.org/abs/2609.36033v1)。

**[R25]** Jun-Hyun Kim, Ahmet Alacaoglu. *Improving the Last-Iterate Guarantees of Anytime Algorithms for Stochastic Monotone Variational Inequalities*. 2026-09-24 v2，**预印本**。[arXiv:2609.15257v2](https://arxiv.org/abs/2609.15257v2)。Jun-Hyun Kim 与初始人物线索中的 Donghwan Kim 不是同一个人。

**[R26]** Jelena Diakonikolas. *Solving Stochastic Fixed-Point Equations with High Probability*. 2026，**预印本**。[arXiv:2607.09097](https://arxiv.org/abs/2607.09097)。本次实际读取 arXiv HTML 的 Theorem 1 与 Corollaries 1–3。

**[R27]** Radu Ioan Boţ, Chiara Schindler. *Long-time analysis of stochastic heavy ball dynamics for convex optimization and monotone equations*. 2026, **Discrete and Continuous Dynamical Systems**, 51:439–474. [DOI:10.3934/dcds.2026035](https://doi.org/10.3934/dcds.2026035)。

**[R28]** Jisun Park, Ernest K. Ryu. *Exact Optimal Accelerated Complexity for Fixed-Point Iterations*. 2022, **ICML**. [arXiv:2201.11413v2](https://arxiv.org/abs/2201.11413v2)。

**[R29]** Yekini Shehu. *Adaptivity, Anchoring, and the Exact Oracle Complexity of Stochastic Fixed-Point Iterations*. 2026，**预印本**。[arXiv:2610.00295v1](https://arxiv.org/abs/2610.00295v1)。正文只引用其 Theorem 4.8 所属的 Hilbert 复杂度方向，不以标题替代对所有模型的证明。

**[R30]** Jelena Diakonikolas, Cristóbal Guzmán, David Martínez-Rubio. *Oracle Complexity of Stochastic Fixed-Point Equations with Nonexpansive Maps*. 2026，**预印本**。[arXiv:2609.09524](https://arxiv.org/abs/2609.09524)。本次元数据核实，正文定理待核实，未据此填写数值速率。

**[R31]** Patrick L. Combettes, Jean-Christophe Pesquet. *Stochastic Quasi-Fejér Block-Coordinate Fixed Point Iterations With Random Sweeping II: Mean-Square and Linear Convergence*. 2019, **Mathematical Programming**, 174:433–451. [arXiv:1704.08083](https://arxiv.org/abs/1704.08083)。用作研究者代表作，不向本报告一般非扩张模型转用其线性率。

**[R32]** Juan Pablo Contreras, Roberto Cominetti. *Optimal error bounds for non-expansive fixed-point iterations in normed spaces*. 2023, **Mathematical Programming**, 199:343–374. [DOI:10.1007/s10107-022-01830-7](https://doi.org/10.1007/s10107-022-01830-7)；[arXiv:2108.10969](https://arxiv.org/abs/2108.10969)。

**[R33]** Saverio Salzo, Silvia Villa. *Inexact and Accelerated Proximal Point Algorithms*. 2012, **Journal of Convex Analysis**, 19(4):1167–1192. [DOI:10.68381/jca19062](https://doi.org/10.68381/jca19062)；[期刊正式页](https://journalofconvexanalysis.com/articles/jca19062/)。

**[R34]** Ahmet Alacaoglu, Yura Malitsky. *Stochastic Variance Reduction for Variational Inequality Methods*. 2022, **COLT**, PMLR 178:778–816. [arXiv:2102.08352](https://arxiv.org/abs/2102.08352)；[会议正式页](https://proceedings.mlr.press/v178/alacaoglu22a.html)。

**[R35]** Radu Ioan Boţ, Ernö Robert Csetnek, Christopher Hendrich. *Inertial Douglas–Rachford splitting for monotone inclusion problems*. 2015, **Applied Mathematics and Computation**, 256:472–487. [DOI:10.1016/j.amc.2015.01.017](https://doi.org/10.1016/j.amc.2015.01.017)；[arXiv:1403.3330](https://arxiv.org/abs/1403.3330)。

## 9. 核查范围与使用限制

本轮按三个层次交叉核对：先用本地讨论笔记和 Zotero 确认研究对象，再阅读原文定理和参数条件，最后用 arXiv / DOI / 官方发表页面复核作者、版本与发表信息。这是三个核查环节，**不表示每个结论都有三个相互独立的证明来源**。

原论文定理是速率的依据；作者主页用来确认身份与任职；元数据只确认书目，不能证明定理正确。核心算法的递推等价、弱点极限推广和候选更弱噪声定理仍为待验证事项。报告没有对预印本证明做逐行形式审查。

原始线索中的 `2609.09152` 不对应 stochastic iKM；本次采用已经核实的 [R22] `2609.28543`。此前抓取到的一个同姓 Yoon 的 ICML PDF 实为 autoencoding 论文，已从证据链排除，EAG 改用已核对作者和标题的 `yoon21d` 正式全文。

配套研究目录保存候选文献、自动核验状态、主页访问记录、核心论文知识库、覆盖关系、反例诊断和方案细化日志。报告正文可独立阅读；这些辅助文件用于后续研究追踪。外部复核的服务失败不影响已保存的本地文献证据，但独立评审仍未完成。
