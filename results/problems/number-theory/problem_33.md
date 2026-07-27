# Problem 33

## 基本信息

- 原始链接: https://www.erdosproblems.com/33
- LaTeX 页面: https://www.erdosproblems.com/latex/33
- 原始状态: `open`
- 奖金: `no`
- 主类别: `number theory`
- 原始标签: `number theory`, `additive basis`
- 形式化状态: `yes`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

Let $A\subset\mathbb{N}$ be such that every large integer can be written as $n^2+a$ for some $a\in A$ and $n\geq 0$. What is the smallest possible value of\[\limsup \frac{\lvert A\cap\{1,\ldots,N\}\rvert}{N^{1/2}}?\]Is\[\liminf \frac{\lvert A\cap\{1,\ldots,N\}\rvert}{N^{1/2}}>1?\]

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `35/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 题面或备注出现有限对象/计算线索
- 已有形式化陈述，可降低语义误读风险

### 主要障碍

- 所属标签偏证明密集：number theory
- 题面含渐近/无限对象线索：liminf, limsup

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: additive basis
- 证明密集标签命中: number theory
- 有限/计算线索: finite
- 渐近/无限线索: liminf, limsup
- 构造/存在性线索: construct

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **中等候选。根据给定摘录，第二个“liminf 是否大于 1”的问题已经由已知下界解决；真正仍开放的是最小可能 limsup 常数。GPT-5.5 级别模型配合计算搜索、形式化验证和文献复核，不太可能直接给出最终最优常数，但有现实机会显著推进上界构造、验证已有结论，或在受限构造族中给出严格可审计的改进。**
- 等级: `medium_candidate`
- 分数: `60/100`
- 信心: `medium`
- 可能路线: 最可行路线是把问题拆成构造上界和不可避免下界两部分：先形式化 additive complement 条件与计数归一化；用程序搜索稀疏集合 A 或递归/分块/self-similar 构造，使每个大整数被平方数加 A 覆盖；再用自动化有限验证加手写或形式化证明把有限覆盖提升为全局覆盖，并估计 limsup 常数。下界方向可复核摘录中的 4/pi 型结论，但原创性改进会更难。

### 支持理由

- 问题已有明确形式化标记，适合用证明助手检查定义、归一化常数、有限到无限的覆盖归纳。
- 目标对象是加法补集，天然适合计算反例搜索、覆盖缺口检测、整数规划或启发式构造搜索。
- 给定摘录显示当前上界约 6.66，而下界约 1.273，间隙较大；较大间隙通常给计算辅助构造留下改进空间。
- 第二个子问题在摘录中已有强于 1 的下界，可由模型复核和形式化，而不是从零突破。
- limsup 最小化据摘录“研究较少”，因此模型辅助探索特定构造族可能产生有价值的新候选。

### 主要障碍

- 精确最优 limsup 常数很可能需要新的结构性定理，而不只是有限搜索。
- 构造 A 必须覆盖所有充分大的整数，有限样本上的高覆盖率不能直接证明渐近结论。
- limsup 而非普通密度使得局部稀疏构造可能被峰值行为破坏，常数估计需要严格控制所有 N。
- 下界改进涉及平方集合与补集覆盖的全局限制，可能需要较深的解析数论或加性组合工具。
- 若搜索得到复杂或非周期构造，将其压缩成可发表、可形式化的无限族证明可能是主要瓶颈。

### 需要的验证

- 对任何新构造，必须给出无限族定义，而不仅是有限前缀。
- 需要机器检查大范围覆盖缺口，并证明有限检查为何足以推出所有大整数覆盖。
- 需要严格证明 |A∩{1,...,N}|/sqrt(N) 的全局 limsup 上界，而不是只在采样点估计。
- 若声称改进下界，需要复核与摘录中 4/pi 下界的关系，并排除只是在额外假设下成立。
- 形式化验证应覆盖自然数边界、平方数允许 n=0、‘every large integer’ 的阈值处理，以及 limsup/liminf 的实分析定义。

### 公开版思考摘要

该问题不是纯粹计算题，但它有可形式化的定义、可自动检验的覆盖条件和明显的构造搜索入口。GPT-5.5 级别系统最有希望在上界构造和验证方面取得进展，例如找到更稀疏的加法补集并把有限验证转化为递归证明。完整确定最小 limsup 常数则仍属于较高风险目标，因为需要解释为什么所有可能的 A 都不能更好。

### 免责声明

这只是对 AI 辅助可推进性的审查，不是该 Erdős 问题的解答，也不声称给出了新的上界、下界或最优常数。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `revised_open`
- 状态信心: `medium`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_33.md](../../prompts/problem_33.md)

### 状态结论

输入把两个问题并列在同一条目中。第二问“对每个平方数加法补集，liminf 是否大于 1？”早已由 Moser 的 1965 年结果肯定解决，且后续工作给出 liminf≥4/π。仍然开放的精确目标是：在所有平方数加法补集中最小化增长常数 limsup A(N)/√N（严格说应取下确界）；截至本次检索未发现该常数的确定或匹配上下界。Erdős Problems 页面及其 2026-03 论坛讨论仍将该剩余优化问题标为 open。

### 当前规范陈述

令 ℕ0={0,1,2,...}，S={n²:n∈ℕ0}，且 A⊆ℕ0。若存在 X0∈ℕ0，使得对每个 m≥X0 都存在 a∈A、n∈ℕ0 满足 m=a+n²，则称 A 是平方数集的加法补集。对实数 x≥1 记 A(x)=|A∩{1,...,⌊x⌋}|。尚存的开放优化问题是确定 C*=inf_A limsup_{x→∞}A(x)/√x，其中下确界遍历所有这类 A；若将其称作“最小值”，完整答案还须证明该下确界是否取到。另一历史问题“是否总有 liminf A(x)/√x>1”已有肯定答案，且事实上 liminf≥4/π。

```text
Let ℕ0={0,1,2,...}, let S={n²:n∈ℕ0}, and let A⊆ℕ0. Call A an additive complement of the squares if there is an X0∈ℕ0 such that, for every m∈ℕ0 with m≥X0, there exist a∈A and n∈ℕ0 satisfying m=a+n². Put A(x)=|A∩{1,...,⌊x⌋}| for real x≥1. The surviving open optimization problem is to determine C*=inf_A limsup_{x→∞} A(x)/√x, where the infimum ranges over all such A; a complete answer must also establish whether the infimum is attained if it is described as a “smallest value.” The separate historical question is whether every such A satisfies liminf_{x→∞}A(x)/√x>1; it has the affirmative answer, in fact liminf≥4/π.
```

### 陈述、量词与反例审计

- 歧义严重度: `material`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 未发现能推翻按上述量词重建后的陈述的简单构造。对形式化文件“every integer”版本，任一 eventual complement 可通过加入有限初段 {0,...,X0−1} 变成 every-integer complement；这不是原固定集合条件的逻辑等价，但足以保持优化下确界和渐近计数常数。
- 版本变化: Erdős 的原始问题来源为 1956 年文献。Moser（1965）已肯定回答 liminf>1，并给出 1.06；Cilleruelo（1993）、Habsieger（1995）及 Balasubramanian–Ramana（2001）独立给出 4/π 的下界。该条目的网页在 2025 年吸收了 Wouter van Doorn 的非同行评议构造，给出 C*≤2φ^(5/2)。2025–2026 年关于表示函数、Ben Green 问题和“exact on average”补集的工作提供相关限制，但没有给出 C* 的值。因而应将原复合条目修订为“已解决的 liminf 子问题 + 开放的 limsup 优化子问题”。

陈述问题：

- 原文并列了两个不等价问题：精确最小化 limsup 的优化问题仍开放，而“liminf>1？”已被 Moser 肯定解决；不能把后者当作当前开放目标。
- “smallest possible value”在未证明极值可达时应解释为下确界 C*；“存在最小元”是额外结论。
- “every large integer”必须显式为“存在阈值 X0，对所有 m≥X0”。自然数是否从 0 或 1 开始、是否允许平方 0，只造成有限初段差异；本审计采用 ℕ0 并允许 n=0。
- Formal Conjectures 中的文件把“eventually”改成“every integer”。对固定 A 两条件并不等价；但将 A 加上有限个小整数可把前者变为后者而不改变该 limsup，因此相应下确界相同。该文件的主定理和 van Doorn 上界均含 sorry，不能视为形式化证明。

需要固定的量词/约定：

- The complement condition is ∃X0∈ℕ0 ∀m∈ℕ0, m≥X0 → ∃a∈A ∃n∈ℕ0, m=a+n².
- All limsup and liminf are taken as x→∞; using integer N instead of real x gives the same values for this counting function.
- The optimization is over infinite sets A satisfying the eventual-cover condition. C* denotes an infimum, not an assumed attained minimum.
- The already-settled liminf assertion is universal: it quantifies over every additive complement A.

### 文献与当前边界

已核验的主要结果：

- Moser（1965，同行评议会议论文）证明任何平方数加法补集都满足 liminf A(N)/√N>1.06，从而已肯定回答原条目的第二问。
- Cilleruelo（1993）、Habsieger（1995）和 Balasubramanian–Ramana（2001，后者书目信息为 C. R. Math. Acad. Sci. Soc. R. Can. 23(1), 6–11）独立给出更强的普遍下界 liminf A(N)/√N≥4/π。因此对每个补集也有 limsup A(N)/√N≥4/π，故 C*≥4/π。
- van Doorn 的 2025 自存档构造（被 Erdős Problems 编辑纳入条目）对所有 N 给出 A(N)<2φ^(5/2)√N，故 C*≤2φ^(5/2)≈6.66；它不是已同行评议的最优性证明。
- Chen–Fang（2017）、Ding（2020）以及 Ding–Sun–Wang–Xia（2026）研究表示数和 Ben Green 的有序补集问题。它们提供了结构性限制，但没有推出 C* 的精确值或改善上述 C* 的直接上下界。

最近相关工作：Ding、Sun、Wang、Xia 的同行评议论文《A note on additive complements of the squares》（Discrete Mathematics 349(2), 114763，2026；预印本 2022）证明表示函数的总超额为 ≫√N，并加强与 Ben Green 问题有关的界。Ding 的 2025-12 预印本又否定了平方数的 exact-on-average 补集。二者均相关但目标不同；检索中没有发现 2023–2026 年确定 C* 的论文或预印本。

剩余核心：确定 C*=inf_A limsup A(N)/√N 的精确值，并给出匹配的普遍下界和构造上界；若声称“最小值”而不是下确界，还须说明是否存在达到 C* 的补集。当前经核验的区间为 4/π≤C*≤2φ^(5/2)。

已使用方法：

- 有限区间覆盖/计数论证，把平方数的密度与 A(N) 的大小联系起来。
- 通过平方差 x²−y²=(x−y)(x+y) 计数不同表示，研究表示函数及其总超额。
- Euler–Maclaurin 型对圆弧求和的估计，用于将 A 的有序元素 w_n 与临界常数 π²/16 联系起来。
- 分层或尺度化的显式构造；van Doorn 的构造给出当前记录的直接 limsup 上界。
- 较新的工作还使用了 Ford 关于给定区间内因子的分布结果，但用于表示函数/精确平均问题而非已知的 C* 定值。

争议或不确定性：

- Erdős Problems 的 open 标签是站点所有者的当前信念，并非文献完备性证明；页面也明确作此警告。
- van Doorn 上界来自公开 GitHub PDF 和论坛，尚非同行评议；本审计核验了文件与其被条目采纳，但未逐页审核证明。
- Formal Conjectures 文件有 sorry，且固定集合层面的 eventual/every-integer 注释不正确；它不能作为任何结果的形式化验证。
- 本次可访问的近期论文均未声称解决 C*；但旧文献并非均可取得全文，故“无更强结果”是有范围的检索结论，不是逻辑上的不存在证明。

### 证据来源

- [Erdős Problems — Problem 33](https://www.erdosproblems.com/33) — Thomas F. Bloom (database owner/editor), 2025-12-27; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 数据库的当前条目陈述了该复合问题、Moser 与 4/π 历史下界，并记录 van Doorn 的 2φ^(5/2) 构造；页面自身警告其 open 标签只是所有者当前判断。
- [Erdős Problem #33 — Discussion thread](https://www.erdosproblems.com/forum/thread/33) — Erdős Problems forum; Wouter van Doorn; Thomas Bloom; Sayan Dutta, 2026-03-06; `forum`, `informal_claim`, directness=`direct`, reliability=`medium`. 当前论坛仍标记 open，称尚无评论中的解答声明；van Doorn 声明并链接其构造，Bloom 明确区分了被忽略过的 liminf 文献与较少研究的 limsup 问题。论坛中的数学断言本身未经同行评议。
- [The smallest set such that every positive integer is the sum of a square and an element from this set](https://github.com/Woett/Mathematical-shorts/blob/main/The%20smallest%20set%20such%20that%20every%20positive%20integer%20is%20the%20sum%20of%20a%20square%20and%20an%20element%20from%20this%20set.pdf) — Wouter van Doorn, date unknown; `other`, `informal_claim`, directness=`direct`, reliability=`medium`. 论坛所链接的自存档证明文件，是 C*≤2φ^(5/2) 的非同行评议来源。网页可核验该文件的存在与链接，但本审计未能逐页独立复核 PDF 证明。
- [On the additive completion of sets of integers](https://doi.org/10.1090/pspum/008/0175874) — Leo Moser, 1965; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 原始文献条目，后续已发表来源和 Erdős Problems 均归因于它：每个平方数加法补集满足严格大于 1 的 liminf 下界，Moser 的数值为 1.06。
- [The additive completion of k-th powers](https://doi.org/10.1006/jnth.1993.1049) — Javier Cilleruelo, 1993; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 原始文献之一；后续发表论文与数据库将平方情形 liminf≥4/π 归因于 Cilleruelo、Habsieger 和 Balasubramanian–Ramana 的独立工作。
- [On the additive completion of polynomial sets](https://doi.org/10.1006/jnth.1995.1039) — Laurent Habsieger, 1995; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 原始文献之一；其多项式加法完成结果在平方情形给出 4/π 下界。
- [Green’s problem on additive complements of the squares](https://comptes-rendus.academie-sciences.fr/mathematique/item/CRMATH_2020__358_8_897_0/) — Yuchen Ding, 2020-12-03; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 开放获取的发表论文给出完整参考书目并叙述历史下界链，且解决 Chen–Fang 关于 Ben Green 的不同顺序型问题的一个猜想；它不确定 C*。
- [Additive complements of the squares](https://doi.org/10.1016/j.jnt.2017.04.016) — Yong-Gao Chen and Jin-Hui Fang, 2017; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 研究平方数补集的表示函数并提出与 Ben Green 问题有关的结果；后续 Ding 的论文将其作为被改进的工作。该方向不等于求 C*。
- [A note on additive complements of the squares](https://arxiv.org/abs/2211.16810) — Yuchen Ding, Yu-Chen Sun, Li-Yuan Wang, Yutong Xia, 2022-11-30; `preprint`, `preprint`, directness=`direct`, reliability=`medium`. 预印本给出表示函数超额的改进及对 Ben Green 问题的更强限制；其 2026 年同行评议版本见下一条。
- [A note on additive complements of the squares](https://www.sciencedirect.com/science/article/pii/S0012365X25003711) — Yuchen Ding, Yu-Chen Sun, Li-Yuan Wang, Yutong Xia, 2026-02; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. Discrete Mathematics 349(2), Article 114763，DOI 10.1016/j.disc.2025.114763。其摘要证明表示函数总超额 ≫√N，并改进 Ben Green 问题的一个界；没有声称确定 C*。
- [No exact on average additive complements of squares](https://arxiv.org/abs/2512.15407) — Yuchen Ding, 2025-12-17; `preprint`, `preprint`, directness=`direct`, reliability=`medium`. 该预印本证明平方数没有 exact-on-average additive complement，并解决 Ruzsa 2001 与 Ben Green 2017 的不同问题；未给出 C* 的值，不能误报为 #33 的解答。
- [FormalConjectures/ErdosProblems/33.lean](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/33.lean) — Formal Conjectures Authors, 2025; `formalization`, `formalized_artifact`, directness=`direct`, reliability=`high`. Lean 文件形式化了一个优化表达式及 van Doorn 型上界表达式，但两条 theorem 都以 sorry 结束，并把 eventual 条件改写为 every-integer 条件；它是陈述草图而非机器核验的证明。

### 完成标准

- 肯定出口: For an explicitly identified real constant C, prove C*=C: (i) construct additive complements A_ε with limsup A_ε(x)/√x≤C+ε for every ε>0 (or one complement attaining C), and (ii) prove limsup A(x)/√x≥C for every additive complement A. If the assertion is that a smallest value is attained, also exhibit an A with limsup=C.
- 否定出口: For any proposed exact constant C or claimed extremal construction, decisively refute that claim by either producing an additive complement with limsup<C, or proving a universal lower bound limsup>C, respectively. A proof that C* is not attained is also decisive only for the attainment claim, not for determining C*.

不构成完成：

- Re-proving only liminf A(x)/√x≥4/π, since that is weaker than and does not determine the limsup infimum.
- Giving an additive complement with any finite limsup, or improving only the numerical upper bound, without a matching universal lower bound.
- Settling Ben Green's ordered-sequence question, the exact-on-average question, or a representation-function estimate without a proved implication for C*.
- Checking finitely many N, numerical optimization on a finite interval, or an asymptotic claim valid only along a subsequence.
- A Lean declaration containing sorry, an opaque axiom, or a formal target whose eventual-coverage condition was changed without the finite-modification equivalence argument.

正确性陷阱：

- Keep the quantifier order: the coverage threshold may depend on A, while the universal lower bound must cover every admissible A.
- Distinguish A(N)<C√N for every N from limsup≤C; neither alone proves an infimum is attained.
- Count a∈A rather than representations; duplicate representations cannot be silently treated as distinct elements of A.
- Treat the square 0 and the initial convention for ℕ consistently; finite changes preserve the normalized limits but do not make fixed-set predicates literally equivalent.
- Do not infer a limsup optimum from liminf bounds, exact-on-average nonexistence, or constraints on the ordered sequence w_n without a proved bridge.

### 更新后的 AI 可解答性

- 等级: `low_to_medium_candidate`
- 分数: `24/100`
- 信心: `medium`
- 结论: 修订后的 C* 优化问题清晰且可检验，但仍是长期开放的全局极值问题；目前上下界差距很大，近期成果主要控制相邻表示函数问题。因此它适合做严谨的定向探索和界改进审计，不宜把有限计算或已解的 liminf 子问题误当作可快速解决的目标。

支持理由：

- 目标可精确定义为一个下确界，所有候选构造和普遍下界都可独立检查。
- 已有明确的下界 4/π、显式上界 2φ^(5/2)，并有多条表示函数方法可供分析。
- 近期论文刻画了临界密度附近的一些障碍，可能提供可分解的中间引理。

主要障碍：

- 要得到精确值需同时处理任意无限补集和构造最优性，现有界之间仍有大间隙。
- 表示函数、exact-on-average 及 Ben Green 问题与 C* 不自动等价，错误迁移结论风险高。
- 最好的上界目前来自非同行评议的构造，需先进行独立证明审查。
- 有限搜索不能证实 eventually 覆盖或 limsup 的全局最优性。

Proof-first 路线：

- 先对 van Doorn 构造作逐步审计，抽象其尺度递推和覆盖不变量；目标是可验证地改进上界或证明该构造族的最优常数，而非只做数值实验。
- 尝试把表示函数的总超额或平方差碰撞转化为直接针对 limsup 的全尺度下界；每一步必须写出从表示数到 A(N) 的量词和误差传递。
- 研究近临界 A(N)≤(4/π+o(1))√N 或 A(N)≤C√N 的刚性后果，寻找能排除某个 C 的可证引理。

需要验证：

- 逐页核对 van Doorn GitHub PDF 的覆盖性、所有尺度计数和常数计算，或取得可同行审阅版本。
- 访问并核对 Cilleruelo、Habsieger、Balasubramanian–Ramana 原文中的定理假设，以排除有限区间/无限补集版本差异。
- 在研究启动前再次搜索 2026 年下半年预印本、作者主页和引用网络，确认 C* 未被新工作改变。
- 若使用 Formal Conjectures，删除 sorry 并修正 eventual 条件；针对 infimum 保持性的有限修改引理应单独形式化。

### 审计限制与人工复核理由

- Erdős Problems 主页面对自动打开返回 403；其搜索索引和可访问论坛线程提供了同一当前条目内容，但这降低了直接网页审阅的完整性。
- Moser、Cilleruelo、Habsieger及 Balasubramanian–Ramana 的 DOI 元数据可核验，但本环境未取得前三篇的全文；4/π 的归因还由 2020 年同行评议的开放获取论文和当前数据库交叉支持。
- van Doorn 的 PDF 是公开但非同行评议的文件；本审计没有逐页验证其证明，故只把它作为已报告上界而非完全独立确认的定理。
- 本次检索覆盖题名、作者、精确术语、当前网页/论坛、arXiv、近期发表页及形式化仓库；未发现解决 C* 的证据，但检索不构成穷尽性或不存在性证明。

- 在启动高成本研究前，应由数学审稿人逐页复核 van Doorn 构造并取得/核对 1993、1995、2001 原始论文的精确假设和定理表述。
- 若要把状态置信度提高到 high，应再做一次针对 2026-07 之后最新预印本、引用网络和作者主页的更新检索。
- Formal Conjectures 中的 sorry 和 eventual/every-integer 条件替换必须修复；现有文件不应被引用为已验证的形式化结果。

<!-- DEEP_REVIEW:END -->
