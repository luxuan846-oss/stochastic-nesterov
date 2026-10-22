# 文献路线图的整理方法

来源：2026-10-22 对 Boţ 系列 FB 文章、随机 FB 近邻的整理。用于以后整理 Fast OGDA、DR、PDHG 等专题。

## 1. 思路

1. **先固定对象。** 写出被研究的算子或递推，例如 $T_{FB}=J_{\gamma A}(I-\gamma C)$。同一名称对应不同递推时分开处理，例如 RFB 与 FRB、Fast FB 与 $T_{FB}$ 上的 Fast KM。
2. **按数学路线分组，不按年份分组。** 本项目使用的组：
   - A. 不动点路线：结论经过 averaged 算子 $T$，可写成 Fast KM 的推论。
   - B. 算子结构路线：直接处理 $0\in Mx+Cx$ 等包含问题，不经过 $T$ 的 averagedness，不能当作 Fast KM 的推论引用。
   - C. 随机方向：再分噪声进入位置，即 full-map 加性噪声、随机梯度进入 prox 内部、先 prox 后采样。
   - D. 早期或连续时间工作：只列条目，不展开。
3. **每篇只记四项：** 问题与算子条件；算法或定理位置；结论的点、误差、随机性、保证类型；与本文递推的差别。
4. **结论落到切入点。** 最后一段写"本文可以与已有结果区分的地方"，按递推、查询方式、噪声条件逐项列出；再给 intro 的引用顺序。
5. **近邻比较必须对齐四个维度：** 同一递推、同一误差位置、同一采样方式、同一收敛类型。任一维度不同就写明哪一维不同。

## 2. 核对流程

1. **作者主页发表列表** 给出完整清单，避免遗漏。Boţ：https://www.mat.univie.ac.at/~rabot/publications.html 。
2. **本地 Zotero 数据库** 判断"在库与否"。复制 `~/Zoterodb/zotero.sqlite` 和 `zotero.sqlite-wal` 到临时目录后查询；直接以 `immutable=1` 打开会漏掉 WAL 中的新条目。
3. **本地原文文本** 核对定理编号和结论：`research/memory/readings/sources/*.txt`、`research/roadmap_20261014/sources/*.txt`、Zotero `storage/<key>/.zotero-ft-cache`。
4. **元数据**：期刊文章用 CrossRef，预印本用 arXiv API，JMLR 用论文页 `citation_*` meta。
5. **写入 Zotero**：MCP 写入需要真实 `ZOTERO_API_KEY`；未配置时用本机 Connector：`POST http://127.0.0.1:23119/connector/saveItems`，再 `POST /connector/updateSession`，`target` 取 `C<collectionID>`。
6. 版本不同导致编号不同时，写明所用版本，例如 VR-FKM v4、VAPEG v2、G 的 arXiv v2 与期刊版。

## 3. 标注规则

- 已用原文核对的定理位置直接写编号。
- 未对照全文的内容写"待核实"，只写一次，放在对应条目。
- 旧说法有误时，指出错在哪一句，再给正确版本。例：把 VFOSA 记成"只有 expected 结果"是错的；其 Theorem 14 给出 a.s. $k^2\lVert G_\lambda x_k\rVert^2\to0$ 与迭代点 a.s. 收敛。

## 4. 输出格式

- 开头一至两句给核心判断，例如"Boţ 的文章里，把 FB 当 averaged 算子做加速的只有 Fast KM Corollary 4.1"。
- 每组一张表，列为：文章（作者、短标题、期刊卷期年）、问题或 FB 出现的位置、结论。
- 结尾一段给切入点和引用顺序。
- 不写防御性声明，不重复提醒边界。

## 5. 固定用词

| 用词 | 含义 |
|---|---|
| 不动点路线 / 算子结构路线 | 结论是否经过 $T$ 的 averagedness |
| full-map 无偏 / prox-induced bias | 噪声在 resolvent 外部 / 内部 |
| 复用上一步的 noisy value | reuse of the previous oracle evaluation，与 same-sample、STORM 型递归区分 |
| last iterate、almost-sure、weak convergence | 收敛对象与收敛类型，沿用本文写法 |
| 最近邻 | 四个维度中差别最少的已有结果 |
| N2、N6、K1、K2 | 本文已定义的噪声与参数条件 |

## 6. 2026-10-22 的结果摘要

- 不动点路线：Boţ–Nguyen SINUM 2023 §4 Corollary 4.1，$B=0$ 得 FB。
- 算子结构路线：Fast FB（Numer. Math. 2026）、Fast RFB（JSC 2025）。
- 随机加速 FB 已有 a.s. 末次 $o(1/k)$：VFOSA Theorem 14，依赖 VR estimator，误差权重 $(k+1)^2$ 与 N6 相同。
- 随机 FB 最近邻：Lee–Kim 2026 VRAF，anchored FB，same-sample 两次查询，只有期望结果。
- 本文切入点：$T_{FB}$ 上的原始 Fast KM，每步一次新样本并复用上一步 noisy value，无 VR 修正，研究噪声门槛。
