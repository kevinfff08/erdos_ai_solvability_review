# Problem 119

## 基本信息

- 原始链接: https://www.erdosproblems.com/119
- LaTeX 页面: https://www.erdosproblems.com/latex/119
- 原始状态: `open`
- 奖金: `$100`
- 主类别: `analysis`
- 原始标签: `analysis`, `polynomials`
- 形式化状态: `yes`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

Let $z_i$ be an infinite sequence of complex numbers such that $\lvert z_i\rvert=1$ for all $i\geq 1$, and for $n\geq 1$ let\[p_n(z)=\prod_{i\leq n} (z-z_i).\]Let $M_n=\max_{\lvert z\rvert=1}\lvert p_n(z)\rvert$.

Is it true that $\limsup M_n=\infty$?

Is it true that there exists $c>0$ such that for infinitely many $n$ we have $M_n > n^c$?

Is it true that there exists $c>0$ such that, for all large $n$,\[\sum_{k\leq n}M_k > n^{1+c}?\]

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `28/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 题面或备注出现有限对象/计算线索
- 已有形式化陈述，可降低语义误读风险

### 主要障碍

- 所属标签偏证明密集：analysis
- 题面含渐近/无限对象线索：\ll, for all large, infinitely many, limsup
- 原记录含奖金 $100，说明该题被长期视为高价值难题；这不是否定依据，但提高验证门槛。

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: polynomials
- 证明密集标签命中: analysis
- 有限/计算线索: finite, finitely
- 渐近/无限线索: \ll, for all large, infinitely many, limsup
- 构造/存在性线索: construct

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5-level model with computation/formalization/literature tools`
- 结论: **这是一个低到中等候选问题：模型很可能能整理并验证已知的前两部分、复现若干计算实验、探索第三问的可行路线和潜在反例结构；但要独立解决第三个仍公开的问题，成功概率不高。**
- 等级: `low_to_medium_candidate`
- 分数: `42/100`
- 信心: `medium`
- 可能路线: 可行路线应聚焦第三问：把问题转化为单位圆上对数势或三角多项式的下界问题，结合已知的 Wagner/Beck 型最大值增长结果，尝试证明大峰值会在足够多的相邻 k 上产生可累积贡献；同时用计算搜索构造低 M_k 序列，检验是否可能存在长期接近线性和的反例。形式化证明工具可用于验证辅助引理，例如 Jensen 公式、L^p 到 L^∞ 估计、乘上一个线性因子后 M_k 的局部变化界等。

### 支持理由

- 题面已说明前两问已有非平凡正向结果，因此该问题不是完全无入口；模型可复现并组织这些路线，作为第三问的基线。
- 对象定义清晰且已形式化，适合把局部不等式、范数估计和有限计算搜索接入证明检查器或数值验证流程。
- 第三问是关于 \sum_{k\le n}M_k 的平均增长，可能比逐点最大值结果更适合通过能量分布、峰值传播或分块论证推进。
- 计算工具可以搜索极小化 M_k 的根序列，帮助发现 Linden 型构造的行为是否接近第三问障碍。

### 主要障碍

- 第三问仍标注为似乎公开，且已有构造能让 M_n 显著低于线性增长，说明简单的系数、Mahler 测度或最大模原理估计远远不够。
- Beck 的 \max_{n\le N}M_n>N^c 只保证稀疏峰值，不能直接推出部分和超过 n^{1+c}；核心缺口是把稀疏大值转化为足够密集的贡献。
- 根序列完全任意且可自适应选择，反例搜索空间很大，数值优化容易产生误导性有限样本。
- 即使找到强实验规律，也需要非渐近常数、无限序列紧致性或递推稳定性论证，形式化成本较高。

### 需要的验证

- 核对 formalized 版本是否覆盖三问以及已知定理引用，而不是只形式化定义或较弱命题。
- 复现 Beck 型下界与 Linden 型上界构造的关键引理，确认第三问不能由现有结果直接推出。
- 进行针对第三问的数值优化：最小化 \sum_{k\le n}M_k 或平均 M_k，并检查最优序列的结构是否稳定。
- 若提出证明路线，需要用独立证明检查或严密手稿验证峰值传播、分块累积和极限过渡步骤。

### 公开版思考摘要

该问题的已解决部分给了模型可利用的理论脚手架，但真正剩余的是第三个平均增长问题。它看起来不像纯计算即可攻破的问题，因为必须处理任意无限单位圆根序列并获得渐近下界。GPT-5.5 级别系统更现实的贡献是复现文献、发现等价命题、测试极端构造、验证局部引理，并可能给出有价值的部分推进；完整解决第三问属于低概率但非零概率事件。

### 免责声明

以上是对 AI 辅助可解性和推进潜力的审查，不是该 Erdős 问题的证明或反例。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `revised_open`
- 状态信心: `medium`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_119.md](../../prompts/problem_119.md)

### 状态结论

该条目包含三个层次的问题：前两问已分别由 Wagner（1980）与 Beck（1991）肯定解决；唯一明确存留的目标是第三问的全体大 n 累积下界。2026-07-20 起有媒体转述 GPT-5.6/Korsky 已解决第三问的说法，但审计时没有找到可检查的论文、预印本、完整论证或无 sorry 的形式化证明；Erdős Problems 的可访问当前索引副本仍标为 OPEN，论坛线程也仍无任何解答声明。因此应将其作为“已部分解决后剩余的开放目标”，而非已解决问题。

### 当前规范陈述

令 (z_i)_{i>=1} 为任意单位圆 T={w∈C:|w|=1} 上的无穷复数序列，允许重复。对 n>=1，令 p_n(w)=∏_{i=1}^n(w-z_i)，并令 M_n=max_{|w|=1}|p_n(w)；该最大值因单位圆紧致而存在。当前存留的目标是：对每个这样的序列 (z_i)，存在常数 c=c((z_i))>0 及 N_0=N_0((z_i))，使得每个整数 n>=N_0 都满足 ∑_{k=1}^n M_k>n^(1+c)。其中“all large n”指存在 N_0 后对所有 n>=N_0 成立，且不等式严格。这里采用当前 Lean 陈述的量词顺序“对每个序列存在 c”。若要求一个对所有序列都相同的绝对 c，则是更强版本，原文及其形式化均未明确要求。

```text
Let (z_i)_{i>=1} be an arbitrary infinite sequence in the unit circle T={w in C: |w|=1}; repetitions are allowed. For n>=1 set p_n(w)=prod_{i=1}^n(w-z_i) and M_n=max_{|w|=1}|p_n(w)|, where the maximum exists by compactness. The surviving target is: for every such sequence (z_i), there exist constants c=c((z_i))>0 and N_0=N_0((z_i)) such that, for every integer n>=N_0, sum_{k=1}^n M_k>n^(1+c). Here “for all large n” means “there exists N_0 such that for every n>=N_0”; the inequality is strict. This uses the current formalization's quantifier order forall sequence exists c. A convention demanding one universal c for all sequences is a stronger statement and is not explicitly asserted by the supplied wording or its formalization.
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 未发现能推翻字面第三问的简单序列。等间隔、重复点或贪婪点等自然构造不能替代对“任意无穷序列”的反例证明。Linden 的已知构造只给出某序列的上界 M_n≪n^(1-c)，并不否定所要求的累积下界。
- 版本变化: 历史上该记录一直并列三问。Wagner 证明第一问的更强定量形式；Beck 证明第二问；因此数据库将整体条目保留为 OPEN，并明确第三问“seems to remain open”。Google DeepMind Formal Conjectures 将 (i)、(ii) 标为 research solved，而将 (iii) 标为 research open；三个定理体均含 sorry，故这只是问题/已知结果的形式化陈述，并非第三问的形式化解答。2026-07-20 的媒体报道声称第三问有一页证明，但没有可审计的证明工件，不能构成状态更新。

陈述问题：

- 原文先固定任意序列后写“there exists c>0”，但未明说 c 是否必须对所有序列统一。当前 Formal Conjectures 文件将其形式化为“对每个序列存在 c”，故本审计采用该较自然且有直接形式化支持的读法；统一常数版本须另行核对原始论文或历史出处。
- 原文仅为 n>=1 定义 M_n，却写 ∑_{k<=n}M_k；本审计取通常含义 ∑_{k=1}^n。Lean 文件使用 Finset.range n（含 M_0、至 n-1），两种端点约定只相差有限项，不改变该渐近问题，但不应在逐字形式化时混用。
- 问题页将三问并列；把 Beck 已解决的第二问误称为整个 #119 已解，是近期媒体说法中实际出现的风险。

需要固定的量词/约定：

- Universal quantification over all infinite sequences (z_i) in T is outermost.
- For the residual third question, c>0 and N_0 may depend on the chosen sequence under the available formalized reading.
- The target requires every sufficiently large integer n, not merely infinitely many n or a subsequence of dyadic endpoints.
- Use sum_{k=1}^n M_k under the original n>=1 indexing; adding M_0=1 or shifting an endpoint is asymptotically harmless but must be stated.
- Repeated zeros z_i are permitted; neither distinctness nor any distributional hypothesis is assumed.

### 文献与当前边界

已核验的主要结果：

- Wagner（1980，同行评议）证明第一问的定量加强：存在 c>0，使 M_n>(log n)^c 对无穷多个 n 成立；故 limsup M_n=∞。
- Beck（1991，同行评议）证明第二问：存在 c>0，使 max_{m<=N}M_m>N^c（对任意大 N 的标准解读）。这蕴含 M_n>n^c 对无穷多个 n 成立：达到最大值的 m 必须无界，且 m<=N。
- Erdős 的构造给出某序列 M_n<=n+1；Linden（1977，同行评议）改进为某序列 M_n≪n^(1-c0)，其中 c0>0。此为上界构造，不是第三问的反例。
- Formal Conjectures 将问题按 (i)、(ii)、(iii) 拆开，精确编码了当前通常读法，但各 theorem 仍为 sorry，不能作为解答证明。

最近相关工作：截至 2026-07-27，未检索到 2023–2026 年针对第三问的可检查同行评议论文或 arXiv 预印本。2026-07-20 起的媒体声称存在 GPT-5.6/Korsky 的一页证明并归因 Bloom 审核；然而没有公开论文、证明文本或无 sorry 的形式化工件，且可访问的 Erdős Problems 记录仍为 OPEN。该声明必须在取得原始论证后逐行审计，不能视为已解决。

剩余核心：证明或反驳：对每个单位圆上的无穷序列，是否存在正指数 c，使所有充分大的 n 都有 ∑_{k=1}^n M_k>n^(1+c)。关键强度是“所有充分大 n”的累积多项式增长；已知的无穷多次单点大值不足以推出它。

已使用方法：

- Wagner 的工作属于丢番图逼近/分布偏差语境；当前问题页提取出对数幂的无穷多次下界。
- Beck 已建立多项式级的初段最大值下界，但该结果本身不提供每个大终点的累积下界。
- Linden 型构造说明不能期待对每个 n 都有接近线性的逐点下界，因此必须处理大值的频率、分布或块和，而非仅寻找一个单独峰值。
- 2026 媒体提到“标准调和分析”，但在没有可检查证明前，这不是可接受的已验证方法结论。

争议或不确定性：

- 原句未显式说明 c 是否须与序列无关；正式化采用序列依赖的 c。统一 c 的更强版本需人工查阅原始语境后另立目标。
- 2026 媒体报道与官方数据库的可访问状态记录冲突/滞后；更准确地说，前者是无公开工件的解答声称，后者是最后一次可核查的状态记录。
- Beck、Wagner、Linden 原文的全文在本审计中未能逐页获取；其精确结果通过出版社元数据以及官方问题页/正式化中的归属交叉核验。

### 证据来源

- [Erdős Problems — analysis tag listing, entry #119](https://www.erdosproblems.com/tags/analysis/yes) — Thomas F. Bloom / Erdős Problems Community, 2026-01-23; `problem_page`, `database_record`, directness=`direct`, reliability=`high`. 可访问的当前官方索引副本将 #119 标为 OPEN，列出三个问题、Wagner/Beck/Linden 的进展，称第三问似乎仍开放，且显示 0 条评论；页面标示最后编辑于 2026-01-23。
- [119 Discussion Thread | Erdős Problems](https://www.erdosproblems.com/forum/thread/119) — Erdős Problems Community, 2026-05-18; `forum`, `database_record`, directness=`direct`, reliability=`medium`. 该问题的官方论坛线程索引仍转述第三问开放；未发现公开的 #119 解答帖或可检查证明链接。
- [FormalConjectures.ErdosProblems.«119»](https://firsching.ch/formal-conjectures/src/FormalConjectures/ErdosProblems/%C2%AB119%C2%BB/) — Formal Conjectures Authors / Google DeepMind Formal Conjectures project, 2025; `formalization`, `formalized_artifact`, directness=`direct`, reliability=`high`. 给出 p、M 及三问的 Lean 类型；(i)、(ii) 标为 research solved，(iii) 标为 research open。所有相关 theorem body 都是 sorry，因此该工件形式化了陈述和项目分类，不验证任何证明。
- [The modulus of polynomials with zeros on the unit circle: A problem of Erdös](https://annals.math.princeton.edu/1991/134-3/p03) — József Beck, 1991; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 确认 Beck 论文的作者、期刊、卷期与页码（Annals of Mathematics 134(3), 609–651）；当前问题页和形式化文件将其作为第二问肯定解答的来源。
- [On a Problem of Erdőos in Diophantine Approximation](https://doi.org/10.1112/blms/12.2.81) — Gerold Wagner, 1980-03; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 确认 Wagner 论文为 Bulletin of the London Mathematical Society 12(2), 81–88；当前问题页和形式化文件将其作为第一问及对数幂无穷多次下界的来源。
- [The Modulus of Polynomials with Zeros on the unit Circle](https://academic.oup.com/blms/article/9/1/65/293413) — C. N. Linden, 1977-03-01; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 确认 Linden 论文的书目信息（BLMS 9(1), 65–69）；当前问题页引用其存在性构造 M_n≪n^(1-c)。
- [New problems, in Proceedings of the Symposium on Complex Analysis Canterbury 1973](https://www.cambridge.org/core/books/proceedings-of-the-symposium-on-complex-analysis-canterbury-1973/new-problems/448E4822E4E02F1F8A73D101B4BECEA2) — W. K. Hayman, 1974; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 确认 Hayman 1974 文献为该问题页所称 Problem 4.1 的历史出处（页 155–180）。
- [La IA se lleva la recompensa de 100 dólares de Erdős: un problema que una revista top de 44 páginas no resolvió, lo resolvió en una sola hoja](https://www.htx.com/es-es/news/ai-claims-erd%C5%91ss-100-bounty-solves-in-one-page-what-a-44-pag-GgPkoNSI/) — marsbit / HTX, 2026-07-20; `other`, `informal_claim`, directness=`indirect`, reliability=`low`. 报道声称 GPT-5.6 Sol 与 Korsky 解决了第三问并称 Bloom 已核验；报道没有提供可检查的证明、预印本或形式化工件，故只能记录为未证实声明。
- [GPT-5.6 Sol Erdős Problem #119 Claim Remains Unverified](https://windowsforum.com/threads/gpt-5-6-sol-erdos-problem-119-claim-remains-unverified.439743/) — Windows Forum contributor, 2026-07-20; `forum`, `informal_claim`, directness=`indirect`, reliability=`medium`. 明确区分 Beck 已解的第二问与仍需证明的第三问，并指出公开记录及可审计数学对象不足以确认媒体解答声明；它不是原始证明来源。

### 完成标准

- 肯定出口: Prove that for every sequence (z_i) in the unit circle there exist c>0 and N_0 such that, for every integer n>=N_0, sum_{k=1}^n max_{|w|=1} product_{i=1}^k |w-z_i| > n^(1+c), with the quantifier convention stated in the canonical target.
- 否定出口: Exhibit one explicit infinite sequence (z_i) in the unit circle and prove that it defeats every positive exponent: for every c>0 and every N_0 there exists an integer n>=N_0 with sum_{k=1}^n M_k <= n^(1+c).

不构成完成：

- Reproving Wagner's unboundedness or logarithmic-power lower bound.
- Reproving Beck's assertion that max_{m<=N} M_m>N^c, or proving large M_n only on infinitely many indices.
- Proving the cumulative lower bound only on an infinite subsequence of endpoints, including merely dyadic endpoints, without a bridge to every sufficiently large n.
- Showing the claim for random, equidistributed, distinct, finite, or specially ordered zeros only.
- Giving numerical evidence for finite prefixes without a theorem that passes to arbitrary infinite sequences.
- Citing a media report, a search snippet, or a Lean declaration containing sorry as a proof.

正确性陷阱：

- Keep the universal quantifier over arbitrary ordered sequences; the ordering affects the prefixes p_n.
- Track the scope of c and N_0, and explicitly state whether c is sequence-dependent or universal.
- Do not replace “for all sufficiently large n” by “for infinitely many n.”
- Do not infer the required sum lower bound solely from rare spikes in M_n.
- Use a consistent sum convention: original indexing is k=1,...,n; a formal proof using M_0 or range n must account for the endpoint shift.
- When using max_{m<=N} M_m, prove carefully what it does and does not imply about individual M_n and cumulative sums.
- Any claimed 2026 proof must be checked for its exact conclusion, positivity/normalization assumptions, and all implicit constants before it changes status.

### 更新后的 AI 可解答性

- 等级: `low_to_medium_candidate`
- 分数: `18/100`
- 信心: `medium`
- 结论: 这是一个定义清楚、可逐引理审计的剩余开放目标，但它已抵抗研究数十年，且已知单点多项式下界与所求全终点累积下界之间存在实质鸿沟；适合严谨的证明优先探索，不适合以有限计算或媒体声明作为捷径。

支持理由：

- 目标量词、严格不等式和渐近终止条件可明确形式化，且已有 Lean 陈述可作语义检查。
- 前两问和上下界构造提供了可核验的基线，能快速筛除只重现旧结果的候选论证。
- 第三问可分解为可审计的块和/频率型中间命题；若取得新的一页证明，其核验也具有明确的逐步终点。

主要障碍：

- 问题开放时间长，Beck 的强单点结论仍不足以控制每个大 n 的前缀和。
- 零点可任意重复和任意排序，排除了随机性或规则分布的默认假设。
- 近期解答报道无公开证明工件；在没有原文时不能把“调和分析”说法转化为可执行证明路线。
- 有限前缀的数值实验无法证明或反驳涉及任意无穷序列和任意充分大 n 的陈述。

Proof-first 路线：

- 先尝试证明一个精确的区间块和引理：存在 c>0，使对每个充分大 N 都有 ∑_{N<k<=2N}M_k >= N^(1+c)（常数和端点须统一）。该引理经前一二进制块的比较可推出原目标；若失败，应记录失败点而非把它误报为原命题。
- 研究能把 Beck 型“初段中有峰值”升级为“每个尺度有足够质量”的结构引理，并明确峰值的数量、间隔或持续性；只接受能量化推出块和的版本。
- 若获得 2026 候选证明，优先将其拆为定义、关键不等式、量词转移和终点处理四类可独立复核的引理；先验算其确实得到第三问，而非第二问。

需要验证：

- 取得并审读 Wagner、Beck 与 Linden 的全文，以确认 c 的统一性、精确常数范围及历史表述。
- 寻找或向原作者/网站维护者索取 2026 声称的一页证明的公开稳定链接；在此之前不改变开放状态。
- 若该证明存在，对其进行独立同行式审计，或建立无 sorry 的 Lean/其他证明助理形式化。
- 若未来发现新论文，核对它是否处理任意序列、所有充分大终点和与本审计一致的求和约定。

### 审计限制与人工复核理由

- 直接打开 https://www.erdosproblems.com/119 及其 LaTeX 页返回 403；通过该站可访问的 analysis 标签页、历史/论坛搜索索引和 Formal Conjectures 镜像核对了同一当前内容。
- Beck、Wagner 与 Linden 的出版社页面确认了书目信息，但其全文未在本次会话逐页可读；具体定理归属还由 Erdős Problems 与 Formal Conjectures 的一致记录交叉支持。
- 未找到 2026 媒体所称的一页证明的原始 PDF、预印本、公开仓库或可编译无 sorry 的形式化文件。因而不能独立审查该声称，也不能逻辑上排除其私下存在。
- 对近三年工作的检索覆盖了精确陈述、作者、arXiv、正式化库和媒体/论坛线索；网络搜索未发现可检查新成果不构成不存在新成果的证明。

- 应由具备访问权限的数学审稿人取得并逐行审阅 Beck、Wagner、Linden 原文，以最终消除 c 是否为绝对常数的历史语义疑问。
- 若要改变状态，必须先取得并独立审计 2026 声称的一页证明，或获得等价的、无 sorry 的形式化验证；现有媒体转述不能满足该标准。
- Erdős Problems 主页面的直接抓取受 403 限制；维护者或人工浏览可再次确认 2026-07-27 后是否已有未被搜索索引捕获的状态更新。

<!-- DEEP_REVIEW:END -->
