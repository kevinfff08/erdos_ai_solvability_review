# Problem 40

## 基本信息

- 原始链接: https://www.erdosproblems.com/40
- LaTeX 页面: https://www.erdosproblems.com/latex/40
- 原始状态: `open`
- 奖金: `$500`
- 主类别: `number theory`
- 原始标签: `number theory`, `additive basis`
- 形式化状态: `yes`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

For what functions $g(N)\to \infty$ is it true that\[\lvert A\cap \{1,\ldots,N\}\rvert \gg \frac{N^{1/2}}{g(N)}\]implies $\limsup 1_A\ast 1_A(n)=\infty$?

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `26/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 已有形式化陈述，可降低语义误读风险

### 主要障碍

- 所属标签偏证明密集：number theory
- 题面含渐近/无限对象线索：\gg, limsup
- 原记录含奖金 $500，说明该题被长期视为高价值难题；这不是否定依据，但提高验证门槛。

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: additive basis
- 证明密集标签命中: number theory
- 有限/计算线索: 无
- 渐近/无限线索: \gg, limsup
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **不太可能完整解决；可在构造、等价改写和有限模型实验上显著推进，但任何正向结果覆盖任意一个发散函数 g(N) 都会触及更强形式的 Erdős-Turán 型难题。**
- 等级: `low_candidate`
- 分数: `22/100`
- 信心: `medium`
- 可能路线: 较现实的路线是让模型先把命题形式化为表示函数 r_A(n)=1_A*1_A(n) 的增长问题，分析 bounded representation 假设下 A(N) 的极限密度障碍；再用计算搜索有限集合或随机/贪心稀疏序列，寻找接近 A(N)≈N^{1/2}/g(N) 且表示数受控的模型；最后把可观察到的结构转化为条件性引理或反例候选。若依赖 formalized 版本，GPT-5.5 可辅助检查已有形式化定义、证明简单归约、验证有限计算证据。

### 支持理由

- 题目陈述清楚、短小，核心对象是加法卷积和计数函数，适合模型配合计算搜索、SAT/ILP、随机构造实验和形式化证明环境做局部验证。
- 问题已标记 formalized=yes，说明至少存在可机检的形式化入口，利于模型在定义层、边界条件和简单推论上减少误读。
- 该命题要求判断哪些发散函数 g(N) 足以强迫表示数 limsup 无界；这允许先做分层结果，例如针对很慢增长的 g、规则增长类、或附加伪随机/单调假设下的条件性推进。
- 计算工具可以系统测试有限前缀中“集合大小接近 sqrt(N)/g(N) 且最大表示数小”的极值结构，为猜测真实阈值或构造障碍提供证据。

### 主要障碍

- remarks 明确指出：即便只对某个 g(N)->infty 建立正向结论，也会推出 Erdős-Turán 猜想的正解，因此完整突破难度很高。
- 问题的量词是无限集合与任意大 N 的下界，有限计算反例或搜索只能提供启发，不能直接证明或否定最终命题。
- 可能需要深层加法组合数论方法来排除稀疏加法基中 bounded representation 的结构；这类全局结构定理通常不是当前模型可靠独立发明的强项。
- “For what functions g” 是分类型问题，不只是证明一个固定阈值；即使取得一个方向，也还需证明最优性或构造匹配反例。

### 需要的验证

- 检查 formalized 版本中卷积、limsup、渐近下界 \gg 和 g(N)->infty 的精确定义，确保与自然数学表述一致。
- 若模型提出正向证明，必须验证其是否真的只假设 A(N) \gg N^{1/2}/g(N)，而没有暗中加入 A 是基、单调密度、随机性或正密度等更强条件。
- 若模型提出反例族，需要证明该集合同时满足计数下界和表示函数有界，而不是只在有限窗口中成立。
- 所有计算搜索应给出可复现代码、参数、极值目标和证书；形式化证明应至少覆盖关键归约和无界性结论。

### 公开版思考摘要

这个问题非常适合 AI 做辅助研究：形式化定义明确，有限模型可搜索，候选构造可快速实验，局部引理也适合机检。但其核心正向结论会触及 Erdős-Turán 型长期难题，因此 GPT-5.5 级别模型更可能产出有用的实验、条件性结果、错误证明排查或形式化验证，而不是给出完整分类定理。

### 免责声明

以上是对 GPT-5.5 配合工具处理该单个问题的可行性评估，不是该 Erdős 问题的解答，也不声称给出了任何满足或否定命题的函数 g(N)。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `confirmed_open`
- 状态信心: `medium`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_40.md](../../prompts/problem_40.md)

### 状态结论

第40题仍是开放的定量分类问题。其精确定义为：刻画所有发散函数 g，使得每个满足 A(N)≫√N/g(N) 的 A⊆N 都具有无界二元有序表示函数。数据库、无评论论坛线程以及2024–2026文献均未给出解决；反而2026年的相关预印本仍将较弱的 Erdős–Turán 基问题列为开放。已知 Erdős–Rényi 型反例排除了每个至少多项式增长的 g（例如 g(N)=N^ε）。

### 当前规范陈述

令 g:N→(0,∞) 且 g(N)→∞。记 A(N)=|A∩{1,…,N}|，并令 r_A(n)=(1_A*1_A)(n)=#{(a,b)∈A²:a+b=n}，其中计数有序对。定义 P(g)：对每个 A⊆N，若存在 c>0、N₀，使一切 N≥N₀ 都有 A(N)≥c√N/g(N)，则 limsup_{n→∞}r_A(n)=∞。第40题要求刻画所有满足 g(N)→∞ 且 P(g) 成立的函数 g 所成的类别 G_*。

```text
Let g: N -> (0,infinity) satisfy g(N)->infinity. Put A(N)=|A cap {1,...,N}| and r_A(n)=(1_A*1_A)(n)=#{(a,b) in A^2:a+b=n}, where ordered pairs are counted. Say P(g) holds if, for every A subseteq N, [there exist c>0 and N_0 such that A(N)>=c sqrt(N)/g(N) for every N>=N_0] implies limsup_{n->infinity} r_A(n)=infinity. Problem 40 asks to characterize the class G_*={g:g(N)->infinity and P(g) holds}.
```

### 陈述、量词与反例审计

- 歧义严重度: `material`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 没有发现能推翻经上述量化修复后的完整分类问题的简单反例。相反，已知 Erdős–Rényi 构造（由 Erdős Problems 第39题页面汇报）对每个 ε>0 给出 A(N)≫_ε N^{1/2-ε} 且 r_A(n)≪_ε1 的集合。因此对 g(N)=N^ε，P(g) 为假；更一般地，若 N^ε=O(g(N))，同一集合满足 A(N)≫√N/g(N)，故 P(g) 为假。这是从被引构造直接推出的否定族，而不是完整分类。
- 版本变化: 未发现该题被后续论文替换或拆分为非等价正式版本。它一直作为 Erdős–Turán 猜想的加强：任何一个发散 g 的正面实例都会推出第28题。2025 年 Formal Conjectures 文件把“对单个 g 的性质”Erdos40For 和“对函数族”的 Erdos40ForSet 分开定义；主定理仍为 sorry，因此它是命题编码而非已核验的证明。

陈述问题：

- 原文没有显式量化 A，也没有规定 g 的陪域、最终正性或单调性；这些对 √N/g(N) 和“函数分类”都必要。
- 符号 ≫ 未说明常数是否依赖于 A 或 g；标准重建为：对给定 A,g，存在 c>0、N₀，使不等式对所有 N≥N₀ 成立。
- 卷积的有序/无序约定未写明。现有 Formal Conjectures 文件将对象实现为自然数上的 sumRep，与网站常用的有序卷积一致；改用无序计数只改变除对角线外的常数倍，故不改变“有界/无界”结论。
- “For what functions”是分类请求，不是单一的 yes/no 命题；可将其严格重建为确定集合 G_*，但必须把“完整刻画”与“对某个具体 g 的部分答案”区分。
- g→∞ 自动给出最终正性，但若允许任意实值函数，仍应把 g 的最终正性和极限的滤子含义写入正式目标。

需要固定的量词/约定：

- The universal quantifier is over every A subseteq N; no additive-basis or coverage assumption is imposed on A.
- g is fixed before A, and may be taken as an eventually positive real-valued function with g(N)->+infinity.
- A(N) >> sqrt(N)/g(N) means exists c>0 and N0 such that the inequality holds for all integers N>=N0; c may depend on A and g.
- The convolution counts ordered pairs: r_A(n)=#{(a,b) in A x A:a+b=n}.
- The question is a full classification of G_*, not merely the existence of one qualifying g. A theorem P(g0) for an explicit diverging g0 is nevertheless a decisive nonempty-membership result and, as the formalization verifies, implies Erdős Problem 28.

### 文献与当前边界

已核验的主要结果：

- Erdős–Rényi 型构造：对每个 ε>0，存在 A⊆N，满足 A(N)≫_εN^{1/2-ε} 且 r_A(n)≪_ε1。因而 P(N^ε) 失败；更一般，若 N^ε=O(g(N))，则 P(g) 失败。这是目前对第40题最直接的已知否定区间。该构造的本轮可核来源是 Erdős Problems 第39题的文献说明，故仍应在真正写作时追溯原始 Erdős–Rényi 论文。
- 经典 Erdős–Turán 猜想只假设 A+A 包含所有充分大的整数。计数即给出这种 A 必有 A(N)≫√N，故若 P(g) 对任何发散 g 成立，便立即推出该经典猜想。Formal Conjectures 中已有这一蕴含的机器检查代码。
- Borwein–Choi–Chu（2006，同行评审）在“所有正整数都被表示”的更强设定中排除了较小的最终上界；Li–Zhang（2026 预印本）说明其结果给出 limsup r≥8。此类有限阈值结果远弱于无界性，且并不只由第40题的密度假设触发。
- Chen（2012，同行评审）构造了一个基，使表示函数等于最小值的 n 构成密度1集合。这说明即使基条件成立，不能期待表示函数在大多数 n 上增长；必须精确针对 limsup。
- Jain–Pham–Sawhney–Zakharov（2024 预印本，后见 Cambridge 期刊页）构造了显式经济基 A+A=N，表示函数为 N^{o(1)}。这改善了显式构造，但没有有界表示函数，因而不触及第40题的结论。

最近相关工作：Li–Zhang《An Improvement of Konstantoulas' Density Constant》（arXiv:2605.30922，2026-05-29，预印本）是本轮检索到的最新直接讨论表示函数阈值的工作；它以生成函数、Abel 密度和表示层级为工具，给出若干固定下界，但明确仍称经典猜想开放。对第40题本身，未检索到2023–2026年可核的正面或反面新定理。

剩余核心：确定 G_*。已知 G_* 不包含任何最终至少为 N^ε（某固定 ε>0）的函数；另一方面，尚无已核验证据表明任何一个发散函数属于 G_*。尤其未知是否存在极慢发散的 g（如迭代对数尺度）使 P(g) 成立，也未知临界尺度或 G_* 是否为空。

已使用方法：

- Sidon/有界表示函数构造与其稠密度：用于制造 P(g) 的反例；需区分“沿某子序列稀疏”与“对所有充分大 N 的统一下界”。
- 生成函数、Abel 密度和 L1/L2 估计：Li–Zhang 对经典基问题的固定表示数阈值结果。
- 有限模型/模循环群中的有界表示基：适合作为结构启发，但 Z 或 Z/mZ 的结论不能直接移至单侧半群 N。
- 概率法与显式经济基构造：说明 A+A=N 与 N^{o(1)} 表示数可兼容，但对有界性没有结论。
- 形式化定义与归约：可用 Lean 先锁定量词、卷积约定和“P(g)⇒第28题”的归约，防止证明目标漂移。

争议或不确定性：

- Smpokos 的 OSF 预印本声称证明经典 Erdős–Turán 猜想，但没有同行评审或形式化验证；其存在不能改变开放状态。
- 原题引用 Er95、Er97c，但本轮无法从公开索引直接取得这两项的完整书目信息及原文页码；应由人工或图书馆核验原始措辞。
- Erdős–Rényi 构造的反例性结论在数据库相邻题目的说明中出现且与问题结构吻合，但本轮未直接检查其原始论文。因此它足以指导审计，不应在正式论文中替代原始引文。
- 网站的“Formalised statement? Yes”只表示陈述已编码；40.lean 主定理含 sorry，不能误报为机器验证解决。

### 证据来源

- [Erdős Problems — Problem 40](https://www.erdosproblems.com/40) — Thomas F. Bloom (database maintainer), date unknown; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 页面将第40题列为 OPEN，给出原题、Erdős 1995/1997c 引文，并说明任何发散 g 的正面结果都会推出第28题；页面同时提示其状态并非文献穷尽保证。
- [40 Discussion Thread — Erdős Problems](https://www.erdosproblems.com/forum/thread/40) — Thomas F. Bloom (platform); no commenter, date unknown; `forum`, `informal_claim`, directness=`direct`, reliability=`medium`. 线程重现 OPEN 状态与原题，并明确显示 0 comments、没有已声称的部分或完整解，因此没有需要核验的论坛解答。
- [FormalConjectures/ErdosProblems/40.lean](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/40.lean) — Formal Conjectures Authors / Google DeepMind repository contributors, date unknown; `formalization`, `formalized_artifact`, directness=`direct`, reliability=`high`. 给出 Erdos40For(g) 的量词结构和 Erdos40ForSet；文件中的主定理 erdos_40 与 answer 均含 sorry，故仅形式化陈述与“全体 g 的正解推出第28题”的已检查归约，绝非第40题证明。
- [Erdős Problems bibliography search for Er95](https://www.erdosproblems.com/search_bib/Er95/yes) — Thomas F. Bloom (database maintainer), date unknown; `secondary_index`, `database_record`, directness=`indirect`, reliability=`medium`. 第40题条目明确由 [Er95][Er97c] 引用；同一数据库还汇报 Erdős–Rényi 的稠密有界表示函数构造。
- [An Improvement of Konstantoulas' Density Constant](https://arxiv.org/abs/2605.30922) — Huixi Li, Zihan Zhang, 2026-05-29; `preprint`, `preprint`, directness=`indirect`, reliability=`high`. 仍将 Erdős–Turán 猜想称为开放；证明若 E=N\(A+A) 的上密度小于 7/32，则 limsup r_A>5，并证明 D(E)<1/2 时 limsup r_A>3。该工作不处理第40题只给出 A(N) 下界而不要求 A+A 稠密的设定。
- [An explicit economical additive basis](https://arxiv.org/abs/2405.08650) — Vishesh Jain, Huy Tuan Pham, Mehtaab Sawhney, Dmitrii Zakharov, 2024-05-14; `preprint`, `preprint`, directness=`indirect`, reliability=`high`. 构造显式 A⊆N，A+A=N 且表示数为 N^{o(1)}；引言仍把“把 Erdős 随机构造中的 log N 因子替换为常数”称为主要开放问题。它显示可得到极经济基，但并未给出有界表示函数或第40题的正面结果。
- [On the Erdős–Turán conjecture](https://www.numdam.org/articles/10.1016/j.crma.2012.10.022/) — Yong-Gao Chen, 2012-11-01; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 证明存在 A 使表示函数等于其最小值的 n 的集合密度为 1，同时列出原始 Erdős–Turán 1941 论文及相关文献；并非原猜想或第40题的解决。
- [An old conjecture of Erdős–Turán on additive bases](https://doi.org/10.1090/S0025-5718-05-01777-1) — Peter Borwein, Stephen Choi, Frank Chu, 2006-01-01; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 在“每个正整数都可表示”的较强基设定中，给出计算密集的有限阈值排除结果；2026 Li–Zhang 文献明确概述其为 limsup r(n)≥8 的改进。它不是无界性的证明。
- [Generalized additive bases, Konig's lemma, and the Erdos-Turan conjecture](https://arxiv.org/abs/math/0302155) — Melvyn B. Nathanson, 2003-02-13; `preprint`, `preprint`, directness=`indirect`, reliability=`high`. 精确陈述经典二阶基猜想，并给出以 König 引理将广义问题等价为有限集合问题的框架；不解决第40题。
- [A Proof of the Erdos-Turan Conjecture on Asymptotic Additive Bases](https://sciety.org/articles/activity/10.31219/osf.io/mxgbu) — Konstantinos Smpokos, 2024-06-20; `preprint`, `informal_claim`, directness=`indirect`, reliability=`low`. 发现一项声称证明经典猜想的 OSF 预印本；页面显示没有 evaluations，且未见同行评审、正式验证或被权威问题库采纳。不能据此关闭第28题或更强的第40题。

### 完成标准

- 肯定出口: A complete affirmative classification supplies a precisely defined class C of eventually positive functions g with g(N)->infinity and proves, for every such g, P(g) iff g belongs to C. At minimum, an affirmative membership result for a named diverging g0 requires a proof that every A with A(N)>=c sqrt(N)/g0(N) eventually has unbounded ordered representation function; it must quantify uniformly over all A and all admissible constants c.
- 否定出口: A complete negative classification supplies the complementary rigor: for every diverging eventually positive g outside the asserted class, an A_g subseteq N and a finite C_g with A_g(N)>>sqrt(N)/g(N) and r_{A_g}(n)<=C_g for every n (or eventually every n). In particular, proving G_* is empty would be a complete negative answer; for a named g0, such an A_g0 is a decisive disproof of P(g0).

不构成完成：

- Showing only that A+A contains all sufficiently large integers, or proving the classical Erdős–Turán conjecture under an extra hypothesis not implied by the density condition.
- A construction whose counting lower bound holds only on a subsequence of N, or with an implicit constant that decays with N.
- A bound for unordered representations without explicitly translating it to the ordered convolution convention.
- A finite search over initial segments without an infinite extension theorem or a certified obstruction.
- A claim based only on a finite cyclic group, Z, or a random heuristic; the target is the one-sided set N and an all-large-N lower bound.
- Proving P(g) for one g and presenting it as a characterization of all functions g.

正确性陷阱：

- The direction of monotonicity is easy to reverse: if g1=O(g2), then the hypothesis for g1 is stronger, so P(g2) implies P(g1); a counterexample for g1 also refutes P(g2).
- The lower bound A(N)>>sqrt(N)/g(N) is required eventually for every N, not merely infinitely often.
- A bounded representation function includes diagonal pairs and ordered-pair doubling; all constants must respect the chosen convention.
- The density hypothesis alone does not say A+A is cofinite or even has positive density; results for additive bases cannot be applied without separately proving their hypotheses.
- g(N)->infinity must be interpreted along integers and g must be eventually positive; irregular/nonmonotone g require care in any claimed threshold comparison.
- Do not infer a solution from the Formal Conjectures file: its open theorem explicitly contains sorry.

### 更新后的 AI 可解答性

- 等级: `low_candidate`
- 分数: `12/100`
- 信心: `medium`
- 结论: 这是定义清晰但极难的开放分类问题；适合以严谨的局部定理、反例区间或可验证引理为目标，而不适合预期短期端到端解决。

支持理由：

- 量词、卷积和渐近条件可被精确形式化，且已有 Lean 陈述可作为规范锚点。
- 已存在清楚的反例区域（多项式级 g）与一个重要的未知慢发散区域，因而可提出可证伪的中间命题。
- 任何具体发散 g 的正面结果都有重大价值，并自动推出经典第28题。

主要障碍：

- 正面结果会解决长期未解的 Erdős–Turán 猜想，故没有理由把一般情形视为近期可解。
- 现有最直接方法对覆盖稀疏度或固定表示阈值施加条件，但第40题只控制 A 的计数函数，缺少 A+A 覆盖信息。
- 有限计算不能覆盖无穷的“所有 A、所有 N”量词；随机/模群构造与单侧自然数问题之间存在实质鸿沟。

Proof-first 路线：

- 先证明函数类的偏序与反例传递引理，并把 Erdős–Rényi 构造所排除的完整函数族写成严谨命题。
- 针对一个明确的极慢发散候选 g，寻求“有界 r_A 导致 A(N)=o(√N/g(N))”的结构性矛盾；每一步须保持 all-large-N 控制。
- 检验生成函数/Abel 密度方法能否仅由 A(N) 下界推出 A+A 的可用覆盖或能量结论；若不能，应形成明确的障碍定理而非强行套用。
- 把任何候选归约先在 Formal Conjectures 定义下表述，以机器可检查方式确认卷积与渐近量词。

需要验证：

- 核验 Er95 和 Er97c 的完整书目信息、原文措辞及其是否含有未被数据库摘录的部分结果。
- 直接追溯 Erdős–Rényi 有界表示构造的原始来源和其对所有大 N 的定量常数，从而替换当前二手索引。
- 继续监测 2026 年后续版本、期刊接受记录及专家评审，尤其是任何宣称解决经典猜想的预印本。
- 若使用 Li–Zhang 结果，逐式核验其 D(E) 与 Abel 密度条件，不能把它误用为 A(N) 下界。

### 审计限制与人工复核理由

- 本审计按要求进行了页面、论坛、原始/相关论文、arXiv、近期工作及形式化仓库的定向检索；但网络检索不能逻辑证明不存在未索引的解决方案。
- 问题页的完整 HTML 与 LaTeX 端点在浏览器中有 403/内部错误；使用了搜索索引、论坛镜像和 Formal Conjectures 文件重建原文及量词。
- Er95 与 Er97c 的完整题名、出版信息和原文段落未能在本轮公开检索中直接取得；相应历史归属应由人类进一步书目核验。
- Erdős–Rényi 反例性结果本轮来自相邻题目的数据库文献说明而非原始论文全文，因此已标为二手证据并列入后续核验。

- 应核验 Er95/Er97c 和 Erdős–Rényi 原始文献，特别是反例构造所满足的“所有充分大 N”均匀下界。
- 若研究代理准备声称发现任意一个 P(g) 的正面实例，必须进行专家级证明审查，因为这将蕴含经典 Erdős–Turán 猜想。
- 存在未经评审的经典猜想“证明”预印本；任何后续研究都应审阅其漏洞或独立验证，而不能依赖其结论。

<!-- DEEP_REVIEW:END -->
