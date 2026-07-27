# Problem 82

## 基本信息

- 原始链接: https://www.erdosproblems.com/82
- LaTeX 页面: https://www.erdosproblems.com/latex/82
- 原始状态: `open`
- 奖金: `no`
- 主类别: `graph theory`
- 原始标签: `graph theory`
- 形式化状态: `yes`
- OEIS: `A120414`, `A390256`, `A390257`, `A390919`, `A392636`, `A394400`, `A394462`, `A394539`, `A394563`, `A394564`, `A394573`, `A394574`, `A394930`, `A394933`
- 原站备注字段: 无

## 原问题

Let $F(n)$ be maximal such that every graph on $n$ vertices contains a regular induced subgraph on at least $F(n)$ vertices. Prove that $F(n)/\log n\to \infty$.

## AI 完成可能性判断

- 结论: **AI 可能做出局部推进或搜索反例，但完整解决把握不足**
- 等级: `low_to_medium_candidate`
- 分数: `40/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 题面或备注出现有限对象/计算线索
- 已有形式化陈述，可降低语义误读风险
- 存在 OEIS 数据入口，利于实验与反例搜索

### 主要障碍

- 题面含渐近/无限对象线索：\gg, \ll, o(

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: graph theory
- 证明密集标签命中: 无
- 有限/计算线索: graph, ramsey
- 渐近/无限线索: \gg, \ll, o(
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5+tools`
- 结论: **不太可能一次性完成原问题的完整证明，但有中等偏低的机会显著推进：例如形式化等价表述、验证小规模值、搜索极端构造、证明若干图类或弱化版本，并可能发现通向 G(n) <= 2^{o(n)} 的可检验中间命题。**
- 等级: `low_to_medium_candidate`
- 分数: `42/100`
- 信心: `medium`
- 可能路线: 较现实的路线是围绕等价形式 G(n) <= 2^{o(n)} 建立自动化研究循环：用 SAT/ILP/约束搜索生成无大正则诱导子图的极端图；用图同构削减与OEIS数据校验小规模 G(k)；从极端样本中抽取结构猜想；再尝试用概率法、Ramsey型递推、度分层、诱导子图正则化或熵压缩证明比 c log n 更强的下界。形式化证明工具可用于验证递推、归纳引理和小规模枚举证书，但核心渐近突破仍需要新的组合思想。

### 支持理由

- 问题陈述短、对象离散，适合计算搜索、SAT编码、证书验证和形式化小引理验证。
- 已给出 formalized=yes，说明至少存在可形式化的定义或相关框架，降低了验证局部结论的门槛。
- 已知精确小值和多个OEIS条目表明该问题存在可扩展的实验数学入口，模型可通过枚举极端图生成猜想。
- 目标是把 Ramsey 定理给出的 F(n) >> log n 提升到 F(n)/log n -> infinity；这可能允许先证明弱增益版本，而不是直接给出强多项式下界。
- 等价表述 G(n) <= 2^{o(n)} 适合转化为递推不等式或禁子结构问题，便于机器辅助检验候选证明框架。

### 主要障碍

- 原问题是开放的渐近极值图论问题，核心难点不是计算验证，而是突破 Ramsey 型对数下界。
- 已知上界仍可低至 n^{1/2} 量级，说明极端构造可能复杂，简单随机图或常规 Ramsey 论证很可能不足。
- 小规模 G(k) 数据未必揭示渐近结构，模型从有限枚举外推时容易产生伪规律。
- 正则诱导子图约束同时涉及诱导性和内部度一致性，比寻找团或独立集更难用标准容器/谱方法直接处理。
- 即使发现候选递推或局部结构引理，形式化证明其适用于所有图可能是主要瓶颈。

### 需要的验证

- 建立独立的 SAT/ILP 或回溯枚举程序，复现给定的小规模结果，例如 G(5)=17、G(7)>=30 等相关断言。
- 对所有计算生成的极端图输出可审计证书，并用第二套程序或形式化检查器验证无目标大小的正则诱导子图。
- 将任何渐近证明拆成明确引理，分别检查量词、常数、递推闭合和从 G(n) 到 F(n) 的等价转换。
- 用随机图、伪随机图、分块构造和已知下界样式测试候选引理，优先寻找反例。
- 若提出弱化定理，例如 F(n) >= log n * omega_slow(n)，需要验证增长函数确实趋于无穷且不依赖隐藏常数。

### 公开版思考摘要

这个问题对AI工具链有吸引力，因为它是离散、可枚举、已有形式化与小规模数据支撑的图论问题；模型可以在实验数学、自动反例搜索和局部证明验证上发挥作用。但完整目标要求超越 Ramsey 对数保证，是一个真正的渐近组合突破。我的判断是：GPT-5.5级模型更可能贡献可验证的中间成果，而不是直接解决原命题。

### 免责声明

以上是对AI辅助可攻性的审查，不是问题82的证明，也不声称已经证明 F(n)/log n -> infinity。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `likely_open`
- 状态信心: `medium`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_82.md](../../prompts/problem_82.md)

### 状态结论

按可核验的当前记录，原猜想仍很可能开放：Erdős Problems 第82题仍标为 open；2026 年 Dyson–McKay 预印本给出显著上界改进及 G(k) 的二次下界，但并未声称证明 F(n)/log n→∞。由于该站点的状态日期早于这篇近期预印本，且未能以可检查证明排除所有未索引的最新结果，结论定为 likely_open（中等置信）而非 confirmed_open。

### 当前规范陈述

对有限简单无向图 G，令 r(G) 为满足 G[S] 为某个 d-正则图的顶点集 S⊆V(G) 的最大基数，其中整数 d 满足 0≤d≤|S|−1。对每个正整数 n，令 F(n)=min{r(G): |V(G)|=n}。证明（log 为任意固定底数大于 1 的对数）F(n)/log n 在 n→∞ 时趋于 +∞。等价地：对任意 C>0，存在 N(C)，使得每个 n≥N(C) 的 n 顶点简单图都含有一个至少 C log n 个顶点的诱导正则子图。

```text
For a finite simple undirected graph G, let r(G) be the maximum cardinality of a set S⊆V(G) such that the induced graph G[S] is d-regular for some integer d with 0≤d≤|S|−1. For each positive integer n, define F(n)=min{r(G): |V(G)|=n}. Prove that, with log denoting any fixed base greater than 1, lim_{n→∞} F(n)/log n=+∞. Equivalently: for every real C>0, there is N(C) such that every n-vertex finite simple graph has an induced regular subgraph on at least C log n vertices whenever n≥N(C).
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 未发现能否定上述规范化字面命题的简单构造。随机图及 Ramsey 型构造反而是已知上界和困难性的来源；它们不否定“相对于 log n 发散”的下界猜想。该结论仅表示完成了针对定义、0-正则子图和小参数的定向检查，并非穷尽性证明。
- 版本变化: 原始问题由 Erdős、Fajtlowicz、Stanton 猜想。文献和题页先给出 Ramsey 理论的 F(n)≳log n 下界及多次上界改进；近期 Dyson–McKay 预印本将已知上界推进到 F(n)≪√n，并给出 G(k) 的二次下界。这些进展未把原下界猜想改写为不同命题，也未宣称解决它。

陈述问题：

- 输入中“Let F(n) be maximal such that every graph ...”应严格解作对所有 n 顶点图所保证的最大整数，即 min_G max_S 的极值定义；否则“maximal”的量词层次不够明确。
- “regular induced subgraph”必须允许正则度 d=0；因而独立集及单顶点图都是正则诱导子图。完全图也属于正则诱导子图。
- 原题未指定对数底，但极限为无穷大的结论对任一固定底数 >1 等价。
- 备注中的 t(n) 问题和 G(k) 表述是相关的更强/等价渐近重述，不是 F(n)/log n→∞ 的定义本身；研究时不得把它们同一化为已证明或未经证明的结论。

需要固定的量词/约定：

- All graphs are finite, simple, undirected graphs.
- The regularity degree may depend on G and S and may be 0.
- F(n)=min over all n-vertex graphs of the maximum order of an induced regular subgraph.
- The limit assertion means: for every C>0, eventually F(n)≥C log n.
- Changing the fixed logarithm base only rescales C and does not change the assertion.

### 文献与当前边界

已核验的主要结果：

- Ramsey 定理给出 F(n)≳log n：每个 n 顶点图含有对数级独立集或团，二者均为诱导正则子图。
- 题页记录 Bollobás 的构造性上界 F(n)≪n^{1/2+o(1)}，随后将 AKS07 记为改进到 n^{1/2}(log n)^{O(1)}。这些是对最坏图的上界，不能支持待证下界。
- Dyson–McKay（2026，预印本）据题页进一步给出 F(n)≪√n；还证明 G(7)≥30，及充分大 k 时 G(k)≥(9/163)k²。
- Fajtlowicz、McColgan、Reid、Staton（1995）计算/界定了小值：题页记录 G(1)=1、G(2)=2、G(3)=5、G(4)=7、G(5)≥12。

最近相关工作：可直接定位的最新核心资料是 Dyson–McKay 的 2026 年 arXiv 预印本《Ramsey numbers for regular induced subgraphs》（arXiv:2604.08215）。它显著压低 F 的已知上界，却没有给出原猜想所需的超对数普遍下界。

剩余核心：证明或否定：对任意常数 C，每个充分大的 n 顶点图均有大小至少 C log n 的诱导正则子图。等价否定证据须给出某固定 C 与无界 n 序列上的图，使所有诱导正则子图大小至多 C log n。

已使用方法：

- Ramsey 理论：以团或独立集给出对数级基线。
- 概率法/随机或伪随机图构造：限制大诱导正则子图，用于 F 的上界及 G 的下界。
- 度数分布、诱导子图计数和近正则子图技术：AKS07 的相关工具线索。
- 小参数的穷举或计算构造：仅用于 G(k) 的具体值/下界，不足以决定渐近猜想。

争议或不确定性：

- 题库的 open 标签最后状态日期为 2025-08-31；其备注已含 2026 预印本，因此标签并非对 2026-07-27 的独立、带证明的状态认证。
- 没有发现可检验的 2026 年解决声明，但搜索未构成对全部新论文、论坛帖或未索引手稿的逻辑排除。
- 输入称该题已形式化，但未提供形式化仓库或定理链接；本审计未将“formalized”当作对原渐近猜想已证明的证据。

### 证据来源

- [Erdős Problem 82](https://www.erdosproblems.com/82) — Erdős Problems database, date unknown; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 给出原题、开放标签、历史归属、已知界、G(k) 的相关表述，以及对 AKS07 和 Dyson–McKay 的引文；其状态更新时间早于近期预印本，故不能单独确证 2026 年的开放状态。
- [Erdős Problem 82 LaTeX record](https://www.erdosproblems.com/latex/82) — Erdős Problems database, date unknown; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 用于核对题目文字、F(n) 与 G(n) 的定义以及题页的参考文献转录。
- [Large nearly regular induced subgraphs](https://arxiv.org/abs/0710.2106) — Noga Alon, Michael Krivelevich, Benny Sudakov, 2007; `preprint`, `preprint`, directness=`indirect`, reliability=`high`. AKS07 是题页所引、与早期 F(n) 上界改进相关的原始预印本；本审计不把其“nearly regular”结果误读为原问题的正面解答。
- [Ramsey numbers for regular induced subgraphs](https://arxiv.org/abs/2604.08215) — P. Dyson, B. McKay, 2026-04; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 题页归因该近期预印本证明 F(n)≪√n、G(7)≥30 及大 k 时 G(k)≥(9/163)k²；这些均为上界/反例构造方向的进展，非 F(n)/log n→∞ 的证明。

### 完成标准

- 肯定出口: A complete affirmative resolution is a rigorous proof that for every C>0 there exists N(C) such that every finite simple graph on n≥N(C) vertices has an induced d-regular subgraph on at least C log n vertices, with d allowed to depend on the graph and induced set.
- 否定出口: A complete negative resolution is a rigorous construction, for one fixed C<∞ and infinitely many unbounded n, of n-vertex finite simple graphs whose every induced regular subgraph has order at most C log n. This is exactly the negation of F(n)/log n→∞.

不构成完成：

- Proving F(n)≥c log n for one fixed constant c, including an improved fixed constant.
- Finding larger induced regular subgraphs for a restricted graph class only.
- Showing F(n)≥(log n)^{1+o(1)} only along a subsequence or under an unproved pseudorandomness hypothesis.
- Improving the upper bound F(n)≪√n, or computing finitely many values of G(k), without settling the required asymptotic lower bound.
- Proving existence of a large nearly regular, rather than exactly regular, induced subgraph without a justified conversion to exact regularity.

正确性陷阱：

- Keep the min over ambient graphs and max over induced vertex sets in the correct order.
- Verify inducedness: deleting edges after choosing vertices is not allowed.
- Treat 0-regular induced subgraphs correctly; independent sets are legitimate witnesses.
- Do not conflate an induced subgraph being regular with its vertices having equal degree in the ambient graph.
- For a purported disproof, the bound must hold for every induced regular subgraph of each constructed graph and on an unbounded sequence of orders.
- For a purported proof, all constants and the eventual threshold must be uniform over every n-vertex graph.

### 更新后的 AI 可解答性

- 等级: `low_candidate`
- 分数: `15/100`
- 信心: `medium`
- 结论: 这是定义清晰、可独立核验但难度很高的长期 Ramsey 型渐近问题；当前适合开展严谨的文献复核和小型引理探索，不宜预期短期由通用 AI 直接解决。

支持理由：

- 目标有精确的全称量词和明确的正/反证完成条件。
- 已有 Ramsey 基线、概率构造和近期上界结果可提供可检验的边界与反例压力测试。
- 原猜想的缺口仍是从常数倍 log n 到任意倍 log n 的全图一致提升，且已有数十年未解。

主要障碍：

- 必须对任意图获得精确正则诱导子图；近正则、平均度或非诱导结论通常不能转化。
- 随机图上界显示不能期待多项式规模保证，并且局部度数方法容易只重现 Ramsey 对数界。
- 有限计算不能证明极限，除非服务于一个可推广的、已明确陈述的引理。

Proof-first 路线：

- 先寻找可陈述为“若图缺少大小 L 的诱导正则子图，则其结构满足 X”的结构引理，并用其导出更大的团/独立集或直接正则集。
- 独立审计近期上界构造中阻止正则诱导子图的机制，判断其是否留下可逆的稳定性/容器式结构。
- 唯一可选计算任务：在预先固定的图类与候选结构引理下，搜索最小反例并要求输出可核验证书；停止条件为找到反例、穷尽规定规模，或判定该引理在该规模不可区分。

需要验证：

- 逐页核验 Dyson–McKay 预印本的定理陈述、适用定义和版本日期。
- 核验 AKS07 的确切结论，避免用题页概述替代原文定理。
- 在正式投入求解前，由人工或另一检索系统再次检查 2026-04 以后是否存在声称解决原猜想的论文、勘误或正式发表版本。
- 定位并核验输入所称的 formalization 对应的精确命题与依赖公理。

### 审计限制与人工复核理由

- 本审计只使用题目 JSON 所给的题目范围和公开网页检索；未检查周边仓库条目。
- Erdős Problems 的开放标签日期早于 Dyson–McKay 预印本；它是重要但非充分的当前状态证据。
- 未发现可检查的论坛解决声明或可定位的形式化工件链接，因此不能把“未发现”解释为不存在。
- AKS07 和 Dyson–McKay 的原文应在后续研究启动时逐条复核；这里没有以搜索摘要替代其完整证明。

- 需要人工逐页核验 2026 Dyson–McKay 预印本的定理、版本和是否含有未在题页概述的解决结论。
- 需再次检索 2026-04 至今的论文、作者页和论坛，以提高“仍开放”结论的置信度。
- 输入所列 formalized=yes 缺少工件 URL 和所形式化的精确命题，必须人工定位后确认其含义。

<!-- DEEP_REVIEW:END -->
