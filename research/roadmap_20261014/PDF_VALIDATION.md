# PDF 检查记录

- 检查日期：2026-10-14。
- 产物：`261014-领域roadmap-随机快速不动点.pdf`，共 12 页，A4。
- 构建：pandoc + XeLaTeX 成功；最终构建日志没有报错。
- 字体：嵌入 TimesNewRomanPSMT 及其粗体、斜体；中文为 PingFangSC-Regular 与 PingFangSC-Semibold；数学使用 LatinModernMath。
- 中文正文实际大小约 9.96 PDF pt，对应 LaTeX 10pt；表格约 8.97 PDF pt，对应 LaTeX 9pt。显式设置 Scale=1，消除了先前的中文缩小问题。
- 字体来源：从系统 PingFang.ttc 提取 SC face 3、11。系统 TTC 各地域 face 共享 CFF 数据，内部名称沿用 HK；提取时保留 SC 字形映射和轮廓，仅规范独立字体的 CFF 名称。HK 与 SC 的 cmap 有 8599 个不同映射，已确认选择的是 SC。
- 排版参数：四侧 2cm 页边距；目录；彩色可点击链接；速率总表按条件和结论分表；跨页表格重复表头。
- 视觉检查：最终 12 页全部渲染并逐页查看联系表；另放大检查密集速率表。未见中文方框、表格重叠、公式裁切或页面溢出。
- 文本辅助检查：所有文本框位于页面边界内；没有 Unicode 替换字符。此检查仅辅助视觉核查，不代替数学验证。
- 中间预览：`renders/final/`；统计：`pdf-validation-data.json`。

本记录确认版面和生成结果，不构成对所引定理或候选研究方案的独立同行评审。
