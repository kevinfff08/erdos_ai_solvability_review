# Problem 90

## 基本信息

- 原始链接: https://www.erdosproblems.com/90
- LaTeX 页面: https://www.erdosproblems.com/latex/90
- 原始状态: `open`
- 奖金: `$500`
- 主类别: `geometry`
- 原始标签: `geometry`, `distances`
- 形式化状态: `yes`
- OEIS: `A186705`
- 原站备注字段: unit distance problem

## 原问题

Does every set of $n$ distinct points in $\mathbb{R}^2$ contain at most $n^{1+O(1/\log\log n)}$ many pairs which are distance 1 apart?

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `25/100`
- 建议路线: 优先提取等价表述、尝试特殊情形、寻找可计算子问题，再决定是否进入证明搜索。

## 判断依据

### 有利因素

- 已有形式化陈述，可降低语义误读风险
- 存在 OEIS 数据入口，利于实验与反例搜索

### 主要障碍

- 所属标签偏证明密集：distances, geometry
- 题面含渐近/无限对象线索：\gg, o(
- 原记录含奖金 $500，说明该题被长期视为高价值难题；这不是否定依据，但提高验证门槛。
- 缺少明显有限搜索入口。

### 公开版思考过程摘要

- 先识别问题类型：无限/渐近或抽象证明倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: distances, geometry
- 有限/计算线索: 无
- 渐近/无限线索: \gg, o(
- 构造/存在性线索: construct

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **低到中等候选。GPT-5.5 配合计算、形式化证明和文献检索，较可能复现并形式化已知的 O(n^{4/3}) 上界、整理障碍、检验候选构造或验证局部引理；但直接证明题目要求的 n^{1+O(1/log log n)} 上界概率很低。真正突破需要利用欧氏度量的特殊结构并越过长期存在的 n^{4/3} 关联几何障碍。**
- 等级: `low_to_medium_candidate`
- 分数: `28/100`
- 信心: `medium`
- 可能路线: 较现实的路线是：先机器辅助重建 Spencer--Szemeredi--Trotter 型上界及其形式化版本；再针对欧氏距离图寻找不可推广到 Valtr 度量的特殊引理，例如圆交结构、代数曲线约束、能量估计或格点型极端例的稳定性；用计算搜索排除错误强化命题，并把任何新局部不等式交给证明助手验证。

### 支持理由

- 问题已有形式化标记，适合用证明助手验证已知引理、定义和有限组合步骤。
- 题目结构清楚：目标是单位距离图的全局边数上界，工具可以有效辅助关联几何、图论分解和反例搜索。
- 计算可以系统检查小规模极端配置、格点构造和候选归纳分解，帮助发现错误命题或可疑瓶颈。
- 文献检索可帮助定位 1946 以来的已知上界、障碍和相关技术，避免重复已失败路线。

### 主要障碍

- 这是经典单位距离问题的强形式，长期未突破 O(n^{4/3}) 上界到 n^{1+o(1)} 方向。
- 题目备注明确指出，SST 方法可推广到某些非欧氏度量，而这些度量存在远多于目标量级的单位距离对；因此必须捕捉非常细的欧氏特性。
- 有限计算或小 n 搜索不能直接证明渐近上界，也很难排除大规模代数或格点近似构造。
- 候选证明很容易隐含未证的均匀性、退化配置排除或 incidence bound 强化，需要高度严格的验证。

### 需要的验证

- 验证任何新上界是否真正给出 n^{1+O(1/log log n)}，而不是只改进常数或局部情形。
- 检查证明是否在欧氏距离条件上使用了不可替代的特殊性质，并明确为什么不适用于 Valtr 类型度量障碍。
- 对所有退化情形进行形式化或准形式化审计，包括共圆、共线、重复距离结构和高重合关联。
- 用已知格点下界测试命题的最优性，确保不会错误推出比已知构造更强的上界。
- 进行完整文献核对，确认新引理不是已知失败路线的重述。

### 公开版思考摘要

该问题可被 AI 工具链显著辅助审查、形式化和局部推进，但不像适合纯计算穷举的问题。核心难点不是缺少搜索，而是需要发现能区分欧氏平面和更一般度量的深层几何机制。GPT-5.5 级别模型有希望提高验证质量、整理路线和发现可测试子命题；完整解决的可信度仍低。

### 免责声明

以上是对 AI 可推进性的审查，不是该 Erdős 问题的解答，也未声称给出了新的单位距离上界。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `disproved`
- 状态信心: `high`
- 可行动性: `closed_verification_only`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_90.md](../../prompts/problem_90.md)

### 状态结论

原命题已被否定，而非仍属开放问题。2026 年的可检查论文给出固定 ε>0 及无穷多个 n，使某些 n 点欧氏平面点集具有至少 n^{1+ε} 条单位距离对；这与“存在常数 C，使所有充分大的 n 均有 u(n)≤n^{1+C/log log n}”矛盾。Sawin 随后给出显式指数 1.014114 的版本。精确的 u(n) 增长率和 4/3 上界的改进仍开放，但它们不是输入中这条断言。

### 当前规范陈述

对每个正整数 n，令 u(n)=max_{P⊂R^2, |P|=n} #{ {x,y}⊂P: ||x-y||_2=1 }，其中计数的是无序且不同的点对。原猜想的精确表述为：存在常数 C>0、N，使得对每个 n≥N（此时 log log n 有定义且为正），都有 u(n)≤n^{1+C/log log n}。对数底的改变只会改变常数 C。

```text
For each positive integer n, let u(n):=max_{P⊂R^2, |P|=n} #{ {x,y}⊂P : ||x-y||_2=1 }, where pairs are unordered and x≠y. The canonical literal conjecture is: there exist constants C>0 and N such that, for every integer n≥N (hence log log n is defined and positive), u(n)≤n^{1+C/log log n}. The logarithm base is immaterial after changing C. This is the standard precise reading of u(n)≤n^{1+O(1/log log n)}.
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `counterexample_found`
- 检查说明: 没有发现初等小参数反例；反例是深的渐近构造。Alon 等人的人类核验预印本证明存在固定 ε>0 和 |P_i|→∞，使单位距离对数至少 |P_i|^{1+ε}；Sawin 给出显式 1.014114 指数。令 i→∞ 后，固定 ε 终将大于任意固定 C/log log |P_i|，故该构造严格否定原断言。
- 版本变化: 未发现把原猜想改写为另一条等价开放命题的正式修订。2026 年的结果改变的是其真值：原上界猜想被反例否定。残留的广义研究问题是确定或改进 u(n) 的上下界；当前已核验的区间仍为 n^{1+0.014114}/O(1)（在无穷多个 n 上）至 O(n^{4/3})，但这不是原 #90 断言的“修订版”。

陈述问题：

- 输入的“大 O”与“充分大 n”未显式量化；按标准渐近约定可唯一重建为存在固定 C、N 的全称上界。
- “pairs”应按通常组合惯例理解为无序不同点对；改用有序对只差常数 2，不改变真假。
- 输入记录截至 2025 年仍标为 open；这已被 2026 年的反例结果取代。
- “单位距离问题”也常泛指求精确渐近增长率的更广问题；该更广问题仍未解决，但不能把它混同为这条已被否定的上界猜想。

需要固定的量词/约定：

- The O-constant must be fixed independently of n and of the point set.
- The asserted upper bound is required for every sufficiently large integer n and every n-point set P⊂R^2.
- A counterexample on an unbounded sequence n_i→∞ with u(n_i)≥n_i^{1+ε} for one fixed ε>0 refutes the conjecture.
- The distance is the Euclidean norm; results for generic, strictly convex, or other norms do not settle this Euclidean statement.

### 文献与当前边界

已核验的主要结果：

- Erdős（1946；由 2026 年论文回顾）给出平方格型下界 n^{1+Ω(1/log log n)}，并提出近线性上界猜想。
- Kővári–Sós–Turán 路径给出初等 O(n^{3/2})：欧氏单位距离图不含 K_{2,3}，因为两单位圆至多交于两点。
- Spencer、Szemerédi、Trotter（1984）证明 O(n^{4/3})；截至所审计的 2026 主来源，这仍是一般欧氏平面的最好已知上界。
- Currier–Solymosi（2025，预印本）证明方向数至多 O(n^{1/3}) 时单位距离数为 o(n^{4/3})，给出接近 4/3 极端情形的方向结构限制。
- Alon 等（2026，预印本）证明存在固定 ε>0 和无穷点集序列，单位距离数至少 n^{1+ε}，从定性上反驳原猜想。
- Sawin（2026，预印本）把该下界显式化为 n^{1.014114}/C（对任意大的 n），从而给出可量化反例。

最近相关工作：截至 2026-07-27，最晚检得的论文式后续工作是 Emmerich（arXiv:2606.03419，2026-06-02），其报告计算证书把 Sawin 型指数提高到约 1.0152；它是未同行评审的单作者预印本，尚未独立重验。MathOverflow/论坛还报告更高的约 1.03583 增益，但该答案本身承认部分相关改进曾有记账问题，故不应作为已核验的最强定理。

剩余核心：若研究目标是广义单位距离问题，核心仍是确定 u(n) 的真实渐近阶，尤其是缩小固定幂下界与 O(n^{4/3}) 上界之间的巨大差距，或证明依赖于欧氏结构的新上界。该目标须另行明确提出；原 #90 的 n^{1+O(1/log log n)} 上界已无待解内容。

已使用方法：

- 点–单位圆关联、交叉数与 Szemerédi–Trotter 型方法；这些自然地停在 4/3 障碍附近。
- 利用 K_{2,3}-free 性质的极值图论。
- 方向数限制等结构性组合几何。
- 代数数论构造：CM 域、类群抽屉原理、低根判别式的无穷塔、Golod–Shafarevich 与 Frobenius/分裂素数控制，再经高维格点投影产生平面单位距离。
- 对 Sawin 参数的有限、可证书化优化；只能用于验证明确不等式，不能替代构造定理的证明。

争议或不确定性：

- 闭合所需的定性反例有两个可检查的 2026 预印本来源，且其中一份由多位数学家署名为人类核验版本；但截至审计日未确认同行评审发表或完整无公理机器形式化。
- 2026 年后续显式指数的“纪录”快速变化；论坛、MathOverflow 和单作者计算预印本的数值主张不应未经逐项审计就并入已核验定理。
- 正式化文档包装了命题及蕴含，但论坛说明某个形式化版本仍引入额外公理；它不能单独取代对数论证明的审阅。

### 证据来源

- [Erdős Problem 90](https://www.erdosproblems.com/90) — Thomas F. Bloom / Erdős Problems, date unknown; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 原始数据库条目给出的历史猜想、引用和 2025 年“open”标签；该旧标签不构成 2026 年状态的决定性证据。直接抓取该页及 LaTeX 页时服务返回错误，故未据其旧状态作结论。
- [Planar Point Sets with Many Unit Distances](https://cdn.openai.com/pdf/74c24085-19b0-4534-9c90-465b8e29ad73/unit-distance-proof.pdf) — OpenAI, 2026-05-20; `primary_paper`, `preprint`, directness=`direct`, reliability=`high`. 定义 ν(n) 为 n 点集的最大无序单位距离对数，并陈述：存在固定 δ>0 与无穷多个 n，使 ν(n)≥n^{1+δ}；文中明确说明这否定 Erdős 猜想，并回顾 SST 的 O(n^{4/3}) 上界。
- [Remarks on the disproof of the unit distance conjecture](https://arxiv.org/abs/2605.20695) — Noga Alon, Thomas F. Bloom, W. T. Gowers, Daniel Litt, Will Sawin, Arul Shankar, Jacob Tsimerman, Victor Wang, Melanie Matchett Wood, 2026-05-20; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 给出人类消化、核验并声称完整证明的 Theorem 1.1：存在 ε>0 和 |P_i|→∞ 的点集序列，其单位距离数至少 |P_i|^{1+ε}；同时说明最优已知上界仍为 O(n^{4/3})。
- [An explicit lower bound for the unit distance problem](https://arxiv.org/abs/2605.20579) — Will Sawin, 2026-05-20; `preprint`, `preprint`, directness=`direct`, reliability=`high`. Theorem 1 给出显式构造：对任意大的 n，存在 n 点集具有至少 n^{1.014114}/C 个单位距离（按其计数约定）；这独立地提供固定正指数增益并足以否定原猜想。
- [Publications of Endre Szemerédi](https://www.renyi.hu/~szemered/pub.html) — Endre Szemerédi, 1984; `author_page`, `database_record`, directness=`indirect`, reliability=`high`. 确认 Spencer–Szemerédi–Trotter 的《Unit distances in the Euclidean plane》发表于 1984；2026 年两份主来源均将 O(n^{4/3}) 归于该工作。
- [Many unit distances requires many directions](https://arxiv.org/abs/2504.04208) — Gabriel Currier, József Solymosi, 2025-04-05; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 证明：若单位距离只来自至多 O(n^{1/3}) 个方向，则其数为 o(n^{4/3})；这是原猜想被否定前后的相关结构性限制，并未改善一般上界。
- [Optimizing Explicit Unit-Distance Lower-Bound Certificates](https://arxiv.org/abs/2606.03419) — Michael T. M. Emmerich, 2026-06-02; `preprint`, `preprint`, directness=`direct`, reliability=`medium`. 报告一个可复现计算证书管线，并声称把 Sawin 型构造的显式指数提高到约 1.0152。该未同行评审的后续量化声明不影响 #90 已被否定的结论，且未在本审计中独立验证。
- [What is the unit distance exponent?](https://mathoverflow.net/questions/511514/what-is-the-unit-distance-exponent?noredirect=1) — Eric Naslund and other MathOverflow contributors, 2026-05-21; `forum`, `informal_claim`, directness=`direct`, reliability=`medium`. 记录 2026 年对显式指数的快速改进和修正；Naslund 的约 0.03583 增益为详述但非正式论文的答案，作者与 Sawin 的评论也指出部分其他计算/记账主张有缺口。因此不能作为本审计的已核验“最佳定理”。
- [FormalConjectures.ErdosProblems.«90»](https://google-deepmind.github.io/formal-conjectures/doc/FormalConjectures/ErdosProblems/90.html) — Formal Conjectures project, date unknown; `formalization`, `formalized_artifact`, directness=`indirect`, reliability=`medium`. 形式化文档明确将 #90 标为 2026 年已被反驳，编码 u(n)、原渐近命题、显式 Sawin 变体及其逻辑蕴含。该页是有价值的逻辑包装证据，但本审计未把它视作对全部数论构造的无公理独立核验。
- [90 Discussion Thread](https://www.erdosproblems.com/forum/thread/90) — Erdős Problems forum contributors, 2026-05-20; `forum`, `informal_claim`, directness=`indirect`, reliability=`medium`. 官方问题论坛已讨论反例、后续指数与一个带额外公理的形式化尝试；它佐证社区更新与不确定性，但不作为闭合结论的证明。

### 完成标准

- 肯定出口: For this closed-record audit, an affirmative verification is a complete, checkable proof of: there exist ε>0 and finite P_i⊂R^2 with |P_i|→∞ and ν(P_i)≥|P_i|^{1+ε}. It must then explicitly derive that no fixed C,N can make ν(n)≤n^{1+C/log log n} for every n≥N.
- 否定出口: A negative verification outcome would identify a material invalid step in every presently relied-on counterexample proof, or show that its conclusion does not supply one fixed positive ε along an unbounded sequence, so that it does not logically contradict the quantified original conjecture. This would invalidate the claimed closure, not prove the original conjecture.

不构成完成：

- A construction with many unit distances for only finitely many n.
- A lower bound n^{1+c/log log n}, which is compatible with the conjecture.
- An empirical graph search or numerical exponent fit without a proof valid on an unbounded sequence.
- A result for a non-Euclidean norm, a generic norm, or a strictly convex norm rather than ||·||_2.
- Improving the numerical value of ε within an unverified certificate without verifying the underlying tower and transfer lemmas.
- Merely restating an informal forum claim or a Lean declaration while leaving imported axioms or load-bearing theorems unchecked.

正确性陷阱：

- Expand n^{1+O(1/log log n)} with the correct order of quantifiers: C is fixed before n varies.
- Use unordered-pair versus ordered-pair conventions consistently; a factor of two is harmless asymptotically but affects exact statements.
- An infinite subsequence is sufficient to refute an eventual-for-all-n upper bound, but the lower-bound exponent ε must be fixed.
- A multiplicative constant in n^{1+ε}/C0 can be absorbed only by reducing the exponent for sufficiently large n; write that step explicitly.
- Audit the number-field construction's projection injectivity, lattice separation/covolume estimates, class-number loss, prescribed splitting, and infinitude of the tower.
- Do not mistake the still-open exact asymptotics of u(n) for survival of the disproved Erdős upper-bound conjecture.

### 更新后的 AI 可解答性

- 等级: `not_applicable_closed_or_invalid`
- 分数: `0/100`
- 信心: `high`
- 结论: 不适用：字面原命题已被反例否定。任何非零“可解性”评分都会错误地把验证已声称的反例或研究另一条残余问题，当作解决 #90 原断言。

支持理由：

- 人类核验的 2026 预印本给出固定正幂增益的无穷序列，逻辑上直接否定原渐近上界。
- Sawin 的独立显式化版本进一步提供可审计的定量反例。
- 适当任务是证明核验与状态更新，而不是重新尝试证明已假的上界。

主要障碍：

- 完整反例依赖深的代数数论和无穷 pro-p 塔；审计者应逐一检查载重引理。
- 截至审计日，主证明很新且未确认同行评审发表；形式化证据的无公理程度也需核查。

Proof-first 路线：

- 先对 Alon 等的 Theorem 1.1 和 Sawin 的 Theorem 1 做逐引理证明核验。
- 单独核验从固定 ε 的无穷子序列下界到原 O(1/log log n) 全称上界之否定的量词推导。
- 如需检查后续更高指数，只接受带有明确有限证书、假设和可重复验证器的独立子任务。

需要验证：

- 确认人类核验预印本的每个数论、格点几何和投影步骤没有隐藏条件。
- 检查任何 Lean 工件是否使用 sorry、额外公理或尚未证明的外部假设。
- 不要把 MathOverflow、论坛或计算预印本的更高常数自动升级为已验证纪录。

### 审计限制与人工复核理由

- AnySearch 服务在本次检索中无法连接；随后使用公开网页检索与全文打开功能完成交叉核验。
- Erdős Problems 的主页面、LaTeX 页面和论坛全文直接抓取分别遇到服务器错误或 403；论坛搜索索引、主论文和形式化文档仍提供了可检查的当前状态线索。
- 本审计检查了论文的定理陈述、证明结构和关键段落，但没有逐行重做全部深层数论证明；2026 主结果尚未确认同行评审发表。
- 对 2026 年 6 月以后更高显式指数的预印本、论坛和 MathOverflow 记录，只作不确定后续工作处理，未认证为最佳已证定理。

- 建议由代数数论与组合几何专家逐引理复核非常新的预印本证明，特别是无穷塔、分裂控制和格点投影的连接。
- 如需把“已形式化”视为独立核验，须检查具体 Lean 源码及其额外公理/不透明依赖；现有文档和论坛线索不足以证明完全无假设形式化。

<!-- DEEP_REVIEW:END -->
