# Problem 3

## 基本信息

- 原始链接: https://www.erdosproblems.com/3
- LaTeX 页面: https://www.erdosproblems.com/latex/3
- 原始状态: `open`
- 奖金: `$5000`
- 主类别: `number theory`
- 原始标签: `number theory`, `additive combinatorics`, `arithmetic progressions`
- 形式化状态: `yes`
- OEIS: `A003002`, `A003003`, `A003004`, `A003005`
- 原站备注字段: 无

## 原问题

If $A\subseteq \mathbb{N}$ has $\sum_{n\in A}\frac{1}{n}=\infty$ then must $A$ contain arbitrarily long arithmetic progressions?

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `22/100`
- 建议路线: 优先文献定位、特殊情形、数值实验和辅助引理搜索；完整证明需要新的数学思想。

## 判断依据

### 有利因素

- 已有形式化陈述，可降低语义误读风险
- 存在 OEIS 数据入口，利于实验与反例搜索

### 主要障碍

- 所属标签偏证明密集：additive combinatorics, arithmetic progressions, number theory
- 题面含渐近/无限对象线索：\ll
- 原记录含奖金 $5000，说明该题被长期视为高价值难题；这不是否定依据，但提高验证门槛。
- 缺少明显有限搜索入口。

### 公开版思考过程摘要

- 先识别问题类型：无限/渐近或抽象证明倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: additive combinatorics, arithmetic progressions, number theory
- 有限/计算线索: 无
- 渐近/无限线索: \ll
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **不太可能由 GPT-5.5 级别模型在一次研究周期内完整解决；较可行的是验证关键等价化、形式化已有充分条件、检查文献中关于 r_k(N) 的量化边界是否足以推出结论，并对特定 k 或有限范围做计算/形式化验证。**
- 等级: `low_candidate`
- 分数: `18/100`
- 信心: `high`
- 可能路线: 最现实路线是把问题规约为对无 k 项等差数列集合最大规模 r_k(N) 的足够强上界，形式化证明“若 r_k(N) 满足类似 N/((log N)(log log N)^2) 的界，则任意倒数和发散集合含任意长等差数列”。随后用文献检索核对 k=3、k=4 和一般 k 的当前最强界，并用证明助理验证这些界与调和级数分块估计之间的逻辑关系。完整解决则需要为所有 k 证明远强于当前一般结果的 r_k(N) 上界。

### 支持理由

- 题目本身已明确核心瓶颈是 r_k(N) 的量化上界，而给出的备注说明已知一般 k 的最好结果仍只是 N/exp((log log N)^{c_k}) 级别。
- 问题有清晰的形式化入口：用分块求和或Abel求和把倒数和条件与计数函数 |A∩[1,N]| 联系起来，再转化为 r_k(N) 的增长界。
- 对 k=3，备注指出已有结果足以处理非平凡情形；这部分较适合由模型配合文献和形式化工具复核。
- 对一般 k，目标不是搜索有限反例，而是证明全局渐近上界；计算实验只能辅助理解，不能替代核心证明。
- 形式化状态为 yes，说明至少命题表达和部分基础结构可能已有机器可读基础，有利于验证推论链而非直接产生突破性组合证明。

### 主要障碍

- 完整结论需要对每个 k 给出足够强的 r_k(N) 上界，这正处于高阶傅里叶分析、密度增量和加性组合学前沿。
- 现有一般 k 上界按备注仍明显弱于足以推出倒数和版本的典型对数级需求。
- 模型容易在复杂组合证明中生成不可验证的密度增量步骤、参数损失或错误的迭代闭合。
- 形式化证明高阶组合工具本身成本很高，即使数学思路已知，也需要大量库建设和细节校验。
- 反例搜索对开放命题帮助有限，因为命题是无限渐近性质，有限无 k-AP 集合不能直接证伪。

### 需要的验证

- 逐行验证从 r_k(N) 上界到倒数和收敛/发散矛盾的推导，特别是分块估计中的对数因子是否足够。
- 检索并核对备注中 Bloom-Sisask、Kelley-Meka、Green-Tao、Gowers、Leng-Sah-Sawhney 等结果的精确陈述与适用范围。
- 在证明助理中形式化计数函数、r_k(N)、无 k 项等差数列条件和充分上界推出原命题的逻辑链。
- 若模型声称新进展，必须给出可审计的密度增量命题、参数递推、终止条件和最终上界，并由专家或形式化工具检查。
- 用计算搜索仅作为 sanity check：验证小 N 的 extremal sets、OEIS 数据和定义一致性，不能作为主证明证据。

### 公开版思考摘要

这个问题的结构很清楚：要证明倒数和发散的集合含任意长等差数列，足够强的 r_k(N) 上界会直接给出结论。模型和工具很适合清理这条规约、检查已知文献边界、形式化充分条件，并复核 k=3 等已知可处理片段。但对任意 k 的完整结论要求突破当前一般上界，属于深层加性组合学难题，不是靠有限计算或常规形式化即可完成。因此评为低候选：可验证和整理，较难实质性解决。

### 免责声明

以上是对 GPT-5.5 级别模型辅助解决潜力的审查，不是该 Erdős 问题的证明或反例。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `confirmed_open`
- 状态信心: `high`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_3.md](../../prompts/problem_3.md)

### 状态结论

该命题仍是开放问题。Erdős Problems 的近期索引仍列 #3 为 open，独立的 2025 MathOverflow 讨论和近期问题索引均将其未解部分定位为所有固定长度 k≥4。已核验的三项等差数列情形已解决；没有发现截至 2026-07-27 可审计的完整证明或反例。

### 当前规范陈述

设 A 为正整数的子集，且正项级数 Σ_{a∈A}1/a 发散。则对每个整数 k≥3，是否存在 x∈N 及 d∈N、d≥1，使 {x,x+d,…,x+(k−1)d}⊆A？也就是说，A 对每个有限长度都含一个非平凡等差数列；数列可依赖于 A 与 k。

```text
Let A be a subset of the positive integers. If the positive series ∑_{a∈A} 1/a diverges, then for every integer k≥3 there exist x∈N and d∈N with d≥1 such that {x,x+d,...,x+(k−1)d}⊆A. Thus A contains a non-trivial k-term arithmetic progression for every finite k. The progression may depend on A and k.
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 没有找到针对规范化字面命题的简单反例。有限集不满足发散假设；已知的避免长等差数列的稀疏构造也未给出同时保持倒数和发散的例子。这只是针对性检查，不是对所有构造的穷尽排除。
- 版本变化: 该问题本身没有发现已被正式替换的版本。历史进展是分长度的：Bloom–Sisask 解决 k=3 所需的阈值；Kelley–Meka 及随后 Bloom–Sisask 的工作大幅强化 r_3(N)；Green–Tao 给出 k=4 的多对数界；Leng–Sah–Sawhney 给出 k≥5 的一般界。这些均未解决原命题要求的所有长度。

陈述问题：

- 输入中的 N 未明说为正整数；按数论惯例及原问题语境应为 {1,2,…}。
- “arbitrarily long”必须理解为“对每个有限 k 都存在一个 k 项等差数列”，并不要求存在无限等差数列。
- “non-trivial”应明确为公差 d>0；否则常数数列会使结论失去内容。
- 问题页所说的 r_k(N) 上界是证明本题的充分路线，不应误读为本题与给定某个精确 r_k 上界逻辑等价。

需要固定的量词/约定：

- The order is: for every A⊆N, if ∑_{a∈A}1/a=∞, then for every k≥3 there exist x∈N and d∈N_{>0}.
- x and d may depend on A and k.
- Since all summands are nonnegative, divergence has its ordinary unambiguous meaning.

### 文献与当前边界

已核验的主要结果：

- Bloom–Sisask（2020，预印本）证明无 3-AP 的 A⊆[N] 满足 |A|≪N/(log N)^(1+c)。对 dyadic 区间求和即可推出每个倒数和发散集含 3-AP。
- Kelley–Meka（FOCS 2023，同行评审）把 r_3 的上界推进到 2^{-O((log N)^β)}N；Bloom–Sisask（2023，预印本）给出 β=1/9 的进一步改进。它们只处理 k=3。
- Green–Tao（2017，同行评审）证明 r_4(N)≪N/(log N)^c（某个 c>0）。这个 c-幂的多对数节省不足以自动使 dyadic 倒数质量求和收敛，故 k=4 仍未由此解决。
- Leng–Sah–Sawhney（2024，预印本）对每个 k≥5 证明 r_k(N)≪N exp(−(log log N)^{c_k})。这比旧的一般长度界强，但仍远弱于常见的、足以解决本题的约 N/((log N)(log log N)^2) 级充分条件。

最近相关工作：本次可完全核验的最新直接一般长度定量结果是 Leng、Sah、Sawhney（2024）的 arXiv:2402.17995。检索还发现 Shkredov 2026 年《Some new results on the higher energies》，其摘要提及该猜想和更长等差数列，但可访问材料不足以核实其是否改进了与本题有关的 r_k 阈值；因此没有把它列为最强已验证结果。

剩余核心：证明或否定：对每一个固定 k≥4，任何 k-AP-free 的 A⊆N 都有收敛的倒数和；等价地，构造一个倒数和发散而全局避免某个固定 k≥4 项非平凡等差数列的集合。完整原题要求前一种结论对全部固定 k 成立。

已使用方法：

- 以 r_k(N) 的有限区间上界控制 dyadic 块中 A 的基数，再以 ∑_j |A∩[2^j,2^{j+1})|/2^j 估计倒数和。
- Roth/Szemerédi 的密度增量、高阶 Fourier/Gowers 范数及逆定理方法。
- 对 k=3，Kelley–Meka 型高阶能量与伪随机性技术及 Bloom–Sisask 的简化/强化。
- 反例路线中的分层或分块 AP-free 构造，但必须同时保留全局调和质量。

争议或不确定性：

- 没有发现 Problem 3 的官方论坛讨论串；问题页面搜索索引显示页面评论为 0。MathOverflow 讨论不是正式状态裁定。
- 输入标记 formalized=yes，但未在公开可检索结果中定位具体的 Lean 定理/文件；只能确认相关形式化项目存在。
- 2026 年的 Shkredov 论文摘要直接提及该猜想，但正文未在本次访问中得到可审计的定理范围，因此其对当前前沿的影响须人工复核。
- 未找到 2025–2026 年可审计的完整解决；这支持而不能逻辑证明“仍开放”。

### 证据来源

- [Erdős Problems — Problem 3](https://www.erdosproblems.com/3) — Thomas F. Bloom / Erdős Problems, date unknown; `problem_page`, `database_record`, directness=`direct`, reliability=`high`. 规范问题陈述、数据库状态和引用链的主记录。网页直开受 403 限制；其近期标签索引仍显示该题为 open。
- [Erdős Problems — LaTeX source for Problem 3](https://www.erdosproblems.com/latex/3) — Thomas F. Bloom / Erdős Problems, date unknown; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 用于核对问题页面提供的 LaTeX 版本；本次直开同样受 403 限制。
- [Erdős Problems — arithmetic progressions tag index](https://www.erdosproblems.com/tags/arithmetic%20progressions) — Thomas F. Bloom / Erdős Problems, 2026; `secondary_index`, `database_record`, directness=`indirect`, reliability=`high`. 近期抓取的索引明确列出 Erdős Problem #3，并将相关一般 r_k 问题、#140 的三项强化结果和一般 k 文献加以区分。
- [Breaking the logarithmic barrier in Roth's theorem on arithmetic progressions](https://arxiv.org/abs/2007.03528) — Thomas F. Bloom; Olof Sisask, 2020-07-07; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 摘要证明无非平凡三项等差数列集满足 |A|≪N/(log N)^(1+c)，并明确称其解决了 Erdős 关于等差数列猜想的首个非平凡情形。
- [Strong Bounds for 3-Progressions](https://doi.org/10.1109/FOCS57990.2023.00059) — Zander Kelley; Raghu Meka, 2023; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. FOCS 2023 论文；对应预印本证明三项等差数列避集的准多项式型密度上界。
- [An improvement to the Kelley-Meka bounds on three-term arithmetic progressions](https://arxiv.org/abs/2309.02353) — Thomas F. Bloom; Olof Sisask, 2023-09-05; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 摘要将三项避集上界强化为 exp(−c(log N)^(1/9))N；这是本次检索中最强的直接 r_3 预印本结果。
- [New bounds for Szemerédi's theorem, III: a polylogarithmic bound for r_4(N)](https://doi.org/10.1112/S0025579317000492) — Ben Green; Terence Tao, 2017; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 证明 r_4(N) 的多对数密度上界；该结果本身不足以通过通常分块求和推出 k=4 的倒数和收敛。
- [Improved Bounds for Szemerédi's Theorem](https://arxiv.org/abs/2402.17995) — James Leng; Ashwin Sah; Mehtaab Sawhney, 2024-02-28; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 摘要证明 k≥5 时 r_k(N)≪N exp(−(log log N)^{c_k})，并说明使用 Gowers 范数逆定理和密度增量策略；未声称解决本题。
- [Why is Erdős' conjecture on arithmetic progressions not discussed much, and is there an active pathway to its resolution?](https://mathoverflow.net/questions/489375/why-is-erd%C5%91s-conjecture-on-arithmetic-progressions-not-discussed-much-and-is-t) — Will Sawin (answer); MathOverflow contributors, 2025-03-13; `forum`, `informal_claim`, directness=`indirect`, reliability=`medium`. 领域专家回答说明 k≥4 的现有 r_k 界距足以推出该猜想的对数级充分条件很远，并区分 k=3 已解决。它是状态交叉核验，不是证明来源。
- [All open Erdős problems formalized — milestone](https://github.com/google-deepmind/formal-conjectures/milestone/1) — google-deepmind/formal-conjectures contributors, date unknown; `formalization`, `formalized_artifact`, directness=`indirect`, reliability=`medium`. 显示存在覆盖开放 Erdős 问题的形式化项目，但本次未定位到 Problem 3 的具体定理文件或 issue，故不能据此断言该题陈述已成功审计式形式化。

### 完成标准

- 肯定出口: A complete affirmative resolution proves: for every A⊆N with ∑_{a∈A}1/a=∞ and every k≥3, there exist x∈N and d≥1 such that x,x+d,...,x+(k−1)d all belong to A.
- 否定出口: A complete negative resolution constructs and proves an A⊆N and one fixed k≥3 such that ∑_{a∈A}1/a=∞ while A contains no k-term arithmetic progression with positive common difference.

不构成完成：

- A proof only for k=3, k=4, or any finite set of lengths.
- An r_k(N) bound that is not strong enough to force convergence of the reciprocal subseries.
- A bound valid only on selected scales without a transfer argument covering every scale.
- A finite computation, asymptotic heuristic, or informal proof claim.
- A construction avoiding progressions only below a cutoff, or avoiding a progression with d=0 only.

正确性陷阱：

- Keep the quantifiers in the order ∀A ∀k ∃x,d; neither uniformity in k nor a single progression for all k is required.
- Require d>0 and check every term is positive and belongs to A.
- In an r_k-to-harmonic argument, control every dyadic block and justify the summation; an initial-segment upper bound must be used with valid monotonicity/block estimates.
- Do not infer k=4 from the Green–Tao N/(log N)^c bound: the associated dyadic series need not converge when c≤1.
- A counterexample must be globally k-AP-free for one fixed k and must prove divergence, not merely arbitrarily large partial reciprocal sums on chosen finite intervals.

### 更新后的 AI 可解答性

- 等级: `low_candidate`
- 分数: `12/100`
- 信心: `medium`
- 结论: 这是定义严谨且确实开放的证明目标，但其剩余部分处于高阶加性组合的深层定量障碍。AI 可有效完成文献审计、引理化和反例筛选，但短期内独立解决完整问题的概率低。

支持理由：

- 正反两种完成条件都有明确、可审计的证明证书。
- 固定长度的已知结果给出精确基线，并可把“r_k 界是否足够”化成可验证的求和引理。
- 可并行探索直接多尺度结构、改进 r_k 界与反例/障碍构造。

主要障碍：

- k≥4 的已知定量界与常见充分的对数级阈值之间仍有很大差距。
- 一般 k 的证明依赖深层的 Gowers 范数、逆定理和密度增量技术，有限计算无法替代全尺度论证。
- r_k 上界只是充分路线；不能假定任何解决必然表现为某个标准 r_k 上界的改进。

Proof-first 路线：

- 先证明一个带完整常数/阈值的“有限区间 AP-free 上界 ⇒ 倒数和收敛”引理，并精确标明现有界为何仅覆盖 k=3。
- 尝试直接从调和质量发散推出多尺度加性结构，预先写出可被反例否定的中间引理。
- 反例方向先研究带显式 AP-free 证书的分层模型，并严格计算其调和质量；若必收敛，应提炼为障碍引理。

需要验证：

- 复核 Green–Tao 的 k=4 指数范围及从各个 r_k 上界到调和级数结论的完整 dyadic 推导。
- 在任何声称突破前刷新 2025–2026 年 arXiv、期刊数据库和作者主页，尤其核验 Shkredov 2026 年工作。
- 定位 formalized=yes 所指的具体仓库、提交、定理陈述和依赖，以确认它是陈述形式化而非完整证明。

### 审计限制与人工复核理由

- Erdős Problems 主页及 LaTeX 页在本次工具中返回 403；已尝试直开，并以其近期标签索引和输入中给出的精确记录交叉核对。
- 审计核验了论文摘要、期刊/会议元数据和可访问来源，但没有重证明深层加性组合定理。
- 网页与 arXiv 检索不能逻辑排除未索引手稿、私人通信或 2026-07-27 后出现的结果。
- 2026 年 Shkredov 论文的可访问摘要不足以审计其精确定理范围，故未将其作为改变状态的证据。
- formalized=yes 的具体工件未找到；形式化状态不影响本题开放性的判断，但需要人工定位。

- 需要领域专家复核 k=4 及一般 k 的每个已知界到调和级数结论的精确阈值与所有常数范围。
- 应审阅 Shkredov 2026 年论文全文，确定它是否给出与本题直接相关的新长等差数列界。
- 应定位并编译/检查 Problem 3 所对应的具体形式化工件，以澄清数据库 formalized 标记。
- 高风险研究启动前应使用 MathSciNet、zbMATH、作者主页和最新 arXiv 再做一次截止日状态检查。

<!-- DEEP_REVIEW:END -->
