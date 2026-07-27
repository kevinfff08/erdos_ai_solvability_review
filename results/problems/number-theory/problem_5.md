# Problem 5

## 基本信息

- 原始链接: https://www.erdosproblems.com/5
- LaTeX 页面: https://www.erdosproblems.com/latex/5
- 原始状态: `open`
- 奖金: `no`
- 主类别: `number theory`
- 原始标签: `number theory`, `primes`
- 形式化状态: `no`
- OEIS: `A001223`
- 原站备注字段: 无

## 原问题

Let $C\geq 0$. Is there an infinite sequence of $n_i$ such that\[\lim_{i\to \infty}\frac{p_{n_i+1}-p_{n_i}}{\log n_i}=C?\]

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `30/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- 题面或备注出现有限对象/计算线索
- 存在 OEIS 数据入口，利于实验与反例搜索

### 主要障碍

- 所属标签偏证明密集：number theory, primes
- 题面含渐近/无限对象线索：arbitrarily large, prime

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: number theory, primes
- 有限/计算线索: finite
- 渐近/无限线索: arbitrarily large, prime
- 构造/存在性线索: is there

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **不太可能在完整无条件证明上成功，但有一定机会做出有价值的验证性或局部推进工作；更适合作为“文献综合、条件性证明、计算实验、形式化部分引理”的任务，而不是直接攻克开放问题。**
- 等级: `low_to_medium_candidate`
- 分数: `32/100`
- 信心: `high`
- 可能路线: 最现实的路线是围绕给定备注中的已知结构展开：系统整理关于极限点集合 S 的已知定理，形式化定义与若干简单推论，复现或检验小素数间隔和大素数间隔的计算证据，并尝试把已有筛法结果转化为更清晰的条件性命题。例如在强素数 k 元组猜想、Hardy-Littlewood 型假设或更强分布假设下证明任意有限 C 为极限点；无条件方向则可尝试重新审查 Pintz、Banks-Freiberg-Maynard、Merikoski 相关方法中的常数、覆盖比例或 bounded gaps 结构，寻找可机器检验的改进空间。

### 支持理由

- 问题陈述短且目标清晰，适合模型辅助做定义澄清、等价表述、文献脉络梳理和证明依赖图构建。
- 备注已经给出明确的研究入口：0、无穷、正测度、任意大有限数、包含小区间、正比例覆盖、bounded gaps 等结果，便于模型沿既有路线定位可推进的子目标。
- 计算工具可以大量枚举素数间隔并观察 (p_{n+1}-p_n)/log n 的经验分布，从而验证启发式、发现异常模式或测试候选猜想。
- 形式化证明工具可以处理定义层、闭包性、极限点集合的基础性质，以及部分条件性或已知定理调用后的推论。
- 若允许文献检索，GPT-5.5 级别模型有能力建立较完整的结果地图，识别哪些步骤依赖深层筛法、哪些只是后处理或常数优化。

### 主要障碍

- 完整证明 S=[0,∞] 涉及素数间隔的精细分布，远超单纯计算验证；有限范围实验无法推出所有极限点。
- 现有已知结果仍只覆盖部分区间或正比例集合，离每个 C 都是极限点存在明显结构性缺口。
- 关键技术很可能依赖 Maynard-Tao/GPY 类型筛法及其极限改进，模型难以独立发明足以跨越缺口的新筛法。
- 对任意指定 C 构造无限子列需要同时控制素数间隔大小和出现频率，这比证明小间隔、巨大间隔或正测度结论更强。
- 形式化验证受限于解析数论库现状；即使模型能写出人类风格证明，也很难快速在 Lean/Isabelle 中完整机检深层筛法结果。

### 需要的验证

- 核对给定备注中每条文献结果的精确定理陈述，避免把比例覆盖、区间包含或 bounded gaps 误读为完整稠密性。
- 复现数值实验时需要明确使用 log n 而不是 log p_n，并检查不同归一化对经验图像的影响。
- 若提出条件性证明，必须清楚列出所依赖的猜想强度，例如 Hardy-Littlewood 素数 k 元组猜想或素数分布假设。
- 若声称改进已知覆盖比例或常数，需要独立审计筛权选择、误差项、极限过程和常数优化代码。
- 任何无条件推进都应经过专家级解析数论审查，并尽量拆成可形式化的局部命题。

### 公开版思考摘要

这个问题的优势是目标非常明确，且给定材料显示已有丰富部分结果，因此 AI 工具链可以有效做“研究基础设施”工作：整理文献、复现实验、检查等价表述、建立条件性证明和审计局部推导。但完整结论要求证明归一化素数间隔的极限点覆盖整个非负实轴，这需要对素数间隔分布达到目前未知的控制强度。综合判断，GPT-5.5 配合工具不应被预期直接解决此题，但可以对问题的验证、条件化版本和局部常数改进尝试产生实质帮助。

### 免责声明

以上是对 AI 辅助可攻性和验证路线的评估，不是该 Erdős 问题的证明，也不声称给出了新的无条件数学结果。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `likely_open`
- 状态信心: `medium`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_5.md](../../prompts/problem_5.md)

### 状态结论

该问题很可能仍然开放。当前 Erdős Problems 页面及其论坛线程均明确标为 open，且页面称该猜想未证；所检得的最强同行评议直接结果仍为 Merikoski（2020）的“每个初段中至少三分之一测度的极限点”与“极限点集有界间隙”。未发现无条件证明 S=[0,∞] 或反例的可检查论文、预印本或正式化成果。2026 年出现了一份自称“conditional solution”的 ResearchGate 手稿，但其摘要明确依赖未解的 Hardy–Littlewood k-tuple conjecture，故不能解决无条件原题。

### 当前规范陈述

设 p_n 为第 n 个素数，g_n:=p_{n+1}-p_n，且 log 为自然对数。问：对每个有限实数 C≥0，是否存在严格递增指标 n_1<n_2<⋯、n_i→∞，使 g_{n_i}/log n_i→C？等价地，序列 (g_n/log n) 的所有有限子序列极限构成的集合 S 是否为 [0,∞)？若在扩展半直线 [0,∞] 中定义 S，则历史表述为 S=[0,∞]，其中 ∞ 指存在趋于无穷大的子序列。

```text
Let p_n be the n-th prime and g_n:=p_{n+1}-p_n. With log denoting the natural logarithm, determine whether, for every finite C≥0, there are strictly increasing indices n_1<n_2<⋯ with n_i→∞ such that g_{n_i}/log n_i→C. Equivalently, the set S of finite subsequential limits of (g_n/log n) is [0,∞). If S is instead taken in the extended half-line [0,∞], the equivalent historical formulation is S=[0,∞], where ∞ means that a subsequence tends to infinity.
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 未发现能否定上述标准化命题的简单构造。素数间隙的整数性、偶性及小素数例外均不妨碍除以趋于无穷的 log n 后逼近给定非负实数；C=0 已由深筛法结果得到。
- 版本变化: 历史上 Erdős 表述为归一化间隙在正半轴处处稠密。由于扩展实数意义下的子序列极限点集是闭集，这等价于 S=[0,∞]。当前数据库未显示正式修订或已解决记录。2026-05 的论坛评论校正了早期文献引文页码，但未改变数学命题。

陈述问题：

- 题面中的“an infinite sequence of n_i”应明确为严格递增的指标子序列；否则允许重复指标会偏离“极限点”的标准含义。
- 题面量词只涉及有限 C≥0，而备注写 S=[0,∞]；应把 ∞ 作为扩展实数极限点单独处理。
- 文献常用 g_n/log p_n，而输入采用 g_n/log n。由 p_n~n log n 可得 log p_n/log n→1，所以两种归一化的有限（以及扩展）极限点集合相同；该转换须在证明中写明。
- 论坛中“1 是否也开放”的回答只是作者的非正式说明，不能当作数学证明或完整文献检索。

需要固定的量词/约定：

- The subsequence may depend on C.
- Require n_1<n_2<⋯ and n_i→∞.
- The primary assertion quantifies over finite C; ∞ is an extended-real limit-point assertion.
- All logarithms are natural.
- The log p_n and log n normalizations have the same limit points because log p_n/log n→1.

### 文献与当前边界

已核验的主要结果：

- Westzynthius（1931；由当前题库记录转述）给出任意大的归一化素数间隙，故 ∞ 是扩展极限点。
- Goldston–Pintz–Yıldırım（2009，Annals）无条件证明 liminf g_n/log p_n=0，故 0∈S。
- Erdős（1955）与 Ricci（1956；当前题库记录转述）独立证明 S 有正 Lebesgue 测度。
- Hildebrand–Maier（1988；当前题库记录转述）证明 S 含任意大的有限元素。
- Pintz（2013 预印本；2016 书章，后由 2018 论文明确回顾）证明存在无效常数 c>0 使 [0,c]⊂S；其 2018 论文还得到测度下界约 T/4。
- Banks–Freiberg–Maynard（2016，PLMS）证明任取九个非负数，至少一个两两差属于 S；特别地 S 在非负半轴中占至少 12.5%。
- Merikoski（2020，JLMS）证明 λ(S∩[0,T])≥T/3，并证明 S 在 [0,∞) 中有有界间隙。

最近相关工作：本次按精确题名、作者、题号、关键短语、arXiv 与 2023–2026 时间窗口检索后，最后一个可核验的无条件同行评议直接推进仍是 Merikoski 的 2020 年 JLMS 论文。2026 年 Kaya 的上传手稿只主张以未解 Hardy–Littlewood 型猜想为条件的结论，因此不改变无条件状态。

剩余核心：必须对每个指定有限 C≥0 证明 g_n/log n 可沿无穷子序列趋于 C。已知的 [0,c] 覆盖、正测度、正下密度和有界间隙均允许遗漏大量目标值，甚至允许遗漏某个具体值如 1，因此均不足以解决本题。

已使用方法：

- GPY 与 Maynard–Tao 型多元筛法，用于在可控平移集合中制造素数。
- Erdős–Rankin 同余覆盖构造，用于排除候选端点间的其他素数并保证连续性。
- Chen 筛上界；Merikoski 用其改进相关素数对和的上界。
- 素数定理及从位置尺度 log p_n 到索引尺度 log n 的归一化换算。

争议或不确定性：

- 题库的 open 标签及论坛回复是当前但二级/非正式证据，不能替代完备文献数据库检索。
- 2026 年条件手稿的条件性推导本身未被本审计逐行验证；无论其是否正确，它都不提供无条件解决。
- 本次没有订阅 MathSciNet 或 zbMATH 的完整 2021–2026 引文索引，故“未发现”不等于不存在未检出的新成果。
- 未发现相关正式化项目；此为定向网络检索的阴性结果，不是对所有证明助理库的穷尽证明。

### 证据来源

- [Erdős Problems — Problem 5](https://www.erdosproblems.com/5) — Thomas F. Bloom / Erdős Problems contributors, 2025-08-31; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 数据库记录将本题标为 open，并称猜想仍未证明；同时列出 0、∞、正测度、区间 [0,c]、12.5% 与 1/3/有界间隙等已知结果。
- [Erdős Problems LaTeX — Problem 5](https://www.erdosproblems.com/latex/5) — Thomas F. Bloom / Erdős Problems contributors, 2025-08-31; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 给出可核对的原题、S=[0,∞] 的备注以及参考文献。
- [Erdős Problems — Discussion Thread 5](https://www.erdosproblems.com/forum/thread/5) — Erdős Problems users; Thomas Bloom comment, 2026-05-04; `forum`, `informal_claim`, directness=`direct`, reliability=`low`. 论坛显示 3 条评论，无解决声明；2025-08 的非正式回复称 1 的情形仍开放，2026-05 评论仅更正早期文献页码。页面也声明评论不经核验。
- [Primes in tuples I](https://annals.math.princeton.edu/2009/170-2/p10) — Daniel A. Goldston, János Pintz, Cem Y. Yıldırım, 2009-09-01; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 明确证明 liminf (p_{n+1}-p_n)/log p_n=0；由归一化等价性，0 属于本题的极限点集。
- [On limit points of the sequence of normalized prime gaps](https://doi.org/10.1112/plms/pdw036) — William D. Banks, Tristan Freiberg, James Maynard, 2016-08-23; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 证明任意九个非负实数中有两个之差属于极限点集，推得至少 12.5% 的非负实数为极限点；并非全覆盖结论。
- [A note on the distribution of normalized prime gaps](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/184/4/112647/a-note-on-the-distribution-of-normalized-prime-gaps) — János Pintz, 2018-09-18; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 该文明确回顾 Pintz 的 [0,c]⊂S 结果，且证明测度下界从约 T/8 改进至约 T/4；还明确说明 log p_n 与 log n 的归一化渐近相同。
- [Limit points of normalized prime gaps](https://doi.org/10.1112/jlms.12314) — Jori Merikoski, 2020-04-07; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 证明对每个 T≥0，极限点集与 [0,T] 的 Lebesgue 测度至少为 T/3，并证明存在绝对常数 C 使其与每个 [T,T+C] 相交；未证明 S=[0,∞)。
- [Polignac Numbers, Conjectures of Erdős on Gaps Between Primes, Arithmetic Progressions in Primes, and the Bounded Gap Conjecture](https://arxiv.org/abs/1305.6289) — János Pintz, 2013-05-27; `preprint`, `preprint`, directness=`indirect`, reliability=`medium`. 作为输入所列 2016 书章的公开预印本版本；用于追溯 [0,c]⊂S 的来源。
- [Analytical Investigation of Normalized Prime Gaps and Residue-Class Driven Sequences](https://www.researchgate.net/publication/405816241_Analytical_Investigation_of_Normalized_Prime_Gaps_and_Residue-Class_Driven_Sequences_A_conditional_solution_to_Erdos_Problem_5_by_the_use_of_AI) — Furkan Kaya, 2026-02-01; `preprint`, `informal_claim`, directness=`direct`, reliability=`low`. 该手稿自称为“conditional solution”，摘要明确说其结论依赖 Littlewood–Hardy k-tuple conjecture；因而不是无条件原题的解决。未发现同行评议发表或正式验证。

### 完成标准

- 肯定出口: Prove that for every finite C≥0, ε>0, and N≥1, there exists n≥N such that |(p_{n+1}-p_n)/log n-C|<ε. Equivalently, construct for each C an increasing subsequence along which the quotient converges to C.
- 否定出口: Prove that there exist a finite C≥0, ε>0, and N_0 such that for every n≥N_0, |(p_{n+1}-p_n)/log n-C|≥ε. This proves C is not a limit point and disproves the universal statement.

不构成完成：

- Proving only 0∈S, ∞∈S, [0,c]⊂S, or membership for a positive-measure, positive-density, or relatively dense subset.
- Finding finitely many numerical gaps near C, or inferring an infinite result from a histogram or random-model heuristic.
- Proving a claim about two primes that are not certified consecutive.
- Proving the statement conditional on Hardy–Littlewood, Elliott–Halberstam, or another unproved hypothesis while presenting it as an unconditional resolution.
- Changing from log p_n to log n, or from a location-scale statement to an index-scale statement, without a justified transfer.

正确性陷阱：

- The endpoints of every constructed gap must be consecutive primes; all intermediate integers require a compositeness certificate.
- The quantifiers are for every prescribed C, not merely for a set of C of positive measure or bounded gaps.
- A density statement about S does not imply S is all of [0,∞).
- C=0 must not be subsumed by an argument that divides by C or assumes a positive target interval.
- Track the conversion p_n~n log n and the resulting log p_n/log n→1 on exactly the constructed subsequence.
- All sieve/distributional hypotheses, uniformity ranges, exceptional moduli, and error terms must be checked simultaneously.
- The extended limit ∞ is already known and does not settle any finite target C.

### 更新后的 AI 可解答性

- 等级: `low_candidate`
- 分数: `12/100`
- 信心: `medium`
- 结论: 这是严谨定义且可独立审查的开放问题，但全覆盖目标远强于现有结果；AI 可有效做文献定理审计、提出并反驳中间引理，却不应把有限计算或启发式视为接近完整解答。

支持理由：

- 目标可化为明确的 C、ε、N 量词命题，正反结论都具有可检查证书。
- 存在相当具体的技术基线（连续性同余覆盖、Maynard–Tao 筛、Chen 筛），使新引理可与既有结果精确比较。
- 文献已把多个弱结论的边界写得很清楚，便于发现错误地从密度跳到全覆盖的推理。

主要障碍：

- 须把“正比例/有界间隙的目标集”升级为“每一个精确目标值”，没有已知的通用提升机制。
- 构造必须同时控制间隙主项、保证端点为连续素数，并在无穷尺度上控制误差。
- 可计算素数表只能检验有限谓词，不能证实全称的无穷子序列极限命题。

Proof-first 路线：

- 逐条重建 BFM 与 Merikoski 的参数化定理，定位从其有限目标集的“至少一个差值”到指定差值所缺的精确引理。
- 先证明或反驳一个明确桥梁引理：可调 Erdős–Rankin 覆盖和多素数簇结果能否把相邻候选平移的差固定到 C log n+o(log n)。
- 把 C=0、固定正 C 和大 C 分成独立机制；任何试图拼接它们的论证都先做量词审计。

需要验证：

- 逐页核验 BFM 2016、Pintz 2016/2018 和 Merikoski 2020 的定理编号、归一化、测度定义与常数依赖。
- 通过 MathSciNet、zbMATH、Crossref、arXiv 和主要作者主页补做 2021–2026 检索。
- 请解析数论专家审查 2026 条件手稿是否确实仅为条件结论及其对 Gallagher/Hardy–Littlewood 的引用。
- 若启动研究，先确认题库论坛后续评论没有新增可验证的文献链接或解答声明。

### 审计限制与人工复核理由

- 本审计仅使用公开可访问网络资料；没有使用 MathSciNet、zbMATH 或 Web of Science 的完整付费索引。
- 题库网页的访问结果一度由搜索索引提供；其 open 状态是近期数据库证据而非关于文献不存在的证明。
- 未逐页检查 Westzynthius、Erdős、Ricci、Hildebrand–Maier 的原始历史论文，相关早期结论在本审计中主要由当前题库和后续论文的回顾支持。
- 2026 条件手稿虽已查看摘要和可见正文，但未作逐行有效性验证；它的条件性已足以说明其不能无条件结题。
- 没有发现正式化并不构成所有 Lean/Isabelle/Coq/其他库的穷尽性否定。

- 应由解析数论专家逐条复核 BFM、Pintz、Merikoski 的完整证明和精确量词，尤其是“有界间隙”与“全覆盖”之间不可跨越的差别。
- 应使用专业索引补做 2021–2026 年的作者、引文追踪和最新预印本检索，以提高“仍开放”判断的覆盖度。
- 若后续代理拟研究该题，应先人工审阅并登记 2026 条件手稿的实际假设与逻辑，以避免把条件结论误报为解答。

<!-- DEEP_REVIEW:END -->
