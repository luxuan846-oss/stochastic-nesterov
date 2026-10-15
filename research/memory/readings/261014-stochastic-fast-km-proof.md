# 随机 Fast KM 的能量、噪声项与可验证结论

日期：2026-10-14。用途：配合研究主报告，明确哪些结论已完成推导，哪些问题仍待解决。

**结论。** 对每步重新查询两个点的版本，下文给出 N6 下几乎必然残差 $o(1/k)$ 和迭代点弱极限的证明。对复用上一步查询值的原 Fast KM，本次只证明更强的加权绝对可和条件足够；N6 的一般结论仍待证明。复用查询的噪声抵消具有实质作用，不能把两个随机实现视为同一个算法。

文中“本次证明”表示下文提供独立推导，不表示已获得公开文献中的新颖性认可。限定范围的独立复核未发现 P1–P4 的实质证明错误；复核方法、修订和未解决问题见 [复核记录](261014-stochastic-km-proof-audit.md)。外部跨模型复核调用超时，没有获得该服务的结论。

## 1. 模型与记号

$H$ 为实可分 Hilbert 空间。$T:H\to H$ 为 $\theta$-averaged 算子，$0<\theta\le1$，且 $\operatorname{Fix}T\ne\varnothing$。这里允许 $\theta=1$ 表示非扩张算子。令 $V=\operatorname{Id}-T$，则

$$
\langle Vx-Vy,x-y\rangle\ge \frac{1}{2\theta}\lVert Vx-Vy\rVert^2.
$$

本文采用固定 $0<s\le1/\theta$。为给出可直接核查的常数，随机定理取 $\alpha=4$。一般 $\alpha>2$ 的能量恒等式也列出，但随机定理不依赖对一般参数区间的省略推断。

原确定性 Fast KM 为

$$
x_{k+1}=x_k+\frac{k}{k+\alpha}(x_k-x_{k-1})-b_k V(x_k)+c_k V(x_{k-1}),
$$

$$
b_k=\frac{s(k+\alpha/2)}{k+\alpha},\qquad c_k=\frac{sk}{k+\alpha}.
$$

出处：[Boţ–Nguyen，arXiv:2206.09462v2](https://arxiv.org/abs/2206.09462)，Algorithm 2.1、式 2.7。其确定性弱极限见 Theorem 3.4，little-o 残差见 Theorem 3.5。

固定 $x^\star\in\operatorname{Fix}T$。所有噪声条件相对于查询前的信息 $\mathcal F_k$ 陈述。若使用随机初值，要求 $\mathbb E\lVert x_0\rVert^2+\mathbb E\lVert x_1\rVert^2<\infty$。以下证明先采用确定的方差上界；只给路径可和的随机上界时，还需要局部化和每步可积性，不能直接推出期望复杂度。

## 2. 原能量与局部下降

记

$$
r_k=x_k-x^\star,\qquad d_k=k(x_k-x_{k-1}),\qquad w_k=sk V(x_{k-1}),\qquad C_\alpha=\frac{3\alpha-2}{2(\alpha-1)}.
$$

原文 Section 3、Lemma 3.1 前的能量展开后恰为

$$
E_{\lambda,k}=2\lambda(\alpha-1)\lVert r_k\rVert^2+4\lambda\langle r_k,d_k+w_k\rangle+2\lVert d_k\rVert^2+2C_\alpha\langle d_k,w_k\rangle+C_\alpha\lVert w_k\rVert^2.
$$

这与原文的平方范数表达式完全相同。对 $0<\lambda<(3\alpha-2)/4$，它是三个变量的正定二次型。验证方法：$(d,w)$ 子块为

$$
\begin{pmatrix}2&C_\alpha\\ C_\alpha&C_\alpha\end{pmatrix},
$$

其行列式为 $C_\alpha(2-C_\alpha)>0$。对该子块作 Schur complement 后，剩余系数为

$$
2\lambda(\alpha-1)-\frac{4\lambda^2}{C_\alpha}>0.
$$

因此，存在仅依赖 $\alpha,\lambda$ 的 $a_\lambda,A_\lambda>0$，满足

$$
a_\lambda(\lVert r_k\rVert^2+\lVert d_k\rVert^2+\lVert w_k\rVert^2)\le E_{\lambda,k}\le A_\lambda(\lVert r_k\rVert^2+\lVert d_k\rVert^2+\lVert w_k\rVert^2).
$$

原文 Lemma 3.1、式 3.1 给出能量差上界。其右端包含距离与残差的配对项、速度平方、速度与残差的混合项，以及 $k^2\lVert V(x_k)-V(x_{k-1})\rVert^2$ 项。Lemma 3.2 消除混合项。Proposition 3.3 的证明随后给出逐项可和性。

下面写出本次使用的明确形式。取 $\alpha=4$、$\lambda\in\{2,9/4\}$，二者均位于原文式 3.3 给出的允许区间 $(5/3,5/2)$。记 $\rho=\sqrt{9/10}<1$。存在仅依赖参数的整数 $k_0$，使得对任意当前状态及其满足确定性更新的虚拟下一步 $\bar x_{k+1}$，有

$$
E^{\mathrm{virt}}_{\lambda,k+1}\le E_{\lambda,k}-D_{\lambda,k},\qquad k\ge k_0,
$$

其中

$$
D_{\lambda,k}=4\lambda s\langle x_k-x^\star,V(x_k)\rangle+4(3-\lambda)(1-\rho)k\lVert\bar x_{k+1}-x_k\rVert^2+\frac{10}{3}(1-\rho)s^2k\lVert V(x_k)\rVert^2+\frac23s(1/\theta-s)k^2\lVert V(x_k)-V(x_{k-1})\rVert^2.
$$

所有项非负。$s=1/\theta$ 时最后一项为零，其余三项仍保留。该不等式只使用当前两个点与下一步的更新关系，因此此前的轨道包含噪声也不影响这一次局部应用。

## 3. 全部新增噪声项

令实际下一步为 $x_{k+1}=\bar x_{k+1}+\eta_k$。在虚拟下一步处记

$$
j=k+1,\qquad r=\bar x_{k+1}-x^\star,\qquad d=j(\bar x_{k+1}-x_k),\qquad w=sj V(x_k).
$$

实际能量的三个变量为 $(r+\eta_k,d+j\eta_k,w)$。直接展开二次型，得到精确恒等式

$$
E_{\lambda,k+1}=E^{\mathrm{virt}}_{\lambda,k+1}+\langle L_{\lambda,k},\eta_k\rangle+Q_{\lambda,k}\lVert\eta_k\rVert^2,
$$

$$
L_{\lambda,k}=4\lambda(j+\alpha-1)r+4(\lambda+j)d+(4\lambda+2C_\alpha j)w,
$$

$$
Q_{\lambda,k}=2\lambda(\alpha-1)+4\lambda j+2j^2.
$$

这一步没有不等式，也没有丢弃噪声项。$Q_{\lambda,k}=\Theta(k^2)$。步长因子通过 $b_k,c_k$ 进入 $\eta_k$。固定 $s$ 且动量尺度 $t_k\asymp k$ 时，二阶代价与 $s^2t_k^2$ 同阶。

### 3.1 复用上一步的随机查询

令 $\widehat T_k(x_k)=T(x_k)+e_k$，并保存该查询值供下一步使用。此时

$$
\eta_k=b_ke_k-c_ke_{k-1}.
$$

新增项完整列为

$$
b_k\langle L_{\lambda,k},e_k\rangle-c_k\langle L_{\lambda,k},e_{k-1}\rangle+Q_{\lambda,k}b_k^2\lVert e_k\rVert^2+Q_{\lambda,k}c_k^2\lVert e_{k-1}\rVert^2-2Q_{\lambda,k}b_kc_k\langle e_k,e_{k-1}\rangle.
$$

若 $\mathbb E[e_k\mid\mathcal F_k]=0$，第一项和最后一项的条件期望为零。第二项保留，因为 $e_{k-1}$ 已属于 $\mathcal F_k$，而 $L_{\lambda,k}$ 还依赖受它影响的 $x_k$。因此，“逐项条件无偏，所以所有线性项消失”不成立。

**待证明。** 以上只是当前能量证明的缺口，不能据此断言 N6 不足。后文的精确线性例子表明，复用查询反而能容许更慢的噪声衰减。

### 3.2 每步重新查询当前点和前一点

在同一步用新的随机样本查询 $T(x_k)+e_k$ 与 $T(x_{k-1})+f_k$。要求两个误差在给定 $\mathcal F_k$ 后均为零均值，并且条件独立。此时

$$
\eta_k=b_ke_k-c_kf_k,\qquad \mathbb E[\eta_k\mid\mathcal F_k]=0.
$$

设 $\mathbb E[\lVert e_k\rVert^2\mid\mathcal F_k]\le v_k$、$\mathbb E[\lVert f_k\rVert^2\mid\mathcal F_k]\le u_k$，其中 $v_k,u_k$ 是确定的非负数。于是

$$
\mathbb E[\lVert\eta_k\rVert^2\mid\mathcal F_k]\le b_k^2v_k+c_k^2u_k=:a_k.
$$

条件独立只用于这个方差和。若改用有相关性的两个新查询，只要组合误差保持条件零均值，并直接给出 $\mathbb E[\lVert\eta_k\rVert^2\mid\mathcal F_k]$ 的上界，证明同样适用。

## 4. 双查询版本在 N6 下的证明

**命题 P1，本次证明。** 在第 1 节的假设下，取 $\alpha=4$，按 3.2 节重新查询两个点。若

$$
\sum_{k\ge1}k^2(v_k+u_k)<\infty,
$$

则在同一无限随机轨道上，几乎必然有

$$
k\lVert V(x_k)\rVert\longrightarrow0,\qquad k\lVert x_k-x_{k-1}\rVert\longrightarrow0,
$$

且 $x_k$ 弱趋于某个取值于 $\operatorname{Fix}T$ 的随机点。有限维时该极限为强极限。另有 $\mathbb E\lVert V(x_k)\rVert^2\le C/(k+1)^2$，其中 $C$ 依赖相对于一个固定解的初始二阶矩、$s,\theta$ 和总加权方差预算，不依赖 $k$。该常数不对所有问题实例统一。

**证明。**

1. **条件能量下降。** 虚拟下一步及 $L_{\lambda,k}$ 均为 $\mathcal F_k$-可测。由精确扰动恒等式和条件零均值，

$$
\mathbb E[E_{\lambda,k+1}\mid\mathcal F_k]\le E_{\lambda,k}-D_{\lambda,k}+Q_{\lambda,k}a_k.
$$

由于 $\sum Q_{\lambda,k}a_k<\infty$，Robbins–Siegmund 引理给出 $E_{\lambda,k}$ 有有限极限，且 $\sum D_{\lambda,k}<\infty$，分别对 $\lambda=2,9/4$ 成立。初始有限步不影响结论。这里的非负性、适应性和可积性分别来自正定能量、查询时序以及初值和每步噪声的二阶矩假设。

2. **实际速度的可和性。** Tonelli 定理和确定的方差预算给出

$$
\mathbb E\sum_k k^2\lVert\eta_k\rVert^2\le\sum_k k^2a_k<\infty.
$$

因此该随机非负级数几乎必然有限。用 $x_{k+1}-x_k=\bar x_{k+1}-x_k+\eta_k$，得到

$$
\sum_k k\lVert x_{k+1}-x_k\rVert^2<\infty,\qquad \sum_k k\lVert V(x_k)\rVert^2<\infty.
$$

能量还控制 $\sup_k\lVert x_k-x^\star\rVert$。

3. **从 big-O 到 little-o。** 定义

$$
p_k=\frac{\alpha-1}{2}\lVert x_k-x^\star\rVert^2+k\langle x_k-x^\star,x_k-x_{k-1}+sV(x_{k-1})\rangle.
$$

恒等式 $E_{\lambda_2,k}-E_{\lambda_1,k}=4(\lambda_2-\lambda_1)p_k$ 说明 $p_k$ 有极限。再令

$$
h_k=E_{\lambda,k}-4\lambda p_k=2\lVert d_k\rVert^2+2C_\alpha\langle d_k,w_k\rangle+C_\alpha\lVert w_k\rVert^2.
$$

$h_k$ 为正定二次型，而且有极限。第 2 步说明 $\sum h_k/k<\infty$。调和级数发散，所以 $\lim h_k=0$。正定性给出 $k\lVert x_k-x_{k-1}\rVert\to0$ 和 $k\lVert V(x_{k-1})\rVert\to0$。移动一个下标即得 P1 的残差结论。

4. **到每个解的距离存在极限。** 第 2–3 步已给出 $r_k$ 有界、$d_k,w_k\to0$，以及 $p_k$ 有极限。由

$$
p_k=\frac{\alpha-1}{2}\lVert r_k\rVert^2+\langle r_k,d_k+w_k\rangle,
$$

第二项趋于零，故 $\lVert x_k-x^\star\rVert^2$ 有极限。这个步骤只使用已经得到的量，不需要额外构造辅助级数。

5. **弱极限。** 先对 $\operatorname{Fix}T$ 的一个可数稠密子集取共同的概率为一事件，再用距离函数的 Lipschitz 性将距离极限扩展到全部解。每个弱聚点由 $\operatorname{Id}-T$ 在零点处的 demiclosedness 属于 $\operatorname{Fix}T$。路径上的 Opial 引理给出唯一弱极限。可分性还保证相应随机极限的可测性。

6. **期望界。** 对第 1 步取全期望并求和，有 $\sup_k\mathbb E E_{\lambda,k}<\infty$。由能量控制 $s^2k^2\lVert V(x_{k-1})\rVert^2$ 得到所述期望平方残差界。该步骤使用总预算可积，不能从仅有路径 N6 自动得到。

证明完毕。P1 对应原任务的结论类型 2、3、4。第 6 节计入批量后才能讨论类型 5。

## 5. 复用查询的保守充分条件

**命题 P2，本次证明。** 对第 3.1 节的原算法，若几乎必然

$$
\sum_k k\lVert e_k\rVert<\infty,
$$

则对 $\alpha=4$ 与第 1 节其余条件，P1 的路径结论成立。这里不要求无偏性。

证明要点：正定二次型平方根为状态空间上的范数。由三角不等式及第 3 节恒等式，

$$
\sqrt{E_{\lambda,k+1}}\le\sqrt{E^{\mathrm{virt}}_{\lambda,k+1}}+\sqrt{Q_{\lambda,k}}\lVert\eta_k\rVert\le\sqrt{E_{\lambda,k}}+\sqrt{Q_{\lambda,k}}\lVert\eta_k\rVert.
$$

假设保证 $\sum k\lVert\eta_k\rVert<\infty$，从而能量有界。由正定性，$\lVert L_{\lambda,k}\rVert\le Ck\sqrt{E_{\lambda,k}}$；虚拟步能量不超过当前能量。于是能量扰动的绝对值可和。结合局部下降，可得两组能量极限及 $\sum D_{\lambda,k}<\infty$。再逐项采用 P1 的第 2–5 步。

若有确定的二阶矩上界 $\mathbb E\lVert e_k\rVert^2\le v_k$，则 $\sum k\sqrt{v_k}<\infty$ 是充分条件。这是加权 RMS 误差的 $\ell^1$ 条件，强于 $\sum k^2v_k<\infty$。

## 6. 查询复用的精确边界例子

本节直接检验将两个随机实现视为等效的判断。取 $H=\mathbb R$、$T=0$、$s=1$、$\alpha=4$，因此残差为 $|x_n|$。本节初值为确定的实数，并且与全部查询噪声独立。下文标准 Gaussian 变量的独立性包括初始误差 $e_0$。

### 6.1 复用查询

更新简化为

$$
x_{k+1}=\frac{k+2}{k+4}x_k+\frac{k+2}{k+4}e_k-\frac{k}{k+4}e_{k-1}.
$$

设 $D_n=(n+2)(n+3)$。逐步乘开并合并同一个误差的系数，得到对 $n\ge2$ 的精确解

$$
x_n=\frac{12x_1-4e_0+2\sum_{j=1}^{n-2}e_j+(n+1)(n+2)e_{n-1}}{D_n}.
$$

合并成立的关键是

$$
(j+2)(j+3)-(j+1)(j+4)=2.
$$

取独立标准 Gaussian 变量 $Z_j$，$e_j=\sigma(j+1)^{-q}Z_j$，$\sigma>0$。对 $q>1$，Gaussian 尾界与 Borel–Cantelli 给出 $n e_{n-1}\to0$ 几乎必然。又因 $\sum\mathbb E e_j^2<\infty$，鞅级数 $\sum e_j$ 几乎必然有有限极限。因此

$$
n|x_n|\longrightarrow0\quad\text{almost surely},\qquad q>1.
$$

当 $0\le q\le1$ 时，$x_n$ 为 Gaussian 变量，且 $n x_n$ 的方差由最后一个独立误差项下界为渐近 $\sigma^2 n^{2-2q}$。$q=1$ 时该下界趋于正数；$q<1$ 时趋于无穷。Gaussian 小区间概率因而排除 $n x_n\to0$ 依概率，继而排除几乎必然极限为零。

**结论 P3，本次证明。** 在这一明确的 Gaussian 一维模型中，复用查询满足几乎必然 $o(1/n)$ 的阈值为 $q>1$。不能把该阈值直接推广到一般非线性 $T$ 或只有二阶矩约束的任意噪声分布。

### 6.2 两个独立的新查询

若将旧误差替换为新的独立 $f_k$，其中 $f_k$ 与 $e_k$ 同分布，则

$$
x_n=\frac{12x_1+\sum_{i=1}^{n-1}(i+2)(i+3)e_i-\sum_{i=1}^{n-1}i(i+3)f_i}{D_n}.
$$

当 $0\le q<5/2$ 时，独立性与幂和渐近式给出

$$
\operatorname{Var}(x_n)\sim\frac{2\sigma^2}{5-2q}n^{1-2q}.
$$

因此 $q\le3/2$ 时，$n x_n$ 的方差不趋于零。Gaussian 小区间概率再次排除依概率趋于零。$q>3/2$ 时 N6 成立，由 P1 得到几乎必然 $o(1/n)$。

**结论 P4，本次证明。** 相同的一维 Gaussian 模型中，双查询版本的阈值为 $q>3/2$。例如 $q=1.2$ 时，原复用版本有目标速率，双查询版本没有目标速率。双查询是证明基准，不能据其条件容易处理就判定它更适合作为研究主线。

这组结论比较相同的单次查询方差；双查询还多用一次查询。将每步总样本数固定只会改变常数，不会改变上述指数区别。

## 7. 不能直接采用快速衰减步长

将原公式中的常数 $s$ 直接替换为 $s_k$，取 $T=0$、$e_k=0$、$x_0=x_1=1$，有

$$
x_{k+1}-x_k=(1-s_k)\frac{k}{k+\alpha}(x_k-x_{k-1})-\frac{\alpha s_k}{2(k+\alpha)}x_k.
$$

设 $0<s_k\le1$，且 $\sum s_k<2(\alpha-1)/\alpha$。在轨道仍为正的任意有限前缀上，$x_k$ 单调递减且不超过 1。对下降量递推并用

$$
\sum_{n=i}^{\infty}\prod_{j=i+1}^n\frac{j}{j+\alpha}=\frac{i+\alpha}{\alpha-1},
$$

可得每个有限前缀的总下降不超过 $\frac{\alpha}{2(\alpha-1)}\sum s_k<1$。因此轨道始终为正，且

$$
x_\infty\ge1-\frac{\alpha}{2(\alpha-1)}\sum_k s_k>0.
$$

取 $\alpha=4$、$s_k=0.1/(k+1)^{1.6}$，用积分上界可得 $x_\infty\ge0.888888\ldots$。实际运行十万步约为 $0.91783745$。这说明 $\delta>3/2$ 仅使某个噪声级数有限，不能保证替换步长后的算法仍能解出无噪声问题。

因此，本次不声称 N2 下存在已求出的“最优 $\delta$”。要优化速率，需要先定义具有有效确定性理论的变步长算法，再核对它的能量关系。$t_k\asymp k^r$ 的 Nesterov 参数关系不能直接代入原 Fast KM。

## 8. 对 AFP 关键引理的最小反例

被检验版本：[Nguyen-Trung–Tran-Dinh，arXiv:2512.13547v1](https://arxiv.org/html/2512.13547v1#S3.SS2)，Lemma 1，式 3、4、5 与 Appendix B.1。该论文 Theorem 2 声明随机 AFP 的几乎必然 little-o 结果。这里区分论文声明与本次已核验的证明。

令 $G\equiv0$、查询误差恒为零、$y^0=z^0=1$，并选择解 $x^\star=0$。AFP 的全部迭代点恒等于 1。满足论文条件的参数取 $s=4$、$\gamma=1/2$、$\eta=1/10$、$t_k=k+13$。注意本节 $s$ 是 AFP 参数，与前文 Fast KM 的步长无关。

论文的步长为 $\eta_k=\eta t_k/[2(t_k-s)]$，随 $k$ 递减。其式 3 的能量在此例简化为

$$
\mathcal L_k=\frac{s^2(s-1)}{2\eta_{k-1}\gamma}.
$$

因此 $\mathcal L_k$ 递增，而式 5 的全部右端项均为零。精确取 $t_{k-1}=13,t_k=14$，有

$$
\mathcal L_k-\mathcal L_{k+1}=\frac{8640}{13}-\frac{4800}{7}=-\frac{1920}{91}<0.
$$

这与式 5 要求的非负性冲突。PDF 原文、arXiv HTML 公式和有理数代入给出相同结果。Appendix B.1 先要求 Young 参数 $c_k>0$，随后选取

$$
c_k=\frac{\eta_k\gamma-\eta_{k-1}\gamma}{\gamma^2\eta_{k-1}\eta_k}<0,
$$

也直接暴露了符号条件不满足。

**已验证的问题：该 v1 中 Lemma 1 的式 5 按印刷形式不成立。** 它处于后续证明链中，因此该版本的证明不能直接作为已通过核查的依据。**本反例没有否定 Theorem 2 的结论**；该结论在 $G=0$ 例中仍成立。加入可和的乘性误差项或调整能量可能修复证明，但本次没有替作者完成修复。

这一问题只作为选题边界证据。报告不把审阅他人论文或修复该文作为研究主课题。

## 9. 批量与证据范围

单样本方差为 $\sigma_0^2$，独立批量大小为 $m_k$ 时，方差不超过 $\sigma_0^2/m_k$。

- P1 的充分条件：$m_k=\lceil c(k+1)^{3+\varepsilon}\rceil$，总查询数为 $\Theta(K^{4+\varepsilon})$，双查询再乘 2。
- 接近边界的充分条件：$m_k=\lceil c(k+1)^3\log^{1+\varepsilon}(k+2)\rceil$，总数为 $\Theta(K^4\log^{1+\varepsilon}K)$。
- P2 的保守条件：$m_k=\lceil c(k+1)^{4+\varepsilon}\rceil$，总数为 $\Theta(K^{5+\varepsilon})$。

这里 $c,\varepsilon>0$ 固定。“$m_k=O(k^p)$”只给上界，不能作为方差足够小的保证。

若使用 P1 的期望残差 $O(1/K)$ 界，再代入批量成本，达到期望残差 $\epsilon$ 的充分查询数为 $\widetilde O(\epsilon^{-4})$，采用幂批量时为 $O(\epsilon^{-4-\varepsilon})$。该结果比固定时域随机 iKM 的近 $\epsilon^{-2}$ 查询复杂度昂贵。无限轨道的路径速率是不同类型的保证。

第 6 节的 Gaussian 阈值不能用于仅假设 N2 的所有噪声。具有稀有大误差的有限方差分布可能需要更强尾部控制。以上没有建立原复用算法在一般 N6 下的结论，也没有建立 N2 下所有快速方法的路径最优速率。

## 10. 可复核数值记录

`km-experiment/check_and_run.py` 验证原能量的展开式和扰动恒等式，最大相对误差分别约 $5.81\times10^{-16}$、$1.32\times10^{-15}$。

`km-experiment/check_reuse_and_afp.py` 验证第 6 节两条精确解。最大绝对误差分别约 $3.66\times10^{-15}$、$7.82\times10^{-14}$。AFP 反例采用有理数运算，能量差精确为 $-1920/91$。

数值运行不用于证明几乎必然速率。第 4–8 节的结论分别依赖能量证明、精确解、Gaussian 尾界和有理数反例。
