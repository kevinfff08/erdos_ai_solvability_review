# Problem 572

## 基本信息

- 原始链接: https://www.erdosproblems.com/572
- LaTeX 页面: https://www.erdosproblems.com/latex/572
- 原始状态: `open`
- 奖金: `no`
- 主类别: `graph theory`
- 原始标签: `graph theory`, `turan number`
- 形式化状态: `no`
- OEIS: `possible`
- 原站备注字段: 无

## 原问题

Show that for $k\geq 3$\[\mathrm{ex}(n;C_{2k})\gg n^{1+\frac{1}{k}}.\]

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

- 题面含渐近/无限对象线索：\gg, \ll

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: graph theory, turan number
- 证明密集标签命中: 无
- 有限/计算线索: graph
- 渐近/无限线索: \gg, \ll
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5级别模型+计算、形式化证明、文献检索与反例搜索工具`
- 结论: **低到中等候选。完整证明对所有 k>=3 的下界很可能需要新的极值图构造思想，难度明显高；但模型有机会在固定 k、候选代数构造验证、已知部分结果统一形式化、或改进弱下界路线方面做出实质推进。**
- 等级: `low_to_medium_candidate`
- 分数: `34/100`
- 信心: `medium`
- 可能路线: 最有希望的路线是构造型而非纯证明型：围绕有限域、Cayley 图、代数超图/图、lift、或高 girth/禁偶圈结构生成参数化候选图族；用计算搜索小参数模式，用 Gröbner 基、有限域符号计算或SAT/ILP排除 2k-圈；再把成功模式提升为一般 k 的代数引理，并形式化验证顶点数、边数和无 C_{2k} 性质。较现实的阶段性目标是先攻克若干未覆盖固定 k 或给出比题面 LUW95 指数更强的可证明下界。

### 支持理由

- 题目是渐近下界，核心产物可以是显式或半随机构造；这类证明较适合用计算搜索候选、自动检查小例子和形式化计数来辅助。
- 题面已给出 k=3、k=5 的成功构造以及任意 k 的较弱下界，说明存在可学习的构造模板和可对照的验证目标。
- 只需禁止一个指定偶圈 C_{2k}，不要求完全刻画 extremal graph；这给代数构造、有限域方程约束和有限搜索留下空间。
- 工具型模型可系统枚举并反驳大量候选构造，减少人类在低层代数验证和小参数实验上的成本。

### 主要障碍

- 题面标注 open，且已有结果只覆盖特殊 k 与弱指数，表明一般 k 的 n^{1+1/k} 下界不是简单推广。
- 达到 n^{1+1/k} 密度接近高 girth/Moore 型极限；随机图直接删圈通常会损失过多边，不能直接给出所需阶。
- 对任意 k 的统一构造需要同时控制长度恰为 2k 的闭路方程，代数条件可能随 k 急剧复杂化。
- 计算搜索只能覆盖有限参数；把小规模无圈现象提升为无限族证明是主要瓶颈。
- 即使模型提出候选，错误风险集中在无 C_{2k} 的全局证明和渐近量词处理上。

### 需要的验证

- 先做严格文献检索，确认候选路线没有被已知反例、上界或已有较弱定理覆盖。
- 对每个候选图族，独立验证顶点数为 Theta(N)、边数为 Omega(N^{1+1/k})，并明确常数可依赖于 k 但不依赖于 n。
- 用程序枚举小有限域/小参数实例，检测是否存在 C_{2k}，作为反例搜索而非最终证明。
- 对无 C_{2k} 的关键代数引理进行形式化或半形式化检查，特别是闭合 walk 与简单 cycle 的区别。
- 验证从无限参数子序列扩展到所有 n 的填充步骤，例如取子图、删点或单调性是否保持所需渐近下界。
- 请极值图论专家审阅候选证明，因为该问题的主要风险是构造看似正确但隐藏短偶圈。

### 公开版思考摘要

根据给定题面，这个问题要求为每个 k>=3 构造足够稠密的 C_{2k}-free 图。已知上界匹配目标阶，但题面只列出 k=3、k=5 的匹配下界和任意 k 的较弱下界，因此一般情形的核心缺口是构造。GPT-5.5 级别模型不应被视为很可能一次性解决该长期开放构造问题，但它适合承担系统搜索、代数验证、形式化计数和候选路线筛选，因而有低到中等概率产生可审计的局部推进。

### 免责声明

这不是该 Erdős 问题的解答，也未声称给出了满足下界的图族；这里只评估工具增强模型对该问题的潜在可解性、推进价值和验证需求。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `confirmed_open`
- 状态信心: `high`
- 可行动性: `research_ready`
- 人工复核: `not_required`
- 独立研究 Prompt: [prompts/problem_572.md](../../prompts/problem_572.md)

### 状态结论

按通常的“对每个固定 k、隐含常数可依赖于 k”解释，该问题仍为公开问题。2026 年同行评审文献仍明确称只有 k=2,3,5 已知达到 n^(1+1/k) 阶的下界；本题所含的 k=4 等情形仍未解决。原条目的 \gg 未写明常数及 k 与 n 的量词，须在研究时采用下述规范化版本。

### 当前规范陈述

设 ex(n,H) 是所有 n 阶有限简单图中不含 H 的（不要求诱导）子图者的最大边数，C_m 是长度为 m 的简单圈。证明：对每个固定整数 k>=3，存在 c_k>0 与 n_0(k)，使得每个 n>=n_0(k) 均有 ex(n,C_{2k})>=c_k n^(1+1/k)。等价地，对每个固定 k>=3，ex(n,C_{2k})=Omega_k(n^(1+1/k))。k=3,5 已知，实质未解部分为每个固定 k>=4 且 k!=5。

```text
Let ex(n,H) be the maximum number of edges in a finite simple graph on n vertices containing no (not necessarily induced) copy of H, and let C_m be the simple cycle of length m. Prove that for every fixed integer k >= 3 there exist constants c_k>0 and n_0(k) such that, for every integer n >= n_0(k), ex(n,C_{2k}) >= c_k n^{1+1/k}. Equivalently, ex(n,C_{2k}) = Omega_k(n^{1+1/k}) for every fixed k >= 3. The cases k=3 and k=5 are already known, so the surviving content is every fixed k >= 4 with k != 5.
```

### 陈述、量词与反例审计

- 歧义严重度: `material`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 未发现能否定上述固定-k规范版本的简单构造。检索到的 C8、C10 相关新结果讨论的是其他 Turán 问题、超立方体子图或“从 C10-自由图抽取 C8-自由稠密子图”的猜想，均不构成对本题的反例。
- 版本变化: Erdős Problems 历史页显示当前陈述与 2025-10-20 版本相同；页面于 2026-01-18 编辑。论坛的三条评论没有给出本题的解答声明，主要补充了上界和综述参考。

陈述问题：

- 原式没有明确 k 是固定参数，还是允许随 n 增长；标准且与文献一致的解释是“先固定 k，再令 n 趋于无穷”。
- 符号 \gg 未说明隐含常数的依赖性。若要求绝对常数同时适用于所有 k，便是显著更强、并非此历史问题的通常表述。
- 原条目说“for k>=3”，但 k=3 与 k=5 已由高围长有限几何构造解决；它不是“每个 k 都未解”的断言。
- 禁止的是恰好长度 2k 的圈，而非自动禁止所有较短圈；高围长构造可作为充分条件，但替代目标不得被误当作等价定义。

需要固定的量词/约定：

- Quantify k first: for every fixed integer k >= 3.
- The constants c_k and n_0(k) may depend on k but not on n.
- The assertion is eventually for every integer n, not merely an unspecified sparse sequence of orders.
- Graphs are finite, simple, undirected; C_{2k} is forbidden as a subgraph, not only as an induced, rainbow, ordered, or bipartite subgraph.

### 文献与当前边界

已核验的主要结果：

- Bondy–Simonovits（1974，同行评审）证明固定 k 的上界 ex(n,C_{2k})=O_k(n^(1+1/k))。Pikhurko（2012）改进一般常数为 ex(n,C_{2k})<=(k-1)n^(1+1/k)+16(k-1)n。
- Benson（1966，同行评审）的 girth 8、12 有限几何图给出 k=3 和 k=5 的目标下界；因此这两个本题内的参数已闭合。
- Lazebnik–Ustimenko–Woldar（1995/1999）的代数高围长图给出所有 k 的经典一般下界：若 k 奇则 Omega(n^(1+2/(3k-3)))，若 k 偶则 Omega(n^(1+2/(3k-2)))。
- Conlon（2021，预印本）以几何方式重述 Wenger 构造，直接验证其在 k=2,3,5 的 C_{2k}-自由性和目标量级。
- Byrne–Tait（2026，同行评审）仍将匹配下界限制为 k=2,3,5，故至少 k=4 的缺口截至审计日仍存在。

最近相关工作：最直接的近时状态证据是 Byrne 与 Tait 于 2026-06-01 在线发表的同行评审论文（Canadian Journal of Mathematics，DOI 10.4153/S0008414X26102314），其明确记载匹配下界仅知 k=2,3,5。Conlon–Mulrenin–Pohoata 的 2026 预印本研究 C8/C10 构造间的抽取现象，但未改进或解决 ex(n,C_{2k}) 的一般下界。

剩余核心：对每个固定 k>=4、k!=5，构造 n 阶 C_{2k}-自由简单图，边数达到 c_k n^(1+1/k)，其中 c_k>0 且对 n 独立。最小未解实例是 C8：已核到的经典下界为 Omega(n^(6/5))，目标为 Omega(n^(5/4))。

已使用方法：

- 有限几何与广义多边形的高围长关联图（成功于 k=3,5）。
- Wenger/代数点线关联图及其几何化解释。
- Lazebnik–Ustimenko 图 D(n,q)、其连通分支和极性操作。
- 路径计数、Theta 图与分层/平均度论证（一般上界）。
- 有限域代数构造、随机代数法及消去/结式工具；这些是邻近 Turán 问题中常用的构造技术，尚非本题一般解。

争议或不确定性：

- 未找到声称解决一般 k 的可核验论文或正式化产物；这不构成不存在此类工作的逻辑证明，但 2026 同行评审状态陈述与当前数据库一致。
- 输入中的 \gg 是否意图要求 k 一致的绝对常数并不明确；本审计采用历史文献一致的固定-k解释。
- 论坛评论为非正式材料；它们只用作线索和状态交叉检查，不作为下界定理的依据。

### 证据来源

- [Erdős Problems — Problem 572](https://www.erdosproblems.com/572) — Thomas F. Bloom (database editor), 2026-01-18; `problem_page`, `database_record`, directness=`direct`, reliability=`high`. 当前数据库仍标为 open，给出原陈述、Benson 的 k=3,5 情形及 LUW 一般下界；页面也明确提醒数据库状态不是文献完备性的证明。
- [Erdős Problems — LaTeX source for Problem 572](https://www.erdosproblems.com/latex/572) — Thomas F. Bloom (database editor), 2026-01-18; `problem_page`, `database_record`, directness=`direct`, reliability=`high`. 核对了输入陈述和备注的 LaTeX 版本，确认其未显式写出固定-k与常数依赖量词。
- [572 Discussion Thread](https://www.erdosproblems.com/forum/thread/572) — Alfaiz; LaiC; Erdős Problems forum users, 2026-05-31; `forum`, `informal_claim`, directness=`direct`, reliability=`medium`. 论坛未出现完整或部分解答声明；一条评论列出 Verstraëte、Pikhurko、Bukh–Jiang、He 的一般上界改进。其数学断言须以原论文核验，未据此认定下界问题已解决。
- [Cycles of even length in graphs](https://doi.org/10.1016/0095-8956(74)90052-5) — J. A. Bondy; M. Simonovits, 1974-04-01; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 给出一般偶圈 Turán 上界的经典来源；特别地，对固定 k 有 ex(n,C_{2k})=O_k(n^(1+1/k))。
- [Minimal Regular Graphs of Girths Eight and Twelve](https://doi.org/10.4153/CJM-1966-109-8) — Clark T. Benson, 1966-01-01; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 构造 girth 8 和 girth 12 的稠密正则图；结合边数与顶点数关系，提供本题 k=3 和 k=5 的匹配阶下界。
- [Polarities and 2k-cycle-free graphs](https://doi.org/10.1016/S0012-365X(99)90107-3) — Felix Lazebnik; Vasiliy A. Ustimenko; Andrew J. Woldar, 1999-01-01; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 提供极值偶圈问题的代数/极性构造和历史；该路线支撑条目所列的一般但较弱下界，并改进 C6 的常数。
- [A Note on the Turán Function of Even Cycles](https://doi.org/10.1090/S0002-9939-2012-11274-2) — Oleg Pikhurko, 2012-03-01; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 证明 ex(n,C_{2k}) <= (k-1)n^(1+1/k)+16(k-1)n，并明确记录当时匹配阶下界只知 k=3,5。
- [Extremal Numbers of Cycles Revisited](https://arxiv.org/abs/2011.11064) — David Conlon, 2021-02-18; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 给出 Wenger 构造的几何解释，并证明其在 k=2,3,5 时达到 n^(1+1/k) 阶；摘要称一般偶圈问题仅在 C4、C6、C10 合理理解。
- [New constructions and bounds for nonabelian Sidon sets with applications to Turán-type problems](https://doi.org/10.4153/S0008414X26102314) — John Byrne; Michael Tait, 2026-06-01; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 2026 年同行评审论文在引言中明确称：对无向图，ex(n,C_{2k})=O(n^(1+1/k))，而匹配下界只在 k=2,3,5 已知。这是本审计关于当前未解状态的最直接近时证据。
- [Two counterexamples to a conjecture about even cycles](https://arxiv.org/abs/2603.24515) — David Conlon; Eion Mulrenin; Cosmin Pohoata, 2026-03-25; `preprint`, `preprint`, directness=`indirect`, reliability=`high`. 近期相关工作：研究 Wenger C10-自由图中 C8-自由子图的稀疏性，且明确区分 Wenger 与广义六边形构造；不解决本题，但说明 C8/C10 构造路线仍活跃且须避免将相邻问题混同。

### 完成标准

- 肯定出口: A complete affirmative resolution proves that for every fixed integer k >= 4 with k != 5, there are c_k>0 and n_0(k) such that every n >= n_0(k) admits a finite simple C_{2k}-free graph with at least c_k n^{1+1/k} edges. Together with the established k=3,5 cases, this proves the canonical statement.
- 否定出口: A complete negative resolution proves, for at least one fixed integer k >= 3, that ex(n,C_{2k}) is not Omega(n^{1+1/k}); equivalently, ex(n,C_{2k})/n^{1+1/k} has no eventually positive lower bound. This must be a rigorous asymptotic upper obstruction, not failure of one construction family.

不构成完成：

- Proving only the already-known cases k=3 or k=5.
- Constructing graphs with a weaker exponent, or with the target number of edges only after allowing copies of C_{2k}.
- Giving a construction only on a sparse sequence of orders without a valid extension argument for all sufficiently large n.
- Proving a result for rainbow, induced, ordered, directed, bipartite-only, hypercube, or multiple-cycle variants without reducing it to ordinary C_{2k}-freeness.
- Finite computer searches without a general construction/certificate and asymptotic proof.

正确性陷阱：

- Check that every alleged cycle exclusion is for simple, ordinary copies of exactly C_{2k}; absence of short cycles is sufficient but not necessary.
- Keep k fixed before taking n to infinity; do not allow c_k or n_0(k) to depend on n.
- If a finite-field construction is used, verify vertex count, edge count, simplicity, distinctness of parameterized objects, and C_{2k}-freeness for every admissible field/order.
- If extending from special orders, prove that the extension preserves the normalized edge lower bound uniformly for every sufficiently large n.
- Do not transfer a theorem about ex(n,{C_3,...,C_{2k}}), ex^*(n,C_{2k}), z(n,C_{2k}), or ex(Q_d,C_{2k}) to ex(n,C_{2k}) without a valid implication.

### 更新后的 AI 可解答性

- 等级: `low_candidate`
- 分数: `8/100`
- 信心: `high`
- 结论: 这是定义明确但极难的长期构造型公开问题。AI 可协助提出、筛选和严格审计候选构造或局部引理，但目前证据不支持把一般解视为近期待办。

支持理由：

- 目标可精确形式化，且 k=3,5 的成功构造、一般下界和紧的指数上界给出了可审计的基准。
- 剩余缺口可在最小未解参数 k=4 上清晰呈现，允许证明优先的局部研究。
- 有限域和关联图构造有明确的边数与圈长度证书框架，适合逐步验证。

主要障碍：

- 几十年后一般 k 仍未突破；2026 文献仍仅承认 k=2,3,5 达到目标阶。
- 仅禁止一个精确偶圈比高围长要求宽得多，现有高围长构造没有自然推广到所需指数。
- 有限样本计算极易掩盖渐近失败；证明必须控制所有足够大的 n 和全部简单 C_{2k}。
- 常数、参数域、连通分支和从特殊阶到任意 n 的填充步骤都可能造成隐蔽失效。

Proof-first 路线：

- 先对任一候选代数/几何图给出可独立核对的“闭合游走到简单 C_{2k}”排除引理，再计算边数。
- 优先寻找能把已有高围长或精确圈规避构造提升为 C_{2k}-规避的结构性引理，而不是盲目枚举图。
- 对 k=4 建立可证伪的中间目标，例如某一显式族中 C8 的参数化分类或可删除边集的严格上界；只有该引理有停止条件时才允许计算。

需要验证：

- 任何声称新一般下界的文献应逐页核验其量词是否为所有固定 k、其图是否真的 C_{2k}-自由，以及是否覆盖所有充分大 n。
- 对 Benson/Wenger/广义多边形的引用应核对所禁圈的长度、顶点/边指数及从无穷子序列到渐近下界的转移。
- 在正式提交结论前，人工应复核 2026 Byrne–Tait 论文所述“only k=2,3,5”的上下文和可能的勘误。

### 审计限制与人工复核理由

- 本审计基于截至 2026-07-27 可公开访问的页面和文献元数据/全文片段；“未找到新解”不是逻辑上的不存在证明。
- 1966、1974、1999 原文的书目信息和相关结论均经出版页/数据库交叉核验，但未对每一页历史论文进行重新证明。
- 2026 Byrne–Tait 论文提供强而近时的状态交叉证据；其“only k=2,3,5”是该文背景陈述而非专门证明未解性的定理。
- 论坛已被检查，但其内容按网站规则属用户负责的非正式材料，未作为解决或下界定理的唯一证据。

- 无

<!-- DEEP_REVIEW:END -->
