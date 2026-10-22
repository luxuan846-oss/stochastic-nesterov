---
title: "Bravo–Cominetti 2024 随机 KM 精读"
date: 2026-10-14
tags: [stochastic-KM, fixed-point, paper-reading]
source: "https://doi.org/10.1137/22M1515550"
fontsize: 11pt
papersize: a4
---

## 1. 论文定位与阅读约定

**本文证明：有限维赋范空间中的普通随机 Krasnosel’skii–Mann 迭代，在合适步长与噪声条件下，迭代点几乎必然收敛到一个随机不动点；原始末次迭代的残差还满足可计算的期望误差界。** 本文允许持续存在的鞅差噪声，也允许二阶矩按受控方式增长。

相对 Combettes–Pesquet 的随机 quasi-Fejér 框架，本文主要增加一般有限维范数下的分析、持续鞅差噪声的处理以及显式末次残差界。Combettes–Pesquet 的结果覆盖可分无限维 Hilbert 空间，因此两者在空间范围与噪声要求上各有侧重。相对经典随机逼近的 ODE 方法，本文将非线性部分交给确定性的含误差 KM 估计，仅对辅助平均噪声使用线性稳定 ODE。

**范围。** 本笔记只精读本篇；外部文献仅核对 Theorem 2.1 的来源、Combettes–Pesquet Corollary 2.7，以及与随机 Fast KM 的直接接口。不据此宣布新颖性，也不制定新算法。

**页码。** 下文“p. 196”指期刊印刷页码。原文从 p. 191 开始，故 PDF 页码等于印刷页码减 190。例如 p. 196 对应 PDF 第 6 页。所有“原文未编号”公式均给出所在章节或结果与页码。新增论证均标为“补充推导”。

**术语。** Nonexpansive 指不放大任意两点之间的距离；fixed-point residual 指不动点残差；martingale difference 指对过去信息的条件期望为零的噪声；almost surely，缩写 a.s.，指在一个概率为一的事件上成立。Last iterate 指原始末次迭代点，random iterate 指另外按指定概率抽取的某个历史迭代点。

**结论类型。** “期望界”“有限时域界”“样本复杂度”互有交集。单个时刻的高概率界单独标明；它不自动成为同一条无限轨道上的 a.s. 速率。第 5 节的随机输出也不等于原始末次点。

## 2. 设定、记号与假设

### 2.1 基本模型与两种范数

设 $T:\mathbb R^d\to\mathbb R^d$ 对给定范数 $\lVert\cdot\rVert$ 非扩张，且 $\operatorname{Fix}(T)\ne\varnothing$。这一背景条件贯穿全文。原文 Introduction，p. 191，未编号：

$$
\lVert Tx-Ty\rVert\le\lVert x-y\rVert,
\qquad \operatorname{Fix}(T)=\{x:Tx=x\}.
$$

原文 (SKM)，p. 191：

$$
x_n=(1-\alpha_n)x_{n-1}+\alpha_n(Tx_{n-1}+U_n),\qquad n\ge1.
$$

$x_0$ 是给定初始点，$\alpha_n$ 是确定性平均权重。$U_n$ 是第 $n$ 步算子评估的加性随机误差。令 $\mathcal F_n$ 表示截至第 $n$ 步的信息，$U_n$ 对该 filtration 适应，$x_{n-1}$ 对 $\mathcal F_{n-1}$ 可测。记号表采用的补充简写：

$$
r_n:=\lVert x_n-Tx_n\rVert.
$$

原范数决定 $T$ 是否非扩张；$\lVert\cdot\rVert_2$ 是标准欧氏范数，用于利用鞅差的平方正交性。有限维范数等价给出原文 (1.1)，p. 193：

$$
\lVert x\rVert\le\mu\lVert x\rVert_2.
$$

$\mu>0$ 是固定常数。若原范数就是标准欧氏范数，可取 $\mu=1$。不能因为底层向量在 $\mathbb R^d$，就把一般原范数当作内积范数。

### 2.2 记号表

| 记号 | 定义或作用 | 原文位置 |
|---|---|---|
| $\alpha_n$ | SKM 平均权重 | p. 191，(SKM) |
| $\theta_n^2$ | $\mathbb E\lVert U_n\rVert_2^2$，非条件二阶矩 | p. 192，H1 |
| $\tau_n$ | $\sum_{k=1}^n\alpha_k(1-\alpha_k)$，累计有效时间 | p. 195，未编号 |
| $\sigma(y)$ | $\min\{1,(\pi y)^{-1/2}\}$，确定性残差核 | p. 195，未编号 |
| $\overline U_n$ | 由 (U) 定义的平均噪声 | p. 195 |
| $\pi_k^n$ | 第 $k$ 次噪声对第 $n$ 次平均的系数 | p. 196，未编号 |
| $\nu_n$ | 平均噪声的欧氏均方根尺度 | p. 196，未编号 |
| $\kappa$ | 路径上的算子像界，可为随机常数 | pp. 195、198 |
| $\bar\kappa$ | 控制期望的确定性常数 | p. 198，H4 |
| $B_n$ | Theorem 2.11 的积分形式误差上界 | p. 199，(2.5) |
| $B_{n,a}$ | 幂步长下的显式误差上界 | p. 206，Theorem 4.4 |

这里 $\kappa$ 是常数，$\sigma$ 才是函数。$\sigma$ 也不是噪声标准差；本文使用 $\theta_n$ 表示噪声尺度。$\pi_k^n$ 沿用原文上、下标写法，避免与圆周率 $\pi$ 混淆。按连续延拓约定 $\sigma(0)=1$。

原文 p. 196，未编号：

$$
\pi_k^n=\alpha_k\prod_{i=k+1}^{n}(1-\alpha_i),\qquad
\nu_n=\sqrt{\sum_{k=1}^{n}(\pi_k^n)^2\theta_k^2}.
$$

取 $\nu_0=0$。当需要表示初值系数时，补充约定 $\alpha_0=1$，从而 $\pi_0^n=\prod_{i=1}^n(1-\alpha_i)$。对 $k\ge1$ 的噪声展开不需要这一补充约定。

### 2.3 H0：迭代必须积累足够的有效时间

原文 p. 192：

$$
0<\alpha_n<1,\qquad
\sum_{k=1}^{\infty}\alpha_k(1-\alpha_k)=\infty.
$$

含义：平均系数合法，且 $\tau_n\to\infty$。这排除总更新量过小或权重过快接近 1 的情况。

**满足例子，补充推导：** $\alpha_n=1/(n+1)$，此时 $\tau_n$ 与 $\log n$ 同阶。**违反例子，补充推导：** $\alpha_n=1/(n+1)^2$，级数有限。取 $T=0$、$U_n=0$、$x_0\ne0$，则 $x_n=x_0\prod_{k=1}^n(1-\alpha_k)$ 趋于非零数，说明步长总量不足确实可能阻止到达不动点。

### 2.4 H1：鞅差与有限二阶矩

原文 p. 192：

$$
\mathbb E[U_n\mid\mathcal F_{n-1}]=0,\qquad
\theta_n^2:=\mathbb E\lVert U_n\rVert_2^2<\infty.
$$

第一条用于消去跨时刻交叉项；第二条定义平均噪声的二阶矩。H1 没有要求噪声独立同分布，也没有要求各时刻方差统一有界。

**满足例子，补充推导：** $U_n=c_n\xi_n$，$c_n$ 为有限确定性数，$\xi_n$ 是与过去独立的对称 $\{-1,1\}$ 随机变量。**违反例子，补充推导：** $U_n\equiv1$ 的条件均值不为零。独立 Cauchy 噪声还会违反二阶可积性。

### 2.5 H2：两种不同的可和性

原文 p. 196：

$$
\sum_{k=1}^{\infty}\alpha_k\nu_{k-1}<\infty.
$$

上式是 H2(a)。它控制平均噪声范数的加权 $\ell^1$ 总量。H2(b) 为：

$$
\sum_{k=1}^{\infty}\alpha_k^2\theta_k^2<\infty.
$$

H2(b) 是原始加权噪声在均方意义下的 $\ell^2$ 条件，用于建立鞅的 $L^2$ 有界性。两条条件控制不同对象，不能用“噪声可和”一句话代替。

**满足例子，补充推导：** $\theta_k=1$、$\alpha_k=1/(k+1)$ 时，$\pi_j^n=1/(n+1)$、$\nu_n=\sqrt n/(n+1)$，两条级数均有限。

**违反例子，补充推导：** 仍取单位方差独立对称噪声，但 $\alpha_k=(k+1)^{-3/5}$。由原文 Lemmas B.1–B.2，pp. 212–213，$\nu_{k-1}$ 与 $k^{-3/10}$ 同阶，因此 H2(a) 中的项与 $k^{-9/10}$ 同阶，级数发散；H2(b) 中的 $k^{-6/5}$ 仍可和。这说明只验证平方可和不足以使用 Theorem 2.5。

### 2.6 H3：允许有偏，但要求加权绝对误差可和

原文 p. 197：

$$
\sum_{k=1}^{\infty}\alpha_k\mathbb E[\lVert U_k\rVert\mid\mathcal F_{k-1}]<\infty
\quad\text{a.s.}
$$

这里不要求条件均值为零。它控制原始噪声的加权条件一阶矩，因而可以容纳确定性误差。

**满足例子，补充推导：** $\alpha_k=1/2$、$U_k=k^{-2}v$，$v$ 为固定向量。**违反例子，补充推导：** $U_k$ 为单位模长的独立对称噪声，$\alpha_k=1/(k+1)$。此时条件范数期望等于 1，级数发散。该例同时满足 H1、H2，说明 Theorem 2.5 的持续噪声机制与 Theorem 2.8 的误差可和机制不同。

### 2.7 H4：为显式期望界提供确定性常数

原文 p. 198。以下两条满足一条即可。

H4(i)：$T$ 的值域有界，且选择

$$
\bar\kappa\ge\sup_{x\in\mathbb R^d}\lVert Tx-x_0\rVert.
$$

H4(ii)：令

$$
S:=\sum_{k=2}^{\infty}\alpha_k\nu_{k-1}<\infty,
\qquad
\bar\kappa\ge2\operatorname{dist}(x_0,\operatorname{Fix}(T))+\mu S.
$$

H4 将逐轨道估计中的 $\kappa$ 控制为可用于取期望的常数。H4(i) 与 H4(ii) 可以同时成立。

**满足例子，补充推导：** $T=0$ 直接满足 H4(i)。另一个例子是 $T=I$、单位方差独立噪声、$\alpha_k=1/(k+1)$，其值域无界，但满足 H4(ii)。

**违反例子，补充推导：** $T=I$、单位方差独立噪声、$\alpha_k=(k+1)^{-3/5}$。值域无界，且上一节计算表明 $S=\infty$。即使此例的真实残差恒为零，它仍不能满足 H4；这说明 H4 是该误差界证明的充分条件，不是残差趋零的必要条件。

### 2.8 BVAR：非条件二阶矩统一有界

原文 p. 204：

$$
\sup_{n\ge1}\theta_n\le\theta<\infty.
$$

在 H1 下可将 $\theta_n^2$ 视为噪声总方差。注意 BVAR 约束 $\mathbb E\lVert U_n\rVert_2^2$；它没有要求条件方差逐路径有统一确定性上界。

**满足例子，补充推导：** 单位方差独立对称噪声。**违反例子，补充推导：** $U_n=n\xi_n$；每个时刻仍满足 H1，但 $\theta_n=n$ 无界。

若研究笔记中的 N2 要求条件方差统一有界，则在相同欧氏噪声定义下，N2 通过取全期望推出 BVAR；反向推论不成立。不能把这两个条件直接写成等价。

### 2.9 UNI：每个平稳策略只有一个常返类

原文 p. 200。对每个平稳策略 $\mu$，转移矩阵

$$
P_{ij}=p(j\mid i,\mu(i))
$$

定义的有限 Markov 链只有一个 recurrent class；允许有暂态状态。此处 $\mu$ 表示策略，与式 (1.1) 的范数常数同字母，含义由上下文区分。UNI 只用于第 3 节应用，不用于一般 SKM 定理。

**满足例子，补充推导：** 两状态、任意动作均以概率 1 转移至状态 1。状态 1 是唯一常返类，状态 2 暂态。**违反例子，补充推导：** 两状态在任何动作下都各自吸收，因而有两个常返类。

## 3. 核心工具与 reduction trick

### 3.1 Theorem 2.1：确定性含误差 KM

**原文位置：** pp. 194–195，(IKM)、Theorem 2.1、(2.1)。残差估计引用参考文献 [8] 的 Theorem 1，即 Bravo–Cominetti–Pavez-Signé，Mathematical Programming 175，2019，pp. 241–262。本篇对迭代点收敛补写了一个有限维论证。

考虑确定性误差 $e_n$：

$$
z_0=x_0,\qquad z_n=(1-\alpha_n)z_{n-1}+\alpha_n(Tz_{n-1}+e_n).
$$

若 $\lVert Tz_n-x_0\rVert\le\kappa$，则原文 (2.1)，p. 195：

$$
\lVert z_n-Tz_n\rVert\le\kappa\sigma(\tau_n)
+2\sum_{k=1}^{n}\alpha_k\lVert e_k\rVert\sigma(\tau_n-\tau_k)
+2\lVert e_{n+1}\rVert.
$$

若进一步 $\tau_n\to\infty$、$\lVert e_n\rVert\to0$，并且

$$
S=\sum_{n=1}^{\infty}\alpha_n\lVert e_n\rVert<\infty,
$$

则可取 $\kappa=2\operatorname{dist}(x_0,\operatorname{Fix}(T))+S$，且残差趋零、$z_n\to x^*\in\operatorname{Fix}(T)$。

**机制。** 第一项是确定性初始误差，第二项是历史误差经过核函数传播的总量，第三项是当前端点误差。即使只要残差趋零，也不能仅凭加权可和忽略第三项。

**迭代点收敛的证明主线，p. 195，未编号：**

1. 固定任意不动点 $\bar x$，由三角不等式与非扩张性得距离递推。
2. 加上剩余误差级数，使距离成为单调有下界的序列。
3. 因误差尾和趋零，$\lVert z_n-\bar x\rVert$ 有极限，因而 $z_n$ 有界。
4. 有限维有界序列存在强聚点；残差趋零与 $T$ 连续保证该聚点为不动点。
5. 对这个不动点的距离既有极限又沿子列趋零，故整个序列趋于它。

关键距离递推与尾和，原文 Theorem 2.1 证明，p. 195：

$$
\lVert z_n-\bar x\rVert\le\lVert z_{n-1}-\bar x\rVert+\alpha_n\lVert e_n\rVert,
\qquad \varepsilon_n=\sum_{k>n}\alpha_k\lVert e_k\rVert.
$$

因此 $\lVert z_n-\bar x\rVert+\varepsilon_n$ 单调不增。此处没有无限维弱收敛论证；不能直接删去“有限维”。

### 3.2 平均噪声把随机迭代化为确定性含误差迭代

**原文位置：** §2.1，pp. 195–196；(U)。定义

$$
\overline U_0=0,\qquad
\overline U_n=(1-\alpha_n)\overline U_{n-1}+\alpha_nU_n.
$$

令 $z_n=x_n-\overline U_n$，将 (U) 从 (SKM) 相减，得到原文 §2.1 未编号式，p. 195：

$$
z_n=(1-\alpha_n)z_{n-1}+\alpha_nTx_{n-1}.
$$

把 $Tx_{n-1}$ 写成 $Tz_{n-1}+e_n$，其中

$$
e_n:=Tx_{n-1}-Tz_{n-1},\qquad
\lVert e_n\rVert\le\lVert\overline U_{n-1}\rVert.
$$

最后一个不等式来自原范数中的非扩张性。**这里的实际误差是两个算子值之差；$\overline U_{n-1}$ 只提供其范数上界。**

直接用原始 $U_n$ 作为误差，会要求噪声本身衰减并满足绝对可和。改用辅助序列后，需验证的条件变为

$$
\overline U_n\to0,\qquad
\sum_{n=1}^{\infty}\alpha_n\lVert\overline U_{n-1}\rVert<\infty
\quad\text{a.s.}
$$

这是原文 p. 196 的归约目标。满足它以后，先由 Theorem 2.1 得 $z_n\to x^*$，再由 $x_n=z_n+\overline U_n$ 得原始迭代点的收敛。分析中的噪声平均不要求算法额外增加样本，也不把输出换成迭代点平均。

## 4. 第 2 节逐个结果

### 4.1 Lemma 2.4：平均噪声的二阶矩计算

**陈述与类型。** 原文 p. 196，Lemma 2.4，未编号；假设 H1。结论是辅助序列的期望界：

$$
\overline U_n=\sum_{k=1}^n\pi_k^nU_k,\qquad
\mathbb E\lVert\overline U_n\rVert\le\mu\nu_n.
$$

**证明步骤。**

1. 递归展开 (U)，得到线性组合。
2. 对 $j<k$，$U_j$ 对 $\mathcal F_{k-1}$ 可测，条件无偏使欧氏内积交叉项的期望为零。
3. 在欧氏平方范数下计算二阶矩，再用 Jensen 不等式和 (1.1) 转回原范数。

第 2 步的展开为补充推导，对应原文 p. 196 一行平方展开：

$$
\mathbb E\langle U_j,U_k\rangle_2
=\mathbb E\langle U_j,\mathbb E[U_k\mid\mathcal F_{k-1}]\rangle_2=0.
$$

原文 Lemma 2.4 证明，p. 196，未编号：

$$
\mathbb E\lVert\overline U_n\rVert_2^2
=\sum_{k=1}^n(\pi_k^n)^2\theta_k^2=\nu_n^2.
$$

**噪声处理。** 使用平方权重 $(\pi_k^n)^2$ 和鞅差正交性；此引理不需要无穷级数可和。

**检查点。** 代入 $\alpha_n=1/(n+1)$、$\theta_k=\theta$，验证 $\nu_n=\theta\sqrt n/(n+1)$。不能写成恰好 $\theta/\sqrt n$，但二者渐近等价。

### 4.2 Theorem 2.5：原始迭代点的几乎必然收敛

**陈述。** 原文 pp. 196–197，Theorem 2.5；H0、H1、H2 保证存在取值于不动点集的随机变量 $x^*$，使

$$
x_n\longrightarrow x^*\in\operatorname{Fix}(T)\quad\text{a.s.}
$$

**结论类型。** 迭代点几乎必然收敛；由 $T$ 连续还可推出 $r_n\to0$ a.s.。该定理本身没有给出显式残差速率，也没有样本复杂度结论。

**逐步对照证明。** 以下步骤 1–7 对应原文从 p. 196 定理后开始至 p. 197 证明结束，所有等式均未编号。

1. **提出两个充分目标。** 令

$$
X_n=\sum_{k=1}^n\alpha_k\lVert\overline U_{k-1}\rVert,
\qquad X_\infty=\sum_{k=1}^{\infty}\alpha_k\lVert\overline U_{k-1}\rVert.
$$

只要 $X_\infty<\infty$ 和 $\overline U_n\to0$ a.s.，第 3.2 节的归约便完成证明。

2. **用 H2(a) 控制平均误差总量。** Lemma 2.4 给出

$$
\mathbb E X_n\le\Delta,
\qquad \Delta:=\mu\sum_{k=1}^{\infty}\alpha_k\nu_{k-1}<\infty.
$$

由于 $X_n$ 非负且单调递增，单调收敛定理给出 $\mathbb E X_\infty\le\Delta$。非负随机变量期望有限，故 $X_\infty<\infty$ a.s.。这里没有把“期望趋零”误当作“几乎必然趋零”；使用的是整个非负级数的期望有限。

3. **将平均噪声识别为线性随机逼近。** 原文将 (U) 写为

$$
\overline U_{n+1}-\overline U_n
=\alpha_{n+1}(-\overline U_n+U_{n+1}).
$$

平均漂移是 $-\overline U_n$，对应的 ODE 为 $\dot u=-u$。

4. **构造平方可积鞅。** 令

$$
M_n=\sum_{k=1}^n\alpha_kU_k.
$$

H1 保证其为鞅，并由正交性及 H2(b) 得

$$
\mathbb E\lVert M_n\rVert_2^2
=\sum_{k=1}^n\alpha_k^2\theta_k^2
\le\sum_{k=1}^{\infty}\alpha_k^2\theta_k^2<\infty.
$$

Doob 鞅收敛定理给出 $M_n$ a.s. 收敛到有限随机向量；特别地，其路径有界。有限维范数等价允许将欧氏有界性换为原范数有界性。

5. **证明辅助平均噪声的路径有界。** 对 (U) 求和得到

$$
M_n=\overline U_n+\sum_{k=1}^n\alpha_k\overline U_{k-1}.
$$

因而

$$
\lVert\overline U_n\rVert\le\lVert M_n\rVert+X_\infty.
$$

前两步已分别控制右边两项，故 $\overline U_n$ a.s. 有界。

6. **原文通过稳定线性 ODE 得到平均噪声趋零。** 原文调用 [6] Benaïm 的 Proposition 4.2 与 Theorem 5.7，并说明前者在 H2(b) 的无条件平方可和形式下仍适用。它们将有界随机逼近的极限集限制为 ODE $\dot u=-u$ 的 internally chain transitive set。这里该术语只用于表示 ODE 方法所限制的候选极限集；此线性系统唯一的此类非空紧极限集为 $\{0\}$，故 $\overline U_n\to0$ a.s.。

7. **回到原始迭代。** 在上述结论共同成立的概率为一事件上，误差 $e_n$ 满足 Theorem 2.1 的条件。因此 $z_n\to x^*$，再由 $x_n=z_n+\overline U_n$ 得结论。极限可以随整条噪声路径变化，见 Remark 2.6，p. 197。

**补充推导：用 Robbins–Siegmund 直接替换步骤 3–6。** 这一补充只证明平均噪声趋零；H2(a) 仍负责步骤 2。设 $V_n=\lVert\overline U_n\rVert_2^2$。由 (U)、H1：

$$
\mathbb E[V_n\mid\mathcal F_{n-1}]
=(1-\alpha_n)^2V_{n-1}
+\alpha_n^2\mathbb E[\lVert U_n\rVert_2^2\mid\mathcal F_{n-1}].
$$

记 $q_n=\alpha_n^2\mathbb E[\lVert U_n\rVert_2^2\mid\mathcal F_{n-1}]$。Tonelli 定理和 H2(b) 给出

$$
\mathbb E\sum_{n=1}^{\infty}q_n
=\sum_{n=1}^{\infty}\alpha_n^2\theta_n^2<\infty.
$$

故 $\sum_nq_n<\infty$ a.s.。又因 $(1-\alpha_n)^2\le1-\alpha_n$，Robbins–Siegmund 引理推出 $V_n$ 有极限且 $\sum_n\alpha_nV_{n-1}<\infty$ a.s.。H0 推出 $\sum_n\alpha_n=\infty$，因此该极限只能为零。这一证明更贴近随机优化中的熟悉工具，并明确表明无需条件方差统一有界。

**噪声处理。** H2(a) 通过 Jensen 和单调收敛处理平均噪声的加权 $\ell^1$ 总量；H2(b) 通过鞅正交性处理原始噪声的加权 $\ell^2$ 总量。两者分工明确。

**检查点。** 由 $\nu_{k-1}\le\theta\sqrt{\alpha_k}$ 解释为什么幂步长在 $a>2/3$ 时满足 H2(a)，而仅 H2(b) 只需要 $a>1/2$。这两个门槛是这套证明的充分条件门槛，不是所有随机 KM 算法的普遍下界。

### 4.3 Theorem 2.8：非鞅型衰减误差

**陈述与类型。** 原文 pp. 197–198；H0、H3 推出 $x_n\to x^*\in\operatorname{Fix}(T)$ a.s.。结论类型为迭代点几乎必然收敛，同时蕴含残差 a.s. 趋零。它不要求 H1 或 H2。

**证明步骤。**

1. 原文 p. 197 定义 $N_n=\sum_{k=1}^n\alpha_k\lVert U_k\rVert$，及 $\eta_n=\alpha_n\mathbb E[\lVert U_n\rVert\mid\mathcal F_{n-1}]$。于是

$$
\mathbb E[N_n\mid\mathcal F_{n-1}]=N_{n-1}+\eta_n.
$$

H3 与 Robbins–Siegmund 型非负过程结论保证 $N_n$ 有有限极限。因此 $\sum_k\alpha_k\lVert U_k\rVert<\infty$ a.s.。

2. 原文 p. 197 定义绝对收敛向量级数的尾和

$$
u_n=\sum_{k>n}\alpha_kU_k,\qquad w_n=\overline U_n+u_n.
$$

本式首个记号是拉丁字母 $u_n$，不是希腊字母 $\nu_n$。两者应区别。利用 $u_{n-1}=\alpha_nU_n+u_n$，得到

$$
w_n=(1-\alpha_n)w_{n-1}+\alpha_nu_{n-1}.
$$

3. $u_n\to0$，而 H0 保证平均权重逐渐忘记初值。Toeplitz 引理给出 $w_n\to0$，于是 $\overline U_n\to0$。

4. 由 (U) 的三角不等式，原文 p. 198：

$$
\alpha_k\lVert\overline U_{k-1}\rVert
\le\lVert\overline U_{k-1}\rVert-\lVert\overline U_k\rVert
+\alpha_k\lVert U_k\rVert.
$$

有限求和后再取极限，得 $\sum_k\alpha_k\lVert\overline U_{k-1}\rVert\le\sum_k\alpha_k\lVert U_k\rVert<\infty$。应用 Theorem 2.1。

**噪声处理。** 核心是原始加权绝对误差的 $\ell^1$ 可和；不使用跨时刻鞅差正交性。H3 可以允许有偏噪声。

**与 Combettes–Pesquet Corollary 2.7 的原文对照。** 已核对其 arXiv:1404.7536v4，PDF pp. 7–8，Corollary 2.7、(2.26)–(2.31)。该文研究可分 Hilbert 空间中的随机 KM，其误差要求为

$$
\sum_n\lambda_n\sqrt{\mathbb E[\lVert e_n\rVert^2\mid\mathcal X_n]}<\infty
\quad\text{a.s.}
$$

这里 $\mathcal X_n$ 是该文的过去信息。对齐索引、过滤及同一个 Hilbert 范数后，条件 Jensen 不等式给出

$$
\mathbb E[\lVert e_n\rVert\mid\mathcal X_n]
\le\sqrt{\mathbb E[\lVert e_n\rVert^2\mid\mathcal X_n]}.
$$

因此 **Combettes–Pesquet 的误差条件推出 H3**。但空间与结论不可省略：其一般结论是 a.s. 弱收敛；在 demicompactness 条件下才另得强收敛。Theorem 2.8 给出有限维任意范数中的范数收敛。

| 比较项 | 本文 Theorem 2.8 | Combettes–Pesquet Corollary 2.7 |
|---|---|---|
| 空间 | 有限维，任意给定范数 | 可分 Hilbert，可无限维 |
| 误差控制 | 加权条件一阶矩可和 | 加权条件均方根可和 |
| 条件无偏 | 不要求 | 不要求 |
| 基本结论 | a.s. 范数收敛 | a.s. 弱收敛 |
| 显式速率 | 此定理未给出 | 此推论未给出 |

**检查点，补充推导。** 取独立非负误差 $U_n=n^2$，概率为 $n^{-4}$，否则为零，并取 $\alpha_n=1/2$。条件一阶矩为 $n^{-2}$，条件二阶矩为 1。因此 H3 成立，而条件均方根可和要求不成立。这说明两种误差要求确实可以区分。

### 4.4 Corollary 2.9：鞅差与衰减扰动叠加

**陈述。** 原文 p. 198。设

$$
U_n=W_n+V_n.
$$

假设 H0，$W_n$ 满足 H1 及对应的 H2，$V_n$ 满足 H3，则 $x_n\to x^*\in\operatorname{Fix}(T)$ a.s.。原文对 H2 中二阶矩对象的表述略简，本笔记按证明用途将其解释为鞅差部分 $W_n$ 的二阶矩与对应 $\nu_n$。

**结论类型。** 迭代点几乎必然收敛及残差 a.s. 趋零。

**证明主线，补充展开原文“combining”的一步。**

1. 分别构造 $\overline W_n$ 与 $\overline V_n$，二者均满足 (U) 的同型递推。
2. Theorems 2.5、2.8 的辅助噪声证明给出二者趋零，以及各自加权平均范数可和。
3. 线性关系 $\overline U_n=\overline W_n+\overline V_n$ 与三角不等式给出归约需要的两个条件。
4. 对总误差使用 Theorem 2.1；无需将非线性 $T$ 或两条原始迭代轨道相加。

**噪声处理。** $W_n$ 走 H1、H2 的鞅差路线，$V_n$ 走 H3 的加权 $\ell^1$ 路线。

**检查点。** 验证 $\alpha_n=1/(n+1)$、$W_n=\xi_n$、$V_n=n^{-1}v$ 满足上述条件；总噪声条件均值不为零，但迭代仍有该 a.s. 结论。

### 4.5 Theorem 2.10：把逐轨道界转成期望界

**陈述。** 原文 pp. 198–199；H1、H4，以及全篇的非扩张、不动点存在与 $0<\alpha_n<1$ 背景条件。原文 (2.3)，p. 199：

$$
\mathbb E r_n\le\bar\kappa\sigma(\tau_n)
+2\mu\sum_{k=2}^n\alpha_k\sigma(\tau_n-\tau_k)\nu_{k-1}
+4\mu\nu_n.
$$

**结论类型。** 每个 $n$ 的有限时域期望界。该界不要求 H0 中无穷级数发散，也不单独保证右边趋零。

**证明步骤。**

1. $I-T$ 为 2-Lipschitz，原文 §2.4，p. 198，未编号：

$$
r_n\le\lVert z_n-Tz_n\rVert+2\lVert\overline U_n\rVert.
$$

2. 对 $z_n$ 使用 (2.1)，并代入 $\lVert e_k\rVert\le\lVert\overline U_{k-1}\rVert$，得到原文 (2.2)，p. 198：

$$
r_n\le\kappa\sigma(\tau_n)
+2\sum_{k=2}^n\alpha_k\sigma(\tau_n-\tau_k)\lVert\overline U_{k-1}\rVert
+4\lVert\overline U_n\rVert.
$$

系数 4 来自 (2.1) 中的末端误差系数 2，以及从 $z_n$ 转回 $x_n$ 的系数 2。$k=1$ 项为零，因为 $\overline U_0=0$。

3. H4(i) 下可直接取确定性 $\kappa=\bar\kappa$；H4(ii) 下，取

$$
\kappa=2\operatorname{dist}(x_0,\operatorname{Fix}(T))
+\sum_{k=2}^{\infty}\alpha_k\lVert\overline U_{k-1}\rVert.
$$

Lemma 2.4 给出 $\mathbb E\kappa\le\bar\kappa$。该处只需有界轨道估计与级数的期望有限，无需先使用 Theorem 2.5 的全部 H2(b)。

4. 对 (2.2) 取期望，再逐项使用 Lemma 2.4，即得 (2.3)。

**噪声处理。** 先通过平方权重将原始噪声变为 $\nu_k$，再按核 $\alpha_k\sigma(\tau_n-\tau_k)$ 做线性累计。H4(ii) 要求 $\sum\alpha_k\nu_{k-1}<\infty$；H4(i) 不要求该级数可和，因而能给出持续噪声与常步长下的有限时域界。

**检查点。** 写出 $n=1$ 的估计，确认历史求和消失，但 $4\mu\nu_1$ 仍保留。

### 4.6 Theorem 2.11：将离散误差卷积化为积分

**陈述。** 原文 pp. 199–200。假设 H1、H4，存在正值、非增、凸且 $C^2$ 的函数 $h$，以及常数 $\gamma\ge1$，使原文 (2.4) 对所有 $k\ge2$ 成立：

$$
\nu_{k-1}\le(1-\alpha_k)h(\tau_k).
$$

$$
\alpha_k(1-\alpha_k)\le\gamma\alpha_{k+1}(1-\alpha_{k+1}).
$$

则原文 (2.5)，p. 199：

$$
\mathbb E r_n\le B_n.
$$

$$
B_n:=\frac{\bar\kappa}{\sqrt{\pi\tau_n}}
+\frac{2\mu\gamma}{\sqrt\pi}\int_{\tau_1}^{\tau_n}\frac{h(x)}{\sqrt{\tau_n-x}}\,dx
+2\mu\alpha_n\nu_{n-1}+4\mu\nu_n.
$$

原文说 decreasing；其 Theorem 4.1 实际使用常函数，因此这里按 nonincreasing 理解。

**结论类型。** 显式有限时域期望界；仍不是几乎必然速率或自动最优的复杂度。

**为什么值得精读。** $\nu_{k-1}$ 是离散平均噪声尺度。$h(\tau_k)$ 将它写为累计时间的函数。(2.4)(b) 限制相邻时间格宽度的比例。两者共同允许把历史噪声和变为可计算的积分。

**逐步对照证明。**

1. **先分离端点。** 从 (2.3) 开始。由于 $\sigma(0)=1$，$k=n$ 一项等于 $2\mu\alpha_n\nu_{n-1}$。这一项必须先取出，否则后面的核 $1/\sqrt{\tau_n-\tau_k}$ 在 $k=n$ 无定义。$n=1$ 时历史和本来为空，结论直接成立；以下讨论 $n\ge2$。

2. **替换噪声尺度与核。** 用 (2.4)(a) 及 $\tau_k-\tau_{k-1}=\alpha_k(1-\alpha_k)$，得到原文 p. 199 未编号推导：

$$
\alpha_k\nu_{k-1}\le h(\tau_k)(\tau_k-\tau_{k-1}).
$$

对 $k<n$ 再用 $\sigma(\tau_n-\tau_k)\le1/\sqrt{\pi(\tau_n-\tau_k)}$。因此只需证明原文 (2.6)，p. 199：

$$
\sum_{k=2}^{n-1}\frac{h(\tau_k)}{\sqrt{\tau_n-\tau_k}}(\tau_k-\tau_{k-1})
\le\gamma\int_{\tau_1}^{\tau_n}\frac{h(x)}{\sqrt{\tau_n-x}}\,dx.
$$

3. **证明被积函数先减后增。** 固定 $n$，原文定义

$$
f(x)=\frac{h(x)}{\sqrt{\tau_n-x}},\qquad \tau_1\le x<\tau_n.
$$

这里 $f$ 是此证明中的辅助函数，与 §4.3 的优化目标函数无关。原文 p. 199，未编号：

$$
f'(x)=\frac{h(x)+2(\tau_n-x)h'(x)}{2(\tau_n-x)^{3/2}}.
$$

记分子为 $\psi(x)=h(x)+2(\tau_n-x)h'(x)$，则

$$
\psi'(x)=-h'(x)+2(\tau_n-x)h''(x)\ge0.
$$

原因是 $h'\le0$、$h''\ge0$。而 $\psi(\tau_n)=h(\tau_n)>0$。所以 $f'$ 至多从非正变为非负一次。存在 $y_n\in[\tau_1,\tau_n)$，使 $f$ 在左侧非增，在右侧非减。若起始处导数已非负，取 $y_n=\tau_1$ 即可。

4. **下降部分用左侧区间面积控制。** 令 $k_n$ 为满足 $\tau_{k_n}\le y_n$ 的最大索引。对 $2\le k\le k_n$，$f(x)\ge f(\tau_k)$ 对 $x\in[\tau_{k-1},\tau_k]$ 成立。因此原文 p. 199 最后一个未编号式给出

$$
\sum_{k=2}^{k_n}f(\tau_k)(\tau_k-\tau_{k-1})
\le\int_{\tau_1}^{\tau_{k_n}}f(x)\,dx
\le\gamma\int_{\tau_1}^{\tau_{k_n}}f(x)\,dx.
$$

5. **上升部分换成右侧区间面积。** 对 $k\ge k_n+1$，$\tau_k>y_n$，所以右侧区间 $[\tau_k,\tau_{k+1}]$ 上有 $f(x)\ge f(\tau_k)$。先用 (2.4)(b) 将左格宽换成右格宽，原文 p. 200：

$$
f(\tau_k)(\tau_k-\tau_{k-1})
\le\gamma f(\tau_k)(\tau_{k+1}-\tau_k)
\le\gamma\int_{\tau_k}^{\tau_{k+1}}f(x)\,dx.
$$

求和得

$$
\sum_{k=k_n+1}^{n-1}f(\tau_k)(\tau_k-\tau_{k-1})
\le\gamma\int_{\tau_{k_n+1}}^{\tau_n}f(x)\,dx
\le\gamma\int_{\tau_{k_n}}^{\tau_n}f(x)\,dx.
$$

跨越最小点的区间未被重复错误使用；最后一步只是增加一个非负积分。因此无需要求最小点恰好落在网格上。

6. **相加并还原系数。** 步骤 4 与步骤 5 相加得到 (2.6)。恢复 $2\mu/\sqrt\pi$，再加上起始误差与两项端点误差，即得 (2.5)。积分在右端具有平方根奇性，但 $h$ 在有限正点附近连续，因而该奇性可积。

**噪声处理。** 概率工具已经由 Lemma 2.4 与 Theorem 2.10 完成；本定理新增的是确定性的离散和–积分比较。它没有凭空增加一个 $\ell^2$ 条件。能否得到衰减速率，需要进一步检查 $h$ 与 $\tau_n$ 的量级。

**检查点。** 取常步长 $\alpha$，$\beta=1-\alpha$。验证可取 $\gamma=1$ 和常函数 $h=\theta\sqrt\alpha/(\beta\sqrt{1+\beta})$，并算出积分为 $2h\sqrt{\tau_n-\tau_1}$。

### 4.7 Corollary 2.12：固定时刻的高概率误差界

**陈述。** 原文 p. 200；Theorem 2.11 的全部假设保证对每个 $p\in(0,1)$：

$$
\mathbb P\{r_n\le B_n/p\}\ge1-p.
$$

**结论类型。** 有限时域的高概率界，由期望界导出。这里的 $p$ 是失败概率。

**证明。** 原文 p. 200，未编号：对任意 $\epsilon>0$，Markov 不等式给出

$$
\mathbb P\{r_n>\epsilon\}\le\frac{\mathbb E r_n}{\epsilon}\le\frac{B_n}{\epsilon}.
$$

取 $\epsilon=B_n/p$。

**噪声处理。** 全部噪声依赖已进入 $B_n$，无需额外尾部分布假设。代价是置信参数以 $1/p$ 进入，不能把它描述成指数集中。

**检查点。** 若要对所有 $n$ 最终同时成立，须另选可和的失败概率序列并使用 Borel–Cantelli；所得阈值为 $B_n/p_n$，可能失去衰减性。固定时刻的高概率界不能原样变成 a.s. 速率。

## 5. 第 3 节 Q-learning 应用

### 5.1 怎样写成 SKM

**原文位置：** pp. 200–203，(3.1)–(3.3)、(RVI-Q)。有限状态动作对的总数为 $d$。最优平均奖励记为 $r$，全 1 向量记为 $e$。Bellman 算子及其平移版本，原文 p. 201 未编号：

$$
M(Q)(i,u)=\sum_jp(j\mid i,u)\left[g(i,u,j)+\max_{u'}Q(j,u')\right],
\qquad H(Q)=M(Q)-re.
$$

固定点方程 $Q=H(Q)$ 对应原文 (3.3)。$H$ 在无穷范数下非扩张。若 $r$ 已知，对每个状态动作对抽样后，可将采样值减去其条件期望定义为 $U_n$，于是得到以 $T=H$ 为算子的 SKM。

实际算法不知道 $r$，故用连续的平移等变函数 $f$：

$$
f(Q+ce)=f(Q)+c.
$$

原文 (RVI-Q)，p. 201：

$$
Q_n(i,u)=(1-\alpha_n)Q_{n-1}(i,u)
+\alpha_n\left[g(i,u,\xi_{iu}^n)+\max_{u'}Q_{n-1}(\xi_{iu}^n,u')-f(Q_{n-1})\right].
$$

加入 $f$ 后，算子未必仍非扩张。作者比较实际序列与一个使用真实 $r$ 的假想序列 $Q_n^r$。两者相差 $c_ne$；残差 $Q-H(Q)$ 对常数平移不变。这里不能直接把实际 RVI-Q 的更新算子宣称为非扩张。

### 5.2 Theorems 3.1 与 3.2 的作用

**Theorem 3.1，pp. 201–202。** 对 $\alpha_n=(n+1)^{-a}$、$4/5<a\le1$，在 H1 和原文 (3.4) 下：

$$
\lVert x_n\rVert\le\lVert x_{n-1}\rVert+\eta\alpha_n,
\qquad
\mathbb E\lVert U_n\rVert^2\le c\left(1+\mathbb E\lVert x_{n-1}\rVert^2\right).
$$

结论是迭代点 a.s. 收敛，且原文 (3.5) 给出 $\mathbb E r_n\le\kappa_a/\sqrt{\tau_n}$。若 $4/5<a<1$，量级为 $O(n^{-(1-a)/2})$；若 $a=1$，为 $O((\log n)^{-1/2})$。

它直接调用 Theorem 2.5 和 Theorem 2.11。式 (3.4) 先导出增长型二阶矩界，再验证 H2，并构造最终递减、凸的噪声包络。原文式 (3.6) 揭示 $\sum\alpha_k^{3/2}\tau_{k-1}$ 的可和门槛，因此出现 $a>4/5$。

**Theorem 3.2，pp. 202–203。** 假设 UNI、$4/5<a\le1$。对假想序列应用 Theorem 3.1，再处理常数平移，得到

$$
f(Q_n)\to r,\qquad Q_n\to Q^*\quad\text{a.s.}
$$

其中 $H(Q^*)=Q^*$ 且 $f(Q^*)=r$。原文 (3.8) 给出

$$
\mathbb E\lVert Q_n-H(Q_n)\rVert_\infty\le\frac{\kappa_a}{\sqrt{\tau_n}}.
$$

该节的一次向量更新对每个状态动作对都抽样。若计算标量环境样本数，应计入状态动作对数量，不能将一次向量迭代无条件等同于一个样本。

### 5.3 数值例子验证了什么

**原文位置：** §3.1，pp. 203–204，Figures 1–2。例子有两个状态、两个动作。作者运行 100 次独立实验，每次 10,000 步；上图展示其中 10 条 $f(Q_n)$ 轨迹，下图用 100 次平均估计残差，再乘上理论尺度。

图像展示估计量趋近最优平均奖励的行为，并显示理论归一化后的误差没有增长。原文也指出实际衰减可能快于给出的上界。右图使用 $a=4/5$，**这个等号边界不在 Theorem 3.2 的严格条件内**；它是探索性数值现象，不能用来宣称边界已获理论证明。

## 6. 第 4 节有界方差与显式速率

### 6.1 Theorem 4.1：预设时域的常步长

**陈述。** 原文 p. 205；H1、H4、BVAR，取 $\alpha_n\equiv\alpha\in(0,1)$，$\beta=1-\alpha$。原文 (4.1)：

$$
\mathbb E r_n\le\frac{\bar\kappa}{\sqrt{\pi\alpha\beta n}}
+\frac{2\mu\theta\sqrt\alpha}{\sqrt{1+\beta}}
\left[2\sqrt{\frac{\alpha n}{\pi\beta}}+\alpha+2\right].
$$

给定终点 $n_0\ge1$，若取 $\alpha=1/(6n_0^{2/3})$，则原文 (4.2)：

$$
\mathbb E r_{n_0}\le\frac{2(\bar\kappa+\mu\theta)}{n_0^{1/6}}.
$$

**结论类型。** 末次迭代的有限时域期望界。若一次 SKM 更新使用一次随机算子调用，并且相关常数统一受控，式 (4.2) 转为 $O(\epsilon^{-6})$ 调用上界是补充推导。此定理不保证固定正步长下原始迭代点 a.s. 收敛。

**证明步骤。**

1. 常步长给出 $\tau_n=\alpha\beta n$、$\pi_k^n=\alpha\beta^{n-k}$。
2. 几何级数与 BVAR 给出原文 p. 205，未编号：

$$
\nu_n\le\theta\alpha\sqrt{\sum_{k=1}^n\beta^{2(n-k)}}
\le\frac{\theta\sqrt\alpha}{\sqrt{1+\beta}}.
$$

3. 在 Theorem 2.11 中取 $\gamma=1$ 和 $h=\theta\sqrt\alpha/(\beta\sqrt{1+\beta})$。积分可以直接计算，再用 $\tau_n-\tau_1\le\tau_n$ 得 (4.1)。
4. 代入 $\alpha=1/(6n_0^{2/3})$，使用 $\alpha\le1/6$ 与 $n_0\ge1$ 控制常数，得到 (4.2)。

**噪声处理。** $\nu_n$ 保持 $O(\sqrt\alpha)$，并未趋零；历史核还会积累噪声。因此算法要随目标时域选择步长。持续非退化噪声与常步长下，H4(ii) 的 $S$ 往往发散，此时须由 H4(i) 等实际满足的分支提供假设。

**检查点，补充推导。** (4.1) 的主要项量级为 $(\alpha n_0)^{-1/2}$ 与 $\alpha\sqrt{n_0}$。令两者同阶，得到 $\alpha\asymp n_0^{-2/3}$，共同量级为 $n_0^{-1/6}$。

### 6.2 Theorem 4.4：不预设终点的幂步长

**陈述。** 原文 p. 206；H1、H4、BVAR，取 $\alpha_n=(n+1)^{-a}$，$1/2\le a\le1$。原文给出 $\mathbb E r_n\le B_{n,a}$，其上界的渐近等价式为 (4.5)。为准确复现，先列原文 (3.7)，p. 202，与 (4.4)，p. 206 的常数：

$$
\gamma_a=\sup_{k\ge2}\frac{\alpha_k(1-\alpha_k)}{\alpha_{k+1}(1-\alpha_{k+1})},
\qquad b_a=\frac{a}{2(1-a)}\quad(a<1).
$$

$$
\lambda_a=\left(3^{a/2}-3^{-a/2}\right)^{2(1-a)/a}-(1-a)\tau_2(a).
$$

$$
d_a=\frac{2\gamma_a}{3a-2}\left[\lambda_a+(1-a)\tau_1(a)\right]^{1-b_a}
\quad(2/3<a<1).
$$

原文 Proposition A.3，p. 210，另定义 $d_1=\sqrt{3}e^{1/9}(32/27)$。以下逐段写出 (4.5)，避免把四种范围混在一起。

当 $1/2\le a<2/3$：

$$
B_{n,a}\approx\frac{2\mu\theta\gamma_a}{\sqrt{1-a}}
\frac{\Gamma(1-b_a)}{\Gamma(3/2-b_a)}n^{-(a-1/2)}.
$$

当 $a=2/3$：

$$
B_{n,2/3}\approx\frac{2\mu\theta\gamma_{2/3}}{\sqrt{3\pi}}
\frac{\log n}{n^{1/6}}.
$$

当 $2/3<a<1$：

$$
B_{n,a}\approx\frac{(\bar\kappa+2\mu\theta d_a)\sqrt{1-a}}{\sqrt\pi}
\frac{1}{n^{(1-a)/2}}.
$$

当 $a=1$：

$$
B_{n,1}\approx\frac{\bar\kappa+2\mu\theta d_1}{\sqrt\pi\sqrt{\log n}}.
$$

这里 $\approx$ 沿用原文 §1.2，p. 193，表示比值趋于 1；原文的 $\sim$ 只表示上下同阶。本笔记需要表示同阶时使用文字或 $\asymp$。上述含 $\theta$ 的主导项在 $\theta>0$ 时适用；若 $\theta=0$，必须回到原始误差界，不能把零主导系数当作有效渐近等价式。

**结论类型。** 每个时刻的末次残差期望界，以及这些上界的渐近阶。$B_{n,a}$ 的渐近等价不等于真实残差的匹配下界。$a=1/2$ 时，该上界趋于正数，不能据此断言真实残差不趋零。

**显式有限时域表达。** 原文 Appendix A，pp. 210–211，Propositions A.1–A.3 给出闭式。保留可直接计算且无需特殊函数的等价积分写法如下。

当 $a<1$，原文 Proposition A.1 证明与 (A.1) 给出

$$
B_{n,a}=\frac{\bar\kappa}{\sqrt{\pi\tau_n}}
+\frac{2\mu\theta\gamma_a}{\sqrt\pi}
\int_{\tau_1}^{\tau_n}\frac{[\lambda_a+(1-a)x]^{-b_a}}{\sqrt{\tau_n-x}}\,dx
+2\mu\theta(\alpha_n+2)\sqrt{\alpha_n}.
$$

当 $a=1$，原文 Proposition A.3 证明采用 $\omega=(\sqrt{3}/2)e^{17/72}$，给出

$$
B_{n,1}=\frac{\bar\kappa}{\sqrt{\pi\tau_n}}
+\frac{2\mu\theta\gamma_1\omega}{\sqrt\pi}
\int_{1/4}^{\tau_n}\frac{e^{-x/2}}{\sqrt{\tau_n-x}}\,dx
+\frac{2\mu\theta(2n+3)}{(n+1)^{3/2}}.
$$

这里 $\gamma_1=32/27$，$\tau_1=1/4$。这两个积分公式来自原文的闭式转换，不是额外算法或数值实验。

**证明主线。**

1. Lemmas B.1–B.2，pp. 212–213，控制平均权重平方和，得到 $\nu_{n-1}\le\theta\sqrt{\alpha_n}$。
2. Lemmas B.6–B.7，pp. 215–216，构造适合 (2.4)(a) 的 $h$。$a<1$ 时其尾部与 $x^{-b_a}$ 同阶；$a=1$ 时呈指数衰减。
3. 由 Theorem 2.11 得上面的积分界。累计时间满足 $\tau_n\approx n^{1-a}/(1-a)$，$a<1$；$a=1$ 时 $\tau_n\approx\log n$。
4. Appendix A，pp. 211–212，按 $b_a<1$、$b_a=1$、$b_a>1$ 估计积分，分别产生幂次项、对数项与有限总质量项。这三个范围恰好对应 $a<2/3$、$a=2/3$、$a>2/3$。

**噪声处理。** 在 $a>2/3$ 时，BVAR 足以推出 H2(a)，进而自动满足 H4(ii)。在 $a\le2/3$ 时，BVAR 本身不足以推出 H4；例如持续单位方差噪声使 $\sum\alpha_k\nu_{k-1}$ 发散。因此引用最快上界 $O(\log n/n^{1/6})$ 时必须保留 H4，不能写成“任意非扩张算子加有界方差即得该速率”。

**检查点。** 验证 $b_a=1$ 等价于 $a=2/3$，并解释它为什么同时是卷积积分的对数临界点与 H2(a) 的可和临界点。

### 6.3 Corollary 4.5：SGD 的梯度残差

**原文陈述。** §4.3，p. 206。设 $f(x)=\mathbb E F(x,\xi)$ 凸、可微，$\nabla f$ 为 $L$-Lipschitz，最小点存在，并允许交换梯度与期望。原文 (SGD) 为

$$
x_n=x_{n-1}-\gamma_n\nabla_xF(x_{n-1},\xi_n).
$$

取 $\gamma_n=2/[L(n+1)^a]$，$1/2\le a\le1$，并假设对应噪声满足 BVAR。原文 (4.6) 声称

$$
\mathbb E\lVert\nabla f(x_n)\rVert_2\le\frac L2B_{n,a}.
$$

原文还给出：$2/3<a\le1$ 时，$x_n$ a.s. 收敛到某个最小点。

**结论类型。** 梯度范数期望界；在指定参数范围内另有迭代点 a.s. 收敛。它不是函数值差界。

**证明主线。**

1. 设 $T=I-(2/L)\nabla f$。凸性与光滑性给出 $\nabla f$ 的 cocoercivity，从而 $T$ 非扩张；不动点正好为最小点。
2. 对齐 (SKM) 与 (SGD)，得到 $\alpha_n=\gamma_nL/2$，并应使用下式噪声。此式是对原文索引的补充核对：

$$
U_n=\frac2L\left[\nabla f(x_{n-1})-\nabla_xF(x_{n-1},\xi_n)\right].
$$

3. $\lVert x_n-Tx_n\rVert_2=(2/L)\lVert\nabla f(x_n)\rVert_2$。**在 Theorem 4.4 的 H4 同时成立时**，(4.6) 随即得到。
4. $a>2/3$ 时，Example 2.7 自动验证 H2，应用 Theorem 2.5 得迭代点 a.s. 收敛。

**适用范围核对。** 原文推论没有单列 H4，却称 (4.6) 直接来自 Theorem 4.4。在 $a>2/3$ 时，BVAR 自动补足 H4(ii)，这条推理完整；在 $a\le2/3$ 时，现有陈述没有自动保证 H4。此处记录为“原文推论的引用条件需要补充核对”，不据此断言所有 SGD 速率结论错误。严格引用本篇这条证明时，应附加 H4，或另给不需要 H4 的证明。

**噪声处理。** 条件无偏由 $\xi_n$ 与过去独立及梯度交换假设保证。若在当前随机点 $x_n$ 上定义误差，就不能用同一独立性理由消掉条件均值。

**检查点。** 对 $f(x)=Lx^2/2$ 算出 $T=-I$；验证其非扩张，但值域无界。光滑凸性本身不能保证 H4(i)。

## 7. 第 5 节欧氏空间的随机输出

### 7.1 Proposition 5.1：平方距离提供加权残差和

**陈述。** 原文 pp. 207–208；原范数由内积诱导，H1 成立。令 $R=\operatorname{dist}(x_0,\operatorname{Fix}(T))$。原文 (5.1)，p. 208：

$$
\sum_{k=1}^n\alpha_k(1-\alpha_k)\mathbb E\lVert Tx_{k-1}-x_{k-1}\rVert^2
\le R^2+\mu^2\sum_{k=1}^n\alpha_k^2\theta_k^2.
$$

另定义随机索引 $J_n$，按与算法轨道独立的额外随机性选择，取值 $k\in\{1,\ldots,n\}$ 的概率为

$$
p_k^n=\frac{\alpha_k(1-\alpha_k)}{\sum_{i=1}^n\alpha_i(1-\alpha_i)},
\qquad \widehat x_n=x_{J_n-1}.
$$

索引 $J_n$ 是为明确随机选择而补充的记号；$p_k^n$ 与 $\widehat x_n$ 沿用原文 p. 208。于是原文 (5.2)：

$$
\mathbb E\lVert T\widehat x_n-\widehat x_n\rVert^2
\le\frac{R^2+\mu^2\sum_{k=1}^n\alpha_k^2\theta_k^2}{\tau_n}.
$$

Jensen 不等式给出原文 (5.3)，p. 208：

$$
\mathbb E\lVert T\widehat x_n-\widehat x_n\rVert
\le\sqrt{\frac{R^2+\mu^2\sum_{k=1}^n\alpha_k^2\theta_k^2}{\tau_n}}.
$$

**结论类型。** 有限时域期望界；对象是随机历史点。Proposition 5.1 本身不要求 BVAR 或 H4。

**证明步骤。**

1. 取 $y_0$ 为初始点到不动点集的投影，令 $\zeta_k=\lVert x_k-y_0\rVert$。
2. 对平方范数使用内积空间恒等式。该步骤正是一般范数证明中不可直接使用的结构。
3. H1 消去噪声与过去可测量之间的交叉项；非扩张性控制 $\lVert Tx_{k-1}-Ty_0\rVert$。
4. 得到原文证明的单步式，p. 208，未编号：

$$
\mathbb E\zeta_k^2
\le\mathbb E\zeta_{k-1}^2+\mathbb E\lVert\alpha_kU_k\rVert^2
-\alpha_k(1-\alpha_k)\mathbb E\lVert Tx_{k-1}-x_{k-1}\rVert^2.
$$

5. 用 $\mathbb E\lVert U_k\rVert^2\le\mu^2\theta_k^2$，求和消去相邻距离平方，丢弃非负末项，得到 (5.1)。随机索引的全期望公式给出 (5.2)。

**噪声处理。** 噪声按 $\alpha_k^2\theta_k^2$ 累积；有限时域不要求无穷级数可和。这里只计算能量和，没有将平均噪声转换为 $\ell^1$ 扰动。

**检查点。** 若所有 $\alpha_k=\alpha$，验证 $p_k^n=1/n$。这给出历史点的均匀随机选择，既不等于平均向量，也不等于末次点。

### 7.2 Corollary 5.4：随机输出的四次方样本量

**陈述。** 原文 p. 209；欧氏空间、H1、BVAR。给定 $n_0$，取

$$
\alpha_n\equiv\alpha=\frac1{\sqrt{n_0+1}}.
$$

令 $\widehat x_{n_0}$ 如 Proposition 5.1。原文 (5.4)：

$$
\mathbb E\lVert T\widehat x_{n_0}-\widehat x_{n_0}\rVert
\le\frac{\sqrt{R^2+\mu^2\theta^2}}{\sqrt{\tau_1(1/2)}\,n_0^{1/4}}.
$$

其中 $\tau_1(1/2)=2^{-1/2}(1-2^{-1/2})$，来自原文 (4.3) 的定义。

**结论类型。** 随机输出的有限时域期望界。在一次更新计一次随机算子调用、其余参数固定时，达到期望残差 $\epsilon$ 的 $O(\epsilon^{-4})$ 调用上界是直接的补充推导。

**证明步骤，补充展开原文 (5.3) 的代入。**

1. $\sum_{k=1}^{n_0}\alpha^2=n_0/(n_0+1)\le1$，故分子至多 $R^2+\mu^2\theta^2$。
2. 分母为 $n_0\alpha(1-\alpha)$。对 $n_0\ge1$，它至少为 $\tau_1(1/2)\sqrt{n_0}$。
3. 将两式代入 (5.3) 并开平方，得到结论。

**噪声处理。** 常步长随预设终点缩小，使有限时域累计方差保持有界。它不是固定步长无限运行的精确收敛结论。

**检查点。** 对比 Theorem 4.1：第 4 节处理任意范数下的末次点且需要 H4；本推论处理内积范数下的随机点且不需要 H4。不能仅比较 $1/6$ 与 $1/4$ 就说同一输出、同一假设下速率提高。

### 7.3 Corollary 5.5：幂步长下的随机输出

**陈述。** 原文 p. 209；欧氏空间、H1、BVAR，$\alpha_n=(n+1)^{-a}$、$1/2\le a\le1$。对 Proposition 5.1 的随机点，原文 (5.5) 分三段给出如下界。

当 $a=1/2$：

$$
\mathbb E\lVert T\widehat x_n-\widehat x_n\rVert
\le\frac{\sqrt{R^2+\mu^2\theta^2\log(n+1)}}{\sqrt{\tau_1(1/2)}\,n^{1/4}}.
$$

当 $1/2<a<1$：

$$
\mathbb E\lVert T\widehat x_n-\widehat x_n\rVert
\le\frac{\sqrt{R^2+\mu^2\theta^2/(2a-1)}}{\sqrt{\tau_1(a)}\,n^{(1-a)/2}}.
$$

当 $a=1$：

$$
\mathbb E\lVert T\widehat x_n-\widehat x_n\rVert
\le\frac{2\sqrt{\log2}\sqrt{R^2+\mu^2\theta^2}}{\sqrt{\log(n+1)}}.
$$

**结论类型。** 每个时刻的随机输出期望界。步长不依赖预设终点，但输出分布 $p_k^n$ 依赖当前评价时刻 $n$。

**证明步骤。**

1. 原文 p. 209 证明中的积分比较：$a=1/2$ 时，$\sum_{k=1}^n\alpha_k^2\le\log(n+1)$；$a>1/2$ 时，$\sum_{k=1}^n\alpha_k^2\le1/(2a-1)$。
2. Lemma B.8，pp. 216–217，给出 $a<1$ 时 $\tau_n(a)\ge\tau_1(a)n^{1-a}$；$a=1$ 时 $\tau_n(1)\ge\log(n+1)/(4\log2)$。
3. 将两组估计代入 (5.3)。

**噪声处理。** 在 $a>1/2$ 时，原始噪声平方权重可和；在临界值 $a=1/2$ 时，只累积对数增长。此推论不需要将噪声变成加权 $\ell^1$ 扰动。

**检查点。** 从 (5.5) 读出 $a=1/2$ 时更准确的量级为 $O(\sqrt{\log n}/n^{1/4})$。原文随后文字写成 $O(\log n/n^{1/4})$，是较松的有效描述，不能当作平方根对数因子消失。

## 8. 假设与结论总表

下面的“幂 $a$”统一指 $\alpha_n=(n+1)^{-a}$；“背景”统一指 $T$ 非扩张、不动点存在、确定性 $0<\alpha_n<1$。除第 5 节外，空间为有限维给定范数。所有速率描述的是保证的上界，不主张真实误差匹配该阶。

| 原文结果及页码 | 假设 | 步长条件 | 结论 | 结论类型 | 速率 |
|---|---|---|---|---|---|
| L2.4，196 | 背景、H1 | 合法平均权重 | 平均噪声矩估计 | 期望界 | $\mu\nu_n$ |
| T2.5，196–197 | H0、H1、H2 | 累计有效时间无限 | $x_n\to x^*$ a.s. | 点收敛、残差趋零 | 定理未量化 |
| T2.8，197–198 | H0、H3 | 允许常步长 | $x_n\to x^*$ a.s. | 点收敛、残差趋零 | 定理未量化 |
| C2.9，198 | H0；两部分分别满足 H1/H2、H3 | 同上 | 混合误差下点收敛 | a.s. 点收敛 | 定理未量化 |
| T2.10，199 | 背景、H1、H4 | 不要求 H0 发散部分 | 末次残差卷积界 | 有限时域期望界 | (2.3) |
| T2.11，199–200 | T2.10 加 (2.4) | 相邻格宽比例受控 | 末次残差积分界 | 有限时域期望界 | $B_n$ |
| C2.12，200 | T2.11 全部假设 | 同上 | 固定时刻概率保证 | 高概率界 | 阈值 $B_n/p$ |
| T4.1，205 | H1、H4、BVAR | 常步长随 $n_0$ 设定 | 末次残差 | 期望界、复杂度换算 | $O(n_0^{-1/6})$ |
| T4.4，206 | H1、H4、BVAR | 幂 $a\in[1/2,1]$ | 末次残差 | 期望界 | 四段见下表 |
| C4.5，206 | 凸光滑 SGD、BVAR；期望界须核对 H4 | 幂 $a$ | 梯度期望界；$a>2/3$ 点收敛 | 期望界、a.s. 点收敛 | $(L/2)B_{n,a}$ |
| P5.1，207–208 | 内积范数、H1 | 合法平均权重 | 随机点平方残差 | 有限时域期望界 | (5.2)、(5.3) |
| C5.4，209 | 内积范数、H1、BVAR | 常步长随 $n_0$ 设定 | 随机点残差 | 期望界、复杂度换算 | $O(n_0^{-1/4})$ |
| C5.5，209 | 内积范数、H1、BVAR | 幂 $a\in[1/2,1]$ | 随机点残差 | 期望界 | 三段见下表 |

对应步长范围的速率比较，原文 (4.5)、(5.5)，pp. 206、209：

| 幂步长参数 | T4.4 的末次点 | C5.5 的随机点 |
|---|---|---|
| $a=1/2$ | 上界未趋零 | $O(n^{-1/4}\sqrt{\log n})$ |
| $1/2<a<2/3$ | $O(n^{-(a-1/2)})$ | $O(n^{-(1-a)/2})$ |
| $a=2/3$ | $O(n^{-1/6}\log n)$ | $O(n^{-1/6})$ |
| $2/3<a<1$ | $O(n^{-(1-a)/2})$ | $O(n^{-(1-a)/2})$ |
| $a=1$ | $O((\log n)^{-1/2})$ | $O((\log n)^{-1/2})$ |

补充定位：Theorem 2.1，p. 195，是确定性工具；Theorem 3.1，pp. 201–202，用 H1、(3.4)、$a>4/5$ 调用 T2.5、T2.11；Theorem 3.2，pp. 202–203，用 UNI 将一般结论转到 RVI-Q。

## 9. 通往随机 Fast KM 的接口

### 9.1 加入动量后，哪些对象会改变

以下是**结构分析与待验证问题**，不构成随机 Fast KM 的新定理。

1. **状态与噪声递推。** 本文 SKM 是一阶递推，平均噪声满足标量系数的一阶线性式 (U)。带动量方法包含相邻迭代点差，可能还包含历史算子值。若要构造同类消噪变量，需要匹配新的状态递推；不能直接照搬 $\pi_k^n$。
2. **噪声相关性。** 本文在 H1 下消去不同时间的噪声交叉项。若 Fast KM 重用前一步的随机算子输出，重用误差已属于当前过去信息，条件均值不会再次自动变零。必须先说明采样点、过滤、样本是否复用。
3. **累计时间与残差核。** 本文的 $\tau_n=\sum\alpha_k(1-\alpha_k)$ 与平方根核 $\sigma$ 来自普通 KM。加速算法中的权重和确定性残差估计会改变。保留这条普通 KM 界本身不会自动产生加速。
4. **稳定性证明。** 有限维 Theorem 2.1 用强聚点闭合证明。若目标是无限维 Hilbert 空间中的 a.s. 弱收敛，必须补充适合该算法的距离极限、弱聚点识别与 Opial 型论证，不能仅以有限维范数等价代替。

### 9.2 本文已经有的结论与尚未提供的结论

**已经有：** 同一条不预设终点的普通随机 KM 轨道的 a.s. 点收敛；原始末次残差的期望界；逐轨道残差估计 (2.2)。原文 p. 198 还明确指出，结合平均噪声的路径估计可导出 a.s. 渐近速率。因此，不应把研究动机写成“本文完全没有几乎必然残差速率”。

**尚未提供：** 带动量随机 Fast KM 的证明；在所需采样模型下，同时给出无限轨道的加速末次 a.s. 速率、迭代点 a.s. 收敛及相应样本复杂度。这里“尚未提供”仅指这篇论文，没有完成全领域新颖性判断。

**关于不预设终点。** Theorem 4.4 已使用不依赖终点的幂步长。因此可讨论“是否达到目标复杂度”，不能把“完全没有不预设终点的方法”当作缺口。

**关于随机 iKM。** 用户指定的 Yang–Jiang–Chi–Cutkosky–Xiao 2026 论文已研究随机惯性 KM 的末次残差样本复杂度，并在附录 A 连接 Fast KM。故后续题目必须写清：目标算法及参数、噪声模型、同一无限轨道、所求概率意义。有限时域复杂度结果是否可以延伸为该目标，仍须逐条核对该文定理；本笔记不展开第二篇精读。

### 9.3 可以直接借用的工具与需要重建的部分

| 工具 | 可借用范围 | 使用边界 |
|---|---|---|
| 鞅差正交性 | 计算过去可测系数乘新噪声的二阶矩 | 要先核对过滤与条件均值；不能忽略重用样本 |
| 非负级数期望有限 | 推出该级数 a.s. 有限 | 需要的是整个级数的期望有限 |
| Robbins–Siegmund | 能量近超鞅与可和误差分析 | 必须先推导新算法的单步能量式 |
| 条件一阶矩与均方根比较 | 区分 H3 型误差条件与更强条件 | 范数、过滤和噪声对象必须对齐 |
| 误差分成鞅差与衰减项 | 处理可控偏差 | 两部分要分别验证可和性 |
| 先处理辅助噪声再分析轨道 | 指导证明结构 | (U)、$\pi_k^n$、Theorem 2.1 不能直接套到动量递推 |
| 离散和–积分比较 | 新残差界含类似卷积时 | 需要重新验证核形状、单调性与格宽条件 |

**与 N2/N6 的关系，补充分析。** 本文 H2(b) 的权重为 $\alpha_k^2$；它没有预先给出 Fast KM 能量中的权重。讨论笔记中的 N6 使用另一套算法参数，其权重不能从 Nesterov 函数值能量直接移植到本篇。应先推导具体随机 Fast KM 单步式，再确定噪声要求。由某个充分条件无法兼容目标步长，不能直接推出任何随机 Fast KM 加速都不可能。

## 10. 五道推导练习与简答

### 10.1 练习一：算出平均噪声权重

取 $\alpha_n=1/(n+1)$、$\theta_n=\theta$。计算 $\pi_k^n$、$\nu_n$、$\tau_n$ 的量级，并验证 H2。依据原文 Lemma 2.4、Example 2.7，pp. 196–197。

**简答，补充推导：** 乘积望远镜消去后，$\pi_k^n=1/(n+1)$。因此 $\nu_n=\theta\sqrt n/(n+1)$，$\tau_n=\sum_{k=1}^n k/(k+1)^2$ 与 $\log n$ 同阶。H2(a) 的项与 $n^{-3/2}$ 同阶；H2(b) 与 $n^{-2}$ 同阶，均可和。

### 10.2 练习二：分别推导两个步长门槛

在单位方差噪声下，取 $\alpha_n=(n+1)^{-a}$。分别从 H2(a)、H2(b) 得到充分门槛，并说明 $a=2/3$ 的状态。依据原文 Example 2.7，p. 197，及 Appendix B，pp. 212–213。

**简答，补充推导：** $\nu_{n-1}$ 与 $n^{-a/2}$ 同阶；H2(a) 要求 $\sum n^{-3a/2}<\infty$，即 $a>2/3$。H2(b) 要求 $a>1/2$。在 $a=2/3$，前者为调和级数型并发散；此时不能调用 Theorem 2.5，但不能反推迭代点必不收敛。

### 10.3 练习三：补全 Theorem 2.5 的一个更短步骤

已知原文步骤中的 $M_n$ 收敛，且 $X_\infty<\infty$。不使用 ODE，证明 $\overline U_n\to0$。依据原文 p. 197 的求和恒等式。

**简答，补充推导：** 向量级数 $\sum_k\alpha_k\overline U_{k-1}$ 因 $X_\infty<\infty$ 而绝对收敛。由

$$
\overline U_n=M_n-\sum_{k=1}^n\alpha_k\overline U_{k-1}
$$

知 $\overline U_n$ 存在极限 $u$。若 $\lVert u\rVert>0$，则充分大时 $\lVert\overline U_{k-1}\rVert\ge\lVert u\rVert/2$，与 $\sum\alpha_k=\infty$、$X_\infty<\infty$ 矛盾。因此 $u=0$。

### 10.4 练习四：为何 Theorem 2.11 必须先取出最后一项

说明直接把 (2.3) 全部求和项替换成平方根核会发生什么，并解释 (2.4)(b) 在证明中的唯一关键用途。依据原文 (2.4)–(2.6)，pp. 199–200。

**简答，补充推导：** 在 $k=n$ 时替换核出现除以零，而真实 $\sigma(0)=1$。应先保留精确端点项 $2\mu\alpha_n\nu_{n-1}$。(2.4)(b) 在被积函数上升区间，将左侧格宽换为右侧格宽，损失系数至多 $\gamma$，然后才能由右侧区间积分控制离散项。

### 10.5 练习五：将随机输出界转为样本量

设原范数为标准欧氏范数，每步调用一次随机算子。由 (5.4) 求使期望残差至多 $\epsilon$ 的充分 $n_0$，并指出结论对象。依据原文 Corollary 5.4，p. 209。

**简答，补充推导：** 可取整数 $n_0$ 满足

$$
n_0\ge\frac{(R^2+\theta^2)^2}{\tau_1(1/2)^2\epsilon^4}.
$$

所得保证属于按指定分布抽取的 $\widehat x_{n_0}$，不属于 $x_{n_0}$。它是充分样本量上界，不能当作所有算法的下界。

## 11. 原文疑点与引用时的修正

### 11.1 已核实的记号或表述问题

1. **p. 195，§2.1 最后一段：中心极限定理不能推出原文写出的 a.s. 根号速率。** 该段在独立同分布情形将算术平均写为 $O(n^{-1/2})$ a.s.。中心极限定理给出分布尺度及 $O_{\mathbb P}(n^{-1/2})$；它不提供该逐路径界。补充反例：非退化独立标准正态噪声满足迭代对数律，样本均值的路径振幅具有 $\sqrt{\log\log n/n}$ 尺度，故根号归一化序列并非 a.s. 有界。正式 Theorem 2.5 的证明不依赖这句说明。阅读时采用 Lemma 2.4 的均方估计及正式概率论证。
2. **pp. 193、206，SGD 对应噪声的索引。** 原文 (SGD) 使用 $x_{n-1}$，但随后噪声写成在 $x_n$ 上评估。与迭代一致且能验证 H1 的写法应为第 6.3 节中的 $U_n=(2/L)[\nabla f(x_{n-1})-\nabla_xF(x_{n-1},\xi_n)]$。这是直接代回迭代可核实的索引问题。
3. **p. 198，式 (2.2) 前的误差记号。** 文字把 $e_k$ 写成 $\overline U_{k-1}$，但 §2.1 真正定义的是算子值之差。正确关系为 $\lVert e_k\rVert\le\lVert\overline U_{k-1}\rVert$；式 (2.2) 只使用这个上界，因此估计不受影响。
4. **p. 209，式 (5.5) 后的速率描述。** 公式在 $a=1/2$ 时给出平方根对数因子；正文写全对数因子，是更松的上界。对 $a=1$ 的比较也应使用单独的对数分支，不能把 $n^{-(1-a)/2}$ 直接代成常数作为精确描述。
5. **p. 211，Gamma 函数脚注。** 原文脚注将 $\Gamma(z)$ 的积分写成 $\int_0^\infty x^ze^{-x}\,dx$；标准定义应为 $\int_0^\infty x^{z-1}e^{-x}\,dx$。原文 (A.4) 后的 Beta–Gamma 恒等式使用的是标准 Gamma 函数，主公式不需随脚注改变。

### 11.2 需要保留限定条件的地方

**Corollary 4.5 的 H4，p. 206。** 上述证明引用缺少显式假设的情况值得记录。补充检验：取 $f=0$、$F(x,\xi)=\xi x$、$\xi$ 为独立对称单位噪声，选择任意允许的 $L>0$；则 $T=I$，原推论所列的光滑凸及有界噪声条件成立。取 $a=3/5$ 时，H4(i)、H4(ii) 均不成立。这个例子只证明所列假设不能自动推出 H4；其梯度残差恒为零，不是对推论结论的反例。**待验证：** 原文作者是否意图沿用 H4，或是否存在覆盖较小 $a$ 的另行证明。

**Corollary 2.9 中 H2 的对象，p. 198。** H2 含 $\theta_n$ 与 $\nu_n$，混合误差后应说明这些量对应哪一部分。按照其证明，鞅差部分 $W_n$ 应满足 Theorem 2.5 的矩条件，衰减部分 $V_n$ 满足 H3。后续引用时明确这一点。

**Example 2.7 的 a.s. 速率对象，p. 197。** 原文写的是对所有 $b<a-1/2$，$n^b\lVert\overline U_n\rVert\to0$ a.s.。对象是平均噪声，不是 $x_n-x^*$ 或残差。要转成残差速率，需要额外处理 (2.2) 的历史卷积。

**数值边界，p. 204，Figure 2。** $a=4/5$ 在图中出现，原文已承认它不在 Theorem 3.2 的严格参数区间。不能把图中的观察写成定理覆盖。

### 11.3 保留给下一轮精读的问题

1. 对同一噪声模型，能否由 (2.2) 和 Example 2.7 写出适合比较的明确末次残差 a.s. 速率？需要把路径上的常数与可计算确定性常数分开。
2. 对指定的随机 Fast KM，随机算子是在什么点调用，历史噪声是否复用？这决定条件无偏能够消去哪些交叉项。
3. Fast KM 的确定性能量究竟给噪声加上什么权重？应从该算法推导，不能直接沿用本篇 H2 或随机 Nesterov 的 N6。
4. 若目标包含无限维弱收敛，有限维 Theorem 2.1 的聚点论证应由哪条 Hilbert 空间结果替换？
5. 随机 iKM 的有限时域参数与目标无限轨道之间是否存在直接衔接？该问题属于第二篇精读，当前不作结论。

## 12. 核对来源

1. Mario Bravo、Roberto Cominetti，*Stochastic Fixed-Point Iterations for Nonexpansive Maps: Convergence and Error Bounds*，SIAM J. Control Optim. 62(1)，2024，pp. 191–219。[DOI](https://doi.org/10.1137/22M1515550)。主要依据为用户指定的 Zotero 正式出版 PDF，共 29 页；本笔记采用期刊页码。
2. Mario Bravo、Roberto Cominetti、Matías Pavez-Signé，*Rates of convergence for inexact Krasnosel’skii–Mann iterations in Banach spaces*，Mathematical Programming 175，2019，pp. 241–262。[预印本与出版信息](https://arxiv.org/abs/1705.09340)。本笔记使用的是主论文 Theorem 2.1 对该工作的明确转述与引用，没有声称重证其核心度量估计。
3. Patrick L. Combettes、Jean-Christophe Pesquet，*Stochastic Quasi-Fejér Block-Coordinate Fixed Point Iterations with Random Sweeping*，SIAM J. Optim. 25，2015，pp. 1221–1248。[DOI](https://doi.org/10.1137/140971233)。对照版本为 [arXiv:1404.7536v4](https://arxiv.org/abs/1404.7536v4)，PDF pp. 7–8，Corollary 2.7 与 (2.26)–(2.31)。
4. Tong Yang、Tao Jiang、Yuejie Chi、Ashok Cutkosky、Lin Xiao，*Stochastic Inertial Krasnosel’skii–Mann Iteration Achieves Near-Optimal Sample Complexity*，2026。[原文](https://arxiv.org/abs/2609.28543)。仅用于确认已有随机惯性 KM 复杂度方向及附录 A 的直接联系；未在本笔记中扩展为该文综述。
