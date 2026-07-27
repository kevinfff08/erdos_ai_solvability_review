# Problem 655

## 基本信息

- 原始链接: https://www.erdosproblems.com/655
- LaTeX 页面: https://www.erdosproblems.com/latex/655
- 原始状态: `open`
- 奖金: `no`
- 主类别: `geometry`
- 原始标签: `geometry`, `distances`
- 形式化状态: `yes`
- OEIS: `possible`
- 原站备注字段: ambiguous statement

## 原问题

Let $x_1,\ldots,x_n\in \mathbb{R}^2$ be such that no circle whose centre is one of the $x_i$ contains three other points. Are there at least\[(1+c)\frac{n}{2}\]distinct distances determined between the $x_i$, for some constant $c>0$ and all $n$ sufficiently large?

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `26/100`
- 建议路线: 优先提取等价表述、尝试特殊情形、寻找可计算子问题，再决定是否进入证明搜索。

## 判断依据

### 有利因素

- 已有形式化陈述，可降低语义误读风险

### 主要障碍

- 所属标签偏证明密集：distances, geometry
- 题面含渐近/无限对象线索：sufficiently large
- 缺少明显有限搜索入口。

### 公开版思考过程摘要

- 先识别问题类型：无限/渐近或抽象证明倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: distances, geometry
- 有限/计算线索: 无
- 渐近/无限线索: sufficiently large
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5-level tool-augmented model`
- 结论: **按给定 JSON 中的原始表述，这个问题是很高优先级的 AI 可处理候选：模型不需要真正证明一个新的下界，而是可以验证并形式化备注中指出的反例。因此它更像是“澄清/反驳原表述并提出可验证修正版”的任务，而不是直接攻克开放版本。**
- 等级: `high_candidate`
- 分数: `88/100`
- 信心: `high`
- 可能路线: 最可能路线是把原命题精确定义化，然后验证正 n 边形顶点集合：对任一顶点为圆心，到其他顶点的相同距离最多对应两个点，因此满足“没有以某个 xi 为中心且经过三个其他点的圆”的条件；但整体 distinct distances 只有约 n/2 个，不能达到 (1+c)n/2。随后可把这一点形式化，并把真正未解决的部分重新表述为需要额外一般位置假设的版本。

### 支持理由

- JSON 备注已经给出关键反例方向：n 个点等距分布在一个圆上会否定原猜想。
- 该反例的验证主要是初等几何和有限组合计数，适合由模型配合符号计算或形式化证明工具完成。
- 问题已标记 formalized=yes，说明把条件和反例转写到形式系统中的成本相对可控。
- 目标若限定为“完成/验证原表述是否成立”，AI 很可能能给出完整、可审计的反驳证明。
- 即使不解决修正版，AI 也能显著推进问题整理：区分原命题、反例、以及可能意图中的一般位置命题。

### 主要障碍

- 最大障碍不是反例本身，而是题目备注指出的 ambiguous statement：真正想问的可能是加入 no three on a line、no four on a circle 等一般位置条件后的版本。
- 若转向一般位置修正版，线性下界的改进可能牵涉到离散几何中较深的 distinct distances 技术，AI 不能仅靠局部搜索保证解决。
- 需要小心区分“每个点看到的 distinct distances 至少 (n-1)/2”和“全局 distinct distances 至少 (1+c)n/2”这两个层级。
- 如果形式化系统已有的问题定义采用了修正解释，而非原始自然语言表述，则反例验证需要重新核对形式化定义。

### 需要的验证

- 形式化验证正 n 边形顶点满足中心圆条件：任一固定顶点到其他顶点的同距点数不超过 2。
- 证明正 n 边形的全局 distinct distances 数为 floor(n/2)，从而对任意 c>0，当 n 足够大时小于 (1+c)n/2。
- 检查 formalized=yes 对应的形式化版本是否忠实于 JSON statement，而不是已经加入额外一般位置条件。
- 若研究修正版，需要先明确额外假设，并对这些假设下的小规模配置做计算搜索和反例排除。

### 公开版思考摘要

公开可审计的核心判断是：原表述已有自然反例。正 n 边形中，从每个顶点出发，同一弦长通常对应左右对称的两个点，不会出现三个其他点落在同一个以该顶点为圆心的圆上；但整个配置只产生约 n/2 种距离。因此原始不等式无法对任何固定 c>0 成立。GPT-5.5 级别模型配合计算和形式化工具，很可能能完整验证这个反例，并帮助整理题目的修正版本；但若问题被改成一般位置版本，则难度显著上升，不能据此判断其可解。

### 免责声明

这不是对可能修正后 Erdős-Pach 一般位置版本的解答；这里只评估给定 JSON 中原始表述及其备注所指反例的 AI 可处理性。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `disproved`
- 状态信心: `high`
- 可行动性: `closed_verification_only`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_655.md](../../prompts/problem_655.md)

### 状态结论

按网页所写的字面命题，其真值已可由正 n 边形严格否定：正 n 边形满足“以配置中一点为圆心的任一圆至多含另外两点”，却仅确定 ⌊n/2⌋ 个全局不同距离。因此对任意 c>0，它都小于 (1+c)n/2。历史上原作者可能意图的附加一般位置/钉住距离版本并不唯一，不能把它们视为同一题。

### 当前规范陈述

字面上的全局版本：是否存在实常数 c>0 与整数 N，使得对每个 n≥N 和任意由 n 个互异平面点组成的集合 X={x_1,…,x_n}，若对所有 x∈X 及 r>0，满足 |{y∈X\{x}:‖x-y‖=r}|≤2（即任何以 X 中一点为圆心的圆至多含另外两点），则 X 所确定的全局不同两点距离数 |{‖x-y‖:x,y∈X,x≠y}| 至少为 (1+c)n/2？

```text
Literal global version. Does there exist a real constant c>0 and an integer N such that, for every integer n≥N and every set X={x_1,...,x_n} of n distinct points of R^2, if for every x∈X and r>0 one has |{y∈X\{x}: ||x-y||=r}|≤2, then |{||x-y||: x,y∈X, x≠y}|≥(1+c)n/2?
```

### 陈述、量词与反例审计

- 歧义严重度: `material`
- 简单反例检查: `counterexample_found`
- 检查说明: 取单位圆上的正 n 边形 X={exp(2πik/n):0≤k<n}。固定顶点 x_i 后，至 x_{i+m} 的距离为 2sin(πm/n)。在 1≤m≤⌊n/2⌋ 上该值严格递增，且仅有 m 与 n−m 给出同一距离；故每个以 x_i 为圆心的圆至多经过另外两个顶点，满足假设。所有边对的距离恰为 {2sin(πm/n):1≤m≤⌊n/2⌋}，数目为 ⌊n/2⌋。对任意 c>0 及任意 n≥1，⌊n/2⌋<(1+c)n/2，故不存在所称 c、N。
- 版本变化: 网页目前仍显示 OPEN，但同时在备注中记录 Hunter 的正多边形反例，并明确说原始来源含糊。2026 年论坛讨论将数据库记录标为“ambiguous statement”，而未指定唯一修复。Formal Conjectures 当前文件也把字面版本标为 answer(False)，另列带 InGeneralPosition 的独立开放变体；但其当前主分支定理本体为 sorry，不能把该文件本身当作已独立核验的 Lean 证明。2026-04 的非同行评议综述进一步区分：1987 年一般位置的 n/3 尺度问题、1988 年带无四点共圆限制的 A2 pinned n/2 问题，以及其他凸位置版本。

陈述问题：

- “determined between the x_i”按通常用法重构为全局不同的无序两点距离数；它不是“从某一点出发”的 pinned 距离数。这个区分对历史修复至关重要。
- 原文未明说 x_i 互异；“n 个点”及“three other points”的通常约定要求互异，且上述重构采用该约定。
- “no circle ... contains three other points”应量化为：对每个配置点 x 和每个正半径 r，等距于 x 的其他配置点至多两个。
- 原始来源的意图具有实质歧义：论坛提出一般位置与凸位置等不同修复；后者若保留 A2 条件仍被正多边形否定。不能擅自选择一个开放修复题替代字面命题。

需要固定的量词/约定：

- The intended asymptotic order is ∃c>0 ∃N ∀n≥N ∀X, not a constant c depending on n or X.
- The points are taken to be pairwise distinct.
- “Other points” excludes the centre x itself, and circles have radius r>0.
- The counted object is the global set of distance values over unordered distinct pairs; multiplicities are ignored.
- The conclusion uses a real lower bound, so the integer count is required to be at least the real number (1+c)n/2.

### 文献与当前边界

已核验的主要结果：

- 字面 A2 条件立刻给出每个 x 的至少 ⌈(n−1)/2⌉=⌊n/2⌋ 个 pinned 距离：将 n−1 个其他点按至 x 的距离分组，每组至多两个。因全局距离数不少于任一 pinned 距离数，D(X)≥⌊n/2⌋。
- 正 n 边形达到该下界：弦长按循环步长 m 的不同取值恰为 2sin(πm/n)，1≤m≤⌊n/2⌋，所以 D(X)=⌊n/2⌋。这给出字面问题的精确极值，而不只是一个渐近反例。
- 所检索的 2026 非同行评议综述称：若改为一般位置的全局问题，已知范围为约 n/3 至 n exp(C√log n)，而历史上较贴近 n/2 尺度的版本是 A2 加无四点共圆的 pinned 问题；这些是不同命题，且该文的历史/状态断言在本审计中仅作线索而非已完全证实的主结论。

最近相关工作：所找到的最近直接相关材料是 2026-04-22 的《Erdős Problem #655 and Its Natural Repairs》非同行评议 PDF；它把正多边形反例写成完整的弦长论证，并整理多种修复。未找到 2023–2026 年专门推翻该反例或解决一个由原网页唯一指定修复版本的同行评议论文或 arXiv 预印本。

剩余核心：字面命题没有剩余开放核心，精确最小值已由初等论证和正多边形闭合。真正未决的是历史意图：没有证据允许唯一地把 #655 改写为某一开放问题。若人类依据原始 1988 文献确认目标是“无四点共圆且 A2 时存在一个点有超过 (1+c)n/2 个 pinned 距离”，那将是一个需另行立项、另行查新的修复目标，而不是 #655 字面命题。

已使用方法：

- 按同心圆距离层分组的鸽巢原理。
- 正多边形的弦长公式与 sin 在 [0,π/2] 上的严格单调性。
- 对于候选修复，需首先核对其是全局距离 D(X)、最大 pinned 距离 M(X)，还是距离和；三者不可互换。

争议或不确定性：

- 网页 OPEN 标签与其备注中的明确反例相冲突；应以可检验的反例为准，视标签为尚未同步的数据库状态。
- 原始 Erdős/Pach 题目的确切表述和 #655 如何从原始文献转写而来没有在本审计中逐页核验，因此不能断言某一个修复就是作者意图。
- Formal Conjectures 文件注释链接到一个历史提交中的“supporting lemmas”，但本次无法检查该历史提交的可编译证明；且当前主分支主定理为 sorry。此不影响初等反例的正确性。

### 证据来源

- [Erdős Problems — Problem 655](https://www.erdosproblems.com/655) — Thomas F. Bloom / Erdős Problems database, date unknown; `problem_page`, `database_record`, directness=`direct`, reliability=`high`. 给出当前字面陈述；备注明确记录 Zach Hunter 的“正 n 边形”反例、原始来源含糊以及可能的一般位置修复。页面自身也警告 OPEN 标签只是维护者信念，不能压倒反例。
- [Erdős Problems — LaTeX source for Problem 655](https://www.erdosproblems.com/latex/655) — Thomas F. Bloom / Erdős Problems database, date unknown; `problem_page`, `database_record`, directness=`direct`, reliability=`high`. 独立呈现了与问题页一致的字面 LaTeX 陈述及正多边形反例备注。
- [655 Discussion Thread | Erdős Problems](https://www.erdosproblems.com/forum/thread/655) — Przemek Chojecki, Neel Somani, Nat Sothanaphan, Thomas Bloom, Terence Tao, and forum participants, 2026-01-19 to 2026-04-22; `forum`, `informal_claim`, directness=`direct`, reliability=`medium`. 论坛确认数据库已加上“ambiguous statement”标记；讨论中的一般位置与凸位置只是候选修复，且 Bloom 明确不愿猜测唯一意图。论坛还链接了一份非同行评议的变体综述。
- [Formal Conjectures — Erdős Problem 655](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/655.lean) — Formal Conjectures Authors, 2026; `formalization`, `formalized_artifact`, directness=`direct`, reliability=`medium`. 形式化文件准确编码了 A2 局部条件和量词结构，并在注释中陈述正 n 边形反例；但当前主分支的 erdos_655 定理以 sorry 结束，因此该可见版本不能作为完整机器核验的证明证据。
- [Erdős Problem #655 and Its Natural Repairs: Exact Resolutions, Historical Sources, and Open Variants](https://www.ulam.ai/research/erdos655-overview.pdf) — Author not stated in the inspected PDF; linked from a forum post by Przemek Chojecki, 2026-04-22; `preprint`, `informal_claim`, directness=`direct`, reliability=`medium`. 给出可检查的正 n 边形弦长计算，并把字面 A2 全局问题与 1987/1988 年的不同问题分开；其关于历史对应、开放状态和文献优先级未逐篇由本审计核验。
- [Paul Erdős publication list](https://sites.math.rutgers.edu/~sg1108/People/Math/Erdos) — Rutgers-hosted Erdős bibliography, date unknown; `secondary_index`, `database_record`, directness=`indirect`, reliability=`medium`. 书目记录确认 P. Erdős 1988 年《Some old and new problems in combinatorial geometry》收于 Applications of Discrete Mathematics, pp. 32–37；它只支持书目信息，而非本审计对该文具体问题表述的独立验证。
- [Intuitive Geometry (Siófok, 1985) table of contents](https://www.bolyai.hu/files/kotetek_48_1987.pdf) — Colloquia Mathematica Societatis János Bolyai, 1987; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`medium`. 目录确认 P. Erdős 的《Some combinatorial and metric problems in geometry》刊于该卷第 167 页起；本次未逐页检查其具体定理或问题文本。

### 完成标准

- 肯定出口: For the literal audit target, verify a family X_n for arbitrarily large n such that (i) X_n has n distinct points, (ii) every circle centred at a point of X_n contains at most two other points of X_n, and (iii) D(X_n)<(1+c)n/2 for every fixed c>0. The regular n-gons satisfy all three conditions, so this condition is met.
- 否定出口: Overturn the claimed disproof only by locating an error in either the A2 verification or the exact count D(X_n)=floor(n/2), or by showing from a primary source that the audited literal statement is not the proposition actually meant to be evaluated. The latter changes the historical target but does not make the literal proposition true.

不构成完成：

- Merely repeating the database's OPEN label or an unverified forum claim.
- Showing the weaker lower bound D(X)≥floor(n/2); it is compatible with the counterexample.
- Checking one polygon size or numerical chord lengths without proving the all-n construction.
- Proving a result for a selected repaired condition while silently replacing the literal target.
- Treating a Lean declaration containing sorry as a completed formal proof.

正确性陷阱：

- Use global D(X), not the pinned count d_X(x) or its maximum, unless explicitly auditing a repaired variant.
- For even n, the antipodal step m=n/2 occurs once; all other nonzero chord-length classes occur in pairs. This still gives exactly floor(n/2) values.
- The local hypothesis concerns circles centred at vertices, not arbitrary circles through vertices.
- The strict inequality needed for disproof is floor(n/2)<(1+c)n/2 for every c>0; it holds for every n≥1.
- Do not infer that 'no three collinear' or convex position repairs the literal problem: regular polygons satisfy both.
- No-four-cocircularity excludes regular polygons, but it is an additional condition and does not identify whether the intended quantity was global or pinned.

### 更新后的 AI 可解答性

- 等级: `not_applicable_closed_or_invalid`
- 分数: `0/100`
- 信心: `high`
- 结论: 字面命题已被一个可完全手算、可逐项验证的无穷反例族否定；AI 研究求解评分不适用。

支持理由：

- 正 n 边形同时满足局部 A2 条件并只给出 ⌊n/2⌋ 个全局距离，直接否定任何固定正增益 c。
- 问题页、论坛和一份近期综述都记录同一反例；审计还独立展开了所需弦长计算。

主要障碍：

- 若改做“作者真正意图”的研究，首先面临不是证明技术而是无法唯一确定目标的史料问题。
- 当前可见形式化主定理含 sorry，不能代替独立的证明检查。

Proof-first 路线：

- 仅保留验证路线：形式化或逐行审查正多边形的 A2 性质、弦长分类和量词否定。
- 若获得并核对原始文献，再单独建立一个有明确对象（global/pinned/sum）和附加条件的修复问题记录；不得从本题自动继承。

需要验证：

- 如需发布“原作者意图”的判断，人工取得并逐页核对 Erdős 1987、1988 原文及 #655 的转录链。
- 如需声称机器验证，检查被注释链接的历史提交是否无 sorry、可在固定依赖下编译，且其定义与本审计的字面命题相同。

### 审计限制与人工复核理由

- 本审计严格判定的是可唯一重构的网页字面命题；没有逐页取得并核对 1987、1988 年原始印刷文献，故不对作者的历史意图作最终断言。
- 未能检查 Formal Conjectures 注释所链接历史提交的实际无 sorry 编译证明；可见主分支文件本身有 sorry。该限制不影响已完全展开的初等反例。
- 对近三年文献的检索未发现专门改变字面反例结论的同行评议工作；检索未命中不是不存在文献的逻辑证明。
- 2026-04 Ulam PDF 是有用的变体地图，但其作者信息、历史溯源和开放状态没有在本审计中逐一以原始论文交叉验证。

- 若数据库需要从 OPEN 改为 CLOSED/DISPROVED，应由维护者确认字面重构及状态迁移；反例本身已经足够明确。
- 若要建立后续开放问题，必须由熟悉原始文献的人确定要审计的修复版本，特别是 global 与 pinned、A2 与无四点共圆条件的区别。
- 若要宣称“已形式化证明”，需人工或可复现 CI 核验所链接历史 Lean 提交，而不是依赖当前含 sorry 的页面。

<!-- DEEP_REVIEW:END -->
