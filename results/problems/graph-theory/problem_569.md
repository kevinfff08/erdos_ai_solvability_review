# Problem 569

## 基本信息

- 原始链接: https://www.erdosproblems.com/569
- LaTeX 页面: https://www.erdosproblems.com/latex/569
- 原始状态: `open`
- 奖金: `no`
- 主类别: `graph theory`
- 原始标签: `graph theory`, `ramsey theory`
- 形式化状态: `no`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

Let $k\geq 1$. What is the best possible $c_k$ such that\[R(C_{2k+1},H)\leq c_k m\]for any graph $H$ on $m$ edges without isolated vertices?

## AI 完成可能性判断

- 结论: **AI 可能做出局部推进或搜索反例，但完整解决把握不足**
- 等级: `low_to_medium_candidate`
- 分数: `44/100`
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

- 计算/组合标签命中: graph theory, ramsey theory
- 证明密集标签命中: 无
- 有限/计算线索: graph, ramsey
- 渐近/无限线索: 无
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **不太可能在一次研究周期内完整解决“最佳常数”问题，但有现实机会显著推进：例如整理已知固定奇圈对稀疏图的线性 Ramsey 上界、构造或验证候选下界族、对小 k 或受限 H 做计算实验，并把某些归纳或极值引理形式化检查。**
- 等级: `low_to_medium_candidate`
- 分数: `45/100`
- 信心: `medium`
- 可能路线: 较可行的路线是把问题拆成上下界两部分：先对固定 k 建立候选常数 c_k 的下界构造，例如让 H 取星、匹配、路径、二部稀疏图或高最小度稀疏图族；再尝试用 Ramsey 理论中的最小度归纳、奇圈禁图结构、边数参数化分解、随机/伪随机构造搜索和小规模 SAT/ILP 反例搜索来逼近上界。GPT-5.5 级模型更适合做文献定位、证明草图拆解、候选极值图生成、有限情形验证和形式化辅助，而不是直接产出最终最优 c_k 的完整新证明。

### 支持理由

- 问题表述短且对象清楚：固定奇圈 C_{2k+1} 与任意无孤立点 m 边图 H，目标是线性 Ramsey 常数，这有利于工具化拆解。
- 参数 m 是边数而非顶点数，且 H 无孤立点，可能允许用稀疏图分解、退化度、匹配/星分解或归纳删除边等方法建立统一线性上界。
- 下界方面可以系统枚举或构造 H，并用 Ramsey 图搜索验证小 k、小 m 的候选极值行为，这类任务适合计算辅助。
- 若已有相关固定图对稀疏图 Ramsey 上界，模型可通过文献检索整合现有引理并尝试把常数追踪到显式形式。

### 主要障碍

- 题目要求“best possible c_k”，不是只要某个线性上界；精确最优常数通常需要匹配的全局上界和极值构造。
- H 是任意无孤立点图，结构范围很宽，最坏情形可能不来自简单族，反例搜索难以覆盖无限图类。
- 奇圈 Ramsey 问题通常对宿主图的二部结构、色类密度和局部扩张很敏感，常数优化可能需要精细稳定性分析。
- 目前 JSON 标明 open 且未形式化，说明没有现成形式证明骨架可直接复用，AI 生成的新证明需要非常严格的人工审计。

### 需要的验证

- 检索并核对固定 C_{2k+1} 对 m 边图的现有 Ramsey 上界、下界和是否已有针对特定 k 的精确结果。
- 对小 k，尤其 k=1 和 k=2，进行穷举、SAT/ILP 或 Ramsey 图搜索，检查候选 c_k 是否被简单 H 族达到。
- 把任何声称的上界证明拆成可验证引理，逐项检查常数损失、归纳基、无孤立点条件的使用和最坏 H 的覆盖性。
- 对候选下界构造验证两点：构造图确实无红 C_{2k+1}，且其蓝补图确实不含目标 H；需要随 m 参数化成立。

### 公开版思考摘要

这是一个适合 AI 做“推进型研究”的问题，而不是高概率一击解决的问题。它有明确参数和可计算的小规模实例，模型可以结合搜索与文献把候选常数范围收紧，并验证部分结构性猜想。但“最佳可能 c_k”要求全图类精确极值，证明难度集中在常数级最优性与无限族覆盖上，因此完整解决概率偏低。

### 免责声明

以上是 AI 可解性与研究推进潜力评估，不是该 Erdős 问题的解答，也不声称给出了最佳常数 c_k。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `solved`
- 状态信心: `medium`
- 可行动性: `closed_verification_only`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_569.md](../../prompts/problem_569.md)

### 状态结论

字面问题已被 2026 年 Cambie 与 Freschi 的公开预印本解决。其定理对任意整数 t≥3 与任意无孤立点、m≥1 条边的图 H 给出 R(C_t,H)≤(t−1)m+1≤tm。代入 t=2k+1 得 R(C_{2k+1},H)≤(2k+1)m；取 H=K_2（m=1）时 R(C_{2k+1},K_2)=2k+1，故最优常数恰为 c_k=2k+1。Erdős Problems 页面仍标为 open，但其最后编辑于该预印本之前，属数据库滞后。

### 当前规范陈述

对每个整数 k≥1，令 c_k 为满足下述条件的最小实常数 c：对每个有限简单图 H，若 e(H)=m≥1 且 H 无孤立点，则 R(C_{2k+1},H)≤cm。其中 C_s 是 s 个顶点的简单环，R(F,H) 是使得 K_N 的每个红蓝边染色均含红色 F 或蓝色 H 的最小 N。精确答案为 c_k=2k+1。

```text
For every integer k>=1, let c_k be the least real constant c such that, for every finite simple graph H with e(H)=m>=1 and no isolated vertices, R(C_{2k+1},H)<=cm. Here C_s is the simple cycle on s vertices, and R(F,H) is the least N such that every red-blue colouring of E(K_N) contains a red copy of F or a blue copy of H. The exact answer is c_k=2k+1.
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 这不是一个待判真假的断言而是求最优常数的问题，未发现会使规范陈述失效的简单反例。相反，H=K_2 是决定性边界例：m=1 时 R(C_{2k+1},K_2)=2k+1，因此任意 c<2k+1 都立即失败。
- 版本变化: Erdős、Faudree、Rousseau、Schelp 于 1993 年提出奇环的精确常数问题。Hng、Ji、Lamaison（2026-03 预印本）先给出对奇环的线性上界但未定出本题精确常数。Cambie、Freschi、Morawski、Petrova、Pokrovskiy（2026-01 预印本）解决了另一个“m 充分大”时的加性精确界问题（数据库 #570）。随后 Cambie、Freschi（2026-06 预印本）证明所有 t≥3 的统一界 R(C_t,H)≤(t−1)m+1，并在文中明确指出原题的最小常数为 t；这直接关闭本题。

陈述问题：

- 原始文字未明说图是有限简单图、m 为正整数、以及“best possible”是在所有实常数中取最小值；这些均是来源论文和标准 Ramsey 数记号所采用的常规解释。
- 不得把这里固定 k 的“对所有 m”常数与“m 相对于环长充分大”时的渐近系数混同：后者是相邻但不同的 Problem 570 型问题。
- 输入页面的 open 标签已过时：其页面最后编辑日为 2026-01-18，而完整解决预印本提交于 2026-06-09。

需要固定的量词/约定：

- k is a fixed integer with k>=1; the cycle has length 2k+1.
- H ranges over all finite simple graphs with e(H)=m>=1 and minimum degree at least 1; H need not be connected.
- The inequality has no additive error term and must hold for every admissible m, including m=1.
- c_k is minimized over real constants. R(F,H) uses non-induced monochromatic copies in a red-blue colouring of K_N.

### 文献与当前边界

已核验的主要结果：

- Erdős–Faudree–Rousseau–Schelp（1993，同行评审）建立 Ramsey size-linear 的研究框架并提出本类奇环问题。
- Goddard–Kleitman（1994）及 Sidorenko（1993）独立证明三角形情形 R(C_3,H)≤2m+1；Cambie–Freschi 的统一定理包含这一情形。
- Cambie–Freschi–Morawski–Petrova–Pokrovskiy（2026，预印本）证明对固定环长 t、m 足够大时 R(C_t,H)≤2m+floor((t-1)/2)，这是渐近精确的相邻结果。
- Hng–Ji–Lamaison（2026，预印本）在最终定理前证明奇环的显式线性上界 R(C_{2k+1},H)≤2m(1+B_km^{-1/20})+|H|。
- Cambie–Freschi（2026-06-09，预印本）证明任意 t≥3 的统一界 R(C_t,H)≤(t−1)m+1。结合 H=K_2 的 m=1 情形，精确常数为 t。

最近相关工作：Cambie 与 Freschi 的 arXiv:2606.11174（2026-06-09，v1）是最新且直接的工作。其证明按 e(H) 归纳，先处理不连通 H，再以 H 的最小度数导出红星；结合路径 Ramsey 上界、二阶邻域中长路径推出环的引理、随机二分 H 的顶点集及边/色数计数完成矛盾。

剩余核心：就 #569 的字面目标而言没有剩余开放核心：c_k=2k+1 已确定。不同的精确/渐近 Ramsey 问题仍可能开放，但不能作为本题的残余目标；特别是“m 足够大”时的加性精确式属于不同量词结构。

已使用方法：

- 对 e(H) 的归纳，并分别处理 H 的连通与不连通情形。
- 由避免蓝色 H 的扩张条件获得红色星；将红色路径闭合为所需红环。
- 路径 Ramsey 界、二阶邻域路径到环的结构引理，以及色数—边数关系。
- 对 H 的顶点作固定大小的随机二分，控制一侧的期望内部边数，再调用归纳假设。

争议或不确定性：

- 主证据是可公开检查的 7 页 arXiv 预印本，尚无同行评审发表记录；本审计未逐行重证每个引理，故建议作一次独立证明核验。
- 数据库 #569 仍标 open，与 2026-06 预印本冲突；时间线表明数据库标签落后，且页面本身警告其状态非权威。
- 论坛线程在检索中显示了解答链接，但直接打开受站点抓取错误影响；这不影响基于预印本本身的结论。

### 证据来源

- [A general bound on R(C_k,H)](https://arxiv.org/abs/2606.11174) — Stijn Cambie; Andrea Freschi, 2026-06-09; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 主定理证明：任意 t≥3、任意 m 条边且无孤立点的 H 都满足 R(C_t,H)≤(t−1)m+1≤tm；引言还明确由 R(C_t,K_2)=t 得最小常数为 t。因此对本题 c_k=2k+1。全文 7 页且含按 e(H) 归纳的证明，可供逐步审计。
- [Erdős Problem #569](https://www.erdosproblems.com/569) — Thomas F. Bloom (database record), 2026-01-18; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 给出待审计的原始表述、将其归为 1993 年图论问题集 Ramsey Theory #34，并仍标为 open；页面也明示该标签只是站点维护者的当前认识，不能代替文献检索。
- [Ramsey Size Linear Graphs](https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/abs/ramsey-size-linear-graphs/2F50FFB56AD4E42EFA80DA5B280225A0) — Paul Erdős; R. J. Faudree; C. C. Rousseau; R. H. Schelp, 1993; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 原始 Ramsey-size-linear 框架来源：固定图 G 的 Ramsey 数是否对任意无孤立点、给定边数的 H 线性有界。Cambie–Freschi 将本题明确归于该文提出的问题。
- [Ramsey number of a cycle versus a graph of a given size](https://arxiv.org/abs/2601.10238) — Stijn Cambie; Andrea Freschi; Patryk Morawski; Kalina Petrova; Alexey Pokrovskiy, 2026-01-15; `preprint`, `preprint`, directness=`indirect`, reliability=`high`. 证明当 m 相对于环长充分大时 R(C_t,H)≤2m+floor((t-1)/2)，并解决原文的另一个问题。它提供本题的相关渐近背景，但不能单独决定本题对所有 m 的最优 c_k。
- [Ramsey size linear and generalization](https://arxiv.org/abs/2603.25453) — Eng Keat Hng; Meng Ji; Ander Lamaison, 2026-03-30; `preprint`, `preprint`, directness=`indirect`, reliability=`high`. 在最终解答前给出奇环的中间上界 R(C_{2k+1},H)≤2m(1+B_k m^{-1/20})+p，并正确重述本题；该结果已被 2026-06 的统一定理严格加强。
- [Erdős Problem #569 discussion thread](https://www.erdosproblems.com/forum/discuss/569) — Stijn Cambie (solution-link comment), 2026-06-10; `forum`, `informal_claim`, directness=`indirect`, reliability=`medium`. 论坛作者评论指向 [CF26] 解答；该非正式声明不作为结论依据，结论依据是可检查的 arXiv 完整证明。
- [Andrea Freschi — Publications](https://www.freschiandrea.com/publications) — Andrea Freschi, date unknown; `author_page`, `informal_claim`, directness=`indirect`, reliability=`medium`. 作者页面将 A general bound on R(C_k,H) 列为与 Stijn Cambie 合作的 preprint，支持其截至审计日尚非同行评审发表物的状态判断。

### 完成标准

- 肯定出口: For the literal problem, a complete resolution is a proof that c_k=2k+1 for every integer k>=1: prove R(C_{2k+1},H)<= (2k+1)e(H) for every finite simple H with no isolated vertices, and prove no smaller constant works. The Cambie-Freschi theorem supplies the stronger upper bound R(C_{2k+1},H)<=2k e(H)+1; H=K_2 supplies the lower bound.
- 否定出口: For the claimed 2026 resolution, the decisive negative audit outcome would be a specific valid counterexample to its stated theorem, or an identified unrepaired gap that prevents the theorem from applying to some finite simple H with no isolated vertices. In that event #569 must be returned to an open/revised status rather than treated as solved.

不构成完成：

- Proving only that R(C_{2k+1},H)=O_k(e(H)) without determining the least uniform constant.
- Proving a bound only for connected H, only for sufficiently large m, or only for a restricted family of H.
- Showing the asymptotic coefficient 2 under an additional large-m hypothesis; that does not answer the all-m constant because H=K_2 is admissible.
- Checking numerical instances without a proof that covers every k and every admissible H.

正确性陷阱：

- Do not confuse the problem parameter k with the cycle-length parameter t in the 2026 paper; substitute t=2k+1.
- The lower bound is dictated by m=1: R(C_t,K_2)=t, so an asymptotic coefficient cannot be reported as the literal c_k.
- Verify that the theorem quantifies over disconnected as well as connected H and retains the no-isolated-vertices condition through induction.
- Check the Ramsey convention: non-induced red/blue copies in K_N, and the exact strict/integer endpoints in (t-1)m+1<=tm.

### 更新后的 AI 可解答性

- 等级: `not_applicable_closed_or_invalid`
- 分数: `0/100`
- 信心: `high`
- 结论: 不适用：字面问题已有可检查的完整预印本证明，后续工作应是证明核验与数据库更正，而非尝试解决开放题。

支持理由：

- Cambie–Freschi 给出直接覆盖所有 t≥3、所有 m≥1、所有无孤立点 H 的定理，并明确指出最优常数。
- H=K_2 的短证明给出精确下界，和该定理合并后不存在未定常数。

主要障碍：

- 证据目前为未经同行评审的 arXiv v1，需核验归纳、二阶邻域引理及小环基例。
- 网页数据库状态尚未同步，容易误把已经关闭的字面题转交为开放研究任务。

Proof-first 路线：

- 逐行审计 arXiv:2606.11174 的 Theorem 3：检查不连通分解、最小度顶点删除、红星大小、路径 Ramsey 调用、随机二分与最终数值矛盾。
- 独立验证边界例 R(C_t,K_2)=t，并检查由 (t-1)m+1≤tm 得出最小 uniform 常数的逻辑。

需要验证：

- 确认预印本自 2026-06-09 后是否有修订、撤回、勘误或同行评审版本。
- 在数据库 #569 更新状态前，由人工或形式化工具审查该预印本的完整证明。

### 审计限制与人工复核理由

- 审计使用了公开网页、arXiv 摘要与可解析的 7 页 PDF 文本；未执行机器形式化，也未逐行独立重写全部证明。
- 截至审计日，未发现 Cambie–Freschi 预印本的同行评审发表版本、勘误或撤回；这是一次时间敏感检索，不等于未来不存在更新。
- 数据库的论坛页面直接抓取发生内部错误；但原作者公开预印本足以支撑状态判断，论坛仅作辅助时间线证据。

- 关闭结论的核心证据为单篇、尚未同行评审的 arXiv v1；应由组合数学专家独立核验其归纳和不等式链。
- Erdős Problems 数据库仍将 #569 标为 open，建议在人工核验后向维护者提交包含 arXiv:2606.11174 和 K_2 边界例的状态更新。

<!-- DEEP_REVIEW:END -->
