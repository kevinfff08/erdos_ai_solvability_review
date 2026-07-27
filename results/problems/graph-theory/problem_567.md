# Problem 567

## 基本信息

- 原始链接: https://www.erdosproblems.com/567
- LaTeX 页面: https://www.erdosproblems.com/latex/567
- 原始状态: `open`
- 奖金: `no`
- 主类别: `graph theory`
- 原始标签: `graph theory`, `ramsey theory`
- 形式化状态: `yes`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

Let $G$ be either $Q_3$ or $K_{3,3}$ or $H_5$ (the last formed by adding two vertex-disjoint chords to $C_5$). Is it true that, if $H$ has $m$ edges and no isolated vertices, then\[R(G,H)\ll m?\]

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

### 主要障碍

- 题面含渐近/无限对象线索：\gg, \ll, o(

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: graph theory, ramsey theory
- 证明密集标签命中: 无
- 有限/计算线索: graph, ramsey
- 渐近/无限线索: \gg, \ll, o(
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **中等候选：GPT-5.5 级别模型不太可能直接完整解决整个开放问题，但有现实机会显著推进若干子情形，尤其是围绕 H_5 的已知部分结果边界、对任意 H 的结构分解、以及小固定图 G 的计算化反例搜索和证明验证。**
- 等级: `medium_candidate`
- 分数: `55/100`
- 信心: `medium`
- 可能路线: 可行路线不是直接“猜出”统一证明，而是把问题拆成三个固定目标图 G=Q_3、K_{3,3}、H_5；对任意 m 边无孤立点图 H，尝试证明任意足够大的宿主图在红蓝染色中要么含红 G，要么含蓝 H。模型可配合工具做三类工作：一是形式化已有 Ramsey-size-linear 证明模板，检查能否迁移到 H_5 或 K_{3,3}；二是用图分解、稀疏正则性、依赖随机选择、嵌入引理等工具寻找足够条件；三是用 SAT/ILP/Lean 或 graph generation 对小 m、特殊 H 类和潜在极端构造做反例搜索与常数估计。

### 支持理由

- 问题的目标图 G 都是固定小图，且命题只要求线性上界 R(G,H) << m；这类问题通常适合把复杂度集中在固定禁图的红色结构分析和蓝色 H 的通用嵌入条件上。
- Problem JSON 明确说明 H_5 已有强相关部分进展：对 bipartite H 已知线性，且较大 K_4 subdivision 已知 Ramsey size linear；这给工具辅助模型提供了可复用证明模板和明确缺口。
- 问题已 formalized，这提高了模型使用形式化证明检查、局部引理验证和机器可审计推导的可行性。
- 反例搜索空间虽然总体巨大，但固定 G、小 m、特定 H 家族、极端稀疏/高最大度 H 可以用 SAT 或约束求解辅助排查，有助于发现错误猜想或证明所需的额外结构。

### 主要障碍

- H 是任意 m 边无孤立点图，而不是限制为二分图、低最大度图或稀疏可控族；统一处理任意 H 的蓝色嵌入是核心难点。
- K_{3,3} 和 Q_3 的红色避让结构可能仍然足够复杂，难以从局部密度或简单退化性条件推出所需蓝色全图嵌入。
- 已有备注表明 H_5 的某些接近情形已被解决但本问题仍 open，说明缺口可能不是简单套用已知 subdivision 或 bipartite-H 技术。
- 线性 Ramsey 上界通常需要强而精细的结构定理；模型可能产生貌似合理但在高最大度 H、非二分 H 或极端组件结构上失效的证明。

### 需要的验证

- 对每个 G 分别验证：Q_3、K_{3,3}、H_5 不能被一个未声明的通用定理误覆盖。
- 若模型提出证明，必须检查所有常数只依赖于固定 G，而不依赖于 H 的顶点数、最大度或组件数。
- 需要对非二分 H、高度不均匀 H、含大 clique 或密集小块的 H 做专门边界测试。
- 需要用形式化证明或至少严格同行级推导验证关键嵌入引理、红色禁图结构引理和归纳/分解步骤。
- 需要进行小规模 Ramsey 染色 SAT/ILP 搜索，寻找可能破坏候选证明的临界例子。

### 公开版思考摘要

该问题不是计算型小题，而是一个开放的图 Ramsey 线性上界问题。GPT-5.5 级别模型最有价值的作用在于组织和迁移已有证明技术、发现可验证的中间引理、自动搜索反例和形式化检查局部证明。由于 Problem JSON 已显示 H_5 有接近结果但完整情形仍未解决，直接完成整题的概率不高；不过固定目标图很小、已有 formalization、且存在强相关部分结果，因此它不是低价值候选。整体判断为中等候选：更可能显著推进或验证子情形，而不是一次性解决全部命题。

### 免责声明

以上只是对 GPT-5.5 配合工具推进该 Erdős problem 的可行性评估，不是该问题的数学证明，也不声称 R(G,H) << m 已被证明。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `likely_open`
- 状态信心: `medium`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_567.md](../../prompts/problem_567.md)

### 状态结论

截至 2026-07-27，未找到对 Q_3、K_{3,3} 或 H_5 任一完整结论的论文、预印本或可检验反例。Erdős Problems 页面于 2026-01-18 仍标为 OPEN，论坛页也未显示解答或部分解答声明。Bradač–Gishboliner–Sudakov 的已发表工作明确只给出 H_5 对所有二分图 H 的线性界，并称不能给出 H_5 的肯定答案；因此三部分原问题仍很可能开放。该判断不是“未检索到即证明不存在”的逻辑证明，故置信度为中等。

### 当前规范陈述

令 r(A,B) 为最小的 N，使得完全图 K_N 的每个红蓝边染色都含有一个红色 A 或一个蓝色 B。对每个固定图 G∈{Q_3,K_{3,3},H_5}，其中 Q_3 是三维立方体图，H_5 是在 C_5 上加入两条顶点不交弦所得的图（等价地，K_4 的一条边恰好细分一次），问是否存在仅依赖于 G 的常数 C_G>0，使得对每个有限简单图 H，若 m=e(H)≥1 且 H 无孤立点，则 r(G,H)≤C_Gm。等价地，问这三个固定图是否各自都是 Ramsey size-linear。原句中的“either”应理解为三个分别提出、合取的断言；因候选图只有有限三个，要求同一常数与分别常数等价。

```text
Let r(A,B) be the least integer N such that every red/blue colouring of E(K_N) contains a red copy of A or a blue copy of B. For each fixed graph G in {Q_3, K_{3,3}, H_5}, where Q_3 is the 3-dimensional cube and H_5 is obtained from C_5 by adding two vertex-disjoint chords (equivalently, K_4 with one edge subdivided once), determine whether there exists a constant C_G>0 such that, for every finite simple graph H with m=e(H)>=1 edges and no isolated vertices, r(G,H)<=C_G m. The constant may depend on the fixed G but not on H or m. Equivalently, each of the three fixed graphs is Ramsey size-linear. The displayed question is naturally a conjunction of these three separate assertions; because the set has three fixed members, allowing one common constant would be equivalent after taking a maximum.
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 未发现可推翻规范化正整数 m 版本的简单构造。m=0 的空图仅是原文未明说的边界约定，不能作为文献中意图明确的 Ramsey size-linear 问题之实质反例。已知的非线性充分条件 e(G)≥2v(G)−2 不适用于 Q_3、K_{3,3}、H_5；已知连通图的充分条件 e(G)≤v(G)+1 也不覆盖它们。
- 版本变化: 1993 年 EFRS 提出 Ramsey size-linear 概念及这些具体边界案例；1995 年 Erdős 又特别重申 K_{3,3} 情形。BGS 的 2024 年已发表论文没有解决 H_5，而证明了 H_5 对二分图右侧 H 的线性界，并证明除 H_5 外、顶点数至少 6 的 K_4 细分均 Ramsey size-linear。因此这是严格的部分推进而不是对原目标的修订或解决。

陈述问题：

- R(G,H) 必须解释为通常的顶点 Ramsey 数，而非 size-Ramsey 数 \hat r(G,H)；原数据库页面和原始问题页面的定义性语境均支持前者。
- 渐近记号 \ll 隐含常数只可依赖固定的左侧图 G，不能依赖 H 或 m；必须显式量化。
- 若字面允许 m=0，则“无孤立点”的空图边界会使线性不等式的通常表述失去意义；相关文献的标准用法隐含 m≥1，故规范陈述加入此条件。
- 形式化仓库的说明性注释把显示公式误写为 \hat r(G,H)\ll m，但其三个实际声明均为 IsRamseySizeLinear，且均含 sorry；这既不是证明，也不应改变原问题的普通 Ramsey 数解释。

需要固定的量词/约定：

- The assertion is universal over the three listed fixed graphs, or equivalently three separately quantified fixed-G assertions.
- For each fixed G, there must be C_G>0 such that for every finite simple H with e(H)=m>=1 and no isolated vertices, r(G,H)<=C_G m.
- r(G,H) is the ordinary two-colour vertex Ramsey number on K_N, not the size-Ramsey number \hat r(G,H).
- Copies are non-induced subgraph copies; the two colours are ordered only to distinguish the G-side from the H-side.

### 文献与当前边界

已核验的主要结果：

- EFRS（1993，同行评审）定义 Ramsey size-linear；证明若 e(G)≥2v(G)−2 则 G 非 Ramsey size-linear，若 G 连通且 e(G)≤v(G)+1 则 G 是 Ramsey size-linear。三目标均处在这些一般界之间，故未被该判据覆盖。
- Erdős（1995，同行评审问题集）特别提出 K_{3,3} 情形；当前问题也保留 Q_3 和 H_5 两个具体边界案例。
- Bradač、Gishboliner、Sudakov（2024，同行评审）证明：每个至少 6 顶点的 K_4 细分图均 Ramsey size-linear；H_5 是唯一的 5 顶点例外。对 H_5，他们证明所有无孤立点二分图 H 满足 r(H_5,H)=O(e(H))，但没有解决任意 H。
- Wigderson（2025，同行评审）构造性地证明存在无穷多个极小非 Ramsey size-linear 图；该成果显示一般分类仍复杂，但不为本题任一 G 给出肯定或否定结论。

最近相关工作：Hng、Ji、Lamaison 的预印本（arXiv:2603.25453，2026-03-26）在相同“按右侧图边数线性控制 ordinary Ramsey number”的框架中推进了所有固定奇圈的结果。它是本次检索到的最新直接同主题工作，但目标是奇圈而非 Q_3、K_{3,3}、H_5，不能作为本题解答。

剩余核心：分别证明或反驳 Q_3、K_{3,3}、H_5 对所有无孤立点有限图 H 都满足 r(G,H)=O_G(e(H))。其中 H_5 的非二分图右侧情形是 BGS 已明确留下的缺口；本次检索亦未发现 Q_3 或 K_{3,3} 的关闭结论。

已使用方法：

- EFRS/后续工作中的概率法与 Lovász 局部引理型下界，用于给出密度过高时非线性的障碍。
- BGS 对 H_5 和 K_4 细分使用平均法、凸性、嵌入引理及 dependent random choice。
- 近期奇圈工作使用按右侧图最小度递归删除、红色邻域计数、路径/圈 Ramsey 界和双计数；它仅提供可比较的思路，不能直接移植成对三目标的证明。

争议或不确定性：

- Erdős Problems 自身声明 OPEN 仅反映维护者当前判断；因而本审计采用 likely_open 而非由数据库标签单独“确认”开放。
- 形式化文件注释中的 \hat r 与普通 r 不一致，但声明名 IsRamseySizeLinear 和原始/同行评审文献均支持普通 vertex Ramsey number；需在后续工作中避免混用两种 Ramsey 参数。
- 未找到 2026-07-27 以后不适用的资料；本结论仍应在正式开题前再做一次作者主页、arXiv 和 MathSciNet/zbMATH 引文更新检索。

### 证据来源

- [Erdős Problem #567](https://www.erdosproblems.com/567) — Thomas F. Bloom (database editor), 2026-01-18; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 数据库当前将问题标为 OPEN，给出三图陈述，记录 BGS 的 H_5 二分图右侧部分结果，并声明评论中没有解答或部分解答主张。页面也明确提醒其开放标签不是完备文献检索的证明。
- [Erdős Problem #567 - Discussion thread](https://www.erdosproblems.com/forum/discuss/567) — Erdős Problems forum, date unknown; `forum`, `informal_claim`, directness=`direct`, reliability=`medium`. 论坛检索结果重复当前开放状态并未显示任何完整或部分解答主张；这是对缺少论坛解答的有限证据，不是数学证明。
- [Ramsey Size Linear Graphs](https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/abs/ramsey-size-linear-graphs/2F50FFB56AD4E42EFA80DA5B280225A0) — Paul Erdős, R. J. Faudree, C. C. Rousseau, R. H. Schelp, 1993; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 原始论文定义 Ramsey size-linear 为对所有无孤立点、n 条边的 H 有 r(G,H)≤Cn；摘要给出 e(G)≥2v(G)−2 时非线性、连通且 e(G)≤v(G)+1 时线性的边界结果。
- [Some of my Favourite Problems in Number Theory, Combinatorics, and Geometry](https://revistas.usp.br/resenhasimeusp/pt_BR/article/view/74798) — Paul Erdős, 1995-05-10; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 这是数据库所引 Erdős 1995 原始问题集的出版记录；数据库据此指出 Erdős 特别提到 K_{3,3} 情形。
- [On Ramsey Size-Linear Graphs and Related Questions](https://epubs.siam.org/doi/10.1137/22M1481713) — Domagoj Bradač, Lior Gishboliner, Benny Sudakov, 2024-01-09; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 证明每个至少 6 个顶点的 K_4 细分图满足 R(S,F)=O(v(F)+e(F))；对例外 H_5=K_4^* 只证明任意无孤立点二分图 F 有 R(H_5,F)=O(e(F))，并明确说不能给出其 Ramsey size-linear 的肯定答案。
- [On Ramsey size-linear graphs and related questions](https://arxiv.org/abs/2202.10388) — Domagoj Bradač, Lior Gishboliner, Benny Sudakov, 2023-03-10; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 可公开核验的预印本全文给出 H_5 的精确例外地位、二分图右侧定理及方法说明（平均法、凸性和 dependent random choice）。该版本对应后来的同行评审论文。
- [Ramsey size linear and generalization](https://arxiv.org/abs/2603.25453) — Eng Keat Hng, Meng Ji, Ander Lamaison, 2026-03-26; `preprint`, `preprint`, directness=`indirect`, reliability=`medium`. 近期预印本推进了奇圈对任意给定边数图的线性 Ramsey 上界，并讨论 EFRS 的一般框架；文中没有声称解决 Q_3、K_{3,3} 或 H_5。
- [Infinitely many minimally non-Ramsey size-linear graphs](https://doi.org/10.1016/j.ejc.2025.104175) — Yuval Wigderson, 2025-05-10; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 给出 Ramsey size-linear 的标准量化定义，重述 EFRS 的密度型非线性判据，并解决了“无穷多个极小非线性图”的不同问题；不解决本题三图。
- [FormalConjectures: Erdős Problem 567](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/567.lean) — Formal Conjectures Authors, date unknown; `formalization`, `formalized_artifact`, directness=`direct`, reliability=`high`. 文件将 Q_3、K_{3,3}、H_5 分成三个 IsRamseySizeLinear 声明，但全部以 sorry 占位；说明性公式误用 \hat r。因此它是未证明的陈述形式化，不是状态关闭的证据。

### 完成标准

- 肯定出口: For each G in {Q_3,K_{3,3},H_5}, prove an explicit theorem: there is a finite constant C_G such that every finite simple graph H with e(H)=m>=1 and no isolated vertices satisfies r(G,H)<=C_G m. A proof must handle arbitrary (including non-bipartite and disconnected) H; for H_5 it must strictly extend the already known bipartite-H theorem.
- 否定出口: Disprove the conjunction by exhibiting at least one specified G in the set and an infinite family (H_i) of finite simple graphs without isolated vertices, with e(H_i)->infinity and r(G,H_i)/e(H_i)->infinity, together with a valid lower-bound proof. A single counterexample G and family refutes the literal three-part assertion.

不构成完成：

- A proof only for H=K_n, only for connected H, bounded-degree H, or only bipartite H; the latter is already known for G=H_5.
- A proof for subdivisions of K_4 having at least six vertices; H_5 has five vertices and is expressly the exception in BGS.
- A finite computational check over H up to a bounded number of vertices or edges.
- A bound whose hidden constant depends on H, m, |V(H)| independently of m, or an unproved external Ramsey estimate.
- A proof about the size-Ramsey number \hat r(G,H) rather than the ordinary vertex Ramsey number r(G,H).

正确性陷阱：

- Verify the parameter is r(G,H), defined through colourings of K_N, not \hat r(G,H).
- Keep colour roles and graph roles consistent: the red graph must contain the fixed G or the blue graph the varying H.
- Quantify C_G before H and independently of m; treating the three fixed G separately is valid, but a result for one does not prove the other two.
- Check that any reduction preserves the condition 'no isolated vertices' and covers m>=1, disconnected H, and non-bipartite H.
- Do not apply BGS Theorem 4 to H_5: its five vertices make it the stated exception.
- For a claimed lower bound, show an unbounded ratio r(G,H_i)/e(H_i), not merely a large constant or a lower bound linear in e(H_i).

### 更新后的 AI 可解答性

- 等级: `low_candidate`
- 分数: `20/100`
- 信心: `medium`
- 结论: 这是定义清楚且可证伪的开放研究目标，但三十余年未解、现有一般分类无法覆盖三图，适合作为长期证明研究而非短期 AI 自动求解候选。

支持理由：

- 目标具有精确的全称量词和清晰的肯定/否定证书，且三个固定左侧图允许按部件分解探索。
- 已有 BGS 的 H_5 二分图右侧定理和 K_4 细分方法提供具体可审计的起点，而非完全无文献的猜想。
- 否定方向有明确的无限族和超线性比值完成标准。

主要障碍：

- 必须处理任意无孤立点 H；H_5 的已知二分图结果不能覆盖非二分图 H。
- Q_3、K_{3,3}、H_5 都绕开 EFRS 的简单充分/必要密度界，显示其正处于难的中间区。
- 任何有限搜索都不能建立所需的统一常数或无限反例族；易发生 ordinary Ramsey number 与 size-Ramsey number 混淆。

Proof-first 路线：

- 先将任意 H 的一个结构性分解或嵌入归约化为少数可验证情形；只有在该引理精确说明如何保留无孤立点和线性损失后，才尝试延伸 BGS 的平均/DRC 框架。
- 把 H_5 的“右侧二分图”证明逐项定位为对一般 H 失败的唯一步骤，并寻求只针对该障碍的替代引理。
- 对三个 G 独立研究：寻找能把红色无 G 条件转化为足够强蓝色嵌入性质的定量引理；不得把对 K_n 的界误当作边数线性结论。

需要验证：

- 在投入研究前重新检查 2026-03-26 之后的 arXiv、作者主页及引用数据库，特别检索三种图名与 Ramsey size-linear 的组合。
- 逐页核验 BGS 的 Theorem 3、Theorem 4 及其假设，确认 H_5 的二分图限制和“至少 6 顶点”限制。
- 若采用 FormalConjectures 文件，应核验 IsRamseySizeLinear 的库定义，并修正其文档中 \hat r 的记号错误；其中 sorry 不可用作任何证明。

### 审计限制与人工复核理由

- 本审计使用了定向公共网页、期刊页、arXiv、作者相关页面、问题页、论坛检索和形式化仓库；未获得所有付费数据库或所有 2026 年未来索引的穷尽检索权限，因此“likely_open”不是开放性的逻辑证明。
- EFRS 原文全文未在本次可浏览来源中逐页检查；其定义和两条一般结果由期刊摘要、BGS 和 Wigderson 的可检查叙述交叉支持。
- 论坛直接打开受访问限制，结论关于论坛仅依赖该问题页和搜索索引所显示的“无解答/无部分解答”信息。
- 形式化仓库可证明其存在声明文件及 sorry，但本审计没有运行 Lean；其作用仅是记录陈述形式化和记号瑕疵，绝不认证数学结论。

- 应由领域专家确认是否有 2026-03-26 至 2026-07-27 间未被公共搜索索引收录的预印本、讲义或已接收论文解决任一具体图。
- 若后续研究依赖原始 EFRS 的具体定理编号、常数或所有中间边界情形，应取得并逐页核查原文。
- 应人工核验 FormalConjectures 库中 IsRamseySizeLinear 的精确定义，并将文档中 \hat r 的误记与普通 r 的规范目标隔离。

<!-- DEEP_REVIEW:END -->
