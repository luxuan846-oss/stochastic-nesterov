# 自行修订记录

## Anchor Check
原始问题锚定保持不变。先判定已有覆盖，再检验原始递推的噪声条件。未引入深度模型或其他算法论文作为新目标。

## Simplicity Check
只保留原始Fast KM为首阶段。Fast OGDA为后续。没有新增训练模块、常规防御脚手架或大规模实验。

## 修订依据
外部复核返回403，无有效评审意见。以下修订来自主报告§7.2的解析反例，不能称为独立模型审阅。仅二阶矩q>2目标已撤回；轻尾版本仍为待验证候选。

## 完整方案

# 研究方案：原始 Fast KM 的随机噪声门槛

## Problem Anchor
- Bottom-line problem：研究原始 Fast KM，并以 Fast OGDA 为后续方向，判断同一无限随机轨道上的末次残差快速率及迭代点极限能在什么噪声条件下成立。
- Must-solve bottleneck：动量与旧 oracle 缓存引入相关误差；已有随机快速框架已证明若干 a.s. o(1/k) 结论，必须先判明算法等价性与假设强弱，才谈新的理论增量。
- Non-goals：非单调 VI、分布式、联邦、深度模型模块、仅有限时域期望复杂度、为了创新而重新命名算法。
- Constraints：优先 Hilbert 空间余强制算子；先完成原始 Fast KM，Fast OGDA 仅在首阶段形成实质增量后推进；不声称尚未证明的速率。
- Success condition：得到可逐式核对的已有框架覆盖判定，并获得一个严格更弱噪声条件下的新定理，或一个明确排除原定目标的反例；只有覆盖判定本身时，交付研究记录而不宣称新论文结果。

## Technical Gap
有限维 VR-FKM 的 Theorem 2 已有 a.s. o(1/k) 及点极限。AFP 的 Theorem 2 和 Corollary 2 还允许一般随机 oracle 加递增 batch；VAPEG v2 的 Theorem 3.2 覆盖单调 Lipschitz 特例。因此“随机快速方法 + 加权平方可和 + a.s. o(1/k)”不是已确认缺口。窄问题是原始 Fast KM 缓存同一旧误差时，最弱可证明噪声门槛是什么，以及是否已有完全相同状态递推。

## Method Thesis
冻结原始递推；把旧误差当作状态的一部分，先推导一步条件漂移，找出真正出现的噪声权重，再与 AFP/VR-FKM 逐式比较。这里没有训练组件；现代大模型工具与研究定理无关，不引入。

## Contribution Focus
唯一候选贡献：在原始递推及明确轻尾假设下，检验能否降低批量增长要求，并保留 a.s. 末次残差 o(1/k) 与弱点极限。此贡献目前未验证；仅二阶矩版本已被标量稀有误差反例排除。算法等价性审计与标量反例属于研究门槛，不自动算论文贡献。

## Proposed Method
设 V=I-T 为 beta-余强制，zer(V) 非空，alpha>2，0<s<=2 beta。固定初值，并缓存 g_k=V(x_k)+e_k，每步仅抽取一个新估计。递推为

$$x_{k+1}=x_k+\frac{k}{k+\alpha}(x_k-x_{k-1})-\frac{s\alpha}{2(k+\alpha)}g_k-\frac{sk}{k+\alpha}(g_k-g_{k-1}).$$

F_k 包含 x_k 及 e_{k-1} 等全部历史，在生成 e_k 前形成；E[e_k|F_k]=0，E[||e_k||^2|F_k]<=sigma_k^2。旧 e_{k-1} 不再是相对于 F_k 的鞅差。

1. 消去 AFP 的辅助变量，比较全部系数、查询点、初值约束和误差传播。对 VR-FKM 和 iKM 的确定性等价命题进行同样比较。记录“同算法同随机过程”“仅无噪声等价”“不同算法”三种判定。
2. 从确定性 Fast KM Lyapunov 出发，保留包含 e_{k-1} 的交叉项，尝试补偿项；先证明非负性与一步漂移，再使用 Robbins–Siegmund。仅二阶矩时，不再以 q>2 为统一目标：主报告§7.2的稀有误差反例排除2<q<=3。AFP典型充分条件 sum k^2 sigma_k^2<infinity 对应q>3。只有显式加入条件次高斯或有界样本平均的浓度约束后，才研究2<q<=3，并另证历史误差累积可控。
3. 检查 V(x)=x、s=1 的精确噪声传递，再检查二维 V=aI+bJ 的单调线性族。不得由线性结论外推全部非线性余强制算子。
4. 若无法降低门槛，明确记录现有覆盖，完成复现。无需自动转向另一个课题。

## 解析诊断
对于 V(x)=x，s=1，递推精确为 x_{k+1}=c_k x_k-c_k e_k+d_k e_{k-1}，其中 c_k=(k+alpha/2)/(k+alpha)，d_k=k/(k+alpha)。新噪声系数趋于 1。若新噪声条件方差恒为 sigma^2>0，则 Var(x_{k+1}|F_k)=c_k^2 sigma^2，故 E|x_{k+1}|^2 无法趋于零。仅由这一方差下界尚不能排除不具一致可积性的 a.s. 极限；若要 a.s. 反例，另外指定独立高斯噪声并证明。

## Claim-Driven Validation Sketch
1. 覆盖判定：逐式变量消元和初值核对是必要证据。任何已有定理推论直接标“已有”。
2. 解析证明：先标量必要条件，再一般算子的条件漂移。只有实际得到闭合不等式后才陈述新定理。
3. 小型数值诊断：二维线性族，在 q=2.2,2.8,3.2 与固定方差下看末次残差和 k*r_k；只能发现错误及支持机制，不证明 a.s. 速率。复杂度同时记录迭代与总 oracle 次数。

## 时间与资源
第一阶段两至三天完成等价性及标量诊断；第二阶段一周集中检验条件漂移。普通 CPU 足够，无 GPU。通过新颖性门槛后再安排正式实验；本次 roadmap 不声称已执行此研究计划。

## 原始证据入口
- memory/readings/sources/delayed.txt，AFP Theorem 2、Corollary 2、公式 AFP。
- memory/readings/sources/vr_fast_km.txt，Theorems 1–2。
- roadmap_20261014/sources/vfog.txt，arXiv 2508.16791v2，Theorem 3.2。
- memory/readings/sources/fast_km.txt；若该文件名不存在，在 sources 目录按标题定位。
- roadmap_20261014/sources/ikm_zotero.txt，Appendix A Proposition 1。
- research-wiki 位于 roadmap_20261014/research-wiki；只读路径，由 reviewer 自行检查。
