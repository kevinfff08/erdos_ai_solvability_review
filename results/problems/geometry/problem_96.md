# Problem 96

## 基本信息

- 原始链接: https://www.erdosproblems.com/96
- LaTeX 页面: https://www.erdosproblems.com/latex/96
- 原始状态: `open`
- 奖金: `no`
- 主类别: `geometry`
- 原始标签: `geometry`, `distances`, `convex`
- 形式化状态: `no`
- OEIS: `possible`
- 原站备注字段: 无

## 原问题

If $n$ points in $\mathbb{R}^2$ form a convex polygon then there are $O(n)$ many pairs which are distance $1$ apart.

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `20/100`
- 建议路线: 优先提取等价表述、尝试特殊情形、寻找可计算子问题，再决定是否进入证明搜索。

## 判断依据

### 有利因素

- 目前只能依靠通用数学推理、文献归纳和特殊情形探索

### 主要障碍

- 所属标签偏证明密集：convex, distances, geometry
- 题面含渐近/无限对象线索：o(
- 缺少明显有限搜索入口。

### 公开版思考过程摘要

- 先识别问题类型：无限/渐近或抽象证明倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: convex, distances, geometry
- 有限/计算线索: 无
- 渐近/无限线索: o(
- 构造/存在性线索: construct

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **不太可能由 GPT-5.5 级别模型直接完成完整证明；但它是一个可做显著辅助推进的中低候选问题。模型较适合重建并形式化已知 O(n log n) 路线、系统化搜索小规模构型与反例、检验加强猜想或中间引理，但要把上界降到 O(n) 预计仍需要新的组合几何核心思想。**
- 等级: `low_to_medium_candidate`
- 分数: `42/100`
- 信心: `medium`
- 可能路线: 较现实的路线是把问题转化为凸多边形顶点上的单位距离图结构分析：先形式化现有 O(n log n) 证明的关键分解，再用计算搜索枚举小 n 的极端或近极端构型，提取可能的 forbidden patterns、度数约束、交叉/嵌套弦约束与局部稀疏性引理；随后用 SAT/SMT、非线性几何约束求解和交互式证明助手验证这些中间引理。目标更可能是得到改进常数、特殊情形的线性界、或验证某个可推广的结构命题，而不是一次性证明完整 O(n)。

### 支持理由

- 问题陈述短且对象清楚：凸位置 n 点、单位距离对数量，适合形式化定义、计算实验和自动化反例搜索。
- 已知上界 O(n log n) 与更精确的 n log_2 n + 4n 给出可审计的技术起点，模型可以尝试重构证明并定位 log 因子来源。
- 下界 2n-7 说明线性量级是合理目标，计算搜索可帮助理解极端构型为何接近 2n。
- 凸性提供强几何约束，单位距离弦的排列、相交、角度和邻接结构可能被拆成可验证的有限或半有限模式。
- 模型配合形式化证明工具时，适合检查许多局部几何不等式和组合计数步骤，能降低人工证明中隐含错误的风险。

### 主要障碍

- 从 O(n log n) 到 O(n) 不是简单常数优化，核心难点很可能是消除递归/分层计数中的 log 因子。
- 单位距离条件包含实代数几何约束，纯图论枚举容易产生不可实现的伪构型，几何可实现性验证成本高。
- 凸多边形的全局连续自由度很大，小 n 搜索得到的模式未必能推广到任意 n。
- 已有下界接近 2n，任何证明都必须精细地区分真实极端结构和可能导致超线性计数的结构。
- 备注中还出现更强的度数和式猜想方向，说明局部最大等距点数的控制非常紧，简单度数论证可能不足。

### 需要的验证

- 完整复现已知 O(n log n) 或 n log_2 n + 4n 证明，并明确每个引理在凸性、单位距离和计数中的作用。
- 建立小规模构型搜索管线：生成候选单位距离图、过滤凸几何可实现性、记录最大边数与极端结构。
- 对模型提出的任何新 forbidden-pattern 引理进行独立验证，包括数值搜索反例、符号几何证明和人工审查。
- 若声称特殊情形线性界，需要清楚说明特殊假设，例如度数有界、边长序列限制、对称性、或某类弦排列限制。
- 若声称完整 O(n) 证明，需要形式化或半形式化地检查所有渐近计数步骤，尤其是没有隐藏 log 因子或未证明的均匀常数。

### 公开版思考摘要

这个问题很适合 AI 做“证明工程”和“结构探索”：定义简洁、已有上界和下界提供锚点，凸几何约束也便于计算实验与形式化局部引理。但完整猜想仍是开放的组合几何上界问题，现有信息显示主要瓶颈是发现新的全局计数机制，而不是补全一个明显缺失的技术细节。因此评为 low_to_medium_candidate：可望显著推进某些子问题或验证候选引理，但直接解决的概率较低。

### 免责声明

以上是对 GPT-5.5 级别模型辅助研究可行性的评估，不是该 Erdős 问题的证明，也不声称给出了 O(n) 上界。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `likely_open`
- 状态信心: `medium`
- 可行动性: `needs_human_clarification`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_96.md](../../prompts/problem_96.md)

### 状态结论

该命题是良定义的长期公开问题，但状态不能仅标为“已确认开放”：Khopkar 的 arXiv:1605.08066v2（2017，未见同行评审版本）声称证明了所需的 O(n) 上界。该论证尚未获得独立验证；当前 Erdős Problems 页面仍将 #96 标为 OPEN，2026 年论坛讨论亦明确将该预印本的结论视为未确认并要求审查。因此，最准确的当前结论是“很可能仍开放”，下一步应优先逐引理核验这份声称的证明，而非把问题当作无既有解答的纯开放题。

### 当前规范陈述

设 P={p_1,...,p_n} 为 R^2 中严格凸 n 边形（n>=3）的顶点集：各点互异、均为其凸包的顶点，并且没有三点共线。令 u(P)=|{{p,q}⊂P: ||p-q||_2=1}|，其中点对不计顺序。是否存在与 n 及 P 无关的绝对常数 C 和 n_0，使得对每个 n>=n_0 及每个这样的 P 都有 u(P)<=Cn？等价地，f(n):=max_P u(P) 是否为 O(n)？

```text
Let P={p_1,...,p_n} be the vertex set of a strictly convex Euclidean n-gon in R^2 (n>=3): the points are distinct, are the vertices of their convex hull in cyclic order, and no three are collinear. Let u(P)=|{{p,q} subset P: ||p-q||_2=1}|, where pairs are unordered. Is there an absolute constant C and an integer n_0 such that u(P)<=Cn for every n>=n_0 and every such P? Equivalently, f(n):=max_P u(P) is O(n), with constants independent of P and n.
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 未发现能推翻按上述标准解释的简单构造。已知 Edelsbrunner–Hajnal 构造给出 2n-7 个单位距离，支持线性下界但并不反驳线性上界。弱凸/共线边界点的措辞歧义值得澄清，但本次检索未找到由此产生超线性单位距离数的直接反例。
- 版本变化: Erdős–Moser 早先提出的更强渐近猜想 f(n)=5n/3+O(1) 已被 Edelsbrunner–Hajnal 的 2n-7 构造否定。Erdős 后来归功于 Erdős–Fishburn 的更强常数猜想为上界 2n；它仍比本题的 O(n) 强。Erdős Problems 的修订记录显示当前 O(n) 表述至少自 2025-10-20 保持不变。2017 年 Khopkar 预印本声称证明 O(n)，但未被数据库采纳为已解，构成当前最重要的未核实“解决声明”。

陈述问题：

- 原文的“大 O”未显式写出量词；审计中的标准解释是存在绝对 C、n_0，对所有足够大的 n 和所有相应多边形一致成立。
- “form a convex polygon”在非严格用法下可能允许共线边界点；被引文献通常使用“convex position/convex n-gon”，即每个点为严格凸多边形的顶点。这里采用该标准版本，且不把该措辞差异当作对原命题的静默修补。
- “pairs”应为无序的不同顶点对，距离为通常的欧氏距离且严格等于 1。

需要固定的量词/约定：

- The constants in O(n) must be absolute and uniform over every admissible polygon.
- The maximisation is over every strictly convex n-gon in the Euclidean plane, not over one fixed polygonal family.
- Unit-distance pairs are unordered pairs of distinct vertices; all polygon chords and sides are eligible.
- The meaningful asymptotic assertion is for all sufficiently large n; finitely many small n do not affect O(n).

### 文献与当前边界

已核验的主要结果：

- Erdős–Moser（1959）提出凸 n 边形单位距离最大数的研究；其早期 5n/3 量级强猜想后来被否定。
- Edelsbrunner–Hajnal（1991，同行评审）证明：对每个 n>=4 存在凸 n 边形有至少 2n-7 条单位距离边。
- Füredi（1990，同行评审）证明 O(n log n) 上界；Brass–Pach（2001，同行评审）给出短证明。
- Aggarwal（2015，同行评审）把显式上界改进到 n log_2 n+4n，并通过距离矩阵的 diagonal/obtuse-angle 性质排除某些模式。
- Ábrego–Fernández-Merchant（2002，同行评审）在中心对称凸多边形这一严格子类中证明线性上界，且给出接近 2n 的行为。
- Khopkar（arXiv v2，2017）声称一般凸独立点集已有 O(n) 上界；该声称未见同行评审发表或独立确认，不能列作已验证定理。

最近相关工作：最新直接相关的“可能解决”是 Khopkar 的 2017 arXiv v2，而非近三年的已确认新定理。2026 年 #96 论坛仍把它标为未确认；本次针对 2023–2026、arXiv 和精确题名的检索未发现另一篇可核验的同行评审一般 O(n) 证明或反例。

剩余核心：若 Khopkar 的证明有不可修复缺口，则剩余核心正是证明存在统一常数 C 使 f(n)<=Cn；已验证范围仍介于 2n-7 与 n log_2 n+4n 之间。若该预印本正确，则核心转为对其完整证明的独立认证，并可进一步研究最优常数（历史上猜想为 2）而非本题。

已使用方法：

- 将凸点集按对踵线分割并编码为有序二分图或 0–1 距离矩阵。
- 利用凸四边形的 diagonal property 与 obtuse angle property，排除单位距离边构成的矩阵模式/交织循环。
- 分治计数以得 O(n log n)；中心对称情形使用额外对称几何。
- Khopkar 声称的路线：单位距离图到两个 GUDG 的线性损失分解，再经模块、辅助边和特殊有序图结构推出线性界。

争议或不确定性：

- Khopkar 预印本的摘要和 Theorem 4 声称完整 O(n) 结果，但没有找到同行评审版本、形式化或独立逐步验证；数据库及论坛未接受其为解答。
- 不能从“后来论文仍引用 O(n log n)”单独推出 Khopkar 证明错误，因为引用可能不完整；同样不能从预印本存在推出其正确。
- 一般问题的最优常数、是否为 2n+O(1)，均不等同于本题的线性存在性命题。

### 证据来源

- [Erdős Problem #96](https://www.erdosproblems.com/96) — Thomas F. Bloom (database editor), date unknown; `problem_page`, `database_record`, directness=`direct`, reliability=`high`. 当前数据库将命题标为 OPEN，记录已知上界 n log_2 n+4n、下界 2n-7，并明确提示数据库标签不是文献检索的替代品。
- [Revision history of Erdős Problem #96](https://www.erdosproblems.com/history/96) — Thomas F. Bloom (database editor), 2025-10-20; `problem_page`, `database_record`, directness=`direct`, reliability=`high`. 确认当前表述、历史的 5n/3+O(1) 强猜想已被 2n-7 构造否定，以及页面所列的研究脉络。
- [96 Discussion Thread](https://www.erdosproblems.com/forum/thread/96) — Allan_Zhao and other forum participants, 2026-01-13; `forum`, `informal_claim`, directness=`direct`, reliability=`medium`. 论坛提出 Khopkar 预印本可能已解本题，但随后明确称其未发表、证明复杂且结论“unconfirmed”；搜索结果还记录了对具体部分的审查担忧。该来源证明存在待核验的解答声明，而不证明该声明正确。
- [Edge complexity of geometric graphs on convex independent point sets](https://arxiv.org/abs/1605.08066) — Abhijeet Khopkar, 2017-04-21; `preprint`, `preprint`, directness=`direct`, reliability=`medium`. 预印本摘要明确声称：凸独立点集上的单位距离图有 O(n) 条边；arXiv 仅显示 v2，且无期刊引用。
- [Edge complexity of geometric graphs on convex independent point sets (full text)](https://arxiv.org/pdf/1605.08066) — Abhijeet Khopkar, 2017-04-21; `preprint`, `preprint`, directness=`direct`, reliability=`medium`. 可直接检查其 Theorem 4 及其依赖链：从单位距离图分解为 GUDG，再以模块/辅助边论证 GUDG 线性稀疏。本文审计未完成该证明的逐步验证，故不能将其视为解决。
- [On Unit Distances in a Convex Polygon](https://arxiv.org/abs/1009.2216) — Amol Aggarwal, 2014-10-21; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 作者的最终 arXiv 版本给出期刊出处并声称将 Füredi 的界改进为 n log_2 n+O(n)。
- [On unit distances in a convex polygon](https://www.sciencedirect.com/science/article/pii/S0012365X14003847) — Amol Aggarwal, 2015-03-06; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 同行评审论文的摘要说明其上界为 n log_2 n+O(n)，使用凸四边形的 diagonal property 与 obtuse angle property，并给出方法局限性的下界。
- [A lower bound on the number of unit distances between the vertices of a convex polygon](https://www.sciencedirect.com/science/article/pii/009731659190042F) — Herbert Edelsbrunner and Péter Hajnal, 1991-03-01; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 证明对每个 n>=4 存在凸 n 边形，恰有至少 2n-7 对顶点距离为 1；该构造否定了旧的 5n/3+O(1) 上界猜想。
- [The maximum number of unit distances in a convex n-gon](https://doi.org/10.1016/0097-3165(90)90074-7) — Zoltán Füredi, 1990; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 经典 O(n log n) 上界的原始同行评审文献；Aggarwal 的论文摘要将其常数表述为此前的 2π n log_2 n+O(n)。
- [The maximum number of times the same distance can occur among the vertices of a convex n-gon is O(n log n)](https://doi.org/10.1006/jcta.2000.3133) — Peter Brass and János Pach, 2001; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 给出 Füredi 型 O(n log n) 结论的短证明；Khopkar 文本的参考文献和数据库页面均将其作为替代证明。
- [The unit distance problem for centrally symmetric convex polygons](https://www.csun.edu/~ba70714/publications/unit.pdf) — Bernardo M. Ábrego and Silvia Fernández-Merchant, 2002-01-01; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 证明中心对称凸多边形的受限问题具有线性上界（文中给出 f_sym(n)<=2n-3），这是支持性特殊情形，而非一般问题的证明。

### 完成标准

- 肯定出口: Produce a complete, independently checkable proof that there are absolute C,n_0 with u(P)<=Cn for every strictly convex Euclidean n-gon P and all n>=n_0. For the existing claim, every reduction and every module/auxiliary-edge lemma used to reach Theorem 4 of arXiv:1605.08066 must be verified or replaced.
- 否定出口: For the current proof-verification task, exhibit a precise false statement, missing case, or non-derivable inference in the Khopkar proof, with an explicit admissible configuration/counterexample where appropriate; then the audit outcome is that the claimed resolution fails and Problem 96 remains open under the verified O(n log n) bound. A mathematical disproof of Problem 96 itself would instead require convex n-gons P_k with u(P_k)/|P_k| unbounded.

不构成完成：

- A finite computation over sampled polygons or small n without a theorem covering all n.
- Showing only O(n log n), a result restricted to centrally symmetric polygons, or an upper bound with a constant depending on P.
- Repeating the preprint's abstract, figures, or a proof sketch without checking its lemmas and all exceptional cases.
- Showing that an abstract ordered graph class is sparse without proving that every geometric unit-distance graph enters that class with only O(n) loss.
- Establishing the conjectural 2n bound only for a special family of polygons.

正确性陷阱：

- Use the Euclidean, exact-equality unit-distance graph, not a unit-disk graph or an arbitrary subgraph convention.
- Keep the strict-convex-position hypothesis and account for all vertex pairs, including polygon sides and long chords.
- Track every edge discarded in an antipodal-line decomposition and prove the loss is O(n) with a uniform constant.
- Do not infer linearity merely from the path-restricted ordered-bipartite property: that class has Theta(n log n) extremal size.
- In the claimed 2017 proof, audit the transition from GUDG to its module decomposition, the definition and charging of auxiliary edges, and every use of geometric realizability rather than treating a drawing as proof.
- Separate a proof of O(n) from the much stronger unproved-looking optimal-constant assertion f(n)<=2n+O(1).

### 更新后的 AI 可解答性

- 等级: `medium_candidate`
- 分数: `42/100`
- 信心: `medium`
- 结论: 适合“先审计既有声称、后决定是否研究”的中等候选目标；不适合在未审查 2017 预印本前直接进行盲目的新证明搜索。

支持理由：

- 目标的量词、对象和完成条件清楚，且已有可直接逐引理核验的完整声称证明。
- 已验证的上下界和多个矩阵/有序图框架提供了明确的比较基线与可检查中间命题。
- 如果声称证明只缺少局部论证，独立审计或修复可比从零突破 O(n) 更有希望。

主要障碍：

- 一般 O(n) 结论历经多年仍未获公认，意味着预印本中的结构性步骤可能存在非局部缺口。
- 几何图形、角度严格不等式、边分配和抽象有序图之间的转换极易遗漏退化或方向情况。
- 有限配置搜索不能证明渐近线性，也不能可靠地否定该命题。

Proof-first 路线：

- 首先将 Khopkar Theorem 4 的依赖图拆为可独立验证的引理；对每个引理写出精确假设、结论和引用的图形/角度事实。
- 并行寻找其关键抽象图命题的最小反例或证明；若抽象命题成立，再单独验证每个抽象对象确由几何单位距离图产生。
- 若该路线失效，回到 Aggarwal 的距离矩阵框架，寻找能把 O(n log n) 分治递推降为线性递推的额外、可由凸性证明的禁止模式。

需要验证：

- 人工或形式化级别核验 Khopkar 预印本第 5 节的模块、辅助边、引理 10–13 与 Theorem 4 的全部依赖。
- 核验其“UDG 是 LGG”及对踵分割后的边分配在边界角、相等角和端点情形是否保持所需性质。
- 检索或联系作者/领域专家确认是否存在撤回、勘误、论文版本或已知反例；本次公开检索未找到。

### 审计限制与人工复核理由

- Erdős Problems 的主页面与论坛在直接打开时返回 403；其搜索索引内容、可打开的历史页以及论坛搜索结果已被交叉使用，但论坛完整嵌套讨论未能逐条直接抓取。
- 未能找到 Khopkar 预印本的同行评审版本、勘误、撤回通知或形式化验证；这正是将状态定为 likely_open 而非 confirmed_open/solved 的主要原因。
- 本审计检查了预印本可访问全文中主结论的依赖结构与若干关键段落，但没有在本轮完成其 18 页证明的逐引理数学复核，不能据此断言其正确或错误。
- 针对近三年检索未发现可核验的一般 O(n) 新证明，但检索失败不是不存在文献的逻辑证明；应在正式研究开始前再次做 MathSciNet/zbMATH/作者联系层面的人工复查。
- “凸多边形”是否允许共线边界点在原始自然语言中未明确；本报告采用凸几何文献通常的严格凸顶点版本，并把该约定显式记录。

- 存在一个直接声称解决问题但未被同行评审或独立确认的预印本；其正确性决定题目究竟已解还是仍开放。
- 论坛中的怀疑是有价值的线索但不是数学反证，需由几何组合领域专家或形式化/逐行审计作出结论。
- 若后续研究要以“开放问题”名义投入资源，必须先确认 Khopkar 版本是否已有后续发表、勘误或已知漏洞。

<!-- DEEP_REVIEW:END -->
