# Stochastic Fast KM 研究工作区

本仓库保存随机 Fast Krasnosel'skiĭ–Mann 方法的论文草稿、研究报告、证明与核查笔记、讨论记录，以及用于科研选题讨论的 Booming skill。

**当前状态（2026-10-22）：研究进行中。** 主线为 Q1 stochastic KM 的 expectation 基准 → Q2 固定参数 pure Fast KM 的 $T=0$ mean-square 反例 → Q3 decaying noise 下的 almost-sure 目标。§4.3 已写入，原 §4.4 已删除；$q>2$ 是 mean-square 必要条件，$q>3$ 对应尚待验证的 almost-sure 候选充分条件。进展、待办和待验证项集中在 [paper/README.md](paper/README.md)。

## 从这里开始阅读

1. [论文草稿](paper/main.tex)与[草稿状态说明](paper/README.md)：当前模型、算法和已明确的结论边界。
2. [10 月 16 日研究背景、动机与科学问题](research/Bot-meeting/261016-研究动机-背景-科学问题.md)及[英文讨论稿](research/Bot-meeting/261016-question-for-Bot.md)：最新候选问题、例子与待证目标。这些是研究讨论稿，部分概括仍需核查。
3. [研究报告](research/memory/readings/261014-stochastic-km-research-report.md)、[证明笔记](research/memory/readings/261014-stochastic-fast-km-proof.md)、[证明核查](research/memory/readings/261014-stochastic-km-proof-audit.md)及[AFP 覆盖关系](research/memory/readings/261014-AFP-coverage-check.md)：阅读时区分历史返回值复用与独立重新查询的算法。
4. [领域 roadmap](research/roadmap_20261014/261014-领域roadmap-随机快速不动点.md)：相关工作、研究分支与早期判断。
5. [Claude 与 Codex 对话索引](research/conversations/README.md)：2026 年 10 月 15、16 日的完整用户/助手正文，按 Europe/Vienna 日期保存；包含追问、公式、批注和观点变化。
6. [讨论白板](sparkling-whiteboard.md)：概念讨论与研究判断的阶段记录。较早条目不自动代表当前决定。

## 科研讨论 skill 与评议指令

- [Booming](skills/booming/SKILL.md)：科研选题、独立洞察、成果提升及前瞻判断的协作方法。
- [模块说明](skills/booming/references/modules.md)：M1–M4 与交付模板。
- [高飞访谈原话及四点提炼](skills/booming/references/gaofei-interview.md)：区分用户提供的访谈文字与讨论提炼。
- [Sparkling](skills/sparkling/SKILL.md)：原有研讨方法与白板约定；完整保留其 README、LICENSE、NOTICE 等来源文件。
- [GPT Pro 研究评议指令](research/reviews/gpt-pro-research-review-prompt.md)：让独立评议者阅读当前材料，判断研究价值并提出推进建议。

仓库中的 Booming 是本次上传快照。`SKILL.md` 中的用户目录路径属于安装后的运行约定；阅读本仓库时直接使用 `skills/booming/` 下的相对路径即可。

Sparkling 来自本机 Codex 已安装版本，其来源和许可见 [Sparkling README](skills/sparkling/README.md) 与 [LICENSE](skills/sparkling/LICENSE)。

## 使用说明

论文编译见 [paper/README.md](paper/README.md)。研究目录保留原有组织；历史笔记中的本机绝对路径可能已经变化，以本页相对链接为阅读入口。

上传内容保留研究源码、参考材料、PDF、笔记与对话正文。临时依赖、编译中间文件、本机配置和嵌套 Git 元数据不纳入版本管理。`research/meeting/overleaf/` 的研究文件按普通文件保存，其本地 Git 元数据保留在本机。
