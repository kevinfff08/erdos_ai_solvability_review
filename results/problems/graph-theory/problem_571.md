# Problem 571

## 基本信息

- 原始链接: https://www.erdosproblems.com/571
- LaTeX 页面: https://www.erdosproblems.com/latex/571
- 原始状态: `open`
- 奖金: `no`
- 主类别: `graph theory`
- 原始标签: `graph theory`, `turan number`
- 形式化状态: `no`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

Show that for any rational $\alpha \in [1,2)$ there exists a bipartite graph $G$ such that\[\mathrm{ex}(n;G)\asymp n^{\alpha}.\]

## AI 完成可能性判断

- 结论: **AI 可能做出局部推进或搜索反例，但完整解决把握不足**
- 等级: `low_to_medium_candidate`
- 分数: `52/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 题面或备注出现有限对象/计算线索

### 主要障碍

- 主要风险是候选证明或计算证书容易存在隐藏漏洞，需要独立复核。

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: graph theory, turan number
- 证明密集标签命中: 无
- 有限/计算线索: counterexample, finite, graph
- 渐近/无限线索: 无
- 构造/存在性线索: counterexample

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5 with computation, formalization, literature search, and counterexample-search tools`
- 结论: **整体不太可能由 GPT-5.5 级别模型一次性完成完整证明，但有现实机会显著推进若干子族、整理并验证已有构造框架，或发现新的候选单图 Turán 指数。该题要求对所有有理 alpha∈[1,2) 构造单个二部图 G，而已知结果仍是分散的参数族；难点更像需要新组合结构与上下界技术，而不是单纯计算或形式化补全。**
- 等级: `low_to_medium_candidate`
- 分数: `32/100`
- 信心: `medium`
- 可能路线: 较现实的路线是把问题拆成可验证的参数化构造搜索：从已知 Turán 指数族出发，抽象其共同模板，生成候选二部图或 rooted graph blow-up / product 类型构造；用符号计算检查密度参数、平衡条件和可望给出的指数；用文献检索定位尚未覆盖的有理区间；对具体小分母 alpha 尝试给出单图候选，并分别寻找随机代数下界与容器法、依赖随机选择、分层 BFS 或 embedding lemma 类型上界。形式化证明工具更适合验证局部引理和参数不等式，而不是直接发现完整通用构造。

### 支持理由

- 问题陈述短，但目标是覆盖所有有理 alpha∈[1,2)，量化范围极大；这通常需要统一构造原理而非逐例证明。
- 备注中显示已有结果只覆盖多个特殊参数族，且有限图族版本已知比单图版本容易，这说明核心障碍正是从 family 到 single graph 的结构转化。
- GPT-5.5 级模型可有效做文献图谱、参数区间覆盖分析、构造模板归纳、候选图自动生成和小参数验证，这些能帮助推进问题。
- 该问题的上下界都很强：既要构造 G 使 ex(n;G) 有给定幂次下界，又要证明匹配上界；两端通常依赖深组合证明，自动化难度高。
- 没有显式形式化版本和 OEIS/计算序列入口，说明可直接机械验证的对象较少，工具价值主要在辅助发现和局部证明检查。

### 主要障碍

- 最大障碍是需要一个覆盖所有有理指数的单图构造理论；已知有限 family 结果不能直接满足题目要求。
- 对特定二部图的精确 Turán 指数通常很难确定，候选图即使计算上看合理，也常缺少匹配上界。
- 下界往往需要随机代数、有限域或概率构造；上界则可能需要高度定制的嵌入和计数论证，二者难以由通用搜索自动产生。
- 已有已知指数族之间的缺口可能并非简单参数优化能填补，可能需要新的 graph operation 或新的 extremal lemma。
- 若模型误把有限图族结果、渐近上下界不匹配的结果、或只对无限子序列 n 成立的结果当作单图 Turán 指数，会产生伪进展。

### 需要的验证

- 对任何候选 alpha 和候选 G，必须分别验证 ex(n;G)=O(n^alpha) 与 ex(n;G)=Omega(n^alpha)，并确认常数不依赖 n。
- 需要检查 G 是固定有限二部图，而不是随 n 或随构造规模变化的图，也不是有限禁止图族。
- 需要系统核对参数范围，避免与备注中已有族重复，明确新覆盖的有理指数。
- 若使用计算搜索，应输出可复现的候选图编码、密度参数、预期指数和失败案例。
- 若给出新证明，应由领域专家审读，并尽量将核心不等式、归纳步骤和小参数边界条件形式化验证。

### 公开版思考摘要

该题不是计算型猜想，而是极值图论中关于所有有理 Turán 指数的统一构造问题。GPT-5.5 级模型配合工具可以在局部参数族、候选构造搜索、文献整合和证明校验上产生价值，尤其可能发现可投稿的特殊情形或简化已有技术。但要一次性证明“所有有理 alpha”需要新的深层组合思想，现有工具链对这种发现的可靠性有限。因此评为 low_to_medium_candidate：可显著辅助推进，但完整解决概率偏低。

### 免责声明

以上是对 AI 辅助可解决性和推进路径的审查，不是该 Erdős 问题的证明，也不声称给出了新的 Turán 指数构造。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `likely_open`
- 状态信心: `medium`
- 可行动性: `research_ready`
- 人工复核: `not_required`
- 独立研究 Prompt: [prompts/problem_571.md](../../prompts/problem_571.md)

### 状态结论

截至 2026-07-27，直接的 Erdős Problems 题页/论坛页仍标为 open，且明确显示没有评论中的解答或部分解答声明。针对精确题意、题号、命名猜想和 2024–2026 文献的检索未发现把“有限禁图族”提升为“单个二部禁图”并覆盖全部有理 α∈(1,2) 的可审查证明。2025、2026 年仍有将其称为未解猜想并仅给出相关新结果的 arXiv 工作。因此最审慎分类为 likely_open（非逻辑意义上的已穷尽证明），可作为研究目标。

### 当前规范陈述

对每个有理数 α（1≤α<2），存在一个有限简单二部图 G=G(α)，以及可依赖于 G（因而可依赖于 α）的常数 c,C>0 和 n0，使得对每个 n≥n0，都有 c n^α≤ex(n,G)≤C n^α。这里 ex(n,G) 是不含 G 作为（非诱导）子图的 n 顶点有限简单图的最大边数；即 ex(n,G)=Θ(n^α)。实质未解部分是 α∈Q∩(1,2)；端点 α=1 是初等情形。

```text
For every rational number α with 1 ≤ α < 2, there exists a finite simple bipartite graph G=G(α) and constants c,C>0 and n0∈N (all allowed to depend on G, hence on α) such that, for every integer n≥n0, c n^α ≤ ex(n,G) ≤ C n^α. Here ex(n,G) is the maximum number of edges of a finite simple n-vertex graph containing no (not necessarily induced) subgraph isomorphic to G. Equivalently, ex(n,G)=Θ(n^α) as n→∞. The substantive unresolved range is α∈Q∩(1,2); α=1 is elementary.
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 未发现能否定字面陈述的简单构造。相反，唯一需单独处理的端点 α=1 可由 G=P3 立即满足：P3-free 图的每个连通分量至多是一条边，所以 ex(n,P3)=⌊n/2⌋。这表明题目应集中于开区间 (1,2)，而非需要修复。
- 版本变化: 题页的当前文本和 2026-03-07 的论坛镜像均保持单图版本，并将有限图族版本明确列为 Bukh–Conlon 的较弱变体。Kang–Kim–Liu 提出 subdivision conjecture，并证明其若成立则推出本猜想；这是一条充分条件，不是对原题的替代或已证明等价。近年结果不断扩大可实现指数族，但未见将原命题拆分为一个已解决和一个不同残余命题的正式修订。

陈述问题：

- 输入中的 \asymp 未明示常数、阈值及 n→∞；按极值图论惯例应解释为 Θ，并允许常数依赖于所选 G。
- 输入未明说图是否为有限简单、禁图是否为诱导子图；文献中的 ex(n,G) 使用有限简单图和通常（非诱导）子图禁法。
- 题面包含 α=1，但文献通常将猜想写成 (1,2)；这不是反例或实质歧义，因为取 G=P3 时 ex(n,P3)=⌊n/2⌋=Θ(n)。

需要固定的量词/约定：

- The order is ∀α∈Q∩[1,2) ∃ a finite bipartite graph G ∃c,C,n0 ∀n≥n0.
- G, c, C, and n0 may depend on α; c,C,n0 may not depend on n.
- The host graphs in ex(n,G) need not be bipartite; only the forbidden graph G is required to be bipartite.
- The occurrence relation is ordinary subgraph containment, not induced containment.

### 文献与当前边界

已核验的主要结果：

- Bukh–Conlon（JEMS, 2018）对每个有理 r∈(1,2) 构造有限禁图族 H_r，满足 ex(n,H_r)=Θ(n^r)。这是严格较弱的命题，不能通过选取该族中一个成员而得到单图结论。
- Kang–Kim–Liu（JCTB, 2021；预印本 2018）实现所有 2−a/b（b>a，b≡±1 mod a），并证明 subdivision conjecture 会推出完整猜想；该条件尚非定理。
- Jiang–Ma–Yepremyan（CPC, 2022）给出 2−2/(2b+1)（b≥2）及 7/5；Conlon–Janzer–Lee（Combinatorica, 2021）与 Jiang–Qiu（SIAM J. Discrete Math., 2020）经细分给出更多显式指数。
- Jiang–Jiang–Ma（arXiv:2007.02975）实现一组满足其算术不等式的 2−a/b；Conlon–Janzer（Advances in Combinatorics, 2022）实现 b≥max{a,(a−1)^2} 的 2−a/b；Jiang–Qiu（CPC, 2023）实现 1+a/b（b>a^2）等大族。

最近相关工作：检索到的最晚直接相关工作是 Liu–Yang，arXiv:2607.07157（2026-07-08），其研究最小反馈点数受限二部图并证明特定图 E^+_{k,t} 的 ex(n,E^+_{k,t})=Θ(n^{(3k−1)/(2k−1)})。此外 Dong–Gao–Li–Liu，arXiv:2506.09020（2025）把“所有有理指数”推广到一个小的诱导禁图族，但两者均未给出本题单图版本的全覆盖。

剩余核心：对每个指定的有理 α∈(1,2)，构造一个单一有限二部图 G_α，并证明匹配的全局下界和上界 ex(n,G_α)=Θ(n^α)。尤其不能把有限图族结论、诱导禁图结论、仅上界、或仅一个新的指数族当作全题的完成。

已使用方法：

- 随机代数构造和有限域上的计数：用于产生稠密的无禁图构造，从而给出下界。
- 嵌入/双计数、最小度清理、Kővári–Sós–Turán 型论证：用于相应的上界。
- 平衡根树及其根部 blow-up：解释并控制有限禁图族的指数。
- 细分、densification 与特定二部图的路径计数：将已知精确极值估计转化为新的单图 Turán 指数。
- 超饱和与正则化/非重路径技术：近年细分极值问题中常见，但尚未给出统一闭合机制。

争议或不确定性：

- “仍未解决”主要由 2026-03 的题页、无论坛解答记录、近年论文持续称其为 conjecture，以及针对性检索无完整证明共同支持；这仍不是穷尽所有未索引文献的逻辑证明。
- 原始历史归属在资料中有不同引文年份；这不影响当前数学目标或状态。
- 输入列出的每一条已知指数公式未逐条重新通读原论文验证；本审计只把经主页面和抽样主文献支持的结果作为文献地形，而不以该列表证明完备性。

### 证据来源

- [Erdős Problem #571](https://www.erdosproblems.com/571) — Thomas F. Bloom (site record), 2026-03-07; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 当前数据库陈述、已知指数列表及 open 标签；该页自身提醒状态反映站点所有者的信念，不能单独充当完备文献结论。
- [571 Discussion Thread | Erdős Problems](https://www.erdosproblems.com/forum/thread/571) — Erdős Problems forum, 2026-03-07; `forum`, `informal_claim`, directness=`direct`, reliability=`medium`. 页面仍标记 OPEN，且显示“没有评论中的解答、部分或完整解答声明”；同时复述单图/有限族的区分。
- [Rational exponents in extremal graph theory](https://arxiv.org/abs/1506.06406) — Boris Bukh; David Conlon, 2015-06-21; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 证明对每个 1 与 2 之间的有理数存在一个禁图有限族 H_r，使 ex(n,H_r)=Θ(n^r)；该结果不构造单一禁图。
- [Rational exponents in extremal graph theory](https://authors.library.caltech.edu/records/fjteg-4ys50) — Boris Bukh; David Conlon, 2018-05-22; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 确认 Bukh–Conlon 结果发表在 Journal of the European Mathematical Society（2018），并确认其摘要所述对象为图族。
- [On the rational Turán exponents conjecture](https://arxiv.org/abs/1811.06916) — Dong Yeap Kang; Jaehoon Kim; Hong Liu, 2018-11-16; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 证明 b>a 且 b≡±1 mod a 时 2−a/b 可实现，并提出 subdivision conjecture；论文明确只证明后者会蕴含全体有理指数猜想。
- [Rational exponents near two](https://www.advancesincombinatorics.com/article/57310-rational-exponents-near-two) — David Conlon; Oliver Janzer, 2022-12-23; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 证明形如 2−a/b 且 b≥max{a,(a−1)^2} 的指数可实现，并明确说明单图原猜想仍 open。
- [More on the extremal number of subdivisions](https://arxiv.org/abs/1903.10631) — David Conlon; Oliver Janzer; Joonkyung Lee, 2019-03-25; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 给出一族明确单图的精确指数 1+s/(sk+1)，并通过 subdivision 方法产生无限多个新 Turán 指数。
- [Many Turán exponents via subdivisions](https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/abs/many-turan-exponents-via-subdivisions/3AF62F3C0AAEA4C1EFE0C7CC5D41CA24) — Tao Jiang; Yu Qiu, 2023-01-01; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 发表版确认该文继续通过 subdivision 建立大参数的可实现指数族，而其引言仍把“每个有理 r∈(1,2)”表述为 conjecture。
- [Induced rational exponents and bipartite subgraphs in K_{s,s}-free graphs](https://arxiv.org/abs/2506.09020) — Zichao Dong; Jun Gao; Ruonan Li; Hong Liu, 2025-06-10; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 近期工作只在“至多 2^a 个诱导禁二部图的图族”框架中实现所有有理指数，不能解决本题的单一、非诱导禁图版本。
- [On Turán Number of Graphs with Small Minimum Feedback Vertex Numbers](https://arxiv.org/abs/2607.07157) — Xiao-Chuan Liu; Xu Yang, 2026-07-08; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 最新相关工作研究反馈点数受限的二部图，并给出一个具体指数族；其内容是局部进展而非全体有理指数的解决。

### 完成标准

- 肯定出口: For every rational α∈(1,2), give an explicit finite simple bipartite graph G_α and prove constants c_α,C_α>0 and n0(α) such that c_α n^α≤ex(n,G_α)≤C_α n^α for every n≥n0(α). A uniform construction indexed by reduced fractions is acceptable only if both inequalities are proved for every index.
- 否定出口: Disprove the statement by exhibiting a specific rational α∈(1,2) and proving that no finite simple bipartite graph G satisfies ex(n,G)=Θ(n^α). The universal nonexistence quantifier over G must be discharged rigorously; a failure of one construction or one method is not a negative resolution.

不构成完成：

- Proving the claim only for a finite forbidden family H_α, even if each member is bipartite.
- Proving an induced-forbidden-family analogue or working under an additional host-graph restriction such as K_{s,s}-freeness.
- Producing only ex(n,G)=O(n^α) or only ex(n,G)=Ω(n^α), or matching bounds with different exponents/logarithmic gaps.
- Realising infinitely many exponents, a dense subinterval, or a parametrized family that leaves some rational α untreated.
- Showing the subdivision conjecture would imply the target without proving the required subdivision bound.
- Finite-n computations or numerical exponent fits without asymptotic certificates.

正确性陷阱：

- Verify that the forbidden object is one graph G_α, not a union or a family whose avoidance has been silently substituted for G_α-freeness.
- Check containment direction: if F⊆G, then ex(n,F)≤ex(n,G); this direction often invalidates attempts to merge forbidden graphs.
- State and prove both Θ constants and the sufficiently-large-n threshold; do not infer a lower bound from a construction at a sparse subsequence without a valid interpolation argument.
- Verify G_α is finite, simple, and bipartite, while the host graphs are arbitrary simple graphs.
- Treat α=1 separately (e.g. P3); do not claim the difficult range starts at the closed endpoint.
- When using rooted blow-ups or subdivisions, audit balance hypotheses, root identifications, multiplicity/disjointness requirements, and every parameter integrality condition.

### 更新后的 AI 可解答性

- 等级: `low_candidate`
- 分数: `16/100`
- 信心: `medium`
- 结论: 这是定义清楚、可逐步验证但极难的开放猜想。AI 可在特定指数、根树/细分引理或上界嵌入论证上提供可检验贡献，但在当前证据下，独立完成全体有理指数的概率很低。

支持理由：

- 目标具有精确的量词结构，肯定/否定完成条件可被严格审计。
- 存在丰富而明确的构造和嵌入技术，局部新引理能形成可发表的中间进展。
- 已知结果覆盖多个算术指数族，提供了检验任何候选方法是否真正超越现状的基线。

主要障碍：

- 需要对任意有理数给出单一图的匹配上下界；有限禁图族方法的关键障碍正是无法保证同一个禁图承担上界。
- 极值上界往往依赖精细的路径/细分嵌入和参数条件；表面相近的指数公式通常不足以闭合缺口。
- 缺少一个已知可归约为有限计算的统一判据；计算很容易只产生启发式证据。

Proof-first 路线：

- 先为一个当前未覆盖的明确有理 α 选择候选 G，并将工作拆为独立的下界构造与上界嵌入定理；只有两边指数完全一致才推进。
- 尝试证明一个具有明确假设和结论的 subdivision 或 rooted-blow-up 上界引理，并逐项核对它是否真的会扩大已知的单图指数族。
- 研究有限图族构造中“某个成员出现”的上界能否在满足额外结构时稳定地强化为“指定成员出现”；任何强化须先经禁图包含方向审计。

需要验证：

- 对拟覆盖的 α 建立已知指数家族的精确成员资格，避免重复已有结果。
- 审阅每个候选图的二部性、有限性、根集合/细分定义及所有整数参数限制。
- 独立重证或逐行审查上下界中最强的嵌入计数步骤；不要把论文摘要或引用链当作证明。
- 若声称解决，至少由两条独立路线进行对抗性证明检查，并检索 arXiv、出版社、作者页面与 Erdős Problems 论坛以排除重复或已知错误。

### 审计限制与人工复核理由

- 本审计使用公开网页、arXiv、出版社/机构记录和题目论坛进行了针对性检索；未能对所有期刊数据库、预印本镜像、私人讲义及未索引稿件做逻辑穷尽。
- Erdős Problems 的 open 标签是站点编辑者的状态意见；其与近期论文的持续“conjecture”表述共同构成中等强度的开放性证据，而非开放性的数学证明。
- 有限图族结果、诱导禁图结果和单一非诱导禁图结果必须严格区分；本审计未把它们互相提升。
- 未逐篇重现所有输入列举论文的证明；对状态判断最关键的原始/近期来源已直接检查。

- 无

<!-- DEEP_REVIEW:END -->
