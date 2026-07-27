# Problem 64

## 基本信息

- 原始链接: https://www.erdosproblems.com/64
- LaTeX 页面: https://www.erdosproblems.com/latex/64
- 原始状态: `falsifiable`
- 奖金: `$1000`
- 主类别: `graph theory`
- 原始标签: `graph theory`, `cycles`
- 形式化状态: `yes`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

Does every finite graph with minimum degree at least 3 contain a cycle of length $2^k$ for some $k\geq 2$?

## AI 完成可能性判断

- 结论: **AI 辅助完成有现实候选路线，但需要外部计算或严格验证**
- 等级: `medium_candidate`
- 分数: `63/100`
- 建议路线: 优先做反例搜索和小规模枚举；若没有反例，不能据此断言问题为真。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 题面或备注出现有限对象/计算线索
- 已有形式化陈述，可降低语义误读风险

### 主要障碍

- 题面含渐近/无限对象线索：sufficiently large
- 原记录含奖金 $1000，说明该题被长期视为高价值难题；这不是否定依据，但提高验证门槛。

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: cycles, graph theory
- 证明密集标签命中: 无
- 有限/计算线索: finite, graph
- 渐近/无限线索: sufficiently large
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **中等候选。该题若为否定，存在可机器验证的有限反例；若为肯定，则需要新的结构性图论证明，难度显著更高。GPT-5.5 配合 SAT/CP-SAT、图枚举、形式化验证和文献检索，较可能在反例搜索、有限范围排除、特殊图类证明和已知定理整合上显著推进，但直接完整解决的概率仍不高。**
- 等级: `medium_candidate`
- 分数: `58/100`
- 信心: `medium`
- 可能路线: 优先走反例搜索与可验证证书路线：把问题限制到最小度 3 的有限图，尤其是三正则图或近三正则图，编码为“无 4、8、16、32、... 长度圈”的约束，用 canonical augmentation、SAT/CP-SAT、ILP 或图同构剪枝枚举候选；若发现反例，输出边表并用独立程序和形式化系统验证最小度与禁用圈长。若搜索无果，则提炼不可行证书、局部结构引理和特殊图族定理，尝试把 Liu-Montgomery 高平均度结果与低平均度核心分解之间的缺口缩小。

### 支持理由

- 问题是否定型时有短证书：一个有限图的边表即可作为反例，最小度和指定长度圈不存在性可由程序独立验证。
- formalized 为 yes，说明验证层较适合接入证明助理或小内核 checker，降低“找到候选但无法审计”的风险。
- 图论约束清晰：最小度至少 3，禁止长度为 2^k 且 k>=2 的圈，适合转成枚举、SAT、CP-SAT、ILP、SMT 或专门图搜索。
- 已知备注显示高平均度情形已有强阳性结果，因此搜索空间可被结构性定理约束，AI 可用文献检索把未知区域聚焦在低平均度、稀疏、近三正则图。
- 即使不能完整解决，也容易产出有价值的阶段性成果：扩大无反例计算范围、证明若干图族、生成最小潜在反例约束、形式化已有归约。

### 主要障碍

- 若命题为真，完整证明很可能需要新的深层稀疏图结构论，而不只是计算搜索。
- 若命题为假，最小反例可能很大，且禁止多个 2 的幂长度圈会导致全局约束，朴素枚举会迅速爆炸。
- 只检查三正则图或小阶图不足以覆盖全部最小度至少 3 的图，需要可靠的归约或覆盖论证。
- 验证“没有某些长度圈”虽然可计算，但对大图需要高可信的独立 checker，避免图搜索程序本身的漏洞。
- 已有高平均度结果与最小度 3 情形之间差距很大，AI 文献整合可能只能给出局部推进而非最终闭合。

### 需要的验证

- 若给出反例，需要至少两个独立实现验证边表、最小度和所有 2^k 圈长缺失，并最好生成形式化证明证书。
- 若给出计算排除范围，需要公开枚举规则、同构剪枝方法、完整性证明和可复现实验脚本。
- 若提出理论证明，需要逐条形式化关键引理，特别是从最小度 3 到某个幂长偶圈的结构性跳步。
- 需要确认搜索范围没有隐含地只覆盖了正则图、连通图、二分图或其他未证明等价的子类。
- 需要将任何引用的高平均度或特殊图族结果精确转化为本题所需的有限图命题。

### 公开版思考摘要

这个问题对 AI 的吸引力在于它是清晰、有限、可反驳、可形式化的图论命题；反例若存在，原则上可以被发现并验证。但肯定解需要跨越从高平均度已知结果到最小度 3 的核心困难，不能指望纯枚举直接完成。综合看，GPT-5.5 更可能通过反例搜索、搜索不可行证书、特殊图族验证和形式化检查产生实质推进；完整解决属于有可能但风险较高的目标。

### 免责声明

以上不是该 Erdős 问题的解答，也不声称命题真假；这是基于所给 problem JSON 对 GPT-5.5 工具辅助可攻性的审查判断。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `confirmed_open`
- 状态信心: `high`
- 可行动性: `research_ready`
- 人工复核: `not_required`
- 独立研究 Prompt: [prompts/problem_64.md](../../prompts/problem_64.md)

### 状态结论

截至 2026-07-27，问题的有限简单图版本仍是公开且未解决的 Erdős–Gyárfás 猜想。当前 Erdős Problems 页面将其标为开放；2024–2026 年直接研究也均将一般情形称为开放，只证明了受限图类或最小反例的结构性质。Liu–Montgomery 的定理解决的是“平均度足够大”时存在某个 2 的幂长度圈，因而推翻了 Erdős–Gyárfás 所设想的任意高最小度反例的更强猜想，但没有处理最小度恰为 3 的一般情形。DeepMind 的 Lean 文件只是带 sorry 的开放问题陈述，并非证明。

### 当前规范陈述

Erdős–Gyárfás 猜想（采用有限简单无向图的标准约定）：对每个非空有限简单无向图 G=(V,E)，若其最小顶点度 δ(G)≥3，则存在整数 k≥2 以及 G 的一个简单圈 C，使得 |E(C)|=|V(C)|=2^k。等价地，G 含有长度为 4、8、16、32，……之一的简单圈。不需要连通性假设；不连通时可在任一满足最小度条件的分量中应用断言。完整解决要么证明该全称命题，要么给出一个 δ(G)≥3 且不含任何 2^k 长度简单圈的显式有限简单反例。

```text
Erdős–Gyárfás conjecture (finite simple-graph convention). For every finite, simple, undirected graph G=(V,E) with V nonempty and minimum vertex degree δ(G)≥3, there exist an integer k≥2 and a simple cycle C in G such that |E(C)|=|V(C)|=2^k. Equivalently, G contains a simple cycle of length 4, 8, 16, 32, … . No connectedness hypothesis is needed: if G is disconnected, δ(G)≥3 holds componentwise and the assertion is applied to a component. The problem asks for a proof of this universal assertion or one explicit finite simple counterexample with δ(G)≥3 and no simple cycle of any length 2^k, k≥2.
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 针对有限简单图的规范命题，未发现简单反例。无限 3-正则树确实反驳把“有限”删去后的扩张版本，但不是原命题的反例。仅避开 4 圈和 8 圈也不够：允许 16、32 等长度。已知小规模与特定图类的计算/结构结果均不构成一般反例搜索的穷尽证明。
- 版本变化: 1990 年代 Erdős 与 Gyárfás提出该最小度 3 猜想，并且提出/相信更强的否定性设想：对每个 r 存在最小度至少 r、但没有任何 2 的幂长度圈的有限图。Liu–Montgomery（2023 年 JAMS，预印本 2020）证明平均度达到某个绝对常数已足以保证存在 2 的幂长度圈，故更强的否定性设想为假；原最小度 3 猜想未被修订且仍开放。近年结果将其验证至 P13-free 图、直径 2 图等子类，并给出假设最小反例的度数结构约束。

陈述问题：

- 原始网页只写“finite graph”和“cycle”，未在句内明说简单、无向、无多重边或无环；该领域的默认约定，以及 DeepMind Formal Conjectures 中的 SimpleGraph 形式化，支持将其规范化为有限简单无向图。
- “cycle of length 2^k for some k≥2”应理解为简单圈；k≥2 明确排除了长度 1、2，目标长度从 4 开始。
- 空图的最小度在不同约定下可能未定义；这不影响规范命题，因为 δ(G)≥3 的通常语义已排除空图。
- 历史文字中“Erdős 和 Gyárfás 相信答案为负”指一个更强的、现已被推翻的高最小度反例猜想，不能误读为当前最小度 3 命题已被否定。

需要固定的量词/约定：

- Universal quantifier: for every finite simple undirected graph G with δ(G)≥3.
- Existential quantifiers: there exist k∈N with k≥2 and one simple cycle C⊆G of length exactly 2^k.
- The exponent k may depend on G; no uniform upper bound on k is asserted.
- A counterexample must avoid every permitted length 2^k, not merely 4 and 8.
- Parallel edges, loops, closed walks, and 2-cycles are outside the canonical simple-graph formulation.

### 文献与当前边界

已核验的主要结果：

- Liu 与 Montgomery（JAMS 2023；预印本 2020）证明存在绝对常数 d，使平均度至少 d 的每个有限图都含一个 2 的幂长度圈；其更强的区间偶圈结果给出某个大 ℓ，使每个偶数 m∈[(log ℓ)^8,ℓ] 都实现为圈长。因此 δ(G)≥d 的高最小度情形成立，但 δ(G)=3 的一般情形没有被覆盖。
- Gao–Shan（Graphs and Combinatorics 2022）证明 P8-free 图情形，并且实际保证 4 圈或 8 圈。
- Hu–Shen（Discrete Mathematics 2024）将该受限类推进到 P10-free，同样保证 4 圈或 8 圈。
- Hegde–Sandeep–Shashank（arXiv v2, 2025）通过计算辅助论证，将“存在某个 2 的幂圈”的受限类推进到 P13-free；该工作为预印本，且一般结论仍开放。
- Carr（arXiv v4, 2026，已接受待 BICA 发表）证明直径 2 的最小度至少 3 图含 4 圈或 8 圈。
- Carr（arXiv, 2026）给出条件性最小反例结构：若反例存在，至少 4/7 顶点为 3 度且每个顶点邻接一个 3 度顶点。其论证不排除这种图的存在。

最近相关工作：审计日可直接核验的最新一般相关预印本为 Carr, arXiv:2605.22844（2026-05-13），它明确把对象称为“最小反例”并仅得出度数结构限制；最新明确解决的受限类预印本是 Hegde–Sandeep–Shashank, arXiv:2410.22842v2（2025-02-11）的 P13-free 结果。两者都没有给出一般证明或有限反例。

剩余核心：核心剩余目标正是规范陈述本身：任意有限简单图 δ≥3 是否含某个 4、8、16、……长度的简单圈。Liu–Montgomery 已排除了“度数无限增大时仍可构造反例”的路线；若一般反例存在，它必须属于尚未被现有受限类定理覆盖的低最小度、长诱导路径的稀疏结构。

已使用方法：

- 高平均度情形：扩张子图、可调节路径长度（adjusters）及连续偶圈长度区间；见 Liu–Montgomery。
- 禁止长诱导路径情形：归纳/回溯与计算辅助的有限状态验证；P13-free 论文公开了配套程序。
- 局部结构情形：邻域配置、无 4 圈时强制 8 圈的分类论证；适用于直径 2。
- 最小反例法：删除顶点或边后保持最小度的矛盾，以及由此导出的近 3-正则度数约束。
- 有限反例搜索可作为证伪工具，但必须给出图的编码、简单性、最小度、所有允许幂次长度的完整检查及穷尽范围；它不能证明无限族上的全称命题。

争议或不确定性：

- 没有发现可审阅的一般证明或一般反例声明。当前网页自身亦明示其开放标签不是完整文献检索的保证；本审计以近期预印本、同行评议论文与形式化文件交叉核验后仍得出“确认开放”。
- P13-free 结论依赖计算辅助验证，预印本未显示同行评议发表信息；使用它作为研究背景时应审计其算法正确性、实现版本和运行证书，而不能把它升级为一般结果。
- Carr 2026 最小反例预印本是未同行评议的条件性结构结果；它的结论与开放状态相容，但不应被描述为解决或近乎解决。
- Lean 文件中的 `sorry` 意味着“formalized: yes”仅指已形式化陈述，绝不表示定理获机器验证。

### 证据来源

- [Erdős Problems — Problem 64](https://www.erdosproblems.com/64) — Thomas F. Bloom (database editor), 2026-04-10; `problem_page`, `database_record`, directness=`direct`, reliability=`high`. 给出当前有限图陈述、开放标签、历史上的更强否定性猜想，以及 Liu–Montgomery 的高平均度结果摘要；页面也警示状态并非完整文献检索的替代品。
- [A solution to Erdős and Hajnal's odd cycle problem](https://arxiv.org/abs/2010.15802) — Hong Liu; Richard Montgomery, 2020-10-29; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 摘要明确称：存在平均度阈值，使图必有长度为 2 的幂的圈；因此该定理直接否定“任意高最小度仍可避免所有 2 的幂圈”的更强猜想。arXiv 记录说明版本已获发表接受。
- [A solution to Erdős and Hajnal’s odd cycle problem](https://wrap.warwick.ac.uk/id/eprint/171505/) — Hong Liu; Richard Montgomery, 2023; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 核验 Liu–Montgomery 文章正式发表于 Journal of the American Mathematical Society 36（2023）, 1191–1234，DOI 10.1090/jams/1018。
- [Erdős-Gyárfás conjecture on graphs without long induced paths](https://arxiv.org/abs/2410.22842) — Anand Shripad Hegde; R. B. Sandeep; P. Shashank, 2025-02-11; `preprint`, `preprint`, directness=`direct`, reliability=`medium`. 作者在摘要中仍将一般猜想表述为猜想，并报告借助计算证明 P13-free 图类的情形；这是截至审计日直接相关的较新限制类进展。
- [Erdos-Gyarfas: program accompanying the Pk-free result](https://github.com/rbsandeep/Erdos-Gyarfas) — Anand Shripad Hegde; R. B. Sandeep; P. Shashank, 2025-09-20; `other`, `unknown`, directness=`indirect`, reliability=`medium`. 公开代码库将其程序定位为验证 Pk-free 图类的算法；它支持该论文的计算辅助性质，但不是对一般猜想的形式化证明。
- [Cycles of Length 4 or 8 in Graphs with Diameter 2 and Minimum Degree at Least 3](https://arxiv.org/abs/2508.19302) — Avery Carr, 2026-01-30; `preprint`, `preprint`, directness=`direct`, reliability=`medium`. 证明直径为 2、最小度至少 3 的图含 4 圈或 8 圈；arXiv 页面标明已被 BICA 接受、待发表。该结果是严格子类结果，不解决一般情形。
- [Every Minimal Counterexample to the Erdős-Gyárfás Conjecture is Predominantly Cubic](https://arxiv.org/abs/2605.22844) — Avery Carr, 2026-05-13; `preprint`, `preprint`, directness=`direct`, reliability=`medium`. 该预印本声称：若最小反例存在，则每个顶点邻接某个 3 度顶点，且至少 4/7 顶点为 3 度；这只是条件性结构缩减，不是反例或证明。
- [Erdős-Gyárfás Conjecture for P10-free Graphs](https://arxiv.org/abs/2308.05675) — Zhiquan Hu; Changlong Shen, 2023-08-12; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 摘要证明每个 P10-free、最小度至少 3 的图有长度 4 或 8 的圈；正式发表信息为 Discrete Mathematics 347（2024）, 114175。
- [Erdős-Gyárfás Conjecture for P8-free graphs](https://arxiv.org/abs/2109.01277) — Yuping Gao; Songling Shan, 2021-09-03; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 摘要证明每个 P8-free、最小度至少 3 的图有长度 4 或 8 的圈；作者主页列出其发表于 Graphs and Combinatorics 38（2022）, Article 168。
- [FormalConjectures/ErdosProblems/64.lean](https://raw.githubusercontent.com/google-deepmind/formal-conjectures/main/FormalConjectures/ErdosProblems/64.lean) — Google DeepMind Formal Conjectures Authors, 2025; `formalization`, `formalized_artifact`, directness=`direct`, reliability=`high`. 该文件以 finite SimpleGraph 和简单 cycle 的形式陈述问题，但定理体为 `by sorry` 且标注 `category research open`；它是形式化陈述，不是已核验的证明。

### 完成标准

- 肯定出口: A complete affirmative resolution is a rigorous proof that every finite simple undirected graph G with δ(G)≥3 contains a simple cycle C with |C|=2^k for some integer k≥2. The proof must cover arbitrary order, disconnected graphs, and all exponents permitted by the statement.
- 否定出口: A complete negative resolution is one explicit finite simple undirected graph G, together with a checkable certificate that δ(G)≥3 and that G has no simple cycle of length 2^k for every k≥2 with 2^k≤|V(G)|. Since G is finite, this is a finite exhaustive cycle-length verification.

不构成完成：

- Proving the claim only for cubic, planar, claw-free, bounded-diameter, P_t-free, high-girth, or high-degree graphs without a reduction from arbitrary graphs.
- Showing only that a graph has no 4-cycle or no 4- and 8-cycles; a 16-, 32-, or longer power-of-two cycle still satisfies the conjecture.
- Finding examples that are infinite, non-simple, have a loop/multiple-edge convention mismatch, or fail δ(G)≥3.
- A finite computation without a proved exhaustive search space, reproducible input/output, and a certificate covering every permitted power-of-two length.
- Citing the Liu–Montgomery high-average-degree theorem as if it implied the δ(G)≥3 case.
- A Lean declaration containing `sorry`, an informal forum assertion, or a search snippet.

正确性陷阱：

- Check that every alleged cycle is simple, not merely a closed walk; its length must be exactly 2^k with k≥2.
- For a counterexample, enumerate every power 2^k≤|V(G)|, including 16 and above, and establish absence of simple cycles at each length.
- Use minimum degree, not average degree, in the target; a graph with average degree at least 3 need not satisfy δ≥3.
- Keep the target finite and simple. Do not import the infinite-tree observation or multigraph 2-cycles into the canonical proposition.
- If reducing to a minimal counterexample, prove that each deletion/contraction preserves all hypotheses needed for the induction; degree loss is the central obstruction.
- If using computer assistance, prove the algorithm's state-space completeness and ensure the implementation's induced-path, graph-isomorphism, degree, and cycle conventions match the theorem.

### 更新后的 AI 可解答性

- 等级: `low_candidate`
- 分数: `18/100`
- 信心: `medium`
- 结论: 这是定义清楚、可被证明或有限证书反驳的研究级开放问题，但其一般低最小度核心长期未解；现有进展主要是高密度/受限图类，尚没有可见的狭窄缺口。因此适合进行严谨、分阶段的探索，当前由 AI 独立解决的概率偏低。

支持理由：

- 命题具有明确的双向完成标准；反例若存在可给出有限、可机械核验的证书。
- 有强而可审阅的高平均度定理、多个受限类定理和最小反例结构，可形成可检验的引理目标。
- 当前文献仍明确把一般情形列为开放，且不存在需先推翻的已证结论。

主要障碍：

- 最小度 3 与“平均度充分大”之间存在本质缺口；Liu–Montgomery 的工具不能直接降至固定小度。
- 若存在反例，必须同时避开无限多个随图阶增长的允许长度；局部排除 4、8 圈不足以控制 16 及以上。
- 受限诱导路径结果包含计算辅助成分，向一般图的推广没有已知停止条件。
- 小规模枚举和启发式优化只能排除有限范围，容易制造不当的进展感。

Proof-first 路线：

- 从最小反例出发，先寻求一个能严格保持 δ≥3 的可归约配置；每条归约都须证明产生的 2 的幂圈能提升/回到原图且长度不被破坏。
- 尝试将现有的“长诱导路径”分支与高平均度/扩张分支之间建立结构二分：证明任何非扩张候选反例包含可归约诱导路径配置，而不是直接枚举一般图。
- 研究循环长度集的组合性约束：需要一个能从稀疏局部结构强制某一精确 2 的幂长度的引理，而不只是获得许多任意长度圈。
- 唯一可选计算子任务：在先证明的、参数明确的最小反例结构类中寻找或排除一个局部配置；先声明引理、图编码、穷尽域和停止条件，完成后立即将资源转回证明。

需要验证：

- 对任何声称的新一般证明，进行逐引理的对抗审稿，特别核验简单圈、精确长度和最小度保存。
- 对任何反例，独立重算最小度并枚举所有 2^k≤|V| 的简单圈；最好提供可复现的 SAT/ILP/证明日志或独立实现。
- 对依赖 P13-free 文献的步骤，审阅预印本算法和公开代码是否给出足够的完备性论证。
- 在实际开展研究前再次查询 arXiv、MathSciNet/zbMATH、作者主页及 Erdős Problems 页面，以捕捉审计日之后的更新。

### 审计限制与人工复核理由

- 无法从网页接口读取 Erdős Problems 的评论正文；搜索结果确认页面仅有一条评论，且未发现该论坛有可审阅的一般证明或反例声明。
- “确认开放”是基于截至审计日的针对性公开检索、当前问题页、近期直接论文/预印本和形式化仓库，而不是对全球未公开研究的逻辑排除。
- P13-free 与部分 2026 预印本的计算或证明细节没有在本审计中逐行重验；它们只作为受限类进展记录，未作为一般状态结论的唯一依据。
- Liu–Montgomery 的阈值常数和完整定量参数未在此处重新推导；本审计只使用其摘要和正式发表记录直接支持的存在性结论。

- 无

<!-- DEEP_REVIEW:END -->
