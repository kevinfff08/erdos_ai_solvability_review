# Problem 18

## 基本信息

- 原始链接: https://www.erdosproblems.com/18
- LaTeX 页面: https://www.erdosproblems.com/latex/18
- 原始状态: `open`
- 奖金: `no`
- 主类别: `number theory`
- 原始标签: `number theory`, `divisors`, `factorials`
- 形式化状态: `yes`
- OEIS: `A005153`
- 原站备注字段: practical numbers

## 原问题

We call $m$ practical if every integer $1\leq n<m$ is the sum of distinct divisors of $m$. If $m$ is practical then let $h(m)$ be such that $h(m)$ many divisors always suffice.

Are there infinitely many practical $m$ such that\[h(m) < (\log\log m)^{O(1)}?\]Is it true that $h(n!)<n^{o(1)}$? Or perhaps even $h(n!)<(\log n)^{O(1)}$?

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `27/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- 题面或备注出现有限对象/计算线索
- 已有形式化陈述，可降低语义误读风险
- 存在 OEIS 数据入口，利于实验与反例搜索

### 主要障碍

- 所属标签偏证明密集：divisors, factorials, number theory
- 题面含渐近/无限对象线索：\ll, infinitely many, o(

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: divisors, factorials, number theory
- 有限/计算线索: finite, finitely
- 渐近/无限线索: \ll, infinitely many, o(
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **这是一个中等候选问题：GPT-5.5 级别模型不应被预期直接解决完整开放问题，但很可能能在阶乘情形、构造性上界、计算实验和形式化验证方面做出有价值推进。**
- 等级: `medium_candidate`
- 分数: `58/100`
- 信心: `medium`
- 可能路线: 可行路线是把 h(m) 转化为“用至多 k 个互异除数覆盖区间 [1,m)”的加性覆盖问题。对 n!，优先利用其除数集合极其稠密这一结构，尝试分块覆盖、贪心基底、平滑数/因子闭包、二进制式压缩表示或概率方法，目标先改进已知的 h(n!)<n，再寻找 n^{o(1)} 或 polylog n 的可验证中间命题。工具层面可结合 SAT/ILP/动态规划反例搜索、小 n 精确 h(n!) 计算、Lean/Isabelle 形式化已有引理，以及文献检索来定位 Vose 型构造是否可迁移到阶乘。

### 支持理由

- 问题已有非平凡但相对初等的入口：Erdos 给出 h(n!)<n，Vose 给出无限多个 practical m 满足 h(m) 远小于 log m，这说明并非完全缺少可扩展构造。
- 阶乘 n! 的除数集合高度结构化，适合模型结合计算发现分块表示模式，并把模式提升为证明草案。
- 该问题的目标是上界或无限构造，AI 工具链可以先产生可机检的充分条件，而不必完全刻画 practical numbers。
- formalized=yes 表明至少部分定义或相关命题已有形式化基础，利于把候选证明拆成可验证引理。
- 反例搜索和最优 h(n!) 计算能为猜想强度提供快速反馈，避免纯符号推理中的错误方向。

### 主要障碍

- 核心困难在于需要同时覆盖所有 1<=n<m，而不是多数整数或随机整数；最坏情况覆盖通常会破坏简单概率论证。
- 互异除数限制使问题不同于无限制硬币系统，局部贪心可行性不自动给出低项数全局上界。
- 从实验模式到渐近证明的跨度较大，尤其是 n^{o(1)} 或 polylog n 级别需要非常强的压缩表示。
- Vose 的无限 practical m 构造只给出约 (log m)^{1/2} 量级，和目标 (log log m)^{O(1)} 之间仍有巨大差距。
- 若依赖文献中的深层分布结果或平滑数估计，AI 生成证明很容易遗漏均匀性、常数范围和边界条件。

### 需要的验证

- 明确定义 h(m)：是最小 k，还是存在某个 k 使每个 1<=n<m 可由至多 k 个互异除数表示，并统一形式化表述。
- 对小 n! 精确计算或给出上下界表，验证模型提出的覆盖策略是否真实优于 h(n!)<n。
- 把任何候选构造写成可执行算法，并用独立 DP/SAT/ILP 检查覆盖区间与互异性约束。
- 将关键组合引理形式化，尤其是区间拼接、除数闭包、项数累加和边界覆盖。
- 做定向文献核查，确认是否已有更强的阶乘情形上界或对 Vose 方法的后续改进。

### 公开版思考摘要

我判断它不是低候选，因为问题结构清晰、阶乘情形有丰富可计算结构，且已有 h(n!)<n 和 Vose 型结果提供可追踪起点。它也不是高候选，因为目标上界极强，要求对所有整数的低项数互异除数表示，现有备注中的最好方向仍远离 loglog 级别。最现实的 AI 贡献是给出新的中间上界、可检验构造、反例排除范围或形式化验证框架，而不是一次性完成完整开放问题。

### 免责声明

以上是对 GPT-5.5 级别工具辅助模型处理该问题潜力的审查，不是该 Erdős 问题的证明或反驳。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `revised_open`
- 状态信心: `medium`
- 可行动性: `research_ready`
- 人工复核: `not_required`
- 独立研究 Prompt: [prompts/problem_18.md](../../prompts/problem_18.md)

### 状态结论

原始 1981 年表述把非 practical 的 n 定义为 S(n)=0，因此若不限制 n 为 practical，"无穷多个 n" 版本平凡成立。当前 Erdős Problems 页面已将主问题修订为只量化 practical m，并仍标为 open；其余两个关于 n! 的问题是并列但逻辑上不同的开放变体。未发现可核验的解决或反例声明。

### 当前规范陈述

设 Div(m) 为 m 的正因子集合。对 practical 整数 m，令 r_m(t)=min{|A|: A⊆Div(m) 且 Σ_{d∈A}d=t}（1≤t<m），并令 h(m)=max_{1≤t<m}r_m(t)。修订后的主目标是：是否存在固定常数 C>0，使得无穷多个 practical 整数 m 满足 h(m)<(log log m)^C？对数取自然对数，且这是渐近断言，故只考虑 log log m>0 的充分大 m。页面还并列两个不同问题：(B) 对每个 ε>0，充分大 n 均有 h(n!)<n^ε；(C) 存在固定 C>0，使充分大 n 均有 h(n!)<(log n)^C。(C) 蕴含 (B)，但二者均不等同于主目标。

```text
Let Div(m) be the set of positive divisors of m. For a practical integer m, define r_m(t)=min{|A|: A⊆Div(m) and Σ_{d∈A}d=t} for 1≤t<m, and h(m)=max_{1≤t<m} r_m(t). The repaired primary target is: does there exist a fixed real C>0 and infinitely many practical integers m such that h(m)<(log log m)^C? Here logs are natural and the assertion is asymptotic, hence only m with log log m>0 matter. The page additionally records two separate questions: (B) for every ε>0, h(n!)<n^ε for all sufficiently large n; and (C) for some fixed C>0, h(n!)<(log n)^C for all sufficiently large n. (C) implies (B), but neither is the same as the primary target.
```

### 陈述、量词与反例审计

- 歧义严重度: `material`
- 简单反例检查: `not_applicable`
- 检查说明: 对修订后的“practical m”主目标，未找到简单反例。对历史字面式则有直接的平凡化：Erdős 1981 将非 practical n 的 S(n) 定为 0，而任意素数 p>2 非 practical（其正因子仅为 1,p，不能表示 2）；故无穷多个非 practical n 自动满足 S(n)<(log log n)^C。这不是修订目标的反例，而是其必须加上 practical 限制的原因。
- 版本变化: Erdős 1981 年原文第 172 页定义 S(n)，并规定非 practical 时 S(n)=0，随后提出无穷多个 n 的 polylog(log n) 界及 250 美元奖励。2025–2026 年的 Erdős Problems 论坛讨论指出字面式会因非 practical 数而平凡；站点维护者最终同意该历史写法有缺陷并更新条目。当前页面将主问题明确为“无穷多个 practical m”，并把 h(n!) 的两个独立问题列为附加问题。Formal Conjectures 的 18.lean 也将其拆成三个 conjectures；该文件含 sorry，占位形式化不构成证明。

陈述问题：

- 1981 年原文定义 S(n)=0（当 n 非 practical）后，随即写“无穷多个 n”满足 S(n)<(log log n)^C；由于无穷多个大素数均非 practical，该字面命题平凡为真，不能是预期的奖励问题。
- 当前页面的“h(m) many divisors always suffice”省略了 h 的 max–min 次序及每个被表示整数可重新选择因子子集的量词；论坛和 Formal Conjectures 文件明确了这一点。
- 条目把主问题、n! 的 n^{o(1)} 问题和更强的 polylog(n) 问题合并为一个编号；它们不是单一命题。
- O(1) 与 o(1) 必须分别解释为固定指数 C 和“对任意 ε>0 最终成立”；允许指数随 m 或 n 变化会改变问题。
- 原文及部分现代文献在 practical 的范围上使用 <m 或 ≤m 的不同习惯。对大 m 的 h(m) 渐近问题无实质影响，因为 t=m 可由单个因子 m 表示，但定义时仍须固定。

需要固定的量词/约定：

- For each target t, the representing subset A may depend on t; no single subset is required to represent every t.
- The primary assertion is ∃C>0 ∃∞ practical m: h(m)<(log log m)^C.
- The factorial subpolynomial assertion is ∀ε>0 ∃n0 ∀n≥n0: h(n!)<n^ε.
- The factorial polylogarithmic assertion is ∃C>0 ∃n0 ∀n≥n0: h(n!)<(log n)^C.
- All inequalities are strict as on the current page; changing < to ≤ is asymptotically inessential only after an explicit adjustment of constants, not by silent convention.

### 文献与当前边界

已核验的主要结果：

- Erdős（1981，已出版会议论文）直接写下 S(n!)<n，并记载无穷多个 m 的较弱小项数构造；同页提出 polylog(log n) 形式并悬赏。原文的 S(n)=0 约定使未加 practical 限制的版本平凡，故只能把它作为历史来源而非最终规范陈述。
- Vose（1985，Bull. London Math. Soc.，同行评审）是当前数据库归因的最强直接 h(m) 结果：存在无穷多个 practical m 使 h(m)≪(log m)^{1/2}。本次核实了论文元数据；因出版商限制未能逐页复核证明，故该定理归因仍建议人工查阅全文。
- Weingartner（2015 预印本，后发表于 Q. J. Math.）证明 practical 数的计数渐近为 cx/log x；这说明 practical 数无穷且相对稀疏，但不缩小 h(m) 的 polylog(log m) 缺口。
- Pollack–Thompson（2012）研究的是另一函数 f(n)：可由 n 的因子表示的初始区间长度；其抽象明确不涉及本题的最坏表示项数 h(n)，不能混用。

最近相关工作：在针对精确 h(m)、h(n!)、作者名及近三年 arXiv/期刊检索后，未找到 2023–2026 年直接改善本题三个目标的可核验论文。Bettin–Grenié–Molteni–Sanna（2025）关于 Egyptian fractions 的预印本是主题相邻但不直接相关的最新工作；不能据此推断状态改变。

剩余核心：经修订的主核是：构造无穷多个 practical m，使其所有 t<m 的因子子集和表示均可在固定 polylog(log m) 项内完成；现有 Vose 界为 (log m)^{1/2} 量级。另有独立的阶乘核：先证明 h(n!)=n^{o(1)}，再可能强化到 (log n)^{O(1)}。后一命题蕴含前一命题。

已使用方法：

- 使用 practical 数的因子子集和表示，把 m 的因子分解为 Egyptian-fraction 表示；Vose 的工作是这一方向的已知基准。
- 通过显式 practical 数构造来控制最坏表示项数，而非只证明可表示性。
- practical 数的分布与因子分布估计提供候选数的背景筛选，但现有计数渐近本身不控制 h(m)。

争议或不确定性：

- Vose 论文全文本次不可访问；数据库对其 h(m) 定理的归因可信但尚未作逐行独立复核。
- 1981 年原文中较弱无穷多 m 界的 OCR 不完全清晰；最终审稿/研究前应从扫描页人工核对其精确分子、分母和常数。
- 没有找到近年直接论文不是“没有解决”的证明；开放状态主要由 2026-04-11 更新的当前数据库和其无解决声明支持。

### 证据来源

- [Some problems and results on additive and multiplicative number theory](https://renyi.hu/~p_erdos/1981-33.pdf) — Paul Erdős, 1981; `primary_paper`, `unknown`, directness=`direct`, reliability=`high`. 第 172 页可直接检查到：S(n) 是表示每个 1<m<n 所需因子数的最小统一上界，非 practical 时 S(n)=0；原文记载 S(n!)<n、无穷多个 m 的较弱界、polylog(log n) 猜想和 250 美元奖励。因此也直接暴露了未限制 practical n 时的平凡化问题。
- [Erdős Problem 18](https://www.erdosproblems.com/18) — Thomas F. Bloom / Erdős Problems contributors, 2026-04-11; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 当前记录将问题标记为 open，采用 practical m 的修订表述，列出 h(n!) 的两个变体，并记载 Erdős 的 h(n!)<n 与 Vose 的 h(m)≪(log m)^{1/2}。页面亦明确警告其状态不是完备文献证明。
- [Discussion thread for Erdős Problem 18](https://www.erdosproblems.com/forum/thread/18) — Thomas Bloom, Dogmachine, Woett, rws and forum contributors, 2025-10-30; `forum`, `informal_claim`, directness=`direct`, reliability=`medium`. 讨论明确记录了历史量词/非 practical 零值缺陷、每个被表示数须允许不同因子子集，以及维护者后来修订页面的理由；线程未列出任何完整或部分解答声明。
- [Egyptian Fractions](https://academic.oup.com/blms/article-abstract/17/1/21/296830) — Michael D. Vose, 1985-01; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`medium`. 核实 Vose 论文的题名、作者、期刊、卷期、页码 21–24 与 DOI 10.1112/blms/17.1.21。其关于 h(m) 的精确结论由当前问题页归因于该论文；本次无法绕过出版商限制检查全文证明。
- [Formal Conjectures: Erdős Problem 18](https://raw.githubusercontent.com/google-deepmind/formal-conjectures/main/FormalConjectures/ErdosProblems/18.lean) — Formal Conjectures Authors, 2026; `formalization`, `formalized_artifact`, directness=`direct`, reliability=`high`. 文件精确定义 practicalH 的 max–min 结构，分列主问题及两个 factorial 变体，并说明每个表示目标可选不同子集。所有研究级定理以 sorry 陈述，故它只形式化了陈述，未形式化解决方案。
- [Practical numbers and the distribution of divisors](https://arxiv.org/abs/1405.2585) — Andreas Weingartner, 2015-03-03; `preprint`, `preprint`, directness=`indirect`, reliability=`high`. 证明 practical 数计数的渐近式 cx/log x；它给出该类数的分布背景，但没有声称处理 h(m) 或阶乘变体。
- [A lower bound for the number of Egyptian fractions](https://arxiv.org/abs/2509.10030) — Sandro Bettin, Loïc Grenié, Giuseppe Molteni, Carlo Sanna, 2025-09-12; `preprint`, `preprint`, directness=`indirect`, reliability=`high`. 这是本次近三年检索中最接近的 Egyptian-fraction 文献之一；它研究分母有界时可表示有理数的数目，而非 fixed practical denominator 的最坏项数 h(m)，不能当作本题进展。

### 完成标准

- 肯定出口: Primary repaired target: prove that there exists a fixed C>0 and infinitely many practical m for which every t with 1≤t<m is a sum of at most (log log m)^C distinct positive divisors of m.
- 否定出口: Primary repaired target: prove that for every C>0, only finitely many practical m satisfy h(m)<(log log m)^C.

不构成完成：

- Showing the bound for non-practical n under Erdős's historical convention S(n)=0.
- Producing any finite list of practical m, even with exact values of h(m).
- Giving a bound (log log m)^{C(m)} with an exponent that is not uniformly fixed.
- Proving h(n!)<n or only a result about the factorial variants; these do not resolve the primary target.
- Showing that many individual t have short representations without controlling the maximum over all 1≤t<m.

正确性陷阱：

- Reverse neither the min over representations nor the max over target integers in the definition of h(m).
- The subset of divisors may depend on t; requiring one common subset is a different and generally impossible problem.
- Verify every selected summand is a distinct positive divisor of the same m.
- State the practicalness restriction explicitly; the historical zero convention for non-practical integers trivializes the unqualified infinitude statement.
- Keep the fixed-exponent quantifier outside the infinitely-many-m quantifier.
- Do not transfer a proof between the primary target and h(n!) without an explicit implication.

### 更新后的 AI 可解答性

- 等级: `low_to_medium_candidate`
- 分数: `28/100`
- 信心: `medium`
- 结论: 修订后的主目标定义清晰、可局部验证，但长期缺口从 (log m)^{1/2} 到 (log log m)^{O(1)} 很大，且目前缺少已知可渐进改进的中间定理；适合做严谨的结构性探索，不适合以有限计算或形式化占位文件作为突破依据。

支持理由：

- max–min 函数、量词与完整正反完成条件可精确定义，候选构造的每一步可检验。
- 有明确的已知构造基线和 practical 数理论背景。
- 三个问题已能分离，主问题可在不混淆阶乘变体的情况下独立研究。

主要障碍：

- 主目标是数十年未解的强渐近改进，现有基线与目标之间存在指数尺度差距。
- 最坏 t 的控制远强于证明所有 t 可表示；平均、计数或有限样本通常不足。
- 历史文献的符号与当前 h 的规范化不同，容易引入无效的“解决”。

Proof-first 路线：

- 从一个明确的 practical 数族出发，先证明“任意 t 的表示可按层级压缩”的固定引理，并追踪该引理产生的统一项数。
- 单独分析 n! 的因子结构，尝试证明可把任意目标分块为受控数量的可表示块；必须先给出从块分解到 h(n!) 的完整误差预算。
- 唯一可选计算任务：在预先写明的候选结构引理及有限范围停止条件下，精确计算小 n 的 h(n!) 或候选 practical m 的最坏目标；一旦区分该引理，立即停止并回到证明。

需要验证：

- 人工检查 Vose 1985 全文，确认其构造和 h(m) 定理的精确常数/量词。
- 人工检查 Erdős 1981 扫描第 172 页，消除 OCR 对较弱无穷多 m 界的歧义。
- 若出现任何新声称，检查其是否真的控制全部 t<m、固定指数和无限多 practical m，而不是只给实例或非 practical 零约定。

### 审计限制与人工复核理由

- 本次可公开检索范围内未发现 2023–2026 年直接处理 h(m) 或 h(n!) 的论文；这不能逻辑证明不存在未索引、付费墙后或尚未检出的结果。
- Vose 1985 的出版商页面可核验元数据但阻止全文访问；其精确 h(m) 定理在此主要依赖当前数据库的归因，应在研究开始前人工复核原文。
- Erdős 1981 PDF 的 OCR 对一个较弱上界式有排版噪声；关于历史零约定、奖励和主要 polylog(log n) 句子的证据清楚，但若引用较弱界的精确形式应查原页图像。
- 当前问题页明确声明其 open 标签反映维护者信念而非完备文献证明；因此状态置信度为中等而非高。

- 无

<!-- DEEP_REVIEW:END -->
