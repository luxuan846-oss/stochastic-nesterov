# 0. 问题设定与讨论入口

考虑随机凸优化问题

$$
\min_{x\in\mathcal H} F(x),
\qquad
F(x):=\mathbb E_{\xi}[\ell(x;\xi)],
$$

其中 $F$ 是凸且 $L$-光滑函数，最优解集

$$
S:=\arg\min F\neq\varnothing,
\qquad
F^\star:=\min F.
$$

在第 $t$ 步，随机梯度写成

$$
g_t=\nabla F(x_t)+e_t,
\qquad
x_{t+1}=x_t-s_t g_t,
$$

其中 $s_t>0$，$\mathcal F_t$ 表示第 $t$ 步前已获得的信息，并假设

$$
\mathbb E[e_t\mid\mathcal F_t]=0,
\qquad
\sigma_t^2:=\mathbb E[\|e_t\|^2\mid\mathcal F_t].
$$

**“随机加速”必须同时说明噪声模型、取值点和收敛意义；只比较一个未注明这些条件的 $O(\cdot)$ 不能判断是否真的加速。**

三种噪声体制：

| 噪声体制       | 条件形式                                                                                                            | 典型含义                                                                                  |
| ---------- | --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| **持续加性噪声** | $\mathbb E[e_t\mid\mathcal F_t]=0$，$\sigma_t^2\le\sigma^2$，且 $\sigma_t$ 不趋于 $0$，例如 $\sigma_t^2\asymp\sigma^2>0$ | 最优点附近仍有固定噪声；按样本预算计，噪声项通常为 $\sigma D/\sqrt T$                                          |
| **噪声递减**   | $\sigma_t\to0$；JOTA 的 a.s. 结论要求 $\sum_k s_k t_k\sigma_k<\infty$，基本期望界对应 $\sum_k(s_k t_k\sigma_k)^2<\infty$      | 例如增大 batch 使 $\sigma_t^2=O(1/m_t)$；标准 $t_k\asymp k$ 时需要 $\sum_k k s_k\sigma_k<\infty$ |
| **相对噪声**   | $\mathbb E[e_t\mid\mathcal F_t]=0$，$\mathbb E[\|e_t\|^2\mid\mathcal F_t]\le\nu^2\|\nabla f(x_t)\|^2$            | 噪声随真实梯度一起消失；在最优点满足 $\nabla f(x^\star)=0$ 时，噪声也消失                                      |

持续加性噪声与噪声递减的区别在于 $\sigma_t$ 是否趋于 $0$；相对噪声的关键是方差由当前梯度大小控制。**JOTA 主要处理第二种体制**

区分三种评价指标：

1. **期望函数值速率**，例如 $\mathbb E[f(\widetilde x_T)-f^\star]$ 或 $\mathbb E[f(x_T)-f^\star]$；
2. **几乎处处的末次迭代速率**，例如 $f(x_t)-f^\star=o(t^{-p})$ a.s.；
3. **迭代点收敛**，即有限维中 $x_t\to X\in S$ a.s.，无限维 Hilbert 空间中相应的弱收敛。

# I. 上回的问题

## 1. JOTA 讲了什么

### Summary

- **机制：** 一条能量不等式，噪声通过 $s_k^2t_k^2\sigma_k^2$ 进入；它与 SGD 的偏差--方差结构同构。
- **速率：** 噪声递减时恢复 a.s. $o(1/k^2)$；持续噪声时最好约为 $1/\sqrt{k}$，与 SGD 同阶。
- **迭代点：** 保住加速的体制下得到 a.s. 收敛，但需要 $\ell^1$ 型噪声条件和不降的步长。
- **未回答的问题：** 这些条件是否紧；持续噪声下的迭代点结论；临界 $\alpha=3$。

本文用一条随机 Lyapunov 不等式，统一分析一般外推参数 $\alpha_k$ 下的随机 Nesterov（SNAG）与 Ravine（SRAG）方法。噪声衰减得足够快时，恢复确定性的 $o(1/k^2)$ 与迭代点收敛；噪声持续时，最好速率约为 $1/\sqrt{k}$，与 SGD 同阶。

### 1.1 设定

**算法与噪声：**

$$
y_k=x_k+\alpha_k(x_k-x_{k-1}),
\qquad
x_{k+1}=y_k-s_k\bigl(\nabla f(y_k)+e_k\bigr),
$$

$$
\mathbb E[e_k\mid\mathcal F_k]=0,
\qquad
\mathbb E[\|e_k\|^2\mid\mathcal F_k]\le\sigma_k^2.
$$

- **$t_k$ 统一所有动量：** 令

  $$
  t_k:=1+\sum_{i\ge k}\prod_{j=k}^{i}\alpha_j
  $$

  其中 (K0) 保证级数有限，则

  $$
  \alpha_k=\frac{t_k-1}{t_{k+1}}.
  $$

  对 $\alpha_k=1-\alpha/k$，有 $t_k\asymp k/(\alpha-1)$。

- **分析变量 $z_k$：** 令

  $$
  z_k:=x_{k-1}+t_k(x_k-x_{k-1}),
  $$

  则

  $$
  z_{k+1}=z_k-s_kt_{k+1}\bigl(\nabla f(y_k)+e_k\bigr),
  $$

  $$
  x_k=\Bigl(1-\frac1{t_k}\Bigr)x_{k-1}+\frac1{t_k}z_k,
  \qquad
  y_k=\Bigl(1-\frac1{t_{k+1}}\Bigr)x_k+\frac1{t_{k+1}}z_k.
  $$

  **$z_k$ 是步长为 $s_kt_{k+1}$ 的类 SGD 序列，$x_k$ 是它的在线平均，$y_k$ 是两者的凸组合。**

- **动量条件：** (K1)

  $$
  t_{k+1}^2-t_k^2\le t_{k+1}
  $$

  对应 $\alpha\ge3$；(K1$^+$) 把右端换成 $m\,t_{k+1}$、$m<1$，对应 $\alpha>3$。经典 Nesterov/FISTA 参数恰好是 $\alpha=3$。

- **Ravine：** 外推点 $y_k$ 满足 Ravine 递推，$\gamma_k=\alpha_{k+1}$（Theorem 2.1）。函数值与迭代点结论可以转移到 $y_k$，梯度结论则需在 $y_k$ 上单独证明。

$z_k$ 的递推一行即可验证：$z_k=x_k+(t_k-1)(x_k-x_{k-1})$，且 $t_{k+1}\alpha_k=t_k-1$。代入

$$
z_{k+1}=x_k+t_{k+1}(x_{k+1}-x_k)
$$

### 1.2 点一：一条能量不等式决定全部速率

思路和 SGD 一样：找一个量，每步大致不增，然后从它的有界性读出速率。取常数步长 $s$ 来突出机制，定义能量

$$
V_k=s\,t_k^2\bigl(f(x_k)-f^\star\bigr)
+\frac12\operatorname{dist}(z_k,S)^2.
$$

**含义：** 第一项是加权的函数值误差，权重 $t_k^2\sim k^2$ 就是加速的来源；第二项是驱动序列 $z_k$ 到解集的距离。只要 $V_k$ 有界，就有

$$
f(x_k)-f^\star\le\frac{V_k}{s\,t_k^2},
$$

速率直接由权重给出。接下来看 $V_k$ 一步之后怎么变。

利用

$$
z_{k+1}=z_k-s\,t_{k+1}\bigl(\nabla f(y_k)+e_k\bigr)
$$

展开距离平方，再用凸性与光滑性，得到

$$
\mathbb E[V_{k+1}\mid\mathcal F_k]
\le V_k
-\underbrace{s\bigl(t_{k+1}-t_{k+1}^2+t_k^2\bigr)\bigl(f(x_k)-f^\star\bigr)}_{\text{动量条件控制}}
+\underbrace{C\,s^2t_{k+1}^2\sigma_k^2}_{\text{噪声代价}}.
$$

**含义：** 能量的变化分成三部分。

- 中间项比较两件事：权重从 $t_k^2$ 增长到 $t_{k+1}^2$，以及梯度步带来的下降 $t_{k+1}$。$(K_1)$ 保证下降不少于涨幅，所以这一项非正。
- 噪声项的来源与 SGD 附录 (A.1)--(A.2) 相同：交叉项 $\langle e_k,\cdot\rangle$ 在条件期望下为零，只剩平方项 $s^2t_{k+1}^2\|e_k\|^2$。**噪声只从这里进入。**

这个不等式正好符合 Robbins--Siegmund 引理的形式：若

$$
\mathbb E[a_{k+1}\mid\mathcal F_k]\le a_k-b_k+c_k,
$$

其中 $a_k,b_k,c_k\ge0$ 且 $\sum_k c_k<\infty$，则 $a_k$ a.s. 收敛，且 $\sum_k b_k<\infty$ a.s.。取 $a_k=V_k$、$c_k$ 为噪声项，得到：

- **$O$ 速率。** 若

  $$
  \sum_k s_k^2t_k^2\sigma_k^2<\infty
  \qquad (K_2),
  $$

  则 $V_k$ a.s. 收敛，从而有界，于是

  $$
  f(x_k)-f^\star
  =O\!\left(\frac{1}{s_kt_k^2}\right)
  \quad\text{a.s.}
  $$

- **$o$ 速率。** 若再有 $(K_1^+)$，中间项至少是

  $$
  -(1-m)s\,t_{k+1}\bigl(f(x_k)-f^\star\bigr),
  $$

  这就是 $b_k$。于是

  $$
  \sum_k s_kt_{k+1}\bigl(f(x_k)-f^\star\bigr)<\infty
  \quad\text{a.s.}
  $$

  **含义（直观）：** 若 $t_k^2(f(x_k)-f^\star)$ 趋于某个正数 $c$，则上面的和约为 $c\sum_k1/t_k$；当 $t_k\sim k$ 时该和发散，矛盾。所以 $O$ 可以改进为 $o$。严格证明还需要论文中的附加条件
  $$
  \sum_k\frac{t_{k+1}}{t_k^2}=\infty,
  $$

  对 $t_k\sim k$ 自动成立。

**这一点的结论：** 噪声递减时加速可以保住；持续噪声下随机 Nesterov 与 SGD 同阶。能保住多少加速，取决于 $s_kt_k\sigma_k$ 的可和性。

**与 SGD 的对照。** 对一步不等式取期望并从 $1$ 到 $k$ 求和，中间项非正可以丢掉，得到

$$
s_kt_k^2\,\mathbb E[f(x_k)-f^\star]
\le
\mathbb E V_k
\le
V_1+C\sum_{i\le k}s_i^2t_i^2\sigma_i^2.
$$

两边除以 $s_kt_k^2$：

$$
\mathbb E[f(x_k)-f^\star]
\lesssim
\underbrace{\frac{D^2}{s_kt_k^2}}_{\text{偏差}}
+
\underbrace{\frac{\sum_{i\le k}s_i^2t_i^2\sigma_i^2}{s_kt_k^2}}_{\text{方差}}.
$$

**含义：** 这与 SGD 的式 (9) 同构，只是分母从 $\sum s_t$ 变成 $s_kt_k^2$。加速放大了分母，也用同样的 $t_i^2$ 放大了噪声。

代入 $t_k\sim k$，看两种噪声体制：

| 噪声体制                        | 参数                                   | 偏差             | 方差                           | 结果                                      |
| --------------------------- | ------------------------------------ | -------------- | ---------------------------- | --------------------------------------- |
| 噪声递减                        | $s$ 常数，$\sum_k k^2\sigma_k^2<\infty$ | $1/k^2$        | 分子有界，也是 $1/k^2$              | 加速保住；加 $(K_1^+)$ 得 a.s. $o(1/k^2)$      |
| 持续噪声 $\sigma_k\equiv\sigma$ | 必须 $s_k=c\,k^{-\delta}$              | $k^{\delta-2}$ | $k^{1-\delta}$（$\delta<3/2$） | 平衡于 $\delta=3/2$，期望 $O(\log k/\sqrt k)$ |
|                             |                                      |                |                              |                                         |

持续噪声下，a.s. 分析还要求噪声项可和，即

$$
\sum_k k^{2-2\delta}<\infty,
$$

也就是 $\delta>3/2$。此时速率为 $k^{-(2-\delta)}$，能得到的 a.s. 速率都**比 $k^{-1/2}$ 略慢**，$\varepsilon$ 越小越接近，只能任意接近 $k^{-1/2}$，与 SGD 的噪声主导阶一致。


### 1.3 点二：迭代点 a.s. 收敛（Theorem 3.1(iii)）

点一只回答“函数值多快趋于最优”，没有回答“点列是否停在某个极小点”。(i)--(ii) 给出的是

$$
f(x_k)\to f^\star,
\qquad
\|x_k-x_{k-1}\|\to0.
$$

**为什么不够：** 当 $S$ 不是单点时，点列可以沿着 $S$ 附近以越来越小的步子来回漂移。例如每步走 $1/k$，相邻差趋于零，但总路程发散，序列仍然可能不停下来。

排除这种漂移的标准工具是 Opial 引理。它要求两件事：

1. 对每个 $x\in S$，$\lim_k\|x_k-x\|$ 存在；
2. 每个聚点都属于 $S$。

**含义：** 第 1 条说点列到每个解的距离最终稳定，因此不能到处漂移；第 2 条说它只能停在解上。两者合起来，聚点只能有一个。

四个条件分别服务于这两条：

| 条件 | 服务于 | 作用 |
|---|---|---|
| $\inf_k s_k>0$ | 第 2 条 | 把 $\sum s_kt_{k+1}(f-f^\star)<\infty$ 变成 $f(x_k)\to f^\star$，从而聚点是解 |
| $(K_1^+)$ | 两条 | 提供可和性和 $\sum_k t_k\|x_k-x_{k-1}\|^2<\infty$ |
| $\alpha_k\in[0,1]$ | 第 1 条 | 建立距离平方 $h_k=\tfrac12\|x_k-x\|^2$ 的准 Fejér 不等式 |
| $(K_2^+)$：$\sum_k s_kt_k\sigma_k<\infty$ | 第 1 条 | 控制该不等式中的噪声 |

**为什么这里要 $\ell^1$，而点一只要 $\ell^2$：** 带动量时，$h_k$ 不单调，动量可能让距离暂时变大。标准做法是证明增量的正部

$$
\sum_k(h_{k+1}-h_k)_+<\infty.
$$

先取正部再取期望，零均值的交叉项就不能再抵消，只能用 Cauchy--Schwarz 界成一次方的 $s_kt_k\sigma_k$。所以 $\ell^1$ 来自证明手法，是否必要仍是开放问题。

**量词问题：** 对每个 $x\in S$，第 1 条成立在一个概率为 1 的事件 $\Omega_x$ 上。但 $S$ 通常不可数，不可数个概率 1 事件的交不一定概率为 1。本文取 $S$ 的可数稠密子集，在其上取交，再用逼近推广到整个 $S$，修复了 [28]、[41] 中的这一处。

**与前人的关系：**

| 工作 | 动量 | 步长 / 噪声 | 迭代点结论 |
|---|---|---|---|
| Sebbouh--Gower--Defazio 2021 | SHB，动量由步长决定 | $\eta_k\sim k^{-1/2-\delta}$，持续噪声 | 有限维 a.s. 收敛，速率与 SGD 同级 |
| Liu--Yuan 2022 | SHB、SNAG，常数动量 | $s_k\sim k^{-2/3-\delta}$，持续噪声 | 有限维 a.s. 收敛 |
| 本文 | 一般 $\alpha_k$，含 $\alpha_k\to1$ | $\inf s_k>0$，噪声递减 | 保留加速速率的 a.s. 收敛；无限维为弱收敛 |

在有限维中，结论就是存在随机极小点 $X(\omega)\in S$，使

$$
\|x_k-X(\omega)\|\to0
\quad\text{a.s.}
$$

**这一点的结论：** 本文的新意在于噪声递减、保住加速的体制下得到迭代点收敛。持续噪声下，$\inf s_k>0$ 与 $\sum_k s_kt_k\sigma_k<\infty$ 不能同时成立，这一格仍然空着。

### 1.4 其余结果（一段话）

Theorem 3.2 把函数值速率和迭代点收敛转移到 Ravine 序列 $y_k$。Theorem 3.3 在常数步长下给出

$$
\sum_k t_{k+1}^2\|\nabla f(y_k)\|^2<\infty
\quad\text{a.s.},
$$

这是 Ravine 侧独有的梯度结果，需要直接在 $y_k$ 上证明。Corollary 4.1--4.3 把一般结论代入 $1-\alpha/k$、$1-\alpha/k^r$ 和常数动量三族参数。Appendix B 用含 Hessian 阻尼项的高分辨率 ODE 解释梯度的快速收敛。


## 2. 基础凸随机

### 2.1 问题、算法与假设

考虑无约束凸优化问题

$$
\min_x f(x),
$$

其中 $f$ 是凸且 $L$-光滑函数，$x^\star\in\arg\min f$，并记

$$
f^\star:=f(x^\star),
\qquad
\Delta_t:=f(x_t)-f^\star\ge0.
$$

随机梯度更新为

$$
x_{t+1}=x_t-s_t\bigl(\nabla f(x_t)+e_t\bigr),
$$

其中 $s_t>0$ 是第 $t$ 次迭代的步长，$\mathcal F_t$ 表示第 $t$ 步之前获得的信息。

有界方差假设

$$
\mathbb E_t[\cdot]:=\mathbb E[\cdot\mid\mathcal F_t],
\qquad
\mathbb E_t[e_t]=0,
\qquad
\mathbb E_t\|e_t\|^2\le \sigma^2.
$$

这里 $\sigma^2$ 是条件方差的统一上界。

### 2.2 主不等式

当 $s_t\le1/(4L)$ 时，

$$
\boxed{
\mathbb E_t\|x_{t+1}-x^\star\|^2
+s_t\bigl(f(x_t)-f^\star\bigr)
\le
\|x_t-x^\star\|^2+2s_t^2\sigma^2.
}
\tag{SGD}
$$

该式控制“下一步到最优解的距离”和“当前函数值误差”；右侧的 $2s_t^2\sigma^2$ 是本步噪声代价。完整推导见附录 A。

### 2.3 加权平均点的基本界（遍历平均）
$$
\mathbb E[f(\widetilde x_T)-f^\star]
=O\left(\frac{LD^2}{T}+\frac{\sigma D}{\sqrt T}\right).
\tag{11}
$$
**结论先行：** 在第 2.1 节的假设及 $s_t\le1/(4L)$ 下，定义

$$
S_k:=\sum_{t=0}^{k-1}s_t,
\qquad
\widetilde x_k:=\frac{1}{S_k}\sum_{t=0}^{k-1}s_t x_t,
\qquad
D:=\|x_0-x^\star\|.
$$

则步长加权平均点满足

$$
\boxed{
\mathbb E[f(\widetilde x_k)-f^\star]
\le
\underbrace{\frac{D^2}{S_k}}_{\text{偏差项}}
+
\underbrace{\frac{2\sigma^2\sum_{t=0}^{k-1}s_t^2}{S_k}}_{\text{方差项}}.
}
\tag{9}
$$

这条界的取值点是 $\widetilde x_k$，度量是期望意义下的函数值间隙 $\mathbb E[f(\widetilde x_k)-f^\star]$。它将初始点造成的优化误差与随机噪声的累计代价明确分开；是否出现加速，取决于 $S_k$ 与 $\sum_t s_t^2$ 的具体阶数。
这里平均的是 $x_0,\ldots,x_{k-1}$，权重为各步长 $s_t$。对主不等式 (SGD) 从 $t=0$ 到 $k-1$ 求和，得到

$$
\sum_{t=0}^{k-1}s_t\,\mathbb E[f(x_t)-f^\star]
\le
D^2+2\sigma^2\sum_{t=0}^{k-1}s_t^2.
$$

再由凸性和 Jensen 不等式，

$$
f(\widetilde x_k)
\le
\frac{1}{S_k}\sum_{t=0}^{k-1}s_t f(x_t),
$$

取期望并结合上式，即得 (9)。因此，这里得到的是**非渐近的期望函数值界**，不是末次迭代 $x_k$ 的界，也不是点列距离或几乎处处速度。

该推导属于随机逼近与 SGD 的标准分析框架，可参见 Nemirovski–Juditsky–Lan–Shapiro（2009）的随机 oracle 分析，以及 Bottou–Curtis–Nocedal（2018）的随机梯度综述。Sebbouh–Gower–Defazio（COLT 2021）也使用同类的望远镜求和与加权平均分析；具体常数由本节采用的一步不等式 (SGD) 决定。


### 2.4 常数步长与已知总时长
若步长为常数 $s_t=s\le1/(4L)$，则

$$
\mathbb E[f(\widetilde x_k)-f^\star]
\le \frac{D^2}{sk}+2s\sigma^2.
\tag{10}
$$

若总运行长度 $T$ 已知，取

$$
s\asymp\min\left\{\frac1L,\frac{D}{\sigma\sqrt T}\right\}
$$

可得标准量级

$$
\mathbb E[f(\widetilde x_T)-f^\star]
=O\left(\frac{LD^2}{T}+\frac{\sigma D}{\sqrt T}\right).
$$

平方根来自平衡 $D^2/(sT)$ 和 $s\sigma^2$。

### 2.5 不依赖最终时长的步长

取 $s_t\asymp t^{-p}$，由 (9) 可得到：

| 步长 | 加权平均点上的期望速率 | 解释 |
|---|---|---|
| $p<1/2$ | $O(k^{-p})$ | 方差累积项主导 |
| $p=1/2$ | $O(\log k/\sqrt{k})$ | 临界步长 |
| $1/2<p<1$ | $O(k^{-(1-p)})$ | $\sum_t s_t^2<\infty$，但指数小于 $1/2$ |

其中 $p>1/2$ 的区域同时满足 Robbins--Monro 条件中的平方可和要求。

### 2.6 期望速率与下界

在固定总样本预算 $T$ 的凸光滑随机一阶 oracle 模型下，SGD 的遍历平均点有上界

$$
O\left(\frac{LD^2}{T}+\frac{\sigma D}{\sqrt T}\right),
$$

而经典随机加速方法可以把偏差项改进为 $LD^2/T^2$，得到上界

$$
O\left(\frac{LD^2}{T^2}+\frac{\sigma D}{\sqrt T}\right).
$$

在相应的 minimax oracle 模型中，下界为

$$
\Omega\left(\frac{LD^2}{T^2}+\frac{\sigma D}{\sqrt T}\right).
$$

因此，持续有界方差下，加速主要改善偏差项；噪声主导阶仍被 $\sigma D/\sqrt T$ 锁定。比较时必须固定函数类、随机 oracle、评价指标和总样本预算；$O(\cdot)$ 是上界，不能直接写成下界。

### 2.7 几乎处处收敛的入口

若步长满足

$$
\sum_t s_t=\infty,
\qquad
\sum_t s_t^2<\infty,
$$

则主不等式 (SGD) 中的噪声误差可和。结合 Robbins--Siegmund 引理，可以得到距离平方收敛，并有

$$
\sum_t s_t\bigl(f(x_t)-f^\star\bigr)<\infty
\quad\text{a.s.}
$$

进一步，在附加的轨道有界性和解集条件下，可推出

$$
f(x_t)\to f^\star
\quad\text{a.s.}
$$

以及有限维中的迭代点收敛，或 Hilbert 空间中的弱收敛。这里要区分：平方可和性是 a.s. 论证的入口，但它本身不自动给出最后迭代点的点态速率。

**推导链：** 条件无偏性消掉交叉项；凸性给出函数间隙；光滑性控制梯度平方；一步界望远镜求和后给出加权平均的期望速率；平方可和步长进入 Robbins--Siegmund 的几乎处处分析。

## 3. 随机加速的四条子线

随机加速必须同时固定噪声模型、取值点、收敛意义和总样本预算。a.s. 结果还要区分速率和单纯的函数值收敛：

$$
f(x_k)-f^\star=O(r_k)
\quad\text{a.s.}
$$

表示存在随机常数的速率，而

$$
f(x_k)\to f^\star
\quad\text{a.s.}
$$

只有收敛性，不能直接写成 a.s. $O$ 或 a.s. $o$ 速率。

目前可以分成五条子线：

| 子线 | 噪声体制 | 主要对象 | 已知结果 | 代表工作 |
|---|---|---|---|---|
| **期望复杂度** | 持续加性噪声 | 遍历点或末次点的函数值 | 加速方法可达到 $\displaystyle O\!\left(\frac{LD^2}{T^2}+\frac{\sigma D}{\sqrt T}\right)$；两项都有匹配下界 $\displaystyle \Omega\!\left(\frac{LD^2}{T^2}+\frac{\sigma D}{\sqrt T}\right)$ | Lan 2012；Nemirovski--Yudin 1983；Agarwal et al. 2012 |
| **动量的 a.s. 理论** | 持续加性噪声 | SHB、常数动量 SNAG 的末次点 | Sebbouh et al. [41]：SHB，动量由步长决定，约为 $1-(3-4\varepsilon)/k$，末次点为 $o(k^{-1/2+\varepsilon})$ a.s.；Liu--Yuan [28]：SHB、SNAG，常数动量，给出 $O(k^{-1/3+\varepsilon})$ a.s. | Sebbouh--Gower--Defazio 2021；Liu--Yuan 2022 |
| **相对噪声下的加速** | $\displaystyle \mathbb E[\|e_k\|^2\mid\mathcal F_k]\le\nu^2\|\nabla f(y_k)\|^2$ | SNAG 及其修正版的函数值、a.s. 速率和迭代点 | Vaswani et al.、Gupta et al. 给出期望加速；Yu--Chen--Feng 的 SHANG/SHANG++ 给出修正版方法的期望 $O(1/k^2)$ 与函数值 a.s. 收敛，但这些 a.s. 结论和具体速率仍需读原文核实 | Vaswani--Bach--Schmidt 2019；Gupta--Siegel--Wojtowytsch 2024；Yu et al. 2026 |
| **噪声递减与不精确加速** | $\sigma_k\to0$ | 一般 $\alpha_k$ 的 SNAG/SRAG | JOTA 在 $(K_2)$ 下给出 a.s. $O(1/(s_kt_k^2))$；$(K_1^+)$、$(K_2)$ 和 $\sum_k t_{k+1}/t_k^2=\infty$ 给出函数值 a.s. $o(1/(s_kt_k^2))$；$(K_2^+)$ 与 $\inf_k s_k>0$ 是迭代点收敛所需条件，Theorem 3.2 对 $y_k$ 的结论使用 $(K_2^+)$ | JOTA 2026；Salzo 2025 |
| **连续时间随机动力学** | 随机惯性 SDE，可含消失黏性和 Hessian 阻尼 | 连续时间能量、时间尺度变换和平均 | 用随机动力系统解释离散随机加速，是 Boţ 所在动力系统方向的连续时间支线 | Maulen-Soto--Fadili--Attouch--Ochs 2025/2026 |

相对噪声行的条件写在 $y_k$ 上，因为 SNAG 在 $y_k$ 处计算随机梯度。Vaswani 等人的条件是随机梯度二阶矩的强增长形式，与方差形式只在常数和展开方式上对应，不能直接写成完全相同的假设。

Liu--Belkin 的负结果需要同时放入这条线：在线性/插值设定下，标准 Nesterov SGD 一般不能保证加速，甚至可能发散。因此剩余问题必须限定为“在什么噪声比例和参数修正下，原始 SNAG 才能恢复 a.s. 加速”，而不能直接假定原始 SNAG 在所有相对噪声下都有效。

SHANG/SHANG++ 由 Hessian-driven Nesterov flow 离散得到；JOTA 的高分辨率 Ravine ODE 同样含 Hessian-driven damping。**推断：**相对噪声下的稳健加速可能依赖这一阻尼项，Ravine 侧的梯度可和分析可能是自然切入口。

## 4. JOTA 在地图上的位置与剩余问题

JOTA 位于

$$
\text{一般 }\alpha_k
\;\times\;
\text{噪声递减}
\;\times\;
\text{SNAG/SRAG}
$$

这一格。它的增量来自参数和算法范围：前人多研究常数动量或由步长决定的动量，JOTA 允许一般 $\alpha_k$；前人主要处理持续噪声下的递减步长，JOTA 在噪声递减时允许不降步长并恢复加速速率；JOTA 还利用 Theorem 2.1 把 SNAG 结果转移到 SRAG。持续噪声下，JOTA 与 [41] 处在同一噪声体制，速率主导阶也相同，JOTA 的区别在算法与参数范围。

| 方向 | 已有结果 | JOTA 是否覆盖 | 仍缺什么 |
|---|---|---|---|
| $\alpha=3$、噪声递减 | JOTA Theorem 3.1(i) 给出 a.s. $O(1/k^2)$；Salzo 2025 在 FISTA、不精确/随机梯度下推进了迭代点 a.s. 弱收敛，具体条件待核 | 部分覆盖 | JOTA 没有给出 a.s. $o(1/k^2)$；Salzo 是否覆盖同一 SNAG 随机模型需核对 |
| $\alpha>3$、噪声递减 | JOTA 给出 a.s. $o(1/k^2)$、梯度可和与迭代点收敛 | 已覆盖 | 主要剩下条件解释和与其他噪声模型的衔接 |
| $\alpha\ge3$、持续噪声 | 期望速率接近 $k^{-1/2}$；JOTA 在递减步长下还可给 a.s. $O$ 或更强条件下的近似 $o$ 速率 | 函数值速率部分覆盖 | SNAG/SRAG 的迭代点收敛仍缺；SHB 已有相关结果 |
| $\alpha\ge3$、相对噪声 | Vaswani、Gupta 等已有期望结果；SHANG/SHANG++ 的函数值 a.s. 结论待核实 | JOTA 未覆盖 | 原始 SNAG/一般 $\alpha_k$ 的 a.s. $O/o$ 速率、迭代点收敛和临界参数依赖 |

因此，汇报中保留三个剩余问题：

1. **相对噪声下的 a.s. 理论。** 具体命题是：对
   \[
   \alpha_k=1-\frac{\alpha}{k},
   \qquad
   \mathbb E[\|e_k\|^2\mid\mathcal F_k]
   \le\nu^2\|\nabla f(y_k)\|^2,
   \]
   在 $\nu<\nu_0(\alpha)$ 和常数步长下，是否有
   \[
   f(x_k)-f^\star=o(1/k^2)
   \quad\text{a.s.}
   \]
   以及迭代点收敛？$\nu_0$ 如何依赖 $\alpha$，临界 $\alpha=3$ 又如何？

2. **持续噪声下的 SNAG/SRAG 迭代点收敛。** 速率已经受噪声下界限制，但迭代点收敛仍是独立问题；SHB 的已有结果可以作为比较对象。

3. **噪声递减、临界 $\alpha=3$ 下的 a.s. $o$ 速率。** JOTA 的 $(K_1^+)$ 余量在临界点消失，Salzo 的结果需要核对是否覆盖同一随机模型。

$\alpha<3$ 的确定性慢速率和“噪声条件是否紧”放在备用材料中，不作为本次汇报的主问题。

# 附录 A. 一步主不等式的完整推导

由随机梯度更新

$$
x_{t+1}=x_t-s_t\bigl(\nabla f(x_t)+e_t\bigr)
$$

展开距离平方：

$$
\begin{aligned}
\|x_{t+1}-x^\star\|^2
={}&\|x_t-x^\star\|^2
-2s_t\langle\nabla f(x_t),x_t-x^\star\rangle
-2s_t\langle e_t,x_t-x^\star\rangle\\
&+s_t^2\|\nabla f(x_t)+e_t\|^2.
\end{aligned}
\tag{A.1}
$$

取条件期望。由 $\mathbb E_t[e_t]=0$，线性交叉项消失：

$$
\begin{aligned}
\mathbb E_t\|x_{t+1}-x^\star\|^2
={}&\|x_t-x^\star\|^2
-2s_t\langle\nabla f(x_t),x_t-x^\star\rangle\\
&+s_t^2\mathbb E_t\|\nabla f(x_t)+e_t\|^2.
\end{aligned}
\tag{A.2}
$$

由凸性，

$$
\langle\nabla f(x_t),x_t-x^\star\rangle
\ge f(x_t)-f^\star
=\Delta_t.
\tag{A.3}
$$

由凸性和 $L$-光滑性，

$$
\|\nabla f(x_t)\|^2\le2L\Delta_t.
\tag{A.4}
$$

条件无偏性还给出

$$
\begin{aligned}
\mathbb E_t\|\nabla f(x_t)+e_t\|^2
&=\|\nabla f(x_t)\|^2+\mathbb E_t\|e_t\|^2\\
&\le2L\Delta_t+\sigma^2.
\end{aligned}
\tag{A.5}
$$

将 (A.3)--(A.5) 代入 (A.2)，得到

$$
\begin{aligned}
\mathbb E_t\|x_{t+1}-x^\star\|^2
&\le\|x_t-x^\star\|^2
-2s_t\Delta_t+s_t^2(2L\Delta_t+\sigma^2)\\
&=\|x_t-x^\star\|^2
-s_t(2-2Ls_t)\Delta_t+s_t^2\sigma^2.
\end{aligned}
\tag{A.6}
$$

当 $s_t\le1/(2L)$ 时，$2-2Ls_t\ge1$，因此有更紧的形式

$$
\mathbb E_t\|x_{t+1}-x^\star\|^2
+s_t\bigl(f(x_t)-f^\star\bigr)
\le
\|x_t-x^\star\|^2+s_t^2\sigma^2.
\tag{A.7}
$$

正文采用的稍松形式

$$
\mathbb E_t\|x_{t+1}-x^\star\|^2
+s_t\bigl(f(x_t)-f^\star\bigr)
\le
\|x_t-x^\star\|^2+2s_t^2\sigma^2
$$

可由 (A.7) 直接推出；也可使用
$\|a+b\|^2\le2\|a\|^2+2\|b\|^2$
并取 $s_t\le1/(4L)$ 得到。


# 参考文献

- Lan, G.: An optimal method for stochastic composite optimization. *Mathematical Programming*, 133(1), 365--397, 2012.
- Cutkosky, A.: Anytime online-to-batch, optimism and acceleration. *ICML*, PMLR 97, 1446--1454, 2019.
- Nemirovski, A. S., Yudin, D. B.: *Problem Complexity and Method Efficiency in Optimization*. Wiley, 1983.
- Agarwal, A., Bartlett, P. L., Ravikumar, P., Wainwright, M. J.: Information-theoretic lower bounds on the oracle complexity of stochastic convex optimization. *IEEE Transactions on Information Theory*, 58(5), 3235--3249, 2012.
- Sebbouh, O., Gower, R. M., Defazio, A.: Almost sure convergence rates for stochastic gradient descent and stochastic heavy ball. *COLT*, PMLR 134, 3935--3971, 2021.
- Liu, J., Yuan, Y.: On almost sure convergence rates of stochastic gradient methods. *COLT*, PMLR 178, 2963--2983, 2022.
- Vaswani, S., Bach, F., Schmidt, M.: Fast and faster convergence of SGD for over-parameterized models and an accelerated perceptron. *AISTATS*, PMLR 89, 1195--1204, 2019.
- Liu, C., Belkin, M.: Accelerating SGD with momentum for over-parameterized learning. *ICLR*, 2020. arXiv:1810.13395.
- Kidambi, R., Netrapalli, P., Jain, P., Kakade, S.: On the insufficiency of existing momentum schemes for stochastic optimization. *ICLR*, 2018. The publication venue should be checked against the JOTA citation.
- Gupta, K., Siegel, J. W., Wojtowytsch, S.: Nesterov acceleration despite very noisy gradients. *NeurIPS*, 2024. arXiv:2302.05515.
- Yu, Y., Chen, L., Feng, M.: SHANG++: Robust stochastic acceleration under multiplicative noise. arXiv:2603.09355, 2026.
- Attouch, H., Fadili, J., Kungurtsev, V.: The stochastic Ravine accelerated gradient method with general extrapolation coefficients. *Journal of Optimization Theory and Applications*, 209:5, 2026.
- Salzo, S.: The iterates of FISTA converge even under inexact computations and stochastic gradients. arXiv:2511.12665, 2025.
- Maulen-Soto, R., Fadili, J., Attouch, H., Ochs, P.: Stochastic inertial dynamics via time scaling and averaging. *Stochastic Systems*, 16(1), 2026.
- Maulen-Soto, R., Fadili, J., Attouch, H., Ochs, P.: An SDE perspective on stochastic inertial gradient dynamics with time-dependent viscosity and Hessian-driven damping. *Optimization*, 2025.
- Attouch, H., Cabot, A., Chbani, Z., Riahi, H.: Inertial forward-backward algorithms with perturbations: application to Tikhonov regularization. *Journal of Optimization Theory and Applications*, 179(1), 1--36, 2018.
- Robbins, H., Siegmund, D.: A convergence theorem for nonnegative supermartingales and some applications. In *Optimizing Methods in Statistics*, 233--257, 1971.

