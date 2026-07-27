# Problem 62

## 基本信息

- 原始链接: https://www.erdosproblems.com/62
- LaTeX 页面: https://www.erdosproblems.com/latex/62
- 原始状态: `open`
- 奖金: `no`
- 主类别: `graph theory`
- 原始标签: `graph theory`
- 形式化状态: `no`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

If $G_1,G_2$ are two graphs with chromatic number $\aleph_1$ then must there exist a graph $G$ whose chromatic number is $4$ (or even $\aleph_0$) which is a subgraph of both $G_1$ and $G_2$?

## AI 完成可能性判断

- 结论: **AI 可能做出局部推进或搜索反例，但完整解决把握不足**
- 等级: `low_to_medium_candidate`
- 分数: `42/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 题面或备注出现有限对象/计算线索

### 主要障碍

- 题面含渐近/无限对象线索：sufficiently large

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: graph theory
- 证明密集标签命中: 无
- 有限/计算线索: chromatic, finite, graph
- 渐近/无限线索: sufficiently large
- 构造/存在性线索: find

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **低到中等候选：GPT-5.5 级别模型不太可能直接解决原问题，但有一定机会通过文献检索、模型论/集合论图论梳理、反例模式搜索和形式化局部引理，显著推进其可判定的子问题或澄清条件版本。**
- 等级: `low_to_medium_candidate`
- 分数: `38/100`
- 信心: `medium`
- 可能路线: 较现实的路线不是直接证明或否定命题，而是先把问题拆成有限 4-色高围长图的不可避免性、可数无穷色公共子图、以及有限族版本三类目标；再检索围长、无穷色数、Erdos-Hajnal-Shelah 型定理的后续结果，寻找是否已有一致性结果、独立性现象或已知构造。计算工具主要用于小型有限图族和候选反例结构的搜索；形式化证明工具可用于验证组合引理，但难以承载核心集合论构造。

### 支持理由

- 题目表述短，但包含清晰的核心对象：两个色数为 aleph_1 的图是否必有共同 4-色或可数无穷色子图，适合被拆成若干明确的子命题。
- 备注给出一个关键已知锚点：每个 aleph_1-色图包含所有足够大的奇圈，因此 3-色公共子图已知，真正门槛集中在 4-色或 aleph_0-色。
- Erdos 的猜测性备注暗示可从“所有足够大围长的 4-色图是否不可避免”入手，这给模型提供了可检索、可形式化、可局部推进的路线。
- 模型可利用文献检索工具系统整理无穷色图的不可避免有限子图结果，并检查是否存在已知的强形式、弱形式或一致性反例。
- 反例搜索虽不能直接覆盖 aleph_1 规模，但可以帮助发现有限模式、构造模板或验证候选 4-色高围长图族之间的嵌入关系。

### 主要障碍

- 原问题处在无穷图论和集合论组合交界处，核心难点可能依赖深层构造，而非有限计算可穷尽搜索。
- 色数 aleph_1 的图非常大，普通 SAT/SMT/图搜索工具只能验证有限影子，无法直接证明全局存在性。
- 若问题存在独立性或需要额外集合论公理，模型很难仅凭常规证明搜索给出可靠结论。
- 题目要求共同子图，而非单个图中的不可避免子图；即使分别证明每个 aleph_1-色图含有某类 4-色图，也还需保证两图共享同构类型。
- 形式化程度为 no，首先需要精确定义子图、同构公共子图、色数和基数语义，这本身会增加验证成本。

### 需要的验证

- 检索并核对 Erdos-Hajnal-Shelah 相关定理及后续工作，确认“足够大奇圈”结果的准确适用范围。
- 确认当前文献中是否已有本问题的部分解、等价表述、一致性结果或反例构造。
- 把“公共子图”的语义固定为同构公共子图，并区分有限 4-色、可数 4-色、以及 aleph_0-色三种目标。
- 对候选推进路线中的每个组合引理进行人工专家审查，尤其检查无穷基数、紧致性和子图嵌入步骤。
- 若模型提出反例，需要验证其两个图确有色数 aleph_1，且不存在任何 4-色或 aleph_0-色共同子图。

### 公开版思考摘要

这个问题对 AI 的吸引力在于目标非常清楚，而且已有 3-色层面的正结果作为基准；但真正的 4-色门槛很可能触及无穷图论中的深层不可避免子结构问题。GPT-5.5 配合工具更可能做出有价值的文献地图、等价化、弱版本证明、候选构造排错和局部引理验证，而不是一次性完成原开放问题。综合看，它不是完全不适合 AI，但直接解决概率偏低。

### 免责声明

以上是对 GPT-5.5 级别模型可推进性的审查，不是该 Erdős 问题的证明、反例或最终数学结论。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `likely_open`
- 状态信心: `medium`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_62.md](../../prompts/problem_62.md)

### 状态结论

截至审计日，未发现可检查的解决或反例。Erdős Problems 的当前条目仍将该问题列作开放问题，其 LaTeX 页面和修订历史给出相同陈述；2020 年的专家讲义也仍将其明确列为问题。该状态未达到高置信“confirmed_open”，因为未找到该问题的近期同行评议状态综述或可访问的题目专属论坛讨论，且“未检出解答”本身不是不存在解答的证明。

### 当前规范陈述

在 ZFC 下，图均为简单、无向、无环图。对任意满足 χ(G_1)=χ(G_2)=ℵ_1 的两图 G_1,G_2，是否存在图 H，使 χ(H)=4，且 H 分别作为（不要求诱导的）子图嵌入 G_1 与 G_2？“同时为二者的子图”指存在到二者的同构嵌入，而非二者顶点集实际相交。原文“or even ℵ_0”表示更强版本：把 χ(H)=4 改成 χ(H)=ℵ_0。题面中的“两图”是主目标；备注中的任意有限族版本是额外加强，不能由两图结论直接迭代得到。

```text
Work in ZFC with simple undirected loopless graphs. For every pair of graphs G_1,G_2 satisfying chi(G_1)=chi(G_2)=aleph_1, does there exist a graph H with chi(H)=4 and injective graph embeddings H -> G_1 and H -> G_2? Here “a subgraph of both” means isomorphic copies as (not necessarily induced) subgraphs; it does not require the vertex sets of G_1 and G_2 to overlap. The parenthetical “or even aleph_0” denotes the stronger variant obtained by replacing chi(H)=4 with chi(H)=aleph_0. The displayed pair statement is the primary target; the finite-family statement in the remarks is a further, not automatically equivalent, strengthening.
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 已针对“common 4-chromatic subgraph”“triangle-free subgraphs”“finite subgraphs of uncountably chromatic graphs”及问题号检索，并检查了已知移位图、有限子图增长和一致性构造的文献摘要。未找到一对 χ=ℵ_1 图且被证明没有任何共同 4-色子图的构造，也未找到该命题的完整证明。Lambie-Hanson 的结果说明不存在统一大小的有限 4-色强制见证，但这不能推出可随图对变化的共同子图不存在。
- 版本变化: Erdős Problems 的公开修订历史显示 2025-10-20 的版本与现行题面及备注实质相同；未显示数学性修订。现行备注还记录了 Erdős 在 Er87 中提出的任意有限族加强，以及“足够长奇圈”已知结果。Er87 的书目信息可由 AMS 卷页核验，但本次未取得并逐页检查该文全文，故不把其未核验措辞当作额外定理。

陈述问题：

- “or even ℵ_0”不是一个单一等价断言：χ(H)=4 是弱目标，χ(H)=ℵ_0 是严格更强的独立目标；审计和后续研究必须分别报告。
- “subgraph of both”按无限图论惯例应理解为 H 的同构副本分别嵌入两图，且不是 induced subgraph；若误作诱导子图或字面顶点交集，问题会变成不同命题。
- 题面精确假设为 χ(G_i)=ℵ_1。许多二手资料用“uncountably chromatic”表述，可能意为 χ(G)>ℵ_0；不能未经证明地把只适用于较宽范围或额外基数假设的结果替换到精确 ℵ_1 命题。
- 备注所称任意有限个图的公共子图是加强，而非由两图版本直接推出：第一次所得公共 4-色图并不满足可再次应用命题的 ℵ_1 色前提。

需要固定的量词/约定：

- The weak target is: for every ordered pair (G_1,G_2) with chi(G_i)=aleph_1, there exists an abstract graph H, allowed to depend on the pair, with chi(H)=4 and embeddings into both factors.
- The stronger target replaces chi(H)=4 by chi(H)=aleph_0; it does not merely ask for infinitely many finite 4-chromatic common graphs.
- No bound on |H| is stated. H may be finite for the 4-chromatic target, but a proof may not assume this without establishing it.
- The relation is non-induced subgraph containment. All edges of H must map to edges of each G_i; nonedges need not map to nonedges.
- The current record separately mentions the stronger assertion for every finite collection; that assertion is not the literal pair problem.

### 文献与当前边界

已核验的主要结果：

- Erdős–Hajnal–Shelah（1974，同行评议会议论文）证明：若 χ(G)>ℵ_0，则存在阈值，使 G 包含所有超过该阈值长度的奇圈。因此对任意 G_1,G_2（χ=ℵ_1），选取两个阈值的最大值即可得到共同的充分长奇圈；这完全解决了相应的 3-色版本，而没有给出 4-色见证。
- Komjáth–Shelah（2005，J. Graph Theory）回顾：固定有限二部图在每张不可数色数图中均出现；另一方面，每个预先固定的奇圈可在适当的大色数图中避免。这与 EHS74 的“对每一张图，所有足够长奇圈出现”相容，说明阈值依赖于图。
- Komjáth–Shelah（2005）给出一致性结果：可构造 χ=|G|=ℵ_1 的图，使任意 n-色子图必须任意大。Lambie-Hanson（2020，Adv. Math.）将对应的任意有限见证大小增长结论在 ZFC 中证明。由后者透明地推出：不存在一个固定有限 4-色图 H 能嵌入每张 χ=ℵ_1 图；但本题允许 H 依赖于 (G_1,G_2)，故该推论不构成反例。
- Halevi–Kaplan–Shelah（2023/2024，JEMS）在稳定图且色数远大于 ℵ_1 的情形得到强 Taylor 猜想的一种版本。它提供了结构化子类中的正向技术背景，但不能推广为本题的无条件结论。

最近相关工作：直接围绕本题的近期可检查状态证据是 Lambie-Hanson 2020 的有限子图谱工作及其 2020 专家讲义中的未解提问；2023–2025 年检索到的 Bowler–Pitz 与 Halevi–Kaplan–Shelah 工作研究不可数色数图的其他结构性质或受限子类，均未声称解决共同 4-色子图问题。

剩余核心：在 ZFC 中，给定任意两张恰有色数 ℵ_1 的图，证明或反驳它们的有限（或可能无限）子图谱之交必含某个色数恰为 4 的图。更强的 χ(H)=ℵ_0 版本以及任意有限族版本仍须与主问题明确分离。

已使用方法：

- Erdős–Hajnal 型无限组合论与移位图：用于控制大色数图可避免的短奇圈及有限子图谱。
- 紧致性/有限见证思想：每张非 3-可着色图各自含有限 4-色子图，但这不产生两图共同的同构类型。
- 集合论构造、forcing、club guessing 与 Hajnal–Máté 图：用于构造有限高色子图必须很大的 χ=ℵ_1 图。
- 模型论稳定性、EM 模型和移位图嵌入：仅在稳定及极高色数等额外假设下得到正向结构结果。

争议或不确定性：

- 未找到题目专属论坛线索；对“无论坛讨论”的判断只是检索结果，不是其不存在的证明。
- 未取得 Er87 全文，故只能核验其书目信息及数据库对其内容的转述。
- 二手材料中的“uncountably chromatic”有时比题面 χ=ℵ_1 更宽；任何声称解决本题的论证都必须逐项核对这一量词和基数差异。
- 未发现相互冲突的已发表正反结论；但缺乏 2020 年后直接讨论本题的论文，故开放状态保留中等置信。

### 证据来源

- [Erdős Problems — Problem 62](https://www.erdosproblems.com/62) — Erdős Problems, date unknown; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 当前数据库记录的题号、开放标签、题面和参考文献来源；数据库标签本身仅作状态证据而非证明。
- [Erdős Problems — LaTeX for Problem 62](https://www.erdosproblems.com/latex/62) — Erdős Problems, date unknown; `problem_page`, `database_record`, directness=`direct`, reliability=`high`. 可检查的现行题面、备注及 EHS74、Er87 书目信息；明确为两张 χ=ℵ_1 图、公共 χ=4（或更强 χ=ℵ_0）子图。
- [Revision history of Erdős Problem 62](https://www.erdosproblems.com/history/62) — Erdős Problems, 2025-10-20; `problem_page`, `database_record`, directness=`direct`, reliability=`high`. 现行陈述及 2025-10-20 修订记录；未见题面数学性改写。
- [Logic and Combinatorics, Contemporary Mathematics 65](https://www.ams.org/books/conm/065/) — American Mathematical Society, 1987; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 核验 P. Erdős 的《Some problems on finite and infinite graphs》确为该卷 pp. 223–228 的原始出处。
- [On Some General Properties of Chromatic Numbers](https://www.renyi.hu/~p_erdos/1974-17.pdf) — Paul Erdős, András Hajnal, Saharon Shelah, 1974; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 原始论文的 Theorem 3 证明：每个 χ>ℵ_0 的图包含所有充分长的奇圈；故任意两张 χ=ℵ_1 图有共同 3-色子图。
- [Uncountable-chromatic graphs have common 4-chromatic subgraphs](https://mathweb.ucsd.edu/~erdosproblems/erdos/newproblems/FourChromaticSubgraph.html) — Erdős problem archive at UCSD, date unknown; `secondary_index`, `informal_claim`, directness=`direct`, reliability=`medium`. 独立历史问题索引以完全相同的两图 χ=ℵ_1 / 共同 4-色子图形式列出问题，并说明 EHS74 只给出 3-色的肯定结论。
- [Finite subgraphs of uncountable graphs](https://speakerdeck.com/clambiehanson/finite-subgraphs-of-uncountable-graphs) — Chris Lambie-Hanson, 2020; `author_page`, `informal_claim`, directness=`direct`, reliability=`medium`. 第 114–116 页仍将“两个不可数色数图是否有共同 4-色子图”作为问题，并与相关未解问题并列；这是近期专家讲义，非解决证明。
- [Finite Subgraphs of Uncountably Chromatic Graphs](https://shelah.logic.at/files/95375/788.pdf) — Péter Komjáth, Saharon Shelah, 2005-02-25; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 回顾 Erdős–Hajnal 对每张不可数色数图必含有限图的分类：固定有限二部图均必含，而固定奇圈可被某些大色数图避开；并给出与有限子图谱有关的一致性结果。
- [Finite subgraphs of uncountably chromatic graphs](https://onlinelibrary.wiley.com/doi/abs/10.1002/jgt.20060) — Péter Komjáth, Saharon Shelah, 2005-02-25; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 同行评议版本的摘要核验：一致地可令 χ=|G|=ℵ_1 且每个 n-色子图任意大；该结果未处理两图共同 4-色子图。
- [On the growth rate of chromatic numbers of finite subgraphs](https://arxiv.org/abs/1902.08177) — Chris Lambie-Hanson, 2019-02-21; `preprint`, `preprint`, directness=`indirect`, reliability=`high`. 给出 ZFC 构造：对任意 f，存在 χ=ℵ_1 图，其小于 f(k) 个顶点的子图均非 k-色；说明不存在统一大小的有限高色数强制见证。
- [On the growth rate of chromatic numbers of finite subgraphs](https://doi.org/10.1016/j.aim.2020.107176) — Chris Lambie-Hanson, 2020-08-01; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 上述有限子图增长定理的同行评议发表版本；它是本题的重要障碍信息而非正反解答。
- [Infinite stable graphs with large chromatic number II](https://ems.press/journals/jems/articles/11115712) — Yatir Halevi, Itay Kaplan, Saharon Shelah, 2023-06-15; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 在稳定图且 χ(G)>beth_2(ℵ_0) 的额外假设下，证明强 Taylor 猜想的一个版本；其门槛和类别均不覆盖本题任意 χ=ℵ_1 图。
- [A Note on Uncountably Chromatic Graphs](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v32i1p23/pdf/) — Nathan Bowler, Max Pitz, 2025-02-14; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 近期 ZFC 构造显示不可数色数图可缺少不可数无限连通子图；展示该领域对象的结构多样性，但不证明本题任一方向。

### 完成标准

- 肯定出口: A complete affirmative resolution is a ZFC proof that for every pair of simple graphs G_1,G_2 with chi(G_1)=chi(G_2)=aleph_1, one can construct or prove the existence of one graph H with chi(H)=4 and embeddings H -> G_1 and H -> G_2. A separate proof is required for the stronger chi(H)=aleph_0 version.
- 否定出口: A complete negative resolution is a ZFC construction of a pair G_1,G_2 with chi(G_1)=chi(G_2)=aleph_1 together with a proof that no graph H of chromatic number 4 embeds as a non-induced subgraph into both. A model-specific pair alone establishes at most a relative-consistency result unless the intended conclusion is explicitly an independence theorem and both sides are proved.

不构成完成：

- Showing that each G_i separately has some finite 4-chromatic subgraph, without proving that the two witnesses are isomorphic.
- Finding a common odd cycle or any other 3-chromatic graph; EHS74 already supplies this kind of conclusion.
- Exhibiting a fixed 4-chromatic graph in a restricted class of graphs, or under an additional axiom, without matching the ZFC universal quantifier.
- Proving a common graph homomorphism image rather than a common subgraph embedding.
- Proving the statement for chi(G_i)>beth_2(aleph_0), for stable graphs, or for graphs of a prescribed construction only.
- Using a finite search as evidence for the universal infinite-graph assertion without a theorem reducing the assertion to that finite search.

正确性陷阱：

- Do not replace chi(G_i)=aleph_1 by merely 'uncountable' or by an unproved hereditary reduction from larger cardinals.
- Check that H has chromatic number exactly 4, not merely at least 4 or at most 4.
- Check that containment is non-induced graph embedding; induced-containment arguments do not settle the stated problem.
- Do not infer the finite-family strengthening by iterating a pair result: the intermediate common graph need not be aleph_1-chromatic.
- Treat 'or even aleph_0' as a stronger target, not as synonymous with the 4-chromatic target.
- Track whether a construction is in ZFC, uses diamond/CH/forcing, or is only a relative consistency result.
- When using the EHS odd-cycle theorem, retain the graph-dependent threshold; it cannot supply a fixed nonbipartite universal finite graph.

### 更新后的 AI 可解答性

- 等级: `low_candidate`
- 分数: `12/100`
- 信心: `medium`
- 结论: 这是定义清楚但高度集合论化的开放目标；可进行严谨的结构性探索和反例审计，但目前不适合把有限计算或一般语言模型搜索视为高概率解题路线。分数只评估弱的共同 χ=4 子图主目标，不包括已知的共同 3-色结论或更强的 χ=ℵ_0 版本。

支持理由：

- 量词、嵌入关系及精确色数目标可以形式化；正反解都具有可审计的明确证书。
- EHS74、移位图和有限子图谱结果给出可检验的障碍与若干自然中间引理。
- 该问题已长期存在，且近期工作解决了相邻问题而未触及它，表明不是简单遗漏的有限构造。

主要障碍：

- 必须处理任意 χ=ℵ_1 图，而非稳定图、特定移位图或受强公理控制的图。
- Lambie-Hanson 的任意慢有限子图出现结果排除了依赖统一小见证的路线。
- 文献中存在大量一致性现象；将模型内反例误报为 ZFC 反例的风险很高。
- 有限计算没有对任意不可数图的自然完备性或停止准则。

Proof-first 路线：

- 把问题重述为两张图的非诱导有限子图同构谱之交是否必含 4-色图，并先证明或反驳适用于该谱交的结构引理。
- 分析 EHS 奇圈证明能否提升为一族共同的非二部有限图，并精确定位从色数 3 到 4 失效的步骤。
- 以移位图、Specker 图和 Hajnal–Máté 图等已知障碍族为测试对象，寻求可证明的不相容嵌入不变量；任何候选反例必须同时核验两图的 χ=ℵ_1。
- 把集合论模型假设显式参数化：先判定一个构造是 ZFC 反例、相对一致性反例，还是只排除某个证明策略。

需要验证：

- 由领域专家或作者核查 2020 年后是否有未被通用检索索引的论文、预印本或论坛结论。
- 取得并检查 Er87 全文，以核对有限族和“大 girth 的所有 4-色图”措辞的原始上下文。
- 若出现正反声称，逐项审计 χ=ℵ_1、非诱导嵌入、ZFC/额外公理和“恰为 4”的证明。

### 审计限制与人工复核理由

- 本审计执行了定向公开检索并检查了可访问的原始或同行评议来源，但不是 MathSciNet、zbMATH、全部引文数据库及私人通信的穷尽搜索。
- Erdős Problems 的当前题目页本身在浏览器提取时发生内部错误；其 LaTeX 页和公开修订历史可访问并给出同一题面。
- 未找到题目专属论坛线程；这只说明按问题号、精确措辞和站内路径的检索未定位到可访问线程。
- Er87 的 AMS 卷和书目信息已核验，但本文全文未取得，故其历史性延伸措辞依赖数据库转述。
- “likely_open”反映截至审计日的证据强度，并非对未来或未索引结果不存在的逻辑证明。

- 建议由无限图论/集合论专家或题目维护者确认 2020 年后是否有未索引的预印本、讲义更新、私人已知结果或论坛讨论。
- 应取得 Er87 全文，核对原题、有限族加强及大 girth 推测的原始量词。
- 若后续代理报告解决或反例，必须进行独立的集合论假设、精确 χ=ℵ_1 与非诱导嵌入审计。

<!-- DEEP_REVIEW:END -->
