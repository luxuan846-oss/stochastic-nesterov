# AFP 与原始 Fast KM 的覆盖核对

2026-10-14。依据：`sources/delayed.txt`（Nguyen-Trung–Tran-Dinh，arXiv:2512.13547v1）第 3.1 节 (AFP)、式 (8)、式 (13)；Boţ–Nguyen 式 2.7 的 $V$ 形式取自 `261014-stochastic-km-proof-audit.md` 第 2 节。

## 1. AFP 消去 $z$ 后的单序列形式

AFP：$x^{k+1}=y^k-\eta_k g_k$，$z^{k+1}=z^k+\frac{\gamma}{s}(x^{k+1}-y^k)$，$y^{k+1}=\frac{t_k-s}{t_k}x^{k+1}+\frac{s}{t_k}z^{k+1}$，其中 $g_k=\widetilde{G}^k=Gy^k+e_k$，$t_k=k+3s+\tau$，$\eta_k=\frac{\eta t_k}{2(t_k-s)}$。

由 $y^k$ 的定义反解 $z^k$，代入后得到，对 $k\ge1$：

$$
y^{k+1}=y^k+\beta_k(y^k-y^{k-1})-\eta_k\Bigl(1-\frac{s-\gamma}{t_k}\Bigr)g_k+\beta_k\eta_{k-1}g_{k-1},\qquad \beta_k=\frac{t_{k-1}-s}{t_k}
$$

代入 $\eta_k$ 后三个系数为：

- 动量：$\beta_k=\frac{t_{k-1}-s}{t_k}$；
- $g_k$：$\frac{\eta}{2}\cdot\frac{t_k-s+\gamma}{t_k-s}$；
- $g_{k-1}$：$\frac{\eta}{2}\cdot\frac{t_{k-1}}{t_k}$。

代数推导见上；未做数值验证。

## 2. 与原始 Fast KM 比较

Fast KM：$x_{k+1}=x_k+\frac{k}{k+\alpha}(x_k-x_{k-1})-s_F\frac{k+\alpha/2}{k+\alpha}g_k+s_F\frac{k}{k+\alpha}g_{k-1}$。

1. 动量相等要求 $\alpha=s+1$，并把 AFP 的下标平移为 $m=k-1+2s+\tau$，此时 $\beta_k=\frac{m}{m+s+1}$。
2. 平移后 $g_{k-1}$ 的系数：AFP 为 $\frac{\eta}{2}\cdot\frac{m+s}{m+s+1}$，Fast KM 为 $s_F\frac{m}{m+s+1}$。两者之比随 $m$ 变化，不存在常数 $\eta,s_F$ 使其对所有 $m$ 相等。
3. 把两项合并成「差分项 + 单独 $g_k$ 项」后，单独 $g_k$ 项的主阶系数：AFP 约为 $\frac{\eta}{2}\cdot\frac{1+\gamma}{m}$，Fast KM 为 $s_F\frac{(s+1)/2}{m}$。主阶相等要求 $s=1+2\gamma$，与 AFP Theorem 1 的 $s\ge1+3\gamma$、$s>1$ 不相容。

**判定：AFP 不是原始 Fast KM 的重新参数化。** 原始 Fast KM 在 N6 下的几乎必然定理不是 AFP Theorem 2 的字面推论。

## 3. 结构上的共同点

AFP 每步只调用一次 oracle。在单序列形式中，存好的 $g_{k-1}$ 再次出现，误差 $e_{k-1}$ 先后以相反符号进入两步更新。因此 **AFP 已经是复用型递推**，并已在 $\sum_k k^2\mathbb{E}_k\lVert e_k\rVert^2<\infty$ 一类条件下证明几乎必然 $o(1/k)$。「复用查询」本身不构成新意。

## 4. 稀有误差反例同样适用于 AFP

取 $G=I$（$\beta=1$ 的余强制算子），单序列递推中新误差 $e_k$ 的系数趋于 $\eta/2>0$。取独立误差 $e_k=\pm1/k$，各以概率 $p_k/2$ 出现，$p_k=k^{2-q}$，$2<q\le3$。给定历史，两种符号中至少一种使 $k\lVert y^{k+1}\rVert\ge c>0$；条件 Borel–Cantelli 给出这件事无穷多次发生。所以只控制二阶矩时，AFP 的 $q>3$ 型条件在幂次尺度上不能放宽到 $(2,3]$。此论证为本次推导，待写成完整证明。

## 5. 对论文定位的影响

1. 定理 A（原始 Fast KM、N6、Hilbert）是 AFP 的系数变体加无限维推广，单独作为 SIOPT 贡献偏弱。
2. 主要贡献应放在尾部门槛：轻尾时 $q>2$ 是否足够（待证），二阶矩下 $(2,3]$ 的反例（第 4 节）。该现象覆盖 Fast KM 与 AFP 这一类单 oracle 加速递推。
3. 待核：AFP Corollary 2 中随机 oracle 情形的批量条件原文表述；AFP 的有限维假设在 Theorem 2 中的具体用途。
