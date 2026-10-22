# Boţ 系列加速方法与 splitting 算法的对应关系

检索日期：2026-10-21。

**文献身份订正：** 用户原称“Fast Inertial”的文献已明确为 Boţ–Nguyen–Zong 的 **Fast Reflected Forward-Backward algorithm: achieving fast convergence rates for convex optimization with linear cone constraints**，Journal of Scientific Computing 105(3), Article 73, 2025。它就是本报告的 **R**，对应 §2.4；RIFBF（I）仅保留为补充对照。正式出版信息已与 Springer、arXiv 和 University of Vienna 记录核对。本次仅订正文献身份，不重新核验其他技术表格。

**核心判断：现有文献已经将 Boţ 系列方法落到多种非光滑 splitting 上。与你研究最接近的三个入口是 Fast Forward–Backward、Fast Reflected Forward–Backward，以及带退化预条件器的 generalized Fast KM。真正需要逐项判断的是：算法输出哪个序列，残差属于哪个算子，以及怎样回到原问题的 KKT、目标误差和可行性。**

本报告按任务书的七部分组织。论文身份用作者主页、arXiv 和期刊／会议页面交叉核对；技术结论以列出的原文版本为准。对尚未确认的名称、未读到的完整定理和本次自行推出的对应关系分别标明。它是本次已核实的文献映射，不声称穷尽 2022–2026 年所有相关论文。

## 1. 论文清单确认结果

### 1.1 与任务书直接对应的论文

| 代号 | 作者与准确标题 | 出版信息与标识 | 本报告使用的原文及身份判断 |
|---|---|---|---|
| K | Radu Ioan Boţ, Dang-Khoa Nguyen. **Fast Krasnosel’skiĭ–Mann algorithm with a convergence rate of the fixed point iteration of o(1/k)** | SIAM Journal on Numerical Analysis 61(6), 2813–2843, 2023；[DOI](https://doi.org/10.1137/22M1504305)；[arXiv:2206.09462](https://arxiv.org/abs/2206.09462) | 已确认。应用集中在 §4、Corollary 4.1 和 §5。 |
| O | Radu Ioan Boţ, Ernö Robert Csetnek, Dang-Khoa Nguyen. **Fast Optimistic Gradient Descent Ascent (OGDA) method in continuous and discrete time** | Foundations of Computational Mathematics 25, 163–222, 2025；[DOI](https://doi.org/10.1007/s10208-023-09636-5)；[arXiv:2203.10947](https://arxiv.org/abs/2203.10947) | 以下算法／定理编号采用 arXiv v3，避免与期刊长版混用。 |
| G | Radu Ioan Boţ, Enis Chenchene, Jalal M. Fadili. **Fast Krasnoselskii–Mann method with overrelaxation and preconditioners** | IMA Journal of Numerical Analysis，2026-08-22 在线发表；[DOI](https://doi.org/10.1093/imanum/drag042)；[arXiv:2411.18574](https://arxiv.org/abs/2411.18574) | 预印本题为 **Generalized Fast Krasnoselskii-Mann Method with Preconditioners**。以下技术定位统一采用 v2：Theorem 3.3、Theorem 4.5 等；期刊版改为另一套编号。 |
| F | Radu Ioan Boţ, Dang-Khoa Nguyen, Chunxiang Zong. **Fast Forward–Backward splitting for monotone inclusions with a convergence rate of the tangent residual of o(1/k)** | Numerische Mathematik 158, 1757–1807, 2026；2026-09-10 在线发表；[DOI](https://doi.org/10.1007/s00211-026-01564-0)；[arXiv:2312.12175](https://arxiv.org/abs/2312.12175) | 已确认。可能是记忆中“Fast KM 推广”的候选，但期刊不是 SIOPT。以下使用期刊版编号。 |
| R | Radu Ioan Boţ, Dang-Khoa Nguyen, Chunxiang Zong. **Fast Reflected Forward-Backward algorithm: achieving fast convergence rates for convex optimization with linear cone constraints** | Journal of Scientific Computing 105(3), Article 73, 2025；[DOI](https://doi.org/10.1007/s10915-025-03103-9)；[arXiv:2412.11505](https://arxiv.org/abs/2412.11505) | 已确认对应用户原称“Fast Inertial”的文献。以下技术表格使用 arXiv v2，2025-10-16。最直接的 nonsmooth saddle-point／composite 应用来源。 |
| V | Michael Sedlmayer, Dang-Khoa Nguyen, Radu Ioan Boţ. **A Fast Optimistic Method for Monotone Variational Inequalities** | ICML 2023，PMLR 202, 30406–30438；[会议全文](https://proceedings.mlr.press/v202/sedlmayer23a.html)；[arXiv:2307.11281](https://arxiv.org/abs/2307.11281) | 已确认。算法名 fOGDA-VI；带 normal-cone 校正，不能理解成对 Fast OGDA 随手加投影。 |

### 1.2 扩展检索与边界文献

| 代号 | 作者、标题 | 出版信息 | 收录理由及边界 |
|---|---|---|---|
| E | Boţ, Chenchene. **Extra-Gradient Method with Flexible Anchoring: Strong Convergence and Fast Residual Decay** | SIOPT 36(3), 1420–1445, 2026；[DOI](https://doi.org/10.1137/24M1703562)；[arXiv:2410.14369](https://arxiv.org/abs/2410.14369) | 是真正的 SIOPT 候选，但研究 anchored extragradient，不是 generalized Fast KM 的多算子应用篇。 |
| H | Boţ, Nguyen. **Tikhonov regularization of monotone operator flows not only ensures strong convergence of the trajectories but also speeds up the vanishing of the residuals** | Journal of Complexity 94, Article 102029, 2026；[arXiv:2406.00852](https://arxiv.org/abs/2406.00852) | 含 Halpern 离散算法和强收敛。以下采用 arXiv v2 编号。 |
| D | Boţ, David Alexander Hulett. **Second Order Splitting Dynamics with Vanishing Damping for Additively Structured Monotone Inclusions** | Journal of Dynamics and Differential Equations 36(1), 727–756, 2024；2022 年在线；[DOI](https://doi.org/10.1007/s10884-022-10160-3)；[arXiv:2201.01017](https://arxiv.org/abs/2201.01017) | 包含 forward–backward 残差与 $f+g$ 应用；属于连续时间，不能当作离散随机复杂度定理。 |
| P | Boţ, Csetnek, Sedlmayer. **An accelerated minimax algorithm for convex-concave saddle point problems with nonsmooth coupling function** | Computational Optimization and Applications 86(3), 925–966, 2023；[DOI](https://doi.org/10.1007/s10589-022-00378-8)；[arXiv:2104.06206](https://arxiv.org/abs/2104.06206) | OGAProx；非光滑 coupling、凸非线性约束。其 $O(K^{-2})$ gap 分支使用强凹性，不能与一般单调末次残差混同。 |
| A | Boţ, Csetnek, Nguyen. **Fast Augmented Lagrangian Method in the convex regime with convergence guarantees for the iterates** | Mathematical Programming 200(1), 147–197, 2023；[arXiv:2111.09370](https://arxiv.org/abs/2111.09370) | 线性等式约束的快速 augmented Lagrangian 方法。首次预印本为 2021 年，期刊在范围内。不是自动等同于 ADMM。 |
| AD | Defeng Sun, Yancheng Yuan, Guojun Zhang, Xinyuan Zhao. **Accelerating preconditioned ADMM via degenerate proximal point mappings** | SIOPT 35(2), 1165–1193, 2025；[DOI](https://doi.org/10.1137/24M1650053)；[arXiv:2403.18618](https://arxiv.org/abs/2403.18618) | 直接使用 Fast KM／Halpern 与退化 PPA，**没有 Boţ 署名**。是“记作 SIOPT、涉及多算子”的另一个候选。以下使用 v2。 |
| I | Radu Ioan Boţ, Michael Sedlmayer, Phan Tu Vuong. **A Relaxed Inertial Forward-Backward-Forward Algorithm for Solving Monotone Inclusions with Application to GANs** | Journal of Machine Learning Research 24(8), 1–37, 2023；[期刊 PDF](https://www.jmlr.org/papers/volume24/20-267/20-267.pdf)；[arXiv:2003.07886](https://arxiv.org/abs/2003.07886) | 补充对照文献，算法名称为 RIFBF；不对应用户已明确的 Fast RFB。原文主要证明收敛；不能因 inertial 一词就填入快速末次残差率。 |

**仍待确认的名称。** “Boţ 的 SIOPT Fast KM 推广”不能据现有描述唯一定位，候选为 F、E、AD；三者问题和作者均不同。G 引用的 *Graph and Distributed Douglas–Rachford Splitting*，SIOPT 34(2), 1569–1594, 2024，DOI 10.1137/22M1535097，也是多算子线索，但本次未完成其作者与全部定理复核。

**已经确认的名称。** 用户补充的“2025_JSC_Fast Reflected Forward-Backward algorithm: achieving fast convergence rates for convex optimization with linear cone constraints”明确对应 R。此前将“Fast Inertial”关联到 I／AGLA／D 的身份猜测撤回；这些文献不能替代 R。

### 1.3 “约 2016 年 reflected forward-backward”应怎样确认

| 文献 | 识别结果 | 与当前主线的关系 |
|---|---|---|
| Yura Malitsky. **Projected Reflected Gradient Methods for Monotone Variational Inequalities** | SIOPT 25(1), 502–520, 2015；[DOI](https://doi.org/10.1137/14097238X) | 投影 VI，反射点上计算算子。 |
| Malitsky. **Proximal extrapolated gradient methods for variational inequalities** | arXiv:1601.04001，2016 初稿；Optimization Methods and Software 33(1), 140–164, 2018；[DOI](https://doi.org/10.1080/10556788.2017.1300899) | **年份最接近“2016”**。若记忆包含 proximal/composite，这篇应保留为候选。 |
| Malitsky, Matthew K. Tam. **A Forward-Backward Splitting Method for Monotone Inclusions Without Cocoercivity** | SIOPT 30(2), 1451–1472, 2020；[arXiv:1808.04162](https://arxiv.org/abs/1808.04162)；DOI 10.1137/18M1207260 | forward-reflected-backward，反射的是算子值。 |
| Volkan Cevher, Bằng Công Vũ. **A reflected forward-backward splitting method for monotone inclusions involving Lipschitzian operators** | [arXiv:1908.05912v1](https://arxiv.org/abs/1908.05912v1)，2019-08-16；本次未可靠确认期刊卷页 | **内容最符合“推广到两／三算子及 composite splitting”**：§2 RFB，§3 三算子，§4 composite monotone inclusions。 |

不能合并以下两个递推。对非线性 $B$，反射点与反射算子值一般不同：

$$
x_{k+1}=J_{\gamma A}\bigl(x_k-\gamma B(2x_k-x_{k-1})\bigr).
$$

$$
x_{k+1}=J_{\gamma A}\bigl(x_k-2\gamma Bx_k+\gamma Bx_{k-1}\bigr).
$$

第一式是 RFB 类型，第二式是 FRB 类型。Boţ–Nguyen–Zong 的 R 位于第一条谱系；随机 FRB 方差缩减文献不能不核对递推就记作随机 Fast RFB。

## 2. 逐篇对应关系

### 2.0 共用记号与结果口径

$J_{\gamma A}=(I+\gamma A)^{-1}$ 是 resolvent；当 $A=\partial f$ 时等于 $\operatorname{prox}_{\gamma f}$。$R_{\gamma A}=2J_{\gamma A}-I$ 是 reflected resolvent。Averaged 指 $T=(1-\vartheta)I+\vartheta N$，其中 $N$ 非扩张；firmly nonexpansive 对应 $\vartheta=1/2$。

Shadow sequence 指由算法状态通过 resolvent/prox 产生、实际代表原问题变量的序列。一般不能从状态弱收敛与 resolvent 的范数连续性，直接推出 shadow 弱收敛。

以下 $o(k^{-1})$ 均指**范数或表内写明的 gap**，不是平方。除标明 ergodic 的地方外，均是指定的末次序列。所有收敛定理都保留解集非空、适当闭凸函数／最大单调性等原文背景条件。

对 saddle-point 问题统一记

$$
\mathcal L(x,y)=f(x)+\Phi(x,y)-g(y),\qquad
G_{z^*}(x,y)=\mathcal L(x,y^*)-\mathcal L(x^*,y).
$$

这里固定一个鞍点 $z^*=(x^*,y^*)$。$G_{z^*}$ 不是在全部 $x,y$ 上取 supremum 的 global primal-dual gap。原文只控制它时，不扩写为全局 gap。

### 2.1 K：Fast KM 对 splitting map 的外层加速

**共同定理：** Algorithm 2.1、Theorems 3.4–3.5。对 $\vartheta$-averaged $T$，$\alpha>2$、$0<s\le1/\vartheta$，外层状态弱收敛到 $\operatorname{Fix}T$，$\lVert x_k-Tx_k\rVert=o(k^{-1})$。以下四个 splitting 都由 **§4、Corollary 4.1** 明确给出。[K]

| 位置 | 原问题 | splitting | 显式算子 | 性质 | 加速结果 | 回到原问题 | 参数 |
|---|---|---|---|---|---|---|---|
| §4，Cor. 4.1 后的特例 | $0\in Ax$；$\min f$ | PPA | $T=J_{\gamma A}$ | firm；$\vartheta=1/2$ | 外层弱收敛；残差 $o(k^{-1})$ | 极限为零点；原文未给通用 objective-gap 换算 | $\gamma>0,\alpha>2,0<s\le2$ |
| 同上，令 $B=0$ | $0\in A+C$；$\min f+h$ | FB | $T=J_{\gamma A}(I-\gamma C)$ | $C$ 为 $\beta$-cocoercive；$\vartheta=2\beta/(4\beta-\gamma)$ | 同上 | FB fixed-point residual；原文未换成统一的 $f+h$ gap | $0<\gamma\le2\beta$；$0<s\le2-\gamma/(2\beta)$ |
| 同上，令 $C=0$ | $0\in A+B$；$\min f+g$ | DR | $T=I-J_{\gamma B}+J_{\gamma A}(2J_{\gamma B}-I)$ | firm | 同上 | $J_{\gamma B}x^*$ 为解；本处不能附加未经证明的两条 shadow 弱收敛／目标率 | $\gamma>0,0<s\le2,\alpha>2$ |
| §4，式 (4.1)、Cor. 4.1 | $0\in A+B+C$；$\min f+g+h$ | Davis–Yin | $T=I-J_{\gamma B}+J_{\gamma A}(2J_{\gamma B}-I-\gamma CJ_{\gamma B})$ | A、B 最大单调，C 为 $\beta$-cocoercive；同一 $\vartheta$ | 同上 | $J_{\gamma B}x^*$ 解包含式；原文未给原目标统一误差率 | 与 FB 行相同 |
| §5.1 | 线性斜对称算子求零 | PPA 数值实例 | $T=(I+\gamma S)^{-1},S^*=-S$ | firm | 数值比较残差 | 无额外目标误差定理 | 沿用 PPA 参数 |
| §5.2，式 (5.1) | 非负正交象限与超平面的可行性问题 | DR 数值实例 | $A=N_C,B=N_D$ 代入 DR | firm | 残差／可行性数值比较 | 不能把数值图扩展为新的一般 feasibility 定理 | 沿用 DR 参数 |

**单独标明的可推导对应。** 对最大单调 A、B，$T_{PR}=R_{\gamma A}R_{\gamma B}$ 非扩张。若其不动点非空，可将其作为 K 的输入，取 $\alpha>2,0<s\le1$。这给出**Fast KM 包装的 PR map**，不是未经包装的 PR 自身的收敛定理；K 的应用节没有把这一项单列。令 $p=J_{\gamma B}z,q=J_{\gamma A}(2p-z)$，则 $z-T_{PR}z=2(p-q)$。此为本报告代数推导。

### 2.2 G：预条件器把具体 splitting 纳入同一框架

**共同定理：** arXiv v2 的 Theorem 4.5。令 $M$ 自伴、半正定，$\mathcal A$ 最大单调，

$$
J=(M+\mathcal A)^{-1}M,\qquad T=(1-s)I+sJ.
$$

要求 J 满定义，$(M+\mathcal A)^{-1}$ 在 $\operatorname{Im}M$ 上 Lipschitz；$0<s\le2$，$\alpha>2$、$\sigma>0$、$1<\theta<\alpha-1$。该文的 $\theta$ 是加速参数，**不与上一节的 averaged 常数 $\vartheta$ 混同**。结论包括 M-残差 $o(k^{-1})$ 和 shadow 弱收敛；不能对任意退化 M、任意 s 自动宣称整个原始状态弱收敛。[G]

| 位置 | 原问题 | splitting | 显式算子 | 性质 | 加速结果 | 原问题的量 | 参数 |
|---|---|---|---|---|---|---|---|
| §4.2，Th. 4.5 | $0\in\mathcal A u$ | degenerate preconditioned PPA | 上述 J、T | J 在 M 半内积下 firm | M-残差、速度 $o(k^{-1})$；$Ju_k$ 弱收敛 | 限制在 M-几何；shadow 才直接给零点 | 共用条件；完整状态另查定理分支 |
| Ex. 4.1；§4.3.1，式 (4.27) | $\min f(x)+g(Lx)$ | CP／PDHG | 下方 PDHG 显式 J；$T=(1-s)I+sJ$ | 产品空间 M-firm；M 可退化 | shadow primal-dual 弱收敛；M-残差 $o(k^{-1})$ | $G_{z^*}(\tilde x_k,\tilde y_k)=o(k^{-1})$；非 global gap | M 半正定要求 $\tau_1\tau_2\lVert L\rVert^2\le1$，另见原文冲突说明 |
| Ex. 4.2；§4.3.2，式 (4.28)–(4.29) | $0\in A_1+A_2$ | DR | $p=J_{A_1}w,q=J_{A_2}(2p-w),T_{DR}w=w+q-p$ | DR 为 firm；可由 lifted degenerate PPA 表示 | 两条 shadow 都弱收敛；$\lVert q_k-p_k\rVert=o(k^{-1})$ | 原文未换成一般 $f+g$ objective gap | 共用参数；步长可吸收到 $A_i$ |
| Ex. 4.3；§4.3.3，式 (4.30)–(4.31) | $0\in\sum_{i=1}^N A_i$；$\min\sum_i f_i$ | Graph-DRS | $T_Gw=w-Z^*q(w)$；q 是 Ex. 4.3 的逐块 resolvent 系统 | lifted M-firm；图矩阵需满足原构造 | shadow 共识及弱收敛；其 variance 为 $o(k^{-2})$ | 共识误差，不是目标误差；variance 此处为各 shadow 的离散方差 | Th. 4.5＋Ex. 4.3 的图条件 |
| §3.3.2，Remark 4.6 | 同一 fixed-point／splitting map | Optimal Halpern special case | 对同一 T 的锚点迭代 | nonexpansive 或 M-nonexpansive | 临界参数 $O(k^{-1})$；强收敛需相应定理条件 | 可在同一映射上切换加速机制；不把 O 写成 o | $\alpha=\sigma=2$ 的特例，按原文初始化 |
| §5.1；§5.4.2，式 (5.3) | 多函数和、geometric median | Graph-DRS 实验 | $A_i=\partial f_i$；median 中 $f_i(x)=\lVert x-p_i\rVert$ | 同上 | 数值观察 | 不增加超出理论的 objective 率 | 同上 |
| §5.1；§5.4.1，式 (5.2) | 斜对称求零；离散 optimal transport | PPA；PDHG | $J_{\tau S}$；OT 用 div 的线性等式约束形成 PDHG | firm／M-firm | 残差、应用表现 | OT 原模型为通量范数最小化与质量守恒 | 按对应原模型 |

**PDHG 的公式。** 对 $\mathcal L(x,y)=f(x)+\langle Lx,y\rangle-g^*(y)$，

$$
\mathcal A(x,y)=(\partial f(x)+L^*y,\ \partial g^*(y)-Lx).
$$

$$
M(x,y)=(\tau_1^{-1}x-L^*y,\ \tau_2^{-1}y-Lx).
$$

$$
\tilde x=\operatorname{prox}_{\tau_1f}(x-\tau_1L^*y),\qquad
\tilde y=\operatorname{prox}_{\tau_2g^*}\bigl(y+\tau_2L(2\tilde x-x)\bigr).
$$

J 为 $(x,y)\mapsto(\tilde x,\tilde y)$。在严格不等式 $\tau_1\tau_2\lVert L\rVert^2<1$ 下 M 强正定；等号处需要保留退化版本的额外假设。

**原文冲突必须保留。** 所查 G 的 arXiv v2 及期刊 HTML §4.3.1 写成 $\tau_1\tau_2\lVert L\rVert^2\ge1$，并把严格大于号与非退化联系起来；这与其 M 的半正定要求相冲突。上述表格的 $\le1$ 是由显示的 M 直接核算得到的适用条件，不能称为原文该段的逐字条件。期刊 HTML 也显示该冲突；未取得作者勘误。实施时采用严格小于号并核对定理前提，不能照抄该段大于号。

**Graph-DRS 的展开。** 沿用 Ex. 4.3 的图矩阵 $L,\widehat L,Z$ 和度数 $d_i$，其逐块系统写为

$$
q_i=J_{\tau A_i/d_i}\left(-\frac{2}{d_i}\sum_{h<i}(L_{hi}+\widehat L_{hi})q_h+\frac1{d_i}\sum_jZ_{ij}w_j\right).
$$

原文要求 $Z,\widehat Z\in\mathbb R^{N\times(N-1)}$、$\ker Z^*=\operatorname{span}\{\mathbf{1}\}\subset\ker\widehat Z^*$，并令 $L=ZZ^*$、$\widehat L=\widehat Z\widehat Z^*$、$d=\operatorname{diag}(L+\widehat L)$。这些矩阵不能任意选择；该方法在提升后的空间运行。

### 2.3 F：Fast FB 的实际 primal-dual 应用

F 的基础算法是

$$
y_k=z_k+\frac{k}{k+\alpha}(z_k-z_{k-1})+\left(1-\frac{\alpha}{2(k+\alpha)}\right)(y_{k-1}-z_k),
$$

$$
z_{k+1}=J_{\gamma M}(y_k-\gamma Cz_k).
$$

**它与对 $T_{FB}=J_{\gamma M}(I-\gamma C)$ 直接运行 Fast KM 不同：前向算子在 $z_k$ 评价，prox 输入含 $y_k$。**

| 位置 | 原问题 | splitting | 算子 | 性质 | rate／点收敛 | 原问题换算 | 参数 |
|---|---|---|---|---|---|---|---|
| Alg. 2.1；Th. 2.9 | $0\in M+C$ | Fast FB | 上述两行；概念上的 $T_{FB}$ 只用于比较 | M 最大单调；C 为 $\beta$-cocoercive | $z_k$ 弱收敛；$\operatorname{dist}(0,Mz_k+Cz_k)=o(k^{-1})$ | tangent residual，即同一个点上的包含式残差 | $\alpha>2,\ 0<\gamma<8(\alpha-1)\beta/(5\alpha-2)$ |
| §3.1，Alg. 3.1，Th. 3.2 | $\min f(x)+h(x)$，$Ax=b$ | preconditioned primal-dual Fast FB | $P=(\partial f+A^*\lambda,b-Ax),Q=(\nabla h,0)$；在 N-度量中分裂 $N^{-1}P+N^{-1}Q$ | N 强正定；变换后的前向算子 cocoercive | primal-dual 弱收敛；KKT residual $o(k^{-1})$ | $\lVert Ax_k-b\rVert=o(k^{-1})$；saddle-relative gap 与绝对目标误差均 $o(k^{-1})$ | $1<\frac{8(\alpha-1)}{5\alpha-2}\frac{1/\tau-\sigma\lVert A\rVert^2}{L_h}$ |
| §4 | $\min\lVert x\rVert_1+\frac12\lVert Bx-c\rVert^2$，$Ax=b$ | 上一行的实例 | $f=\lVert\cdot\rVert_1,h=\frac12\lVert B\cdot-c\rVert^2$ | 同上 | 数值验证 feasibility、objective、velocity | 非独立新定理 | §4 给定理论兼容参数 |

这里 $N(x,\lambda)=(\tau^{-1}x-A^*\lambda,\sigma^{-1}\lambda-Ax)$。其 resolvent／前向组合具体产生

$$
x^+=\operatorname{prox}_{\tau f}\bigl(v-\tau A^*\eta-\tau\nabla h(x)\bigr),
$$

$$
\lambda^+=\eta+\sigma(Ax^+-b)+\sigma A(x^+-v).
$$

$v,\eta$ 是 Algorithm 3.1 的外推状态，不能删去而声称仍是同一个加速方法。[F]

### 2.4 R：Fast RFB 将单调 Lipschitz 算子与非光滑项分离

令 M 最大单调，F 单调且 L-Lipschitz。Algorithm 1 为

$$
y_k=z_k+\frac{k}{k+\alpha}(z_k-z_{k-1})+\left(1-\frac{c}{k+\alpha}\right)(y_{k-1}-z_k),
$$

$$
w_k=z_k+y_k-y_{k-1},\qquad z_{k+1}=J_{\gamma M}(y_k-\gamma Fw_k).
$$

参数为 $\alpha>2$、$\alpha/2<c<\alpha-1$、$0<\gamma<1/(2L)$。Theorems 2.8–2.9 给弱收敛及 tangent residual $o(k^{-1})$。**无需 F cocoercive；也不要求整个 FB map averaged。**

| 位置 | 原问题 | splitting | M、F 的显式对应 | 性质 | 加速结果 | 原问题换算 | 参数 |
|---|---|---|---|---|---|---|---|
| §3.1，Alg. 2，Th. 3.1 | $\min_x\max_y f(x)+\Phi(x,y)-g(y)$ | Fast RFB primal-dual | $M=\partial f\times\partial g$；$F=(\nabla_x\Phi,-\nabla_y\Phi)$ | f、g 凸；Φ 凸–凹且全梯度 Lipschitz | primal-dual 弱收敛；tangent residual $o(k^{-1})$ | KKT residual、$G_{z^*}$ 均 $o(k^{-1})$ | 上述参数；L 为 saddle-gradient Lipschitz 常数 |
| §3.2，式 (3.3)，Alg. 3，Th. 3.2 | $\min f(x)+g(Ax)+h(x)$ | composite primal-dual Fast RFB | $M=\partial f\times\partial g^*$；$F=(\nabla h+A^*y,-Ax)$ | A 有界线性；h 凸光滑；F 单调 Lipschitz | 同上 | KKT 与 saddle-relative gap；**不自动给 $f(x_k)+g(Ax_k)+h(x_k)-F^*$** | 可用 $L=\sqrt{(L_h+\lVert A\rVert)^2+\lVert A\rVert^2}$，$\gamma<1/(2L)$ |
| §3.3，Alg. 4，Th. 3.4 | $\min f+h$，$Ax-b\in-K$ | cone-constrained primal-dual Fast RFB | $M=\partial f\times N_{K^*}$；$F=(\nabla h+A^*\lambda,b-Ax)$ | K 闭凸锥；线性 A；单调 Lipschitz F | primal-dual 弱收敛；KKT residual $o(k^{-1})$ | 原文给绝对目标误差、互补项 $\lvert\langle\lambda_k,Ax_k-b\rangle\rvert$、saddle-relative gap 的 $o(k^{-1})$ | 同上一行，且鞍点存在 |
| §4 | 线性锥约束的数值问题 | 上一行实例 | 沿用 Alg. 4 | 同上 | 数值检验理论量 | 不构成随机或非凸定理 | 按 §4 |

**从 Th. 3.4 进一步得到的可行性解释。** 若定理构造 $v_k\in N_{K^*}(\lambda_k)$，则 $v_k\in-K$，所以

$$
\operatorname{dist}(Ax_k-b,-K)\le\lVert v_k-Ax_k+b\rVert.
$$

右侧是该 KKT 证书的一个分量。因此其 $o(k^{-1})$ 控制给出同阶 cone feasibility。此行是不等式层面的直接推导，区别于原文单独列出的结论。[R]

### 2.5 O 与 V：从 smooth saddle gradient 到受约束 VI

| 论文与位置 | 原问题 | 算法 | 算子 | 性质 | rate／点收敛 | 原问题换算 | 参数 |
|---|---|---|---|---|---|---|---|
| O §1，式 (3)、(5)；Alg. 2；Th. 16–17 | 无约束 smooth convex–concave min-max | explicit Fast OGDA | $V(x,y)=(\nabla_x\Phi,-\nabla_y\Phi)$ | 单调 L-Lipschitz | 弱收敛；$\lVert Vz_k\rVert=o(k^{-1})$ | smooth saddle stationarity；没有自动的全局 primal-dual gap 换算 | $\alpha>2,0<s<1/(2L)$，按 O 的 s 记号 |
| O §5 | 线性单调求零 | Fast OGDA 实验 | 线性 V | 单调 Lipschitz | 残差数值验证 | 无非光滑 prox 或随机理论扩展 | 同上 |
| V §3，Alg. 1；Th. 3.2–3.3；Rem. 3.4 | $0\in Fz+N_C(z)$ | fOGDA-VI | $\zeta_k\in N_C(z_k)$；显式计算 normal-cone 校正 | F 单调 L-Lipschitz；C 非空闭凸；有限维 | 整个序列收敛；natural residual、restricted VI gap、tangent residual 为 $o(k^{-1})$ | constrained VI certificate；不是任意 prox-composite objective gap | $\alpha>2,0<\gamma<1/(4L)$ |
| V §4.1 | simplex 上双人 matrix game | fOGDA-VI | $F=(Ay,-A^*x),C=\Delta\times\Delta$，矩阵方向按原问题约定 | 单调斜线性 | 同上 | 受约束鞍点；需区分文中的 restricted gap 与全 simplex supremum gap | 同上 |
| V §4.2 | GAN | 数值应用 | 网络训练梯度与约束 | 不保证单调 | 实验表现 | **原文理论不因此覆盖随机非凸 GAN** | 实验参数不作为一般定理条件 |

V 的投影主步为

$$
w_k=z_k+\frac{k}{k+\alpha}(z_k-z_{k-1})-\gamma\frac{\alpha}{k+\alpha}\bigl(F(w_{k-1})+\zeta_k\bigr),
$$

$$
z_{k+1}=P_C\left[w_k-\gamma\left(1+\frac{k}{k+\alpha}\right)\bigl(F(w_k)-F(w_{k-1})-\zeta_k\bigr)\right].
$$

$\zeta_{k+1}$ 按 Algorithm 1 的投影最优性条件更新。这是算法的一部分；省略它再套用 Theorem 3.3 无效。[O, V]

### 2.6 其他加速、惯性与锚点分支

| 论文与位置 | 原问题／splitting | 显式算子或迭代 | 性质与参数 | 原文结果及边界 |
|---|---|---|---|---|
| I §1.1、§3，Th. 13；§4.1–4.2 | $0\in A+B$；nonsmooth saddle；RIFBF | $z_k=x_k+\alpha_k(x_k-x_{k-1})$；$p_k=J_{\lambda_kA}(z_k-\lambda_kBz_k)$；$x_{k+1}=(1-\rho_k)z_k+\rho_k[p_k-\lambda_k(Bp_k-Bz_k)]$ | A 最大单调，B 单调 Lipschitz；惯性、松弛、步长联动需满足原文式 (14) 等条件，本次不抄未经逐项核实的常数 | Th. 13 弱收敛；未确认通用加速末次 $o(k^{-1})$。matrix-game 与 GAN 实验不能加强理论。 |
| E Alg. 1.1、Th. 2.4、Cor. 2.6 | 单调 Lipschitz 求零；anchored extragradient | $y_{k+1}=(1-\theta\epsilon_k)x_k+\theta\epsilon_kv-\theta Mx_k$；$x_{k+1}=(x_k+\theta\epsilon_{k+1}v-\theta My_{k+1})/(1+\theta\epsilon_{k+1})$ | $0<\theta<1/L$；$\epsilon_k=a/[\theta(k+b)],a>1,b>0$ | 残差 $O(k^{-1})$，强收敛到 anchor 对解集的投影；没有把所有 prox splitting 单独实例化。 |
| H §1；§4，Th. 4.6、4.8 | nonexpansive fixed point；Halpern | $x_{k+1}=\lambda_kv+(1-\lambda_k)Tx_k$；$\lambda_k=(\alpha-1)/(k+\alpha)$ | T 非扩张，$\alpha>1$；averaged 扩展另有参数条件 | $\alpha\ge2$ 时残差 $O(k^{-1})$，强收敛；不是 $o(k^{-1})$。§1 的 Yosida 算子 $V=(I-J_{\rho A})/\rho$ 连接 PPA。 |
| D §1，式 (2)；§4，Th. 4.1 | $0\in A+B$；$\min f+g$ | $T_{\lambda,\gamma}=\lambda^{-1}[I-J_{\gamma A}(I-\gamma B)]$ | 这里 T 是**残差算子**；$B$ cocoercive；连续时间参数 $\lambda(t)\asymp t^2$、$\gamma(t)\in(0,2/L)$ 等 | 连续轨道与 shadow 的结论；梯度映射尺度写成 $o(1/\gamma(t))$，不能把 $\lambda(t)\asymp t^2$ 直接误读成原目标 $o(t^{-2})$。 |
| P §1.1–1.2；Th. 9、12、14 | $\min_x\max_y\Phi(x,y)-g(y)$；OGAProx | $y^+=\operatorname{prox}_{\sigma_kg}[y+\sigma_k((1+\theta_k)\nabla_y\Phi(x,y)-\theta_k\nabla_y\Phi(x^-,y^-))]$；$x^+=\operatorname{prox}_{\tau_k\Phi(\cdot,y^+)}x$ | Φ 在 x 凸且可非光滑，在 y 光滑凹；Th. 12 需强凹，Th. 14 双侧强性；按各定理参数方案 | Th. 9 weak＋ergodic gap $O(K^{-1})$；Th. 12 ergodic gap $O(K^{-2})$；Th. 14 linear。不是一般单调末次 $O(K^{-2})$。 |
| P §1.1 式 (5)–(6)；§5.1–5.3 | 凸非线性不等式；nonsmooth-linear；multi-kernel SVM；minimax fairness | 将非线性凸约束放入 coupling 的 proximal subproblem | 需要 coupling-prox 可执行；数值分类指标未必为理论 gap | 接近非线性结构，但不保证只使用分量 prox 与一次 Jacobian 的廉价实现；SVM 指标的理论边界原文明确说明。 |
| A 主算法与主收敛定理 | $\min f(x)$，$Ax=b$；fast ALM | augmented Lagrangian $f(x)+\langle\lambda,Ax-b\rangle+\frac{\rho}{2}\lVert Ax-b\rVert^2$ 的加速 primal-dual 更新 | 凸光滑、线性约束；特定外推与隐式更新 | 原文给 $O(k^{-2})$ 的 gap／feasibility／objective 及相应迭代点结论；本次没有逐行提取其全部参数及定理编号，不能据本行直接实施。 |

### 2.7 AD：Fast KM 真正落到 ADMM 的一篇直接文献

问题为 $\min f_1(y)+f_2(z)$，约束 $B_1y+B_2z=c$。按 AD 的变量顺序 $w=(y,z,x)$，

$$
\mathcal A(w)=(\partial f_1(y)+B_1^*x,\ \partial f_2(z)+B_2^*x,\ c-B_1y-B_2z),
$$

$$
\mathcal M(w)=\bigl((\sigma B_1^*B_1+\mathcal T_1)y+B_1^*x,\ \mathcal T_2z,\ B_1y+\sigma^{-1}x\bigr).
$$

| 位置 | splitting／算子 | 条件 | rate 与原问题量 |
|---|---|---|---|
| §3.1，式 (28)、(30)，Prop. 13 | preconditioned ADMM 的一步等价于 $J=(\mathcal M+\mathcal A)^{-1}\mathcal M$ 的 PPA 表示 | Assumptions 1–2；KKT 解存在，$\mathcal T_i\succeq0$，各子问题强单调／唯一性条件；penalty $\sigma>0$ | 这是算法等价，不是仅有相同解集。 |
| Alg. 3；Th. 18，式 (53)–(56) | 对 $T_\rho=(1-\rho)I+\rho J$ 使用加速／锚点更新 | $0<\rho\le2$；$\alpha\ge2$；仍需 Assumptions 1–2 | shadow $\bar w_k$ 收敛。$\alpha=2$：KKT residual 与目标误差 $O(k^{-1})$；$\alpha>2$：二者 $o(k^{-1})$。评价对象是原文的 shadow，不是任意外推状态。 |

AD 是 G 在应用章节明确指向的相邻成果。将它写成“Boţ 的 SIOPT ADMM 论文”不正确。[AD]

## 3. 反向汇总表

**表格口径：** 填写原文明确给出的算法／特例与结果；未填格表示本次未确认该论文作了这种实例化，不表示数学上不可能。$r$ 为对应 fixed-point residual，$t$ 为 tangent residual，$G_*$ 为固定鞍点的相对 gap。所有参数和算子条件仍以前节为准。

### 3.1 核心 Boţ 方法

| splitting | K：Fast KM | G：preconditioned GFKM | F：Fast FB | R：Fast RFB | O：Fast OGDA | V：fOGDA-VI |
|---|---|---|---|---|---|---|
| proximal point | §4／Cor.4.1；$r=o(k^{-1})$ | §4.2／Th.4.5；M-残差 $o(k^{-1})$ |  |  |  |  |
| forward-backward | §4／Cor.4.1；$r=o(k^{-1})$ | 引言列举，未单独写应用定理 | Alg.2.1／Th.2.9；$t=o(k^{-1})$ |  |  |  |
| Douglas–Rachford | §4／Cor.4.1；$r=o(k^{-1})$ | §4.3.2；shadow 差 $o(k^{-1})$ |  |  |  |  |
| Peaceman–Rachford |  |  |  |  |  |  |
| Davis–Yin | §4／Cor.4.1；$r=o(k^{-1})$ | 引言列举，未单独写应用定理 |  |  |  |  |
| Chambolle–Pock／PDHG |  | §4.3.1；M-残差、$G_*=o(k^{-1})$ | 相关 primal-dual 变体；Th.3.2，不等同原始 CP | §3.2 的另一种 primal-dual splitting，不等同原始 CP |  |  |
| ADMM |  | §4.3 引用 AD，非本篇独立实例 |  |  |  |  |
| Tseng FBF |  |  |  |  |  |  |
| forward-reflected-backward |  |  |  |  |  |  |
| reflected forward-backward |  |  |  | Alg.1／Th.2.8–2.9；$t=o(k^{-1})$ |  |  |
| extragradient |  |  |  |  |  |  |
| OGDA／optimistic 分支 |  | 连续模型比较，不是独立离散 OGDA 定理 |  |  | Alg.2／Th.16–17；$\lVert Vz_k\rVert=o(k^{-1})$ | Alg.1／Th.3.3；restricted gap、natural residual $o(k^{-1})$ |
| Halpern 型 splitting |  | §3.3.2／Rem.4.6；$O(k^{-1})$ 临界分支 |  |  |  |  |
| 多算子 Graph-DRS |  | §4.3.3；shadow variance $o(k^{-2})$ |  |  |  |  |

### 3.2 其他分支与非 Boţ 对照

| splitting | I：RIFBF | E：GEAG | H：Halpern／Tikhonov | D：splitting dynamics | P：OGAProx | A：fast ALM | AD：accelerated pADMM |
|---|---|---|---|---|---|---|---|
| proximal point |  |  | §1 Yosida 联系；具体包装见下文说明 |  |  |  | Th.7／Prop.9 的 dPPM 基础 |
| forward-backward |  |  |  | §4／Th.4.1；连续时间 |  |  |  |
| Douglas–Rachford |  |  |  |  |  |  |  |
| Peaceman–Rachford |  |  |  |  |  |  |  |
| Davis–Yin |  |  |  |  |  |  |  |
| Chambolle–Pock／PDHG |  |  |  |  |  |  |  |
| ADMM |  |  |  |  |  | ALM，不等于 ADMM | Prop.13／Th.18；KKT 与 objective 的 O／o |
| Tseng FBF | §3／Th.13；弱收敛，无本次确认的快速末次率 |  |  |  |  |  |  |
| forward-reflected-backward |  |  |  |  |  |  |  |
| reflected forward-backward |  |  |  |  |  |  |  |
| extragradient／anchored EG |  | Th.2.4／Cor.2.6；$O(k^{-1})$，强收敛 |  |  |  |  |  |
| OGDA／optimistic proximal |  |  |  |  | Th.9／12／14；ergodic O／加速／linear 分支 |  |  |
| Halpern 型 splitting |  |  | Th.4.6、4.8；strong＋$O(k^{-1})$ |  |  |  | Alg.3 的 $\alpha=2$ 分支 |

**未填格的三类原因。**

1. **原文没有单列，但数学上能够实例化。** 例如 PR 的非扩张 map 可作为 K 输入；PPA／DR map 可作为 H 的 T。需要明确说是“把已知映射代入通用定理”，不能伪造原文 Corollary。
2. **原变量下的算子类别不符。** 对一般单调 Lipschitz B，$I-\gamma B$ 未必非扩张；因而不能据解集相同，把 EG、FRB、FBF 的全部迭代都归入普通 Fast KM。增加状态、改变 metric 或建立其他性质以后可能另有对应，本次没有证明。
3. **名称相近，但递推与评价量不同。** Fast RFB 不是 FRB；fast ALM 不是 ADMM；OGAProx 的 ergodic objective/gap 加速不是 Fast OGDA 的末次算子范数率。

## 4. 算子类别、方法分支与原问题指标

### 4.1 哪个结构进入哪个理论

| 问题／splitting | 可用算子及性质 | 对应加速分支 | 必须保留的条件／边界 |
|---|---|---|---|
| PPA | $J_{\gamma A}$ firm | K、G；H 的通用输入 | A 最大单调，零点存在，resolvent 可计算 |
| FB | $J_{\gamma A}(I-\gamma C)$，$C$ cocoercive 时 averaged | K；F 为专门设计的 FB 加速 | $0<\gamma<2\beta$ 为标准 averaged 区间；K 处理其允许的端点时按 Cor.4.1。不能只用 C 单调 Lipschitz 替代 cocoercivity |
| DR／PR | $T_{DR}=(I+R_{\gamma A}R_{\gamma B})/2$ firm；$T_{PR}$ nonexpansive | K；G 增加 shadow 分析 | K 包装 PR 与纯 PR 是不同算法；shadow convergence 另有论证 |
| DY | $I-J_{\gamma B}+J_{\gamma A}(2J_{\gamma B}-I-\gamma CJ_{\gamma B})$ averaged | K；G 提供广义框架背景 | 需 $C$ cocoercive。其他文献允许更大 DY 步长，不自动保证 K 所用的同一个 averaged 常数 |
| smooth convex–concave min-max | $V=(\nabla_x\Phi,-\nabla_y\Phi)$ 单调 Lipschitz | O、E | 只有在额外 cocoercivity 下才能通过 $I-\gamma V$ 直接进入 K |
| nonsmooth convex–concave min-max | $0\in(\partial f\times\partial g)+V$ | R；约束特例 V；惯性 FBF 为 I | 多值部分不能忽略；R 用一 resolvent 加单调 Lipschitz 前向算子 |
| CP／PDHG | 产品空间 $J=(M+\mathcal A)^{-1}M$ M-firm | G | 强正定 M 是真正等价范数；半正定 M 时需要 shadow／退化 Opial 与映射正则性 |
| ADMM | lifted KKT 系统的 degenerate PPA；也有对偶 DR 解释 | AD；与 G 相邻 | 子问题可解与唯一性、范围条件、松弛范围必须核对，不能只按“ADMM=DR”口号代入 |
| 非线性 $f+r\circ A$／弱凸 saddle | saddle operator 可能非单调 | 不自动进入 K/O/F/R | 需要局部／正则化／弱单调理论，或不同的 stationarity 度量；这是结构变化，不是符号替换 |

### 4.2 三条引用关系的确切含义

**PDHG 与 PPA。** He–Yuan，*Convergence Analysis of Primal-Dual Algorithms for a Saddle-Point Problem: From Contraction Perspective*，SIAM Journal on Imaging Sciences 5(1),119–149,2012，DOI [10.1137/100814494](https://doi.org/10.1137/100814494)，是相关早期结构解释。当前可直接核对的显式 M、J 和加速应用为 G 的 Example 4.1 与 §4.3.1。本次不为未读到的 He–Yuan 公式臆造编号。

**ADMM 与对偶 DR。** Gabay，*Applications of the Method of Multipliers to Variational Inequalities*，Studies in Mathematics and its Applications 15,299–331,1983，DOI [10.1016/S0168-2024(08)70034-1](https://doi.org/10.1016/S0168-2024(08)70034-1)，为这一关系的经典来源。对本报告中的具体 accelerated preconditioned ADMM，应以 AD 的 Proposition 13 核对完整递推与条件，而非仅援引历史归属。本次未逐页核对 Gabay 的原始证明。

**DY residual 与 objective。** Davis–Yin，*A Three-Operator Splitting Scheme and its Optimization Applications*，Set-Valued and Variational Analysis 25(4),829–858,2017，DOI [10.1007/s11228-017-0421-z](https://doi.org/10.1007/s11228-017-0421-z)，[arXiv:1504.01032](https://arxiv.org/abs/1504.01032)。本次核对其预印本 §4、Appendix D，尤其 Corollary D.3。

该文先控制在两个不同 shadow 上取值的目标组合；若希望统一在同一个 shadow 上计算完整目标，需要额外正则性。例如 f 在相关有界区域 L-Lipschitz 时，直接有

$$
(f+g+h)(x_g)-F^*\le f(x_f)+g(x_g)+h(x_g)-F^*+L\lVert x_g-x_f\rVert.
$$

这里 $\lVert x_g-x_f\rVert$ 与 fixed-point residual 对应。**这说明额外假设用在“不同 shadow → 同一原变量目标”这一步。** Davis–Yin 的原算法 objective 率不能仅因 K 使用同一 T，就连同原来的能量推导整体移植给 Fast KM。预印本 PDF 截图接口失败，相关公式按可提取的原文文本核对；不声称已经视觉核对该页排版。

### 4.3 能直接换算与不能直接换算的量

**PPA：** $p=J_{\gamma A}x$ 给出 $(x-p)/\gamma\in Ap$。因此原 map residual 控制 shadow 上的一项包含式残差。这是 resolvent 恒等式；并不自动给目标误差。

**FB：** $p=J_{\gamma A}(x-\gamma Bx)$ 时

$$
\frac{x-p}{\gamma}-Bx\in Ap.
$$

若 B 为 L-Lipschitz，则构造的真实包含式证书满足

$$
\operatorname{dist}(0,Ap+Bp)\le(\gamma^{-1}+L)\lVert x-p\rVert.
$$

这是本报告直接推导。即便只知道 $T_{FB}$ 的残差，也能得到 **shadow p 上**的 KKT/tangent certificate；不能把评价点误写成 x。

**预条件 PPA：** $p=Jx$ 给出 $M(x-p)\in\mathcal A p$。由于 M 半正定有界，

$$
\lVert M(x-p)\rVert\le\sqrt{\lVert M\rVert}\,\lVert x-p\rVert_M.
$$

因此 M-残差可控制一个真实 KKT 证书，但 M-距离不控制 $\ker M$ 方向的状态距离。两种问题需要分开。

**目标差：** 有约束／非光滑函数可能取 $+\infty$；状态 x 未必处于全部函数定义域。没有原文推导或额外 Lipschitz／有界乘子等条件时，报告一律保留“原文未换算”，不把 residual rate 自动写成 objective rate。

## 5. 随机与 inexact 版本

### 5.1 首先按噪声进入位置分类

**外部加性模型。** 若整个算子评价直接满足 $\widehat T_k(x)=T(x)+\xi_k$ 且 $\mathbb E[\xi_k\mid\mathcal F_k]=0$，则是 full-map 条件无偏。随机 KM、某些随机 iKM 定理可直接从这一模型出发，但仍需它们各自的矩／步长／误差条件。

**前向随机梯度后接 prox。** 对

$$
T(x)=J_{\gamma A}(x-\gamma Bx),\qquad
\widehat T(x)=J_{\gamma A}(x-\gamma(Bx+\xi)),
$$

即使 $\mathbb E[\xi\mid\mathcal F]=0$，也不能推出 $\mathbb E[\widehat T(x)\mid\mathcal F]=T(x)$。**随机梯度位于前向步骤，并不代表它在整个 prox 映射外部；在上述计算图中，它进入 prox 输入内部。**

由 resolvent 非扩张性只能直接得到

$$
\mathbb E[\lVert\widehat T(x)-T(x)\rVert^2\mid\mathcal F]\le\gamma^2\mathbb E[\lVert\xi\rVert^2\mid\mathcal F].
$$

应将误差分为

$$
b_k=\mathbb E[\widehat T_k(x_k)\mid\mathcal F_k]-T(x_k),\qquad
\zeta_k=\widehat T_k(x_k)-\mathbb E[\widehat T_k(x_k)\mid\mathcal F_k].
$$

于是全映射误差为 $b_k+\zeta_k$。偏差可有上界，但不能未经证明置零。VFOSA／VAPEG 的 estimator 分析及 iKM 的 bias 模型正与此相关。

**先 prox 后采样。** 对 exact $p=J_{\lambda A}x$，

$$
\widehat G_\lambda(x)=\widehat B(p)+(x-p)/\lambda,
$$

若 $\widehat B(p)$ 在给定查询历史后无偏，则该方向也无偏。这是 VR-FKM §5 的 backward-forward 结构能够保留无偏性的原因之一；不是普通 stochastic FB 的同一个顺序。

### 5.2 已核对的主要随机文献

| 代号 | 身份与原文 | 结果位置与边界 |
|---|---|---|
| S1 | Bravo–Cominetti，**Stochastic Fixed-Point Iterations for Nonexpansive Maps: Convergence and Error Bounds**，SIAM J. Control Optim.62(1),191–219,2024；[DOI](https://doi.org/10.1137/22M1515550) | Th.2.5、2.8 点收敛；Th.2.10–2.11 与 Th.4.4 residual 界。普通 SKM，不是加速算法；完整 T 的鞅差误差模型不能自动由随机 prox 得到。 |
| S2 | Yang–Jiang–Chi–Cutkosky–Xiao，**Stochastic Inertial Krasnosel’skii-Mann Iteration Achieves Near-Optimal Sample Complexity**，[arXiv:2609.28543v1](https://arxiv.org/abs/2609.28543v1)，2026 | §2.2、Th.1；允许 full-map bias；有限时域末次残差，参数依赖 K；不能直接记成同一无限轨道的 a.s. 快速率。 |
| S3 | Quoc Tran-Dinh，**Variance-Reduced Fast Krasnosel’skiǐ-Mann Methods for Finite-Sum Root-Finding Problems**，[arXiv:2406.02413v4](https://arxiv.org/html/2406.02413v4)，2026-09-09 版 | Assumption1.1 平均 cocoercivity；Th.3.2、3.4；§5 Lemma5.1、Th.5.2 backward-forward。新版结论不能全部记作 2024 已有。 |
| S4 | Quoc Tran-Dinh，**VFOSA: Variance-Reduced Fast Operator Splitting Algorithms for Generalized Equations**，JMLR26,1–68,2025；[官方全文](https://www.jmlr.org/papers/v26/25-0500.html) | Th.12–14；Cor.21；Appendix D。FBS／BFS、finite-sum／expectation、允许不同 estimator 结构；a.s. 结论需定理的累计误差与参数条件。 |
| S5 | Tran-Dinh–Nguyen-Trung，**New Accelerated Past-Extragradient Methods with Variance Reduction for Generalized Equations**，[arXiv:2508.16791v2](https://arxiv.org/html/2508.16791v2)，2026-09-09 版 | Th.3.1–3.2、Cor.3.4、§4；多值包含式与 biased/unbiased estimators。不能概括成任意非单调或任意持续方差下的加速。 |
| S6 | Nguyen-Trung–Tran-Dinh，**A Class of Accelerated Fixed-Point-Based Methods with Delayed Inexact Oracles and Its Applications**，[arXiv:2512.13547v1](https://arxiv.org/html/2512.13547v1)，2025 | 一般 delayed/inexact 条件；随机与 finite-sum 分支。存在通用框架不等于本报告每个 splitting 已有对应实现。 |
| S7 | Xufeng Cai, Chaobing Song, Cristóbal Guzmán, Jelena Diakonikolas，**Stochastic Halpern Iteration with Variance Reduction for Stochastic Monotone Inclusions**，NeurIPS2022；[arXiv:2203.09436](https://arxiv.org/abs/2203.09436) | 直接的随机加速包含式文献。检索确认其 expected residual／oracle complexity；本报告不额外给未经核对的 a.s. 同阶命题。 |
| S8 | Chambolle–Ehrhardt–Richtárik–Schönlieb，**Stochastic Primal-Dual Hybrid Gradient Algorithm with Arbitrary Sampling and Imaging Applications**，SIOPT28(4),2783–2808,2018；[arXiv:1706.04957](https://arxiv.org/abs/1706.04957)；DOI10.1137/17M1134834 | 随机 block sampling，含额外强性／结构下的加速分支；不能记成一般凸 last-iterate a.s. $o(k^{-1})$。 |
| S9 | Yakun Dong, Kristian Bredies, Hongpeng Sun，**A Stochastic Preconditioned Douglas–Rachford Splitting Method for Saddle-Point Problems**，SINUM63(4),1691–1728,2025；[arXiv:2212.13001](https://arxiv.org/abs/2212.13001)；DOI10.1137/23M1622490 | stochastic preconditioning、a.s. 点收敛、expected ergodic restricted gap；不能写成一般 Fast DR 的末次加速定理。 |
| S10 | Ahmet Alacaoglu, Yura Malitsky, Volkan Cevher，**Forward-reflected-backward method with variance reduction**，COAP80,321–346,2021；[DOI](https://doi.org/10.1007/s10589-021-00305-3) | 原文分析 VR-FRB 的收敛／ergodic rate，强单调情形另有 linear 结论；它不是 R 的原始 Fast RFB 系数。 |
| S11 | Jianchao Bai, William W. Hager, Hongchao Zhang，**An Inexact Accelerated Stochastic ADMM for Separable Convex Optimization**，COAP81(2),479–518,2022；[arXiv:2010.12765](https://arxiv.org/abs/2010.12765)；DOI10.1007/s10589-021-00338-8 | smooth finite-sum＋非光滑约束结构；加速随机内层与外层 ADMM 成本需区分；不是 AD 的同一随机递推。 |
| S12 | Jian-Chao Bai, Feng-Miao Bian, Xiao-Kai Chang, Lin Du，**Accelerated Stochastic Peaceman-Rachford Method for Empirical Risk Minimization**；[DOI](https://doi.org/10.1007/s40305-023-00470-8) | 身份可按 DOI 定位；本次没有核完正式卷年与全部定理，只作为 PR 的已检索候选，不据此确认一般加速末次/a.s. 率。 |
| S13 | Konstantin Mishchenko, Peter Richtárik，**A Stochastic Decoupling Method for Minimizing the Sum of Smooth and Non-Smooth Functions**，[arXiv:1905.11535](https://arxiv.org/abs/1905.11535) | 多个非光滑项的随机 decoupling 近邻；不是对原始 Fast DY 的完整随机化证明。 |
| S14 | Mario Bravo, Juan Pablo Contreras，**Stochastic Halpern iteration in normed spaces and applications to reinforcement learning**，Mathematical Programming，2026；[arXiv:2403.12338](https://arxiv.org/abs/2403.12338)；[DOI](https://doi.org/10.1007/s10107-026-02345-1) | 一般范数随机 Halpern、误差累计与采样成本；算子随机化前提仍需核对。 |

### 5.3 每个 splitting 的随机对应与误差位置

| splitting | 已找到的加速／inexact 路径 | 随机误差进入位置 | 能否直接得到 full-map 无偏模型 | 本次确认的范围 |
|---|---|---|---|---|
| PPA | S2/S6 的通用 inexact-map 框架；S7 的包含式方向 | resolvent 近似求解；或者随机 A 后求 resolvent | 随机 $J_{A_\xi}$ 的均值一般不等于 $J_{\mathbb EA_\xi}$；需偏差／求解精度条件 | 通用框架可研究；未确认覆盖全部随机 resolvent 的同一快速 a.s. 定理 |
| FB | S4 VFOSA；S3 的 BFS 另一个顺序 | 随机 B 后进入 prox；或 exact prox 后随机 B | 前者不自动无偏；后者在条件无偏采样下可保持方向无偏 | S4 已有 expected/as residual 率及点收敛，条件不是仅“二阶矩有界” |
| DR | S9 stochastic preconditioned DR；S2/S6 对有误差完整 map 的抽象路线 | 两个 prox、随机 block／子问题误差 | prox 非线性及复合传播会产生 bias | S9 为重要收敛／ergodic 基准；未确认原始 Fast DR 的一般对应加速结论 |
| PR | S12 | ERM 子问题内的加速随机计算 | 不能将内层随机误差自动看成完整 reflected map 无偏 | 完整卷年、定理、末次／平均指标待核实 |
| Davis–Yin | S13；一般 inexact-map S2/S6 | 随机 C 经第二个 prox；也可能近似两个 prox | 不自动无偏；两个 shadow 的误差分别传递 | 本次未确认与 K 的 Fast DY 同一系数、同一噪声模型的现成定理 |
| CP／PDHG | S8 的随机 block 加速；S9 的近邻；一般 inexact-map 框架 | 随机更新 dual blocks，或 prox 前的梯度／线性算子采样 | block 更新的平均不等于完整同步 PDHG 步；需坐标采样理论 | 部分强性下加速与 a.s. 收敛结果分别存在，不能合并成任意凸末次快速 a.s. 定理 |
| ADMM | S11；S6 的抽象 inexact 解释需另核 | 内层随机梯度／近似 primal 子问题；dual update 继承误差 | 不自动全映射无偏 | 需计算内层原始样本总量，不只数外层 ADMM 轮次 |
| Tseng FBF | Boţ–Mertikopoulos–Staudigl–Vuong 的 minibatch FBF；Boţ 合作者 Tseng/GAN 文献；S5 是加速近邻 | 两次 forward evaluation，第二次查询点依赖第一次；prox 内外都有噪声 | 两个查询各自无偏不代表整个更新对过去无偏；样本复用须重算 | 原始 RIFBF 的具体随机加速率未在本次确认 |
| forward-reflected-backward | S10 VR-FRB；S5 optimistic/past-EG 近邻 | 当前与历史估计器差分 | 旧误差已在 filtration 中；必须使用估计器递推 | 已有 VR 分析；不等于任意历史误差可用一次条件期望消去 |
| reflected forward-backward | S5、S4 提供近邻框架 | 反射评价点内的随机算子，再进入 resolvent | 一般带 prox-induced bias；也有旧状态相关性 | 未确认 R 的原始全部系数直接被哪一现有定理覆盖；不据此宣布新颖性 |
| extragradient | S7 stochastic Halpern/extra-gradient；S5 past-EG | 两阶段 oracle；相关采样或独立批量 | 应按阶段 filtration 表述，不按原始历史一次性假定全部无偏 | 加速 expected complexity 已有；a.s. 率需另看各文定理 |
| OGDA | S5 在多值部分为零时的 optimistic 近邻；S3 有相关差分估计结构 | 当前／历史 oracle 差分 | 条件均值不为零的旧误差不能直接删除 | 现有类已有随机加速，原始 O 参数与实现仍需逐式匹配 |
| Halpern 型 splitting | S7、S14；G 的确定性 special case | 完整 map 的扰动、递增 batch 或 VR estimator | 取决于采样计算图；随机 prox 不自动无偏 | 不同范数、输出与采样成本模型分别成立 |

**补充的非加速／不同口径基准。** Boţ–Mertikopoulos–Staudigl–Vuong，*Minibatch Forward-Backward-Forward Methods for solving Stochastic Variational inequalities*，Stochastic Systems 11(2),112–139,2021；Böhm–Sedlmayer–Csetnek–Boţ，*Two Steps at a Time—Taking GAN Training in Stride with Tseng’s Method*，SIAM Journal on Mathematics of Data Science 4(2),750–771,2022，DOI10.1137/21M1420939；Alacaoglu–Fercoq–Cevher，*On the convergence of stochastic primal-dual hybrid gradient*，SIOPT32,1288–1318,2022，DOI10.1137/19M1296252。这些结果有助于检验随机稳定性，不能与一般凸加速末次率混列。

**本节没有建立全新随机定理。** 通用框架可以接收某种 inexact oracle，和某个实际 prox／ADMM／PDHG 采样实现满足该 oracle 条件，是两个需要分别证明的命题。

## 6. 结构带来的研究问题

**本节为依据前述文献和直接计算提出的判断，不是文献已经证明的结论，也不是全领域新颖性声明。** 仓库中的 `research/untitled folder/Radu讨论_非线性复合优化与分裂算法.md` 研究的是 $f(x)+r(A(x))$，其中 A 可非线性；这一点不能被 $f+g\circ L$ 的线性理论替代。

### 6.1 非线性 composite 的 Fenchel 表示不自动产生单调 saddle operator

结构：

$$
\min_x f(x)+r(A(x))
=\min_x\sup_y f(x)+\langle A(x),y\rangle-r^*(y).
$$

前向算子为

$$
B(x,y)=(\nabla f(x)+JA(x)^*y,-A(x)).
$$

若 A 非线性，仅有 r 凸、f 凸或弱凸，不能保证 B 单调或全局 Lipschitz。**甚至原 composite 目标本身凸，也不保证这一 saddle 表示满足凸–凹假设。**

直接检验：$f=0,r(u)=|u|,A(x)=x^2$，则原目标为 $x^2$，但 saddle coupling 为 $yx^2$，$y\in[-1,1]$。取 $(x,y)=(1,-1)$ 与 $(0,-1)$，上述 B 的单调性配对等于 $-2$。因此不能直接调用 O／R 的单调 Lipschitz 定理。

**最近文献：** P 的非光滑凸–凹 coupling；Boţ–Böhm，*Alternating Proximal-Gradient Steps for (Stochastic) Nonconvex-Concave Minimax Problems*，SIOPT33(3),1884–1913,2023，DOI [10.1137/21M1465470](https://doi.org/10.1137/21M1465470)，[arXiv:2007.13605](https://arxiv.org/abs/2007.13605)；Drusvyatskiy–Paquette，*Efficiency of Minimizing Compositions of Convex Functions and Smooth Maps*，Mathematical Programming178,503–558,2019，DOI [10.1007/s10107-018-1311-3](https://doi.org/10.1007/s10107-018-1311-3)。

**仍需解决的具体问题：** 在用户希望的 single-loop、分量 prox 可计算条件下，能否利用局部弱单调性、正则化或误差界控制 dual tracking，并给可实现的驻点证书与总一阶复杂度？不能把确定性 monotone residual 的 $o(k^{-1})$ 原样作为目标问题结论。

### 6.2 随机 prox 产生的 bias 与历史复用一起进入加速能量

结构：对 $f+\mathbb E h_\xi$ 或非光滑 saddle，在 forward 算子中采样，随后 prox。第 5.1 节已给出 bias 来源。

**最近文献：** S4 VFOSA、S5 VAPEG 已处理多种 biased/unbiased estimator；S2 对完整 map 明确允许 bias；S3 用 BFS 顺序保留方向无偏。因此“随机 prox 有偏”本身不是研究空白。

**具体待证问题：** 对选定的 Fast RFB／preconditioned Fast KM 递推，给出真实采样实现的 conditional bias、方差和时间相关性界，再证明加速末次证书及无限轨道点收敛。比较是否减少总样本成本，不能只比较一个抽象噪声可和条件。旧查询值复用与在旧点重新采样必须分开。

### 6.3 退化 metric 的快速残差与随机状态稳定性并不相同

结构：PDHG 临界步长、lifted DR／ADMM 中 M 仅半正定。M-残差对 $\ker M$ 方向不敏感；随机误差可能沿这些方向累积。G 的 deterministic shadow 定理需要映射在 $\operatorname{Im}M$ 上的 Lipschitz 性等条件。

**最近文献：** G、AD；S9 的 stochastic preconditioned DR；S8 与随机 PDHG 收敛工作。2026 年还有 Ning Zhang、Benqi Liu、Liwei Zhang 的 *Halpern-Accelerated Majorized ADMM with Optimal Non-Ergodic Convergence under Degenerate Preconditioning*，[arXiv:2609.38808](https://arxiv.org/abs/2609.38808)，作为最新近邻；本次没有逐定理审计其全部参数。

**具体待证问题：** 在明确的误差位置与 range compatibility 下，是否能同时控制 M-残差、真实 primal-dual shadow 的 almost-sure 收敛、KKT 证书和成本？S9 已解决重要的随机点收敛／ergodic 部分，不能概括为“退化 metric 没有随机理论”。

### 6.4 多个非光滑项的 shadow residual 未必是原目标精度

结构：DY／DR 中 $x_A$ 与 $x_B$ 分别属于不同函数定义域。当一个函数是约束集合的 indicator，完整目标在另一个 shadow 上可能为 $+\infty$，即便 $\lVert x_A-x_B\rVert$ 已经很小。

**最近文献：** K 的 Corollary4.1；G 的 shadow 收敛；Davis–Yin Corollary D.3 的额外 Lipschitz 换算；F／R／AD 对具体结构完成的 KKT 与 objective 转换。

**具体待证问题：** 对所选 composite 结构提供可计算、有限且对应原问题的输出证书；必要时输出一对 shadow／primal-dual pair，或者进行可行性恢复。不能只换一个 residual 名称便声称改善了原问题复杂度。

### 6.5 可计算的分裂与“对整个耦合函数做一次 prox”有成本差别

结构：P 可以处理某些非线性凸约束，因为它允许计算 $\operatorname{prox}_{\tau\Phi(\cdot,y)}$。对于 $\Phi(x,y)=f(x)+\langle A(x),y\rangle$，这个 proximal 子问题可能与原问题一样难，不能把它等同于一个原始一阶调用。

**最近文献：** P；Drusvyatskiy–Paquette 的 prox-linear 内层求解；Boţ–Böhm 的随机非凸–凹 proximal-gradient；F／R 的线性 composite 完全分裂实现。

**具体待证问题：** 在不要求精确求解耦合 prox 的前提下，利用一次 Jacobian/adjoint-Jacobian 计算和分量 prox，建立 tracking-error 能量与 stationarity complexity。这里“算法可实现性＋误差传播＋原问题证书”比仅补一个 almost-sure 结论更能形成与你原研究的连接。

**针对当前课题的取舍。** 要保留已有 stochastic Fast KM 积累，先用一个明确的 splitting（Fast RFB 的 nonsmooth saddle，或 G 的 Fast PDHG）检验实际 oracle 与误差传播。要进入仓库的非线性 A 主问题，则把单调性失效和耦合 prox 成本作为实质数学障碍。不要同时把所有 splitting 随机化；也不要把一般随机加速 monotone inclusion 已有结果重新命名为新问题。

## 7. 待核实事项与资料范围

### 7.1 仍未完成的核对

| 事项 | 当前可以说什么 | 还不能说什么 |
|---|---|---|
| “SIOPT 的 Boţ Fast KM 推广” | F、E、AD、Graph-DRS 是不同候选；F 实际 Numerische Mathematik，G 实际 IMAJNA | 不能凭描述选定一篇并将其他作者归给 Boţ |
| Cevher–Vũ RFB 正式卷年 | arXiv 身份、方法、两／三算子应用已确认 | 正式期刊卷页本次未确认，不能写作“2016 的 RFB” |
| G 的 PDHG 步长符号 | 显示的 M 要求乘积 ≤1；应用段 ≥1 与之冲突 | 未取得作者勘误；不能声称该冲突已由期刊修复 |
| G 的参数和版本 | 表内 Theorem4.5／Example4.1 等均属于 arXiv v2；期刊为 Theorem4／Example1 等另一编号 | 不跨版本混搭定理编号；§4.3.3 参数区间若与 Alg.1 不同，应回到 Th.4.5 核对 |
| I、P、A 的全部参数 | 方法结构与主结论分支已定位；I、P 的精确联动参数未全部录入，A 仅提取身份及主要范围 | 本报告不是这三篇的逐行实现规范，不能据未列参数运行并宣称定理保证 |
| 随机 PR S12 | 标题、作者与 DOI 可定位 | 完整 theorem、正式年份、rate 指标待全文核对 |
| stochastic Fast DY／Fast RFB／Fast DR | 已给出具体近邻与 full-map 噪声条件障碍 | “本次未确认同一递推的定理”不能写成“领域无人研究” |
| 2026 three-operator 最新候选 | 检索出现加速 three-operator 新稿线索 | 未完成原文核查的候选不纳入已证覆盖表 |
| He–Yuan／Gabay 原始证明 | 身份与历史关系已定位，当前具体公式由 G／AD 核对 | 未逐页核实的历史原始定理不虚构编号 |
| Davis–Yin PDF | 文本读取及关键 Corollary D.3 已核对 | web screenshot 对该 PDF 连续失败；未声称视觉复核公式排版 |
| 全文“所有应用”的穷尽性 | K、G、F、R、V 的主要 applications、special cases 与实验联系已逐项提取 | 对所有扩展候选，尚不能声称检索已穷尽整个 2022–2026 作者群的全部 Remark／Example |

### 7.2 实际使用的仓库材料

仓库通过 GitHub 连接器读取；未写入仓库。此次用到的主要文件为：

1. `README.md`：确认现有项目范围与证明状态。
2. `research/roadmap_20261014/261014-领域roadmap-随机快速不动点.md`：作为文献线索，不以历史总结代替原文定理。
3. `research/roadmap_20261014/sources/generalized_fast_km.txt`：确认 G 的正式出版标题、作者和 DOI。
4. `research/memory/readings/sources/vr_splitting.txt`：VFOSA 期刊版本线索。
5. `research/memory/readings/sources/delayed.txt`：AFP 版本和问题设定。
6. `research/untitled folder/Radu讨论_非线性复合优化与分裂算法.md`：确认用户真正的 nonlinear composite／single-loop primal-dual 方向。
7. 仓库递归目录：定位已有 `fast_km.txt`、`fast_ogda.txt`、`ikm.txt` 等资料；“在目录中找到”不表示这些文件本轮全部逐行重读。

任务依据是用户上传的 `261021-gptpro-prompt-splitting-link.md`。本轮外部核查以作者发表目录、论文原文、arXiv 版本记录、Springer／SIAM／Oxford／PMLR／JMLR 页面为主。此前聊天中独立推导的两个随机 Fast KM 命题未作为公开文献或已确立定理使用。

### 7.3 核心原文入口

- [Boţ 作者发表目录](https://www.mat.univie.ac.at/~rabot/publications.html)
- [K：Fast KM 原文](https://arxiv.org/pdf/2206.09462)
- [O：Fast OGDA v3](https://arxiv.org/abs/2203.10947v3)
- [G：generalized Fast KM v2](https://arxiv.org/html/2411.18574v2)
- [G：期刊正式标题和版本](https://academic.oup.com/imajna/advance-article/doi/10.1093/imanum/drag042/8768710)
- [F：Fast FB 期刊全文](https://link.springer.com/article/10.1007/s00211-026-01564-0)
- [R：Fast RFB v2](https://arxiv.org/html/2412.11505v2)
- [R：JSC 正式出版版本](https://link.springer.com/article/10.1007/s10915-025-03103-9)
- [R：University of Vienna 出版记录](https://ucrisportal.univie.ac.at/en/publications/fast-reflected-forward-backward-algorithm-achieving-fast-converge/)
- [V：fOGDA-VI 会议全文](https://proceedings.mlr.press/v202/sedlmayer23a/sedlmayer23a.pdf)
- [I：RIFBF 期刊全文](https://www.jmlr.org/papers/volume24/20-267/20-267.pdf)
- [AD：preconditioned ADMM v2](https://arxiv.org/html/2403.18618v2)
- [S3：VR-FKM v4](https://arxiv.org/html/2406.02413v4)
- [S4：VFOSA 期刊全文](https://www.jmlr.org/papers/volume26/25-0500/25-0500.pdf)
- [S5：VAPEG v2](https://arxiv.org/html/2508.16791v2)
- [S6：AFP v1](https://arxiv.org/html/2512.13547v1)

[K]: https://arxiv.org/pdf/2206.09462
[O]: https://arxiv.org/abs/2203.10947v3
[G]: https://arxiv.org/html/2411.18574v2
[F]: https://link.springer.com/article/10.1007/s00211-026-01564-0
[R]: https://arxiv.org/html/2412.11505v2
[V]: https://proceedings.mlr.press/v202/sedlmayer23a.html
[I]: https://www.jmlr.org/papers/volume24/20-267/20-267.pdf
[E]: https://arxiv.org/abs/2410.14369
[H]: https://arxiv.org/html/2406.00852v2
[D]: https://link.springer.com/article/10.1007/s10884-022-10160-3
[P]: https://link.springer.com/article/10.1007/s10589-022-00378-8
[A]: https://arxiv.org/abs/2111.09370
[AD]: https://arxiv.org/html/2403.18618v2
