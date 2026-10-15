# Research Wiki Query Pack

_Auto-generated. Do not edit._

## Project Direction
# 研究问题

原始Fast KM与Fast OGDA的无限随机轨道、末次a.s.快速率及点极限。先做精确覆盖判定。宽泛a.s.o(1/k)已有VR-FKM/AFP/VFOSA/VAPEG覆盖。仅二阶矩q>2的原始Fast KM目标受到稀有误差反例排除。

## Open Gaps
# Gap Map

## gap:raw_equivalence
原始Fast KM/Fast OGDA与AFP、VR-FKM、VAPEG的随机递推、初值和查询点是否完全相同？状态：待验证。不是“无人研究”的声明。

## gap:tail_condition
在明确条件轻尾约束下，能否使用2<q<=3的方差衰减取得原始Fast KM的末次a.s.o(1/k)？状态：待验证。仅二阶矩版本已被标量反例排除。

## gap:anytime_path
单次oracle、持续方差、无需时域的惯性轨道：可证明的末次a.s.速率及点极限是什么？状态：待验证。iKM有限时域界不能直接转用。

## Failed Ideas (avoid repeating)
- **首次建立随机快速不动点的a.s.小o速率**: ## Failure Notes
VR-FKM Thm.2、AFP Thm.2、VAPEG v2 Thm.3.2已有对应结论。不得再将三重交集整体当作未研究领域。

- **仅用二阶矩将原始Fast KM的q门槛放宽到2**: ## Failure Notes
主报告§7.2给出V(x)=x、s=1、独立稀有误差的解析反例；2<q<=3时条件方差k^-q仍不能保证k*r_k趋于零a.s.。只排除这一定义的原始递推与噪声类。

## Key Papers (12 total)
- [paper:attouch2024_stochastic_ravine_accelerated] The stochastic Ravine accelerated gradient method with general extrapolation coefficients: 
- [paper:bot2022_fast_krasnoselskiimann_algorithm] Fast Krasnosel'skii-Mann algorithm with a convergence rate of the fixed point iteration of $o\\left(\\frac{1}{k}\\right)$: 
- [paper:bot2022_fast_optimistic_gradient] Fast Optimistic Gradient Descent Ascent (OGDA) method in continuous and discrete time: 
- [paper:bravo2024_stochastic_halpern_iteration] Stochastic Halpern iteration in normed spaces and applications to reinforcement learning: 
- [paper:cortild2026_stochastic_krasnoselskiimann_iterations] Stochastic Krasnoselskii-Mann Iterations: Convergence without Uniformly Bounded Variance: 
- [paper:hermant2024_gradient_correlation_key] Gradient correlation is a key ingredient to accelerate SGD with momentum: 
- [paper:nguyentrung2025_class_accelerated_fixedpointbased] A Class of Accelerated Fixed-Point-Based Methods with Delayed Inexact Oracles and Its Applications: 
- [paper:salzo2025_iterates_fista_converge] The iterates of FISTA converge even under inexact computations and stochastic gradients: 
- [paper:trandinh2024_variancereduced_fast_krasnoselkiimann] Variance-Reduced Fast Krasnoselkii-Mann Methods for Finite-Sum Root-Finding Problems: 
- [paper:trandinh2025_new_accelerated_pastextragradient] New Accelerated Past-Extragradient Methods with Variance Reduction for Generalized Equations: 
- [paper:yang2026_stochastic_inertial_krasnoselskiimann] Stochastic Inertial Krasnosel'skii-Mann Iteration Achieves Near-Optimal Sample Complexity: 
- [paper:yoon2026_dualanchor_acceleration_nearoptimal] Dual-Anchor Acceleration Is Near-Optimal for Stochastic Monotone Root-Finding: 
## Recent Relationships (11 total)
  paper:trandinh2024_variancereduced_fast_krasnoselkiimann --extends--> paper:bot2022_fast_krasnoselskiimann_algorithm
  paper:trandinh2025_new_accelerated_pastextragradient --inspired_by--> paper:bot2022_fast_optimistic_gradient
  paper:nguyentrung2025_class_accelerated_fixedpointbased --extends--> paper:trandinh2024_variancereduced_fast_krasnoselkiimann
  paper:yang2026_stochastic_inertial_krasnoselskiimann --supports--> paper:bot2022_fast_krasnoselskiimann_algorithm
  paper:trandinh2024_variancereduced_fast_krasnoselkiimann --invalidates--> idea:001
  paper:nguyentrung2025_class_accelerated_fixedpointbased --invalidates--> idea:001
  paper:trandinh2025_new_accelerated_pastextragradient --invalidates--> idea:001
  paper:bot2022_fast_krasnoselskiimann_algorithm --addresses_gap--> gap:raw_equivalence
  paper:nguyentrung2025_class_accelerated_fixedpointbased --addresses_gap--> gap:raw_equ
