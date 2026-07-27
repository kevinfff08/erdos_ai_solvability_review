# Problem 12

## 基本信息

- 原始链接: https://www.erdosproblems.com/12
- LaTeX 页面: https://www.erdosproblems.com/latex/12
- 原始状态: `open`
- 奖金: `no`
- 主类别: `number theory`
- 原始标签: `number theory`
- 形式化状态: `yes`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

Let $A$ be an infinite set such that there are no distinct $a,b,c\in A$ such that $a\mid (b+c)$ and $b,c>a$. Is there such an $A$ with\[\liminf \frac{\lvert A\cap\{1,\ldots,N\}\rvert}{N^{1/2}}>0?\]Does there exist some absolute constant $c>0$ such that there are always infinitely many $N$ with\[\lvert A\cap\{1,\ldots,N\}\rvert<N^{1-c}?\]Is it true that\[\sum_{n\in A}\frac{1}{n}<\infty?\]

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `26/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- 题面或备注出现有限对象/计算线索
- 已有形式化陈述，可降低语义误读风险

### 主要障碍

- 所属标签偏证明密集：number theory
- 题面含渐近/无限对象线索：\gg, \ll, density, infinitely many, liminf

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: number theory
- 有限/计算线索: finite, finitely
- 渐近/无限线索: \gg, \ll, density, infinitely many, liminf, prime
- 构造/存在性线索: construct, does there exist, is there

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **中等候选。按给定 JSON 的备注，前三个问法中前两个已经由构造性结果否定/肯定地解决，真正仍开放的是是否存在满足条件且倒数和发散的集合 A，或反过来证明所有这类 A 的倒数和收敛。GPT-5.5 级别模型配合计算、形式化证明和反例搜索，较有希望完成已知构造的验证、形式化、简化和参数优化，也可能显著推进第三问的候选构造筛选；但直接解决第三问仍有明显难度。**
- 等级: `medium_candidate`
- 分数: `62/100`
- 信心: `medium`
- 可能路线: 最现实路线是把问题拆成“局部禁止三元组约束”的有限模型和“块构造/稀疏同余类构造”的无限提升。模型可用 SAT/ILP/CP-SAT 搜索有限高密度样本，抽取可迭代的块结构；再用符号推导或 Lean/Isabelle 形式化验证该结构确实避免 a|(b+c)。若目标是第三问，则应重点寻找倒数和发散的分块构造，控制每个块的贡献约为非可和序列，同时保证跨块之间的整除冲突被快速增长、同余隔离或素因子结构消除。

### 支持理由

- 问题具有清晰的可计算有限版本：给定上界 N，可以把禁止条件转化为有限约束，适合用 CP-SAT、MILP、局部搜索或反例搜索产生数据。
- 给定备注已显示存在强构造路线：Erdos-Sarkozy 的稀疏同余块、平方素数例子、Elsholtz-Planitzer 构造，以及 DeepMind 后续构造，说明问题不是纯不可计算型，而是构造和验证并重。
- 形式化状态为 yes，意味着至少部分定义和结论适合机器检查；GPT-5.5 可在形式化环境中帮助补齐证明脚手架、检查边界条件和避免跨块冲突遗漏。
- 第一问和第二问在备注中已有解决方向，因此 AI 的近期价值可以集中在复现、压缩、验证和参数改进，而不必从零处理全部开放难题。
- 第三问与倒数和发散相关，天然适合用分块密度贡献、增长率和冲突概率估计来做程序化实验和符号不等式验证。

### 主要障碍

- 真正开放的第三问可能需要新的结构性思想：既要让 A 足够厚以使倒数和发散，又要全局避免所有跨尺度的 a|(b+c) 冲突。
- 有限搜索得到的高密度样本未必能提升为无限构造；局部最优模式可能依赖 N，缺少可证明的递归或同余机制。
- 跨块冲突是核心技术风险：即使每个块内部安全，较小 a 整除较大 b+c 的情形会产生大量全局约束。
- 证明倒数和发散需要比已有接近 N/(log N)^{O(log log log N)} 的计数下界更精细的全尺度控制；只在稀疏 N 上很厚通常不足够。
- 如果尝试证明所有此类 A 倒数和收敛，需要强得多的全局稀疏性定理，而备注中的已知构造表明简单密度零或幂次稀疏界不够。

### 需要的验证

- 将禁止条件精确定义为：不存在互异 a,b,c in A 且 b,c>a 且 a | b+c，并在所有构造验证中检查互异性和大小条件。
- 对任何候选无限构造，分别验证块内、相邻块、远距离跨块三类冲突。
- 若声称倒数和发散，需要给出全体 N 或全体块的可和性/不可和性证明，而不仅是某些 N 上的计数下界。
- 用有限搜索复现小 N 极值或高密度样本，检查是否与候选构造的局部统计一致。
- 对参数增长条件进行机器代数或形式化证明，确保“足够快增长”等语句被替换为明确递归不等式。

### 公开版思考摘要

这个问题对 AI 不是低价值候选，因为它有明确约束、可搜索有限版本、已有构造传统和形式化入口。按给定备注，前两问已经由构造性进展解决，剩余关键是倒数和是否可能发散。GPT-5.5 级别系统最可能的贡献是构造验证、有限模型搜索、参数优化和形式化证明，而不是短期内直接完成第三问。综合看，它是一个中等候选：有可操作推进路径，但最终开放部分仍需要实质性数学新意。

### 免责声明

以上只是 AI 可推进性评估，不是该 Erdős 问题的解答，也未声称解决剩余开放的倒数和问题。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `revised_open`
- 状态信心: `high`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_12.md](../../prompts/problem_12.md)

### 状态结论

该数据库条目原含三个问题。2026 年 4 月的可审查 Lean 形式化工件及其附带的人类可读论证已确认：第一个问题答案为“是”，第二个问题答案为“否”。因此原始复合条目不能再整体标为 open；唯一明确存留的开放核心是第三问：每个具有 Property P 的集合的倒数和是否必收敛。

### 当前规范陈述

令 A 为正整数集合。若不存在两两不同的 a,b,c∈A，使 b>a、c>a 且 a 整除 b+c，则称 A 具有 Property P。原条目含三个问题。现已闭合的部分为：(i) 存在无限 Property-P 集合 A，使 liminf_{N→∞}|A∩[1,N]|/√N>0；(ii) 不存在绝对常数 c>0 使每个无限 Property-P 集合 A 都有无穷多个 N 满足 |A∩[1,N]|<N^(1-c)。当前唯一存留目标是：对每个无限 Property-P 集合 A，是否都有正项级数 ∑_{n∈A}1/n 收敛？把有限 A 也纳入全称量词不改变该命题，因为其倒数和显然有限。

```text
Let A be a subset of the positive integers. Say that A has Property P if there do not exist pairwise distinct a,b,c in A with b>a, c>a, and a divides b+c. The original record asked three questions. Parts (i) and (ii) are now closed: (i) there exists an infinite Property-P set A such that liminf as N tends to infinity of |A∩[1,N]|/sqrt(N) is positive; (ii) it is false that there is an absolute c>0 such that every infinite Property-P set A has infinitely many N with |A∩[1,N]|<N^(1-c). The current residual target is: prove or disprove that, for every infinite Property-P set A, the positive series sum over n in A of 1/n converges. Finite A may harmlessly be included in the universal quantifier because its reciprocal sum is finite.
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 未找到能使第三问字面命题失效的简单 Property-P 构造。已验证的高计数构造只给出 A(N)=N^(1-o(1)) 型下界（或较早的平方根量级下界）；这些下界本身并不推出倒数和发散。针对原复合陈述，前两问已有经审查的肯定/否定构造，属于解答而非“简单反例”。
- 版本变化: 1970 年 Erdős–Sárközy 证明任一 Property-P 集合密度为 0，并构造在无穷多个尺度上可任意缓慢趋零密度的例子。2017 年 Elsholtz–Planitzer 改进了全尺度平方根量级下界。2026 年 4 月，DeepMind Formal Conjectures 的可检查 Lean 工件及 Erdős Problems 讨论线程给出第 (i) 问肯定、第 (ii) 问否定；数据库页面仍把整条记录标为 OPEN，是因为第 (iii) 问未解。

陈述问题：

- 输入把三个逻辑上独立的问题并列成一个“open”记录；截至 2026-04，前两问已有形式化证明，只有第三问仍是开放目标。
- “there are always infinitely many N”必须明确为：存在一个绝对 c>0，使对每个满足 Property P 的（无限）A，满足严格不等式的 N 构成无限集。
- Property P 中“distinct”适用于 a,b,c 全部两两不同；b,c>a 是严格不等式。
- 倒数和应理解为正项子级数，故不存在条件收敛或排列约定问题。

需要固定的量词/约定：

- Part (i): exists an infinite A with Property P such that liminf_{N→∞} A(N)/sqrt(N)>0, where A(N)=|A∩{1,...,N}|.
- Part (ii): the proposed assertion is exists c>0 such that for every infinite Property-P A, the set of N with A(N)<N^(1-c) is infinite. Its verified negation is: for every c>0, some Property-P A has only finitely many such N; equivalently, for that A, A(N)>=N^(1-c) for all sufficiently large N.
- Residual part (iii): for every infinite Property-P A, the nonnegative series sum_{n∈A} 1/n is finite.

### 文献与当前边界

已核验的主要结果：

- Erdős–Sárközy（1970，同行评议）证明每个 Property-P 集合的自然密度为 0；但对任意 f(x)→∞，存在 Property-P 集合在无穷多个 N 满足 A(N)>N/f(N)。这只控制稀疏子序列上的计数，不能决定倒数和。
- 经典例子 A={p²:p≡3 mod 4 为素数} 给出 liminf A(N)log N/√N>0。
- Elsholtz–Planitzer（2017，同行评议）给出全尺度下界 A(N)≫√N/[√log N(loglog N)²(logloglog N)²]，用素因子为 3 mod 4 的平方及分层指示因子保证 Property P。
- Schoen（2001）及 Baier（2004）仅在 A 两两互素时证明无穷多 N 的上界；Baier 的形式是 A(N)≪N^(2/3)/log N。不能将互素性默认为原问题条件。
- Bedert（2023，arXiv 预印本）解决有限版本的极值界 floor(n/3)+1；此结论与无限集的调和级数收敛性不等价。
- 2026 年的 Lean 工件构造了第 (i) 问的 √N-liminf 正例，以及对每个 c>0 的第 (ii) 问反例；讨论线程还说明可达到对所有充分大 N 的 N^(1-ε) 型计数下界（ε 任意但构造可依赖于 ε）。

最近相关工作：直接改变原条目状态的最新可检查工作是 2026-04 的 Formal Conjectures/DeepMind 形式化第 (i)、(ii) 问。针对完全相同 Property P 的最近传统论文检索到 Bedert 2023，但它解决的是有限极值版本而非倒数和；截至审计日，没有发现第三问的同行评议解答、预印本解答或可检查反例。

剩余核心：证明“任意无限 Property-P 集合 A 的 ∑_{n∈A}1/n 收敛”，或构造一个无限 Property-P 集合 A 使该级数发散。第 (i)、(ii) 的密集构造均不能单独推出后者，因为 N^(1-o(1)) 的计数下界仍可能与收敛倒数和相容。

已使用方法：

- 分块构造：在窄区间内放置集合，并用不同模数及中国剩余定理消除跨块可整除关系。
- 局部结构：若同一窄块中的 b+c 只能等于 2a，则可借助无三项等差数列集合；讨论中的后续简化指出严格条件 b,c>a 已排除 b+c=2a，因此可进一步简化。
- 以 p≡3 mod 4 的素因子和平方和二次剩余障碍来证明 Property P。
- 在两两互素附加假设下，使用算术大筛与均值估计获得计数上界。

争议或不确定性：

- Erdős Problems 页面和讨论认为第三问未解，但数据库明确声明其开放标签只是维护者的当前认识；本审计未发现相反的可检查来源，不能把检索失败当作逻辑证明。
- 第 (i)、(ii) 的关闭依据是可检查 Lean 工件及官方 Formal Conjectures 页面，而非传统同行评议论文。正式采用前应由人工在固定提交、依赖锁定环境中重新编译，并检查项目对 sorry/公理的完整性策略。
- 讨论中将第 (ii) 构造含混地归于 Cilleruelo；讨论作者明确说未找到对应的既有文献直接解答。因此不应把 2026 解答归作 Cilleruelo 已发表定理。

### 证据来源

- [Erdős Problems — Problem 12](https://www.erdosproblems.com/12) — Thomas F. Bloom (database owner/editor), 2026-04-08; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 当前数据库页明确称前两问已由 DeepMind 构造解决，第三问“是否存在倒数和发散的 A”仍未知；同时记录 1970、2001、2004、2017 的背景结果。
- [12 Discussion Thread — Erdős Problems](https://www.erdosproblems.com/forum/thread/12) — Terence Tao, Thomas Bloom, Nat Sothanaphan, GTsoukalas, and others, 2026-04-09; `forum`, `informal_claim`, directness=`direct`, reliability=`medium`. 讨论提供了第 (i)、(ii) 问的具体人类可读构造、量词结论及通往 Lean 工件的链接；它本身是非同行评议讨论，故结论需与形式化工件合读。
- [Formal Conjectures theorem: Erdos12.erdos_12.parts.i](https://google-deepmind.github.io/formal-conjectures/theorem/?name=Erdos12.erdos_12.parts.i) — Google DeepMind Formal Conjectures project, date unknown; `formalization`, `formalized_artifact`, directness=`direct`, reliability=`high`. 官方 Formal Conjectures 页面登记第 (i) 问为已完成形式化定理；对应代码给出一个 Property-P 集合且其计数函数除以 √N 的 liminf 为正。
- [FormalConjectures/ErdosProblems/12.lean — proof of part (i)](https://github.com/mo271/formal-conjectures/blob/8d872b465955e46e2d28bc165d186ea41fd0da9e/FormalConjectures/ErdosProblems/12.lean) — DeepMind prover-agent contribution, hosted in Formal Conjectures repository fork, date unknown; `formalization`, `formalized_artifact`, directness=`direct`, reliability=`high`. 可审查 Lean 源码将 erdos_12.parts.i 标作 research solved，并由 exists_dense_good_set 供给存在性结论。
- [Formal Conjectures theorem: Erdos12.erdos_12.parts.ii](https://google-deepmind.github.io/formal-conjectures/theorem/?name=Erdos12.erdos_12.parts.ii) — Google DeepMind Formal Conjectures project, date unknown; `formalization`, `formalized_artifact`, directness=`direct`, reliability=`high`. 官方 Formal Conjectures 页面登记第 (ii) 问的否定结论为已完成形式化定理。
- [FormalConjectures/ErdosProblems/12.lean — proof of part (ii)](https://github.com/mo271/formal-conjectures/blob/118a6a60df73a9f47d6c89f3cdb3786eaa2e8d0a/FormalConjectures/ErdosProblems/12.lean) — DeepMind prover-agent contribution, hosted in Formal Conjectures repository fork, date unknown; `formalization`, `formalized_artifact`, directness=`direct`, reliability=`high`. 可审查 Lean 源码将 erdos_12.parts.ii 标作 research solved；其引理 cilleruelo_dense_good_set 对任意 c>0 构造一个反驳该统一上界的 Property-P 集合。第三问在同一版本中仍为 answer(sorry) 且标作 research open。
- [On the Divisibility Properties of Sequences of Integers](https://londmathsoc.onlinelibrary.wiley.com/doi/pdf/10.1112/plms/s3-21.1.97) — P. Erdős and A. Sárközi, 1970-07; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 原始同行评议论文及其书目信息；后续资料一致归因于该文：Property-P 集合必须密度为 0，并给出在无穷多个尺度上密度任意缓慢趋零的构造。
- [On Erdős and Sárközy’s sequences with Property P](https://link.springer.com/article/10.1007/s00605-016-0995-9) — Christian Elsholtz and Stefan Planitzer, 2017-03; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 构造 Property-P 集合 S，满足 S(x) ≫ √x/[√log x (log log x)^2 (log log log x)^2]；文章也明确采用与本题一致的 Property P 定义。
- [A Note on P-sets](https://math.colgate.edu/~integers/e13/e13.pdf) — Stephan Baier, 2004-10-08; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 对元素两两互素的 P-set，改进 Schoen 的无穷多 N 上界至 (3+ε)N^(2/3)/log N；该受限结果不能解决无附加条件的第三问。
- [On a problem of Erdős and Sárközy about sequences with no term dividing the sum of two larger terms](https://arxiv.org/abs/2301.07065) — Benjamin Bedert, 2023-01-17; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 解决了相关但不同的有限极值问题：充分大 n 时，[n] 中 Property-P 子集的最大大小为 floor(n/3)+1；不涉及无限集合的倒数和问题。
- [FormalConjectures.Subsets.FC100OpenSet1](https://firsching.ch/formal-conjectures/src/FormalConjectures/Subsets/FC100OpenSet1/) — Formal Conjectures project, date unknown; `formalization`, `formalized_artifact`, directness=`direct`, reliability=`medium`. 该项目当前公开的 open-problem 子集仍列出 Erdos12.erdos_12.parts.iii，独立佐证第三问在该项目记录中尚未关闭。

### 完成标准

- 肯定出口: Prove that for every infinite A⊆N with Property P, the nonnegative series Σ_{n∈A}1/n converges. The proof must cover all Property-P sets, without silently imposing pairwise coprimality, a block construction, or a density regularity hypothesis.
- 否定出口: Give one explicitly defined infinite A⊆N with Property P and prove Σ_{n∈A}1/n=∞. Both the no-divisibility condition for all pairwise distinct triples and a rigorous divergence argument are required.

不构成完成：

- A construction with A(N)≥N^(1-ε) for every fixed ε>0, or A(N)=N^(1-o(1)), without a proof that its reciprocal sum diverges.
- A density-zero theorem or a lower bound attained only at infinitely many scales.
- A proof for pairwise-coprime Property-P sets only.
- A finite extremal result such as max{|A|:A⊆[N] has Property P}=floor(N/3)+1.
- Numerical checks up to any finite cutoff, or an informal extrapolation from block constructions.

正确性陷阱：

- Quantify over all infinite Property-P sets in an affirmative proof; finite sets are harmless but must not replace the target class.
- Check a,b,c are pairwise distinct and b>a,c>a. In particular, b+c=2a is incompatible with b,c>a, so arguments importing 3-AP obstructions must not overlook this simplification.
- For a proposed counterexample, verify cross-block triples, not just triples within a block.
- Do not infer divergence from near-linear subpower losses in A(N); apply a valid partial-summation or dyadic-shell calculation.
- Do not infer convergence merely from natural density zero.
- Keep strict versus non-strict inequalities in part (ii) separate from the residual harmonic-sum question.

### 更新后的 AI 可解答性

- 等级: `low_candidate`
- 分数: `14/100`
- 信心: `medium`
- 结论: 当前目标定义清楚、可证伪，但缺少对一般 Property-P 集合的有效全局结构定理；以现有公开进展衡量，适合作为长期证明导向研究而非高概率短期 AI 攻关题。

支持理由：

- 残余问题是清晰的二分命题，肯定与否定均可由可审计证明完成。
- 2026 年形式化构造和既有分块方法提供了明确的结构样本及可形式化的局部引理。
- 已有结果显示计数密度可远高于传统平方根屏障，因此不应把问题误化为简单计数上界。

主要障碍：

- 一般 Property-P 集合无需两两互素，Baier/Schoen 型大筛上界不能直接使用。
- 极高但仍可使调和和收敛的计数下界表明单纯优化密度构造未必产生反例。
- 肯定方向可能需要新的逆结构或跨尺度控制；当前文献没有给出足以决定调和和的通用上界。

Proof-first 路线：

- 尝试把 Property P 转化为按尺度的模结构、可整除图或加法结构约束，并证明足以使各 dyadic 壳层的调和质量可求和。
- 独立探索非传统分块构造是否能在每个 dyadic 壳层保留不可求和的调和质量，同时由可验证模不变量排除所有跨层三元组。
- 将 2026 构造抽象成必要条件与充分条件，严查哪些参数选择必然导致调和质量可和。

需要验证：

- 在固定版本的 Lean/Mathlib 环境中复编译第 (i)、(ii) 形式化工件，并审计是否有未允准的 sorry、axiom 或未固定依赖。
- 对第三问再做一次 MathSciNet/zbMATH/作者主页与 arXiv 的人工检索，重点覆盖 2026 年后续版本。
- 任何声称倒数和发散的构造必须给出 dyadic 壳层或分部求和的明确下界，而非仅报 counting function。

### 审计限制与人工复核理由

- 本审计使用了公开网页、出版商页面、arXiv、论坛及公开 Lean 工件；未能在本环境中完整重编译 Lean 项目，故形式化关闭结论虽有很强证据，仍建议人工复编译。
- 没有访问 MathSciNet、zbMATH 的受限全文索引或所有引用文献的全文；“第三问仍开放”是高置信度文献状态判断，不是对不存在未知证明的逻辑证明。
- 2026 形式化解答尚未发现对应同行评议论文；其数学内容、依赖和无 sorry 策略需要独立形式化审计。
- Bedert 2023 的有限版本与本题相邻但不等价，已刻意不当作第三问进展。

- 应在固定提交和锁定依赖下独立编译第 (i)、(ii) Lean 文件，并审计其依赖链中的 sorry/axiom 政策，之后再把复合记录的数据库状态正式改为 revised_open。
- 应由具备数学数据库访问权限的审稿人补做 2026-04 至 2026-07 的 MathSciNet/zbMATH/引用追踪，以排除未被一般网页检索收录的第三问新进展。

<!-- DEEP_REVIEW:END -->
