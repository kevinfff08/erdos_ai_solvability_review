# Problem 74

## 基本信息

- 原始链接: https://www.erdosproblems.com/74
- LaTeX 页面: https://www.erdosproblems.com/latex/74
- 原始状态: `open`
- 奖金: `$500`
- 主类别: `graph theory`
- 原始标签: `graph theory`, `chromatic number`, `cycles`
- 形式化状态: `yes`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

Let $f(n)\to \infty$ (possibly very slowly). Is there a graph of infinite chromatic number such that every finite subgraph on $n$ vertices can be made bipartite by deleting at most $f(n)$ edges?

## AI 完成可能性判断

- 结论: **AI 辅助完成有现实候选路线，但需要外部计算或严格验证**
- 等级: `medium_candidate`
- 分数: `56/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 题面或备注出现有限对象/计算线索
- 已有形式化陈述，可降低语义误读风险

### 主要障碍

- 题面含渐近/无限对象线索：\gg
- 原记录含奖金 $500，说明该题被长期视为高价值难题；这不是否定依据，但提高验证门槛。

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: chromatic number, cycles, graph theory
- 证明密集标签命中: 无
- 有限/计算线索: chromatic, counterexample, finite, graph, hypergraph
- 渐近/无限线索: \gg
- 构造/存在性线索: counterexample, is there

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5 + computation/formalization/literature tools`
- 结论: **低到中等候选。该问题已有形式化版本，且已知在线性误差 f(n)=εn 情况有正例，因此 GPT-5.5 级别模型可能在整理等价表述、检验候选构造、形式化局部引理、搜索有限反例或改进常数/子线性边界方面产生有用推进；但要解决任意趋于无穷的 f(n)，尤其覆盖已注明仍开放的 f(n)=sqrt(n)，很可能需要新的极值图论或无限图构造思想，完整解决概率偏低。**
- 等级: `low_to_medium_candidate`
- 分数: `42/100`
- 信心: `medium`
- 可能路线: 最可行路线不是直接蛮力求解，而是把条件转化为有限图族的“所有 n 点子图的 odd-cycle edge transversal 至多 f(n)”约束，结合已形式化陈述建立可机检的引理库；随后尝试改造已知 f(n)=εn 的构造，寻找可迭代稀疏化、分层随机图或紧致性/模型论构造，使局部非二分性预算降到 o(n)。计算工具可用于小规模 extremal 搜索，寻找障碍结构；证明助手可验证候选递推构造是否真的保持无限色数和局部可二分化预算。

### 支持理由

- 问题陈述短且结构清晰，核心性质可形式化为有限子图上的删边二分化预算，适合 proof assistant 和有限模型搜索辅助。
- 已有正向结果覆盖 f(n)=εn，说明目标并非完全脱离现有构造；AI 可尝试分析该构造中导致线性误差的瓶颈。
- 形式化状态为 yes，降低了验证候选证明、抽取精确定义、检查边界条件的成本。
- 计算搜索可以枚举小图的最小二分化删边数、色数和局部子图约束，帮助发现潜在有限障碍或反例模式。

### 主要障碍

- 问题已注明即使 f(n)=sqrt(n) 仍开放；任意慢增长 f(n) 比已知线性结果强很多。
- 无限色数与所有有限子图近似二分之间存在张力，常规高围长高色数随机构造不自动给出足够小的删边预算。
- 若想证明存在性，需要同时控制全局色数和每个 n 点有限子图的 odd-cycle 破坏边数，这通常涉及很强的多尺度一致性。
- 计算只能覆盖有限规模，难以直接证明无限图存在；有限模式也可能无法代表极限构造。
- 反例方向同样困难，需要排除所有无限色数图满足任意慢增长预算的可能性，可能要求新的结构定理。

### 需要的验证

- 核对形式化版本中的“finite subgraph on n vertices”是否指任意有限子图而非诱导子图，并固定删边预算的精确定义。
- 复现并形式化已知 f(n)=εn 构造的关键引理，定位线性项来源。
- 对候选构造证明三件事：图无限色数；每个 n 点有限子图可删至二分图；删边数确实为给定 f(n) 或渐近受控。
- 用有限图搜索验证小 n 下的障碍结构，并检查候选递推/随机参数是否被小规模反例击穿。
- 若给出证明草案，需要 proof assistant 或独立形式化检查处理所有量词顺序，尤其是任意慢增长 f(n) 与无限图构造的依赖关系。

### 公开版思考摘要

该题适合 AI 工具链做严谨辅助研究：定义可形式化、已有线性正例可作为起点、有限搜索能提供反馈。但它的核心难点正落在从线性局部误差降到任意趋于无穷的误差，而题面明确指出 sqrt(n) 情形仍开放。综合判断，GPT-5.5 更可能产出可验证的局部推进、等价重述或候选构造排错，而不是高概率独立完成完整证明。

### 免责声明

以上是对 GPT-5.5 级别模型辅助攻关可行性的审查，不是该 Erdős 问题的证明、反例或解答。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `likely_open`
- 状态信心: `medium`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_74.md](../../prompts/problem_74.md)

### 状态结论

截至 2026-07-27，直接的当前数据库记录仍将本题列为 open（2026-01-25 编辑、无评论中的解答声称），其正式化文件也把同一全称量词版本标为 research open。检索到的 Lambie-Hanson 2020 年定理解决的是“有限子图色数增长”这一不同的 EHS 问题，并不控制删边至二分图所需的边数；未发现可核验的论文或形式化工件解决本题。因此最合适的结论是 likely_open，而非把数据库标签视为决定性证明。

### 当前规范陈述

对每个满足 f:N→N 且 lim_{n→∞}f(n)=∞ 的函数 f，是否存在一个简单无向图 G，使 χ(G) 为无限（即不存在有限的正常顶点着色），并且对每个 n∈N 及每个满足 |V(H)|=n 的有限子图 H⊆G，都存在 D⊆E(H)，|D|≤f(n)，使 H−D 为二分图？等价地，令 b(H) 为将 H 删边化为二分图所需的最少边数，则每个 n 点子图的 b(H) 均不超过 f(n)。见证图 G 可以依赖于 f。

```text
For every function f: N → N with lim_{n→∞} f(n)=∞, there exists a (simple undirected) graph G with infinite chromatic number such that, for every n∈N and every finite subgraph H⊆G with |V(H)|=n, there is a set D⊆E(H) with |D|≤f(n) for which H−D is bipartite. Equivalently, if b(H):=min{|D|:D⊆E(H), H−D is bipartite}, then sup{b(H):H⊆G, |V(H)|=n}≤f(n) for every n. The witnessing graph G may depend on f.
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 未发现能否定上述精确全称命题的初等构造。已知“若强制 χ(G)=aleph_1 则失败”的事实不能反驳本题，因为本题只要求无限色数，允许 χ(G)=aleph_0。对某个固定 f 的反例也不足以否定原命题，除非该 f 趋于无穷。此结论是定向核查结果，并非穷尽性证明。
- 版本变化: 1982 年 Erdős、Hajnal、Szemerédi提出该问题；Rödl 同年给出 3-一致超图版本及图的线性容差版本。至少到 2008 年的 Erdős 问题汇编，仍特别要求处理 f=o(n^ε) 或 f=o((log n)^c) 的情形。2020 年 Lambie-Hanson 解决了另一项关于有限子图色数增长的 EHS 问题，不能作为本题的修订或解答。2025 年的 Lean 文件将本题明确编码为 ∀f∃G 的原命题，并额外列出 sqrt(n) 变体；该文件含 sorry，因而只是陈述正式化，不是证明。

陈述问题：

- 原句“Let f(n)→∞ (possibly very slowly)”未把全称量词写明；历史表述的“arbitrarily slowly”以及现有 Lean 工件均支持“对每个趋于无穷的 f，存在可依赖于 f 的 G”，而非要求同一张 G 同时适用于所有 f。
- 原句未说明 f 的值域。由于删边数为整数，规范版本取 f:N→N；若允许实值 f，应将上界解释为 ⌊f(n)⌋。
- “finite subgraph”应理解为任意有限（不必诱导）子图。只量化诱导子图是等价的：对诱导子图的一个二分化删边集与任意边子图相交即可二分化该边子图，且不增加删边数。
- “infinite chromatic number”是色数不是顶点数：它指没有有限着色。题目并不要求 χ(G)=aleph_1；数据库明确警告把色数加强到 aleph_1 的版本失败。
- n=0、1、2 的边界条件自动成立；不应把它们误作额外限制。

需要固定的量词/约定：

- The intended/formalized order is ∀f with f(n)→∞, ∃G=G_f, ∀n, ∀ finite H⊆G with |V(H)|=n, ∃D⊆E(H.
- No monotonicity of f is assumed; only eventual divergence is required.
- The deletion set D may depend on H. A single deletion set for all n-vertex subgraphs is not required.
- The term “subgraph” is edge-subgraph inclusive; induced-subgraph wording yields an equivalent condition here.

### 文献与当前边界

已核验的主要结果：

- Erdős、Hajnal、Szemerédi（1982，同行评议）提出关于大色数图有限子图“近二分”的问题族；本题是其无限色数、任意慢发散删边预算版本。
- Rödl（1982，同行评议）证明了相应的 3-一致超图结论。Erdős Problems 当前记录进一步归纳：对任意固定 ε>0，存在色数 aleph_0 的图使每个 n 点有限子图可在至多 εn 次删边后变为二分图。该线性预算结果不能推出 f(n)=o(n) 的任何情形。
- 历史问题页和 2008 年汇编均将 f=o(n^ε) 或 f=o((log n)^c) 明列为仍有意义的更强残余方向；当前页面特别称 f(n)=sqrt(n) 未解。
- Lambie-Hanson（2020，同行评议）对每个函数构造不可数色数图，并限制不同色数级别的有限子图最小规模。这是有限子图色数增长问题，不给出 b(H) 的上界；例如“低色数”不等于“只需少量删边即可二分”。

最近相关工作：检索到的最近相邻方向是 Lambie-Hanson 与 Uhrik 的 2023 预印本（后续研究 Hajnal–Máté 图和有限子图色数增长）。截至审计日，未发现 2023–2026 年直接声称证明或反驳 Problem 74 的论文、预印本、作者网页或正式化证明。

剩余核心：在 ZFC 中证明或反驳：对每个整数值且趋于无穷的预算 f，能否构造某个无限色数图，其每个 n 点有限子图的最小二分删边数至多 f(n)。最具体的公开瓶颈是 f(n)=sqrt(n)，更强的是任意次线性、任意慢发散预算。

已使用方法：

- Rödl 的有限/无限组合构造，已达到固定线性删边预算。
- 超图版本的构造方法。
- 无限图与集合论的色数构造；Lambie-Hanson 的工作展示了可把有限子图的色数增长推得任意慢，但该不变量不同。
- 对每个有限子图的 odd-cycle edge transversal（删边至二分距离）进行统一控制，而非仅控制 girth、局部色数或有限子图色数。

争议或不确定性：

- 当前状态主要由 2026-01 的问题页面及无解答评论支持；未取得一份 2026 年专家综述或所有引文的全文，因此不能给出“confirmed_open”。
- Rödl 论文的正式书目和当前数据库摘要均已核验，但本审计未能逐页检查其全文定理的量词；在后续研究启动前应核对该论文的精确定理陈述。
- Lambie-Hanson 2020 摘要称解决 EHS 的一个问题，容易造成同名问题族的误归属；经不变量比较，它不解决本题。

### 证据来源

- [Erdős Problems — Problem 74](https://www.erdosproblems.com/74) — Thomas F. Bloom / Erdős Problems, 2026-01-25; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 当前页面将本题列为 OPEN，称对 f(n)=sqrt(n) 仍开放，记录 Rödl 的线性容差图结果及超图结果，并显示无评论中的完整或部分解答声称。页面本身也明确提示状态不是穷尽性文献审查。
- [On Almost Bipartite Large Chromatic Graphs](https://users.renyi.hu/~p_erdos/1982-11.pdf) — P. Erdős, A. Hajnal, E. Szemerédi, 1982; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 原始论文及题目来源；其引言说明研究大色数图的有限子图如何接近二分图。
- [Nearly bipartite graphs with large chromatic number](https://doi.org/10.1007/BF02579434) — Vojtěch Rödl, 1982; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. Rödl 的 Combinatorica 论文（2(4), 377–383）的正式书目信息；当前问题页将其列为固定 εn 图版本和超图版本的来源。
- [Almost-bipartite graphs with infinite chromatic number](https://mathweb.ucsd.edu/~erdosproblems/erdos/newproblems/AlmostBipartiteInfiniteGraphs1.html) — Erdős problem collection (UCSD mirror), date unknown; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 保留了“f(n) arbitrarily slowly”的历史措辞，并明确列出 f=o(n^ε) 和 f=o((log n)^c) 的残余目标及 3-一致超图正解。
- [On the growth rate of chromatic numbers of finite subgraphs](https://arxiv.org/abs/1902.08177) — Chris Lambie-Hanson, 2019-02-25; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 证明对任意函数可构造不可数色数图，使高色数有限子图足够大；摘要称其回答 EHS 的一个问题。该结论控制有限子图的色数而非删边二分距离，故不是本题的解答。
- [On the growth rate of chromatic numbers of finite subgraphs](https://doi.org/10.1016/j.aim.2020.107176) — Chris Lambie-Hanson, 2020-08-01; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 上述不同问题的同行评议版本，发表在 Advances in Mathematics 369, Article 107176；用于排除把该 2020 结果误报为本题解答的风险。
- [Hajnal–Máté graphs, Cohen reals, and disjoint-type guessing](https://arxiv.org/abs/2312.01828) — Chris Lambie-Hanson, Dávid Uhrik, 2023-12-04; `preprint`, `preprint`, directness=`indirect`, reliability=`high`. 近三年相关工作继续研究有限子图色数增长及 Hajnal–Máté 图；摘要没有声称控制本题的删边二分距离。
- [Formal Conjectures — Erdős Problem 74](https://raw.githubusercontent.com/google-deepmind/formal-conjectures/main/FormalConjectures/ErdosProblems/74.lean) — Formal Conjectures Authors, 2025; `formalization`, `formalized_artifact`, directness=`direct`, reliability=`high`. 将本题编码为 ∀f, Tendsto f atTop atTop → ∃G，并定义每个 n 点有限子图的最大删边二分距离；定理以 sorry 结束且标注 research open，故证实当前形式化目标但不提供证明。

### 完成标准

- 肯定出口: Provide a ZFC proof that for every f:N→N with f(n)→∞ there exists a simple graph G of infinite chromatic number such that b(H)≤f(|V(H)|) for every finite subgraph H⊆G, where b(H) is the minimum number of edges whose deletion makes H bipartite.
- 否定出口: Provide a ZFC proof of the logical negation: exhibit one f:N→N with f(n)→∞ and prove that every graph G of infinite chromatic number has a finite subgraph H with b(H)>f(|V(H)|).

不构成完成：

- Constructing a graph only for f(n)=εn, or for any other one fixed non-sublinear budget, does not settle the universal statement.
- Solving the analogous 3-uniform-hypergraph problem does not settle the graph problem.
- Showing that finite subgraphs have slowly growing chromatic number, high odd girth, or few short odd cycles does not suffice without a quantitative bound on b(H).
- Showing the claim fails after strengthening χ(G) to aleph_1 does not refute the stated infinite-chromatic-number target.
- A construction for f(n)=sqrt(n) would be major partial progress but would not prove the full ∀f claim.

正确性陷阱：

- Verify the quantifier order ∀f∃G, not ∃G∀f, and allow G to depend on f.
- Use chromatic number, not cardinality of the vertex set; “infinite chromatic” permits χ(G)=aleph_0.
- Quantify over every finite edge-subgraph. If working only with induced subgraphs, explicitly prove the monotonicity reduction.
- For every finite H, certify an actual edge set D with H−D bipartite; bounding odd-cycle counts, girth, or χ(H) is not an equivalent certificate.
- Handle nonmonotone diverging f and all small n; do not silently replace f by a larger convenient function unless the reduction is proved.
- Do not import assumptions such as CH, diamond, forcing axioms, or a special model of set theory into a claimed ZFC resolution.

### 更新后的 AI 可解答性

- 等级: `low_candidate`
- 分数: `15/100`
- 信心: `medium`
- 结论: 这是定义清楚、可审计但很难的开放构造/反构造问题。AI 可在精确化、有限引理、文献辨析和反例审计上有帮助；仅凭枚举或常规局部图构造，完整解决的机会低。

支持理由：

- 目标具有清晰的量词、可验证的有限局部证书和明确的正反完成条件。
- 存在非平凡的线性预算先例以及已隔离的 sqrt(n) 次线性门槛。
- 问题长期开放，且相邻的色数增长理论并未自动转化为 odd-cycle edge transversal 控制，显示存在实质性结构鸿沟。

主要障碍：

- 必须同时维持无限色数并对所有有限子图施加任意慢发散的删边预算。
- 有限计算只能检验候选有限图，不能认证无限色数或全体有限子图条件。
- 无限图/集合论方法易将色数增长结论误当作二分删边距离结论；模型依赖构造也不等于 ZFC 证明。

Proof-first 路线：

- 先证明或否定一个精确的桥接引理：何种局部稀疏/分解条件足以统一控制 b(H)，并明确其常数与量词。
- 将任意 f 归约为一族阶梯状预算时，必须严格证明该归约而不是假定 f 单调。
- 分别探索“从 Rödl 型分层构造压低局部 odd-cycle transversal”与“从无限色数强迫某一有限子图具有超过给定预算的二分删边距离”的互不依赖路线。

需要验证：

- 逐页核验 Rödl 1982 定理的图与超图版本、色数和预算量词。
- 对 2020–2026 引用网络做人工数据库检索（MathSciNet/zbMATH/Google Scholar）以补强未发现最新解答的结论。
- 若得到候选证明，逐项审计其 ZFC 依赖、全称 f、全体有限子图及 χ(G)=∞ 的证明。

### 审计限制与人工复核理由

- 已尝试打开当前 Erdős Problems 的普通页与 LaTeX 页；普通页内容可由检索结果核验，但该会话中 LaTeX 页的直接打开返回内部错误。
- Rödl 1982 论文的 DOI、卷页和作者书目已核验，但没有取得其全文逐页审读；线性版本和超图版本的精确定理量词目前依赖当前问题页及历史汇编的摘要。
- 近年检索覆盖精确短语、题号、原论文、arXiv、形式化仓库与相邻有限色数增长文献，但不能替代 MathSciNet/zbMATH 的完整人工引文审查。
- 未发现论坛中的证明主张；因此没有可供逐步验证的非正式解答。

- 在投入长期研究前，应由图论专家核对 Rödl 1982 的精确定理和后续引用链，以确认线性预算先例没有被误述。
- 建议使用专业文献数据库完成 2020–2026 的引文追踪；当前“likely_open”基于直接页面、定向搜索和未发现解答，而不是开放性的逻辑证明。
- 任何未来声称的解答均应优先接受独立证明审计，并在可行时与现有 Lean 陈述逐项比对。

<!-- DEEP_REVIEW:END -->
