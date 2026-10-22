# 随机快速不动点 roadmap

主报告为 `261014-领域roadmap-随机快速不动点.md` 与同名 PDF。PDF 共 12 页，由 Markdown 经 pandoc 与 XeLaTeX 生成。

- `research-wiki/`：12 篇核心文献的证据、11 条关系、2 条被否定思路和 3 个待验证问题。
- `refine-logs/`：研究锚定、初步方案、自行修订及指定外部复核失败记录。外部服务返回 403，没有独立评分或 READY 判定。
- `SOURCE_AUDIT.md`：证据范围与未完成核查。
- `homepage_checks.json`：主页访问状态。
- `verified_papers.json`：自动存在性核验的原始状态。VFOSA 的正式 JMLR 全文另已核对，自动匹配状态仍为待核验。
- `zotero-export.bib`：Zotero 原始书目导出。
- `PDF_VALIDATION.md`：最终 PDF 的字体、页数和视觉检查记录。
- `build_pdf.py`、`pdf-header.tex`、`pdf-tables.lua`：PDF 复现设置。

## 排版复现

在本目录运行 `python3 build_pdf.py`。需要 pandoc、XeLaTeX、系统 Times New Roman 和 PingFang 字体。首次提取字体需要 fontTools；本次将依赖安装在 `tmp/fonttools`，没有修改系统 Python。

系统字体集合的第 3 与第 11 个 face 分别为 PingFang SC Regular 和 Semibold。脚本使用这两个 face 的原始字形映射和轮廓，并将共享 CFF 内部名称与 SC face 名称一致化。中文 Scale=1，正文 10pt，表格 9pt；A4 页面，四侧页边距参数为 2cm，含目录与可点击链接。原始字体仅留在本地临时目录。

完整工作目录：`/Users/liluxuan/Documents/My_Papers/5_stochastic_nesterov/roadmap_20261014`。原始全文、提取文本和排版中间文件保留在本地，不混入两份主交付文件。
