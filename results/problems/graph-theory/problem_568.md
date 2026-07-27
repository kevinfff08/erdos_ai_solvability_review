# Problem 568

## 基本信息

- 原始链接: https://www.erdosproblems.com/568
- LaTeX 页面: https://www.erdosproblems.com/latex/568
- 原始状态: `open`
- 奖金: `no`
- 主类别: `graph theory`
- 原始标签: `graph theory`, `ramsey theory`
- 形式化状态: `no`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

Let $G$ be a graph such that $R(G,T_n)\ll n$ for any tree $T_n$ on $n$ vertices and $R(G,K_n)\ll n^2$. Is it true that, for any $H$ with $m$ edges and no isolated vertices,\[R(G,H)\ll m?\]

## AI 完成可能性判断

- 结论: **AI 可能做出局部推进或搜索反例，但完整解决把握不足**
- 等级: `low_to_medium_candidate`
- 分数: `41/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 题面或备注出现有限对象/计算线索

### 主要障碍

- 题面含渐近/无限对象线索：\ll

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: graph theory, ramsey theory
- 证明密集标签命中: 无
- 有限/计算线索: graph, ramsey
- 渐近/无限线索: \ll
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **较有希望显著推进，但不宜评为高概率完全解决。问题把树 Ramsey 线性、团 Ramsey 二次这两个对固定图 G 的假设，要求提升为对所有无孤立点 m 边图 H 的线性 Ramsey 大小。GPT-5.5 配合计算和文献检索可能系统化梳理已知充分条件、抽象出可证明的中间定理，并尝试反例族搜索；但完全证明需要统一处理任意稀疏 H 的结构和 Ramsey 嵌入机制，存在明显理论障碍。**
- 等级: `medium_candidate`
- 分数: `63/100`
- 信心: `medium`
- 可能路线: 可行路线不是直接蛮力求解，而是把命题拆成可验证的结构引理：从 R(G,T_n) 线性提取 G 对低退化或有界平均度图的嵌入控制，从 R(G,K_n) 二次提取 dense host 中的约束，再尝试证明任意无孤立点 m 边图 H 可按森林核心、高度数核心和剩余稀疏部分分解并逐步嵌入。工具层面可用文献检索定位 Ramsey size linear、tree Ramsey、graph Ramsey bounds 的已知定理，用形式化或半形式化证明检查关键归纳，用计算搜索小型 G 与 H 族寻找反例模式或测试分解猜想。

### 支持理由

- 问题陈述短且假设清晰，适合由模型把目标转化为若干可审计的中间命题，而不是依赖大量隐藏背景定义。
- 两个前提分别控制树目标和团目标，覆盖稀疏连通结构与极稠密目标的两端；这给 AI 构造插值式证明路线提供了可操作入口。
- 结论对 H 只按边数 m 线性计，因此自然可尝试按度序、核分解、树状展开、匹配/星森林分解等算法化结构分解来推进。
- 计算反例搜索有实际价值：可以枚举小图 G 和小规模 H，测试满足前提迹象但可能违反结论的候选结构，从而决定证明方向是否可信。
- 形式化证明工具可能帮助验证局部组合引理、递推不等式和嵌入贪心过程，降低模型在复杂 Ramsey 参数推导中的错误率。

### 主要障碍

- 前提只给出 G 对所有树和所有团的 Ramsey 增长约束，如何推出对任意 H 的统一线性边数界并不直接；中间图族可能包含复杂高度数局部结构和多环结构。
- R(G,H) 的线性边数目标要求常数只依赖 G，而 H 完全任意且无孤立点；这使得证明必须同时处理稀疏、半稠密和由多个尺度混合的 H。
- 树界和团界之间可能存在很大空隙，AI 需要证明不存在利用该空隙构造的反例族，这通常比证明若干正例困难。
- 若需要新的 Ramsey 理论思想，当前模型更可能提出可检查猜想和部分结果，而不是可靠地产生完整原创证明。
- 形式化验证完整命题难度较高，因为需先建立或导入 Ramsey 数、树、任意图分解等组合库；短期内更现实的是验证有限子引理。

### 需要的验证

- 检索并核对该问题相关的 Ramsey size linear 定义、已知等价条件、以及对固定 G 的树目标和团目标 Ramsey 上界文献，确认是否已有接近该命题的定理。
- 对候选证明路线中的每个分解引理给出明确常数依赖，特别检查线性 m 界是否在多轮嵌入或递归中膨胀为 m log m 或更差。
- 进行小规模计算搜索：枚举固定 G 候选与多类 H，包括星、路径、稠密小团块并联、二分图、长环加高度数核心等，寻找违背线性趋势的迹象。
- 用证明助理或严格手写证明验证核心归纳步骤，例如从树 Ramsey 线性推出某类森林或有界退化图的 Ramsey 线性界是否真的成立。
- 若得到疑似反例，需要验证该 G 同时满足两个前提；若得到疑似证明，需要独立专家审查所有 Ramsey 参数与常数依赖。

### 公开版思考摘要

该问题适合作为 GPT-5.5 级模型的中等偏高价值目标：它的输入条件少、目标明确，并且可拆成文献定位、结构分解、有限反例搜索和局部证明验证等工具友好子任务。模型有现实机会显著推进，例如证明若干大类 H、找出更强充分条件、排除常见反例族，或把问题归约到一个清晰的新结构命题。但由于结论覆盖所有无孤立点图 H，且需要从树和团两个极端假设推出全局线性 Ramsey size，完整解决仍很可能需要新的组合洞察。

### 免责声明

以上是对 AI 辅助可解性和推进潜力的审查，不是该 Erdős 问题的证明或反例。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `likely_open`
- 状态信心: `medium`
- 可行动性: `research_ready`
- 人工复核: `not_required`
- 独立研究 Prompt: [prompts/problem_568.md](../../prompts/problem_568.md)

### 状态结论

该题很可能仍开放。Erdős Problems 当前页面在 2026-01-18 编辑时仍标为 open，论坛线程无评论或解答声称；定向检索到的 2024–2026 工作解决或推进了若干特定 Ramsey-size-linear 图类，但没有找到证明或反例来解决本题的“树上的线性界加团上的二次界蕴含 Ramsey size linear”这一一般蕴含。数据库自己明确说明 open 标签只是站长的当前判断，故只能定为 likely_open，而非 confirmed_open。

### 当前规范陈述

设 G 为固定有限图。对有限图 A、B，R(A,B) 表示最小的 N，使得 K_N 的每个红蓝边染色均含一个红色的 A 的非诱导副本，或一个蓝色的 B 的非诱导副本。记 f(n)=O_G(g(n))，表示存在只依赖固定图 G、且不依赖 n 或任何变动图的常数。假设：(i) 存在 C_T(G)，使对每个 n>=2 和每棵 n 顶点树 T，R(G,T)<=C_T(G)n；(ii) 存在 C_K(G)，使对每个 n>=2，R(G,K_n)<=C_K(G)n^2。是否必存在 C(G)，使对每个无孤立点、边数 m=e(H)>=1 的有限图 H，均有 R(G,H)<=C(G)m？等价地，G 是否必为 Ramsey size-linear？

```text
Let G be a fixed finite graph. For finite graphs A,B, let R(A,B) be the least N such that every red-blue colouring of E(K_N) contains a red non-induced copy of A or a blue non-induced copy of B. Write f(n)=O_G(g(n)) if there is a constant depending only on G and independent of n and of all varying graphs. Assume that (i) there is a constant C_T(G) such that, for every n>=2 and every tree T on n vertices, R(G,T)<=C_T(G)n; and (ii) there is a constant C_K(G) such that, for every n>=2, R(G,K_n)<=C_K(G)n^2. Does it follow that there is C(G) such that, for every finite graph H with no isolated vertices and m=e(H)>=1, R(G,H)<=C(G)m? Equivalently: must G be Ramsey size-linear?
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 对当前字面题述（H 无孤立点）未发现能直接否定蕴含的简单构造。对历史转录中漏掉无孤立点条件的版本，则存在明显的退化问题：可在固定边图上附加任意多孤立顶点，因此按边数的统一界不应作为该版本的规范目标。
- 版本变化: EFRS93（1993）提出该问题。UCSD 的旧题集页面以同一树/团测试条件列出问题，但其文字版本未写 H 无孤立点。当前 Erdős Problems #568 明确写入“m edges and no isolated vertices”，并将其解释为 Ramsey size-linear；这与 EFRS93 论文摘要及后续标准定义一致。未发现本一般问题被后续论文替换、分裂或解决的证据。

陈述问题：

- 题面未显式说 G 固定，也未说明 \ll 的隐含常数依赖；但“is G Ramsey size linear?”及文献中的标准定义确定了常数应只依赖 G。
- “for any tree T_n”必须指同一个常数对所有 n 阶树一致有效；不能对每棵树另取常数。
- 原始 UCSD 题集页面的转录写作“any graph H with n edges”，未写“no isolated vertices”；当前 Erdős Problems 页面和 EFRS93 的定义均加了无孤立点条件。该条件不可省略：若将孤立点当作非诱导子图中的实际顶点要求而允许任意多孤立点，则固定边数不能控制所需顶点数。
- 原文两处都用 c，而当前 \ll 记号可允许不同常数；这不改变问题，因为可取两常数的最大值。

需要固定的量词/约定：

- G is fixed before quantifying n, T, H, and all implicit constants.
- The tree hypothesis is uniform over every tree on n vertices and over all n.
- The conclusion requires one constant C(G), uniform over every isolate-free H; it may not depend on H, m, v(H), maximum degree, or a decomposition of H.
- The restriction e(H)>=1 avoids empty-graph convention issues.

### 文献与当前边界

已核验的主要结果：

- EFRS93：若连通 G 满足 e(G)<=v(G)+1，则 G Ramsey size-linear；若 e(G)>=2v(G)-2，则 G 非 Ramsey size-linear，且界在相应意义下 sharp。
- Bradač–Gishboliner–Sudakov（SIAM J. Discrete Math., 2024）：所有至少 6 顶点的 K4-细分图 Ramsey size-linear；对 K4* 证明了第二图 H 为二分图时 R(K4*,H)=O(e(H))。
- Wigderson（European J. Combin., 2025）：证明存在无穷多个极小非 Ramsey-size-linear 图，解决的是另一问题，并未给出本题测试条件的充要刻画。
- Cambie–Freschi–Morawski–Petrova–Pokrovskiy（2026 预印本）：对固定环 C_k 给出 R(C_k,H)<=2e(H)+O_k(1) 的强结果（在边数相对 k 足够大时），所以为特定 G 类提供线性结论。
- Hng–Ji–Lamaison（2026 预印本）：给出关于奇环的进一步量化界及 clique/multicolour 推广；不是本题的证明或反例。

最近相关工作：截至审计日，直接检索到的最新相关预印本是 Hng、Ji、Lamaison 的 arXiv:2603.25453（2026-03-26）以及 Cambie 等人的 arXiv:2601.10238（2026-01-15）。两者推进的是环作为固定第一图时的 size-linear 问题；其摘要和可检索正文均未宣称解决 #568。

剩余核心：对任意固定 G，证明或反驳：树测试 R(G,T)=O_G(v(T)) 与团测试 R(G,K_n)=O_G(n^2) 是否共同推出对所有无孤立点 H 的 R(G,H)=O_G(e(H))。已知的特殊 G 类、以及仅把 H 限制为二分图或环的结果都不消除此一般量词。

已使用方法：

- EFRS93 使用固定图的边/点稠密度来给出 size-linear 与非 size-linear 的充分条件及随机/局部引理型下界。
- Bradač–Gishboliner–Sudakov 使用平均法、凸性和 dependent random choice；也利用树宽与 R(H,K_n) 的关系。
- 近年的环结果采用针对环结构的嵌入与 Ramsey 论证，不能直接视为一般 G 的闭包定理。

争议或不确定性：

- 当前题库明确警告其 open 标签不是完备文献证明；定向搜索未找到相反的解答声称，但不能逻辑排除未索引的新稿。
- UCSD 历史题集的 H 表述缺少“no isolated vertices”，而当前页与同行评审原文的定义包含该条件；后续研究必须采用当前的无孤立点版本。
- 2026 年两篇环论文均为预印本，且即使其结果成立也只覆盖特定固定图，不能外推为 #568 的解。

### 证据来源

- [Erdős Problem #568](https://www.erdosproblems.com/568) — Thomas F. Bloom / Erdős Problems, 2026-01-18; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 当前页面逐字给出本题、标为 OPEN、列 EFRS93 为来源、称其等价于 Ramsey size linear，并显示无论坛解答声称；页面同时警告 open 状态仅反映站长判断。
- [LaTeX source for Erdős Problem #568](https://www.erdosproblems.com/latex/568) — Thomas F. Bloom / Erdős Problems, 2026-01-18; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 核对了当前题面 LaTeX 转录：树条件、团条件和结论中的“no isolated vertices”与输入相符。
- [Erdős Problem #568 discussion thread](https://www.erdosproblems.com/forum/thread/568) — Erdős Problems forum, date unknown; `forum`, `informal_claim`, directness=`direct`, reliability=`medium`. 线程显示没有评论，故未发现该论坛中的解答或反例声称。
- [A linear bound on some size Ramsey numbers for trees](https://mathweb.ucsd.edu/~erdosproblems/erdos/newproblems/SizeRamseyLinearTree.html) — Erdős problems in graph theory collection, date unknown; `secondary_index`, `informal_claim`, directness=`direct`, reliability=`medium`. 保存了题集 #33 的历史转录和 EFRS93 书目信息；该版本未在 H 的短句中写出无孤立点限制，构成转录差异的证据。
- [Ramsey Size Linear Graphs](https://doi.org/10.1017/S096354830000078X) — Paul Erdős, R. J. Faudree, C. C. Rousseau, R. H. Schelp, 1993-12; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 原始 EFRS93 论文。期刊摘要定义 Ramsey size-linear 为：对任意无孤立点、n 条边的 H，有 r(G,H)<=Cn；并报告 q>=2p-2 时非 size-linear、连通且 q<=p+1 时 size-linear，且两阈值均 sharp。
- [On Ramsey size-linear graphs and related questions](https://arxiv.org/abs/2202.10388) — Domagoj Bradač, Lior Gishboliner, Benny Sudakov, 2024; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 证明所有至少 6 顶点的 K4-细分图是 Ramsey size-linear，并对 K4* 得到所有二分 H 的线性界；文章仍把更广的相关问题表述为未解，不给出 #568 一般蕴含的解答。
- [Infinitely many minimally non-Ramsey size-linear graphs](https://arxiv.org/abs/2409.05931) — Yuval Wigderson, 2025-08; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 给出 Ramsey size-linear 的标准 O_G(e(H)) 定义，并证明存在无穷多个极小非 Ramsey-size-linear 图；该结果不判定本题的两个测试条件是否充分。
- [Ramsey number of a cycle versus a graph of a given size](https://arxiv.org/abs/2601.10238) — Stijn Cambie, Andrea Freschi, Patryk Morawski, Kalina Petrova, Alexey Pokrovskiy, 2026-01-15; `preprint`, `preprint`, directness=`indirect`, reliability=`high`. 声称对每个固定环 C_k 和任意无孤立点、m 条边 H，R(C_k,H)<=2m+floor((k-1)/2)（m 相对 k 足够大），从而解决一个特定环问题；并非本题的一般蕴含。
- [Ramsey size linear and generalization](https://arxiv.org/abs/2603.25453) — Eng Keat Hng, Meng Ji, Ander Lamaison, 2026-03-26; `preprint`, `preprint`, directness=`indirect`, reliability=`high`. 对奇环与任意无孤立点图给出新的上界，并讨论 clique/multicolour 推广；未声称解决树/团测试蕴含的一般问题。

### 完成标准

- 肯定出口: Prove that for every fixed finite G satisfying the two stated uniform hypotheses, one constant C(G) satisfies R(G,H)<=C(G)e(H) for every finite isolate-free H with e(H)>=1.
- 否定出口: Exhibit one fixed finite graph G; rigorously prove both uniform hypotheses for that same G; and give isolate-free graphs H_i with R(G,H_i)/e(H_i) unbounded.

不构成完成：

- Proving the conclusion only for H in a restricted class such as trees, cliques, connected graphs, bipartite graphs, bounded-degree graphs, or cycles.
- Obtaining O_G(e(H) log e(H)), O_G(e(H)^{1+epsilon}), or a bound whose constant depends on H or its extra parameters.
- Showing R(G,K_n)=O(n^2) without establishing the uniform tree hypothesis, or conversely.
- Finite computations or numerical experiments that do not prove a uniform asymptotic statement.

正确性陷阱：

- Check the red/blue ordering and use of non-induced copies in each imported Ramsey theorem.
- Check that every O-constant is uniform over the full quantified family and depends only on fixed G.
- Do not replace e(H) by v(H) without tracking the direction: isolate-free gives v(H)<=2e(H), but this alone does not prove the desired Ramsey inequality.
- A proposed counterexample must verify both hypotheses for exactly the same G before using an H-family.
- Keep the no-isolated-vertices condition: dropping it changes the intended problem materially.

### 更新后的 AI 可解答性

- 等级: `low_candidate`
- 分数: `12/100`
- 信心: `medium`
- 结论: 该题已足够清晰，可作为研究代理的 proof-first 目标；但它是一个宽泛的条件式 Ramsey 蕴含，已知方法覆盖的是特定图类，且没有已知的结构刻画将两个测试条件闭合到任意 H，因此 AI 独立完成的概率低。

支持理由：

- 肯定和否定均有明确、可审计的统一常数证书。
- 存在近期的结构性部分结果、树宽界及特殊图类结果，可形成可验证的引理目标。

主要障碍：

- 前提涉及对所有树和所有团的渐近 Ramsey 行为，结论又涉及所有无孤立点图；这不是有限计算能判定的性质。
- 现有结果主要利用固定 G 的特殊结构，尚无证据表明它们可由两个抽象测试条件推出。
- 反例路线同样困难：必须为同一 G 严格证明两个前提，并构造超线性的 H 家族。

Proof-first 路线：

- 先寻求或证明一个结构闭包引理：将任意无孤立点 H 分解为能由树测试和团测试控制的部件，并逐步核查常数是否仍只依赖 G。
- 并行研究反例候选：从已知极小非 Ramsey-size-linear 图出发，逐个审计其团测试是否可能仍为二次；只有先证实两个前提才值得构造 H 家族。
- 将近期的 K4-细分、二分目标图和环结果作为测试案例，提炼它们实际使用的额外结构，防止把特例误当作一般引理。

需要验证：

- 持续监测 arXiv、作者主页和期刊在线优先出版物，特别是 2026-07-27 之后的更正或新解。
- 若采用任何 EFRS93 的细部引理，应取得全文并按定理编号而非只依赖摘要核对。
- 对任何声称的归约，逐项检查所有隐含常数的依赖。

### 审计限制与人工复核理由

- 开放状态不能由未找到论文逻辑证明；当前结论依赖于 2026-01 的题库记录、空论坛以及对精确短语和近年文献的定向检索。
- EFRS93 的可访问期刊页提供摘要和书目信息，但本审计未逐页检查其付费全文；对其细部定理的使用仅限于摘要及后续论文一致陈述的范围。
- 2026 年相关成果中有预印本；它们被作为领域进展记录，而非作为本题状态的决定性证据。
- 历史 UCSD 页面与当前页在“no isolated vertices”短语上不一致；规范题述采用当前页、EFRS93 定义和后续文献共同支持的无孤立点版本。

- 无

<!-- DEEP_REVIEW:END -->
