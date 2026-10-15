# 随机 KM 与 Fast KM 研究报告


**精华总结。** 随机快速不动点方法已有几乎必然 little-o 残差与迭代点极限理论，因此“把 Fast KM 随机化”本身不足以构成新贡献。本次找到的明确问题是：**原 Fast KM 复用上一步随机查询时，如何在能量中利用噪声差分的抵消，并证明 N6 下的路径速率。** 双查询版本的 N6 证明已写出；原复用版本的一般 N6 结论仍待证明。

**结论。** 按“一个月内独立推完”的优先级，将双查询 Fast KM 的 N6 定理列为入门主课题。其证明已在附录写出，适合独立重建；可发表的新意仍待确认。将原算法查询复用的一般 N6 定理列为研究备选，将仿射算子的噪声阈值列为第二备选。查询复用是值得继续研究的机制，但当前不能保证其一般定理在一个月内完成。

本报告采用三种状态：**文献事实**表示核对过指定版本的定理陈述；**本次证明**表示附录提供了推导；**待验证**表示缺少证明或尚未完成新颖性排查。文献陈述与已独立检查的证明不混为一项。

**精华总结：** 老大，研究报告、证明附录和独立复核记录已完成。双次新查询版本的 N6 定理已有完整证明；**原版 Fast KM 复用历史查询时的一般 N6 定理仍待证明**。

**结论：** 按“一个月内独立推完”的要求，建议把**双查询 Fast KM 的 N6 定理**作为入门主课题。原版查询复用的一般定理与仿射算子的噪声阈值作为两个备选。可发表的新意仍待确认。

交付文件：

- [研究报告](/Users/liluxuan/Documents/My_Papers/5_stochastic_nesterov/memory/readings/261014-stochastic-km-research-report.md)：包含算法入门、应用、文献比较、候选课题、两周计划和向 Boţ 提的三个问题。
- [证明附录](/Users/liluxuan/Documents/My_Papers/5_stochastic_nesterov/memory/readings/261014-stochastic-fast-km-proof.md)：包含完整噪声展开、双查询定理、查询复用例子及反例。
- [独立复核记录](/Users/liluxuan/Documents/My_Papers/5_stochastic_nesterov/memory/readings/261014-stochastic-km-proof-audit.md)：记录假设、证明依赖、修订及未解决问题。

核心判断有四项：

1. **已证明：** 对参数 $$\alpha=4$$ 的双查询版本，在条件零均值及确定的 N6 方差预算下，残差与速度几乎必然为 $$o(1/k)$$，迭代点几乎必然有弱极限。独立复核未发现实质证明错误。
2. **查询复用具有实际作用。** 指定的一维 Gaussian 模型表明，复用历史查询能抵消部分噪声，允许比双次独立查询更慢的噪声衰减。该结论尚未推广到一般非线性算子。
3. **N2 下不能直接给出“最优步长指数”。** 直接把快速递减步长代入原公式，即使没有噪声，也可能留下非零残差。
4. **AFP v1 的 Lemma 1 式 5 存在精确反例。** 这否定该引理的印刷陈述，**没有否定其最终 Theorem 2**。
5. 

## 0. 两个首先需要纠正的前提

1. **本地 iKM PDF 对应错误。** `2609.09152v2 2.pdf` 对应 Yuhan Ye、Kaizhao Liu 的 *Silver Rate Is (Almost) Optimal for Gradient Descent*。它与随机 iKM 无关。正确的 iKM 是 Tong Yang、Tao Jiang、Yuejie Chi、Ashok Cutkosky、Lin Xiao 的 [arXiv:2609.28543](https://arxiv.org/abs/2609.28543)。
2. **N2 和 N6 都需要明确零均值条件。** 方差有界或可和并不排除系统性误差。下文凡利用条件期望消去线性项，都另要求 $\mathbb E[e_k\mid\mathcal F_k]=0$。保守的路径绝对可和定理则不要求零均值。

本文将 N2 写为 $\mathbb E[\lVert e_k\rVert^2\mid\mathcal F_k]\le\sigma^2$。对固定步长 Fast KM，$t_k\asymp k$，N6 对应 $\sum_k k^2v_k<\infty$，其中 $v_k$ 是条件二阶矩上界。路径上随机预算可和，与预算的期望有限，也需要区别。

## 1. 任务 A：四种算法解决了什么问题

设 $H$ 为 Hilbert space（希尔伯特空间），$T:H\to H$，$F=\operatorname{Fix}T\ne\varnothing$。**residual（残差）**为 $r_k=\lVert x_k-Tx_k\rVert$。它衡量 fixed-point equation（不动点方程）是否满足；没有额外误差界时，小 residual 不等于到 solution set（解集）的距离具有相同速率。

nonexpansive（非扩张）指 $\lVert Tx-Ty\rVert\le\lVert x-y\rVert$。$\theta$-averaged operator（$\theta$-平均算子）满足 $T=(1-\theta)\operatorname{Id}+\theta R$，其中 $R$ nonexpansive 且 $0<\theta<1$。为统一 Fast KM 记号，允许 $\theta=1$ 覆盖所有 nonexpansive operator（非扩张算子）。

| 算法 | 假设与参数 | deterministic residual（确定性残差） | iterate convergence（迭代点收敛） | 机制与边界 |
|---|---|---|---|---|
| Picard | $T$ 为 contraction mapping（压缩映射），常数 $q<1$ | $O(q^k)$ | strong convergence（强收敛）到唯一 fixed point（不动点） | 直接重复查询；仅有 nonexpansiveness（非扩张性）时可能形成周期 |
| KM | $T$ nonexpansive，固定 $0<\lambda<1$ | $o(k^{-1/2})$ | weak convergence（弱收敛）到某个 fixed point；有限维为 strong convergence | averaging（平均化）抑制旋转；没有指定最近解 |
| Halpern | $T$ nonexpansive，anchor point（锚点）$u=x_0$，$\beta_k=1/(k+2)$ | $O(1/k)$，不能普遍替换为 little-o | strong convergence 到 $P_Fu$ | 逐渐减弱的 anchor point 选择最近解；它是独立路线，不是给 KM 添加 momentum（动量） |
| Fast KM | $T$ 为 $\theta$-averaged operator，$\alpha>2$，固定 $0<s\le1/\theta$ | $o(1/k)$ | weak convergence 到某个 fixed point；有限维为 strong convergence | inertial term（惯性项）与 operator difference（算子差分）共同加速；单独添加 inertia（惯性）没有同样保证 |

KM 的 little-o 可由下文的 square summability（平方可和性）与 residual 单调性直接证明。Halpern 的速率见 [Lieder，Theorem 2.1](https://doi.org/10.1007/s11590-020-01617-9)；strong limit（强极限）是其引言引用的 Wittmann Theorem 2 所述经典结论。Fast KM 的结论见 [Boţ–Nguyen，Theorems 3.4–3.5](https://doi.org/10.1137/22M1504305)。

四个更新格式分别为

$$
x_{k+1}=Tx_k.
$$

$$
x_{k+1}=(1-\lambda)x_k+\lambda Tx_k.
$$

$$
x_{k+1}=\beta_k u+(1-\beta_k)Tx_k.
$$

$$
x_{k+1}=x_k+\frac{k}{k+\alpha}(x_k-x_{k-1})-\frac{s(k+\alpha/2)}{k+\alpha}(\operatorname{Id}-T)x_k+\frac{sk}{k+\alpha}(\operatorname{Id}-T)x_{k-1}.
$$

KM 的基本距离不等式为

$$
\lVert x_{k+1}-x^\star\rVert^2\le\lVert x_k-x^\star\rVert^2-\lambda(1-\lambda)r_k^2.
$$

residual 不增且 $\sum r_k^2<\infty$，因此 $kr_k^2\to0$。这个结论针对固定松弛参数的 Hilbert setting（Hilbert 情形）；一般变参数只由该不等式得到加权级数有限，不能直接照搬同一速率。

### 1.1 四个可手算的二维例子

**Picard 的周期。** 取 $T(x,y)=(-y,x)$、$x_0=(1,0)$。Picard 在四个点之间循环，始终有界，但没有 limit（极限）。研究指令中的“发散”应在这里解释为 iterates（迭代点）不趋于一点，不能说范数趋于无穷。

**KM 的平均化。** 对同一个 rotation（旋转）取 $\lambda=1/2$，更新矩阵为 $(I+T)/2$，它的模长缩小因子为 $1/\sqrt2$。iterates 与 residual 均按 geometric rate（几何速率）趋于零。

**Halpern 的锚点作用。** 取 $T(x,y)=(x,0)$、$u=x_0=(1,1)$。则 $x_k=(1,1/(k+1))$，residual 恰为 $1/(k+1)$，limit 为 $P_Fu=(1,0)$。这个例子直接说明其 $O(1/k)$ 不保证 $o(1/k)$。

**Fast KM 的速度。** 对同一 projection（投影）取 $\alpha=4,s=1,x_0=x_1=(1,1)$。对 $k\ge1$ 有

$$
x_k=\left(1,\frac{12}{(k+2)(k+3)}\right).
$$

该特殊例子的 residual 是 $O(k^{-2})$；它没有将一般 nonexpansive operator 的保证提高到 $O(k^{-2})$。

### 1.2 与 Nesterov 及 Fast OGDA 的关系

Boţ–Nguyen 的 continuous-time model（连续时间模型）为

$$
\ddot x(t)+\frac{\alpha}{t}\dot x(t)+\frac{d}{dt}V(x(t))+\frac{\alpha}{2t}V(x(t))=0,\qquad V=\operatorname{Id}-T.
$$

$\alpha/t$ 是随时间减小的 damping coefficient（阻尼系数）。$dV(x(t))/dt$ 是 operator variation（算子变化）的校正项。离散化同时产生 velocity term（速度项）和 operator difference，因此不能把 Fast KM 简化为“给 KM 加一个 Nesterov momentum（Nesterov 动量）”。$\alpha>2$ 为原定理提供严格的 square-summable term（平方可和项）；改变 $\alpha$ 会同时改变阻尼和 energy coefficient（能量系数）。

非扩张性等价于下式：

$$
\langle Vx-Vy,x-y\rangle\ge\frac12\lVert Vx-Vy\rVert^2.
$$

这种不等式称为 **cocoercivity（余强制性）**。它还给出 monotonicity（单调性）与 $2$-Lipschitz continuity（Lipschitz 连续性）。因此 fixed-point problem（不动点问题）属于 Fast OGDA 面向的 monotone Lipschitz equation（单调 Lipschitz 方程）问题类。**这不表示两个离散算法等同。** 原 Fast KM 的 Remark 2.2 明确区分了它与显式 Fast OGDA 的步骤及允许步长。

反方向不成立。取非零斜对称旋转 $V$，有 $\langle Vx,x\rangle=0$，但 $\lVert(I-V)x\rVert>\lVert x\rVert$。因此仅有单调 Lipschitz 性不足以保证 $I-V$ 非扩张。

## 2. 任务 B：四种应用的算子形式

### 2.1 Proximal gradient

假设 $f$ 凸可微且梯度 $L$-Lipschitz，$g$ 为 proper、lower semicontinuous、convex 函数。对 $0<\gamma<2/L$，令

$$
T=\operatorname{prox}_{\gamma g}\circ(\operatorname{Id}-\gamma\nabla f).
$$

该 $T$ 为 averaged 算子，且 $\operatorname{Fix}T=\operatorname{argmin}(f+g)$。随机梯度、有限数据抽样和提前结束近端子问题是误差来源。

**oracle 边界。** 即使随机梯度条件无偏，把它送入非线性的 prox 后，完整更新映射的误差也未必条件无偏。要套用无偏 $\widehat T$ 定理，必须对完整算子证明零均值，或使用允许可控系统误差的模型。prox 的非扩张性能够控制误差大小，不能自动证明零均值。

### 2.2 Douglas–Rachford

设 $A,B$ 为 maximal monotone 算子，$\gamma>0$。定义 resolvent $J_{\gamma A}=(I+\gamma A)^{-1}$ 与反射 $R_{\gamma A}=2J_{\gamma A}-I$，再取

$$
T=\frac12(I+R_{\gamma B}R_{\gamma A}).
$$

该 $T$ 为 firmly nonexpansive，即 $1/2$-averaged。若 $z\in\operatorname{Fix}T$，则 **shadow** $x=J_{\gamma A}z$ 满足 $0\in A(x)+B(x)$。算法迭代的是辅助变量 $z$，不能直接把它叫作原问题的解。

随机误差来自 inexact resolvent、随机子问题和数据子集。其均值与大小需要在 resolvent 输出处验证。

### 2.3 PDHG

考虑 $\min_x f(x)+g(Ax)$，并假设存在鞍点。采用 x-first PDHG：

$$
x^+=\operatorname{prox}_{\tau f}(x-\tau A^*y),
$$

$$
y^+=\operatorname{prox}_{\sigma g^*}(y+\sigma A(2x^+-x)).
$$

记 $z=(x,y)$，$M(z)=(\partial f(x)+A^*y,\partial g^*(y)-Ax)$，并令

$$
P=\begin{pmatrix}\tau^{-1}I&-A^*\\-A&\sigma^{-1}I\end{pmatrix}.
$$

当 $\tau\sigma\lVert A\rVert^2<1$ 时，$P$ 正定，PDHG 的完整更新为

$$
T=J_{P^{-1}M}.
$$

它在 $\langle z,w\rangle_P=\langle Pz,w\rangle$ 下 firmly nonexpansive。这里使用的是加权度量，不能省略后直接声称 Euclidean firmly nonexpansiveness。

随机误差来自线性算子的抽样、数据块、随机梯度和近端子问题。若采用随机坐标更新，需要另行核对随机更新的模型是否符合所用定理。

### 2.4 KKT 与斜对称块

鞍点问题为

$$
\min_x\max_y\ f(x)+\langle Ax,y\rangle-g^*(y).
$$

其 KKT 条件是 $0\in M(z)$。算子由 $\partial f\times\partial g^*$ 和线性块 $S(x,y)=(A^*y,-Ax)$ 组成。由于

$$
\langle S(z-z'),z-z'\rangle=0,
$$

斜对称块不破坏单调性。非光滑情形的 $M$ 是集合值算子，不能直接把它写成单值 Lipschitz 方程。若要得到适用于 Fast KM 的单值残差，使用 $V_M=I-J_M$；若要直接应用 Fast OGDA，需要相应的单值与 Lipschitz 假设。

**研究价值。** 这些问题都能通过完整更新映射或 resolvent 残差表达。随机理论有价值的前提是：所假设的误差模型能够由实际查询过程产生，且查询成本没有被隐藏。

## 3. 任务 C：文献实际证明的结论

以下依照指定顺序将前三篇放在最前。结论类型记为：**1** 预设时域；**2** 期望；**3** 残差几乎必然；**4** 迭代点几乎必然；**5** 查询复杂度。

| 论文与证据锚点 | 噪声或问题模型 | 参数条件与预设时域 | 已核对的结论 | 类型与核心工具 |
|---|---|---|---|---|
| Bravo–Cominetti 2024，Theorem 2.5、Example 2.7 | 有限维一般范数，martingale difference，有二阶矩界 | $\lambda_k=(k+1)^{-a}$，有界方差时 $2/3<a\le1$ 足够；不需要预设 $K$ | 迭代点几乎必然强趋于随机不动点，故残差趋于零；不能把滤后噪声的速率直接称为原残差速率 | 3、4；滤后噪声、确定性 inexact KM、Doob 与随机逼近 |
| 同文 Theorems 2.10、4.1、4.4，Corollary 5.4 | 期望末次界另需 bounded range 或原文 h4 的可和性；随机输出界限 Euclidean 情形 | 固定时域优化松弛参数；或幂次递减参数 | 一般范数末次 $O(K^{-1/6})$；Euclidean 随机输出 $O(K^{-1/4})$；查询数分别为 $O(\epsilon^{-6})$ 与 $O(\epsilon^{-4})$ | 1、2、5；确定性残差卷积与平方距离估计。输出方式与几何条件不同 |
| Yang–Jiang–Chi–Cutkosky–Xiao 2026，Theorem 1、式 12、17 | Hilbert；完整 $T$ 的条件零均值噪声，方差 $\le\sigma^2$；允许可预测系统误差 | 三组参数按式 12 设置，**显式依赖 $K$**；每步一次查询 | RMS 末次残差 $O(D/K+\sigma\log K/\sqrt K+B_K\log K/K)$；无系统误差时近 $\epsilon^{-2}$ 查询数 | 1、2、5；两次外推与加权二次估计。该定理没有给出同一无限轨道的路径速率或迭代点极限 |
| Boţ–Nguyen 2023，Algorithm 2.1、Proposition 3.3、Theorems 3.4–3.5 | 确定性，Hilbert，$\theta$-averaged | $\alpha>2$、固定 $0<s\le1/\theta$；不依赖 $K$ | 残差和速度均 $o(1/k)$；迭代点有弱极限 | 确定性基准；两组能量极限、加权平方可和、Opial |
| Bravo–Contreras 2026，Theorem 3.3、Corollary 3.5、Theorem 3.10 | 有限维一般范数；Halpern；批量控制误差的一阶矩 | 算子权重 $\beta_n=n/(n+1)$；批量 $m_n=n^4$；不依赖 $K$ | 期望残差 $\widetilde O(1/n)$，查询数 $\widetilde O(\epsilon^{-5})$。若 $\sum\mathbb E\lVert U_n\rVert<\infty$ 及锚点条件，残差几乎必然趋零；smooth norm 下迭代点有强极限 | 2、3、4、5；递归误差界与路径绝对可和。Theorem 3.10 本身没有宣称一般 $o(1/n)$ 路径速率 |
| Combettes–Pesquet 2015，Corollary 2.7 | 可分 Hilbert，允许非零均值误差 | $\sum\lambda_n(1-\lambda_n)=\infty$；$\sum\lambda_n\sqrt{\mathbb E[\lVert e_n\rVert^2\mid\mathcal X_n]}<\infty$ | 迭代点几乎必然有弱极限；demicompact 时为强极限 | 4；stochastic quasi-Fejér。误差条件是加权 RMS 的绝对可和，不能写成仅加权方差可和 |
| Tran-Dinh，VR Fast KM，arXiv:2406.02413v4，Theorems 1–2 | 有限维 $\mathbb R^p$；有限和；average cocoercivity；对算子差分构造条件无偏 VR estimator | 按式 19 的固定参数规则；误差满足 Definition 1 的递归条件；不依赖 $K$ | 平方残差的期望与几乎必然 $o(1/k^2)$；迭代点几乎必然强趋于一个解；SVRG/SAGA 查询复杂度 $O(n+n^{2/3}/\epsilon)$ | 2、3、4、5；带 estimator 误差量的能量与 Robbins–Siegmund |
| Nguyen-Trung–Tran-Dinh 2025，AFP，arXiv:2512.13547v1，Theorem 2、Corollary 2 | 有限维 cocoercive 算子；允许延迟与非零均值 inexact oracle | Definition 1；$\sum\delta_k<\infty$；批量使 $k^2\mathbb E_k\lVert e_k\rVert^2$ 可和 | **论文声明**几乎必然 $o(1/k)$ 残差与迭代点极限；本次发现其 Lemma 1 式 5 的反例，因此该版本证明不能直接计为通过独立核查 | 声明覆盖 2、3、4、5；证明问题及准确范围见附录第 8 节 |
| Tran-Dinh，VFOSA，JMLR 2025，Theorem 14、Remark 15 | 有限维；方差缩减 splitting；不同于原 Fast KM 的更新 | Theorem 12 的条件、式 38 与 42；Remark 15 给出 $O(k^{-3-\omega})$ 的方差充分条件 | $\lVert G_\lambda x_k\rVert$ 和 $\lVert x_{k+1}-x_k\rVert$ 均几乎必然为 $o(1/k)$；两组迭代点几乎必然强趋于一个解 | 3、4；扩展能量和 estimator 递归。残差属于该文的变换算子 $G_\lambda$ |
| Boţ–Schindler 2026，Theorem 3.5 | **连续时间** stochastic Fast OGDA；单调算子 | $\int s^2\lVert\sigma_Z(s)\rVert^2ds<\infty$ 等原文条件 | 残差几乎必然 $o(1/s)$，轨迹几乎必然有弱极限 | 连续时间 3、4；stochastic energy。不能据此宣称离散原 Fast KM 已解决 |

表中的 $B_K=\sum_{k<K}(\mathbb E\lVert b_k\rVert^2)^{1/2}$，$D=\operatorname{dist}(x_1,F)$。iKM 的 $b_k$ 是系统误差，与证明附录的 Fast KM 系数 $b_k$ 属于不同记号系统。

### 3.1 iKM 的准确关系

iKM 在两个外推点之间组合更新：

$$
y_k=x_k+\alpha_k(x_k-x_{k-1}),\qquad z_k=x_k+\beta_k(x_k-x_{k-1}),
$$

$$
x_{k+1}=(1-\lambda_k)y_k+\lambda_k\widehat T_k(z_k).
$$

其 Appendix A、Proposition 1 通过特定初始化和另一组参数，将确定性 Fast KM 表示为 iKM 的查询序列。这组参数对应式 21，**不同于 Theorem 1 使用的式 12**。因此，确定性等价关系没有自动把 iKM 的随机复杂度定理转移到原 Fast KM 的参数和查询复用方式。

### 3.2 两篇 Zotero 文献与补充条目

| 文献 | 核对位置 | 与本课题的关系和边界 |
|---|---|---|
| Shehu，arXiv:2610.00295v1 | Theorems 4.3、4.8 | Theorem 4.3 在 Hilbert/2-uniformly smooth 空间给出 $O(K_{\mathrm{sm}}\sigma^2D^2\epsilon^{-4})$ 批量复杂度；批量 $m_k=\lceil c\max\{k,1\}\rceil$ 的 $c=8K_{\mathrm{sm}}\sigma^2/\epsilon^2$ **依赖目标精度**，$N=\lceil4D/\epsilon\rceil+8$。Theorem 4.8 借助外部 Chen–Luo RAIN reduction 陈述近最优复杂度，该 reduction 未逐行重建。均不能据此推出原 Fast KM 的无限轨道定理 |
| Yoon–Loizou，arXiv:2609.36033 | Theorems 2.2、3.2，Corollaries 3.3、3.6 | Corollary 3.6 使用 samplewise monotone、统一 $L$-Lipschitz 随机算子及 approximate resolvent 内循环；使末次算子残差的 RMS 不超过 $\epsilon$ 的调用数为 $O((1+LD/\epsilon)\log(1+LD/\epsilon)+(\sigma^2/\epsilon^2)\log^2(1+LD/\epsilon))$。参数依赖目标精度，属于有限时域期望复杂度；没有据此得到同一无限轨道的路径定理 |
| Cortild–Cartis–Peypouquet，arXiv:2604.22581v3 | Theorem 2.13、Corollary 2.12 | samplewise nonexpansive $T_\xi$，并在一个解处有有限方差；含路径渐近结果。running minimum 的路径速率与末次期望界须分开。旧摘要的两人作者表不能代替该版本三人作者表 |
| Bravo–Cominetti–Pavez-Signé 2019 | Theorems 1.1、2.4、3.1 | inexact KM 的确定性残差估计是 Bravo–Cominetti 随机证明的输入；它本身不负责借条件零均值消去随机项 |
| Lee–Bravo–Cominetti，ICML 2025 | Theorems 3.4、3.6，Corollaries 3.5、3.7 | 锚点化用于 MDP 的查询复杂度；依赖应用结构，不能直接称为所有随机不动点问题的统一复杂度 |

结论：**已有随机快速方法的路径速率，因此缺口需要落在某个明确算法和 oracle 模型上。** 这次研究保留的对象是原 Fast KM 的单次新查询与历史查询复用，而不是整个随机快速方法类别。

## 4. 核心证明：随机 KM 为什么能趋于解

### 4.1 条件零均值到底消除了什么

先在 Euclidean/Hilbert 度量写出随机 KM 的单步估计。令 $y_k=(1-\lambda_k)x_k+\lambda_kTx_k$，则 $x_{k+1}=y_k+\lambda_ke_k$。因此

$$
\lVert x_{k+1}-x^\star\rVert^2\le\lVert x_k-x^\star\rVert^2-\lambda_k(1-\lambda_k)r_k^2+2\lambda_k\langle y_k-x^\star,e_k\rangle+\lambda_k^2\lVert e_k\rVert^2.
$$

因为 $y_k$ 在查询前已知，线性项的条件期望为零。二阶项的系数为 $\lambda_k^2$。因此此处需要的是 **$\sum\lambda_k^2v_k<\infty$**，即已经包含平方的项作为非负级数可和。不能将它与 $\sum\lambda_k\sqrt{v_k}<\infty$ 的 RMS 绝对可和条件混淆。

Robbins–Siegmund 给出到每个固定解的距离有极限，并得到 $\sum\lambda_k(1-\lambda_k)r_k^2<\infty$。仅由加权级数有限，不能直接写出末次 $o(1/k)$。

### 4.2 Bravo–Cominetti 的一般范数证明骨架

他们没有把 Hilbert 的平方范数恒等式当作一般范数的性质。关键是先滤除噪声。按该文下标，设

$$
\bar U_n=(1-\lambda_n)\bar U_{n-1}+\lambda_nU_n,\qquad z_n=x_n-\bar U_n.
$$

则 $z_n$ 满足确定性 inexact KM，误差为 $T(x_{n-1})-T(z_{n-1})$，其范数不超过 $\lVert\bar U_{n-1}\rVert$。即使原噪声 $U_n$ 不消失，滤后噪声仍能消失。

记

$$
\pi_k^n=\lambda_k\prod_{i=k+1}^n(1-\lambda_i),\qquad \nu_n^2=\sum_{k=1}^n(\pi_k^n)^2\theta_k^2.
$$

Lemma 2.4 用 martingale difference 的正交性给出 $\mathbb E\lVert\bar U_n\rVert\le\mu\nu_n$。$\mu$ 是一般范数与 Euclidean 范数的比较常数，可能含维数依赖。

Theorem 2.5 的两项噪声条件是

$$
\sum_n\lambda_n\nu_{n-1}<\infty,\qquad \sum_n\lambda_n^2\theta_n^2<\infty.
$$

第一项使 $\sum\lambda_n\lVert\bar U_{n-1}\rVert$ 几乎必然有限。第二项控制噪声鞅。原文用 Doob 与随机逼近的极限集论证 $\bar U_n\to0$；随后调用确定性 inexact KM 的 Theorem 2.1。有限维紧性给出迭代点的强极限。

在本任务更强的条件二阶矩上界下，滤后噪声也能用二次能量解释：

$$
\mathbb E[\lVert\bar U_n\rVert_2^2\mid\mathcal F_{n-1}]\le(1-\lambda_n)\lVert\bar U_{n-1}\rVert_2^2+\lambda_n^2v_n.
$$

若 $\sum\lambda_n^2v_n<\infty$ 且 $\sum\lambda_n=\infty$，Robbins–Siegmund 先给出二次能量极限及加权级数有限，再推出极限为零。这段解释使用 Euclidean 度量分析噪声，确定性 $T$ 仍按其原范数处理。

有界方差和 $\lambda_n\asymp n^{-a}$ 给出 $\nu_n=O(n^{-a/2})$。因此第一项条件要求 $\sum n^{-3a/2}<\infty$，即 $a>2/3$。这个阈值来自这套证明，不是所有 Hilbert 随机方法的统一下界。

### 4.3 残差路径速率与期望界分开读

令 $\tau_n=\sum_{i\le n}\lambda_i(1-\lambda_i)$，$\psi(t)=\min\{1,1/\sqrt{\pi t}\}$。原文式 3 给出路径残差估计

$$
\lVert x_n-Tx_n\rVert\le\kappa\psi(\tau_n)+2\sum_{k=2}^n\lambda_k\psi(\tau_n-\tau_k)\lVert\bar U_{k-1}\rVert+4\lVert\bar U_n\rVert.
$$

这里 $\kappa$ 可以是随机常数。Example 2.7 给出的是滤后噪声 $n^b\lVert\bar U_n\rVert\to0$ 的路径结论，$b<a-1/2$。要得到原残差的具体指数，还须估计中间卷积。Theorem 4.4 的期望指数不能原封不动写成路径指数。

对一般范数，Theorem 4.4 在 $a=2/3$ 的期望残差为 $O(\log n/n^{1/6})$；该边界值没有同时满足 Theorem 2.5 的上述充分条件。选择期望界中的最优指数，不能自动继承无限轨道的迭代点结论。

## 5. 任务 D：Fast KM 的噪声权重与边界

### 5.1 能量与五个新增项

确定性能量、Lemma 3.1 式 3.1、Lemma 3.2 的参数区间，以及全部展开式见证明附录第 2–3 节。最关键的精确关系为

$$
E_{k+1}=E^{\mathrm{virt}}_{k+1}+\langle L_k,\eta_k\rangle+Q_k\lVert\eta_k\rVert^2,\qquad Q_k=\Theta(k^2).
$$

原算法复用查询时 $\eta_k=b_ke_k-c_ke_{k-1}$。新增项包括两个线性项、两个平方项和一个交叉平方项。当前新误差的线性项可借零均值消去；历史误差的线性项 $-c_k\langle L_k,e_{k-1}\rangle$ 保留。

**本次证明。** 若每步在当前点与前一点分别使用新的条件零均值查询，$\eta_k=b_ke_k-c_kf_k$ 整体条件零均值。对 $\alpha=4$，N6 给出残差与速度几乎必然 $o(1/k)$，并给出迭代点的弱极限。证明使用两组能量极限、加权可和性与路径 Opial，引理使用条件在附录逐项列明。

**待验证。** 原复用版本在一般非扩张算子和 N6 下是否具有同一结论，本次没有完成证明。只有更强的 $\sum k\lVert e_k\rVert<\infty$ 路径条件已在附录证明。

### 5.2 查询复用的抵消是真实机制

附录对 $T=0,s=1,\alpha=4$ 求得精确随机解。若 $e_k=\sigma(k+1)^{-q}Z_k$，其中 $Z_k$ 为独立标准 Gaussian，则有下列精确阈值。

| 实现 | 残差几乎必然为 $o(1/k)$ 的条件 | 额外查询成本 |
|---|---|---|
| 保存并复用上一步查询值 | $q>1$ | 每步一次新查询 |
| 每步对两个点分别重新独立查询 | $q>3/2$ | 每步两次新查询 |

复用版本中，同一个历史误差的两个系数合并后从二次增长降为常数。双查询版本的误差相互独立，无法作这一步合并。$q=1.2$ 因而是两种实现具有不同路径行为的具体例子。

该阈值只针对所述 Gaussian 零算子模型。它为研究查询复用提供证据，但没有证明一般 N6 可被同样程度地放宽。

### 5.3 N2、递减步长与所谓最优指数

**本次证明。** 固定步长和持续 Gaussian 查询噪声下，原 Fast KM 对 $T=0$ 的残差不趋于零依概率。因此仅有 N2 不足以保住原参数下的目标速率。

若为满足形式上的 N6 而令 $s_k\asymp k^{-\delta}$，$t_k\asymp k$，则 $\delta>3/2$ 确实使 $\sum s_k^2t_k^2\sigma^2$ 有限。但是，直接替换原公式中的 $s$ 会产生无噪声反例：取 $s_k=0.1/(k+1)^{1.6}$、$T=0$、$x_0=x_1=1$，残差的极限至少为 $0.888888\ldots$。

**结论。** 不能仅比较幂指数来给出 N2 下的“最优 $\delta$”。在明确有效的变步长更新与能量关系前，这个优化问题尚未成立。N2 下原固定步长实现没有正的普遍消失速率；这不排除其他算法有近最优的期望复杂度。

一维常值映射 $T_b(x)=b$ 配合 Gaussian 位置观测，已包含估计未知均值的困难。它给出期望误差的 $\Omega(\sigma/\sqrt N)$ 级别障碍。该期望障碍不等于几乎必然速率的最优性结论。iKM Theorem 1 已在一般非扩张 Hilbert 问题上给出接近这个期望数量级的上界。

### 5.4 递增批量需要付出的查询数

单样本方差为 $\sigma_0^2$，独立批量 $m_k$ 的方差为 $O(\sigma_0^2/m_k)$。

| 目标条件 | 一个明确充分的批量规则 | 运行 $K$ 步的总样本数 |
|---|---|---|
| 固定步长 N6 | $m_k=\lceil c(k+1)^{3+\varepsilon}\rceil$ | $\Theta(K^{4+\varepsilon})$ |
| 接近 N6 边界 | $m_k=\lceil c(k+1)^3\log^{1+\varepsilon}(k+2)\rceil$ | $\Theta(K^4\log^{1+\varepsilon}K)$ |
| 保守加权 RMS 绝对可和 | $m_k=\lceil c(k+1)^{4+\varepsilon}\rceil$ | $\Theta(K^{5+\varepsilon})$ |

双查询版本的总数再乘 2。所有 $c,\varepsilon$ 固定为正数。原指令用 $O(k^{4+\delta})$ 表达批量增长时，应补足下界或直接指定上述批量规则，单纯的上界不能保证噪声充分小。

附录 P1 同时证明期望平方残差 $O(K^{-2})$。结合批量成本，只得到接近 $\epsilon^{-4}$ 的充分查询数。相对近 $\epsilon^{-2}$ 的固定时域 iKM，它没有 oracle complexity 加速。相对一般范数随机 KM 或 Halpern 的 $\epsilon^{-6}$、$\widetilde\epsilon^{-5}$，还存在几何条件与输出保证不同的问题，不能只比较指数。

### 5.5 哪些 Nesterov 技巧能够移植

**可直接使用的工具：** 条件零均值消去查询前可测的线性项；Robbins–Siegmund；先证明加权可和，再证明能量极限以获得 little-o；路径 Opial；用批量控制确定的方差预算。

**需要重新推导的部分：** 算子残差不能替换成函数值误差；历史查询噪声不能视为新的 martingale difference；任意 $t_k\asymp k^r$ 与 $s_k\asymp k^{-\delta}$ 未必保持原参数恒等式；双步长设计需要明确两个更新位置和各自的 oracle，不能只借用 Nesterov 中的指数条件。

**加权 $\ell^1$ 与平方条件的区别：** 前者通过绝对值控制线性项，容许非零均值但更昂贵；后者利用零均值保留二阶代价，更弱但依赖正确的查询时序。复用误差正好是两条证明路线之间需要解决的位置。

## 6. novelol：Claim、证明与实现的对照

本次实际检查了定理假设、算法系数、噪声查询位置、能量恒等式、复杂度计数和低维反例。以下判断不只来自论文摘要。

| 可检验 Claim | Formal theorem 与假设 | Proof dependency | Oracle cost | 已完成的检查 | 剩余问题 |
|---|---|---|---|---|---|
| 随机 iKM 有近最优末次复杂度 | Theorem 1，固定 $K$，完整 $T$ 的零均值噪声 | 式 12 的时域参数；式 17 的 RMS 界 | 每步一次 | 参数依赖、输出指标、Appendix A 的不同参数已核对 | 没有据此得到同一无限轨道的原 Fast KM 定理 |
| 随机快速方法已有路径 little-o | VR Fast KM Theorem 2，有限和与差分 VR 递归 | 对整个 $Gx_k-\gamma_kGx_{k-1}$ 的新随机估计 | SVRG/SAGA 的有限和成本 | Definition 1、式 19、Theorems 1–2 已对照 | 一般独立加性查询及历史复用不自动满足该递归 |
| AFP 允许更一般 inexact oracle | v1 Theorem 2 的陈述如此 | Lemma 1 式 5 | 增长批量必须计数 | $G=0$、零误差给出式 5 的精确反例 | 该引理需修复；最终定理真伪未由此确定 |
| 双查询 Fast KM 在 N6 下具有目标路径速率 | 本次附录 P1，$\alpha=4$，可分 Hilbert | 正定能量、整体条件零均值、两组能量极限 | 每步两次 | 已给出证明与恒等式检查 | 新颖性未确认；更高查询成本和噪声阈值不能省略 |
| 复用查询可能降低噪声衰减要求 | 本次附录 P3–P4，$T=0$，Gaussian 模型 | 同一误差的系数抵消与精确线性解 | 每步一次对每步两次 | 两个闭式解及阈值已证明 | 向非线性算子或仅有 N2 的噪声推广仍待证明 |

关于 AFP 的发现需要保留准确边界：其参数使步长递减，但证明选择了一个需要为正、实际为负的 Young 参数。零算子例中，原式 5 要求能量不增，实际能量差精确为 $-1920/91$。这否定该引理按印刷形式的陈述。报告不据此否定 AFP 最终定理，也不把审阅他人论文当作主研究任务。

**经过比较的研究缺口：** 复用查询给原能量引入一个历史线性项，同时又在算法层面带来更强抵消。证明需要同时表达这两点。仅将查询重新独立化会避开历史线性项，也会改变值得保留的噪声结构。

## 7. 一个主课题与两个备选

### 7.1 主课题：双查询 Fast KM 的 N6 定理

**定理模板，本次已证明。** 附录 P1：可分 Hilbert，$\theta$-averaged，$\alpha=4$，$0<s\le1/\theta$，两个新查询的误差整体条件零均值，确定的平方加权方差预算有限。结论为类型 2、3、4；使用批量计数得到类型 5 的充分上界。

**Evidence anchor 与增量。** 原文 Lemma 3.1 的局部下降、附录精确扰动恒等式，以及原文 Theorems 3.4–3.5 的两能量证明结构。与 VR Fast KM 相比，误差模型更直接且不要求有限和；与 AFP 相比，算法系数与证明不同。不能仅凭这些差异确认可发表的新意。

**最难步骤。** 证明能量极限并不足以立即得到 little-o，须用两组 $\lambda$ 提取 $p_k$，再从 $h_k$ 有极限及 $\sum h_k/k<\infty$ 得到 $h_k\to0$。弱极限还须处理共同的概率为一事件。

**最小证伪。** 检验扰动恒等式、端点步长与纯旋转。误把前一点查询设为保存值，会破坏证明的条件零均值，必须在实现中区分。

**两周计划。** 第 1 周独立重建能量、条件下降和全部可积性条件。第 2 周完成 little-o、弱极限、期望界与批量成本，并用二维例子验证实现。

**小实验。** 已完成角度 $0.04$ 的二维旋转，$\alpha=4,s=0.75$，128 条轨道，每条 6000 步，结果见第 8 节。后续重建实验时，画 $k r_k$ 与总查询数下的残差。

**可能贡献。** 一个可独立检查的原 Fast KM 参数下的随机稳定性证明。**Novelty 判断。** 低至待验证；更适合作为证明练习和后续基准。**Soundness 风险。** 本次已完成推导，外部复核另记；它与原复用算法的结论不能互换。**下一步。** 按附录重建全证。

### 7.2 备选一：复用查询的 Fast KM 在 N6 下的路径理论

**已验证事实与 Evidence anchor。** Boţ–Nguyen 式 2.7、Lemma 3.1；本次精确扰动恒等式；附录 P3–P4 的噪声抵消。它们把研究困难定位到 $-c_k\langle L_k,e_{k-1}\rangle$。

**定理模板，待证。** 采用原 Fast KM，只保存前一次 $\widehat T$，每步一次新查询。设 $T$ 为非扩张算子，$F\ne\varnothing$，先固定 $\alpha=4$ 和严格内部步长 $0<s<1$。噪声条件零均值且 $\sum k^2v_k<\infty$。目标是证明同一无限轨道上残差与速度几乎必然 $o(1/k)$，迭代点几乎必然有弱极限，对应类型 3、4。期望界另加可积预算并单独证明。

**增量边界。** 相对 iKM，需要不同参数下的无限轨道结果；相对 VR Fast KM，需要一般加性 oracle 下原更新及历史复用的证明；相对 AFP，需要保留原系数与查询方式。检索未确认这些增量已被直接覆盖，但这不构成“尚无人证明”的证据。

**核心方法与最难步骤。** 在能量中加入历史误差的校正项，或把相邻两步线性噪声合并为一个可预测鞅增量。必须证明校正后的量仍能控制距离与残差。直接对历史线性项取绝对值，会退回更强的 $\ell^1$ 条件。

**最小证伪。** 先检验 $T=0$ 与二维旋转，再检验非线性 $T=P_C\circ R$。一个具体反例即可否定所提的一般定理；数值未发现反例不能证明定理。

**两周计划。** 第 1 周重建原能量与校正项，先完成条件期望关系和正定性，不追求最优步长。第 2 周证明加权可和、两组能量极限和距离极限。若旧噪声项在第二周结束时仍无法控制，将这个定理保留为开放目标，按主课题完成一个月的独立证明交付。

**小实验。** 比较原复用实现与双查询实现。画 $k\lVert V(x_k)\rVert$ 的单轨道曲线和 RMS 曲线；同时按总查询数作横轴。重点使用 $q=1.2,1.5,1.7$，因为它们能区分两种噪声机制。

**可能贡献。** 在明确原算法和查询成本的条件下给出路径定理；进一步的噪声条件放宽只有在证明完成后才列入贡献。

**Novelty 判断。** 待验证，已有明确的形式差异，但尚未确认公开文献是否覆盖。**Soundness 风险。** 历史误差的补偿能量尚未完成。**下一步。** 先完成该单项的可预测分解；不先扩展 Fast OGDA 或 Fast RFB。

**一个月可行性判断。** 适合作为有证据的研究尝试，不能保证一般定理必定在一个月内完成。主课题的双查询定理具有已写出的完整证明，承担入门任务。

### 7.3 备选二：仿射算子下查询复用的噪声阈值

**定理模板。** 第一阶段采用附录 P3–P4，精确比较 $T=0$、$\alpha=4,s=1$、Gaussian 衰减噪声时两种实现的必要与充分指数条件，对应类型 3；两种算法在相应条件下均趋于唯一解，对应类型 4。第二阶段将 $T$ 限制为有限维 normal 仿射非扩张算子，逐个特征模态研究噪声传递，这一推广标为待证。

**Evidence anchor 与 Gap。** 同一个历史误差在闭式解中抵消二次权重。零算子模型的两个阈值已完成推导，清楚显示独立化查询会改变噪声条件。

**与已有结果的比较。** N6 是双查询一般算子的充分条件；这一例子证明它并非复用实现的必要条件。iKM 的固定时域 RMS 界和 VR 的 estimator 条件没有直接给出该路径阈值。但仅有一维闭式解不足以宣称完整论文贡献。

**最难步骤。** 特征值接近 1 时，常数可能失去统一控制；不能把每个固定谱点的渐近式当作对所有算子统一的结论。

**最小证伪。** 先从实数缩放、二维旋转和非正规矩阵寻找与猜测阈值不同的例子。把噪声从 Gaussian 换成有限方差的稀有大误差模型，检验尾部条件是否必要。

**两周计划。** 第 1 周独立求出两种实现的闭式解、Gaussian 必要性和充分性。第 2 周完成二维模态分析与查询数相同的对照；所有常数注明谱依赖。

**小实验。** $T=0$ 上先计算精确方差，避免仿真误差；再在旋转算子上画 $k r_k$。$q=1.2$ 对两种实现有不同结论，是最便宜的区分试验。

**可能贡献。** 解释查询复用为何改善路径噪声容忍度，并指导一般非线性能量的设计。**Novelty 判断。** 单独一维结果较低；需要非平凡算子类上的统一定理才有更强价值。**Soundness 风险。** Gaussian 证明不能覆盖所有只有二阶矩约束的误差。**下一步。** 完成一个含非零旋转的模态证明后，再判断是否值得独立成题。

## 8. 已完成的小实验

所有记录保存在 `km-experiment/`。第一组只核查代数恒等式；第二组检查会影响选题的反例；随机仿真用于发现实现错误与理论边界，不能证明路径极限定理。

| 检验 | 结果 | 可以支持的判断 |
|---|---|---|
| 原能量展开与扰动恒等式，200 组随机输入 | 最大相对误差约 $5.81\times10^{-16}$ 和 $1.32\times10^{-15}$ | 两种表达在实现中一致；证明仍由代数展开提供 |
| 直接代入递减步长，无噪声，十万步 | 残差约 $0.91783745$；理论下界 $0.888888\ldots$ | 该变步长实现不能普遍解出无噪声方程 |
| 旋转算子，双查询，持续噪声，6000 步 | RMS 残差约 $6.4397$ | 与该参数下持续噪声失败相符；不据有限仿真判断普遍最优速率 |
| 同一旋转，噪声标准差 $0.1/(k+1)^{1.7}$ | RMS 残差约 $7.531\times10^{-6}$ | 与 N6 情形的推导相符 |
| 同一旋转，标准差 $0.1/(k+1)^{2.2}$ | RMS 残差约 $6.450\times10^{-6}$ | 更强绝对可和条件的基准 |
| $T=0$ 的两个闭式解与逐步更新 | 最大绝对差约 $3.66\times10^{-15}$ 和 $7.82\times10^{-14}$ | 检查查询复用和双查询的两个不同递推 |
| AFP Lemma 1 最小例子 | 有理数能量差 $-1920/91$，所声称下界为 0 | 该版本的引理按印刷形式不成立 |

对 $T=0,q=1.2,\sigma=1$，使用精确方差得到的 $n$ 倍标准差如下。指标为 $n\sqrt{\operatorname{Var}(x_n)}$，没有 Monte Carlo 抽样误差。确定初值只影响均值，因此没有进入该表；采用 $x_1=0$ 时，它也等于 $n$ 倍 RMS 残差。

| $n$ | 复用查询 | 双查询 |
|---|---|---|
| 1000 | 0.25072 | 6.95909 |
| 10000 | 0.15846 | 13.89890 |
| 100000 | 0.10000 | 27.73470 |

对应闭式解与 Gaussian 尾界的证明见附录第 6 节。

## 9. 下一次向 Boţ 提的三个问题

1. **算法对象。** 您希望首先保留 Boţ–Nguyen 式 2.7 的每步一次新查询与历史查询复用，还是接受对算子差分构造一个新的条件无偏 estimator？这会改变可用能量和样本成本。
2. **可发表增量。** 在 VR Fast KM 的 Theorem 2 和 AFP 的既有陈述附近，若我们为原参数证明一般加性 martingale oracle 下的 N6 路径定理，您认为增量是否足够，还是需要进一步利用查询复用放宽噪声条件？
3. **N2 的目标。** 持续噪声下，您更重视同一无限轨道的末次路径速率，还是近最优的期望查询复杂度？原固定步长已有失败例子，两个目标需要不同的参数和证明任务。

## 10. 原始文献与核查范围

前三篇保持指令顺序。核心书目信息使用原 PDF、arXiv 记录及出版或作者记录交叉核对；定理陈述的核查不等于全文证明已逐行通过。原始 PDF 与文字提取均保存在 `sources/`，便于复查。

1. Mario Bravo、Roberto Cominetti. *Stochastic Fixed-Point Iterations for Nonexpansive Maps: Convergence and Error Bounds*. SIAM Journal on Control and Optimization，2024。[DOI](https://doi.org/10.1137/22M1515550)，[arXiv:2208.04193v3](https://arxiv.org/abs/2208.04193)。重点核查 Theorems 2.5、2.8、2.10、4.1、4.4，Example 2.7，Proposition 5.1，Corollary 5.4。
2. Tong Yang、Tao Jiang、Yuejie Chi、Ashok Cutkosky、Lin Xiao. *Stochastic Inertial Krasnosel’skii–Mann Iteration Achieves Near-Optimal Sample Complexity*. 2026。[arXiv:2609.28543v1](https://arxiv.org/abs/2609.28543)。重点核查 Theorem 1，式 12、17，Appendix A Proposition 1。未声称已发表期刊。
3. Radu Ioan Boţ、Dang-Khoa Nguyen. *Fast Krasnosel’skiĭ–Mann algorithm with a convergence rate of the fixed point iteration of o(1/k)*. SIAM Journal on Numerical Analysis，61(6):2813–2843，2023。[DOI](https://doi.org/10.1137/22M1504305)，[arXiv:2206.09462v2](https://arxiv.org/abs/2206.09462)。本次重建 Algorithm 2.1、Lemma 3.1、Lemma 3.2、Proposition 3.3、Theorems 3.4–3.5 的关键证明结构。
4. Mario Bravo、Juan Pablo Contreras. *Stochastic Halpern iteration in normed spaces and applications to reinforcement learning*. Mathematical Programming，2026。[DOI](https://doi.org/10.1007/s10107-026-02345-1)，[arXiv:2403.12338v4](https://arxiv.org/abs/2403.12338)。重点核查 Theorem 3.3、Corollary 3.5、Theorems 3.7、3.10。
5. Mario Bravo、Roberto Cominetti、Matías Pavez-Signé. *Rates of convergence for inexact Krasnosel’skiĭ–Mann iterations in Banach spaces*. Mathematical Programming，175:241–262，2019。[arXiv:1705.09340v2](https://arxiv.org/abs/1705.09340)。
6. Patrick L. Combettes、Jean-Christophe Pesquet. *Stochastic Quasi-Fejér Block-Coordinate Fixed Point Iterations with Random Sweeping*. SIAM Journal on Optimization，2015。[DOI](https://doi.org/10.1137/140971233)，[arXiv:1404.7536](https://arxiv.org/abs/1404.7536)。Corollary 2.7 的 RMS 可和条件已直接核查。
7. Quoc Tran-Dinh. *Variance-Reduced Fast Krasnosel’skii–Mann Methods for Finite-Sum Root-Finding Problems*. [arXiv:2406.02413v4](https://arxiv.org/abs/2406.02413)，2026-09 修订。使用该版本 Definition 1、Theorems 1–2、式 19。PDF 的 MOR 页眉为占位格式，本报告不据此断言期刊发表状态。
8. Nghia Nguyen-Trung、Quoc Tran-Dinh. *A Class of Accelerated Fixed-Point-Based Methods with Delayed Inexact Oracles and Its Applications*. [arXiv:2512.13547v1](https://arxiv.org/abs/2512.13547)，2025。[作者记录](https://nghiant01.github.io/publications/)。本次对 Lemma 1 给出反例；后续 Theorem 2 的独立修复待验证。
9. Quoc Tran-Dinh. *VFOSA: Variance-Reduced Fast Operator Splitting Algorithms for Generalized Equations*. JMLR 26(254):1–68，2025。[期刊原文](https://jmlr.org/papers/v26/25-0500.html)。Theorem 14、Remark 15 核对至陈述层面。
10. Radu Ioan Boţ、Chiara Schindler. *Long-time analysis of stochastic heavy ball dynamics for convex optimization and monotone equations*. DCDS，51:439–474，2026。[DOI](https://doi.org/10.3934/dcds.2026035)。Theorem 3.5 为连续时间结果。
11. Daniel Cortild、Coralia Cartis、Juan Peypouquet. *Stochastic Krasnoselskii-Mann Iterations: Convergence without Uniformly Bounded Variance*. [arXiv:2604.22581v3](https://arxiv.org/abs/2604.22581)，2026。引用该版本作者表，核对 Theorem 2.13、Corollary 2.12 的模型与输出区别。
12. Yekini Shehu. *Adaptivity, Anchoring, and the Exact Oracle Complexity of Stochastic Fixed-Point Iterations*. [arXiv:2610.00295v1](https://arxiv.org/abs/2610.00295)。外部 RAIN reduction 未独立重建。
13. TaeHo Yoon、Nicolas Loizou. *Dual-Anchor Acceleration Is Near-Optimal for Stochastic Monotone Root-Finding*. [arXiv:2609.36033](https://arxiv.org/abs/2609.36033)，2026。核对 samplewise 假设、内循环与期望复杂度的范围。
14. Felix Lieder. *On the Convergence Rate of the Halpern-Iteration*. Optimization Letters，15:405–418，2021。[DOI](https://doi.org/10.1007/s11590-020-01617-9)，[作者原稿](https://optimization-online.org/wp-content/uploads/2017/11/6336.pdf)。Theorem 2.1 的残差界已直接核查。
15. Jongmin Lee、Mario Bravo、Roberto Cominetti. *Near-Optimal Sample Complexity for MDPs via Anchoring*. ICML 2025，PMLR 267:32907–32929。[会议原文](https://proceedings.mlr.press/v267/lee25c.html)。

本次定向检索与比较覆盖随机 KM、随机 Halpern、VR Fast KM、AFP、VFOSA 和连续时间 stochastic Fast OGDA。这个范围足以排除宽泛的新颖性表述，尚不足以认证任何候选为“首次”结果。
