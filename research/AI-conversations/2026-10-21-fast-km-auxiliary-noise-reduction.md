# 原始复用 Fast KM：辅助噪声归约与随机稳定性比较

日期：2026-10-21。本文为独立推导的研究笔记，不声明首创性。目标限于迭代点的几乎必然弱收敛和残差趋零，不包含随机残差的 $o(1/k)$ 速率。本笔记保留原始 Fast KM 的历史查询复用。

## 1. 来源与本次推导的边界

Bravo–Cominetti（2024）的 Theorem 2.5 通过辅助平均噪声，将随机 KM 归约为逐轨道满足条件的确定性含误差 KM。其 H2(a) 控制平均噪声的加权范数总量，H2(b) 配合鞅差结构控制平均噪声趋零。

Boţ–Nguyen（2023）的 Algorithm 2.1 给出原始 Fast KM；Theorem 3.4 给出无误差迭代的弱收敛。该论文的无误差定理不能直接用于下面的含误差递推。本笔记第 4 节独立证明所需的确定性扰动稳定性引理。

2026-10-21-fast-km-almost-sure-convergence.md 中的上一版采用随机尾段稳定性。本笔记重新推导其关键估计，并在第 6 节将其条件方差预算放宽为无条件二阶矩预算。这是本次推导的扩展，不能归于原笔记原有陈述。

## 2. 统一模型

设 $H$ 为实可分 Hilbert 空间，$T:H\to H$ 非扩张，且 $\operatorname{Fix}T\ne\varnothing$。固定 $\alpha>2$ 和 $0<s\le1$。这里固定的 $\alpha$ 是 Fast KM 的动量参数，与 Bravo–Cominetti 的步长序列 $\alpha_n$ 不同。

定义

$$
a_k=\frac{k+\alpha/2}{k+\alpha},\qquad d_k=\frac{k}{k+\alpha},\qquad k\ge0.
$$

取确定性 $x_0,x_1$。查询前信息为 $\mathcal F_k$，误差 $e_k$ 为 $\mathcal F_{k+1}$-可测、平方可积，且

$$
\mathbb E[e_k\mid\mathcal F_k]=0,\qquad \mathbb E\lVert e_k\rVert^2\le\sigma_k^2<\infty.
$$

$\sigma_k\ge0$ 为确定性均方根上界；$\sigma_k^2$ 才是二阶矩预算。这里不要求条件方差有确定性统一上界，也不要求不同时刻独立。

令 $V=I-T$、$g_k=Vx_k-e_k$。原始复用算法为

$$
x_{k+1}=x_k+d_k(x_k-x_{k-1})-sa_kg_k+sd_kg_{k-1},\qquad k\ge1.
$$

$g_{k-1}$ 是上一轮保存的返回值，不是在本轮重新查询的结果。

为简化归约，定义

$$
M=(1-s)I+sT,\qquad \widehat M_k(x_k)=Mx_k+se_k.
$$

$M$ 非扩张，$\operatorname{Fix}M=\operatorname{Fix}T$。由于 $1+d_k=2a_k$，原算法精确等价于

$$
x_{k+1}=a_kx_k+a_k\widehat M_k(x_k)-d_k\widehat M_{k-1}(x_{k-1}).
$$

这是同一个算法的代数重写，未增加查询。$s=1$ 时 $M=T$。

## 3. 按 Bravo–Cominetti 思想构造辅助噪声

### 3.1 消去直接噪声

定义线性辅助序列

$$
u_0=0,\qquad u_1=sa_0e_0=\frac{s}{2}e_0,
$$

$$
u_{k+1}=a_ku_k+sa_ke_k-sd_ke_{k-1},\qquad k\ge1.
$$

上面第一项记号为拉丁字母 $u$，并非 $\nu$。这一初值是分析上的选择，不改变给定的 $x_1$。

令 $z_k=x_k-u_k$。相减后有

$$
z_{k+1}=a_kz_k+a_kMx_k-d_kMx_{k-1}.
$$

定义有效算子误差

$$
\delta_k=Mx_k-Mz_k.
$$

于是

$$
z_{k+1}=a_kz_k+a_k(Mz_k+\delta_k)-d_k(Mz_{k-1}+\delta_{k-1}).
$$

这恰是以 $M$ 为算子、步长为 1 的含误差复用 Fast KM。非扩张性给出

$$
\lVert\delta_k\rVert\le\lVert u_k\rVert.
$$

因此，一条足够的逐轨道条件是

$$
\sum_{k=1}^{\infty}\lVert u_k\rVert<\infty.
$$

它同时保证 $u_k\to0$ 和有效误差范数可和。与普通 KM 不同，这个辅助递推并非噪声的凸组合；不得直接称它为算术平均。

### 3.2 辅助噪声如何传播

定义

$$
b_k=a_ka_{k-1}-d_k=\frac{\alpha(\alpha-2)}{4(k+\alpha)(k+\alpha-1)}>0,\qquad k\ge1.
$$

令 $v_k=u_k-sa_{k-1}e_{k-1}$。则 $v_1=0$，并且

$$
v_{k+1}=a_kv_k+sb_ke_{k-1}.
$$

因而

$$
u_{k+1}=sa_ke_k+s\sum_{j=1}^{k}b_j\left(\prod_{i=j+1}^{k}a_i\right)e_{j-1}.
$$

这一步保留了同一份旧误差两次出现的抵消，净系数为 $b_j=O(j^{-2})$。若在最开始就对两次出现分别取范数，这个结构会消失。

令 $K_{n,j}$ 表示 $u_n$ 中 $se_j$ 的系数。它由两种情况定义：$K_{j+1,j}=a_j$；对 $n\ge j+2$，

$$
K_{n,j}=b_{j+1}\prod_{i=j+2}^{n-1}a_i.
$$

所有 $K_{n,j}$ 非负。下面证明每个误差的总传播权重恰好为 1：

$$
\sum_{n=j+1}^{\infty}K_{n,j}=1.
$$

记 $\gamma=\alpha/2>1$。对 $m\ge1$，有

$$
\sum_{k=m}^{\infty}\prod_{i=m+1}^{k}a_i=\frac{m+\alpha}{\gamma-1}.
$$

验证方法：令 $P_{m,k}=\prod_{i=m+1}^{k}a_i$。则

$$
(k+\alpha)P_{m,k}-(k+1+\alpha)P_{m,k+1}=(\gamma-1)P_{m,k}.
$$

有限求和后取极限即可。边界项趋零，因为 $P_{m,k}=O(k^{-\gamma})$ 且 $\gamma>1$。乘积阶可由 Gamma 函数比值或对数求和得到。

代入 $m=j+1$，得到

$$
a_j+b_{j+1}\frac{j+1+\alpha}{\gamma-1}=1.
$$

因此，在非负扩展实数意义下，逐轨道有

$$
\sum_{n=1}^{\infty}\lVert u_n\rVert\le s\sum_{j=0}^{\infty}\lVert e_j\rVert.
$$

### 3.3 对应原文的平均噪声均方根尺度

定义本笔记的确定性上界

$$
\nu_n^{\mathrm F}=s\sqrt{\sum_{j=0}^{n-1}K_{n,j}^2\sigma_j^2},\qquad n\ge1.
$$

由于系数确定，且不同时刻的鞅差在期望内积中正交，

$$
\mathbb E\lVert u_n\rVert^2\le (\nu_n^{\mathrm F})^2,\qquad \mathbb E\lVert u_n\rVert\le\nu_n^{\mathrm F}.
$$

这就是与原文 Lemma 2.4 对应的步骤。于是

$$
\sum_{n=1}^{\infty}\nu_n^{\mathrm F}<\infty
$$

保证 $\sum_n\lVert u_n\rVert<\infty$ a.s.，从而 $u_n\to0$ a.s.。证明使用 Tonelli 定理和非负随机变量期望有限性。

这条上界条件有一个透明的等价形式。由于 $a_j\ge1/2$，

$$
\frac{s}{2}\sum_{j=0}^{\infty}\sigma_j\le\sum_{n=1}^{\infty}\nu_n^{\mathrm F}\le s\sum_{j=0}^{\infty}\sigma_j.
$$

右侧利用 $\sqrt{\sum t_j^2}\le\sum |t_j|$ 和每列传播权重总和为 1。因此，对这里定义的确定性预算上界，

$$
\sum_n\nu_n^{\mathrm F}<\infty\quad\Longleftrightarrow\quad\sum_j\sigma_j<\infty.
$$

这是本归约的充分条件，不是算法收敛的必要条件。若预算取得不紧，更不能反推真实辅助过程不收敛。

此外，$\sum_j\sigma_j<\infty$ 本身已通过 Jensen 和 Tonelli 推出 $\sum_j\lVert e_j\rVert<\infty$ a.s.；所以使用这一较强充分条件时，最终点收敛甚至不必要求噪声条件中心化。保留鞅差设定是为了与原文及第二条路线进行同模型比较。

## 4. 必须补出的确定性含误差 Fast KM 引理

### 4.1 陈述

设 $M$ 是 Hilbert 空间上的非扩张算子，固定点集非空。固定 $\alpha>2$。若

$$
z_{k+1}=a_kz_k+a_k(Mz_k+\delta_k)-d_k(Mz_{k-1}+\delta_{k-1})
$$

满足

$$
\sum_{k=0}^{\infty}\lVert\delta_k\rVert<\infty,
$$

则 $z_k$ 弱收敛到 $\operatorname{Fix}M$ 中一点，且 $\lVert z_k-Mz_k\rVert\to0$。误差允许依赖轨道；不要求它无偏。

这是下面独立证明的扰动引理，并非 Boţ–Nguyen 原文 Theorem 3.4 的直接陈述。

### 4.2 一个非扩张的双状态表示

令 $G=I-M$、$\widetilde g_k=Gz_k-\delta_k$，定义

$$
Y_k=z_k+\frac{k}{\alpha-1}(z_k-z_{k-1}+\widetilde g_{k-1}),\qquad W_k=z_k-Y_k.
$$

再记

$$
c=\frac{\alpha-2}{2(\alpha-1)},\qquad h=\frac{\alpha}{2(\alpha-1)},\qquad q_k=\frac{k+1}{k+\alpha},\qquad \rho=\frac{c}{h}>0.
$$

直接代入递推可得

$$
Y_{k+1}=Y_k-c(Gz_k-\delta_k),
$$

$$
W_{k+1}=q_k\bigl(W_k-h(Gz_k-\delta_k)\bigr),\qquad z_k=Y_k+W_k.
$$

在 $H\times H$ 上定义随指标变化的范数

$$
\lVert(Y,W)\rVert_k^2=\lVert Y\rVert^2+m_k\lVert W\rVert^2,\qquad m_k=\rho\left(\frac{k+\alpha-1}{k}\right)^2.
$$

令 $\Phi_k$ 为将上述 $\delta_k$ 设为零后的双状态映射。对两个状态之差，记 $X=\Delta Y+\Delta W$、$R=Gz-Gz'$。利用 $m_{k+1}q_k^2=\rho$、$\rho h=c$ 和 $c+h=1$，平方展开为

$$
\lVert\Phi_k(Y,W)-\Phi_k(Y',W')\rVert_{k+1}^2
=\lVert(\Delta Y,\Delta W)\rVert_k^2-(m_k-\rho)\lVert\Delta W\rVert^2-2c\langle X,R\rangle+c\lVert R\rVert^2.
$$

$M$ 非扩张给出 $2\langle X,R\rangle\ge\lVert R\rVert^2$，所以

$$
\lVert\Phi_k(Y,W)-\Phi_k(Y',W')\rVert_{k+1}\le\lVert(Y-Y',W-W')\rVert_k.
$$

加入误差的双状态增量为 $(c\delta_k,q_kh\delta_k)$，其第 $k+1$ 个范数等于 $\sqrt c\lVert\delta_k\rVert$。

### 4.3 可和扰动不会改变尾段的收敛性质

从任意时刻 $m$ 的同一双状态出发，令 $z_k^{[m]}$ 为此后误差全为零的比较轨道。由上面的非扩张性和三角不等式，

$$
\lVert(Y_k-Y_k^{[m]},W_k-W_k^{[m]})\rVert_k\le\sqrt c\sum_{i=m}^{k-1}\lVert\delta_i\rVert.
$$

又因为 $m_k\ge\rho$ 且 $c(1+1/\rho)=1$，

$$
\sup_{k\ge m}\lVert z_k-z_k^{[m]}\rVert\le\sum_{i=m}^{\infty}\lVert\delta_i\rVert.
$$

每条精确比较轨道从 $m+1$ 开始满足原始无误差 Fast KM 的两步递推。Boţ–Nguyen Theorem 3.4 的证明对任意有限起始指标仍成立：其局部能量估计从某个有限指标成立，尾段求和和 Opial 论证不依赖前面有限步。因此

$$
z_k^{[m]}\rightharpoonup p_m\in\operatorname{Fix}M,\qquad \lVert Gz_k^{[m]}\rVert\to0.
$$

令 $\varepsilon_m=\sum_{i=m}^{\infty}\lVert\delta_i\rVert\to0$。对两条精确比较轨道，三角不等式和范数的弱下半连续性给出

$$
\lVert p_m-p_\ell\rVert\le\varepsilon_m+\varepsilon_\ell.
$$

故 $p_m$ 按范数收敛到某个 $p_\infty\in\operatorname{Fix}M$。对任意 $v\in H$，

$$
\limsup_{k\to\infty}|\langle z_k-p_\infty,v\rangle|
\le(\varepsilon_m+\lVert p_m-p_\infty\rVert)\lVert v\rVert.
$$

令 $m\to\infty$ 得 $z_k\rightharpoonup p_\infty$。由于 $G$ 是 2-Lipschitz，

$$
\limsup_{k\to\infty}\lVert Gz_k\rVert\le2\varepsilon_m,
$$

再令 $m\to\infty$ 得残差趋零。确定性引理证毕。

## 5. 辅助噪声归约得到的随机命题

在第 2 节的同一原始复用算法下，若

$$
\sum_{k=0}^{\infty}\sigma_k<\infty,
$$

则第 3 节保证 $u_k\to0$ 且 $\sum_k\lVert\delta_k\rVert<\infty$ a.s.。在该概率为一的事件上逐轨道应用第 4 节引理，得到

$$
z_k\rightharpoonup x_\infty\in\operatorname{Fix}M,\qquad \lVert z_k-Mz_k\rVert\to0.
$$

由于 $x_k=z_k+u_k$、$u_k\to0$、$I-M=s(I-T)$，

$$
x_k\rightharpoonup x_\infty\in\operatorname{Fix}T,\qquad \lVert x_k-Tx_k\rVert\to0\quad\text{a.s.}
$$

可分性保证弱极限可以作为 $H$ 值可测随机变量。有限维时为范数收敛。

这条证明按“线性辅助噪声 → 有效扰动范数控制 → 确定性含误差收敛”的顺序展开，与 Bravo–Cominetti 的归约思想一致。不过它使用的确定性扰动引理和噪声滤波器都不同。

## 6. 上一版随机稳定性路线的核对与放宽

本节仍使用第 2 节的原始复用算法，直接定义 $V=I-T$ 和双状态

$$
y_k=x_k+\frac{k}{\alpha-1}(x_k-x_{k-1}+sg_{k-1}),\qquad w_k=x_k-y_k.
$$

此处的常数含步长：

$$
c=\frac{s(\alpha-2)}{2(\alpha-1)},\qquad h=\frac{s\alpha}{2(\alpha-1)},\qquad \rho=c/h,\qquad m_k=\rho\left(\frac{k+\alpha-1}{k}\right)^2.
$$

状态更新为

$$
y_{k+1}=y_k-c(Vx_k-e_k),\qquad w_{k+1}=q_k(w_k-h(Vx_k-e_k)).
$$

从时刻 $m$ 的同一状态启动无噪声比较轨道。记差量为 $Y_k,W_k$，$X_k=Y_k+W_k$，$R_k=Vx_k-Vx_k^{[m]}$，以及

$$
D_k=\lVert Y_k\rVert^2+m_k\lVert W_k\rVert^2.
$$

平方展开精确给出

$$
D_{k+1}=D_k-(m_k-\rho)\lVert W_k\rVert^2-2c\langle X_k,R_k\rangle+cs\lVert R_k\rVert^2+2c\langle X_k-sR_k,e_k\rangle+cs\lVert e_k\rVert^2.
$$

因为 $X_k,R_k$ 在查询前可测，鞅差条件消去线性交叉项。令 $Q_k=\mathbb E[\lVert e_k\rVert^2\mid\mathcal F_k]$，得到

$$
\mathbb E[D_{k+1}\mid\mathcal F_k]\le D_k+csQ_k.
$$

只假设

$$
\sum_{k=0}^{\infty}\sigma_k^2<\infty.
$$

不需要额外的确定性条件方差上界。定义

$$
A_k=\mathbb E\left[\sum_{i=k}^{\infty}\lVert e_i\rVert^2\,\middle|\,\mathcal F_k\right].
$$

由于整个误差平方和可积，$A_k$ 有意义，并有

$$
\mathbb E[A_{k+1}\mid\mathcal F_k]=A_k-Q_k.
$$

因此 $Z_k=D_k+csA_k$ 为非负超鞅。由其最大值不等式及 $D_m=0$，

$$
\mathbb P\left(\sup_{k\ge m}D_k>t\right)\le\frac{cs}{t}\sum_{i=m}^{\infty}\sigma_i^2.
$$

利用 $(1+1/\rho)cs=s^2$，得到上一版的尾段界：

$$
\mathbb P\left(\sup_{k\ge m}\lVert x_k-x_k^{[m]}\rVert>\varepsilon\right)
\le\frac{s^2}{\varepsilon^2}\sum_{i=m}^{\infty}\sigma_i^2.
$$

选取 $m_j$ 使 $s^2\sum_{i\ge m_j}\sigma_i^2\le2^{-4j}$，并取 $\varepsilon_j=2^{-j}$。失败概率可和，所以 Borel–Cantelli 引理保证，在同一概率为一的事件上，充分大 $j$ 满足

$$
\sup_{k\ge m_j}\lVert x_k-x_k^{[m_j]}\rVert\le2^{-j}.
$$

逐轨道调用精确 Fast KM 的弱收敛，并沿第 4.3 节的极限比较论证，得到原始 $x_k$ 的几乎必然弱收敛及残差趋零。

因此，上一版的核心稳定性论证可成立，且条件方差上界不是必要的额外假设：H1 型条件中心化加无条件二阶矩可和已足够。这只是点收敛结论。

## 7. 三条路线的条件对应

| 部分 | Bravo–Cominetti Theorem 2.5 | 本笔记的辅助噪声归约 | 本笔记的直接随机稳定性 |
|---|---|---|---|
| 空间与算子 | 有限维给定范数，$T$ 非扩张 | 可分 Hilbert，$T$ 非扩张 | 同左 |
| 参数 | H0：$0<\alpha_n<1$，$\sum\alpha_n(1-\alpha_n)=\infty$ | 固定 $\alpha>2$，$0<s\le1$ | 同左 |
| H1 型条件 | 条件中心化，无条件二阶矩有限 | 同型条件；采用较强可和条件时甚至可省去中心化 | 条件中心化不可在本证明中省略 |
| 有效扰动 | $\lVert e_n^{\mathrm{eff}}\rVert\le\lVert\overline U_{n-1}\rVert$ | $\lVert\delta_k\rVert\le\lVert u_k\rVert$ | 直接比较随机与精确双状态 |
| H2(a) 型要求 | $\sum\alpha_n\nu_{n-1}<\infty$ | $\sum\nu_n^{\mathrm F}<\infty$，对定义的预算等价于 $\sum\sigma_k<\infty$ | 不要求范数绝对可和 |
| H2(b) 型要求 | $\sum\alpha_n^2\theta_n^2<\infty$ | $\sum\sigma_k^2<\infty$ 已由上一条推出，无需单列 | $\sum\sigma_k^2<\infty$ |
| 结论 | a.s. 点收敛，无明确点收敛速率 | a.s. 弱点收敛、残差趋零，无速率 | 相同 |

要直接比较空间设定，可将三者都限制在有限维欧氏空间。Hilbert 版本使用内积结构，不能宣称覆盖原文的任意范数。

若仅用幂次预算 $\sigma_k^2\le C(k+1)^{-q}$ 作为检验，辅助归约由 $q>2$ 保证，直接随机稳定性由 $q>1$ 保证。这些都是充分范围，不是必要性或最优门槛。

原文对普通 SKM 取 $\alpha_n=(n+1)^{-a}$、$2/3<a\le1$ 时，统一有界二阶矩就足以保证 H2。Fast KM 在本笔记中固定 $s>0$，当前噪声系数 $sa_k\to s$，没有对应的逐次缩小。不能把普通 SKM 的递减步长条件原样移植过来。

还需区分两种代价：固定参数 Fast KM 的持续新噪声并未被步长缩小；而辅助归约中的 $\sum\sigma_k<\infty$ 比直接稳定性的 $\sum\sigma_k^2<\infty$ 更强，则来自将随机影响转换成逐轨道范数绝对总量的证明要求，不能认定是惯性算法本身必需的条件。

## 8. 方法取舍

辅助噪声归约的结构最接近 Bravo–Cominetti：能明确展示旧误差如何抵消、有效扰动如何形成、确定性结果如何逐轨道应用。但它还要证明线性传播核和确定性扰动引理，完整证明并未更短；其方便核查的噪声条件也更强。

在同一条件中心化模型下，直接随机稳定性更适合作为当前点收敛的主证明。它保留二阶矩层面的抵消，仅需方差预算可和。辅助归约适合作为机制说明和方法对照。

两条路线均未证明在上述条件下保留 $o(1/k)$ 的随机残差速率。本笔记不比较样本复杂度，不宣布新的研究缺口。

## 9. 参考位置与核对记录

1. Bravo、Cominetti，*Stochastic Fixed-Point Iterations for Nonexpansive Maps: Convergence and Error Bounds*，SIAM J. Control Optim. 62(1)，2024，pp. 191–219。本文参考其 §2.1 的变量变换、Lemma 2.4、H2(a)(b)、Theorem 2.5 的证明组织；未将本笔记新引理归于该文。
2. Boţ、Nguyen，*Fast Krasnosel’skiĭ–Mann Algorithm with a Convergence Rate of the Fixed Point Iteration of o(1/k)*，SIAM J. Numer. Anal. 61(6)，2023，pp. 2813–2843。核对 arXiv:2206.09462v2，Algorithm 2.1、Proposition 3.3、Theorems 3.4–3.5。原文链接：https://arxiv.org/pdf/2206.09462 。
3. 本会话先前生成的 `2026-10-21-fast-km-almost-sure-convergence.md`：本次核对的双状态、变动度量、全未来尾段概率界与弱极限衔接。

写作参照：算法及参数沿用 Boţ–Nguyen；查询前信息与误差索引沿用项目当前模型；条件分工与逐轨道归约沿用 Bravo–Cominetti。传播系数 $K_{n,j}$、$\nu_n^{\mathrm F}$ 和扰动稳定性引理均是本笔记中的局部记号和独立推导，不替换项目主稿记号。

已针对会改变结论的代数关系进行核对：$a_ka_{k-1}-d_k$ 的系数、每个噪声传播系数的列和、双状态变换、$m_{k+1}q_k^2=\rho$、$c^2+\rho h^2=cs$ 以及尾段概率界的常数。代数核对不替代概率与弱收敛证明；这些部分已在正文展开。未修改远端论文。
