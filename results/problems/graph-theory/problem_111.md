# Problem 111

## 基本信息

- 原始链接: https://www.erdosproblems.com/111
- LaTeX 页面: https://www.erdosproblems.com/latex/111
- 原始状态: `open`
- 奖金: `no`
- 主类别: `graph theory`
- 原始标签: `graph theory`, `chromatic number`, `set theory`
- 形式化状态: `no`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

If $G$ is a graph let $h_G(n)$ be defined such that any subgraph of $G$ on $n$ vertices can be made bipartite after deleting at most $h_G(n)$ edges.

What is the behaviour of $h_G(n)$? Is it true that $h_G(n)/n\to \infty$ for every graph $G$ with chromatic number $\aleph_1$?

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `35/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 题面或备注出现有限对象/计算线索

### 主要障碍

- 所属标签偏证明密集：set theory
- 题面含渐近/无限对象线索：\gg, \ll

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: chromatic number, graph theory
- 证明密集标签命中: set theory
- 有限/计算线索: chromatic, graph
- 渐近/无限线索: \gg, \ll
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **中等候选。GPT-5.5 级别模型配合计算、文献检索和形式化工具，较可能显著推进该问题的局部结构分析、候选构造验证和已知界限重构；但要完整解决“对每个染色数为 aleph_1 的图是否都有 h_G(n)/n 趋于无穷”很可能仍需要新的无限图组合与集合论思想，不能视为高概率可直接解决。**
- 等级: `medium_candidate`
- 分数: `58/100`
- 信心: `medium`
- 可能路线: 较现实的路线是先形式化 h_G(n) 与“删除边使诱导或任意 n 点子图二分”的等价表述，把问题转化为有限子图中最小奇环破坏集或最大二分子图缺口的下界；然后重构备注中已有的线性下界来源，即大量顶点不交奇环，并分析为何它只给 h_G(n) 远大于 n 的弱形式或不能给出极限无穷；接着针对染色数 aleph_1 的特殊构造搜索稀疏高染色无限图，尝试证明任意 n 点子图的非二分边删除数必须超线性，或反向构造 h_G(n)=O(n) 的候选反例。计算工具可用于有限模型搜索、极值猜想生成和小规模 obstruction 分类，形式化证明工具可验证有限图引理与归纳构造的局部正确性。

### 支持理由

- 问题有清晰的有限图参数 h_G(n)，可被算法化为每个 n 点子图的最小边删除到二分图问题；这适合计算实验、SAT/ILP 搜索和有限引理验证。
- 备注已经给出非平凡结构信息：染色数 aleph_1 的图必含某个长度的 aleph_1 多个顶点不交奇环，因此至少能导出线性级别下界；模型可围绕这一机制寻找加强条件。
- 已知存在染色数 aleph_1 且 h_G(n) 远小于 n^{3/2} 的图，说明目标区间相对窄：需要区分线性、超线性和 n^{1+epsilon} 级别，而不是完全无结构地搜索。
- 问题同时涉及无限图染色数、有限子图密度和奇环破坏集，适合用文献检索梳理 Erdős-Hajnal-Szemerédi 构造、稀疏不可数染色图和相关 set-theoretic graph constructions。
- GPT-5.5 级别模型可能擅长把旧证明拆成可验证模块，并提出中间命题，例如限制在特定构造族、附加稀疏性条件或特定集合论假设下的版本。

### 主要障碍

- 核心难点不是有限计算规模，而是对任意染色数为 aleph_1 的无限图给出统一超线性下界，或者构造满足精细有限子图控制的反例。
- 备注中的已知事实只保证大量不交奇环，从直觉上容易给出线性障碍，但要推出 h_G(n)/n 趋于无穷需要随 n 增长的强制奇环复杂度，这一步很可能是主要缺口。
- 涉及 aleph_1 染色数的无限图可能受集合论构造、独立性现象或额外公理影响；若问题存在模型依赖，常规计算和有限形式化无法直接解决。
- h_G(n) 对所有 n 点子图取最坏情形，既要控制局部有限结构又要保留不可数染色数，这种局部-全局张力使反例构造和下界证明都很脆弱。
- 形式化证明工具目前更适合验证明确的有限组合引理；不可数基数、图染色数和旧式组合构造的完整形式化成本较高。

### 需要的验证

- 检索并核对 Erdős-Hajnal-Szemerédi 1982 结果和 Erdős 1981 猜想的原始表述，确认 h_G(n) 的精确定义是任意子图还是诱导子图，以及隐含常数和量词。
- 验证线性下界 h_G(n) 远大于 n 的推导细节，尤其是从 aleph_1 多个顶点不交同长奇环到有限 n 点子图删除边数下界的精确渐近含义。
- 对已知 h_G(n) 远小于 n^{3/2} 的构造进行重建，检查它是否可能通过参数调整达到 O(n) 或 n^{1+epsilon}。
- 用 SAT/ILP 或极值图搜索验证相关有限猜想，例如给定奇环打击数、最大二分子图缺口、稀疏高 girth 子结构之间的关系。
- 若提出完整证明或反例，需要由人类专家审查集合论量词、不可数构造、极限过程和所有 n 的一致性。

### 公开版思考摘要

这个问题对 AI 来说有一个有利面和一个硬障碍。有利面是 h_G(n) 本身是有限图参数，可计算、可形式化、可通过小规模搜索产生猜想；备注也给出了已知上下界和自然攻击点。硬障碍是最终命题要求所有染色数为 aleph_1 的无限图满足超线性有限子图非二分性，这需要新的不可数图组合结构定理或精细反例构造。因而我判断 GPT-5.5 更可能在重构文献、验证局部引理、发现条件性版本或缩小构造空间上有实质贡献，而不是高概率独立完成最终开放问题。

### 免责声明

以上不是该 Erdős 问题的解答，也不声称证明或否定原命题；它只是基于给定 problem JSON 对 GPT-5.5 级别模型可推进性的审查判断。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `likely_open`
- 状态信心: `medium`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_111.md](../../prompts/problem_111.md)

### 状态结论

截至 2026-07-27，题目页仍标为 OPEN，配套论坛线程没有任何解答或部分解答声明。已核查原始 EHS82 论文：其确实定义了同一类“删边后可二分”的极值函数，并证明了上界 O(n^{3/2}) 及每个不可数色数图的线性下界。定向检索到的 2020 年 Lambie-Hanson 结果解决的是有限子图色数增长问题，不控制删边二分距离，不能视为本题的解答。未找到可核查的解决或反例文献；这只支持“很可能仍开放”，不是不存在未检索到文献的逻辑证明。

### 当前规范陈述

取简单无向图。对有限图 F，令 β(F)=min{|D|:D⊆E(F) 且 F−D 为二分图}。对无限图 G 及 n∈N，定义 h_G(n)=max{β(G[A]):A⊆V(G), |A|=n}。这等价于：使 G 的每个 n 顶点子图变为二分图所需删除边数的最小统一上界；因为在固定顶点集 A 上，诱导子图 G[A] 是最坏情形。精确的是非问题为：对每个 χ(G)=aleph_1 的图 G，是否有 h_G(n)/n→+∞？原文“h_G 的行为如何”本身不是单一可判定命题。另一个历史性构造猜想是：对每个 ε>0，是否存在 χ(G)=aleph_1 的图 G，使 h_G(n)=O_{G,ε}(n^{1+ε})？

```text
Work with simple undirected graphs. For a finite graph F, let β(F)=min{|D|:D⊆E(F) and F−D is bipartite}. For an infinite graph G and n∈N, define h_G(n)=max{β(G[A]):A⊆V(G), |A|=n}. Equivalently, this is the least t such that every n-vertex subgraph of G can be made bipartite after deletion of at most t edges, since the induced subgraph G[A] is the worst choice on A. The precise yes/no target is: for every graph G with χ(G)=aleph_1, is lim_{n→∞} h_G(n)/n=+∞? The accompanying broad request to determine the full behaviour of h_G is not a single proposition. A distinct historical construction conjecture is: for every ε>0, does there exist a graph G with χ(G)=aleph_1 for which h_G(n)=O_{G,ε}(n^{1+ε}) as n→∞?
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 未找到能使字面极限命题立刻失败的简单构造。EHS82 的不可数多个同长度、顶点不交奇圈只给出 h_G(n)≥c_G n（某个依赖 G 的正 c_G），并不推出 h_G(n)/n→∞；而 EHS82 的 O(n^{3/2}) 构造也不反驳该极限。
- 版本变化: EHS82 第 3 节定义 f_W^3(n) 为 n 顶点诱导子图到二分图的最大最小删边数；这与规范化后的 h_G 相同。EHS82 证明了 f_W^3(n)<2n^{3/2} 的构造性上界，并指出任何不可数色数图都有 ε_G n 的线性下界。1981 年 Erdős 将 n^{3/2} 改进至任意 n^{1+ε} 提为猜想。题目页的可见修订记录仅显示 2025-10-20 的排版性改动，未显示数学性改写。

陈述问题：

- 输入中的“let h_G(n) be defined such that”没有给出唯一的极值定义；应明确为所有 n 元顶点集上最小删边数的最大值。
- “any subgraph”可能指诱导或非诱导子图；在上述最大化定义下两种读法等价，但必须说明这一点。
- “What is the behaviour”是开放式请求，不能独立给出唯一完成标准；后面的极限问题才是明确的核心命题。
- EHS82 的原始记号为 f_W^3(n)，并以诱导在 A 上的子图定义；数据库将其记为 h_G(n)。
- Erdős 的“可改进为 n^{1+ε}”表述须将量词写成“对每个 ε 存在一个 G”，除非原始文本另行证明同一个 G 同时适用于所有 ε。

需要固定的量词/约定：

- The universal question is ∀G [χ(G)=aleph_1 ⇒ ∀M>0 ∃N ∀n≥N, h_G(n)>Mn].
- Its negation is the existence of G with χ(G)=aleph_1, a constant C, and arbitrarily large n for which h_G(n)≤Cn.
- In h_G(n), the maximum ranges over all n-element subsets of V(G); the definition is meaningful for every n because χ(G)=aleph_1 implies |V(G)|≥aleph_1.
- The asymptotic notation h_G(n)=O(n^{1+ε}) permits a constant depending on G and ε but not on n.
- The historical upper-bound conjecture should be treated separately from the universal lower-growth question.

### 文献与当前边界

已核验的主要结果：

- Erdős、Hajnal、Szemerédi（1982，同行评议会议论文）定义了与 h_G 相同的 f_W^3(n)。他们证明：对每个无限基数 κ>aleph_0，存在色数大于 κ 的图 W，使 f_W^3(n)<2n^{3/2}；论文用有序边图/移位图构造给出此界。
- 同一论文证明：任一不可数色数图含有不可数多个某一固定奇长度的顶点不交奇圈。取这些奇圈的有限并可得 h_G(n)≥c_G n（足够大的相应 n，及按常数调整的线性下界）；这不足以推出比线性更大的增长。
- Erdős（1981，Combinatorica）提出把 n^{3/2} 上界改进为任意 n^{1+ε} 的构造性猜想。该猜想与“每个 G 都有 h_G(n)/n→∞”并不逻辑等价，二者均应分别处理。
- Lambie-Hanson（2020，Advances in Mathematics）在 ZFC 中解决了 EHS 的另一问题：可以令有限子图色数随顶点数增长任意慢。该性质不控制奇圈打包或最小删边二分数，故不解决本题。

最近相关工作：检索到的最新近邻工作是 Lambie-Hanson 与 Uhrik（2024，Mathematika）：它延伸了 Hajnal–Máté 图及有限子图色数增长的构造。其讨论并未给出 h_G(n) 的有界线性子序列、超线性普遍下界或 n^{1+ε} 删边上界。针对 2023–2026 年 arXiv、作者页和精确短语检索，未发现直接解决 #111 的可核查论文。

剩余核心：明确核心是证明或反驳：每个 χ(G)=aleph_1 的图都满足 h_G(n)/n→∞。独立但高度相关的构造核心是：对每个 ε>0 构造一个 χ(G)=aleph_1 的图，使 h_G(n)=O(n^{1+ε})。目前已验证的界仍在“某个正线性下界”与“某个 n^{3/2} 上界构造”之间。

已使用方法：

- EHS82 的有序边图、移位图及递归的低色数删边分解。
- 由不可数多个同长度、顶点不交奇圈导出的线性下界。
- 集合论组合方法：club guessing、Hajnal–Máté 图，以及控制有限子图色数增长的 forcing/构造方法；现有文献未将这些方法转化为 h_G 控制。
- 有限图的 edge-bipartization、最大割与奇圈横截理论可为局部引理提供语言，但有限计算本身无法决定无限色数结论。

争议或不确定性：

- 题目页自身说明 OPEN 只是维护者信念；论坛无解答声明是弱的负面证据，不能取代文献穷尽性证明。
- EHS82 表述其构造为对任意 κ>aleph_0 有 χ(W)>κ 的图，而题目页称存在 χ(G)=aleph_1 的图具有相应上界。应在开始研究前核验从原构造到“恰为 aleph_1”的限制/子图化步骤，或直接使用文献中的精确构造。
- Lambie-Hanson 2020 的 f_G（有限子图色数阈值）与本题 h_G（edge-bipartization）容易混淆；低色数不意味着低删边二分距离，例如大量不交三角形仍可有线性删边距离。

### 证据来源

- [Erdős Problems — Problem 111](https://www.erdosproblems.com/111) — Thomas F. Bloom / Erdős Problems database, 2026; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 当前数据库将该题标为 OPEN；列出线性下界、EHS82 的 O(n^{3/2}) 存在性上界及 Erdős 的 n^{1+ε} 猜想，并明确提醒状态只是站点维护者的判断。
- [Erdős Problems — Problem 111 LaTeX source](https://www.erdosproblems.com/latex/111) — Thomas F. Bloom / Erdős Problems database, 2026; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 核对题目文本、备注和参考文献与网页显示一致；LaTeX 源没有补足 h_G(n) 的极值量词。
- [111 Discussion Thread | Erdős Problems](https://www.erdosproblems.com/forum/thread/111) — Erdős Problems forum, 2026; `forum`, `informal_claim`, directness=`direct`, reliability=`medium`. 该线程显示没有评论、完整解答或部分解答声明；它不能单独确证开放性。
- [On Almost Bipartite Large Chromatic Graphs](https://www.renyi.hu/~p_erdos/1982-11.pdf) — Paul Erdős, András Hajnal, Endre Szemerédi, 1982; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 原文 Definition 3.1 定义删边到二分图的函数 f_W^3(n)；其 Theorem 3(a) 给出 f_W^3(n)<2n^{3/2} 的构造，且此前由奇圈论证得到对每个不可数色数图的线性下界。
- [Combinatorica Volume 1, Issue 1 (1981) contents](https://combinatorica.hu/issues.htm) — Combinatorica, 1981; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 核实 Erdős 1981 年文章《On the combinatorial problems which I would most like to see solved》的书目信息：Combinatorica 1(1), 25–42，DOI 10.1007/BF02579174。
- [On the growth rate of chromatic numbers of finite subgraphs](https://arxiv.org/abs/1902.08177) — Chris Lambie-Hanson, 2020-08-05; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 证明任意给定函数 f 都存在 χ(G)=aleph_1 的图，其有限子图达到色数 k 所需顶点数可至少为 f(k)；论文明确将所解问题定义为有限子图色数增长。该结论不提供 h_G 的删边二分距离界。
- [Hajnal–Máté graphs, Cohen reals, and disjoint-type guessing](https://doi.org/10.1112/mtk.12261) — Chris Lambie-Hanson, Dávid Uhrik, 2024-05-28; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 后续工作进一步讨论有限子图色数增长及 Hajnal–Máté 图，但所呈现的增长率结果仍是色数函数而非 h_G 的删边二分函数；未构成 #111 的解决。

### 完成标准

- 肯定出口: A complete affirmative resolution proves in ZFC that for every simple graph G with χ(G)=aleph_1 and every real M>0, there is N=N(G,M) such that h_G(n)>Mn for all n≥N.
- 否定出口: A complete negative resolution gives, in a stated foundational setting, a specific graph G with χ(G)=aleph_1, a constant C<∞, and arbitrarily large integers n such that h_G(n)≤Cn. This is exactly the negation of h_G(n)/n→∞.

不构成完成：

- Proving only h_G(n)≥c_G n for a positive constant c_G; this is already known and does not imply divergence of h_G(n)/n.
- Giving an O(n^{3/2}) bound, or an O(n^{1+ε}) bound, for a single construction without proving the claimed quantifiers.
- Controlling the chromatic number of finite subgraphs without an explicit implication for edge-bipartization number.
- A result for finite graphs of arbitrarily large chromatic number, or for a graph of countable chromatic number, without the required χ(G)=aleph_1 conclusion.
- Checking finitely many n or finite induced subgraphs without a uniform theorem covering all sufficiently large n.

正确性陷阱：

- Use edge deletion, not vertex deletion; the EHS paper studies both and they have different functions.
- Take a maximum over n-vertex induced subgraphs. Do not replace it with an average, an existential subgraph, or the edge count of G[A].
- For a negative answer, a bounded ratio along an unbounded subsequence suffices; a bound only for one n does not.
- For a positive answer, the threshold N may depend on G and M, but the assertion must cover every sufficiently large n.
- Do not infer a bound on β(F) merely from a bound on χ(F): graphs of chromatic number three can have arbitrarily large edge-bipartization number.
- State whether any extra principle such as diamond, CH, or forcing is used. A conditional result is not an unconditional ZFC resolution.
- Audit the exact-cardinality claim χ(G)=aleph_1 rather than merely χ(G)>aleph_0 or χ(G)≥aleph_1.

### 更新后的 AI 可解答性

- 等级: `low_candidate`
- 分数: `16/100`
- 信心: `medium`
- 结论: 这是定义清楚、可独立验算但难度很高的开放问题；适合以证明优先的长期研究而非以搜索或有限计算为主的尝试。16 分仅衡量解决当前明确核心的机会，不代表验证既有结果的难易。

支持理由：

- 核心极限命题有精确的正反完成条件，且已有明确的线性下界和 n^{3/2} 构造上界。
- 原始论文公开可读，并给出可复用的移位图/有序边图技术和关键障碍。
- 近年的不可数图构造文献提供了另一套潜在工具，但尚未与 edge-bipartization 连接。

主要障碍：

- 问题横跨无限图色数、集合论组合和有限极值图论；44 年以上没有填补线性与超线性之间的缺口。
- 需要对所有有限顶点集作最坏情形控制；有限实验不能证明 χ(G)=aleph_1 或极限量词。
- 有限子图色数增长与删边二分距离之间没有可直接使用的逆向蕴涵。
- 可能依赖 ZFC 与额外集合论公理之间的区分，且原始构造的精确色数需要谨慎核验。

Proof-first 路线：

- 尝试证明一个结构性紧致性命题：若某个 χ=aleph_1 图在任意大规模上有 h_G(n)=O(n)，是否能推出可数染色或其他矛盾。
- 反向尝试改造 EHS 的有序边/移位构造，寻找统一线性删边二分界或至少有界比率子序列，同时保持 χ=aleph_1。
- 研究奇圈横截、最大割和不可数不交奇圈定理之间能否升级为随比例增长的打包/横截下界。
- 只有在先给出明确有限引理、假设和停止条件时，才使用一次有限模型搜索来证伪候选引理或产生精确证书。

需要验证：

- 由领域专家或 MathSciNet/zbMATH 核验 2024–2026 年文献与引文网络，特别是难以被关键词索引的集合论图论文章。
- 从 EHS82 原构造核验题目页所称 χ(G)=aleph_1 的精确版本，或给出可靠的子图化论证。
- 若出现声称解决的预印本，逐项核验其对 h_G 的最坏情形量词、edge deletion、ZFC 假设和 χ=aleph_1 结论。

### 审计限制与人工复核理由

- 本审计按要求使用公开网页、原始论文 PDF、期刊/预印本记录和论坛；没有访问 MathSciNet、zbMATH 或付费全文数据库，因而不能排除索引不充分的最新文献。
- EHS82 的可访问 PDF 足以核对函数定义和主要定理，但题目页从“不可数色数/色数大于 κ”的构造表述到“恰有 aleph_1 色数”的具体说法，应由专家进一步核验。
- “未发现解决”来自精确短语、作者、引文及近三年检索，不是文献不存在的证明。
- 论坛无评论只说明没有可见的论坛主张；它不能为开放状态提供独立数学证明。

- 应由无限图论/集合论专家核对 EHS82 构造是否直接给出或可无损限制到 χ=aleph_1。
- 建议用专业书目库复核 2024-07 至 2026-07 的引文网络，以降低未被通用网页检索收录的解决文献风险。
- 历史性 n^{1+ε} 猜想的“同一个 G”还是“每个 ε 可取不同 G”的量词，应在可访问的 Erdős 原文页码处再作核对。

<!-- DEEP_REVIEW:END -->
