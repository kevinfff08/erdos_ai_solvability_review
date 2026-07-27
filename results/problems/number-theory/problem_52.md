# Problem 52

## 基本信息

- 原始链接: https://www.erdosproblems.com/52
- LaTeX 页面: https://www.erdosproblems.com/latex/52
- 原始状态: `open`
- 奖金: `$250`
- 主类别: `number theory`
- 原始标签: `number theory`, `additive combinatorics`
- 形式化状态: `yes`
- OEIS: `A263996`
- 原站备注字段: sum-product problem

## 原问题

Let $A$ be a finite set of integers. Is it true that for every $\epsilon>0$\[\max( \lvert A+A\rvert,\lvert AA\rvert)\gg_\epsilon \lvert A\rvert^{2-\epsilon}?\]

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `26/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- 题面或备注出现有限对象/计算线索
- 已有形式化陈述，可降低语义误读风险
- 存在 OEIS 数据入口，利于实验与反例搜索

### 主要障碍

- 所属标签偏证明密集：additive combinatorics, number theory
- 题面含渐近/无限对象线索：\gg, o(
- 原记录含奖金 $250，说明该题被长期视为高价值难题；这不是否定依据，但提高验证门槛。

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: additive combinatorics, number theory
- 有限/计算线索: finite
- 渐近/无限线索: \gg, o(
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **不太可能在一次端到端研究中完成完整猜想；但作为“显著推进或验证局部路线”的候选有一定价值，尤其适合自动化整理已知证明、形式化关键引理、搜索极值构造和做指数优化。**
- 等级: `low_to_medium_candidate`
- 分数: `38/100`
- 信心: `medium`
- 可能路线: 最现实的路线不是直接证明 |A+A| 或 |AA| 接近 |A|^2，而是把问题拆成可验证的子任务：形式化现有 sum-product 证明框架，自动检查能量不等式、覆盖引理和 incidence bound 的依赖；用符号优化或线性规划搜索现有方法中的指数瓶颈；用计算反例搜索和结构化构造搜索验证小规模极值；尝试在附加假设下证明更强局部结论，例如排除某类高加法能量且高乘法能量的整数集。

### 支持理由

- 问题已有 formalized=yes，说明可以把部分目标、定义或已知引理接入形式化证明工具，降低验证新证明草稿的风险。
- 题目属于加性组合和数论交叉，存在大量可机械化的中间对象：和集、积集、能量、分解、图/超图 incidence、指数不等式链。
- 工具增强模型可以在文献检索、证明依赖图整理、已知 bound 的重构、参数优化和小规模搜索方面发挥作用，这些任务不要求一次性产生全新核心思想。
- 给出的记录指数 1962/1469 约为 1.3356，距离目标 2-epsilon 很远，因此即使不能解决完整猜想，也可能通过发现局部改进、形式化验证或瓶颈定位构成有意义推进。

### 主要障碍

- 完整结论要求几乎二次增长，远超当前已知指数，说明现有技术与目标之间存在结构性缺口。
- 整数 sum-product 的困难在于需要排除同时具有强加法结构和强乘法结构的复杂集合；这通常需要新的组合洞察，而不只是代数化推导。
- 计算搜索只能覆盖有限规模，难以直接支持渐近下界；未发现反例也不能显著证明 conjecture。
- 形式化证明工具能提高可靠性，但如果缺少新的数学核心引理，形式化本身不会自动弥合指数差距。
- 已有上界接近 |A|^2 乘以次指数损失，说明猜想尺度很精细，任何证明都必须处理接近极值的构造族。

### 需要的验证

- 复现 problem JSON 中提到的当前最佳下界，并形式化记录每个外部定理依赖。
- 建立小规模整数集搜索基准，确认模型提出的任何候选反例或极值族是否真实降低 max(|A+A|,|AA|)。
- 对模型生成的新引理做独立证明检查，最好用 Lean/Isabelle 或至少用人工可审计的证明脚本验证。
- 将任何声称改进指数的证明转化为明确的不等式链和参数优化问题，检查是否存在循环引用、隐藏常数依赖或 o(1) 滥用。
- 验证新路线是否真正针对整数情形，而不是无意使用了有限域、实数或复数情形中特有的假设。

### 公开版思考摘要

这个问题是经典 sum-product 猜想的强形式：要求对任意有限整数集，和集或积集几乎达到二次规模。根据给定 JSON，当前记录指数只有约 1.3356，而目标是 2-epsilon，差距很大，所以 GPT-5.5 级模型直接解决完整问题的概率较低。不过该问题结构清晰、已经形式化、并且有丰富的可计算中间框架，因此模型配合计算和形式化工具有可能在验证、重构、局部改进、参数搜索和反例排查方面产生实质贡献。

### 免责声明

以上是 AI 可攻关性评估，不是该 Erdős 问题的证明、反例或完整研究方案。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `confirmed_open`
- 状态信心: `high`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_52.md](../../prompts/problem_52.md)

### 状态结论

题目字面上是整数 Z 上的 Erdős–Szemerédi 和积猜想，至 2026-07-27 仍为开放问题。2026 年 Bloom、Sawin、Schildkraut、Zhelezov 对实数 R 的版本给出了反例，但其集合由次数随集合大小增长的数域中的代数整数构成；这不产生整数反例。Erdős Problems 当前页、该站作者 Thomas Bloom 的后续说明，以及近期定向检索均一致将整数版本保留为开放。最佳通用下界记录为 Cushman 的 1962/1469−o(1)。

### 当前规范陈述

对任意有限非空整数集 A⊆Z，定义 A+A={a+b:a,b∈A}、AA={ab:a,b∈A}。需证明或否证：对每个 ε∈(0,1)，存在只依赖于 ε 的常数 cε>0，使得对每个这样的 A 都有 max(|A+A|,|AA|)≥cε|A|^(2−ε)。等价地，固定 |A|=n 时该最大值的最小可能量级为 n^(2−o(1))。

```text
For a finite nonempty set A⊆Z, define A+A={a+b:a,b∈A} and AA={ab:a,b∈A}. Prove or disprove: for every ε∈(0,1) there exists a constant cε>0, depending only on ε, such that for every finite nonempty A⊆Z, max(|A+A|,|AA|)≥cε|A|^(2−ε). Equivalently, the minimum of this maximum over |A|=n is n^(2−o(1)) as n→∞.
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 未找到针对 A⊆Z 的简单或文献化反例。Bloom–Sawin–Schildkraut–Zhelezov 的实数构造不能直接视为整数构造：其元素属于次数约为 log|A| 的数域，官方后续说明明确称整数反例是否存在仍开放。
- 版本变化: Erdős Problems 的修订记录显示：2026-05-28 后，页面保留了整数原命题及 Cushman 的记录下界，同时加入“实数版本已被否证”的说明，并将实数和高阶实数变体与整数问题区分。输入 JSON 中“实数当前最佳下界”的旧式表述缺少这一关键更新；整数目标未被替换。

陈述问题：

- 原题的 ≫ε 未显式写出常数只可依赖 ε，且未说明是否排除空集；按加法组合标准约定，应解释为存在统一于 A 的正数 cε。
- 原文写 every ε>0；对 ε≥1 该断言由平凡线性下界覆盖。为避免零基数与负指数等边界记号问题，标准且形式化的核心范围是 0<ε<1。
- 2026 年实数版本已被否证，不能把“整数、实数或复数皆无特殊区别”的历史性评论当成可用推论。整数命题本身没有被改写或否证。

需要固定的量词/约定：

- For every ε with 0<ε<1, choose one cε>0 before A is quantified; cε may not depend on A or |A|.
- A+A and AA use all ordered choices a,b∈A but are sets, so repeated representations count once.
- The conventional n^(2−o(1)) formulation is equivalent to the displayed all-ε lower bounds, after allowing constants depending on ε.

### 文献与当前边界

已核验的主要结果：

- Erdős–Szemerédi（1983，同行出版的论文集章节）证明存在绝对 c>0 使通用下界为 |A|^(1+c)，并构造任意大整数集使两个集合的最大基数至多 |A|² exp(−c log|A|/loglog|A|)。这说明仅有常数倍于 |A|² 的改进不能否证猜想。
- 现代通用下界路线经由点线关联、Szemerédi–Trotter 型估计、加性能量和控制/分解工具推进：Bloom（2025 预印本）达到 1270/951−ε；Cushman（2025 预印本，2026 修订）达到 4/3+10/4407−ε=1962/1469−ε。该实数定理自动覆盖整数集。
- 受限整数集可以有更强结果：Hanson–Rudnev–Shkredov–Zhelezov（2023，2025 年 Compositio Mathematica）对素因子数适度受限的集合给出 5/3−o(1)；Bloom（2025 预印本）对每个元素有 O(1) 个不同素因子的集合给出 17/10−o(1)。这些都不是一般 A⊆Z 的结论。
- Bloom–Sawin–Schildkraut–Zhelezov（2026 预印本）否证了 R 上的对应猜想，并否证了 R 上高阶版本；这推翻了“整数与实数没有本质区别”的启发式，但没有改变本题的整数状态。

最近相关工作：最直接的通用记录仍是 Cushman 的 2026-01 修订预印本；最新改变问题背景的工作是 BSSZ 的 2026-05 实数反例及 Bloom 的 2026-05 说明。检索至审计日未发现声称或证明一般整数版本的完整正解或整数反例。

剩余核心：必须在所有有限整数集上取得近二次下界，或构造一族任意大的整数集，使两个集合同时具有真正的幂次次二次上界。实数数域构造、有限域/复数构造、以及素因子受限情形都不能关闭这个核心。

已使用方法：

- Szemerédi–Trotter 关联几何及其和积应用。
- 加性能量、高阶能量、Balog–Szemerédi–Gowers 型结构提取。
- 控制量与集合分解；改进控制指数会传播到和积下界。
- 整数算术方法：素因子数限制、乘法结构与丢番图障碍。
- 反例方向的数域格点/单位构造；已知实数构造不能直接降到 Z。

争议或不确定性：

- Cushman 与 BSSZ 均为预印本；本审计核对了其摘要、版本和适用域，未逐行独立复核完整证明。
- Erdős Problems 自己声明其开放标签反映维护者的知识状态；不过其 2026-05 修订、讨论串与作者说明相互一致，且精确检索未发现相反的整数结果。
- “当前记录”按一般整数集解释；对算术受限子类有明显更高指数，不能将其误报为本题的无条件记录。

### 证据来源

- [Erdős Problem 52: The sum-product problem](https://www.erdosproblems.com/52) — Thomas F. Bloom / Erdős Problems, 2026-05-28; `problem_page`, `database_record`, directness=`direct`, reliability=`high`. 当前题页将 A⊆Z 的命题标为 OPEN，给出 Cushman 的 1962/1469−o(1) 记录，并明确注明实数版本已失效。
- [Erdős Problem 52 LaTeX source](https://www.erdosproblems.com/latex/52) — Thomas F. Bloom / Erdős Problems, 2026-05-28; `problem_page`, `database_record`, directness=`direct`, reliability=`high`. 核对了当前题目文字、引用和整数域限定。
- [Discussion thread for Erdős Problem 52](https://www.erdosproblems.com/forum/thread/52) — Thomas F. Bloom and forum contributors, 2026-06-06; `forum`, `informal_claim`, directness=`indirect`, reliability=`medium`. 论坛记录了 2026 年实数反例及题页更新；它不是整数命题已解的证据。
- [On sums and products of integers](https://users.renyi.hu/~p_erdos/1983-16.pdf) — Paul Erdős; Endre Szemerédi, 1983; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 原始论文提出近二次型猜想，证明某个 1+c 下界，并给出接近二次但带次多项式节省的构造性上界。
- [A Note on the Sum-Product Problem and the Convex Sumset Problem](https://arxiv.org/abs/2512.13849) — Adam Cushman, 2025-12-15; revised 2026-01-29; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 对任意有限 A⊆R 证明 max(|A+A|,|AA|)≫ε|A|^(4/3+10/4407−ε)，即 1962/1469−ε；因 Z⊆R，该结果适用于整数集。
- [Control and its applications in additive combinatorics](https://arxiv.org/abs/2501.09470) — Thomas F. Bloom, 2025-01-16; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 给出 Cushman 之前的 1270/951 和积指数，并说明控制量、能量和 Szemerédi–Trotter 型工具的作用。
- [The sum-product conjecture is false for real numbers](https://arxiv.org/abs/2605.28781) — Thomas F. Bloom; Will Sawin; Carl Schildkraut; Dmitrii Zhelezov, 2026-05-27; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 声称并给出一族任意大的实数集，使 max(|A+A|,|AA|)≤|A|^(2−c)；摘要明确元素是高次数数域中的代数整数，故不直接否证整数版本。
- [Sum-product, unit distances, and number fields](https://www.erdosproblems.com/forum/thread/blog%3A6) — Thomas F. Bloom, 2026-05-31; `author_page`, `informal_claim`, directness=`direct`, reliability=`high`. 作者解释实数构造为何远非整数集，并明确写道整数版本的证明或反例仍广泛开放。
- [The sum-product problem for integers with few prime factors](https://arxiv.org/abs/2305.04038) — Brandon Hanson; Misha Rudnev; Ilya Shkredov; Dmitrii Zhelezov, 2023-05-06; `preprint`, `peer_reviewed`, directness=`direct`, reliability=`high`. 对素因子数受限的整数集得到 5/3−o(1) 的条件性下界，显示整数算术限制能给出远强于通用记录的结果。
- [More on the sum-product problem for integers with few prime factors](https://arxiv.org/abs/2512.04931) — Thomas F. Bloom, 2025-12-04; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 若 A 中每个整数只含 O(1) 个不同素因子，则得到 17/10−o(1) 的条件性下界；不适用于一般整数集。
- [FormalConjectures: Erdős Problem 52 formal statement](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/52.lean) — Formal Conjectures Authors, 2026; `formalization`, `formalized_artifact`, directness=`direct`, reliability=`high`. Lean 文件形式化了量词结构：0<ε<1、存在 C>0、对所有 Finset Z 的不等式；定理证明体含 sorry，因此它是已形式化的陈述，不是机器验证的解答。

### 完成标准

- 肯定出口: A complete affirmative resolution proves that for every ε∈(0,1) there is cε>0 such that every finite nonempty A⊆Z satisfies max(|A+A|,|AA|)≥cε|A|^(2−ε), with every dependence and asymptotic conversion justified.
- 否定出口: A complete negative resolution proves the negation; in particular, it suffices to exhibit constants δ,C>0 and arbitrarily large finite A⊆Z with max(|A+A|,|AA|)≤C|A|^(2−δ). Such a family contradicts the conjecture by taking any 0<ε<δ.

不构成完成：

- Improving 1962/1469 by a fixed amount, while valuable, is not a complete resolution.
- A result only for A⊆R, C, a finite field, p-adics, or a number field is not a result for A⊆Z.
- A bound under a bounded-prime-factor, positivity, density, or other structural hypothesis does not settle arbitrary integer sets.
- A finite search, or a construction giving only o(1), logarithmic, or fixed-constant savings from |A|², does not disprove the conjecture.
- A Lean statement containing sorry/admit is not a formal proof of either outcome.

正确性陷阱：

- Keep cε independent of A, n, height, and all auxiliary parameters.
- Do not transfer a real algebraic-integer construction to Z without an injective encoding that simultaneously preserves the relevant sum and product collision counts.
- For a claimed counterexample, prove arbitrarily large cardinalities and a fixed δ>0; quantify all implied constants.
- For a positive proof, distinguish an exponent α−o(1) from the all-ε assertion and account for logarithmic losses.
- Audit zero, negative integers, duplicate representations, and the use of set cardinalities rather than representation multiplicities.

### 更新后的 AI 可解答性

- 等级: `low_candidate`
- 分数: `6/100`
- 信心: `high`
- 结论: 这是定义清楚、可检验但极其困难的开放目标；适合长期、证明优先的研究审查，不适合把有限计算或实数反例迁移当作高概率解法。

支持理由：

- 命题具有精确的全称量词形式，正反两种完成条件都可独立验证，且已有 Lean 陈述可用于终检。
- 存在具体的成熟技术脉络和若干受限整数子类结果，可产生可审查的中间引理。
- 实数版本最近被否证，为整数问题提供了重要的反例设计线索和边界条件。

主要障碍：

- 通用最佳指数 1.3356 与目标 2 的差距极大，且该问题历经四十余年未解。
- 实数反例表明传统的统一域直觉失效；将高次数代数整数构造转化为整数集正是核心障碍而非技术细节。
- 大量较强结果依赖额外算术限制，容易误把条件性进展当成一般结论。

Proof-first 路线：

- 先选择一个可陈述为一般整数引理的目标，例如从小加法/乘法集合导出可量化的整数结构；只有在该引理与全局指数闭合相关时才投入。
- 并行检验两个互不依赖的方向：强化下界链条，或严格寻找整数反例族；每个方向先写出会导致完整结论的定量阈值。
- 可选的唯一计算任务只能用于一个明确、有限、可停止的局部命题或候选构造碰撞验证，不能以枚举小集合代替渐近证明。

需要验证：

- 若有新声称，先核验其域确为 Z、量词确为任意有限集合、并且常数不随集合参数变化。
- 对 Cushman 的指数换算核验 4/3+10/4407=1962/1469，并确认其定理覆盖实数从而覆盖整数。
- 对任何依赖 BSSZ 的论证，核验它没有把数域中的代数整数错误替换为有理数或整数。
- 若使用 Lean，须移除 sorry 并在固定依赖版本上由内核成功编译。

### 审计限制与人工复核理由

- 本审计使用公开网页和论文页面进行状态核验；未逐行重审 Cushman 或 BSSZ 预印本的完整证明。
- 开放性不能由未找到新论文在逻辑上证明；高置信度来自官方当前页、其修订历史、作者后续说明和多组精确检索的一致性。
- 当前记录的最终同行评审状态可能在审计后变化，后续研究启动前应重新检查 arXiv 版本和正式出版信息。

- 若研究代理拟把实数反例作为启发或障碍，数学审阅者应复核其完整证明以及不能转化为整数反例的关键点。
- Cushman 的记录结果为预印本；在将其作为严格基线或引用于正式工作前，应核对最新版本、勘误和出版状态。
- 任何后续声称必须优先接受整数域、量词顺序和统一常数的人工对抗审查。

<!-- DEEP_REVIEW:END -->
