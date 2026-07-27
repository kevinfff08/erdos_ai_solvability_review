# Problem 30

## 基本信息

- 原始链接: https://www.erdosproblems.com/30
- LaTeX 页面: https://www.erdosproblems.com/latex/30
- 原始状态: `open`
- 奖金: `$1000`
- 主类别: `number theory`
- 原始标签: `number theory`, `sidon sets`, `additive combinatorics`
- 形式化状态: `yes`
- OEIS: `A143824`, `A227590`, `A003022`
- 原站备注字段: 无

## 原问题

Let $h(N)$ be the maximum size of a Sidon set in $\{1,\ldots,N\}$. Is it true that, for every $\epsilon>0$,\[h(N) = N^{1/2}+O_\epsilon(N^\epsilon)?\]

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `19/100`
- 建议路线: 优先文献定位、特殊情形、数值实验和辅助引理搜索；完整证明需要新的数学思想。

## 判断依据

### 有利因素

- 已有形式化陈述，可降低语义误读风险
- 存在 OEIS 数据入口，利于实验与反例搜索

### 主要障碍

- 所属标签偏证明密集：additive combinatorics, number theory, sidon sets
- 题面含渐近/无限对象线索：o(
- 原记录含奖金 $1000，说明该题被长期视为高价值难题；这不是否定依据，但提高验证门槛。
- 缺少明显有限搜索入口。

### 公开版思考过程摘要

- 先识别问题类型：无限/渐近或抽象证明倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: additive combinatorics, number theory, sidon sets
- 有限/计算线索: 无
- 渐近/无限线索: o(
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5 级别模型配合计算、形式化证明、文献检索、反例搜索等工具`
- 结论: **低到中等候选。该问题有清晰定义、已形式化、可做有限规模验证和证明检查，因此适合 AI 工具体系做严谨辅助推进；但目标是把已知上界误差从约 N^{1/4} 级别降到任意 N^epsilon，属于经典 Sidon 集极值问题中的核心指数障碍，单靠当前模型较难直接完成完整证明。**
- 等级: `low_to_medium_candidate`
- 分数: `38/100`
- 信心: `medium`
- 可能路线: 最现实的路线不是直接证明最终命题，而是让模型围绕现有上界框架做局部推进：形式化复核 Erdős--Turán/Lindström 型证明，重建 Carter--Hunter--O'Bryant 型常数优化思路；用 SAT/ILP/CP-SAT 精确计算 h(N) 的更大范围；从极值 Sidon 集的差集、和集、模结构中搜索稳定结构；再尝试把经验结构转化为可形式化的加强引理。若要接近完整解决，需要发现能突破 N^{1/4} 误差屏障的新全局计数或结构定理。

### 支持理由

- 问题陈述短且精确定义，Sidon 条件可直接编码为组合约束，适合自动化搜索、精确验证和形式化证明辅助。
- JSON 显示该问题已经 formalized=yes，这显著降低了机器检查证明、复用定义和验证有限引理的门槛。
- 已有上界形态明确：从 N^{1/2}+N^{1/4}+1 到 0.98183N^{1/4}+O(1)，说明现有方法可被模型复现、局部优化和自动化审计。
- 有限 N 的 h(N) 可通过反例搜索、整数规划、SAT 编码和 OEIS 相关数据进行交叉验证，有助于发现或排除强版本 h(N)=N^{1/2}+O(1) 的小规模模式。
- 这是加性组合与数论交界的结构化问题，模型可结合文献检索、证明草稿生成、计算实验和形式化验证形成闭环，而不只是自然语言猜测。

### 主要障碍

- 核心目标要求将误差指数从 1/4 降到任意 epsilon；根据给定备注，近年进展仍主要是 N^{1/4} 前常数优化，暗示现有方法存在强屏障。
- 有限计算无法直接验证渐近命题，除非转化出可证明的结构引理；反例搜索也很难否定全称渐近断言。
- Sidon 极值构造与有限几何、模结构、差分集等深层对象相关，模型容易生成看似合理但实际不足以控制全局误差的计数论证。
- 命题可能需要全新组合思想，而不是对已有证明做局部常数改进；这类创造性跨越目前仍是大模型最不稳定的能力区间。
- 形式化虽然有帮助，但形式化系统通常只能验证已经足够清楚的证明，对发现突破性不等式本身帮助有限。

### 需要的验证

- 复现并机器检查已知上界证明，确认模型没有误用 Sidon 条件或忽略边界项。
- 构建 h(N) 的精确计算流水线，并用多种编码方式交叉验证小到中等规模结果。
- 若模型提出新引理，需要先在随机和极值候选 Sidon 集上做自动反例搜索，再进入人工或形式化证明检查。
- 任何声称突破 N^{1/4} 的论证都必须明确指出其避开既有 Erdős--Turán/Lindström 型计数瓶颈的位置。
- 最终证明需要形式化或至少由独立专家逐行审查，特别是所有 O_epsilon 常数依赖和渐近量词顺序。

### 公开版思考摘要

这个问题非常适合 AI 做辅助研究：定义可编码、已有证明可复核、有限数据可扩展、形式化基础已存在。但从给定备注看，八十多年后的最好结果仍停留在 N^{1/4} 误差项的常数优化层面，而目标要求几乎消除该幂次误差。因此 GPT-5.5 级别模型有现实机会完成证明审计、数据扩展、局部常数优化或提出可检验的新引理；直接解决完整命题的概率较低，但不能视为完全不适合，因为它有清晰的计算与形式化切入点。

### 免责声明

以上是对 AI 辅助可解性和推进潜力的评估，不是该 Erdős 问题的解答，也不声称证明或否定原命题。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `confirmed_open`
- 状态信心: `high`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_30.md](../../prompts/problem_30.md)

### 状态结论

该精确定式仍为开放问题。2026-07 的 Hou–Zhao 预印本将已检索到的上界常数推进到 0.9435，但仍是 N^{1/4} 量级，远未证明任意 ε>0 的次多项式误差；没有发现完整解答或反例。Erdős Problems 当前页面和讨论串也仍标为 OPEN。

### 当前规范陈述

令 [N]={1,...,N}（N 为正整数）。若有限集 A⊆[N] 满足：对任意 a,b,c,d∈A，a+b=c+d 蕴含无序对 {a,b}={c,d}（因此包含重复加数的情形），则称 A 为 Sidon（B_2）集。令 h(N)=max{|A|:A⊆[N] 为 Sidon 集}。目标是：对每个实数 ε>0，存在常数 C_ε≥0、N_ε，使得每个整数 N≥N_ε 都满足 |h(N)-√N|≤C_εN^ε。

```text
Let [N]={1,...,N} for each positive integer N. A finite A⊆[N] is a Sidon (B_2) set if, for all a,b,c,d∈A, a+b=c+d implies {a,b}={c,d} as unordered pairs (so repeated summands are included). Define h(N)=max{|A|:A⊆[N] is Sidon}. The target is: for every real ε>0, there exist constants C_ε≥0 and N_ε∈N such that, for every integer N≥N_ε, |h(N)-√N|≤C_εN^ε.
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 已针对定义、量词、平移区间 {0,...,N-1} 与 {1,...,N}、以及有限计算型“反例”检查。未发现能否定该渐近命题的简单反例；这不是对所有构造的穷尽证明。
- 版本变化: 核心问题未被后续文献替换。历史上常把较弱任务表述为改进 √N+N^{1/4}+O(1) 的误差项；这不等价于本题。数据库仍列 CHO25 的 0.98183，但 2026-07 的 Hou–Zhao 预印本声称并给出精确有理证书以得到 0.9435，故数据库的“current record”文字已过时。Lean 工作形式化了 Singer 构造及若干基线结果，并只形式化了在“次多项式素数间隙 + 所需上界”假设下推出本题的条件性归约；它不是本题的证明。

陈述问题：

- 原句未明说 Sidon 集采用“无序二元和唯一”的 B_2 约定；该约定在该文献中是标准约定，但必须排除调和分析中的另一种“Sidon set”含义。
- 原句中的等式与 O_ε 需要解释为对 h(N)-√N 的绝对值估计，且隐含常数和起始阈值可依赖于 ε、不能依赖于 N。
- 没有发现会推翻字面命题的简单构造或小参数反例；这是渐近命题，有限范围的精确值不能决定其真伪。

需要固定的量词/约定：

- N ranges over positive integers and the asserted bound holds for all sufficiently large N, not merely infinitely many N.
- For each ε>0, both C_ε and N_ε may depend on ε; neither may depend on N.
- The equality f(N)=g(N)+O_ε(N^ε) means |f(N)-g(N)|≤C_εN^ε eventually.
- Sidon means uniqueness of unordered two-term sums, including sums a+a.

### 文献与当前边界

已核验的主要结果：

- Singer（1938）的有限域构造给出 h(N)≥(1-o(1))√N；这是主项下界，而不是所需的任意 ε 次多项式误差。Erdős Problems 页面和后续论文的历史介绍均如此归纳。
- Erdős–Turán（1941）及 Lindström 的方法给出 h(N)≤√N+N^{1/4}+O(1)；这是对所有大 N 的上界，但指数 1/4 固定，不能推出本题。
- Balogh–Füredi–Roy（2021，预印本）把 N^{1/4} 系数改为 0.998；O'Bryant（2022 预印本、后有期刊版本）改为 0.99703。
- Carter–Hunter–O'Bryant（2025，同行评议）证明 h(N)≤√N+0.98183N^{1/4}+O(1)。论文明确区分了重计算辅助版本与可手工核查的较弱版本。
- Hou–Zhao（2026-07，预印本）进一步声称 h(N)≤√N+0.9435N^{1/4}+O(1)，以向量值平滑、凸二次优化和有限精确有理证书实现。该结果若经核查，是本次检索中最强的已公开上界；仍只改善常数。
- Hulak–Ramos–de Queiroz（2026，Lean 4 预印本）报告了 Singer 构造与若干基线不等式的形式化，并清楚地把本题的条件性归约与无条件解答分开。

最近相关工作：最直接的最新工作是 Hou–Zhao, arXiv:2607.01169v2（2026-07-05）：其摘要和可检查的文稿部分给出 √N+0.9435N^{1/4}+O(1) 上界，并说明有限有理证书的验证器。它尚未同行评议，故应独立运行或逐项复核证书后才作为可依赖的最新记录。

剩余核心：须同时控制上下两侧，且对每个 ε>0 都在所有充分大 N 上达到 |h(N)-√N|=O_ε(N^ε)。现有的上界仍有固定 N^{1/4} 误差；Singer 型构造只给主项的 (1-o(1)) 下界。仅把 N^{1/4} 前的常数再降低，或只在无穷多个 N 上构造接近 √N 的集合，都不足以完成本题。

已使用方法：

- Erdős–Turán 与 Lindström 的差分计数/交叉差分不等式。
- 移位集合的关联计数（Johnson-route）及将不同上界方法的松弛量相互制约。
- 以直径下界重新表述区间 Sidon 极值问题，并分析边界窗口、局部密度和表示函数恒等式。
- 有限域 Singer 差集构造、模循环群到整数区间的窗口/展开转移。
- Hou–Zhao 的多核向量值卷积平滑、L² 能量平均、凸二次边界优化和精确有理证书。
- 形式化验证可用于固定引理、有限证书及量词/取整边界，但不能把条件性素数间隙假设误当作已证定理。

争议或不确定性：

- Erdős Problems 数据库的正文仍把 0.98183 称为当前记录，已被 2026-07 Hou–Zhao 预印本的 0.9435 声称超越；后者尚未同行评议。
- 论坛中 0.98173、0.97633 与“tentatively 0.947”的说法没有已检查的论文或形式化制品，且不构成对原问题的解答。
- 输入标注为 formalized；检索到的 Lean 预印本报告零 sorry 的相关核心，但本审计未获得可独立构建的代码仓库和构建日志，故形式化覆盖范围需人工复核。

### 证据来源

- [Erdős Problems — Problem 30](https://www.erdosproblems.com/30) — Thomas F. Bloom / Erdős Problems, 2025-08-31; `problem_page`, `database_record`, directness=`direct`, reliability=`high`. 给出本题表述、OPEN 标签及历史结果摘要；该站明确提醒其开放标签不是替代文献检索的证明。
- [Problem 30 discussion thread](https://www.erdosproblems.com/forum/thread/30?embed=1) — Erdős Problems forum contributors, 2026-02-17; `forum`, `informal_claim`, directness=`direct`, reliability=`medium`. 讨论串仍显示 OPEN；其中 0.98173、0.97633 和“tentatively 0.947”等说法均为未发表或待确认的论坛陈述，不能视为对本题的解答。
- [On the diameter of finite Sidon sets](https://link.springer.com/article/10.1007/s10474-024-01499-8) — Daniel Carter, Zach Hunter, Kevin O'Bryant, 2025-02-07; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 经同行评议地证明 h(N)≤√N+0.98183N^{1/4}+O(1)，并说明一个可手工核查但较弱的 1.99058 直径常数版本；不证明次多项式误差。
- [Vector-valued smoothing for finite Sidon sets](https://arxiv.org/abs/2607.01169) — Jianfeng Hou, Hongbin Zhao, 2026-07-05; `preprint`, `preprint`, directness=`direct`, reliability=`medium`. v2 声称证明 F(N)≤√N+0.9435N^{1/4}+O(1)，并将八核数值搜索转为可用精确有理算术检查的有限证书；平移使其 F(N) 定义与本题 h(N) 等价。该工作尚未同行评议。
- [On the size of finite Sidon sets](https://arxiv.org/abs/2207.07800) — Kevin O'Bryant, 2022-07-16; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 证明此前的改进 h(N)<√N+0.99703N^{1/4}（充分大 N），并明确给出 B_2/Sidon 的等价定义和直径—区间极值函数的对应。
- [An upper bound on the size of Sidon sets](https://arxiv.org/abs/2103.15850) — József Balogh, Zoltán Füredi, Souktik Roy, 2021-03-29; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 证明 h(N)≤√N+0.998N^{1/4}（充分大 N），是 1941 年后误差常数的首个实质改进。
- [Formalizing Singer Sidon Constructions and Sidon Set Infrastructure in Lean 4](https://arxiv.org/abs/2605.03274) — David B. Hulak, Arthur F. Ramos, Ruy J. G. B. de Queiroz, 2026-05-12; `formalization`, `preprint`, directness=`direct`, reliability=`medium`. 报告 Lean 4 中 Singer 构造、区间/模 Sidon 基础设施和 √N+N^{1/4}+O(1) 型基线的形式化；还报告本题仅在次多项式素数间隙和所需上界假设下的条件性归约。该网页本身不足以独立复建并编译底层代码。
- [100 Open Problems](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf) — Ben Green, 2026-05-01; `author_page`, `informal_claim`, directness=`indirect`, reliability=`high`. Green 的 Problem 31 将本题列为仍待改进的有限 Sidon 集问题，并记录 2021 与 2023 的上界常数进展；它是独立的近期开放问题清单，但并非完整文献综述。

### 完成标准

- 肯定出口: A complete affirmative resolution proves that for every ε>0 there are C_ε,N_ε such that every integer N≥N_ε satisfies |h(N)-√N|≤C_εN^ε, using the B_2 definition stated above and with no unproved analytic hypotheses.
- 否定出口: A complete negative resolution proves that there exists ε_0>0 such that h(N)-√N is not O(N^{ε_0}); equivalently, for every C,N_0 there is N≥N_0 with |h(N)-√N|>CN^{ε_0} (or provides an explicit unbounded witnessing sequence).

不构成完成：

- Reducing the coefficient of N^{1/4}, even with an exact finite certificate.
- Proving the estimate for one fixed ε, one subsequence, infinitely many N, or only one inequality.
- A conditional proof relying on a prime-gap conjecture or an assumed subpolynomial Sidon upper bound.
- Finite computation of h(N) up to any cutoff without a theorem that covers all larger N.
- A proof for a different convention of Sidon set, for modular groups only, or for {0,...,N-1} without explicitly transferring it to the stated interval.

正确性陷阱：

- Check that every sum, including a+a, has a unique unordered representation.
- Audit the order of quantifiers: C_ε and N_ε may depend on ε, but the claim must hold for every sufficiently large integer N.
- Do not confuse h(N)=√N+O_ε(N^ε) with h(N)=(1+o(1))√N or with a fixed-power error bound.
- When converting a diameter theorem, account for the exact interval-length/diameter offset and all floor/ceiling terms.
- For claimed computer assistance, check the theorem linking the finite certificate to the asymptotic inequality, not just the rational inequalities in the certificate.
- Treat the 2026 preprint and forum assertions as unrefereed until their proof/certificate and scope are independently verified.

### 更新后的 AI 可解答性

- 等级: `low_candidate`
- 分数: `6/100`
- 信心: `high`
- 结论: 这是定义严谨、可审计但对 AI 而言极难的开放证明目标；适合开展有明确停止条件的引理级探索，而不适合把有限搜索或常数优化误报为“解决”。

支持理由：

- 目标的量词和完成条件清楚，已有多条可独立验证的上界、构造和形式化基础设施。
- 近期进展揭示了可审计的局部工具（精确证书、窗口不等式、边界优化），可支持小而严格的子引理研究。
- 但近 85 年主要进展仍停留在固定 N^{1/4} 误差的常数改善；主问题要求所有 ε>0 的质变，并同时涉及上、下界。

主要障碍：

- 没有已知机制把固定幂次误差自动降至任意次多项式误差。
- Singer 型下界向每个 N 的高精度转移与素数/模数分布问题耦合；现有 Lean 工作也将这一点显式保留为条件。
- 有限数值实验、凸优化或更好常数没有通向完整量词结论的自动外推。

Proof-first 路线：

- 优先寻找一个有明确陈述、能直接把上界或下界从固定幂次改善到任意 ε 的结构性引理，并先证明其确实足以推出目标。
- 独立审查“模 Sidon 构造—区间窗口转移—参数分布”链，定位下界中真正缺失的定量命题。
- 把新平滑法视为可比较的理论框架：寻找能随尺度迭代且有严格误差传播的引理，而非仅重优化有限核。

需要验证：

- 独立检查 Hou–Zhao 预印本的主引理、渐近展开以及随附有理证书/验证器。
- 独立构建或审阅 2026 Lean 工件，确认无 sorry 的模块、依赖、精确覆盖范围和条件性定理。
- 在依赖任何“最新记录”或论坛常数前，检索是否已有期刊版、撤回、勘误或更强公开预印本。

### 审计限制与人工复核理由

- 本审计只使用公开网页和可访问论文/预印本页面；未对历史原始论文逐页复核。历史陈述主要由近期论文和 Erdős Problems 的出处链交叉支持。
- Hou–Zhao 的 2026 预印本及其证书尚未经过同行评议；本审计检查了其公开定理陈述、方法说明和证书描述，但没有执行其外部代码。
- 论坛中关于更好常数的陈述按非正式主张处理，未作为数学结论。
- “未发现解答”是有范围的定向检索结论，不是对全球未发表工作或未来文献的逻辑排除。
- 当前数据库页的正文数值记录滞后于 2026-07 预印本；后者是否成为公认记录仍需独立验证。

- 应由领域专家独立核查 2026 Hou–Zhao 预印本从有限有理证书到全体 N 渐近上界的推导，并跟踪其同行评议、修订或勘误状态。
- 若要依据“formalized=yes”作决策，应取得并实际构建 Lean 源码，确认所报告的零 sorry 模块、导入依赖和条件性边界；当前公开预印本并不等同于本审计已完成构建验证。
- 任何后续研究计划都应首先决定是攻击上界、下界还是寻找反例；三者不能由已有的常数优化自动互相替代。

<!-- DEEP_REVIEW:END -->
