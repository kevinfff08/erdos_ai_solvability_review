# Problem 103

## 基本信息

- 原始链接: https://www.erdosproblems.com/103
- LaTeX 页面: https://www.erdosproblems.com/latex/103
- 原始状态: `open`
- 奖金: `no`
- 主类别: `geometry`
- 原始标签: `geometry`, `distances`
- 形式化状态: `no`
- OEIS: `possible`
- 原站备注字段: 无

## 原问题

Let $h(n)$ count the number of incongruent sets of $n$ points in $\mathbb{R}^2$ which minimise the diameter subject to the constraint that $d(x,y)\geq 1$ for all points $x\neq y$. Is it true that $h(n)\to \infty$?

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `21/100`
- 建议路线: 优先提取等价表述、尝试特殊情形、寻找可计算子问题，再决定是否进入证明搜索。

## 判断依据

### 有利因素

- 目前只能依靠通用数学推理、文献归纳和特殊情形探索

### 主要障碍

- 所属标签偏证明密集：distances, geometry
- 题面含渐近/无限对象线索：for all large
- 缺少明显有限搜索入口。

### 公开版思考过程摘要

- 先识别问题类型：无限/渐近或抽象证明倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: distances, geometry
- 有限/计算线索: 无
- 渐近/无限线索: for all large
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5 + computation/formalization/literature/search tools`
- 结论: **低到中等候选。GPT-5.5 级别模型有机会显著推进有限 n 的计算验证、候选极值构型分类、反例搜索和局部最优性证明，但直接完成“h(n) 是否趋于无穷”的全局证明概率不高。**
- 等级: `low_to_medium_candidate`
- 分数: `42/100`
- 信心: `medium`
- 可能路线: 较现实的路线是把问题转化为有限点集的最小直径 packing/diameter 优化：先用非线性优化、图约束枚举和 interval/SMT 证明工具，对给定 n 枚举所有候选接触图与最小直径构型；再尝试从大量 n 的最优构型中抽取可证明的族，尤其寻找导致多个非全等极小构型的边界或壳层自由度；最后把局部刚性、排除证书和构造族形式化。若能证明某些宽区间或无限序列上 h(n) 有可控下界，已经是有意义推进。

### 支持理由

- 问题陈述短、目标明确，适合建立计算管线：输入 n，输出最小直径候选、非全等分类、接触图和可验证证书。
- 约束是代数/半代数型：点间距离至少 1、直径最小化、全等判别，原则上可结合非线性优化、分支定界、区间算术和形式化验证。
- AI 模型可在候选构型搜索、自动生成接触图、识别模式、写验证脚本和提炼可证明构造族方面发挥较强作用。
- 备注显示连 h(n) 是否最终至少为 2 都未知，这意味着寻找单个无限多样性机制或反例方向都可能构成实质推进。

### 主要障碍

- 核心难点是全局最优性：必须排除所有连续平面构型，而不仅是优化器找到的候选。
- h(n) 计数的是非全等的最小直径构型；即使最小直径数值已知，完整分类所有极小构型也可能比求数值更难。
- 局部最优、数值近似和图枚举容易产生假阳性，需要严格证书才能支持数学结论。
- 目标是 h(n) 趋于无穷，要求随 n 增长的统一机制，而不是零散小规模计算。
- 问题属于离散几何中的开放极值分类问题，缺少明显可由现有自动定理证明直接闭合的标准形式。

### 需要的验证

- 为每个计算得到的最优构型生成可独立检查的坐标区间、距离约束和直径上界证书。
- 为排除其他构型，需要接触图枚举完整性证明或等价的分支定界/interval 证书。
- 需要严格的非全等判别，包括处理对称、重标号和数值误差。
- 若提出无限构造族，需要证明其直径达到全局最小，而非只是满足距离约束的好构型。
- 若声称 h(n) 下界增长，需要给出适用于无限多个或最终所有 n 的统一论证，并最好形式化关键几何不等式。

### 公开版思考摘要

这个问题对 AI 辅助很适合做“计算发现加严格证书”的推进：模型可以把几何问题工程化，搜索大量 n 的最优 packing，分类非全等构型，并尝试抽象出可证明模式。但题目要求的是渐近非唯一性，且当前备注表明连最终至少两个最优构型都未知；这把任务从数值优化推到全局分类和统一渐近证明。因此我判断它不是高概率可直接解决的问题，但有中等价值的可推进空间。

### 免责声明

以上只是对 GPT-5.5 级别模型辅助研究可行性的审查，不是该 Erdős 问题的证明、反例或求解。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `confirmed_open`
- 状态信心: `medium`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_103.md](../../prompts/problem_103.md)

### 状态结论

截至 2026-07-27，题库当前页直接标为 OPEN，说明尚未知对充分大 n 均有 h(n)≥2，且页面显示 0 条问题评论、无已声称的部分或完整解。对原表述、作者、关键短语、Bezdek–Fodor 论文和近三年 arXiv 检索均未发现可核查的解或反例。故将其列为已确认仍开放，但置信度为中等：题库明确提示其开放标签是站长的当前判断，并非穷尽性文献证明。

### 当前规范陈述

对每个整数 n≥2，令 D(n) 为所有满足 |A|=n 且任意不同 x,y∈A 都有 ||x-y||≥1 的平面点集 A 的直径 diam(A)=max{||x-y||:x,y∈A} 的下确界。令 M_n 为达到 D(n) 的全部 n 点集；若两个点集相差一个平面欧氏等距变换（包括反射），则视为全等。令 h(n)=|M_n/Isom(R²)|（如有必要按扩展基数理解）。问：是否对每个整数 K 都存在 N，使全部 n≥N 均满足 h(n)≥K？

```text
For each integer n >= 2, let D(n) = inf { diam(A) : A is a subset of R^2, |A| = n, and ||x-y|| >= 1 for all distinct x,y in A }, where diam(A) = max { ||x-y|| : x,y in A }. Let M_n be the family of all n-point sets attaining D(n), and identify two members of M_n when one is the image of the other under a Euclidean isometry of R^2 (including reflections). Define h(n) = |M_n / Isom(R^2)|, interpreted as an extended count if necessary. Does h(n) tend to infinity, i.e. for every integer K there is N such that h(n) >= K for every n >= N?
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 未发现能否定该渐近命题的简单构造。小 n 的唯一性或多重性均不足以决定“对所有充分大 n”的量词；刚体运动已由全等关系取商，缩放也不能制造另一最优构型。此结论仅为针对性检查结果，并非对所有构造的穷尽证明。
- 版本变化: 未发现原题被撤回、修订或拆分为非等价后继命题的证据。题库将 #99 列为“See also”，但该题是相关而非替换版本。当前页仍以原问题为 OPEN，并显示没有评论中的解答声称。

陈述问题：

- 原句未显式定义 diameter、全等所允许的变换、n 的起点，以及 h(n) 在最优构型族可能无限时的值域；这些均可按离散几何的标准约定补全，未发现会改变题意的致命歧义。
- “minimise”是对所有满足弱分离约束 d(x,y)≥1 的 n 点集作全局最小化，不是局部最小、圆内装填，亦不是只在三角格点中最小化。
- 关联问题 #99 的“最优点集含单位等边三角形”是不同命题；其 n=4 反例不构成本题 h(n)→∞ 的反例。

需要固定的量词/约定：

- The asymptotic quantifier is over every sufficiently large integer n, not merely an infinite subsequence.
- Congruence should mean the full Euclidean isometry group; quotienting only by orientation-preserving motions would change h(n) when a minimizer is chiral.
- The separation inequality is weak (>= 1). No replacement by a lattice-restricted or circle-container problem is licensed.
- A rigorous treatment should state whether h(n) is a natural number or an extended cardinal; the displayed limit is read in the lower-bound sense.

### 文献与当前边界

已核验的主要结果：

- Erdős（1994）在 Mathematica Pannonica 的问题文中提出该题；当前题库引为 [Er94b]。
- Bezdek 与 Fodor（1999，同行评审）研究同一约束下最小直径 D(n)，而非 h(n) 的增长。其摘要报告：D(n) 至 n=6 易于精确求出，Bateman–Erdős 已有 D(7)=2，本文确定 D(8)。这给出有限 n 的最优值背景，但不推出任意 h(n) 下界。
- 当前 #103 页的最强直接现状说明仍是：甚至尚未知是否对所有充分大的 n 都有 h(n)≥2；页面没有评论中的部分或完整解答声称。
- #99 的页面将三角格点截圆盘的渐近最优直径背景及 Erdős 的格点交叠猜想列为相关结构线索；这些不是 h(n)→∞ 的已证结果。

最近相关工作：未检到 2023–2026 年直接证明或反驳 h(n)→∞ 的论文、arXiv 预印本或形式化产物。最新可直接核验的现状记录是当前 Erdős Problems #103 页面；这只是负面检索结果，不应解释为不存在未索引文献的证明。

剩余核心：证明或否证：最小直径的单位分离 n 点集在欧氏全等意义下的最优构型数 h(n)，是否对每个充分大的 n 都任意大。已知的 D(n) 数值或渐近密度信息本身不能控制恰好达到最优值的构型数。

已使用方法：

- 有限点集装填/最小直径的精确几何分析，用于确定 D(n) 的小 n 值。
- 平面最密堆积与三角格点的渐近密度比较，可约束近似最优或最优构型的宏观形状。
- 若要从有限 n 推进 h(n)，需要全局最优性与非全等性的严格证书；纯数值优化或展示局部极小值不足。

争议或不确定性：

- 题库明确警告其开放标签反映站长判断，可能遗漏文献；本审计未发现冲突来源，但不能从“未检到”逻辑推出绝对无解。
- Bezdek–Fodor 论文的摘要可访问，但本次未能在出版商页面读取全文；所归因的结论严格限于摘要明确给出的 D(n) 结果。
- 未发现 #103 专属论坛讨论串；当前问题页显示 0 条评论和无声称解答。

### 证据来源

- [Erdős Problem #103](https://www.erdosproblems.com/103) — Thomas F. Bloom (database editor), date unknown; `problem_page`, `database_record`, directness=`direct`, reliability=`high`. 给出当前原题、OPEN 标签、Er94b 来源、无评论中已声称部分或完整解的记录，以及“尚不知充分大 n 时 h(n)≥2”的现状说明。页面同时明确开放标签只是站长当前判断。
- [Erdős Problems LaTeX page for #103](https://www.erdosproblems.com/latex/103) — Thomas F. Bloom (database editor), date unknown; `problem_page`, `database_record`, directness=`direct`, reliability=`high`. 可核对题目 LaTeX 原文及其唯一备注：未知充分大 n 时 h(n)≥2，并关联 #99。
- [Some problems in number theory, combinatorics and combinatorial geometry](https://eudml.org/doc/232764) — Paul Erdős, 1994; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 确认 Er94b 的作者、期刊、卷期和页码（Mathematica Pannonica 5(2), 261–269），即本题所列原始问题来源。
- [Some Problems in Number Theory, Combinatorics and Combinatorial Geometry](https://mathematica-pannonica.ttk.pte.hu/articles/mp05-2/mp05-2-261-269.pdf) — Paul Erdős, 1994; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 原论文的公开 PDF；检索结果确认其为 1994 年的开放问题论文。
- [Minimal Diameter of Certain Sets in the Plane](https://www.sciencedirect.com/science/article/pii/S0097316598928898) — András Bezdek, Ferenc Fodor, 1999-01; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 该文研究相同的最小直径函数 D(n)，摘要称精确值易得至 n=6，Bateman–Erdős 已证 D(7)=2，本文确定 D(8)。它不声称计算或证明 h(n) 的渐近行为。
- [Erdős Problem #99](https://www.erdosproblems.com/latex/99) — Thomas F. Bloom (database editor), date unknown; `problem_page`, `database_record`, directness=`indirect`, reliability=`medium`. 说明 #99 是关于同一最小直径构型的不同问题，并将 Bezdek–Fodor 工作描述为小 n 行为的研究；亦记录三角格点/圆盘的渐近背景为相关启发而非 #103 的证明。
- [teorth/erdosproblems database](https://github.com/teorth/erdosproblems) — Erdős Problems community, date unknown; `secondary_index`, `database_record`, directness=`direct`, reliability=`medium`. 当前公开数据库表将 #103 列为 open、not formalized、标签 geometry/distances；作为独立数据库记录与当前问题页相符。

### 完成标准

- 肯定出口: A complete affirmative resolution is a proof that for every K in N there exists N_K such that, for every integer n >= N_K, the quotient M_n / Isom(R^2) contains at least K distinct classes.
- 否定出口: A complete negative resolution is a proof of the logical negation: there exists K in N such that for every N there is an n >= N with h(n) < K. A proof that h(n) is globally bounded is sufficient but stronger than necessary.

不构成完成：

- Computing D(n), or h(n), for finitely many values of n without a theorem covering all sufficiently large n.
- Producing several locally optimal or numerically near-optimal configurations without an exact global-optimality certificate.
- Showing h(n) -> infinity only along a subsequence.
- Showing h(n) >= 2 for all sufficiently large n; this is substantial progress but does not imply h(n) -> infinity.
- Using a triangular-lattice construction that is asymptotically efficient but not proved to attain the exact D(n).

正确性陷阱：

- Verify the order of quantifiers: the target is eventual growth along every integer n, not infinitely many n.
- Prove that every displayed configuration attains the global minimum D(n), not merely a packing bound or a stationary point.
- Check noncongruence under every Euclidean isometry, including reflections and permutations of unlabeled points.
- Retain the weak separation condition ||x-y|| >= 1 and the exact, not asymptotic, diameter objective.
- If h(n) might be infinite, state the cardinal convention and show that all lower-bound statements remain meaningful.

### 更新后的 AI 可解答性

- 等级: `low_candidate`
- 分数: `12/100`
- 信心: `medium`
- 结论: 这是定义清楚、可证伪的开放问题，但目前连最终构型的两种非全等性都无法在充分大 n 的一般情形下保证；对 AI 而言是低可解性候选，而非适合依赖试算直接攻克的题目。

支持理由：

- 目标可严格表述，且全等、分离和直径均可由有限点集的实代数条件编码；任何候选定理可按精确证书审查。
- 问题与有限圆/点装填和三角格点边界组合有关，存在可分解的结构性子引理。
- 题库给出了明确但很弱的当前缺口 h(n)≥2，说明若能建立结构刚性或多重性引理，会有可验证的实质推进。

主要障碍：

- 已知小 n 的最小直径或渐近密度不控制恰好最优构型的数目；核心是精确极值而非近似装填。
- 需要对每个充分大 n 控制全局最优解空间，量词强于在特定 n 或子序列上构造多种好构型。
- 连续构型空间、边界效应与全等判别使数值结果容易把近优、局部优或同构重复误报为新最优构型。

Proof-first 路线：

- 先寻求一个可严格陈述的结构定理：例如对全部足够大的精确极小构型，其接触图、凸包边界或缺陷模式必须满足何种离散约束；再从该约束推出多个非全等最优类或相反的刚性。
- 研究能把“接近三角格点的密度最优”升级为“精确最优的有限边界缺陷分类”的引理；只有该升级成立时，边界组合计数才与 h(n) 有关。
- 至多安排一个计算任务，且仅用于一个先声明的有限 n 引理或反例搜索；必须预先给出精确算术、全局穷尽证书和停止条件。

需要验证：

- 人工查阅 Bezdek–Fodor（1999）全文及其引用链，确认是否存在摘要未体现的构型唯一性/多重性结论。
- 在 MathSciNet、zbMATH、Google Scholar 或作者主页作补充引文追踪，以降低隐蔽的后续文献风险。
- 若出现解答声称，须独立核验其对所有足够大 n 的量词、精确最优性和全等取商。

### 审计限制与人工复核理由

- 题库自身明确说明 OPEN 仅反映维护者当前判断；开放状态无法由有限检索作逻辑证明。
- 对精确短语、问题号、作者、原始论文、相关论文和 arXiv 作了定向检索，但未使用可穷尽的引文数据库检索。
- Bezdek–Fodor（1999）出版商全文在本次会话中不可读；本审计只将其摘要明示的 D(n) 结论作为已验证事实，未假定任何未读的 h(n) 结论。
- 当前问题页显示 0 条评论，因而没有可打开的 #103 专属论坛讨论串；已查看站点论坛入口及问题页的评论状态。

- 建议人工通过 MathSciNet、zbMATH 或 Google Scholar 做引用追踪，并核读 Bezdek–Fodor（1999）全文，以排除未被一般网页索引到的直接后续结果。
- 若后续出现“解答”主张，必须单独核查其全称最终量词、精确全局最优性和将反射纳入的全等判别。

<!-- DEEP_REVIEW:END -->
