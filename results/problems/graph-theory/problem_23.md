# Problem 23

## 基本信息

- 原始链接: https://www.erdosproblems.com/23
- LaTeX 页面: https://www.erdosproblems.com/latex/23
- 原始状态: `falsifiable`
- 奖金: `no`
- 主类别: `graph theory`
- 原始标签: `graph theory`
- 形式化状态: `yes`
- OEIS: `A389646`
- 原站备注字段: 无

## 原问题

Can every triangle-free graph on $5n$ vertices be made bipartite by deleting at most $n^2$ edges?

## AI 完成可能性判断

- 结论: **AI+计算/形式化工具有较高机会完成或显著推进**
- 等级: `high_candidate`
- 分数: `71/100`
- 建议路线: 优先做反例搜索和小规模枚举；若没有反例，不能据此断言问题为真。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 题面或备注出现有限对象/计算线索
- 已有形式化陈述，可降低语义误读风险
- 存在 OEIS 数据入口，利于实验与反例搜索

### 主要障碍

- 主要风险是候选证明或计算证书容易存在隐藏漏洞，需要独立复核。

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: graph theory
- 证明密集标签命中: 无
- 有限/计算线索: graph
- 渐近/无限线索: 无
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5 + tools`
- 结论: **中等候选。该题目标清晰、已形式化、可反例搜索，且已知上界与猜想常数只差约6.4%，因此 GPT-5.5 级别模型配合计算搜索、极值结构归约和形式化验证，有机会显著推进证明框架或验证有限子情形；但要完成锐常数 n^2 的一般证明仍很难，主要障碍是需要控制所有三角形-free图的全局结构，而不只是接近 C5 blow-up 的稳定情形。**
- 等级: `medium_candidate`
- 分数: `58/100`
- 信心: `medium`
- 可能路线: 可行路线是把问题表述为 triangle-free 图的最小奇割/最大二分子图缺边界问题，围绕 C5 blow-up 极值结构做稳定性分析；用计算搜索小规模或压缩后的候选极端图，寻找是否存在超过 n^2 删除代价的反例模板；对接近极值的结构建立分区和不等式证书；最后将有限约化、线性/半定规划证书或图不等式用形式化系统验证。更现实的成果是把 1.064n^2 的常数压低、验证一类结构、或给出可信的反例搜索阴性证据，而不是一次性完成完整定理。

### 支持理由

- 题目短且形式明确：triangle-free、5n 顶点、删除至二分图的边数上界，适合转化为最大割或 odd-cycle transversal in edges 的极值优化问题。
- JSON 标明 formalized=yes，说明至少存在可形式化表达或验证的基础版本；这提高了模型生成证明后被 proof assistant 或证书检查器审计的可能性。
- status=falsifiable 使计算反例搜索有实际价值：若猜想假，模型可通过小图搜索、 blow-up 模板、flag algebra/SDP 启发或整数规划发现候选。
- 备注给出 blow-up of C5 为紧例，说明极值形态有明确锚点；AI 可以围绕该结构尝试稳定性分解，而不是在完全无结构空间中搜索。
- 已知最好上界为 1.064n^2，距离目标常数较近，暗示已有方法可能留下可被自动化不等式优化、局部改进或证书化计算推进的余量。

### 主要障碍

- 锐常数问题通常对局部误差极敏感；从 1.064 降到 1 可能需要新的结构洞察，而不只是改进计算参数。
- triangle-free 图的全局结构非常多样，C5 blow-up 只是紧例；必须排除大量非接近五分结构的潜在极端配置。
- 如果证明依赖复杂稳定性分类、flag algebra 或大规模 case analysis，GPT-5.5 可能能生成候选证明，但很容易在边界条件、归一化常数和例外情形上出错。
- 形式化验证虽有帮助，但把现代极值图论证明完全形式化的成本可能接近或超过发现证明本身。
- 计算搜索只能给出有限规模或有限模板证据；若没有可证明的压缩/放大原理，阴性搜索不能验证一般 n。

### 需要的验证

- 复核形式化版本是否准确覆盖原题中的所有 n、所有 triangle-free simple graphs，以及“删除至二分图”的精确定义。
- 用独立程序做小 n 穷举或约束搜索，检查是否存在删除边数超过 n^2 的反例，并保存可复现证书。
- 若模型提出结构归约，需要验证归约没有默认正则性、连通性、最大度或均衡分区等未声明假设。
- 对任何常数改进证明，逐项检查不等式链，尤其是 5n 顶点归一化、n^2 缩放、取整误差和等号情形。
- 若使用 SDP、LP、SAT/ILP 或 flag algebra 证书，需要独立求解器复算，并最好生成可机器检查的有理证书。

### 公开版思考摘要

我只依据给定 JSON 判断：这是一个形式化、可反例化、目标常数明确的极值图论问题。它对 AI 工具友好的一面是可以转化为优化、搜索和证书验证任务，并且 C5 blow-up 给出清晰极值候选；困难的一面是一般 triangle-free 图结构复杂，锐界 n^2 可能需要新的稳定性或分类论证。因此我评为中等候选：很适合显著推进、验证子情形或寻找反例，但完整解决的概率不能评高。

### 免责声明

这不是该 Erdős 问题的解答，也不声称证明或反驳了命题；它只是对 GPT-5.5 级别模型在工具辅助下处理该单一问题的可行性评估。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `likely_open`
- 状态信心: `medium`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_23.md](../../prompts/problem_23.md)

### 状态结论

本题的精确全称命题很可能仍开放。Erdős Problems 当前页面仍列为“FALSIFIABLE Open”；2026 年 6 月的 Ferudun 预印本只证明了 5n 个顶点时 n≤40 的情形，并明确说明全体 n 的中等密度障碍仍未解决。未发现完整证明或反例；但近期预印本尚未经过同行评审，且无法由检索逻辑证明不存在未索引结果，故置信度定为 medium。

### 当前规范陈述

对每个正整数 n 和每个恰有 5n 个顶点的有限简单无向无三角形图 G，是否都存在 G 的生成二分子图 H，使得 |E(G)\E(H)|≤n²？等价地，令 β(G) 为使 G 成为二分图所需删除边数的最小值，则是否恒有 β(G)≤n²；又等价地，maxcut(G)≥e(G)−n²。

```text
For every positive integer n and every finite simple undirected triangle-free graph G with exactly 5n vertices, there exists a spanning bipartite subgraph H of G such that |E(G) \ E(H)| <= n^2. Equivalently, if beta(G) is the minimum number of edges deleted from G to obtain a bipartite graph, then beta(G) <= n^2; equivalently, maxcut(G) >= e(G)-n^2.
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 已检查标准极值构造 C5 的均匀 blow-up：五个大小均为 n 的独立集，只在循环相邻的类之间完全连接。它无三角形，并满足 β=n²，因此证明常数 1 若成立即为最优；它不是反例。未找到能反驳字面命题的简单构造。
- 版本变化: 未发现原命题被撤回或改写为非等价版本。其常见等价重述是任意 N 顶点无三角形图满足 β(G)≤N²/25；本题是 N=5n 的整除子序列。Ferudun（2026）新增 n≤40 的计算机辅助有限范围结果，而不是对原题的修订。Erdős（1992）提出了更广的奇圈围长版本；该版本不是本题的替代陈述。

陈述问题：

- 原句未显式说明图是有限、简单、无向图；这与题目来源、Erdős Problems 和 Lean 表述的标准约定一致。
- “made bipartite by deleting”必须是只删边、保留全部顶点；不能误作删点问题。
- n 的范围应为正整数。Lean 文件允许 n=0，但这只加入平凡边界例，未改变研究内容。
- 历史文献通常以总顶点数 N 陈述 β(G)≤N²/25；在 N=5n 时恰为本题的 n²，不能混淆两个 n。

需要固定的量词/约定：

- n is a positive integer.
- G is finite, simple, and undirected, with |V(G)|=5n exactly.
- Triangle-free means G contains no copy of K3.
- The retained graph is spanning: H has V(H)=V(G) and E(H) subseteq E(G).
- 'At most' includes equality.
- The maximum-cut formulation uses all bipartitions V(G)=A disjoint union B, with no balance condition.

### 文献与当前边界

已核验的主要结果：

- 将总顶点数记为 N，BCL（2021，预印本/EuroComb 扩展摘要）证明对每个 N 顶点无三角形图 β(G)≤N²/23.5；换回本题 N=5n，即 β(G)≤25n²/23.5≈1.064n²。
- BCL 还证明：对充分大的 N，若边密度 e(G)/binom(N,2)≤0.2486 或 ≥0.3197，则已得到精确 β(G)≤N²/25。该结论没有覆盖中间密度带。
- 均匀 C5 blow-up 满足 β=n²（在 N=5n 时），故本题若真则最优。
- Ferudun（arXiv:2606.28041，2026-06，未同行评审）声称使用 flag algebra 精确算术证书、图 blow-up 恒等式和整数性证明 a(5n)=n² 对全部 1≤n≤40；这是有限范围进展，并非全称解答。
- FormalConjectures 的 Lean 文件准确表达了原命题，但目标和若干变体皆为 `sorry`，因此不提供已验证证明。

最近相关工作：可直接检查的最新工作是 Ferudun 于 2026-06-26 提交的 arXiv:2606.28041。它的定理只覆盖 5,10,…,200 个顶点，并明确指出 n≥41 时其证书余量不足，故当前最相关的剩余问题不是已被该预印本关闭的有限情形。

剩余核心：证明或反驳：对所有 n≥41，每个 5n 顶点无三角形图都满足 β(G)≤n²。已有 BCL 尾部结果和 Ferudun 有限范围结果表明，任何潜在困难必须避开已处理范围；但除非独立核验证书及其有限/渐近转移，不能把这种定位误称为完整结构分类。

已使用方法：

- 最大割等价：β(G)=e(G)−maxcut(G)。
- BCL 使用 flag algebra 与密度分区，获得全局常数改进和两个精确密度尾部。
- Erdős–Győri–Simonovits 的工作涉及 pentagonlike 图与稳定性思想。
- Ferudun 的未审稿方法使用每根 MaxCut envelope、10 阶 flag-algebra 精确有理证书、blow-up 恒等式 β(G[t])=t²β(G) 和整数性；这些是可审计思路，不应在未复核前当作无条件背景定理。

争议或不确定性：

- Ferudun 的结果为单作者新预印本，虽有辅助文件并称可独立验证，但本审计未逐行运行证书或完成数学审稿；其 n≤40 结论应视为强但未同行评审的已声明结果。
- 题库页当前仍标开放，而其最近可见抓取时间早于/接近该预印本；两者不矛盾，因为预印本只给出部分结果。
- 论坛直接访问被拒，因而不能排除其含有未索引讨论，但也没有可用的论坛解答证据。

### 证据来源

- [Erdős Problems — Problem 23](https://www.erdosproblems.com/23) — Thomas Bloom / Erdős Problems contributors, date unknown; `problem_page`, `database_record`, directness=`direct`, reliability=`high`. 页面当前将问题标作 FALSIFIABLE、Open，并记录 C5 blow-up 的锐性及 BCL 的 1.064n² 界。该状态是数据库编辑判断，不是证明。
- [Erdős Problems — LaTeX for Problem 23](https://www.erdosproblems.com/latex/23) — Thomas Bloom / Erdős Problems contributors, date unknown; `problem_page`, `database_record`, directness=`direct`, reliability=`high`. 提供输入题面、备注和书目的可解析版本；用于核对原始转录。
- [Erdős Problems — Problem 23 discussion thread](https://www.erdosproblems.com/forum/thread/23) — Erdős Problems forum contributors, date unknown; `forum`, `informal_claim`, directness=`indirect`, reliability=`low`. 论坛线程被搜索索引定位，但直接访问受 403 限制；本审计未从中取得可审查的证明或反例，故未将任何论坛信息视为解决证据。
- [Max Cuts in Triangle-free Graphs](https://arxiv.org/abs/2103.14179) — József Balogh, Felix Christian Clemen, Bernard Lidický, 2021-03-25; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 摘要和正文将 β(G)≤N²/25 明确称为 Erdős 猜想；证明全局 β(G)≤N²/23.5，并证明精确界在两个密度尾部成立（大 N、边密度至多 0.2486 或至少 0.3197）。
- [The Erdos n^2/25 max-cut conjecture for small multiples of five, via a per-root-MaxCut envelope and blow-up integrality](https://arxiv.org/abs/2606.28041) — Alper Ferudun, 2026-06-26; `preprint`, `preprint`, directness=`direct`, reliability=`medium`. 声称并给出带辅助精确算术证书的结果 a(5n)=n²（1≤n≤40）；同时明确说全 n 猜想未解决，指出中等密度带和其证书误差为障碍。该预印本没有同行评审，完整正确性仍需独立审计。
- [OEIS A389646 — Maximum number of edges that need to be removed from a triangle-free graph on n vertices to make it bipartite](https://oeis.org/A389646) — Elijah Beregovsky and OEIS contributors, date unknown; `oeis`, `database_record`, directness=`indirect`, reliability=`medium`. 将 a(N) 定义为该最大删边数，列出 BCL 上界，并在 2026-07 的更新中记录 Ferudun 的 a(5k)=k²（k≤40）声称及其 arXiv 链接。
- [FormalConjectures — Erdős Problem 23 Lean statement](https://raw.githubusercontent.com/google-deepmind/formal-conjectures/main/FormalConjectures/ErdosProblems/23.lean) — Formal Conjectures contributors, 2026; `formalization`, `formalized_artifact`, directness=`direct`, reliability=`high`. 精确形式化了全称目标，并把它标记为 research open；文件中的相关定理均以 `sorry` 结束，故这是陈述形式化而非机器核验的完整证明。
- [How to Make a Graph Bipartite](https://combinatorica.hu/~p_erdos/1988-12.pdf) — Paul Erdős, Ralph Faudree, János Pach, Joel Spencer, 1988-08; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 原始相关论文，书目信息为 Journal of Combinatorial Theory, Series B 45, 86–98；提供早期删边二分化背景。
- [How Many Edges Should Be Deleted to Make a Triangle-Free Graph Bipartite?](https://korandi.org/docs/misc/erdos_gyori_simonovits.pdf) — Paul Erdős, Ervin Győri, Miklós Simonovits, 1992; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 早期工作研究此删边问题与 pentagonlike 结构/稳定性；历史问题页将其归为高边数范围的结果来源。

### 完成标准

- 肯定出口: Prove that for every positive integer n and every finite simple triangle-free graph G on exactly 5n vertices, beta(G)<=n^2; equivalently, construct or prove the existence of a cut of G with at least e(G)-n^2 crossing edges. The proof must cover n>=41 as well as the already claimed finite range, unless it rigorously imports independently verified finite-range results.
- 否定出口: Give an explicit positive integer n and a finite simple triangle-free graph G on 5n vertices with beta(G)>n^2, together with a proof that every bipartite spanning subgraph omits more than n^2 edges (equivalently maxcut(G)<e(G)-n^2).

不构成完成：

- An improvement of 1.064n^2 that still has any constant strictly larger than 1.
- A result only in a density range, only asymptotically with a positive error, or only for n<=M without a theorem covering all remaining n.
- Rechecking that the balanced C5 blow-up has beta=n^2: that establishes sharpness, not the universal upper bound.
- A finite search without a proved reduction of all possible counterexamples to its finite input family.
- A flag-algebra numerical output without an exact certificate and a proof connecting its normalization to the finite graph claim.

正确性陷阱：

- Keep N (the total vertex count) distinct from n=N/5; N^2/25=n^2 only when N=5n.
- A bipartite retained subgraph must be spanning; vertex deletion is irrelevant.
- Check the conversion beta(G)=e(G)-maxcut(G) and count all uncut edges, including those within both sides of a partition.
- Verify triangle-freeness and exact order 5n for any construction.
- Do not use an asymptotic density-tail theorem at a finite boundary without a justified blow-up/limit argument.
- For a computer-assisted proof, audit the stated flag identities, PSD/rational certificates, graphon-to-finite transfer, integrality step, and every strict versus non-strict density endpoint.
- Do not assume C5-blow-up stability or uniqueness without proof.

### 更新后的 AI 可解答性

- 等级: `low_to_medium_candidate`
- 分数: `25/100`
- 信心: `medium`
- 结论: 目标严谨、可证伪且已有可审计的中间结构，适合证明优先的研究代理；但精确常数已长期抵抗现有极值方法，最新计算机辅助结果也只覆盖 n≤40，因此完整解决的短期概率偏低。

支持理由：

- 命题可准确写成最大割不等式，正反两类证书都明确。
- 已有全局 1.064 常数、精确密度尾部和有限 n≤40 进展，能把探索聚焦于具体缺口。
- flag-algebra、稳定性和最小反例路线可拆为可独立审计的引理。

主要障碍：

- 必须消除固定常数余量并处理全体 n，而非取得渐近近似。
- 中等密度图的结构未被完整刻画；C5 blow-up 的极值直觉并非分类定理。
- 有限计算和图论枚举不能自行外推到任意 n。
- 最新有限范围进展依赖大型计算机辅助证书，复现与验证本身成本高。

Proof-first 路线：

- 先独立审计 BCL 的精确尾部定理以及 Ferudun 证书的 soundness，明确哪些结论可安全复用。
- 在最小反例框架下尝试建立可归约配置或加强命题，注意维持 5n 的整除归一化。
- 尝试量化稳定性：若 β(G) 接近 n²，则 G 是否必须接近可控的 pentagonlike/C5-blow-up 结构；随后在该结构邻域构造精确割。
- 从局部最优最大割条件导出对同侧边的严格计数不等式，目标必须恰达 n²。

需要验证：

- 运行并审计 arXiv:2606.28041 所列精确有理证书与源代码；确认其 graphon envelope 和 blow-up/integrality 转移无缺口。
- 核验 BCL 结果的最终公开版本、定理假设和密度归一化。
- 在人类可访问的 MathSciNet、zbMATH、arXiv 引用/更新网络中做一次 2026-06-26 后的最终追踪。
- 将 FormalConjectures 文件中的 `sorry` 状态与项目构建规则核对，避免误读为已验证定理。

### 审计限制与人工复核理由

- Erdős Problems 主页面和论坛直接访问均受到 403 限制；题面和状态主要通过搜索索引及公开仓库交叉核对。
- Ferudun 2026 预印本的辅助文件虽公开列出，本审计没有下载、运行或逐步审查其大型精确算术证书，故只确认其声明范围，不把其数学正确性升级为已独立验证事实。
- 未找到 BCL 预印本以外可独立确认的同行评审完整版本；本审计不声称存在或不存在后续期刊版。
- 开放状态是基于截至 2026-07-27 的定向公开搜索；未索引论文、私人通讯或付费数据库中遗漏的结果仍可能存在。

- 在启动高成本研究前，应由图论专家/形式化审计者运行并检查 Ferudun 的证书，特别是 envelope soundness、flag-algebra PSD、图极限到有限图的转移和整数性步骤。
- 应通过 MathSciNet、zbMATH、Crossref 和 arXiv 更新/引文网络做一次 2026-06-26 后的最终文献追踪。
- 应人工核对 BCL 的发表状态、精确密度归一化及“充分大 N”如何用于任何有限 N 推断。
- 应确认 FormalConjectures 构建规则下 `sorry` 的含义；从所检文件看它是陈述形式化而非已核验定理。

<!-- DEEP_REVIEW:END -->
