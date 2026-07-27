# Problem 91

## 基本信息

- 原始链接: https://www.erdosproblems.com/91
- LaTeX 页面: https://www.erdosproblems.com/latex/91
- 原始状态: `open`
- 奖金: `no`
- 主类别: `geometry`
- 原始标签: `geometry`, `distances`
- 形式化状态: `yes`
- OEIS: `A186704`, `possible`
- 原站备注字段: 无

## 原问题

Let $n$ be a sufficiently large integer. Suppose $A\subset \mathbb{R}^2$ has $\lvert A\rvert=n$ and minimises the number of distinct distances between points in $A$. Prove that there are at least two (and probably many) such $A$ which are non-similar.

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `30/100`
- 建议路线: 优先提取等价表述、尝试特殊情形、寻找可计算子问题，再决定是否进入证明搜索。

## 判断依据

### 有利因素

- 已有形式化陈述，可降低语义误读风险
- 存在 OEIS 数据入口，利于实验与反例搜索

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
- 模型: `GPT-5.5`
- 结论: **低到中等候选。GPT-5.5 配合计算和形式化工具较可能在小 n 例子、候选构型搜索、局部变形排除、以及命题形式化方面取得显著推进，但直接证明“充分大 n 的全局极小构型至少有两个非相似类”很可能需要突破当前对平面最少不同距离问题极值结构的理解。**
- 等级: `low_to_medium_candidate`
- 分数: `38/100`
- 信心: `medium`
- 可能路线: 可行路线不是直接求解，而是先把问题拆成两个方向：一是对给定 n 的候选极小构型做计算枚举、SAT/SMT/代数约束搜索和距离多项式验证，扩大已知非相似极小例子的范围；二是研究已知低距离构造族的可扰动性、拼接性或参数化变体，尝试证明若某一构造族达到最小距离数，则存在至少两个非相似实现。形式化证明系统可用于验证有限 n 分类或距离计数引理，但对“充分大”部分仍需新的全局极值论证。

### 支持理由

- 题目已形式化，目标陈述清晰，适合把“相似类”“距离集合大小”“极小性”等概念编码进证明助手或计算搜索框架。
- 目标是非唯一性结论，而不是精确给出最小不同距离数；理论上可能通过构造两个同样达到已知下界或同一极值值的族来推进。
- 几何距离约束可转化为代数方程、不等式和图实现问题，适合用计算代数、SMT、数值搜索加严格验证组合使用。
- 备注中已有小 n 的唯一性和非唯一性线索，说明有限规模实验可能产生结构猜想和可验证证据。
- AI 可以较好地组织文献、抽取已知构造、生成候选参数族，并为有限案例建立可复查的验证脚本。

### 主要障碍

- 对任意充分大 n 的全局极小构型缺少已知结构刻画；若不知道哪些集合真正最小，就很难证明存在两个非相似极小集合。
- 问题隐含依赖最少不同距离数的精确极值，而这通常比渐近上下界更强。
- 计算搜索只能覆盖有限 n，不能直接推出充分大 n，除非发现可推广的递推、拼接或稳定性机制。
- 相似类判定和距离重合关系在连续几何中容易出现退化，需要严格代数验证，单纯数值证据不足。
- 若极小构型接近格点或高对称构造，证明非唯一性可能要求非常精细的距离重复计数和边界效应控制。

### 需要的验证

- 建立可复现的程序，输入 n 和候选点集，严格计算不同距离数并判定非相似性。
- 对小 n 和中等 n 做完整或半完整搜索，区分真实极小、局部最优和启发式候选。
- 把距离重合、非重合、相似等条件转化为精确有理数、代数数或区间证明，避免浮点误判。
- 检索并核对关于最少不同距离构造、有限 n 极小构型、以及 n=5 证明等相关文献，但最终论证不能只依赖经验表。
- 若提出无限族，需要证明该族确实达到全局最小距离数，或给出一个独立下界与两个构造的上界精确吻合。

### 公开版思考摘要

这个问题对 AI 的主要吸引力在于目标形式清楚、有限实例可计算、几何约束可代数化；因此 GPT-5.5 级模型可以有效推进实验、分类、形式化验证和候选构造生成。但核心难点是“极小”是全局性质，并且陈述要求所有充分大 n。没有对大 n 极小不同距离构型的强结构定理，证明非相似极小集合存在仍然很硬。因此我评为低到中等候选：适合显著推进和验证局部成果，但不应预期一次性解决。

### 免责声明

以上是关于 GPT-5.5 级工具增强模型可解性与推进潜力的审查判断，不是该 Erdős 问题的证明或反例。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `confirmed_open`
- 状态信心: `medium`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_91.md](../../prompts/problem_91.md)

### 状态结论

截至审计日，官方 Erdős Problems 数据将 #91 标为 open，且其 formal_status 为 unformalized；针对精确陈述、Kovács 预印本、近三年 arXiv 检索、形式化仓库及相关关键词的检索均未找到解决或反例。Kovács 的 2024 工作只证明 n=5 的历史小例，不解决渐近命题。因此当前最合理分类是开放，但由于主网页受 403 限制、1987 原文未全文核读且检索不可能完备，置信度为中等。

### 当前规范陈述

对每个整数 n≥2，令 D(n)=min{|{||x-y||:x,y∈A,x≠y}|:A⊂R²，|A|=n}。若 n 点集 A 恰好确定 D(n) 个非零欧氏距离，称其为全局极小构型。按通常欧氏相似的约定（平移、正交变换〔含反射〕与正比例缩放），可形式化的核心问题为：是否存在整数 n₀，使得每个 n≥n₀ 都有两个彼此不相似的 n 点全局极小构型？原文“and probably many”只是猜测性措辞，不是另一个已量化命题。

```text
For each integer n >= 2, define D(n) = min{|{||x-y|| : x,y in A, x != y}| : A is a subset of R^2 and |A| = n}. A finite n-point set A is a global minimizer if it determines exactly D(n) distinct nonzero Euclidean distances. Interpreting “similar” in its usual Euclidean sense—translation, an orthogonal transformation (including reflection), and multiplication by a positive scalar—the formal core asks: does there exist an integer n0 such that for every n >= n0 there are two global minimizers A,B of size n that are not similar? The phrase “and probably many” is heuristic, not a separately quantified assertion.
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 小 n 的唯一性并不反驳“充分大 n”的命题。官方记录给出 n=3、n=5 的唯一性，并称 n=4 及 6≤n≤9 有至少两个非相似极小例。未发现可否定最终全称量词的简单构造或已证无限反例子序列。
- 版本变化: Erdős 在 1987、1990 的问题汇编中提出该渐近多重性问题。官方记录后来补充小规模情形；Kovács（2024，预印本）给出对 n=5 正五边形唯一性的可检查计算机辅助论证。该工作澄清历史评语，不改变大 n 的开放核心。

陈述问题：

- “sufficiently large”须解释为“存在 n₀，使得对所有 n≥n₀ 成立”。
- “minimises”必须是对所有平面 n 点集的全局最小，而非某一构造族内或局部最小。
- 原文未界定 similar；本审计采用通常允许反射的欧氏相似。若采用仅保向相似，须重述命题。
- “probably many”未给出量词、增长函数或完成标准，不能当作与“至少两个”并列的正式目标。

需要固定的量词/约定：

- There must exist one integer n0 such that the property holds for every integer n >= n0.
- The minimization ranges over all n-element subsets of the Euclidean plane.
- The two examples must represent two Euclidean-similarity classes of global minimizers, not two labelled, congruent, or scaled copies.
- “Probably many” has no fixed formal content and is excluded from the canonical target.

### 文献与当前边界

已核验的主要结果：

- 官方记录称 n=3 时等边三角形唯一；n=4 时正方形与两个共边等边三角形给出两个非相似极小构型；n=5 时正五边形唯一；并转述 Erdős 1987 对 6≤n≤9 至少有两个非相似例子的陈述。前两组及 6≤n≤9 的原始证明在本次审计中未逐页独立核读。
- Kovács（2024，arXiv 预印本）证明：若五点集仅确定两个距离，则每个三角形均等腰；其对所有五点等腰三角形配置的消元/分类排除其余候选，得到正五边形唯一。这证明的是 n=5 的有限事实。
- Guth–Katz（2015，Annals of Mathematics）证明 D(n)≥c n/log n。它显著约束最小距离数的量级，但既不确定一般 D(n) 的精确值，也不比较达到 D(n) 的构型相似类。

最近相关工作：直接针对 #91 的最新可检查研究是 Kovács 的 2024 预印本 arXiv:2412.05190，内容为 n=5 的历史小例。对 2023–2026 年 arXiv、精确措辞、作者和形式化仓库的目标检索未发现解决“所有充分大 n”的论文、预印本或可审计反例。

剩余核心：证明或否定：存在 n₀，使每个 n≥n₀ 的 D(n)-极小 n 点集至少属于两个欧氏相似类。最根本的困难在于，对一般 n，D(n) 的精确值及所有达到它的构型均未知；仅有 D(n) 的渐近上下界并不能强制或排除极小构型的非唯一性。

已使用方法：

- 有限 n 的精确分类：距离图、等腰三角形约束、代数消元及可核查的穷举。Kovács 的 n=5 论证是这种方法。
- 一般 distinct-distances：Elekes–Sharir 的刚体群转化、三维点线关联、分割多项式、代数曲面/直纹曲面工具（Guth–Katz）。
- 任何计算若被使用，应仅检验一个有限且事先陈述的分类引理或反例问题，并输出精确代数证书；它不能替代最终的全称渐近论证。

争议或不确定性：

- 官方数据同时写 formalized=yes 与 formal_status=unformalized：前者表示已有形式化陈述/登记，后者表明没有 Lean 等形式化解答；不能把它报告为已验证证明。
- Erdős 1987 原文及其关于 6≤n≤9 的具体页尚未取得并全文核验，因此该陈述保留为官方记录转述的历史事实。
- 没有检索到解答并非文献不存在的逻辑证明；付费数据库及全部最新作者网页未能穷尽。

### 证据来源

- [Erdős Problems official data: entry 91](https://raw.githubusercontent.com/teorth/erdosproblems/refs/heads/main/data/problems.yaml) — Erdős Problems database contributors, date unknown; `problem_page`, `database_record`, directness=`direct`, reliability=`high`. 官方数据中 #91 的 informal_status 与 status 均为 open（最后更新 2025-08-31），formal_status 为 unformalized，且 formalized 标记为 yes（最后更新 2026-04-16）。这区分了“命题已有形式化表述”与“已有机器验证解答”。
- [Erdős Problems database repository](https://github.com/teorth/erdosproblems) — Erdős Problems database contributors, date unknown; `secondary_index`, `database_record`, directness=`direct`, reliability=`high`. 仓库说明其 YAML 数据为该数据库的 ground truth，并在表中列 #91 为 open、statement formalized 为 yes。
- [Erdős Problems — Problem 91](https://www.erdosproblems.com/91) — Thomas F. Bloom / Erdős Problems database contributors, 2025-08-31; `problem_page`, `database_record`, directness=`indirect`, reliability=`medium`. 问题的公开主页面与原始陈述入口。审计时直接抓取返回 403，因此关于状态和元数据采用同一官方项目的公开 YAML 记录复核。
- [A note on Erdős's mysterious remark](https://arxiv.org/pdf/2412.05190) — Zoltán Kovács, 2024-12-09; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 文章第 5 节明确将 #91 的 n=5 评语化为“两距离五点集”的唯一性，并用前述分类/消元论证排除其余候选，从而证明正五边形是唯一两距离五点构型；文章不声称解决充分大 n 的主问题。
- [A note on Erdős's mysterious remark — arXiv record](https://arxiv.org/abs/2412.05190) — Zoltán Kovács, 2024-12-06; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 核实作者、提交日期、预印本状态及该文的六点等腰三角形分类背景。
- [Some of my favourite unsolved problems](https://www.cambridge.org/core/books/abs/tribute-to-paul-erdos/some-of-my-favourite-unsolved-problems/D45197FBE776AF3E275CFF55B2C3BE65) — Paul Erdős, 1990; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 核实 Erdős 1990 章节的作者、书名、页码 467–478、出版年及 DOI。全文受限，未将该入口单独作为小 n 断言的全文核验。
- [OEIS A186704: minimum number of distinct distances determined by n points in the Euclidean plane](https://oeis.org/A186704) — OEIS Foundation contributors; sequence initiated by Michael Somos, date unknown; `oeis`, `database_record`, directness=`indirect`, reliability=`medium`. 给出 D(n) 的相关小 n 序列与 distinct-distance 文献交叉索引；可作为小值背景，不能推出极小构型相似类数。
- [On the Erdős distinct distances problem in the plane](https://annals.math.princeton.edu/2015/181-1/p02) — Larry Guth and Nets Hawk Katz, 2015-01-01; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 证明任意 N 点平面集确定至少 cN/log N 个不同距离。该结果是 D(n) 的强一般下界，但没有分类 D(n)-极小构型，因而不解决 #91。
- [On the Erdos distinct distance problem in the plane](https://arxiv.org/abs/1011.4105) — Larry Guth and Nets Hawk Katz, 2010-11-17; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 可检查 Guth–Katz 结果的预印本陈述及其入射几何、分割多项式和直纹曲面方法说明。
- [Formal Conjectures Repository issue 324: Erdős Problems 91](https://github.com/google-deepmind/formal-conjectures/issues/324) — Formal Conjectures contributors, date unknown; `formalization`, `formalized_artifact`, directness=`indirect`, reliability=`medium`. 检索结果显示 #91 在 Formal Conjectures Repository 中以开放的新命题 issue 建立；结合官方 YAML 的 formal_status=unformalized，不能把 formalized=yes 误读为正式证明。

### 完成标准

- 肯定出口: Prove that there exists an integer n0 such that for every integer n >= n0 there are n-point sets A_n,B_n subset R^2, each determining exactly D(n) distinct nonzero distances, and prove that no Euclidean similarity maps A_n to B_n.
- 否定出口: Prove that infinitely many integers n have a unique D(n)-minimizing n-point set up to the stated Euclidean-similarity convention. Such an infinite sequence contradicts the eventual-for-every-n affirmative statement.

不构成完成：

- Producing two non-similar n-point sets with the same distance count without proving that count equals D(n).
- Settling finitely many n, or an affirmative construction on only a subsequence.
- Giving relabelled, congruent, reflected-under-an-excluded-convention, or uniformly scaled copies.
- Improving asymptotic bounds on D(n) without proving a statement about exact global minimizers.
- Using floating-point optimization or heuristic enumeration without a complete exact certificate.

正确性陷阱：

- Global optimality must be established separately from the construction: an upper bound D(n) <= k is not enough.
- The proof must keep the reflection convention for similarity fixed.
- Count distinct distance values, not the number of pairs attaining a distance.
- The threshold n0 must work for every larger integer, not merely a density-one set or an infinite subsequence.
- A negative resolution needs infinitely many unique-minimizer values of n, not isolated small cases.

### 更新后的 AI 可解答性

- 等级: `low_candidate`
- 分数: `9/100`
- 信心: `medium`
- 结论: 命题本身可精确定义，但其开放核心远超当前可由有限分类或常规 AI 推理直接处理的范围；可作为长期证明优先探索，而非短期可望解决的目标。

支持理由：

- 有清晰的正、反完成条件，且小 n 的子问题可以生成可审核引理和证书。
- 已有 distinct-distance 的强工具与小规模代数分类可提供互不相同的研究入口。

主要障碍：

- 一般 n 的 D(n) 精确值及极小构型分类均未知，故构造“距离数相同”的两个点集通常无法证明它们是全局极小。
- Guth–Katz 型结果控制数量级而非精确极值结构，不能直接导出相似类多重性。
- 任何有限计算都无法单独证明“所有充分大 n”的量词。

Proof-first 路线：

- 寻找可证明的结构性转移引理：在明确假设下，把任一全局极小构型变换为不相似的全局极小构型；随后独立证明该假设最终必然成立。
- 研究是否存在保留精确最优性而非仅保留上界的加点、替换或拼接操作。
- 仅在一个明确、有限的距离图/代数配置分类引理下使用精确计算；先声明假设、证书格式和停止条件。

需要验证：

- 人工获取并核读 Erdős 1987、1990 的相关页，核实 n=6 至 9 的历史陈述与 similar 的语境。
- 定位 Formal Conjectures #91 的具体 Lean 文件或确认 issue 状态，核定 formalized 标记所覆盖的命题。
- 在 MathSciNet、zbMATH 和作者主页补做 2025–2026 检索。

### 审计限制与人工复核理由

- 直接访问 erdosproblems.com 的 #91 页面及 LaTeX 页面时遇到 403；状态改由同一官方项目公开的 YAML 数据和交互表复核。
- 未能获得 Erdős 1987 论文的相关全文页，因此没有独立验证其对 6≤n≤9 的具体构型断言。
- Kovács 论文是预印本，尽管可公开检查，其计算机辅助部分仍应由后续研究者按作者给出的代码/消元步骤复核。
- 文献检索覆盖公开网页、arXiv、出版社页面、OEIS 与形式化仓库索引，但不覆盖所有付费数据库或未索引手稿。

- 需核读 Erdős 1987、1990 的原始相关页，以确认历史小 n 叙述及相似约定。
- 需检查 Formal Conjectures #91 的具体 formal artifact，明确 `formalized: yes` 的精确内容。
- 建议以 MathSciNet/zbMATH 和作者主页补检 2025–2026 年工作，再把当前开放状态提升至高置信度。

<!-- DEEP_REVIEW:END -->
