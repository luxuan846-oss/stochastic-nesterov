from pathlib import Path
import json,re,subprocess
P=Path(__file__).parent
W=P/'research-wiki'
H='/Users/liluxuan/Documents/Codex/Auto-claude-code-research-in-sleep/tools/research_wiki.py'
data=[
('2206.09462','Fast KM 原始递推给 o(1/k) 残差与弱点极限。','Thms. 3.4–3.5；Remark 2.2。','Hilbert；theta-averaged，含 theta=1；alpha>2。','无噪声结果；不能把随机化和确定性等价混同。','memory/readings/sources/fast_km.txt'),
('2203.10947','Fast OGDA 给单调 Lipschitz 末次 o(1/k) 与弱点极限。','期刊版 Thms. 16–17，Algorithm 2。','Hilbert；单调 L-Lipschitz；s<1/(2L)。','这是确定性定理；预测点相关误差需另证。','roadmap_20261014/sources/fast_ogda.txt'),
('2406.02413','VR-FKM v4 已有 a.s. o(1/k) 残差和点极限。','Thm. 2；Cors. 1–2：O(n+n^(2/3)/epsilon)。','有限维有限和；平均分量余强制型条件；SVRG/SAGA。','不能只保留均值算子余强制；MOR模板不等于正式发表。','memory/readings/sources/vr_fast_km.txt'),
('2512.13547','AFP 已覆盖一般随机 oracle 加递增批量的 a.s. 快速率。','Thm. 2 在 y_k 上的残差 o(1/k)；Cor. 2。','有限维余强制；递推误差条件(7)与可和delta。','与原始缓存 Fast KM 的全部系数、初始化和随机过程等价性待核对。','memory/readings/sources/delayed.txt'),
('2508.16791','VAPEG v2 的单调特例已有 a.s. o(1/k) 及点极限。','Thm. 3.2；Cor. 3.4 批量成本 epsilon^(-4-nu)。','有限维；单调 Lipschitz 特例；一般误差条件(15)。','v1 名称VFOG不能和v2定理编号混用；不可自动推广至原始Fast OGDA。','roadmap_20261014/sources/vfog.txt'),
('2609.28543','stochastic iKM 给预设时域的近最优 RMS 残差。','Thm. 1；Appendix A Proposition 1。','实Hilbert；N2；时域依赖参数；每步一次新oracle。','确定性Fast KM等价参数与随机主定理schedule不同；无直接无限轨道a.s.结论。','roadmap_20261014/sources/ikm_zotero.txt'),
('2604.22581','随机KM在解处有限方差及样本映射结构下有弱点极限。','Thm. 2.13；Cor. 2.12 区分末次与running minimum。','可分Hilbert；非扩张样本映射；RM步长。','不能忽略样本映射条件；running minimum率不是末次率。','memory/readings/sources/cortild.txt'),
('2403.12338','随机Halpern在一般范数中有期望误差界及轨道极限。','Thm. 3.3、Cor. 3.5、Thm. 3.7、Thm. 3.10。','有限维一般范数；点极限需要光滑范数及误差可和。','epsilon^-3下界使用特定范数及算法访问模型，不否定Hilbert epsilon^-2。','memory/readings/sources/bravo_contreras.txt'),
('2410.07870','SGC可使SNAG保留加速目标差的a.s.小o速率。','ICLR2025正式版Thms. 3–4。','光滑凸有限和；SGC；双步长参数。','不是持续加性方差界；目标差不能直接代替一般算子残差。','roadmap_20261014/sources/hermant.txt'),
('2511.12665','随机FISTA在衰减梯度步长下有a.s.弱点极限。','v3 Thm.3.10、Remark3.11。','Hilbert；有界条件方差；gamma_k约k^-1.5 log^-r，r>0.5。','对应O(log^r/sqrt(k))目标差是期望界，不是a.s.o(k^-2)。','roadmap_20261014/sources/salzo.txt'),
('2403.04860','随机Ravine区分目标差快率与点极限所需的噪声权重。','JOTA2026 Thm.3.1、Cor.4.1。','条件无偏；目标值用加权平方可和；点极限需更强加权一阶可和。','不能把目标值条件直接用作点极限条件。','roadmap_20261014/sources/ravine.txt'),
('2609.36033','dual-anchor结合内层resolvent近似给近最优随机求零复杂度。','Cor.3.6。','单调Lipschitz样本算子；无偏有界方差。','有限精度复杂度，非原始Fast OGDA的无限轨道定理。','memory/readings/sources/dual_anchor.txt')]
meta={x['id'].split('/abs/')[-1].split('v')[0]:x for x in json.loads((P/'arxiv_metadata.json').read_text())}
nodes={}
for aid,thesis,result,assume,limit,source in data:
 m=meta[aid]
 subprocess.run(['python3',H,'ingest_paper',str(W),'--arxiv-id',aid,'--title',m['title'],'--authors',','.join(m['authors']),'--year',m['published'][:4],'--venue','arXiv；正式版见roadmap书目','--thesis',thesis,'--tags','fixed-point,stochastic,core'],check=True)
 for f in (W/'papers').glob('*.md'):
  s=f.read_text()
  if 'arxiv: "'+aid+'"' not in s:continue
  nodes[aid]=re.search(r'^node_id: (.+)$',s,re.M)[1]
  entries={'Problem / Gap':'同一无限随机轨道的末次残差与点极限；以roadmap的精确问题类为准。','Method':thesis,'Key Results':result+' 原文位置：`'+source+'`。','Assumptions':assume,'Limitations / Failure Modes':limit,'Reusable Ingredients':'按原文定理的误差权重、输出点和filtration组织证明。','Open Questions':'原始Fast KM/Fast OGDA的随机过程覆盖判定仍需逐式证明。','Claims':'这里只记录论文报告的结论；未进行逐行形式证明审核。','Relevance to This Project':'核心邻近文献；参见主报告四组速率表与第5–7节。'}
  for sec,body in entries.items():s=re.sub(r'(## '+re.escape(sec)+r'\n).*?(?=\n## |\Z)',lambda z:z[1]+body+'\n',s,flags=re.S)
  f.write_text(s)
  break
(P/'wiki_nodes.json').write_text(json.dumps(nodes,ensure_ascii=False,indent=2))
(W/'ideas'/'001-covered-broad-claim.md').write_text('''---
type: idea
node_id: idea:001
title: "首次建立随机快速不动点的a.s.小o速率"
stage: rejected
outcome: negative
---
# 已有覆盖的宽泛创新性表述
## Failure Notes
VR-FKM Thm.2、AFP Thm.2、VAPEG v2 Thm.3.2已有对应结论。不得再将三重交集整体当作未研究领域。
''')
(W/'ideas'/'002-second-moment-threshold.md').write_text('''---
type: idea
node_id: idea:002
title: "仅用二阶矩将原始Fast KM的q门槛放宽到2"
stage: rejected
outcome: negative
---
# 二阶矩目标受到反例排除
## Failure Notes
主报告§7.2给出V(x)=x、s=1、独立稀有误差的解析反例；2<q<=3时条件方差k^-q仍不能保证k*r_k趋于零a.s.。只排除这一定义的原始递推与噪声类。
''')
(W/'gap_map.md').write_text('''# Gap Map

## gap:raw_equivalence
原始Fast KM/Fast OGDA与AFP、VR-FKM、VAPEG的随机递推、初值和查询点是否完全相同？状态：待验证。不是“无人研究”的声明。

## gap:tail_condition
在明确条件轻尾约束下，能否使用2<q<=3的方差衰减取得原始Fast KM的末次a.s.o(1/k)？状态：待验证。仅二阶矩版本已被标量反例排除。

## gap:anytime_path
单次oracle、持续方差、无需时域的惯性轨道：可证明的末次a.s.速率及点极限是什么？状态：待验证。iKM有限时域界不能直接转用。
''')
edges=[('2406.02413','2206.09462','extends','VR-FKM采用Fast KM结构并加入VR；不声称所有噪声过程等价。'),('2508.16791','2203.10947','inspired_by','VAPEG使用加速past-gradient机制；与Fast OGDA完全等价尚未核实。'),('2512.13547','2406.02413','extends','AFP一般递推误差模型覆盖有限和之外的随机oracle。'),('2609.28543','2206.09462','supports','Appendix A Proposition 1给确定性特殊参数下等价，不是随机主定理的自动覆盖。')]
for a,b,t,e in edges:subprocess.run(['python3',H,'add_edge',str(W),'--from',nodes[a],'--to',nodes[b],'--type',t,'--evidence',e],check=True)
for aid in ['2406.02413','2512.13547','2508.16791']:
 subprocess.run(['python3',H,'add_edge',str(W),'--from',nodes[aid],'--to','idea:001','--type','invalidates','--evidence','原文已明示a.s.残差小o与点极限，否定宽泛首次性。'],check=True)
for aid in ['2206.09462','2512.13547','2508.16791','2203.10947']:
 subprocess.run(['python3',H,'add_edge',str(W),'--from',nodes[aid],'--to','gap:raw_equivalence','--type','addresses_gap','--evidence','提供覆盖判定所需原始递推；关系不代表判定已经完成。'],check=True)
# Connections are generated only from the canonical edge store.
edges=[json.loads(l) for l in (W/'graph'/'edges.jsonl').read_text().splitlines() if l.strip()]
for f in (W/'papers').glob('*.md'):
 s=f.read_text();node=re.search(r'^node_id: (.+)$',s,re.M)[1]
 connected=[e for e in edges if node in (e['from'],e['to'])]
 body='自动由 graph/edges.jsonl 生成。\n'+('\n'.join('- '+e['from']+' —'+e['type']+'→ '+e['to']+'：'+e['evidence'] for e in connected) or '本轮没有添加显式关系。')
 s=re.sub(r'(## Connections\n).*?(?=\n## |\Z)',lambda z:z[1]+body+'\n',s,flags=re.S);f.write_text(s)
subprocess.run(['python3',H,'log',str(W),'research-lit/refine: 12 papers enriched; relationships generated; 2 rejected ideas and 3 pending questions saved.'],check=True)
for cmd in ['rebuild_index','rebuild_query_pack','stats']:subprocess.run(['python3',H,cmd,str(W)],check=True)
