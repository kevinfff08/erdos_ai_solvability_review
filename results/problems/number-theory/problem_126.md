# Problem 126

## 基本信息

- 原始链接: https://www.erdosproblems.com/126
- LaTeX 页面: https://www.erdosproblems.com/latex/126
- 原始状态: `open`
- 奖金: `$250`
- 主类别: `number theory`
- 原始标签: `number theory`
- 形式化状态: `yes`
- OEIS: `possible`
- 原站备注字段: 无

## 原问题

Let $f(n)$ be maximal such that if $A\subseteq\mathbb{N}$ has $\lvert A\rvert=n$ then $\prod_{a\neq b\in A}(a+b)$ has at least $f(n)$ distinct prime factors. Is it true that $f(n)/\log n\to\infty$?

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `19/100`
- 建议路线: 优先文献定位、特殊情形、数值实验和辅助引理搜索；完整证明需要新的数学思想。

## 判断依据

### 有利因素

- 已有形式化陈述，可降低语义误读风险

### 主要障碍

- 所属标签偏证明密集：number theory
- 题面含渐近/无限对象线索：\ll, o(, prime
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
- 渐近/无限线索: \ll, o(, prime
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5+tools`
- 结论: **有可能显著推进或验证局部结构，但完整证明 f(n)/log n→∞ 的可完成性偏低；更合理定位是中低候选。**
- 等级: `low_to_medium_candidate`
- 分数: `42/100`
- 信心: `medium`
- 可能路线: 把反面命题形式化为：存在很大的 n 元集合 A，使所有两两和的素因子都落在一个大小 O(log n) 的素数集合内。模型可结合计算搜索、SAT/ILP/SMT 编码、P-smooth 数枚举、模小素数约束、加性组合与筛法来寻找不可能性证据；再把可证明的局部引理或有限验证转成 Lean 证明，目标可能先是改进已知下界中的常数、证明特定结构族不可能达到 O(log n)，或建立 f(n) ≥ log n·g(n) 的弱发散函数。

### 支持理由

- 问题陈述短、量词结构清楚，并且已有 Lean 形式化入口，适合模型把自然语言命题、有限反例搜索和形式化验证连接起来。
- 反面构造具有可计算表示：若素因子数很少，则所有 pair sums 都必须来自同一个有限素数集合生成的平滑数集合，这给约束求解和实验数学提供了明确抓手。
- 现有摘录只给出 log n 级下界和 n/log n 上界，中间差距大；即使不能解决主问题，模型可能通过系统搜索发现新的障碍结构、候选引理或可验证的弱改进。
- 该问题属于数论与加性组合交界，GPT-5.5 级模型可调用文献检索、符号计算、枚举和形式化证明工具，对既有方法进行组合式推进。

### 主要障碍

- 主命题要求渐近发散，不能靠有限计算直接证明；计算只能排除有限范围或指导猜想。
- 最困难部分是把“所有两两和只含少量不同素因子”的全局结构转化为随 n 增强的定量矛盾，这通常需要新筛法或加性组合论输入。
- 上界示例 A={1,...,n} 已给出 n/log n，说明 pair sums 的素因子集合可以相当稀疏；简单素数计数或大小估计很可能只能重现已知 log n 级别。
- Lean 形式化有助于验证，但不会自动产生关键数学想法；复杂筛法、平滑数估计和渐近常数的形式化成本也较高。
- 问题历史很长且仍开放，说明主证明可能依赖尚未被标准工具直接覆盖的结构性洞察。

### 需要的验证

- 复现摘录中的 log n ≪ f(n) 下界，确认模型没有只是在改写已知证明。
- 对小 n 或受限素数集合做独立枚举，检查候选极端集合及其 pair-sum 素因子数。
- 将任何新引理明确归约为可检验的有限命题、标准筛法不等式或 Lean 可形式化定理。
- 若声称证明 f(n)/log n→∞，必须给出显式发散函数 g(n) 并严格证明 f(n) ≥ log n·g(n)。
- 用 Lean 或至少机器可检查的证明脚本验证关键组合计数、整除约束和渐近推导。

### 公开版思考摘要

这个问题对 AI 友好的部分在于反例结构可计算、形式化状态良好、且存在清晰的约束搜索入口；AI 可以围绕少量素数控制所有两两和这一核心限制做系统实验和局部定理验证。但主问题是强渐近下界，核心难点不是计算规模而是新的定量结构定理。因此我不认为它是高概率可完全解决的 AI 目标，但它适合作为 GPT-5.5+工具显著推进的中低候选。

### 免责声明

以上是可解性与推进潜力评估，不是该 Erdős 问题的证明或反例。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `likely_open`
- 状态信心: `medium`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_126.md](../../prompts/problem_126.md)

### 状态结论

截至 2026-07-27，当前 Erdős Problems 页面仍将此题列为 open，论坛页显示没有评论中的完整或部分解答声明；针对精确表述、原始论文、作者和近三年 arXiv 的检索亦未找到可核验的解决或反例。1934 年 Erdős–Turán 论文已直接核对到其指数型结构定理，足以给出 f(n)≫log n，但未解决题设要求的任意发散倍数。由于公开检索不能穷尽未索引文献，结论为 likely_open 而非 confirmed_open。

### 当前规范陈述

令 N={1,2,...}。对每个整数 n>=1，定义 f(n)=min_{A⊆N, |A|=n} ω(∏_{(a,b)∈A²,a≠b}(a+b))，其中 ω(m) 是正整数 m 的不同素因子个数，且 ω(1)=0。等价地，f(n) 是使得每个 n 元集合 A⊆N 的该乘积至少有 k 个不同素因子的最大整数 k。判定是否 lim_{n→∞}f(n)/log n=+∞；等价地，是否对每个 C>0，存在 N_C，使得所有 n>=N_C 及所有满足 |A|=n 的 A⊆N 都有 ω(∏_{a≠b}(a+b))>=C log n。

```text
Let N={1,2,...}. For every integer n>=1, define f(n)=min_{A⊆N, |A|=n} ω(∏_{(a,b)∈A², a≠b}(a+b)), where ω(m) is the number of distinct prime divisors of the positive integer m and ω(1)=0. Equivalently, f(n) is the greatest integer k such that every n-element A⊆N makes the displayed product have at least k distinct prime divisors. Decide whether lim_{n→∞} f(n)/log n=+∞; equivalently, whether for every C>0 there is N_C such that every n>=N_C and every A⊆N with |A|=n satisfy ω(∏_{a≠b}(a+b))>=C log n.
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 未找到否定字面精确定义的简单构造。A={1,...,n} 只给出上界；它不是反例。由于 A 是集合，重复元素也不能用于压低素因子数。
- 版本变化: 可访问的 Erdős Problems 历史页显示 2025 年版本与当前主命题相同，未见把该问题替换为非等价目标的修订。后来加入 Lean 形式化链接，但该文件只含带 sorry 的语句，不是证明。1934 原论文还提出了关于相关极值函数 n(k) 的明显更强猜想；这不是对当前目标的已完成替代。

陈述问题：

- “f(n) be maximal such that”应明确为：对所有 n 元集合均成立的整数下界的最大值；它等于所涉 ω 值在所有 n 元集合上的最小值。
- 题面没有说明 a≠b 的乘积使用有序还是无序对；两种乘积相差平方，因此 ω 完全相同。
- 原始 1934 论文明确使用正整数；题面中的 N 需据此指定为 {1,2,...}。
- Lean 文件采用 Finset ℕ，因此允许 0，严格说与正整数版本并不字面相同。其渐近目标仍等价：若 f_+(n) 为正整数版本、f_0(n) 为允许 0 的版本，则 f_+(n-1)<=f_0(n)<=f_+(n)，而 f_+ 单调不减。
- n=1 时乘积为空乘积 1、f(1)=0；这不影响渐近问题。

需要固定的量词/约定：

- The maximum is over integers k satisfying a universal condition over every n-element set A; it is not a maximum over choices of A.
- The asserted limit is divergence to +∞, stronger than unboundedness on a subsequence.
- All constants in a lower bound must be independent of both n and A.
- Ordered and unordered distinct-pair products give the same value of ω.

### 文献与当前边界

已核验的主要结果：

- Erdős–Turán（1934，同行评议期刊论文）证明：任取 3·2^(k-1) 个正整数，它们的两项和不可能全部只含一组给定的 k 个素因子。因而若某 n 元集合的所有两项和只使用 k 个不同素数，则 n<3·2^(k-1)，从而 f(n)≫log n。其论证使用逐素数筛选/减半的初等 p-进赋值结构。
- 对 A={1,...,n}，所有不同两项和均不超过 2n-1；其素因子并集包含于 p<=2n 的素数集合。因此 f(n)<=π(2n)≪n/log n。这与当前题目页转述的上界一致。
- 1934 原文称相关最大规模 n(k) 可能满足 n(k)=O_ε(k^(1+ε))（每个 ε>0）。若成立，它将远强于当前 f(n)/log n→∞ 目标；原文明确说当时无法证明。
- Formal Conjectures 的 126.lean 形式化了主问题和上述大 O 两侧界的陈述，但源码均保留 sorry；因此它是语句工件而非已验证数学结果。

最近相关工作：本次检索到的最近直接相关公开工件是 Formal Conjectures 的 2025 年 Lean 语句文件，而非新的数论进展。对精确措辞、原文标题、n(k) 表述及 2023–2026 arXiv 的定向检索均未找到可审查的后续证明、反例或严格改进。

剩余核心：证明或否定：对任意 C>0，所有充分大的 n 以及每个 n 元正整数集合 A，都有 ω(∏_{a≠b}(a+b))>=C log n。已知结论仅给出某个固定正比例的 log n 下界；要解决问题必须使该比例任意大。

已使用方法：

- Erdős–Turán 的逐素数筛选和 p-进赋值论证：每处理一个给定素数，将候选集合保留为约一半，最后以三个数的 2-进矛盾结束。
- 区间构造 A={1,...,n} 与素数计数函数，给出 n/log n 级上界。
- 将“所有两项和的素因子并集很小”改写为有限素数集上的 S-unit 型限制；原始论文已给出这一视角，但没有给出足以超过对数下界的结构定理。
- Lean 可用于检查定义、量词、正整数/非负整数版本的等价性和已获得的有限引理；当前文件不能用于引用完整证明。

争议或不确定性：

- Erdős Problems 页面明确称 open 状态只是维护者的当前相信，并警示其可能未知文献；这阻止将数据库标签视作决定性证明。
- 当前论坛没有解答声明，但论坛沉默不是文献检索的替代品。
- 页面还列出 Er95c、Er97、Er97e 等来源代码；本次公开检索未能可靠恢复其完整书目信息或逐页核对其与本题的关系，故未将它们用于任何实质数学结论。
- 未发现新结果是阴性检索证据，不排除未索引、名称变化、付费墙后或未公开的工作。

### 证据来源

- [Erdős Problems — Problem 126](https://www.erdosproblems.com/126) — Thomas F. Bloom / Erdős Problems contributors, date unknown; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 给出当前题面、open 标签、历史备注中的两侧界、formalized 标记，以及数据库拥有者关于状态非穷尽性的明确警示。
- [126 Discussion Thread | Erdős Problems](https://www.erdosproblems.com/forum/thread/126) — Erdős Problems, date unknown; `forum`, `informal_claim`, directness=`direct`, reliability=`medium`. 页面显示当前 open 状态、0 条评论，并明确写明没有评论中声称的完整或部分解答；这只支持“未发现论坛声明”，不能证明文献中无解答。
- [On a Problem in the Elementary Theory of Numbers](https://www.renyi.hu/~p_erdos/1934-03.pdf) — Paul Erdős and Paul Turán, 1934; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 原文给出：由 3·2^(k-1) 个正整数形成的两项和不可能全由给定的 k 个素数构成；并讨论相关 n(k) 的更强猜想。该定理直接推出 f(n)≫log n。
- [On a Problem in the Elementary Theory of Numbers](https://www.tandfonline.com/doi/abs/10.1080/00029890.1934.11987659) — Paul Erdős and Paul Turán, 1934; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 出版方记录核实论文标题、作者、期刊 American Mathematical Monthly、卷 41 和页码 608–611，以及 DOI。
- [FormalConjectures/ErdosProblems/126.lean](https://raw.githubusercontent.com/google-deepmind/formal-conjectures/main/FormalConjectures/ErdosProblems/126.lean) — Google DeepMind Formal Conjectures contributors, 2025; `formalization`, `formalized_artifact`, directness=`direct`, reliability=`high`. 文件精确形式化了 f 的“最大下界”定义和主极限命题，但两个主张均以 sorry 留空；同时它采用 Nat/Finset，故允许 0。
- [Formal Conjectures](https://google-deepmind.github.io/formal-conjectures/) — Google DeepMind Formal Conjectures contributors, date unknown; `formalization`, `formalized_artifact`, directness=`direct`, reliability=`high`. 项目主页说明其收集开放猜想的 Lean 语句，并区分“statements”“open”和“formally proved”；支持不能从“formalized”推断已证明。

### 完成标准

- 肯定出口: Prove that for every real C>0 there exists N_C such that, for every integer n>=N_C and every A⊆{1,2,...} with |A|=n, ω(∏_{a≠b∈A}(a+b))>=C log n.
- 否定出口: Prove that the limit is not +∞. Equivalently, exhibit a finite C and infinitely many n for which there is an n-element set A_n⊆{1,2,...} satisfying ω(∏_{a≠b∈A_n}(a+b))<=C log n.

不构成完成：

- Improving only the constant in f(n)>=c log n for one fixed c>0.
- A result for intervals, random sets, sets of bounded height, or any restricted family that does not cover arbitrary A.
- A proof that f is unbounded, or a lower bound c(n)log n without proving c(n)→∞.
- Finite computation or sampled numerical evidence.
- A proof of f(n)=o(n/log n), which is compatible with both the affirmative target and the known bounds.
- A proof about Ω, the number of prime factors with multiplicity, instead of ω.

正确性陷阱：

- Keep the quantifier order uniform over all A after choosing C and N_C.
- Distinguish the union of distinct prime divisors from multiplicities across many pair sums.
- Do not use pair sums with a=b unless an explicit reduction proves they are harmless.
- Check ordered versus unordered pair products before changing notation.
- If using the Lean artifact, account for its inclusion of 0 and its unresolved sorry placeholders.
- For a negative construction, prove both its infinite parameter range and the claimed uniform prime-support bound.

### 更新后的 AI 可解答性

- 等级: `low_candidate`
- 分数: `12/100`
- 信心: `medium`
- 结论: 目标定义清楚、完成条件可审计，但它要求对任意稀疏正整数集合取得超对数的统一不同素因子下界；现有公开记录仅见 1934 年的固定常数对数界，故当前 AI 直接解决概率低。

支持理由：

- 命题可精确量化，正反两种完成条件均明确。
- 1934 证明提供可重建、可审计的具体基线机制。
- 形式化语句有助于检查定义和局部辅助引理。

主要障碍：

- 从固定常数倍 log n 提升到任意发散倍数是定性跨越，而非改进常数。
- 集合 A 的元素没有高度约束；有限枚举和随机实验不能处理“每个 A”的全称量词。
- 同一素数可整除大量两项和，故把大量配对直接转化为大量不同素数通常失效。
- 尚无检索到的现代方法链或近期部分结果可显著缩小缺口。

Proof-first 路线：

- 逐行重建 1934 的筛选引理，明确每次减半及最终矛盾的最强可推广形式；仅当发现可量化损失时才提出新主张。
- 研究“有限素数集覆盖所有两项和”时集合的模素数与 p-进结构，寻找能把反复覆盖转为集合大小上界的统一引理。
- 把正整数和 Lean 非负整数版本的夹逼、f 的单调性及有序/无序乘积等价性首先写成可机检的辅助结果，以排除语义漏洞。
- 唯一可选计算任务：在预注册一个具体有限结构引理后，搜索小 k 的模素数覆盖配置；必须预先指定参数域、证书、反证条件与停止点。

需要验证：

- 继续通过 MathSciNet、zbMATH、Crossref 引用链和 Erdős 1995/1997 问题集的原文，恢复 Er95c、Er97、Er97e 的准确书目信息并检查是否有后续结果。
- 对 1934 论文完整阅读并人工转录 n(k) 的精确量词、常数和其与 f 的反演关系。
- 若有人主张 Lean 已证明本题，要求其提供无 sorry 的固定提交、构建日志和与正整数版本的对应证明。

### 审计限制与人工复核理由

- 当前 Erdős Problems 页面的 open 标签及论坛无评论均为重要但非决定性证据；页面本身警告它可能遗漏文献。
- 1934 原论文的核心定理已通过公开扫描文本核对，但该扫描 OCR 有排版噪声；涉及 n(k) 的精确指数、常数和量词时应重新阅读原始页面图像。
- 对 2023–2026 年检索覆盖了精确短语、原始标题、作者、n(k) 和 arXiv 定向检索，但没有覆盖所有付费引文数据库、所有语言和所有未索引手稿。
- Er95c、Er97、Er97e 在当前页面的参考代码中出现，但本次未能以足够可靠的方式恢复其完整文献元数据，因而没有将其当作已核验来源。

- 应使用 MathSciNet、zbMATH 或图书馆目录恢复并核读 Er95c、Er97、Er97e，以确认它们是否报道了超出 1934 结果的工作。
- 应由数论专家核阅 1934 原文中相关 n(k) 猜想与当前 f(n) 的精确反演关系。
- 在投入实质研究前，应对近期引文链、作者网页及未索引预印本再做一轮人工检索；当前 likely_open 不等于证明没有后续解决。

<!-- DEEP_REVIEW:END -->
