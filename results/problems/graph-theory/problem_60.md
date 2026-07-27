# Problem 60

## 基本信息

- 原始链接: https://www.erdosproblems.com/60
- LaTeX 页面: https://www.erdosproblems.com/latex/60
- 原始状态: `open`
- 奖金: `no`
- 主类别: `graph theory`
- 原始标签: `graph theory`, `cycles`
- 形式化状态: `no`
- OEIS: `A006855`
- 原站备注字段: 无

## 原问题

Does every graph on $n$ vertices with $>\mathrm{ex}(n;C_4)$ edges contain $\gg n^{1/2}$ many copies of $C_4$?

## AI 完成可能性判断

- 结论: **AI 可能做出局部推进或搜索反例，但完整解决把握不足**
- 等级: `low_to_medium_candidate`
- 分数: `42/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 题面或备注出现有限对象/计算线索
- 存在 OEIS 数据入口，利于实验与反例搜索

### 主要障碍

- 题面含渐近/无限对象线索：\gg

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: cycles, graph theory
- 证明密集标签命中: 无
- 有限/计算线索: graph
- 渐近/无限线索: \gg
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **不太可能由 GPT-5.5 级别模型在一次研究流程中完整解决，但有现实机会显著推进局部情形、整理可验证的证明路线，或对有限范围与特殊构造做高质量验证。**
- 等级: `low_to_medium_candidate`
- 分数: `42/100`
- 信心: `medium`
- 可能路线: 较可行的路线是把问题转化为 C4 超饱和与 extremal C4-free 图结构的稳定性问题：先形式化“刚超过 ex(n;C4)”时新增边如何强迫多个 4-环；结合已知特殊情形 n=q^2+q+1 且 q 为偶数的证明思路，尝试推广到接近投影平面阶数的 n，或证明弱版本如至少 2 个、n^alpha 个、或在额外稳定性假设下的 Ω(n^{1/2}) 个。计算上可用 SAT/ILP/flag algebra/枚举检查小 n 和候选极值图，帮助发现反例模式或验证局部引理。

### 支持理由

- 问题陈述短、目标明确，适合被拆成超饱和下界、极值图稳定性、有限阶数构造和计算验证几个子任务。
- 已有备注显示存在重要特殊情形证明，这给模型提供了可复用的证明模板，而不是完全无结构的开放问题。
- C4 计数可由度序列、共同邻居数、谱方法和凸性不等式表达，适合模型配合计算机代数、SAT/ILP 与形式化证明工具探索。
- 即使无法解决一般情形，GPT-5.5 级别模型也可能产出有价值的弱化命题、边界案例验证、证明草图审计和文献路线图。

### 主要障碍

- 这是开放的 Erdős-Simonovits 猜想，核心困难不是计算规模，而是需要新的 extremal graph theory 结构性洞察。
- ex(n;C4) 本身行为复杂；当 n 不等于投影平面相关阶数时，极值图结构和精确边数可能不够稳定。
- “只多一条边”属于非常稀薄的超饱和区间，常规 supersaturation 定理通常给不出 Ω(n^{1/2}) 级别的强结论。
- 可能存在大量近极值 C4-free 图，新增边产生的 C4 数量高度依赖具体结构，反例搜索也难以穷尽。
- 形式化证明会受限于缺少已形式化的深层有限几何和极值图论库。

### 需要的验证

- 检索并复核 He-Ma-Yang 2021 特殊情形证明，确认其关键引理是否可迁移到一般 n 或近似阶数。
- 对已知 ex(n;C4) 精确值或最佳界的范围做文献核查，避免把未知极值结构误当作已知。
- 用独立计算程序枚举小 n 的 extremal 或 near-extremal 图，检查“超过 ex 后的最少 C4 数”是否符合 n^{1/2} 趋势。
- 对任何模型提出的新引理进行人工专家审查，并尽量用 Lean/Isabelle 或可复现实验验证局部计数不等式。
- 特别验证渐近符号中的常数依赖和 n 的充分大条件，防止只证明了较弱的 n^{o(1)} 或条件化版本。

### 公开版思考摘要

这个问题具有清楚的计数目标和可计算的有限版本，因此适合 AI 工具链做系统探索；但一般情形要求理解 C4-free 极值图在最稀薄超饱和区间的精细结构，目前备注中也显示即使证明至少两个 C4 都曾是难点。综合看，GPT-5.5 更可能帮助推进特殊情形、弱化版本和验证框架，而不是独立完成完整猜想。

### 免责声明

以上是关于 AI 可推进性的审查判断，不是该 Erdős 问题的证明或反例。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `likely_open`
- 状态信心: `high`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_60.md](../../prompts/problem_60.md)

### 状态结论

原题的弱形式可精确化为 h(n)=Ω(√n)，并且仍很可能公开未解。Erdős Problems 的 2025 年页面仍标为 OPEN；He–Ma–Yang 的同行评审论文只在无穷子序列 n=q²+q+1（特别是 q=2^k）上给出精确结果；2025 年论文仍将一般情形称作长期猜想。未发现可核查的一般证明或反例。

### 当前规范陈述

令 C4 为长度 4 的简单环，ex(n,C4) 为所有 n 顶点、不含 C4 的有限简单图的最大边数，#C4(G) 为 G 中与 C4 同构的无标号子图数。令 h(n)=min{#C4(G): |V(G)|=n, |E(G)|=ex(n,C4)+1}。原文“≫n^{1/2}”的标准精确读法为：存在绝对常数 c>0 与 N，使每个 n≥N 及每个满足 |V(G)|=n、|E(G)|>ex(n,C4) 的有限简单图 G 都有 #C4(G)≥c√n。等价地，h(n)≥c√n；只需处理恰有 ex(n,C4)+1 条边的情形。

```text
Let C4 be the simple cycle of length four, let ex(n,C4) be the maximum number of edges in a finite simple n-vertex C4-free graph, and let #C4(G) count unlabelled subgraphs of G isomorphic to C4. Define h(n)=min{#C4(G): |V(G)|=n, |E(G)|=ex(n,C4)+1}. The literal “≫ n^{1/2}” formulation is canonically read as: there are absolute constants c>0 and N such that, for every integer n≥N, every finite simple graph G with |V(G)|=n and |E(G)|>ex(n,C4) satisfies #C4(G)≥c√n. Equivalently, h(n)≥c√n for all n≥N; it suffices to consider exactly ex(n,C4)+1 edges by deleting excess edges.
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 已核查有限小 n 的反例文献：Qiao–Zhan 证明 n=6,…,11 时可恰有一个 C4，但这不影响渐近命题。未找到对任意大的 n 构造 o(√n) 个 C4 的可核查反例。Ning–Zhai 的预印本/论文文字称 He–Ma–Yang 曾“announced”某些 q²+q+2 情形反驳“至少两个 C4”的弱猜想；但当前 He–Ma–Yang v4/同行评审文本没有这一断言，且与其明确陈述的正向无穷子序列结果不相符。因此该二手主张不能作为反例，须人工追溯版本或作者说明。
- 版本变化: 1984 年 Erdős–Simonovits 提出强形式 h(n)≥(1+o(1))√n；Erdős 的另一弱问法仅要求最终 h(n)≥2。He–Ma–Yang（2021，后扩展为 2023 同行评审版）证明 q=2^k 的无穷子序列上 h(q²+q+1)=q−1，并刻画低计数极值图，因而验证强形式于该子序列。原数据库条目保留的是较弱的 Ω(√n) 总体目标；这不是已被替换的命题，而是强猜想尚未解决时仍有意义的弱残余目标。

陈述问题：

- 原文没有说明图为有限简单图、C4 拷贝按无标号子图计数，且没有把“≫”的绝对常数和“充分大 n”量词写明。
- “>ex(n;C4)”在整数边数下等价于“≥ex(n,C4)+1”；删边可把研究归约到恰好 ex(n,C4)+1 条边，但该归约应在证明中明说。
- 文献中的 Erdős–Simonovits 强形式是 h(n)≥(1+o(1))√n；数据库的“≫√n”是较弱的 Ω(√n) 版本。二者不可混同。
- 输入备注“n=q²+q+1 for some even integer q”过宽：可直接核查的精确结论用于 q=2^k 的无穷子序列；一般偶数 q 的表述涉及有限射影平面/极性图存在性及 ex 的精确值，不能不加条件地代入。

需要固定的量词/约定：

- All graphs are finite, undirected, loopless, and without multiple edges.
- The assertion is asymptotic: ∃c>0 ∃N ∀ integers n≥N ∀G with |V(G)|=n and e(G)>ex(n,C4), #C4(G)≥c√n.
- #C4(G) counts distinct unlabelled copies; equivalently, 4-element vertex sets whose induced/subgraph edge set contains a cycle C4, with each cycle counted once as a subgraph.
- The exact-edge formulation h(n) uses e(G)=ex(n,C4)+1. It is equivalent to the all-excess formulation because an ex(n,C4)+1-edge subgraph can be selected from G and deleting edges cannot create C4 copies.
- The historically strongest stated conjecture is h(n)≥(1+o(1))√n, meaning h(n)/√n has lower limit at least 1.

### 文献与当前边界

已核验的主要结果：

- Füredi 的结果给出 ex(q²+q+1,C4)≤q(q+1)²/2；对足够大的素数幂 q，有限几何的正交极性图给出相等式。这是 He–Ma–Yang 精确超饱和论证的阈值基础。
- He–Ma–Yang 的已核查结果：对 q=2^k、k≥40，h(q²+q+1)=q−1；极值图恰为在正交极性图两个度为 q 的顶点间加一条边。更一般地，他们对小 t 给出 h(q²+q+1,t)=t(q−1) 的精确范围，并研究更大 t。
- Qiao–Zhan 只给出有限 n=6,…,13 的最小 C4 数信息。它表明若遗漏“充分大 n”，弱的“至少两个”文字会被小参数反例击穿。
- Nagy 研究的是平衡二分图、以 Zarankiewicz 数为阈值的 C4 超饱和问题；其有限设计和码度计数方法可作背景，但不解决非二分、精确 ex(n,C4)+1 的原题。

最近相关工作：本次检索中最晚直接提及原猜想的是 Ning–Zhai 的 2025 年同行评审论文；它仍在引言中将一般问题称为长期猜想，但论文主定理转向谱半径阈值。未检出 2023–2026 年间给出原题一般解答的可核查论文或正式反例。

剩余核心：证明存在绝对 c>0，使每个充分大的 n 均满足 h(n)≥c√n；更强的历史目标是 h(n)≥(1+o(1))√n。核心困难是一般 n 的 ex(n,C4) 及其极值图缺乏精确结构，不能把 q=2^k 的极性图稳定性直接推广。

已使用方法：

- 码度/二路径双计数，把 C4 数表示为顶点对共同邻居数的二项式和。
- Reiman/Füredi 型极值上界与度序列凸性估计。
- 正交极性图、有限射影平面及其局部结构。
- 极值 C4-free 图的稳定性：少 C4 的超阈值图须接近极性图。
- 二分 Zarankiewicz 超饱和、设计和差集构造；仅作可比较但不同模型的工具。

争议或不确定性：

- Ning–Zhai 旧版/2025 论文引言中关于 He–Ma–Yang 已宣布 q²+q+2 反驳“至少两个 C4”弱猜想的说法，与已检查的 He–Ma–Yang arXiv v4 和 2023 同行评审文本不一致。该说法没有可检查构造，不能用来判定本题已被反驳。
- 没有穷尽所有非英语文献、未索引预印本和个人网页；“likely_open”是有强证据支持的文献状态判断，不是不存在未来或未检索解答的逻辑证明。

### 证据来源

- [Erdős Problems – Problem 60](https://www.erdosproblems.com/60) — Thomas F. Bloom (database owner), 2025-11-18; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 页面把该题标为 OPEN，并给出 Ω(√n) 表述及 He–Ma–Yang 的无穷子序列结果；它是当前状态的数据库证据，不是证明。
- [60 Discussion Thread | Erdős Problems](https://www.erdosproblems.com/forum/thread/60) — Thomas F. Bloom / forum, date unknown; `forum`, `informal_claim`, directness=`direct`, reliability=`medium`. 线程没有任何完整或部分解答声称；重述数据库的 OPEN 状态和 He–Ma–Yang 引文。
- [Some exact results on 4-cycles: stability and supersaturation](https://arxiv.org/pdf/1912.00986) — Jialin He, Jie Ma, Tianchi Yang, 2021-01-28; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 精确定义 h(n,t)；将强猜想写为 h(n)≥(1+o(1))√n；证明 q=2^k、k≥40 时 h(q²+q+1)=q−1，并给出更一般的低超饱和计数结果。
- [Some Exact Results on 4-Cycles: Stability and Supersaturation](https://www.global-sci.com/csiam-am/article/view/7823) — Jialin He, Jie Ma, Tianchi Yang, 2023; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 同行评审版确认其结论仅验证 Erdős–Simonovits 猜想于无穷多个 n，并陈述一般 n 的强猜想仍为长期猜想。
- [Some extremal results on 4-cycles](https://www.sciencedirect.com/science/article/pii/S0095895621000071) — Jialin He, Jie Ma, Tianchi Yang, 2021; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 原始 JCTB 论文的摘要说明其以稳定性和有限几何方法确认该长期猜想的无穷多个情形。
- [Counting substructures and eigenvalues II: quadrilaterals](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v32i4p1/pdf/) — Bo Ning, Mingqing Zhai, 2025-10-03; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 该文引言仍把一般 C4 的 ex(n,C4)+1 计数问题称为长期猜想，但本文实际解决的是不同的谱半径条件下的计数问题，不能当作原题的证明。
- [On a problem of Erdős about graphs whose size is the Turán number plus one](https://www.cambridge.org/core/journals/bulletin-of-the-australian-mathematical-society/article/abs/on-a-problem-of-erdos-about-graphs-whose-size-is-the-turan-number-plus-one/E5E215F3ACD73F6164C862E5078BE13D) — Pu Qiao, Xingzhi Zhan, 2022; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 证明 n=6,…,11 的 C4 情形可恰有一个拷贝，n=12,13 的最小数为二；仅提供小参数边界审计，未触及渐近目标。
- [Supersaturation of C4: From Zarankiewicz towards Erdős–Simonovits–Sidorenko](https://real.mtak.hu/83888/) — Zoltán Lóránt Nagy, 2019; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 给出二分 Zarankiewicz/超饱和模型中的精确和渐近结果，说明设计与有限几何方法的相关背景；其阈值和图类不同于原题。
- [Counting substructures and eigenvalues II: quadrilaterals](https://arxiv.org/abs/2112.15279) — Bo Ning, Mingqing Zhai, 2021-12-31; `preprint`, `preprint`, directness=`indirect`, reliability=`medium`. 其旧版文字声称 He–Ma–Yang 曾宣布 q²+q+2、q=4^k 情形反驳“至少两个 C4”的弱猜想；该说法未在被检查的 He–Ma–Yang v4 或同行评审版中找到可核查支撑，构成待人工核实的冲突，而非已验证反例。

### 完成标准

- 肯定出口: Prove that there exist absolute constants c>0 and N such that for every integer n≥N and every finite simple n-vertex graph G with e(G)≥ex(n,C4)+1, #C4(G)≥c√n. A stronger acceptable affirmative resolution may prove h(n)≥(1-o(1))√n or h(n)≥(1+o(1))√n with its precise asymptotic interpretation.
- 否定出口: Disprove the literal Ω(√n) target by proving its negation: for every c>0 and N there are an integer n≥N and a finite simple graph G with v(G)=n, e(G)=ex(n,C4)+1, and #C4(G)<c√n. In particular, an explicit infinite family with #C4(G_n)=o(√|V(G_n)|), together with a proof of the exact ex(n,C4) edge condition, is decisive.

不构成完成：

- A result only for n=q^2+q+1, or only for q=2^k, without a mechanism covering all sufficiently large n.
- A lower bound at an edge count expressed using Reiman's upper bound, a Zarankiewicz number, or another surrogate threshold unless it is proved to be at most ex(n,C4)+1 in the required direction.
- A proof for bipartite graphs, triangle-free graphs, regular graphs, or spectral-radius hypotheses only.
- A finite computational verification, no matter how large, without an all-n theorem or a certified infinite construction.
- Showing merely that every such graph contains one C4, or that the assertion holds along a density-one/subsequence set of n.
- A construction with few C4s whose edge count is not proved equal to ex(n,C4)+1.ൈവ

正确性陷阱：

- Do not replace ex(n,C4) by its asymptotic value: the problem is at an additive-one threshold, where an o(n^{3/2}) error is overwhelming.
- Keep the direction of threshold comparisons correct. A graph with more than a known lower bound for ex(n,C4) need not have ex(n,C4)+1 edges.
- Specify whether C4 copies are labelled, induced, or ordinary subgraphs; the canonical target uses unlabelled ordinary subgraphs.
- Justify the reduction from e>ex(n,C4) to e=ex(n,C4)+1 by choosing a spanning edge-subgraph and using monotonicity of C4 counts.
- For polarity constructions, establish the finite-field/projective-plane existence, exact order, degrees, C4-freeness, and exact number of newly formed C4s.
- Do not generalize a q=2^k statement to all even q; general even q need not supply the same finite-geometric construction or equality for ex.
- Distinguish the weak Ω(√n) target from the stronger (1+o(1))√n conjecture.

### 更新后的 AI 可解答性

- 等级: `low_candidate`
- 分数: `18/100`
- 信心: `high`
- 结论: 这是定义良好但难度很高的开放证明目标；AI 可协助形成和审计局部引理、比较极值结构，却不宜把有限搜索或 q=2^k 特例误当作一般突破。

支持理由：

- 目标有清晰的极值函数 h(n) 和可判定的正反完成条件。
- 已有强的无穷子序列精确结果、稳定性定理和有限几何模型，为可检验的局部结构引理提供了锚点。
- 原题仅要求 Ω(√n)，形式上弱于历史的常数 1 渐近猜想。

主要障碍：

- 一般 n 的 ex(n,C4) 与极值图结构未知，恰好是加一条边时计数问题的关键输入。
- 子序列极性图高度刚性，无法直接控制不接近射影平面参数的 n。
- 常规全局二路径/码度下界在精确阈值处损失过大；必须获得结构性而非仅平均性的信息。
- 可能存在未核实的关于弱“至少两个”版本的二手声称，开始研究前应先消解该文献冲突。

Proof-first 路线：

- 先证明一个明确的结构二分引理：若 #C4(G)<c√n，则 G 与某种近极性 C4-free 核之间必须满足可量化的编辑/度/码度约束；再证明该约束在一般 n 下不可能或已产生足够多 C4。
- 发展不依赖精确 ex(n,C4) 的“删除一条边/饱和核心”论证：从极小反例抽取 C4-free 边删除结构，并把每条候选补边的共同邻居对计数汇总。
- 比较一般 n 与邻近素数幂极性图时，必须先建立保留加一阈值的精确嵌入或稳定性引理；粗略填充顶点的构造不足。

需要验证：

- 人工核实 Ning–Zhai 对 q²+q+2、q=4^k 的二手“announced”说法所指的版本、构造和后续更正。
- 对 2023–2026 的 MathSciNet/zbMATH、arXiv 及作者发表列表作最终人工补检，特别检索 h(n,1)、Erdős–Simonovits C4 和 exact supersaturation。
- 任何声称的证明必须逐项核对其边数是否为真正的 ex(n,C4)+1，而不是 Füredi/Reiman 的代理值。

### 审计限制与人工复核理由

- 本审计使用公开网页、arXiv、期刊页和可访问 PDF；未能对所有索引库及未公开手稿作穷尽检索。
- 未直接检查 1984 原始章节的全文；强形式通过 He–Ma–Yang 的明确引述和后续论文交叉核对。
- Ning–Zhai 关于 q²+q+2 的二手陈述与当前 He–Ma–Yang 版本冲突，必须在启动长期研究前由人工追溯其所称公告或更正。

- 需人工处理 Ning–Zhai 的二手“宣布反例”说法与 He–Ma–Yang 当前正式版本之间的冲突；在未取得构造和精确 ex 证明前，不能据此改判为 disproved。
- 建议对 MathSciNet/zbMATH 和作者 2026 年发表列表作一次最终补检，以降低近期未收录解决方案的风险。

<!-- DEEP_REVIEW:END -->
