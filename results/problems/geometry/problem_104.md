# Problem 104

## 基本信息

- 原始链接: https://www.erdosproblems.com/104
- LaTeX 页面: https://www.erdosproblems.com/latex/104
- 原始状态: `open`
- 奖金: `$100`
- 主类别: `geometry`
- 原始标签: `geometry`
- 形式化状态: `no`
- OEIS: `A003829`
- 原站备注字段: 无

## 原问题

Given $n$ points in $\mathbb{R}^2$ the number of distinct unit circles containing at least three points is $o(n^2)$.

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `23/100`
- 建议路线: 优先提取等价表述、尝试特殊情形、寻找可计算子问题，再决定是否进入证明搜索。

## 判断依据

### 有利因素

- 存在 OEIS 数据入口，利于实验与反例搜索

### 主要障碍

- 所属标签偏证明密集：geometry
- 题面含渐近/无限对象线索：\gg, o(
- 原记录含奖金 $100，说明该题被长期视为高价值难题；这不是否定依据，但提高验证门槛。
- 缺少明显有限搜索入口。

### 公开版思考过程摘要

- 先识别问题类型：无限/渐近或抽象证明倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: geometry
- 有限/计算线索: 无
- 渐近/无限线索: \gg, o(
- 构造/存在性线索: construct

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **中等候选。GPT-5.5 级别模型配合文献检索、计算搜索和形式化检查，较可能给出有价值的结构化推进，例如统一已有构造、排除若干极端配置、验证小规模最优值或提出可证明的条件性子二次上界；但直接证明一般情形的 o(n^2) 仍很不稳，因为它要求突破当前简单二次双计数界，且已知 n^{3/2} 构造说明不能靠粗糙稀疏化解决。**
- 等级: `medium_candidate`
- 分数: `58/100`
- 信心: `medium`
- 可能路线: 较现实的路线不是直接蛮力证明，而是把问题转写为单位圆三点共圆配置的极值超图/ incidence 问题：先按圆上点数分层，处理富圆与稀圆；再研究若接近二次多圆会强迫大量受限距离、重复弦长或近网格结构；同时用计算搜索和 SAT/SMT/整数规划验证小 n 与特殊族，寻找反例机制或稳定性猜想。若能证明任何接近 cn^2 的配置必含某种不可能的局部模式，就可能得到子二次改进。

### 支持理由

- 问题表述短且结构清楚，适合模型把几何问题转成组合计数、单位距离图、圆-点关联和三元超图语言。
- 已有上界来自非常简单的双计数，说明存在明确的改进目标：只需排除正比例于 n^2 的三点单位圆即可证明 o(n^2)。
- 已有下界为约 n^{3/2}，给模型提供了可分析的候选极值结构，有利于判断哪些证明策略过强或不可能。
- 计算工具可枚举小规模配置、格点/代数点族和随机扰动族，帮助发现接近极值的结构模式或验证 OEIS 小项。
- 形式化证明工具可用于核查局部几何引理，例如两点决定至多两个单位圆、特定局部配置不可同时满足等，降低复杂几何论证中的错误率。

### 主要障碍

- 核心难点是从 O(n^2) 降到 o(n^2)，这通常需要全局结构定理，而不是单个局部双计数改良。
- 三点在同一单位圆上的条件比普通单位距离或一般圆关联更刚性但也更非线性，标准 Szemeredi-Trotter 型界未必直接给出所需强度。
- 接近 n^{3/2} 的构造可能具有精细代数或格点结构，模型容易提出被这些构造立即否定的过强猜想。
- 如果存在非常稀疏但全局交织的近二次候选，单纯小 n 搜索很难发现，也难以外推。
- 问题尚未形式化，完整证明需要严谨处理退化情形、重合圆、圆上多点和一般位置以外的配置。

### 需要的验证

- 系统检索并核对题目备注中提到的 Erdős、Elekes、Harborth-Mengerson 结果，确认当前最佳上下界和是否已有后续改进。
- 复现 n^{3/2} 级构造，检查其圆上点数分布、距离分布和可推广参数。
- 对小 n 或受限点集类别进行精确搜索，验证 OEIS 数据与候选极值配置。
- 把任何拟议证明分解成局部几何引理、组合计数引理和结构稳定性命题，并分别用符号计算或交互式定理证明器核查。
- 特别测试所有中间断言是否被 Elekes 型构造、格点构造、圆簇构造或高重合度配置反驳。

### 公开版思考摘要

这个问题对 AI 有吸引力，因为目标、已知平凡上界和非平凡下界都很明确，而且工具可以在文献、计算搜索和形式化局部几何上发挥作用。可是一般性 o(n^2) 结论需要排除所有近二次规模的三点单位圆配置，这更像一个深层 incidence/组合几何结构问题。GPT-5.5 级别模型更可能产生可验证的局部推进、特殊情形证明或新猜想，而不是可靠地一次性完成最终证明。

### 免责声明

以上是 AI 可攻克性审查，不是该 Erdős 问题的证明或反例；其中路线和障碍均需独立数学验证。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `likely_open`
- 状态信心: `medium`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_104.md](../../prompts/problem_104.md)

### 状态结论

截至 2026-07-27，原命题看来仍为开放问题：当前 Erdős Problems 页面明确标作 OPEN，问题论坛没有任何解答或部分解答主张；针对精确表述、三重交点表述及 2023--2026 年文献的检索未发现可核验的解决或反例。此结论不是“未找到即不存在”的证明，故定为 likely_open 而非 confirmed_open。

### 当前规范陈述

设 P⊂R² 为由 n 个互异点组成的有限点集。令 U(P) 为所有半径恰为 1、且圆周上至少含 P 中三个点的互异欧氏圆的集合，并令 f(n)=max_{|P|=n}|U(P)|。证明 f(n)=o(n²)；等价地，对每个 ε>0，存在 N(ε)，使得对每个整数 n≥N(ε) 及每个 n 点集 P⊂R²，均有 |U(P)|≤εn²。

```text
For a finite set P⊂R² of n distinct points, let U(P) be the set of distinct Euclidean circles of radius exactly 1 whose circumferences contain at least three points of P. Define f(n)=max_{|P|=n}|U(P)|. Prove that f(n)=o(n²); equivalently, for every ε>0 there is N(ε) such that for every integer n≥N(ε) and every n-point set P⊂R², |U(P)|≤εn².
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 未发现能否定字面命题的简单构造。对任意 P，每对点至多位于两个单位圆上；把每个被计单位圆的至少三对点双计数，立即得 |U(P)|≤n(n−1)/3。这只给二次上界，不足以证明 o(n²)，也不构成反例。
- 版本变化: 未见原命题被正式改写或分裂。Erdős 还悬赏更强的 O(n^{3/2}) 上界；它严格强于本题的 o(n²)，不能把该较强猜想当作本题的等价表述。文献中的“三个固定点所穿过的三族单位圆的三重交点”是受限的相关问题，不是本题的全局两参数单位圆族。

陈述问题：

- 原文的“Given n points”按组合几何惯例应指 n 个互异点；须明说，否则“点集”与允许重数的点列不同。
- 小 o 必须量化为对所有 n 点配置一致成立的渐近上界，而非对某一固定点集族的逐项陈述。
- “unit circle”须固定为欧氏半径恰为 1 的圆周；计数对象是互异圆，而非其所含三点组。一个圆若含 k≥3 个点，仍只计一次。

需要固定的量词/约定：

- P ranges over all finite subsets of R² with |P|=n; its elements are distinct.
- A circle is counted once by its centre (equivalently, by equality as subsets of R²), even if it contains more than three points of P.
- The little-o assertion is uniform in P: ∀ε>0 ∃N ∀n≥N ∀P with |P|=n, |U(P)|≤εn².
- No general-position hypothesis is part of Problem 104. Historical questions imposing general position are separate variants.

### 文献与当前边界

已核验的主要结果：

- Erdős（1981，问题页所引原始文献）给出平凡的 O(n²) 上界；直接的精确双计数为 |U(P)|≤n(n−1)/3：每个被计圆贡献至少 3 个点对，而每点对至多确定 2 个单位圆。
- Elekes（1984，同行评审）构造出 Ω(n^{3/2}) 个所求单位圆；故任何正确渐近上界必须至少为该量级。
- Harborth 与 Mengersen（1986，同行评审）确定了 n≤7 的极值；OEIS A003829 还列出 n=8 的记录值。有限 n 数据不能判定小 o。
- Elekes--Simonovits--Szabó（2009，同行评审）及 Raz--Sharir--Solymosi（2015，同行评审）得到的是固定锚点的三族一参数单位圆问题的次二次界，后者为 O(n^{11/6})；这不是对一般单位圆排列的上界。

最近相关工作：检索到的较新、可核验的相关方法工作为 Solymosi--Zahl 的 2022 预印本（后见 JCTA 2024 书目记录）《Improved Elekes-Szabó type estimates using proximity》，其一般实代数笛卡尔积估计为 O(N^{12/7})（有群型例外）。未检得 2023--2026 年直接证明或反驳 Problem 104 的论文。

剩余核心：证明或反驳：不存在一列 n 点集 P_n 使 |U(P_n)|≥c n²（某固定 c>0）。更强但未必要的目标是将全局上界降至 O(n^{3/2})，与 Elekes 下界匹配。

已使用方法：

- 点对--圆双计数与 K_{2,3}-型禁止结构：给出 O(n²)，但没有次二次节省。
- Elekes 的和集式/一般单位向量构造：产生约 n^{3/2} 个三重交点或等价的支持单位圆。
- Elekes--Szabó 型代数曲面、参数化与包络方法：在三族一参数、固定锚点情形有效。
- Raz--Sharir--Solymosi 的曲线关联和入射几何：给出固定锚点三族的 O(n^{11/6})。
- Solymosi--Zahl 的 proximity 型 Elekes--Szabó 方法：为受控代数参数问题提供更强的一般工具，但尚无将其全局化到本题的验证。

争议或不确定性：

- 当前数据库维护者仍标 OPEN，但明确其状态不是完备文献证明；故本审计采用 likely_open、medium，而非声称确定开放。
- 2009/2015 年三族固定锚点结果很容易因“单位圆三重交点”的表面相似性被误报为本题的解；其参数空间和量词均更受限。
- 2026 年关于平面单位距离问题的新闻和预印本不解决本题；两题的对象分别是单位距离边与三点支持的单位圆。

### 证据来源

- [Erdős Problem 104](https://www.erdosproblems.com/104) — Thomas F. Bloom / Erdős Problems database, date unknown; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 页面当前标记 OPEN，给出本题表述、Erdős 的 O(n²) 上界、Elekes 的 Ω(n^{3/2}) 构造、Harborth--Mengersen 的 n(n−1)/3 计数改进，以及较强的 O(n^{3/2}) 悬赏目标。该站也明确警告状态是维护者的当前判断，仍应自行检索文献。
- [104 Discussion Thread | Erdős Problems](https://www.erdosproblems.com/forum/thread/104) — Erdős Problems forum, date unknown; `forum`, `informal_claim`, directness=`direct`, reliability=`medium`. 该问题线程显示“没有在评论中主张的完整或部分解答”；现有评论只涉及奖金货币和补充历史出处，未出现可审查的解决声称。
- [n points in the plane can determine n^{3/2} unit circles](https://dblp.org/rec/journals/combinatorica/Elekes84) — György Elekes, 1984; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 书目记录确认 Elekes 1984 年 Combinatorica 4(2--3), p.131 的构造性论文；结合当前问题页的说明，它给出 Ω(n^{3/2}) 个所求单位圆的下界。
- [Point sets with many unit circles](https://www.sciencedirect.com/science/article/pii/0012365X86900117) — Heiko Harborth; Ingrid Mengersen, 1986; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 期刊页面确认论文、作者、卷期及页码（Discrete Mathematics 60, 193--197），并说明其确定 n≤7 的极值。问题页归因其指出三对点双计数给出 n(n−1)/3。
- [A003829: Maximal number of unit circles through n points in plane, each circle containing 3 of the points](https://oeis.org/A003829) — N. J. A. Sloane / OEIS Foundation, date unknown; `oeis`, `database_record`, directness=`direct`, reliability=`medium`. 确认该序列所记录的正是本题有限 n 极值，并列出 n=3 至 8 的已知项及 Harborth--Mengersen 文献链接；它不是渐近解决的证据。
- [A Combinatorial Distinction Between Unit Circles and Straight Lines: How Many Coincidences Can they Have?](https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/abs/combinatorial-distinction-between-unit-circles-and-straight-lines-how-many-coincidences-can-they-have/3DD2B9E8C08472D387681246B949DA0F) — György Elekes; Miklós Simonovits; Endre Szabó, 2009-09-01; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 该文证明的是一参数曲线族在附加包络条件下的三重交点次二次界，并以带固定穿过点的单位圆族为应用；其结果不可直接推广为本题对任意 n 个单位圆的结论。
- [On triple intersections of three families of unit circles](https://arxiv.org/abs/1407.6625) — Orit E. Raz; Micha Sharir; József Solymosi, 2014-07-24; `preprint`, `preprint`, directness=`indirect`, reliability=`high`. 预印本的定理 3 对三个各自穿过一个固定点的单位圆族给出 O(n^{11/6}) 三重交点界。该工作后来以 2015 年同行评审论文发表；它是严格受限的相关问题，不能作为 Problem 104 的解答。
- [On Triple Intersections of Three Families of Unit Circles](https://cris.huji.ac.il/en/publications/on-triple-intersections-of-three-families-of-unit-circles-13/) — Orit E. Raz; Micha Sharir; József Solymosi, 2015-10-13; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 大学研究门户确认该受限三族结果发表于 Discrete & Computational Geometry 54(4), 930--953，且为同行评审；摘要清楚限定每族圆都穿过给定点。
- [Improved Elekes-Szabó type estimates using proximity](https://arxiv.org/abs/2211.13294) — József Solymosi; Joshua Zahl, 2022-11-23; `preprint`, `preprint`, directness=`indirect`, reliability=`high`. 给出实数上的一般 Elekes--Szabó 型界 O(N^{12/7})（除非存在群型特殊结构），是与受限三参数/笛卡尔积方法相关的较新工具；论文摘要未声称解决本题。

### 完成标准

- 肯定出口: Provide a complete proof that for every ε>0 there exists N(ε) such that every n≥N(ε) and every n-point set P⊂R² span at most εn² distinct radius-1 circles containing at least three points.
- 否定出口: Provide a fixed c>0 and an infinite sequence of finite point sets P_j⊂R² with |P_j|→∞ such that |U(P_j)|≥c|P_j|², with a complete verification that the counted circles are distinct, radius 1, and each contains at least three points of P_j.

不构成完成：

- Re-deriving O(n²), n(n−1)/3, or any fixed-density upper bound c n² with c>0.
- Giving a lower bound, including Ω(n^{3/2}), without a quadratic construction.
- Proving a bound only for a fixed-anchor three-family, a one-parameter subfamily, generic configurations, lattice configurations, or a bounded range of n.
- Finite computation without a theorem that converts its output into one of the two asymptotic alternatives.
- Proving the stronger O(n^{3/2}) claim only conditionally, or asserting it from numerical data.

正确性陷阱：

- Count circles, not triples: a circle containing k≥4 points has many supporting triples but contributes only one to |U(P)|.
- In a dual formulation, map each input point p to the unit circle centred at p. A circle centred at x through at least three input points corresponds to a 3-rich intersection point x; prove this correspondence preserves distinctness and handles higher multiplicities.
- Do not import an incidence theorem for arbitrary points and unit circles unless its hypotheses and its relation to the number of 3-rich points are explicitly established.
- A fixed exponent n^{2−δ} with δ>0 would settle the problem, even if δ is tiny; a merely improved constant times n² would not.
- Check uniformity in all n-point sets and make the little-o quantifiers explicit.

### 更新后的 AI 可解答性

- 等级: `low_candidate`
- 分数: `8/100`
- 信心: `medium`
- 结论: 这是定义清楚、可被严格验算的开放目标，但其核心障碍已持续约四十年，且现有一般工具仍停在二次上界；对 AI 而言属于低概率研究候选，而非适合主要依赖枚举的题目。

支持理由：

- 目标具有明确的肯定/否定终止条件，且双计数、对偶三重交点和已有下界提供可验证的基线。
- 相关受限问题已有成熟的代数--入射方法，可能帮助识别可推广的结构性障碍。
- 任何真正的固定幂次节省 n^{2−δ} 都已足以完成原题，故中间引理可有清晰的成功判据。

主要障碍：

- 一般单位圆族是两参数族；已知固定锚点的一参数三族结果不能直接覆盖它。
- 纯粹的“每对点至多两个圆”组合性质允许二次规模，必须利用尚未被充分捕获的欧氏几何结构。
- 下界 Ω(n^{3/2}) 与二次上界间差距大，且没有已验证的全局非平凡上界。
- 小 n 极值搜索容易制造误导，不能替代一致的渐近论证。

Proof-first 路线：

- 先尝试证明结构性归约：若 |U(P)|≥c n²，则点--圆三重关联迫使某个可精确定义的一参数退化或加法型结构；再证明该结构与固定半径 1 不相容，或从中抽取受限三族子配置。
- 研究支持圆的三均匀超图与圆心参数间的兼容条件，目标是排除近似 Steiner 型二次三元系统，而不是只重复 pair-codegree≤2。
- 尝试以分层/富圆剥离把高重数圆和恰三点圆分开；每个分支都须给出能累加至 o(n²) 的明确损失。
- 仅可选一个计算任务：在提出具体结构引理后，有限搜索可检验其最小反例或生成精确反例证书；须事先写明假设、搜索空间、输出证书和停止条件。

需要验证：

- 对所有声称将固定锚点三族结果推广到任意单位圆族的步骤做逐量词核验。
- 若发现近年预印本或论坛解答，必须取得完整证明或形式化工件，而非依赖摘要、搜索片段或声誉。
- 核查任何对偶变换是否保持半径、三重性和“不同圆只计一次”的计数。
- 若使用计算，独立复算坐标、距离、圆的互异性及全部候选圆的完备枚举。

### 审计限制与人工复核理由

- Erdős Problems 的开放标签是有价值但非完备的数据库判断；网站自身明确提醒可能遗漏文献。
- 已对精确短语、等价的三重交点语言、主作者和 2023--2026 年工作进行定向网页/预印本搜索，但没有穷尽付费索引、MathSciNet、zbMATH 或全部引用网络。
- Elekes 1984 原文的可访问页面主要为书目记录；其下界的具体构造细节未在本审计中逐行复核。
- 未发现 Problem 104 论坛中的解答声称；这只排除了该线程中可见的主张，不排除其他平台的未索引材料。

- 若将审计用于发布“已确认仍开放”的正式结论，应由熟悉离散几何的人工复核 MathSciNet/zbMATH 和近年引文链，以降低数据库和搜索覆盖遗漏的风险。
- 研究启动前应人工确认 2026 年单位距离相关工作没有产生可迁移到三重单位圆问题的新全局定理；本审计已将两者严格区分，但该领域术语相近。

<!-- DEEP_REVIEW:END -->
