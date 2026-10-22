# 原始复用 Fast KM 的几乎必然点收敛

日期：2026-10-21。状态：本次独立推导的研究草稿，附完整证明；不声明文献首创性。本文保留 Boţ–Nguyen 的原始系数和历史查询值，不使用双查询替代算法。

**主要结论：条件中心化噪声的方差预算可和，足以保证原始复用 Fast KM 的迭代点几乎必然弱收敛。这里不证明随机残差的 $o(1/k)$ 速率。**

## 1. 命题

设 $H$ 为实可分 Hilbert 空间，$T:H\to H$ 非扩张，且 $\operatorname{Fix}T\ne\varnothing$。令 $V=I-T$。固定 $\alpha>2$ 和 $0<s\le1$，并取确定性初值 $x_0,x_1\in H$。

$\mathcal F_k$ 表示第 $k$ 次查询之前的信息。设 $x_k$ 为 $\mathcal F_k$-可测，误差 $e_k$ 为平方可积、$\mathcal F_{k+1}$-可测的 $H$ 值随机变量，并满足

$$
\mathbb E[e_k\mid\mathcal F_k]=0,
\qquad
\mathbb E[\lVert e_k\rVert^2\mid\mathcal F_k]\le\sigma_k^2,
$$

其中 $\sigma_k^2$ 是确定性非负数，且

$$
\sum_{k=0}^{\infty}\sigma_k^2<\infty.
$$

令 $g_k=Vx_k-e_k=x_k-\widehat T_k(x_k)$。初始化时计算并保存 $g_0$，随后对 $k\ge1$ 运行

$$
x_{k+1}=x_k+\frac{k}{k+\alpha}(x_k-x_{k-1})
-s\frac{k+\alpha/2}{k+\alpha}g_k
+s\frac{k}{k+\alpha}g_{k-1}.
$$

其中 $g_{k-1}$ 是上一轮保存的同一返回值。则存在取值于 $\operatorname{Fix}T$ 的随机变量 $x_\infty$，使得

$$
x_k\rightharpoonup x_\infty\quad\text{almost surely},
\qquad
\lVert x_k-Tx_k\rVert\longrightarrow0\quad\text{almost surely}.
$$

若 $H$ 有限维，则迭代点的收敛为范数收敛。不需要噪声跨时刻独立，也不需要高阶矩。

## 2. 证明

### 2.1 将旧误差纳入查询前状态

定义

$$
y_k=x_k+\frac{k}{\alpha-1}
\bigl(x_k-x_{k-1}+s g_{k-1}\bigr),
\qquad k\ge1.
$$

这里 $y_k$ 是 $\mathcal F_k$-可测的。再令

$$
c=\frac{s(\alpha-2)}{2(\alpha-1)},
\qquad
h=s-c=\frac{s\alpha}{2(\alpha-1)},
\qquad
w_k=x_k-y_k,
\qquad
q_k=\frac{k+1}{k+\alpha}.
$$

原递推等价于

$$
y_{k+1}=y_k-cg_k,
$$

$$
w_{k+1}=q_k(w_k-hg_k),
\qquad x_k=y_k+w_k.
$$

验证第一式：将 $y_{k+1}-y_k$ 乘以 $\alpha-1$，得到

$$
(\alpha-1)(y_{k+1}-y_k)
=(k+\alpha)(x_{k+1}-x_k)
+s(k+1)g_k
-k(x_k-x_{k-1}+s g_{k-1}).
$$

代入原递推后，右侧等于 $-s(\alpha-2)g_k/2$。第二式由 $w_{k+1}=x_{k+1}-y_{k+1}$ 直接得到。

因此，新的状态递推只接受当前随机输入 $e_k$：

$$
y_{k+1}=y_k-cVx_k+ce_k,
$$

$$
w_{k+1}=q_k\bigl(w_k-hVx_k+he_k\bigr).
$$

这一步没有假设 $e_{k-1}$ 重新成为鞅差。旧误差已包含在 $y_k,w_k$ 中；当前 $e_k$ 对这些查询前状态条件中心化。若 $T$ 非线性，整个双状态动力学仍然非线性。

### 2.2 两条轨道之间的稳定性估计

定义正数

$$
\rho=\frac{c}{h}=\frac{\alpha-2}{\alpha},
\qquad
m_k=\rho\left(\frac{k+\alpha-1}{k}\right)^2.
$$

它们满足

$$
m_k\ge\rho>0,
\qquad m_{k+1}q_k^2=\rho.
$$

从某个确定性时刻 $m\ge1$ 开始，以实际状态 $(y_m,w_m)$ 初始化一条精确比较轨道 $(y_k^{[m]},w_k^{[m]})$。该轨道在以后各步使用同一系数，但令噪声恒为零。记

$$
x_k^{[m]}=y_k^{[m]}+w_k^{[m]}.
$$

该比较轨道只依赖时刻 $m$ 已有的信息，因而对所有 $k\ge m$ 都是 $\mathcal F_k$-可测的。定义差量

$$
Y_k=y_k-y_k^{[m]},\qquad
W_k=w_k-w_k^{[m]},\qquad
X_k=x_k-x_k^{[m]}=Y_k+W_k,
$$

$$
R_k=Vx_k-Vx_k^{[m]},
\qquad
D_k=\lVert Y_k\rVert^2+m_k\lVert W_k\rVert^2.
$$

相减得到

$$
Y_{k+1}=Y_k-c(R_k-e_k),
\qquad
W_{k+1}=q_k\bigl(W_k-h(R_k-e_k)\bigr).
$$

利用 $m_{k+1}q_k^2=\rho$、$\rho h=c$、$c^2+\rho h^2=cs$，展开平方范数得到精确恒等式

$$
D_{k+1}
=D_k-(m_k-\rho)\lVert W_k\rVert^2
-2c\langle X_k,R_k\rangle
+cs\lVert R_k\rVert^2
+2c\langle X_k-sR_k,e_k\rangle
+cs\lVert e_k\rVert^2.
$$

由于 $T$ 非扩张，$V=I-T$ 为 $1/2$-cocoercive，即

$$
2\langle X_k,R_k\rangle\ge\lVert R_k\rVert^2.
$$

又由于 $X_k,R_k$ 为 $\mathcal F_k$-可测，当前噪声的线性交叉项条件期望为零。因此

$$
\mathbb E[D_{k+1}\mid\mathcal F_k]
\le D_k-(m_k-\rho)\lVert W_k\rVert^2
-c(1-s)\lVert R_k\rVert^2
+cs\sigma_k^2
\le D_k+cs\sigma_k^2.
$$

这是证明的核心单步估计。它适用于任意启动时刻 $m$，也保留了边界步长 $s=1$。它没有把 $e_k$ 与 $e_{k-1}$ 分别用绝对值估计。

### 2.3 控制整个未来尾段，而非单个时刻

令

$$
S_k=cs\sum_{i=k}^{\infty}\sigma_i^2,
\qquad
Z_k=D_k+S_k,\qquad k\ge m.
$$

由上一节的不等式，$Z_k$ 是非负超鞅。两条轨道在时刻 $m$ 同步初始化，所以 $D_m=0$、$Z_m=S_m$。非负超鞅的最大值不等式给出

$$
\mathbb P\left(\sup_{k\ge m}D_k>t\right)
\le\frac{cs}{t}\sum_{i=m}^{\infty}\sigma_i^2,
\qquad t>0.
$$

另一方面，加权 Cauchy–Schwarz 不等式给出

$$
\lVert X_k\rVert^2
\le\left(1+\frac1\rho\right)D_k.
$$

注意常数恰好满足

$$
\left(1+\frac1\rho\right)cs=s^2.
$$

因此，对任意 $\varepsilon>0$，有整个尾段的概率保证

$$
\boxed{
\mathbb P\left(\sup_{k\ge m}
\lVert x_k-x_k^{[m]}\rVert>\varepsilon\right)
\le\frac{s^2}{\varepsilon^2}
\sum_{i=m}^{\infty}\sigma_i^2.
}
$$

这里的上确界覆盖所有 $k\ge m$。这一点使下面的几乎必然论证成立，不能用固定时刻的期望界代替。

选择确定性递增时刻 $m_j\to\infty$，使

$$
s^2\sum_{i=m_j}^{\infty}\sigma_i^2\le2^{-4j}.
$$

取 $\varepsilon=2^{-j}$，上式给出的失败概率不超过 $2^{-2j}$。第一 Borel–Cantelli 引理因此保证：在一个概率为一的事件上，存在有限 $J(\omega)$，使对所有 $j\ge J(\omega)$，都有

$$
\sup_{k\ge m_j}\lVert x_k-x_k^{[m_j]}\rVert\le2^{-j}.
$$

不要求这些事件独立。

### 2.4 调用确定性 Fast KM 收敛定理

固定上一节概率为一事件中的一条轨道。

对每个 $j$，精确比较轨道 $(y_k^{[m_j]},w_k^{[m_j]})$ 是无噪声双状态递推。消去辅助变量后，$x_k^{[m_j]}$ 从 $k=m_j+1$ 开始满足 Boţ–Nguyen Algorithm 2.1 的原始更新式，使用初始两点 $x_{m_j}^{[m_j]},x_{m_j+1}^{[m_j]}$。

Boţ–Nguyen 的 Theorem 3.4 及 Proposition 3.3 证明只依赖足够大指标处的局部递推和尾段求和。把起始指标 $1$ 替换成任意固定的 $m_j+1$，仅改变有限的初始项。因此该证明适用于这里的精确尾段轨道，并给出

$$
x_k^{[m_j]}\rightharpoonup p_j\in\operatorname{Fix}T,
\qquad
\lVert Vx_k^{[m_j]}\rVert\to0.
$$

这一步使用确定性点收敛结果；无须将确定性 $o(1/k)$ 速率转成随机速率。

对充分大的 $i,j$，以及 $k\ge\max\{m_i,m_j\}$，

$$
\lVert x_k^{[m_i]}-x_k^{[m_j]}\rVert
\le2^{-i}+2^{-j}.
$$

令 $k\to\infty$，由范数的弱下半连续性，得到

$$
\lVert p_i-p_j\rVert\le2^{-i}+2^{-j}.
$$

故 $(p_j)$ 为范数 Cauchy 序列，收敛到某个 $p_\infty\in\operatorname{Fix}T$。这里使用 Hilbert 空间完备性以及不动点集的范数闭性。

任取 $v\in H$。对充分大的固定 $j$，

$$
\limsup_{k\to\infty}
\bigl|\langle x_k-p_\infty,v\rangle\bigr|
\le\bigl(2^{-j}+\lVert p_j-p_\infty\rVert\bigr)\lVert v\rVert.
$$

再令 $j\to\infty$，即得 $x_k\rightharpoonup p_\infty$。由于 $V$ 为 $2$-Lipschitz，

$$
\limsup_{k\to\infty}\lVert Vx_k\rVert
\le2\,2^{-j}.
$$

令 $j\to\infty$ 得残差趋零。若 $H$ 有限维，精确轨道的弱收敛就是范数收敛；同一尾段比较进一步给出 $x_k\to p_\infty$。

最后，可分性保证上述弱极限定义了强可测的 $H$ 值随机变量；在零概率例外集上取任一固定不动点，即得到命题中的 $x_\infty$。证明完成。

## 3. 结论边界

### 3.1 与 Bravo–Cominetti Theorem 2.5 的对应

两者都先用概率论建立轨道性质，再逐轨道使用确定性收敛理论。本稿的辅助对象是包含历史查询的双状态，以及从该状态启动的精确尾段轨道；没有直接照搬普通 KM 的平均噪声递推。

普通 KM 的归约要求平均噪声趋零和加权绝对可和。本稿使用的是尾方差控制的全未来稳定性估计，不要求将噪声或辅助误差转成加权绝对可和的扰动。

### 3.2 点收敛与快速率严格区分

本命题要求 $\sum_k\sigma_k^2<\infty$。对于方差预算 $\sigma_k^2\le C(k+1)^{-q}$，$q>1$ 是满足这一条件的充分范围。条件并非必要性声明，也没有覆盖只有固定方差上界的持续噪声模型。

项目 N6 要求 $\sum_k(k+1)^2\sigma_k^2<\infty$，它是更强的条件。本命题没有证明在更弱条件下仍保留 $o(1/k)$ 残差，也没有完成 N6 下的快速率定理。

事实上，仅凭本命题的假设不能普遍得到 $o(1/k)$。取一维 $T=0$、$s=1$，确定性零初值，并令独立中心高斯噪声满足 $\mathbb E e_k^2=(k+1)^{-2}$。此时方差预算可和，但

$$
x_{k+1}=\frac{k+\alpha/2}{k+\alpha}x_k
+\frac{k+\alpha/2}{k+\alpha}e_k
-\frac{k}{k+\alpha}e_{k-1}.
$$

当前噪声独立于过去，因而

$$
\operatorname{Var}\bigl((k+1)x_{k+1}\bigr)
\ge\left(\frac{k+\alpha/2}{k+\alpha}\right)^2\longrightarrow1.
$$

该随机变量是中心高斯，故不能依概率趋零，更不能几乎必然趋零。这与本命题的无速率点收敛不矛盾。

### 3.3 averaged 算子扩展

若 $T=(1-\theta)I+\theta R$，其中 $0<\theta\le1$、$R$ 非扩张，则取 $0<s\le1/\theta$。相同证明中唯一改变的估计为

$$
\mathbb E[D_{k+1}\mid\mathcal F_k]
\le D_k-(m_k-\rho)\lVert W_k\rVert^2
-c(1/\theta-s)\lVert R_k\rVert^2
+cs\sigma_k^2.
$$

其余步骤不变。这里 $R_k$ 仍表示两条轨道的 $V$ 值之差，勿与 averaged 表示中的算子 $R$ 混淆。

## 4. 文献核对与来源

核对日期：2026-10-21。下述比较只涉及指定原文，不构成全领域的首创性证明。

1. **Boţ–Nguyen，SINUM 2023。** *Fast Krasnosel’skiĭ–Mann Algorithm with a Convergence Rate of the Fixed Point Iteration of o(1/k)*，61(6), 2813–2843，DOI 10.1137/22M1504305；核对 arXiv:2206.09462v2。Algorithm 2.1 提供本文算法；Proposition 3.3、Theorem 3.4 提供精确轨道残差趋零和弱收敛。以上文献不是随机点收敛命题的来源。

2. **Nguyen-Trung–Tran-Dinh，AFP，2025。** *A Class of Accelerated Fixed-Point-Based Methods with Delayed Inexact Oracles and Its Applications*，arXiv:2512.13547v1。Theorem 3.2、Corollary 2 已证明其算法的几乎必然点收敛与残差速率。Lemma 3 在基本能量上加入算子差和估计误差项；Appendix B.1、B.3 控制误差代价，没有把已知旧误差当成新鞅差。其主结果要求指定的时变步长及参数约束，不能直接代入本稿的原始 Fast KM 系数。

3. **Tran-Dinh，VR-FKM。** *Variance-Reduced Fast Krasnosel’skiǐ-Mann Methods for Finite-Sum Root-Finding Problems*，arXiv:2406.02413v4，2026-09-09。Theorem 3.4 给出其估计器和参数条件下的几乎必然点收敛。Definition 2.1 对完整差分方向要求条件无偏，与直接复用上一轮含噪返回值的模型不同。

4. **Yang–Jiang–Chi–Cutkosky–Xiao，随机 iKM，2026。** *Stochastic Inertial Krasnosel’skii–Mann Iteration Achieves Near-Optimal Sample Complexity*，arXiv:2609.28543v1。Appendix A, Proposition 1 给出确定性 Fast KM 与 iKM 的参数对应，并明确该参数组不同于其主定理的随机参数方案。其主结果不能仅凭这个算法对应就充当本命题的证明。

5. **Cortild–Peypouquet，JOTA 2025。** *Krasnoselskii–Mann Iterations: Inertia, Perturbations and Approximation*，204, Article 35，DOI 10.1007/s10957-024-02600-5。其 Hypothesis 2.1 要求惯性相关参数一致小于一，并要求松弛参数有正常数下界；对应 Fast KM 的 iKM 参数不满足这些限制。本文未将其作为本命题的直接来源。

**检索结论：已有随机加速不动点方法的点收敛结果。以上核对没有确认“原始 Fast KM 系数、复用旧返回值、可和方差、一般非扩张算子”的同一命题已有公开出处。本稿是独立证明，不据此声称新颖性。**

## 5. 配套写作与核查记录

| 草稿部分 | 参照位置 | 采用方式 |
|---|---|---|
| 算法、初值、参数先于结论 | Boţ–Nguyen Algorithm 2.1 | 保留原始两步递推及参数范围 |
| 查询前 filtration 与条件中心化 | 项目 paper/main.tex 的 oracle 设定；随机 iKM §2.2 | 保留 $e_k$、$\mathcal F_k$、$\sigma_k^2$ |
| 几乎必然点收敛的陈述 | Bravo–Cominetti Theorem 2.5；Boţ–Nguyen Theorem 3.4 | 随机极限取值于不动点集；Hilbert 空间写弱收敛 |
| 辅助状态及两轨道平方距离 | 本次代数推导 | $y_k,w_k,m_k,D_k$ 只在本独立草稿中使用，不替换旧证明笔记的同名符号 |
| 超鞅尾段比较及极限衔接 | 本次证明 | 不归于上述文献已有结论；不使用随机快速率作为前提 |

已用符号计算核对：原始复用递推与双状态更新的等价关系、$m_{k+1}q_k^2=\rho$、两轨道距离的精确展开、尾段界系数 $(1+1/\rho)cs=s^2$。符号计算只核对代数恒等式；概率与弱极限步骤由本文证明给出。未执行数值收敛实验，也未将本稿写入远端论文。
