# Problem 123

## 基本信息

- 原始链接: https://www.erdosproblems.com/123
- LaTeX 页面: https://www.erdosproblems.com/latex/123
- 原始状态: `open`
- 奖金: `$250`
- 主类别: `number theory`
- 原始标签: `number theory`
- 形式化状态: `yes`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

Let $a,b,c\geq 1$ be three integers which are pairwise coprime. Is every large integer the sum of distinct integers of the form $a^kb^lc^m$ ($k,l,m\geq 0$), none of which divide any other?

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `25/100`
- 建议路线: 优先文献定位、特殊情形、数值实验和辅助引理搜索；完整证明需要新的数学思想。

## 判断依据

### 有利因素

- 已有形式化陈述，可降低语义误读风险

### 主要障碍

- 所属标签偏证明密集：number theory
- 题面含渐近/无限对象线索：prime
- 原记录含奖金 $250，说明该题被长期视为高价值难题；这不是否定依据，但提高验证门槛。
- 缺少明显有限搜索入口。

### 公开版思考过程摘要

- 先识别问题类型：无限/渐近或抽象证明倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: number theory
- 有限/计算线索: 无
- 渐近/无限线索: prime
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5级别模型+计算搜索+形式化证明+文献检索工具`
- 结论: **中等候选。完整解决对模型仍有明显难度，但该题结构离散、可计算、已有若干有限验证型进展且已形式化，因此GPT-5.5级别系统有现实机会复现和扩展已知方法，生成可验证证书，推进一批新参数族；直接证明全称命题的把握不高。**
- 等级: `medium_candidate`
- 分数: `58/100`
- 信心: `medium`
- 可能路线: 较可行的路线不是直接猜一个全局证明，而是先把d-complete条件转化为可迭代的有限区间覆盖或归纳扩张准则；对给定的a,b,c用动态规划、SAT/ILP或启发式反例搜索寻找 antichain 表示证书；再尝试抽象出随参数变化稳定的覆盖引理，并把有限证书和归纳步骤形式化验证。

### 支持理由

- 题目对象是三生成乘法半群中的整数，搜索空间虽大但结构清楚，适合程序枚举、反例搜索和证书生成。
- 备注中已有多个参数族的正面结果，并且至少部分进展看起来依赖有限区间表示条件，这给模型提供了可复现、可推广的技术模板。
- 问题已标记为 formalized=yes，说明形式化验证或至少形式化陈述已有基础，有利于把计算证书转成可审计证明片段。
- 约束“所选项互不整除”可以自然建模为偏序 antichain 约束，适合用组合优化、DP、SAT/ILP 或证明助理中的有限检查来处理。
- 模型可能特别擅长整理已知证明模式、发现遗漏边界情形、批量验证新三元组，并从计算输出中提炼候选归纳不变量。

### 主要障碍

- 全称量词覆盖所有两两互素的a,b,c，参数无界；有限计算只能覆盖样例或有条件族，距离统一定理仍有鸿沟。
- d-completeness要求“所有充分大的整数”，需要一个可无限延展的归纳或密度机制；单纯表示很多区间不足以证明最终结论。
- 互不整除条件比普通子集和表示更强，会破坏许多贪心或密度直觉，证明中需要精确控制指数向量的偏序关系。
- 若a、b、c允许等于1，可能存在退化情形或重复表示问题，必须先严格澄清题目约定。
- 搜索证书可能非常大，且不同参数的证书不一定呈现简单规律；模型容易把经验性模式误当成证明。

### 需要的验证

- 先形式化确认输入命题的边界条件，尤其是a,b,c是否可为1以及“distinct integers of the form”如何处理重复生成。
- 基于题目备注中给出的已知结果，复现至少一个已知正例的有限证书或证明框架，以校准搜索程序和形式化定义。
- 对若干未覆盖参数运行反例搜索和表示搜索，记录失败区间、证书大小和是否存在可归纳的区间扩张。
- 若提出一般证明，需要把有限覆盖引理、放缩步骤、antichain保持条件和最终“所有充分大整数”结论分别机械化或独立审查。
- 所有计算证书应输出为可重放格式，并由独立程序或证明助理复核，避免依赖模型文本推断。

### 公开版思考摘要

该题不像纯结构性猜想那样完全不可计算：对象可枚举，约束可编码，已有进展也显示有限区间覆盖可能是核心机制。因此GPT-5.5级别模型配合工具很可能能做出实质推进，例如扩大已知参数范围、发现统一的候选引理、生成形式化可检验证书。不过从这些局部证书上升到所有两两互素三元组，需要新的统一数论或组合构造，仍是主要难点。

### 免责声明

以上是对AI辅助可攻性的审查，不是该Erdős问题的证明或反例。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `disproved`
- 状态信心: `high`
- 可行动性: `closed_verification_only`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_123.md](../../prompts/problem_123.md)

### 状态结论

按网页当前的字面量词，命题已被反驳：允许底数 1，而 (a,b,c)=(1,5,7) 两两互素；相应集合正是 {5^l7^m:l,m≥0}。Erdős–Lewin 的两底数定理表明它仅在底数集合为 {2,3} 时才 d-完全，故该集合不是 d-完全。网站仍标为 open，但论坛已明确指出“≥1”是笔误，Lean 表述也改用 a,b,c>1；修正后的三底数全称猜想则未由本审计证实已解决。

### 当前规范陈述

字面命题：对任意两两互素的整数 a,b,c≥1，令 S(a,b,c)={a^k b^l c^m:k,l,m∈Z_{≥0}}（按数值组成集合，重复值不重复计）。是否存在 N=N(a,b,c)，使每个 n≥N 都可写为某有限 F⊆S(a,b,c) 的元素和，且任意不同 x,y∈F 均满足 x∤y 且 y∤x？

```text
Literal printed statement: For every triple of pairwise coprime integers a,b,c>=1, let S(a,b,c)={a^k b^l c^m:k,l,m in Z_{>=0}} as a set of positive integers (so equal numerical values are not repeated). Is there an N=N(a,b,c) such that every integer n>=N has a finite subset F of S(a,b,c) with n=sum_{x in F}x and, for all distinct x,y in F, neither x divides y nor y divides x?
```

### 陈述、量词与反例审计

- 歧义严重度: `material`
- 简单反例检查: `counterexample_found`
- 检查说明: 取 (a,b,c)=(1,5,7)。它们两两互素，且 S(1,5,7)={5^l7^m:l,m≥0}。Erdős–Lewin 的已发表两底数结论（亦被 Chen–Yu 2023 明确复述）说：对 1<p<q，{p^αq^β} d-完全当且仅当 {p,q}={2,3}。故 {5^l7^m} 不 d-完全，即对任意阈值均存在更大的不可表示整数。这直接否定当前字面全称命题；无需有限枚举。
- 版本变化: 截至 2026-01-20，Erdős Problems 页面仍显示 ≥1 且标为 open；2026-04-25 的论坛评论指出该范围的明显反例，并称应改为 >1。FormalConjectures 的对应定义同样使用 a,b,c>1，但该 Lean 声明含 sorry，不能作为已形式化证明。应将“a,b,c≥2 的修正全称猜想”单列为残余开放目标，而不把它与已反驳的字面题混同。

陈述问题：

- 主陈述写作 a,b,c≥1；“两两互素”并不排除 1，亦不要求三者彼此不同。因此该字面命题包含退化为两底数的情形。
- 论坛评论已明确指出 a=1,b=5,c=7 是反例，并称 ≥ 应为 >；同一问题的 Lean 记录也量化为 a>1,b>1,c>1。这强烈表明原意是每个底数至少为 2，但不能悄然以此修正当前字面命题。
- 网页/输入的 Ma–Chen 条目声称讨论 a=2,b=5，却将区间条件中的集合写为 {2^k3^lc^m}；Ma–Chen 的出版摘要对应 {2^α5^βp^γ}。这是背景条目中的转录不一致，不能据网页中的 3 当作已核实定理。
- “large integer”应显式读为“存在阈值 N，使所有 n≥N 成立”；“none divide any other”应作用于同一表示中所选的不同加数。

需要固定的量词/约定：

- The universal quantifier is over ordered triples of pairwise coprime positive integers; pairwise coprime permits 1.
- The exponents k,l,m are independently quantified nonnegative integers.
- d-completeness means exists N such that for every integer n>=N there exists a finite admissible set F; it does not merely mean infinitely many representable n.
- Distinctness concerns the selected numerical summands. If a base is 1, different exponent triples can denote the same integer and must be deduplicated in S.
- For different selected x,y, the condition is neither x|y nor y|x; equality is already excluded by F being a set.

### 文献与当前边界

已核验的主要结果：

- Erdős–Lewin（1996，同行评审）定义 d-完全性，证明两底数 {p^αq^β} 在正整数 p,q 情形 d-完全当且仅当 {p,q}={2,3}；并给出若干三底数正例，包括 (3,5,7) 与若干 (2,5,p)。该两底数定理直接完成本字面反例的证明。
- Ma–Chen（2016，同行评审）为 {2^α5^βp^γ} 给出有限区间覆盖可推出 d-完全性的准则，并验证更多 p/复合 c 特例。
- Chen–Yu（2023，同行评审）对 p,q,r≥2 的一般三底数集合建立 d-完全性准则，并证明：{2^a5^br^c} 对 1<r≤87 且 (r,10)=1、{2^a7^br^c} 对 1<r≤33 且 (r,14)=1、{3^a5^br^c} 对 1<r≤14 且 (r,15)=1 均 d-完全。
- Yu–Chen（2022，同行评审）解决一个不同的两底数猜想；其标题中的“settle a conjecture”不涉及 #123 的全称三底数命题。
- Jiang–Wu（2024，同行评审）研究 d-完全模 l；这不是“所有充分大整数均可表示”的普通 d-完全性。

最近相关工作：本次检索中，普通三底数 d-完全性最直接、最新的已核实主结果是 Chen–Yu 2023。2024 Jiang–Wu 是模 l 变体而非本目标；未发现 2024–2026 年可核验的论文或预印本解决修正后的全称三底数猜想。该未发现结论仅是检索结果，不是无解文献的证明。

剩余核心：若人工确认历史意图并将范围修正为两两互素的 a,b,c≥2，剩余问题是：是否对每个这样的三元组，{a^kb^lc^m} 都 d-完全？本审计没有找到该修正命题的完整证明或反例；但它不是当前字面题的真值状态。

已使用方法：

- 两底数情形的可表示性障碍及乘以底数的不可表示性传播。
- 按倍增/缩放构造的归纳表示法。
- 先证明有限乘法区间内的全部覆盖，再以缩放引理推广为 d-完全性。
- 对特定底数三元组建立可检验的覆盖区间和一般判据。

争议或不确定性：

- 网站仍将字面 ≥1 版本标为 open，与其论坛指出的明显退化反例矛盾；最合理解释是页面尚未修订而非两底数定理失效。
- 修正为 >1 的历史原意有论坛和 Lean 陈述支持，但本审计没有检查 Erdős 原始题目文本以最终裁定措辞。
- FormalConjectures 页面虽显示 formalized，但核心声明使用 sorry，不能视为形式化完成。
- Ma–Chen 背景条目中 5/3 的不一致需要以原文定理而非网页转录为准。

### 证据来源

- [Erdős Problem #123](https://www.erdosproblems.com/123) — Terence F. Bloom / Erdős Problems, 2026-01-20; `problem_page`, `database_record`, directness=`direct`, reliability=`high`. 给出当前字面陈述、网站的 open 标签、已知特例及网站自身关于状态并非穷尽文献结论的免责声明。
- [123 Discussion Thread](https://www.erdosproblems.com/forum/thread/123?order=oldest) — Erdős Problems users, including mysticflounder and Woett, 2026-04-25; `forum`, `informal_claim`, directness=`direct`, reliability=`medium`. 明确提出 a=1,b=5,c=7 的退化反例，并指出应把 ≥ 改成 >；还记录网站尚无评论区的完整或部分解答主张。该评论不是反例证明的主要依据。
- [d-Complete Sequences of Integers](https://www.brand.site.co.il/riddles/201507a_files/2153618.pdf) — P. Erdős and Mordechai Lewin, 1996-04; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 原论文给出：对正整数 p,q，集合 {p^αq^β} d-完全当且仅当 {p,q}={2,3}。取 p=5,q=7 即证明字面题的反例。
- [d-complete sequences of integers — bibliographic record](https://dblp.org/rec/journals/moc/ErdosL96) — Paul Erdős and Mordechai Lewin, 1996; `secondary_index`, `database_record`, directness=`indirect`, reliability=`high`. 独立核对 Erdős–Lewin 论文的作者、题名、期刊 Mathematics of Computation 65(214) 及页码 837–840。
- [On d-complete sequences of integers](https://www.sciencedirect.com/science/article/pii/S0022314X16000342) — Mi-Mi Ma and Yong-Gao Chen, 2016-07; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 核对 Ma–Chen 2016 的定义、其对 {2^α5^βp^γ} 的区间覆盖准则及其具体应用；也显示网页背景条目把 5 误写成 3 的风险。DOI: 10.1016/j.jnt.2015.12.003。
- [On d-complete sequences of integers, II](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/207/2/115065/on-d-complete-sequences-of-integers-ii) — Yong-Gao Chen and Wang-Xing Yu, 2023-03-20; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 明确复述两底数 iff 结论；对 a,b,c≥2 的一般三底数集合建立准则，并证明网页所列三组有限范围。DOI: 10.4064/aa220818-20-1。
- [On a conjecture of Erdős and Lewin](https://www.sciencedirect.com/science/article/pii/S0022314X21003358) — Wang-Xing Yu and Yong-Gao Chen, 2022-09; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 解决的是一个不同的两底数 Erdős–Lewin 猜想，并非 #123 的三底数全称猜想；用于避免把“settle a conjecture”误读为解决本题。DOI: 10.1016/j.jnt.2021.09.018。
- [On d-complete sequences modulo l](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/online/115470/on-d-complete-sequences-modulo-l) — Xing-Wang Jiang and Bing-Ling Wu, 2024-02-27; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 给出 d-完全模 l 的相关但不同问题，不能作为普通 d-完全或 #123 已解决的证据。DOI: 10.4064/aa230602-31-10。
- [FormalConjectures.ErdosProblems.«123»](https://firsching.ch/formal-conjectures/src/FormalConjectures/ErdosProblems/%C2%AB123%C2%BB/) — FormalConjectures contributors, date unknown; `formalization`, `formalized_artifact`, directness=`direct`, reliability=`high`. 该记录以 a,b,c>1 编码问题，但核心 theorem 标注为 declaration uses sorry。因此它是待证明的形式化陈述，而不是本题或其特例的机器核验证明。

### 完成标准

- 肯定出口: For the literal printed proposition, a complete negative resolution consists of: (i) verifying that a=1,b=5,c=7 satisfies the printed hypotheses; (ii) proving S(1,5,7)={5^l7^m:l,m>=0}; and (iii) applying or independently reproving the Erdős–Lewin theorem that this two-base set is not d-complete. This establishes that arbitrarily large integers fail the required representation.
- 否定出口: The audit conclusion would fail only if a primary source or authoritative erratum establishes that the operative statement already required a,b,c>1 despite the displayed literal text, or if the cited two-base theorem is shown not to apply to p=5,q=7 under the same d-completeness definition. In that event, reclassify the displayed record as a repaired/open statement and rerun the status search for the >1 target.

不构成完成：

- Checking finitely many integers for (1,5,7).
- Showing merely that one small integer is not representable.
- Treating the website's open label as overriding the literal quantifiers.
- Proving a result only for a,b,c>1 without recording that it answers a different, repaired proposition.
- Citing a Lean declaration containing sorry as a machine-checked proof.

正确性陷阱：

- Pairwise coprimality permits 1; it neither requires bases to exceed one nor makes three bases distinct.
- With a=1, exponent k creates duplicate descriptions, but the set of numerical summands is exactly the two-base set.
- Negating d-completeness requires failures beyond every threshold, not merely a finite exception; the two-base iff theorem supplies this.
- Do not replace the printed a,b,c>=1 by >1 silently.
- Keep ordinary d-completeness distinct from d-completeness modulo l and from the stronger snug/clustered conjecture.

### 更新后的 AI 可解答性

- 等级: `not_applicable_closed_or_invalid`
- 分数: `0/100`
- 信心: `high`
- 结论: 字面命题已由已知两底数定理和退化三元组反驳；因此不存在应由 AI 尝试解决的当前开放字面目标。

支持理由：

- (1,5,7) 满足当前量词，且集合精确退化为已分类的两底数集合。
- 反驳依赖的是同行评审论文中的一般定理，而非有限计算或论坛断言。

主要障碍：

- 若要研究修正后的 a,b,c≥2 全称猜想，必须先获人工确认这是题目的授权修订目标。
- 现有范围结果不等同于任意三元组的统一结论，且网站背景的一个公式转录不一致。

Proof-first 路线：

- 本记录仅需审计式验证：核验 Erdős–Lewin 两底数定理、集合等式和量词代入。
- 对修正题的任何后续研究应重新立项；不能把验证字面反例包装成对修正猜想的解答。

需要验证：

- 核阅 Erdős–Lewin 原文的两底数 corollary 及其定义是否与当前网页完全一致。
- 核阅 Erdős 的原始问题陈述或权威勘误，以决定是否正式把页面范围改为 a,b,c>1。
- 若维护形式化状态，移除/替换 sorry 后才可宣称机器验证。

### 审计限制与人工复核理由

- Erdős–Lewin 原文可检索到且相关 corollary 可见，但本环境未能从 AMS 直接取得原始出版页面；已以原文扫描件、DBLP 书目和 Chen–Yu 的同行评审复述交叉核对。
- arXiv API 连接被本环境拒绝；同时进行了网页/arXiv 域名检索，未发现 2024–2026 年针对普通三底数全称命题的可核验预印本。未发现不构成不存在的证明。
- 本审计未查看 Erdős 1992/1997 原始题面，故“>1 是作者原意”保持为有力但未最终裁定的修复解释。
- 未声称验证 Ma–Chen 或 Chen–Yu 的完整证明；仅依据出版页面摘要和与本审计相关的明示结果。

- 需要维护者或人工文献审阅者确认原始题目是否应正式勘误为 a,b,c>1，并决定数据库记录应将字面题标为 disproved、另建或改写为 revised open。
- 若需把反驳作为正式发表级结论，应人工核对 Erdős–Lewin 原文中两底数分类 corollary 的完整定义和页码。

<!-- DEEP_REVIEW:END -->
