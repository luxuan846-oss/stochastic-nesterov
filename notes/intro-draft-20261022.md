# Introduction 与 Related work 改写对照表

日期：2026-10-22。对象：`paper/main.tex` §1、§1.1。原文路径见 `notes/writing-phrasebook.md` 的来源列表。

## 1. 结构与参照

| 段落 | 功能 | 参照文献及位置 | 采用的结构或格式 |
|---|---|---|---|
| §1 第 1 段 | 问题与统一形式 | Yang et al. 2026 §1 第 1–3 段；Bravo–Cominetti §4.3；Cortild–Cartis–Peypouquet 摘要 | 先给问题，再给"把确定性格式中的精确评估换成随机返回值"的统一递推，随后举 SGD 与随机 proximal gradient |
| §1 第 2 段 | 确定性加速 | Boţ–Nguyen 2023 §1 式 (1.3) 后的速率综述、Algorithm 2.1、Theorems 3.4–3.5、Corollary 4.1 | 速率对比 $o(1/\sqrt{k})\to o(1/k)$ 写成独立公式 |
| §1 第 3 段 | 随机情形的困难 | 本稿 §3.3 式 (3.6)–(3.7)；Bravo–Cominetti Theorem 2.5 | 误差分解前置；$T=0$ 反例由递推直接计算 |
| §1 问题框 | 研究问题 | Yang et al. §1 用 quote 环境陈述问题的格式 | 只借格式，问题内容按本文递推重写 |
| §1 Objectives | 目标 | 本项目约定：未证结论标为目标 | 编号列表，末句统一标注未证 |
| §1.1 | Related work | Yang et al. §1.2 的加粗段首分组 | 四组：stochastic KM、fast deterministic、stochastic accelerated、lower bounds |

## 2. 关键事实的出处

| 正文陈述 | 出处 |
|---|---|
| SGD 对应 $T=\Id-\gamma\nabla h$ | Bravo–Cominetti §4.3 |
| KM 常数松弛 $o(1/\sqrt{k})$ | Boţ–Nguyen §1 |
| BC Theorem 2.5：有界方差，$\lambda_k=(k+1)^{-a}$，$2/3<a\le1$ | Bravo–Cominetti Theorem 2.5 与 H2；精读笔记 §4.2 检查点 |
| BC Theorem 2.8：H3，允许偏差和常步长，只有点收敛 | `bravo_cominetti.txt` 第 380–395 行 |
| Combettes–Pesquet Corollary 2.7：separable Hilbert，弱收敛 | Bravo–Cominetti Theorem 2.8 后的说明 |
| Cortild 等：fixed point 处方差有限，SGD 与随机 backward–forward | `cortild.txt` 摘要 |
| Fast FB、Fast RFB 不经过 averaged map | `notes/literature-route-map.md` §6 |
| Park–Ryu Theorem 4.6 最优 $O(1/k)$ | Yang et al. §1.2 引用 |
| Fast KM 是 iKM 的参数特例 | Yang et al. §1.2、Appendix A |
| VFOSA Theorem 14：$(k+1)^2$ 加权估计误差平方可和 a.s. | `vr_splitting.txt` 第 1274–1293 行 |
| AFP 批量 $k^{3+\omega}$ | `delayed.txt` 第 1453–1470 行；Yang et al. §1.2 |
| Yang Theorem 1 的 RMS 界 | `ikm.txt`；白板 2026-10-15 |
| Foster et al. Theorem 2：$\Omega(\varepsilon^{-2})$ | Yang et al. §1 引用 |
| Lee–Kim 的不可能性结果 | Zotero 全文 Theorem 5.1 |

## 3. 本稿新增、参考文献中无对应出处的表达

- `single-query implementation`、`stores the response … uses it again`：沿用 phrasebook 中 `stored response` 的约定。
- $T=0$ 下 $\mathbb{E}\lVert x_{k+1}-Tx_{k+1}\rVert^2\ge\sigma^2/4$：由递推直接推出，条件无偏消去交叉项，$a_k\ge1/2$。

## 4. 与旧稿的差别

- 旧稿 §1 只有 "Background and motivation"，没有统一形式与研究问题；新稿把问题框和 Objectives 前置。
- 旧稿 Related work 只有 BC、Yang、AFP 三篇；新稿按路线分四组。
- 旧稿 "No sharp threshold or novelty claim is asserted" 删除，改为 Objectives 末句一次性标注。
- N6 已在 §2.2 按原稿恢复，见第 5 节。

## 5. §2–§3 修订（同日）

| 部分 | 修改 | 依据 |
|---|---|---|
| §2.1 | 假设改为 $\theta$-averaged；cocoercivity 常数改为 $\frac{1}{2\theta}$ | Boţ–Nguyen §1 定义、式 (2.1) |
| §2.2 oracle | $e_k=b_k+\xi_k$，$b_k=\mathbb{E}[e_k\mid\mathcal F_k]$ | Yang et al. §2.2 式 (6) |
| §2.2 基础假设 | Assumption 2.2：$\mathbb E\lVert e_k\rVert^2<\infty$ | BC (H1) 的有限方差部分 |
| §2.2 噪声条件 | N1、N2 按原稿；N6 恢复为 $(s_kt_k\sigma_k)\in\ell^2$ 或 $\ell^1$；Fast KM 取 $s_k\equiv s$、$\alpha_k=k/(k+\alpha)$，$t_k=(k+\alpha-1)/(\alpha-1)$ | `main_20260926_ProfBot.tex` 第 45、136–137 行；Attouch–Fadili–Kungurtsev Theorem 3.1 的 $(K_2)$、$(K_2^+)$ |
| §2.2 新增 N7 | $(s_kt_k\lVert b_k\rVert)\in\ell^1_+(\mathscr F)$，Fast KM 下为 $\sum_k(k+1)\lVert b_k\rVert<\infty$ | 仿 BC Theorem 2.8 的 (H3)；$\ell^1_+(\mathscr F)$ 记号沿用 Combettes–Pesquet Notation 2.1 与 Attouch $(K_2^+)$；为本文候选条件 |
| Remark 2.3 | BC 递减步长与 H3 对比；batch $m_k\asymp k^q$ 时 N6-$\ell^2\Leftrightarrow q>3$，N6-$\ell^1\Leftrightarrow q>4$ | BC Theorem 2.5、2.8；直接计算 |
| §2.3 | 两个实例：SGD（$b_k=0$，$\frac{\gamma L}{2}$-averaged）；随机 proximal gradient（$\frac{2}{4-\gamma L}$-averaged，$\lVert b_k\rVert\le\gamma\tau_k$） | BC §4.3；Boţ–Nguyen §4 Corollary 4.1 前的 $\frac{2\beta}{4\beta-\gamma}$ |
| §3 | $0<s\le1/\theta$；条件均值加入 $b_k$ 项 | Boţ–Nguyen Algorithm 2.1 |
| §1.2 Notation and preliminaries | 记号、averaged 定义、cocoercivity 等价、prox、随机变量与 $\ell^p_+(\mathscr F)$、$\asymp$ | 结构仿 Boţ–Chenchene–Fadili §1.2；随机记号仿 Combettes–Pesquet Notation 2.1；$\asymp$ 仿 BC §1.2 |

本稿新增的约定：把 N6 的 $t_k$ 由 Fast KM 的系数 $k/(k+\alpha)$ 生成，以及 N7 的权重。两者在 §2.2 正文各注明一次。

## 6. 新增 §4 Applications to stochastic optimization（同日）

位置参照：Boţ–Nguyen §4 的 splitting 应用、BC §4.3 的 SGD、Cortild 等 §3.2 的 SBF，都放在主体分析之后。intro 第一段压缩为两句，并引用 §4。

| 小节 | 内容 | 依据 |
|---|---|---|
| 4.1 Setting | Assumption 4.1 复合问题；Assumption 4.2 采样梯度 $\tau_k$；mini-batch $\tau_k^2\le\tau^2/m_k$；Lemma 4.3 残差与最优性度量 | Baillon–Haddad 1977；Lemma 4.3 由 prox 最优性条件直接推出 |
| 4.2 SGD | $T_G$ 为 $\frac{\gamma L}{2}$-averaged；$b_k=0$；显式递推 (4.6)，$0<s\le\frac{2}{\gamma L}$ | BC §4.3；代入 (3.4) 直接整理 |
| 4.3 Prox gradient | $T_{FB}$ 为 $\frac{2}{4-\gamma L}$-averaged；显式递推 (4.9)；Lemma 4.4 $\lVert b_k\rVert,\sigma_k\le\gamma\tau_k$；Remark 4.5 偏差例子；batch $q>4$ | Boţ–Nguyen §4；Combettes–Yamada 2015 Prop. 2.4；条件 Jensen |
| 4.4 Backward–forward | $T_{BF}$ 同一常数；$\operatorname{Fix}T_{BF}=(\Id-\gamma\nabla h)(\operatorname{argmin})$；$b_k=0$；shadow 上的最优性度量 | Combettes–Yamada 公式对两因子对称；Cortild 等 §3.2、Corollary 3.4 (SBF)；VR-FKM 的 BFS |
| 4.5 Summary | Table 1：三种方法的 $T$、$\theta$、偏差、条件与 batch 指数 | 前三小节 |

本稿新增的推导：(4.6) 的整理、Lemma 4.3、$\operatorname{Fix}T_{BF}$ 的刻画，以及"prox 与梯度的顺序决定 oracle 是否有偏"这一比较。
