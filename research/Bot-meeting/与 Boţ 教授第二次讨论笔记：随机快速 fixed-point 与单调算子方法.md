# 与 Boţ 教授第二次讨论笔记：随机快速 fixed-point 与单调算子方法

Oct 10, 2026 · @Yuan

## 1. 讨论背景与任务

核心结论：Boţ 希望把确定性的快速 fixed-point / 单调算子方法推广到随机场景，研究**无限轨道上末次迭代的 almost-sure（几乎必然）收敛**。第一步是随机 Fast KM，第二步是随机 Fast OGDA。

本笔记中，“任务”一节来自我对讨论内容的转述，其余部分是会后的整理与分析。凡属推断的内容均已标注。

### 1.1 Boţ 布置的五项任务

1. **噪声假设。** 他偏好 N2（统一有界方差）和 N6（带权噪声可和），认为 N4/N5（ABC 条件、相对噪声）不够有趣。我需要弄清 ABC 的来源和局限，判断 N2 与 N6 的强弱关系，并说明“有界方差”是否等于“小噪声”。
2. **文献定位。** 精读 Zotero 中 fixed-point 一栏的四篇论文：随机 iKM（Xiao 等）、Fast KM、Fast OGDA、G-EAG（Fast EG）。要准确说明每篇的问题、算法、结论和收敛类型。
3. **单调性。** 理解 monotone operator 的定义和层次。Boţ 认为 Vx = 0 是一个好的、也很热门的问题。
4. **主线。** 先做特例，即随机 Fast KM 的 almost-sure 收敛；再推广到一般的随机 Fast OGDA，他对后者的随机收敛速度尤其感兴趣。
5. **动机。** 说明 proximal gradient、Douglas–Rachford、PDHG 以及 min f(x) + g(Ax) 的 KKT 系统如何写成单调算子问题。

隐含任务：确定 benchmark，并划清 gap 的边界。

## 2. 噪声假设：结论

结论：N2 与 N6 控制的对象不同，二者之间没有无条件的强弱关系。N2 不是“小噪声”。Boţ 不偏好 ABC 是有道理的。

随机误差统一写成以下形式，其中 z\_k 是计算 oracle 的点，F\_k 表示第 k 步之前已知的信息。

```latex
g_k = \nabla f(z_k) + e_k, \qquad \mathbb E[e_k \mid \mathcal F_k] = 0
```

| 条件 | 内容 | 要点 |
| --- | --- | --- |
| N2 | 条件方差有统一上界 σ² | 允许噪声持续存在，不要求 σ 小 |
| N4（ABC） | 二阶矩 ≤ A·函数值差 + B·梯度范数² + C | 二阶矩可随状态变化，常见于有限和问题 |
| N5 | 方差 ≤ ν²·梯度范数² | 噪声随梯度一起消失，需要 interpolation 一类的结构 |
| N6 | Σ s\_k² t\_k² σ\_k² < ∞ | 控制经步长和动量放大后的累积噪声 |

### 2.1 四条要点

1. **N2 ≠ 小噪声。** 强凸二次函数加上固定方差的高斯噪声满足 N2。但在固定步长下，迭代只会停留在一个稳态误差上，不能精确收敛。问题出在“固定步长 + 不消失的噪声”，而不是 N2 本身。
2. **N2 与 N6 的强弱取决于 s\_k 和 t\_k。** 若步长为常数且 t\_k ≍ k，则 N6 要求 Σ k² σ\_k² < ∞，远强于 N2。若 s\_k ≍ k^(−δ) 且 δ > 3/2，则 N2 可以推出 N6。
3. **ABC 的来源与过参数化无关。** 它主要来自有限和结构以及各分量的光滑性。过参数化（例如 LLM）最多可能带来 interpolation，不能自动推出 ABC 或 N5。
4. **Boţ 的偏好有道理。** 一般单调算子 Vx = 0 没有函数值差这一项，ABC 无法直接表述。而 N2/N6 直接对应 Lyapunov 不等式中噪声项的累积。

细节和例子见附录 A。

## 3. fixed-point 文献定位

结论：Fast KM 和 Fast OGDA 本身就有确定性的末次迭代结果；随机 iKM 只给出有限时域的复杂度。因此，卖点只能落在“随机 + 无限轨道 + almost-sure + 快速率”这一组合上。

| 方法 | 问题与假设 | 速率 | 收敛类型 |
| --- | --- | --- | --- |
| 随机 iKM（Xiao 等） | x = Tx，T 非扩张；单次随机 oracle；参数依赖预设的 K | (E‖x\_K − Tx\_K‖²)^(1/2) = O(1/K + σ log K/√K + B\_K log K/K) | 有限时域的期望界，不直接给出无限轨道的 a.s. 收敛 |
| Fast KM | x = Tx，T averaged | ‖x\_k − Tx\_k‖ = o(1/k)，末次迭代 | 迭代点弱收敛 |
| Fast OGDA | Vx = 0，V 单调、Lipschitz | ‖V(z\_k)‖ = o(1/k)，末次迭代 | 迭代点弱收敛 |
| G-EAG（Fast EG） | Mx = 0，M 单调、Lipschitz | ‖M(x\_k)‖ = O(1/k) | 强收敛到 anchor 在解集上的投影 |

### 3.1 需要纠正的几处表述

1. 第一个问题应写成 (Id − T)x = 0，不是 (Id − I)x = 0。
2. 不能把卖点写成“他们只有平均点，我们有 last iterate”。只给平均点结果的是 PDHG 一类的部分理论，Fast KM 和 Fast OGDA 本身就是末次迭代结果。
3. G-EAG 不使用显式的 Nesterov momentum。它的快速性来自 extragradient 与 Tikhonov anchoring 的组合。它处理的是单调 Lipschitz 算子，而不是一般的极大单调算子；得到的是强收敛和 O(1/k)，而不是弱收敛和 o(1/k)。
4. Fast KM 是 Fast OGDA 问题类中的特例：取 V = Id − T，则 V 是 cocoercive 的（见附录 B）。

### 3.2 “随机 fixed-point”的定义

最基本的模型是：真实算子 T 固定不变，算法只能看到带噪声的版本。

```latex
\widehat T_k(z_k) = T(z_k) + e_k, \qquad \mathbb E[e_k \mid \mathcal F_k] = 0
```

如果从随机算子族 T(x) = E\_ξ\[T\_ξ(x)\] 出发，需要区分两个目标：平均算子的 fixed point，即 x\* = E\[T\_ξ(x\*)\]；以及共同 fixed point，即 T\_ξ(x\*) = x\* a.s.。后者的要求更强。

## 4. 研究主线与候选 gap

主问题：在 N2 或 N6 下，随机 Fast KM 的末次残差能否达到 almost-sure 速率，迭代点能否 almost-sure 收敛。之后把同样的问题推广到随机 Fast OGDA。

### 4.1 已有结果（需逐条核实原文）

1. 随机 iKM：有限时域、末次残差、样本复杂度。
2. 随机 KM：在较弱的方差条件下，迭代点 a.s. 弱收敛。
3. 随机 KM：在加权误差可和的条件下，末次残差具有 a.s. 速率。

因此，以下几种说法都不能用：“随机 fixed-point 还没有人研究”“随机 last-iterate 还没有结果”“我们第一次把 fixed-point 随机化”。

### 4.2 候选 gap（推断）

对随机 Fast KM 或随机 Fast OGDA 的**同一条无限随机轨道**，同时证明以下三点：

```latex
\|V(z_k)\| = o(1/k) \ \text{a.s.}, \qquad z_k \rightharpoonup z^\star \ \text{a.s.}
```

- 末次残差几乎必然快速衰减；
- 迭代点几乎必然弱收敛；
- 按总 oracle 调用次数给出样本复杂度。只报告迭代次数不足以支撑“随机加速”的说法。

以下五类结论不能互相替代：有限时域的 O(1/K)、期望界 E‖V(z\_K)‖、‖V(z\_k)‖ → 0 a.s.、迭代点收敛，以及总 oracle 次数。

### 4.3 一个可能的关键难点（推断）

若想让 N2 推出 N6，需要 s\_k ≍ k^(−δ) 且 δ > 3/2。但步长衰减得这么快，很可能会破坏确定性情形下的 o(1/k) 速率。也就是说，“在 N2 下保住 o(1/k) a.s.”与“满足 N6”之间可能存在本质冲突。这一点应直接向 Boţ 确认。

## 5. 下一步与待问 Boţ 的问题

下一步的重点是逐行拆解 Fast KM 的证明，找出噪声在能量不等式中出现的位置及其权重。

### 5.1 阅读顺序

- [ ] Fast KM 原文：Lyapunov 函数、参数选择、o(1/k) 与弱收敛的证明结构；标出噪声项以及它前面的系数
- [ ] 已有的随机 KM / 随机 iKM 原文：它们覆盖了哪些参数区间、哪些收敛类型
- [ ] Fast OGDA：相比 Fast KM 多处理了什么（单调 + Lipschitz，而非 cocoercive）
- [ ] 单调算子的层次关系，以及 PGD / DR / PDHG 的 fixed-point 表述（附录 B、C）
- [ ] G-EAG：作为“无显式动量的加速”对照来读

### 5.2 核对清单

1. 随机算法的参数是否 horizon-free，即不依赖预设的 K。
2. 噪声是否条件无偏。
3. 能量不等式中的噪声项需要 ℓ¹ 可和还是 ℓ² 可和。
4. 已有的随机 KM / iKM 是否已经覆盖目标参数区间。
5. 最终比较是否按 oracle 调用次数，而不仅仅按迭代次数。

### 5.3 下次讨论想问 Boţ 的问题

1. 随机 Fast KM 中，步长 s\_k 是保持常数，还是允许衰减？
2. 若在 N2 下必须让步长衰减，o(1/k) 是否还有希望保住，还是目标改为“N6 下的 o(1/k) a.s.”？
3. 目标是平均算子的 fixed point，还是共同 fixed point？

## 附录 A：噪声条件细节与例子

### A.1 四个条件的公式

N2，统一有界方差：

```latex
\mathbb E[\|e_k\|^2 \mid \mathcal F_k] \le \sigma^2
```

N4，ABC 条件（沿轨道的条件形式）：

```latex
\mathbb E[\|g_k\|^2 \mid \mathcal F_k] \le A\bigl(f(z_k)-f^\star\bigr) + B\|\nabla f(z_k)\|^2 + C
```

N5，相对噪声：

```latex
\mathbb E[\|e_k\|^2 \mid \mathcal F_k] \le \nu^2 \|\nabla f(z_k)\|^2
```

N6，带权噪声可和：

```latex
\sum_k s_k^2 t_k^2 \sigma_k^2 < \infty, \qquad \sigma_k^2 = \mathbb E[\|e_k\|^2 \mid \mathcal F_k]
```

### A.2 N2 与 N6 的比较

若 s\_k ≡ s > 0 且 t\_k ≍ k，则 N6 变成下式。此时固定方差不满足 N6，N6 强于 N2。

```latex
\sum_k k^2 \sigma_k^2 < \infty
```

若 s\_k ≍ k^(−δ)，则加权项满足下式。当 σ\_k² ≤ σ² 且 δ > 3/2 时，N2 可以推出 N6。

```latex
s_k^2 t_k^2 \sigma_k^2 \asymp k^{2-2\delta} \sigma_k^2
```

另外，对同一个序列有 ℓ¹ ⊂ ℓ²，所以要求噪声项 ℓ¹ 可和比要求 ℓ² 可和更强。

### A.3 ABC 的来源：有限和例子

设 f = (1/n)Σ f\_i，每个 f\_i 是 L\_i-光滑且有下界的函数。由光滑性可得下式；对随机索引取期望，就得到 B = 0 的 ABC 条件。

```latex
\|\nabla f_i(x)\|^2 \le 2L_i\bigl(f_i(x) - f_i^{\inf}\bigr)
```

一个具体例子：取 f\_1 = x²/2，f\_2 = 3x²/2，则 f = x²。随机梯度以相同概率取 x 或 3x，因此 E\[g²\] = 5x² = 5f(x)。这个例子说明：梯度二阶矩在全空间上没有统一上界，ABC 却成立，而且这里不涉及任何过参数化。

### A.4 ABC 的局限

1. 常数 A、B、C 可能非常宽松，导致理论界无法反映算法的实际表现。
2. 一般单调算子没有函数值差，ABC 无法直接表述。
3. 对真实的深度模型，这个条件很难在全空间上验证。在实验轨迹上观察到近似关系，不能当作定理假设。

### A.5 过参数化与 interpolation

若所有分量在同一点 x\* 达到最小，即对每个 i 都有 ∇f\_i(x\*) = 0，则随机梯度在最优点处没有采样噪声。此时常可推出 strong growth 条件、相对噪声条件，或 ABC 中的 C = 0。但“参数比样本多”只说明可能存在插值解，并不能保证整条轨道上的全局不等式成立。

### A.6 高斯噪声例子

设 f(x) = μx²/2，g\_k = μx\_k + ξ\_k，ξ\_k \~ N(0, σ²)。条件方差恰好等于 σ²，所以满足 N2；但它不满足 N5。固定步长 η 时，迭代为：

```latex
x_{k+1} = (1-\eta\mu)x_k - \eta\xi_k
```

均方误差会趋向一个正的稳态值，而不会趋于零。递减步长可以压低噪声的总影响，从而恢复 almost-sure 收敛。

## 附录 B：单调性与算子层次

### B.1 定义

算子 V 称为单调，是指对任意 x、y，下式成立：

```latex
\langle V(x) - V(y),\, x - y \rangle \ge 0
```

凸可微函数的梯度 ∇f 是单调算子，但单调算子不一定是梯度。例如旋转算子 V(u, v) = (v, −u)：它的上述内积恒为 0，所以是单调的，但它不对应任何凸势函数。这正是 minimax 问题与普通优化问题的差别所在。

### B.2 非扩张 fixed-point 是 cocoercive 的特例

若 T 非扩张，令 V = Id − T，则 V 满足 cocoercivity（共强制性）：

```latex
\langle V(x) - V(y),\, x - y \rangle \ge \tfrac12 \|V(x) - V(y)\|^2
```

由此得到下面的包含关系。这也说明了为什么 Fast OGDA 处理的问题类比 Fast KM 更一般，证明也更难。

```latex
\text{nonexpansive fixed-point} \subset \text{cocoercive zero-finding} \subset \text{monotone Lipschitz zero-finding}
```

### B.3 G-EAG 的迭代格式

其中 v 是 anchor，ε\_k ≍ 1/k 是逐渐消失的 Tikhonov 参数；M(y\_{k+1}) 一项提供 extragradient 结构。

```latex
\begin{aligned}
y_{k+1} &= x_k - \theta\varepsilon_k (x_k - v) - \theta M(x_k),\\
x_{k+1} &= x_k - \theta\varepsilon_{k+1}(x_{k+1} - v) - \theta M(y_{k+1})
\end{aligned}
```

## 附录 C：PGD、DR、PDHG、KKT 的单调算子表述

这四类方法都可以纳入单调包含或 fixed-point 框架。这就是研究 Vx = 0 和 x = Tx 的动机。

### C.1 Proximal gradient

问题 min f(x) + g(x) 的最优性条件，以及对应的 fixed-point 映射如下。其中 ∇f 单调，∂g 极大单调。

```latex
0 \in \nabla f(x) + \partial g(x), \qquad T = \operatorname{prox}_{\gamma g}\bigl(\operatorname{Id} - \gamma \nabla f\bigr)
```

### C.2 Douglas–Rachford

对于 0 ∈ A(x) + B(x)，DR 使用 resolvent J 和 reflector R：

```latex
J_{\gamma A} = (\operatorname{Id} + \gamma A)^{-1}, \quad R_{\gamma A} = 2J_{\gamma A} - \operatorname{Id}, \quad T_{\mathrm{DR}} = \tfrac12\bigl(\operatorname{Id} + R_{\gamma B} R_{\gamma A}\bigr)
```

### C.3 PDHG 与 KKT 系统

对 min f(x) + g(Ax) 引入对偶变量 y，得到鞍点问题：

```latex
\min_x \max_y \; f(x) + \langle Ax, y \rangle - g^\ast(y)
```

其 KKT 系统可以写成一个算子：

```latex
\mathcal A\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} \partial f(x) + A^\ast y \\ \partial g^\ast(y) - Ax \end{pmatrix}
```

这个算子是单调的，原因有两点：∂f 和 ∂g\* 都是极大单调的；而线性块 \[\[0, A\*\], \[−A, 0\]\] 是斜对称的，对内积的贡献为零。

## 附录 D：benchmark 与比较指标

理论比较至少应覆盖以下五类方法，并对每个方法使用同一组指标。

| 类别              | 方法                                        |
| --------------- | ----------------------------------------- |
| 确定性 fixed-point | Classical KM、Fast KM、Halpern              |
| 确定性单调算子         | EG、Fast OGDA、G-EAG                        |
| 随机 fixed-point  | Stochastic KM、Stochastic Halpern、随机 iKM   |
| 随机单调算子          | Stochastic EG、随机 OGDA、随机 forward-backward |
| 应用型方法           | SGD、SGDA、PDHG、DR、proximal splitting       |

比较指标：

1. 噪声模型（N2、N6、相对噪声）
2. oracle 调用次数
3. 单次迭代所用样本数
4. 末次残差
5. 迭代点是否收敛
6. objective gap 或 primal-dual gap
7. 弱收敛还是强收敛
8. 是否需要 variance reduction
9. 是否需要递增 batch
10. 是否需要预知总迭代次数 K

## 附录 E：待核实清单

以下内容来自会后的整理分析，尚未与原文逐条对照。写入论文或汇报之前必须先核实。

- [ ] 每篇论文的完整作者、标题、年份、期刊，以及对应的定理编号（随机 iKM、Fast KM、Fast OGDA、G-EAG）
- [ ] “随机 KM 在较弱方差条件下的 a.s. 弱收敛”：找到具体论文和定理
- [ ] “随机 KM 在加权误差可和条件下的末次残差 a.s. 速率”：找到具体论文，确认其参数区间是否已覆盖随机 Fast KM
- [ ] 随机 iKM 结果中 B\_K（bias 项）的确切含义及所需假设
- [ ] Fast KM 对 T 的确切要求（averaged 还是 nonexpansive），以及参数条件
- [ ] 第 4.3 节中“N6 与 o(1/k) 速率的冲突”：在 Fast KM 的能量不等式中验证
