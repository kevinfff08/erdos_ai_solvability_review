# Problem 32

## 基本信息

- 原始链接: https://www.erdosproblems.com/32
- LaTeX 页面: https://www.erdosproblems.com/latex/32
- 原始状态: `open`
- 奖金: `no`
- 主类别: `number theory`
- 原始标签: `number theory`, `additive basis`
- 形式化状态: `yes`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

Is there a set $A\subset\mathbb{N}$ such that\[\lvert A\cap\{1,\ldots,N\}\rvert = o((\log N)^2)\]and such that every large integer can be written as $p+a$ for some prime $p$ and $a\in A$?

Can the bound $O(\log N)$ be achieved? Must such an $A$ satisfy\[\liminf \frac{\lvert A\cap\{1,\ldots,N\}\rvert}{\log N}> 1?\]

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `23/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 已有形式化陈述，可降低语义误读风险

### 主要障碍

- 所属标签偏证明密集：number theory
- 题面含渐近/无限对象线索：\ll, liminf, o(, prime, primes

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: additive basis
- 证明密集标签命中: number theory
- 有限/计算线索: 无
- 渐近/无限线索: \ll, liminf, o(, prime, primes
- 构造/存在性线索: is there

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5 with computational/formalization/literature tools`
- 结论: **不太可能在一次研究周期内完整解决前两个开放问题，但有较现实机会显著推进“可验证的构造框架、随机/贪心模型实验、已有证明形式化、以及下界部分复核”。若目标是证明存在 o((log N)^2) 的完全加性补集，候选性偏低；若目标是改进常数、建立条件性结果或严格验证 Ruzsa 型下界，则候选性中等。**
- 等级: `low_to_medium_candidate`
- 分数: `38/100`
- 信心: `medium`
- 可能路线: 最可能的路线不是直接猜出最终构造，而是把问题转化为 primes 的稠密覆盖/命中集问题：复核 Erdős 的随机构造，形式化 Ruzsa 的 liminf 下界；用素数分布估计、随机稀疏集、分块选择和 Lovasz local lemma/容斥/大筛式工具尝试把全体整数覆盖从 (log N)^2 降到 o((log N)^2)。计算上可测试有限区间的最小补集、随机贪心覆盖和例外集结构，以寻找可证明的分块策略。

### 支持理由

- 问题已有明确的经典上界、几乎处处版本和下界，给模型提供了可复核的证明骨架，而不是完全无结构的开放问题。
- 第三问在给定材料中已由 Ruzsa 解决，GPT-5.5 级别模型配合文献检索和形式化工具有较好机会重建、检查并形式化该部分。
- 前两个问题与随机构造、覆盖引理、素数定理及筛法相关，适合模型做证明路线枚举、参数优化、有限实验和反例搜索。
- 计算实验可对有限 N 的最优或近优 A 进行整数规划/贪心搜索，帮助识别是否存在 O(log N) 级别的局部模式或不可避免障碍。

### 主要障碍

- 核心难点是“所有充分大整数”而非“几乎所有整数”；极少数未覆盖点通常会破坏随机稀疏构造。
- 要从 (log N)^2 降到 o((log N)^2) 需要比标准一阶随机覆盖更强的相关性控制，涉及素数在大量平移集合中的联合分布。
- O(log N) 若成立会接近 Ruzsa 下界量级，需要极精细的构造；若不成立则需要新的全局下界机制，单靠有限搜索很难证明。
- 形式化证明工具可验证局部论证，但目前对解析数论中复杂筛法、渐近估计和文献级证明的端到端形式化成本较高。

### 需要的验证

- 检索并核对 Erdős 1954、Lorentz 1954、Wolke 1996、Kolountzakis 1996、Ruzsa 1998c 的原始证明，确认现有边界和未解决部分。
- 把 Erdős 的 O((log N)^2) 构造拆成可机器检查的引理，明确瓶颈参数来自哪里。
- 实现有限区间覆盖优化：给定 N，求最小 A 使区间尾部均可由 p+a 表示，并比较 log N、log N log log N、log^2 N 尺度。
- 测试随机分块/贪心算法的例外集密度和聚集方式，判断是否可能转化为可证明的二阶段修补法。
- 若提出新构造，需要独立验证所有素数分布假设，区分无条件结果、GRH 条件结果和启发式结果。

### 公开版思考摘要

这个问题对 AI 的可攻性主要来自其结构清楚：它是素数集的加性补集问题，已有 O((log N)^2) 的完全覆盖构造、接近 O(log N) 的几乎处处覆盖结果，以及已知的 liminf 下界。因此模型可以有效做文献复核、证明重构、形式化和计算探索。但真正开放的部分要求把覆盖从几乎所有整数提升到所有充分大整数，同时保持极低计数函数，这正是随机法和筛法最脆弱的区域。GPT-5.5 级别系统可能产生有价值的条件性定理、实验线索或证明瓶颈分析，但直接完成 o((log N)^2) 或 O(log N) 的无条件证明概率较低。

### 免责声明

以上是对 AI 辅助可解性和推进潜力的审查，不是该 Erdős 问题的解答，也未声称给出了新的构造或证明。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `revised_open`
- 状态信心: `medium`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_32.md](../../prompts/problem_32.md)

### 状态结论

该数据库条目把三个问题并列，但它们的状态不同：Ruzsa（1998）已证明任一覆盖所有充分大整数的加法补集均满足 liminf A(x)/log x≥e^γ>1，故第三问已肯定解决。其余核心仍是：是否存在 A 使 P+A 包含所有充分大整数且 A(x)=o((log x)^2)；更强地，能否做到 A(x)=O(log x)。2026年1月仍标为 open 的 Erdős Problems 页面与2011/2014文献均支持该判断；本次未找到可核验的后续解决论文或严肃反例。

### 当前规范陈述

令 P 为正素数集合，A⊆N={1,2,...}，并记 A(x)=|A∩[1,x]|。若存在 n0，使得对每个 n≥n0 都存在 p∈P、a∈A 满足 n=p+a（等价地，P+A 包含所有充分大的正整数），则称 A 为 P 的加法补集。尚存问题为：(Q1) 是否存在这样的 A，满足 A(x)=o((log x)^2)？(Q2) 更强地，是否可满足 A(x)=O(log x)？原条目的第三问已有肯定答案：每个这样的 A 都满足 liminf_{x→∞}A(x)/log x≥e^γ>1，其中 γ 为欧拉–马歇罗尼常数。

```text
Let P be the set of positive prime numbers and, for A⊆N={1,2,...}, write A(x):=|A∩[1,x]|. Call A an additive complement to P if ∃n0∈N such that ∀n≥n0 there exist p∈P and a∈A with n=p+a (equivalently, P+A contains every sufficiently large positive integer). The surviving questions are: (Q1) does there exist such an A with A(x)=o((log x)^2) as x→∞, i.e. ∀ε>0 ∃X ∀x≥X, A(x)≤ε(log x)^2? (Q2) more strongly, does there exist such an A with A(x)=O(log x), i.e. ∃C,X such that A(x)≤C log x for every x≥X? The original third question has a known affirmative answer: every additive complement A to P satisfies liminf_{x→∞}A(x)/log x≥e^γ>1, where γ is the Euler–Mascheroni constant.
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 对字面陈述未发现小参数或奇偶性反例：A 可同时含奇、偶元素，有限个异常整数被定义允许。计数法只给出 A(x)≳log x，不能否定 o((log x)^2)。已核验的 Ruzsa 定理反而直接肯定了第三问。
- 版本变化: Erdős 1954 给出 A(x)=O((log x)^2) 的全覆盖构造；后续 Wolke、Kolountzakis、Ruzsa 的接近 O(log x) 结果均只保证密度1（几乎所有）覆盖。Ruzsa 1998 同时证明在全覆盖情形 liminf A(x)/log x≥e^γ，因此原第三问从开放问题变为已解决子问题。Dai–Pan 2011预印本、2014同行评审论文仍明确称不知道是否存在全覆盖的 O(log x) 补集。

陈述问题：

- 原始条目实际上并列了两个嵌套的存在性问题和一个下界问题；若将其视为单一“open”命题，会掩盖第三问已解决这一事实。
- “every large integer”须明确为“存在阈值 n0，使所有 n≥n0 可表示”；“almost all”不能替代这一全称覆盖条件。
- A⊂N 的起点采用正整数；允许 0 或改变有限个元素不会改变渐近问题，但应固定约定。
- “O(log N)”与“o((log N)^2)”均是对同一个全局计数函数的渐近上界，不是只在子序列上成立的界。

需要固定的量词/约定：

- The set A is fixed once and for all; neither A nor the implied O-constant may depend on the represented integer n.
- The covering condition is ∃n0∀n≥n0∃(p,a)∈P×A with n=p+a.
- Q1 uses a full limit little-o condition for every real x→∞; it is equivalent here to checking integer x, but not merely infinitely many x.
- Q2 implies Q1, but an affirmative solution of Q1 alone does not settle Q2.
- The proved lower bound is quantified over every additive complement A and concerns liminf, not an eventual pointwise bound A(x)≥e^γ log x.

### 文献与当前边界

已核验的主要结果：

- Erdős（1954，同行评审）：存在全覆盖补集 A，A(x)=O((log x)^2)；并且素数计数导致任何全覆盖补集至少有 A(x)≳log x 的粗下界。
- Wolke（1996，同行评审）：对“几乎所有”整数而非每个充分大整数取得接近线性的稀疏度。
- Kolountzakis（1996，同行评审）：构造 A(x)=O(log x log log x) 的几乎补集，异常集合具有上密度0。
- Ruzsa（1998，同行评审）：对任意 ω(x)→∞ 构造 A(x)=O(ω(x)log x) 的密度1补集；同时以同余类/筛法证明全覆盖（甚至某种定量近全覆盖）必有 liminf A(x)/log x≥e^γ。
- Vu（2001，结果经 Dai–Pan 2011/2014准确转述）：存在 A(x)=O(log x)，使每个充分大 n=p+a1+a2；这是二阶补集，不能把 A+A 误作所求的一阶 A。
- Dai–Pan（2014，同行评审）：构造稀疏素数集合参与的三素数/二阶型表示，并重证明/扩展 Ruzsa、Vu 型结论；并未改进 P+A 的全覆盖界。

最近相关工作：本次检索中，最近直接、同行评审地陈述本问题状态的是 Dai–Pan（Acta Arithmetica 2014），其称 O(log x) 全覆盖未知。检索到2025/2026关于一般加法补集的论文，但其假设和目标不是素数补集 Q1/Q2，未构成进展。2026-01-23 的 Erdős Problems 页面仍列为 open，且无论坛解答记录。

剩余核心：严格剩余的研究目标是把“密度1覆盖”的近线性构造升级为同一个固定 A 的逐点最终覆盖：至少证明或否定 A(x)=o((log x)^2)；特别地，证明或否定 A(x)=O(log x)。Ruzsa 的 e^γ 下界已排除 liminf≤1，却没有排除固定常数倍 log x，也没有排除介于 log x 与 (log x)^2 之间的增长。

已使用方法：

- 概率法与分尺度块构造。
- 短区间素数分布估计、筛法与Janson/相关不等式，用于控制随机补集遗漏。
- Mertens 型乘积、模小素数同余类和覆盖障碍，用于 e^γ 下界。
- 二阶补集/Goldbach 型表示；它提供相邻结构信息，但不能直接降为一个加数的补集。

争议或不确定性：

- 当前开放状态得到近期数据库记录和最后直接论文支持，但负面文献检索不能逻辑证明不存在2025–2026未索引的解答；因此为 medium 而非 high 置信度。
- 输入数据库标记“formalized=yes”，但本次检索未找到该问题的可访问 Lean/Isabelle/Coq 工件或其精确语句；不得把此元数据当作已形式化的证明。
- 数据库页面可见摘要称没有论坛解答，直接打开其猜测的 /forum 路径未成功；这不影响数学状态，但意味着论坛核验仅限页面报告。

### 证据来源

- [Erdős Problem #32](https://www.erdosproblems.com/32) — Thomas F. Bloom / Erdős Problems, 2026-01-23; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 页面在2026-01修订后仍把全覆盖的稀疏补集问题列为 OPEN，称评论区没有待处理的完整或部分解答；同时记录 Ruzsa 对第三问的 e^γ 下界。页面也明确警告其开放标签不是完备文献检索的证明。
- [Erdős Problem #32 LaTeX source](https://www.erdosproblems.com/latex/32) — Thomas F. Bloom / Erdős Problems, date unknown; `problem_page`, `database_record`, directness=`direct`, reliability=`low`. 按协议尝试打开 LaTeX 页面；浏览器返回403，故未将其作为独立的数学证据。
- [Some results on additive number theory](https://users.renyi.hu/~p_erdos/1954-09.pdf) — Paul Erdős, 1954; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 原文定理1证明存在补集，使每个充分大整数为 p+b 且计数函数 O((log x)^2)；引言还给出由素数计数产生的 Ω(log x) 必要量级。
- [On a Problem of Erdős in Additive Number Theory](https://www.sciencedirect.com/science/article/pii/S0022314X96900943) — Dieter Wolke, 1996-07; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 该论文的出版记录和摘要确认其改进针对“almost all n”而非全覆盖；因此不能解决 Q1/Q2。DOI: 10.1006/jnth.1996.0094。
- [On the additive complements of the primes and sets of similar growth](https://matwbn.icm.edu.pl/ksiazki/aa/aa77/aa7711.pdf) — Mihail N. Kolountzakis, 1996; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 证明存在 A(x)=O(log x log log x) 的几乎补集，并明确指出 Erdős 的全覆盖 O((log x)^2) 结果当时未被改进。
- [On the additive completion of primes](https://matwbn.icm.edu.pl/ksiazki/aa/aa86/aa8638.pdf) — Imre Z. Ruzsa, 1998; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 定理1给出 A(x)=O(ω(x)log x)、密度1覆盖（任意 ω→∞）；定理2表明若缺失集足够小，特别是全覆盖，则 liminf A(x)/log x≥e^γ。它直接解决第三问但不解决 Q1/Q2。
- [Note on the additive complements of primes](https://arxiv.org/abs/1101.1653) — Li-Xia Dai, Hao Pan, 2011-01-09; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 作者在引言明确写道仍不知道是否存在全覆盖 A(x)=O(log x) 的素数加法补集，并区分 Ruzsa 的几乎处处结果和 Vu 的二阶补集结果。
- [The additive complements of primes and Goldbach's problem](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/en/publishing-house/journals-and-series/acta-arithmetica/all/162/3/83028/the-additive-complements-of-primes-and-goldbach-s-problem) — Li-Xia Dai, Hao Pan, 2014; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 同行评审版本延续并扩展 Ruzsa/Vu 的不同结果；其可访问正文再次明确称全覆盖 O(log x) 问题未知。它是本次检索所见直接讨论本问题的最近同行评审来源。DOI: 10.4064/aa162-3-1。
- [On additive complements in the complement of a set of natural numbers](https://www.cambridge.org/core/journals/bulletin-of-the-australian-mathematical-society/article/on-additive-complements-in-the-complement-of-a-set-of-natural-numbers/10B671C7D04C9050726FF66E78FDBDEE) — Bhuwanesh Rao Patil, Mohan, 2025-11-07; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 2025/2026 的相关加法补集论文引用 Dai–Pan 与 Erdős，但研究的是具有指数间隔集合的互补补集，未声称处理素数的 Q1/Q2；用于排除该近年相邻文献被误判为解答。

### 完成标准

- 肯定出口: For Q1: exhibit one fixed A⊆N and prove both A(x)=o((log x)^2) and ∃n0∀n≥n0, n∈P+A. For the stronger Q2: prove the same coverage and A(x)=O(log x). A proof of Q2 is an affirmative resolution of Q1 as well. The historical third question is already affirmatively resolved by proving the universal bound liminf A(x)/log x≥e^γ>1.
- 否定出口: For Q1: prove that every A⊆N with P+A containing all sufficiently large integers fails A(x)=o((log x)^2); equivalently, prove a lower obstruction incompatible with little-o. Such a theorem also rules out Q2. For Q2 alone, prove that no fixed A with eventual P+A coverage has A(x)=O(log x), while recognizing that this would leave Q1 potentially open.

不构成完成：

- A construction for which P+A has density 1, lower density 1, or covers all but a sparse exceptional set.
- A construction that works only up to a finite computational cutoff, or whose set A depends on that cutoff or on n.
- A proof for n=p+a1+a2 with A(x)=O(log x), without converting it to a single summand a from a fixed set of the required size.
- Reproving A(x)=O((log x)^2), the e^γ lower bound, or only the elementary Ω(log x) counting lower bound.
- Showing A(x)=o((log x)^2) along a subsequence rather than as x→∞.

正确性陷阱：

- Keep eventual pointwise coverage distinct from density-one coverage at every scale-gluing step.
- Verify all constants and thresholds are uniform in n and that the final A is fixed, not a sequence of incompatible finite block choices.
- For any claimed O(log x) construction, bound its cumulative counting function across all blocks; a per-block O(log N) estimate does not automatically telescope to O(log x).
- For any lower bound, do not confuse liminf, limsup, an averaged lower bound, and an eventual pointwise lower bound.
- Check parity and the treatment of the prime 2 only as finite/structured exceptions; neither permits omitting one residue class indefinitely.
- Do not infer a one-summand complement from Vu/Dai–Pan two-summand results without proving the resulting sumset has the required counting bound.

### 更新后的 AI 可解答性

- 等级: `low_candidate`
- 分数: `12/100`
- 信心: `medium`
- 结论: 这是定义清楚、可严格验算但长期卡在深层素数分布与随机覆盖障碍上的开放问题；适合作为低概率、证明优先的研究任务，不适合作为计算主导任务。

支持理由：

- Q1/Q2 的量词、渐近界和成功证书均明确，任何构造或普适下界都可逐段审计。
- 存在强而精确的相邻结果：全覆盖 O(log²x)、密度1的 O(ωlog x)、以及 e^γ 必要下界。
- 问题剩余间隙窄且具有清晰的“全覆盖 versus 几乎处处覆盖”技术断层。

主要障碍：

- 开放时间很长；现有近线性概率构造控制的是遗漏密度，升级为零个最终遗漏需要更强的依赖控制或新结构。
- 仅靠有限计算不能认证“所有充分大 n”或任何渐近 little-o/O 界。
- 最自然的下界 e^γ 仍与排除 O(log x) 或 o(log²x) 相距很远，不能由简单计数补足。

Proof-first 路线：

- 审计 Ruzsa 分尺度概率构造中导致 ε_i→0 时累计大小必须带任意发散 ω 的确切损失；寻求可证明消除该损失的结构性引理，或证明该类策略不可能。
- 从模小素数覆盖障碍推广 Ruzsa 的 e^γ 论证，明确目标为获得随 x 发散的 A(x)/log x 下界，或可量化的非 o(log²x) 下界。
- 研究能把遗漏事件的局部相关性转化为确定性消除的条件；任何候选引理必须保留固定 A 与全尺度一致性。

需要验证：

- 由人工/专业数据库补做 MathSciNet、zbMATH、Google Scholar 前向引文及作者主页检索，特别核验2014年后是否有直接 Q1/Q2 论文。
- 若要依赖“formalized=yes”，须取得工件URL、固定版本、原始定理文本和无公理检查结果；否则只把它视为未核实的数据库元数据。
- 任何新声称的 O(log x) 结果都须逐项核验其覆盖是否是 every sufficiently large n，而不是 almost all、平均意义或二阶表示。

### 审计限制与人工复核理由

- 无法从“未检索到”推出不存在2025–2026的新论文；此次直接的最新状态证据主要是2026年数据库页和2014年直接研究文献。
- Erdős Problems 的 LaTeX URL 在本次浏览环境返回403；主页面的搜索索引内容仍足以核对输入转录，但未能独立读取其源码。
- 未获得 Vu（2001）原始论文；其陈述仅作为 Dai–Pan 同行评审论文和预印本中的二手、明确转述使用，且并非判断 Q1/Q2 状态的唯一依据。
- “formalized=yes”缺少可访问工件链接，未核验其范围或可信度。

- 建议由具有 MathSciNet/zbMATH/Google Scholar 访问权限的研究者完成2014年至2026年的前向引文和作者主页核查，以把“likely/revised open”提升为更高置信度。
- 需要人工取得并检查任何所谓正式化工件；当前只能确认数据库元数据，不能确认其是命题编码、部分引理还是完整证明。
- 若未来出现声称 O(log x) 的论文，人工审计应优先核对其是否真正给出单一固定 A 的最终逐点覆盖。

<!-- DEEP_REVIEW:END -->
