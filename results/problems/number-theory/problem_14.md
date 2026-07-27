# Problem 14

## 基本信息

- 原始链接: https://www.erdosproblems.com/14
- LaTeX 页面: https://www.erdosproblems.com/latex/14
- 原始状态: `open`
- 奖金: `no`
- 主类别: `number theory`
- 原始标签: `number theory`, `sidon sets`, `additive combinatorics`
- 形式化状态: `yes`
- OEIS: `A143824`, `possible`
- 原站备注字段: 无

## 原问题

Let $A\subseteq \mathbb{N}$. Let $B\subseteq \mathbb{N}$ be the set of integers which are representable in exactly one way as the sum of two elements from $A$.

Is it true that for all $\epsilon>0$ and large $N$\[\lvert \{1,\ldots,N\}\backslash B\rvert \gg_\epsilon N^{1/2-\epsilon}?\]Is it possible that\[\lvert \{1,\ldots,N\}\backslash B\rvert =o(N^{1/2})?\]

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

- 所属标签偏证明密集：additive combinatorics, number theory, sidon sets
- 题面含渐近/无限对象线索：\gg, \ll, infinitely many, o(

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: additive combinatorics, number theory, sidon sets
- 有限/计算线索: finite, finitely
- 渐近/无限线索: \gg, \ll, infinitely many, o(
- 构造/存在性线索: construct

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **这是一个低到中等候选问题：GPT-5.5 级别模型配合计算、形式化证明和文献检索，较可能给出有限模型验证、构造实验、证明片段或把已知有限 analogue 与无限问题之间的障碍梳理清楚；但直接解决原问题的概率不高。**
- 等级: `low_to_medium_candidate`
- 分数: `42/100`
- 信心: `medium`
- 可能路线: 可行路线是把问题重写为表示函数 r_A(n) 的约束优化：要求大量 n 满足 r_A(n)=1，并估计 r_A(n)=0 或 r_A(n)>=2 的数量。模型可以先形式化有限版本，搜索小 N 的极值构造，尝试用 SAT/ILP/CP-SAT 验证最优或近最优样例，再把计数恒等式、加性能量、Sidon 型约束和边界效应组合成可机检的引理。更现实的成果是证明若干附加假设下的 N^{1/2-o(1)} 下界，或验证 Erdős-Freud 有限 analogue 常数与构造模式，而不是一次性解决完整无限问题。

### 支持理由

- 问题陈述短、对象明确，可直接转化为有限区间上的布尔选择变量和表示计数约束，适合计算搜索与形式化验证。
- 它有明确的有限 analogue：存在 A subset {1,...,N} 使非唯一表示数小于 2^{3/2}N^{1/2}，这给了模型可复现、可检验的目标尺度。
- 问题与 Sidon sets、加性组合和表示函数相关，已有工具链能处理部分计数不等式、能量估计、极值小例和自动化反例搜索。
- 要判断 o(N^{1/2}) 是否可能，计算实验可以帮助排除简单构造、发现周期或分块构造模式，并形成可证明猜想。

### 主要障碍

- 核心难点是无限集合的全局结构控制：有限区间最优或近最优并不自动给出所有大 N 的渐近下界。
- r_A(n)=1 是非常刚性的局部条件，但 complement 同时包含无表示和多重表示，两类坏点可相互抵消计数压力，简单能量法可能只给弱界。
- 备注中提到的上界构造接近 N^{1/2+epsilon}，说明目标下界若真为 N^{1/2-o(1)}，很可能需要接近最优的结构理论。
- 存在形式化版本并不意味着证明容易；Lean/Isabelle 更可能验证人工设计的引理，而难以自动发现关键组合结构。
- 若要排除 o(N^{1/2})，需要处理所有稀疏、分块、随机化或递归构造的 A，这超出纯计算枚举能力。

### 需要的验证

- 建立有限版本的精确定义：和是否有序、是否允许同一元素使用两次、A subset {1,...,N} 与 sums <=N 的边界处理必须固定。
- 对小到中等 N 运行 ILP/SAT/CP-SAT，记录最小 complement、极值 A 的结构，并与 2^{3/2}N^{1/2} 尺度比较。
- 把任何模型生成的不等式证明翻译为形式化证明或至少逐引理检查，尤其检查从有限区间到渐近大 N 的量词转换。
- 检索并核对备注中 Erdős-Freud 有限 analogue 以及 Erdős 所称构造的原始证明细节，避免基于不完整摘要误推。
- 测试候选反例构造在长区间、多尺度 N 和偏移区间上的表现，确认不是只在少数 N 上降低 complement。

### 公开版思考摘要

这个问题适合 AI 工具介入，因为它有清楚的表示函数表述、有限极值版本和可计算实验入口。GPT-5.5 很可能能搭建搜索程序、发现样例结构、形式化若干计数引理，并帮助判断哪些证明策略失败。但完整命题要求对任意无限集合 A 给出接近平方根级别的下界，且已知构造接近该尺度上界，因此关键步骤很可能是深的加性组合结构定理，而不是单纯枚举或常规能量估计。

### 免责声明

以上是对 GPT-5.5 加工具在该单一问题上的可推进性评估，不是该 Erdős 问题的解答，也不声称证明或反驳了原命题。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `likely_open`
- 状态信心: `medium`
- 可行动性: `needs_human_clarification`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_14.md](../../prompts/problem_14.md)

### 状态结论

截至审计日，Erdős Problems 的当前记录仍标为 open，且定向检索未发现可核验的解决或反例论文。该结论只能定为“很可能仍开放”：1991 年 Erdős–Freud 原论文的网页可核验书目信息和摘要，但本次无法取得其全文来独立核对网页转述的精确常数；近年检索仅找到一个把关键历史结论列为公理的 LeanGenius 工件，并非证明。题目应先明确采用无序表示 a≤b、A 的量词及隐含常数的依赖性；在该标准修订下，两个问题均仍是开放目标。

### 当前规范陈述

采用无序表示。对 A⊆ℕ 与 n∈ℕ，令 r_A(n)=#{(a,b)∈A×A:a≤b 且 a+b=n}，B_A={n∈ℕ:r_A(n)=1}，U_A(N)=|[1,N]\B_A|。记录实际上提出两个独立问题：(Q1) 对每个 A⊆ℕ 和每个 ε>0，是否存在 c=c(A,ε)>0、N_0=N_0(A,ε)，使所有整数 N≥N_0 都有 U_A(N)≥cN^{1/2−ε}？(Q2) 是否存在 A⊆ℕ 使 U_A(N)=o(N^{1/2})？编辑者仍须决定 Q1 的 c、N_0 是否本意上应对 A 一致；原文的 \gg_ε 本身未说明。

```text
Use unordered representations. For A⊆ℕ and n∈ℕ, set r_A(n)=#{(a,b)∈A×A:a≤b and a+b=n}, B_A={n∈ℕ:r_A(n)=1}, and U_A(N)=|[1,N]\B_A|. The record contains two separate questions: (Q1) for every A⊆ℕ and every ε>0, do there exist c=c(A,ε)>0 and N_0=N_0(A,ε) such that U_A(N)≥cN^{1/2−ε} for every integer N≥N_0? (Q2) does there exist A⊆ℕ such that U_A(N)=o(N^{1/2}) as N→∞? A human editor must decide whether Q1 was intended with c,N_0 uniform in A; the displayed notation alone does not settle this.
```

### 陈述、量词与反例审计

- 歧义严重度: `material`
- 简单反例检查: `counterexample_found`
- 检查说明: 对“有序表示”这一字面解释有立即退化：若 n=a+b 且 a≠b，则 (a,b) 与 (b,a) 是两种表示，故 B_A 只能包含形如 2a 的和；于是 U_A(N)≥⌊N/2⌋，Q1 平凡为真而 Q2 为假。这不是对预期的无序版本的反例，而证明了原文必须固定表示约定。对采用 a≤b 的标准版本，未发现简单反例。
- 版本变化: Erdős Problems 的历史页显示，至少在 2025-10-20 的可见修订与当前文字相同，未记录数学命题的实质改写。当前页面备注将该问题的早期归属描述为 Erdős–Nathanson，但又称 Erdős 后来归于 Erdős–Sárközy–Szemerédi且未给出处；此归属尚不能视为已核实。

陈述问题：

- “exactly one way”未说明是否把 (a,b) 与 (b,a) 视为同一表示，也未说明是否允许 a=b。Sidon-set 文献及本题的形式化工件都采用 a≤b，故这是最合理的修订；若把有序对算作不同方式，则任意 a≠b 的和自动至少有两种有序表示，问题会退化。
- 题面先“Let A⊆ℕ”但没有显式写出 Q1 的“对所有 A”与 Q2 的“存在 A”；标准阅读如此，但应写明。
- \gg_ε、\ll_ε 与“large N”没有说明常数和阈值是否依赖 A。固定 A 的渐近命题通常允许依赖 A；若要求对所有 A 一致，则是更强且不同的命题。
- Q1 的 N^{1/2−ε} 下界并不逻辑否定 Q2：例如量级 N^{1/2}/log N 同时满足每个固定 ε 的 Q1 型下界和 o(N^{1/2})。因此不得把两问当作正反命题。
- 题面的“not representable in exactly one way”包括零表示与至少两种表示；不应误改为只计多重表示。

需要固定的量词/约定：

- Representations must be unordered with repetition permitted: count pairs (a,b) with a≤b.
- Q1 is naturally ∀A∀ε>0∃c>0∃N_0∀N≥N_0, but uniformity of c,N_0 in A is not specified by the source.
- Q2 is ∃A such that lim_{N→∞}U_A(N)/√N=0.
- For each fixed ε, the constants implicit in \gg_ε and \ll_ε may depend on ε; their dependence on A must be declared.
- Q1 and Q2 are independent in the sense that Q1 as written does not negate Q2.

### 文献与当前边界

已核验的主要结果：

- Erdős Problems 当前备注报告：Erdős 曾构造某个无限 A，使对每个 ε>0，U_A(N)≪_ε N^{1/2+ε}（所有充分大 N）；同一备注还报告对每个 ε>0 存在无穷多个 N 有 U_A(N)≫_ε N^{1/3−ε}。这是数据库转述，不应在未查阅原始构造前升级为独立验证的定理。
- Erdős–Freud（1991，同行评审）是已核验的有限 Sidon/和集论文。数据库将其有限类比转述为：对每个 N 存在 A⊆[1,N]，使 [1,N] 中非唯一表示数少于 2^{3/2}√N，并称作者猜测常数可能最佳。由于本次未能查看正文，这个精确不等式应作为“待全文核验的历史已报道结果”。
- O'Bryant（2004）的同行评审注释书目确认 Erdős–Freud 论文并概述其有限 Sidon 和集、均匀分布和 quasi-Sidon 内容；它没有给出本题无限 Q1/Q2 的解决。
- LeanGenius（2026）的工件实现了 a≤b 的表示计数、一些基本引理和问题陈述，但将 Erdős 构造与 Erdős–Freud 有限结果作为公理，因此没有缩小开放证明缺口。

最近相关工作：本次针对 2023–2026、arXiv、精确短语及作者名的检索，没有找到直接处理 Q1 或 Q2 的近期同行评审论文或预印本。最晚直接命中的材料是 2026-02-15 LeanGenius 的“axiomatized”定义工件，而非解答；这一“未发现”不是不存在新结果的证明。

剩余核心：在 a≤b、重复允许的标准解释下，仍须分别决定：(Q1) 任意无限 A 的 U_A(N) 是否最终至少为每个 N^{1/2−ε} 量级；(Q2) 是否存在单个无限 A 令 U_A(N)/√N→0。尤其不能用 Q1 型次幂损失下界声称排除了 Q2。

已使用方法：

- 有限 Sidon 序列的和集与分布研究。
- quasi-Sidon／有限极值构造。
- 表示函数 r_A(n) 的计数与缺失/多重表示分解。
- 形式化工件中的基本组合计数和 Sidon 差分注入论证。

争议或不确定性：

- 原题的有序/无序表示、a=b 是否允许、Q1 常数是否一致于 A，均未在网页题面写明。
- 历史归属存在数据库自己注明的冲突且无参考文献。
- 网页转述的 Erdős 构造和 Erdős–Freud 精确常数尚未由本次直接阅读全文独立核对。
- 当前 open 标签与定向检索相符，但不构成穷尽性文献证明。

### 证据来源

- [Erdős Problems, Problem 14](https://www.erdosproblems.com/14) — Erdős Problems database, date unknown; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 当前数据库题面将该问题标为 open，并给出两问及 Erdős–Freud 的有限版本备注；数据库标签本身不是解决状态的证明。
- [Revision history of Erdős Problem 14](https://www.erdosproblems.com/history/14) — Erdős Problems database, 2025-10-20; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 可直接核验当前题面、2025-10-20 可见版本及网站对历史构造、无限次 N 下界和有限类比结果的转述。
- [Erdős Problems forum thread for Problem 14](https://www.erdosproblems.com/forum/thread/14?embed=1) — Erdős Problems forum users, date unknown; `forum`, `informal_claim`, directness=`indirect`, reliability=`low`. 检索到该题论坛线程；其可见内容复述了页面备注，未提供可审阅的解决或反例证明。
- [On sums of a Sidon-sequence](https://www.sciencedirect.com/science/article/pii/0022314X9190083N) — P. Erdős; R. Freud, 1991-06-01; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 核验了 J. Number Theory 38(2), 196–205 与 DOI 10.1016/0022-314X(91)90083-N；摘要明确该文研究有限 Sidon 序列的和。网页摘要未展示本审计所需的有限构造精确不等式，故该精确结论仍需人工查阅全文核验。
- [A Complete Annotated Bibliography of Work Related to Sidon Sequences](https://www.combinatorics.org/ojs/index.php/eljc/article/download/DS11/pdf/) — Kevin O'Bryant, 2004; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 该注释书目核验 Erdős–Freud 论文的书目信息，并概述其研究有限 Sidon 集的分布、和集和 quasi-Sidon 推广；它不证明本题的无限版本。
- [Some of my forgotten problems in number theory](https://hrj.episciences.org/125) — Paul Erdős, 1992-01-01; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 核验该 1992 年文章及其公开下载入口；它与数据库所称 Erdős 的后续说法在时间上相关。PDF 下载在本次审计超时，因此未把未阅全文中的具体构造或归属作为独立已核验事实。
- [Erdős #14: Unique Representation Sums](https://leangenius.org/proof/erdos-14-unique-sums) — Lean Genius, 2026-02-15; `formalization`, `formalized_artifact`, directness=`direct`, reliability=`medium`. 该工件明确定义表示为 a≤b，并形式化计数基础；其页面将历史主要结果列为 axioms，因而不是 Q1 或 Q2 的形式化证明，也不是解决证据。
- [OEIS A389182](https://oeis.org/A389182) — OEIS Foundation and contributors, date unknown; `oeis`, `database_record`, directness=`indirect`, reliability=`medium`. 该条目以 a≤b 表达有限和的无序约定，并引用 Erdős–Freud；它只支持约定及有限相关背景，不支持无限问题的状态。

### 完成标准

- 肯定出口: For Q1, a complete affirmative resolution is a proof, under the declared unordered convention and declared A-dependence of constants, that ∀A⊆ℕ ∀ε>0 ∃c>0 ∃N_0 ∀N≥N_0: U_A(N)≥cN^(1/2−ε). For Q2, a complete affirmative resolution is one explicitly defined A⊆ℕ together with a proof that lim_{N→∞}U_A(N)/√N=0.
- 否定出口: For Q1, a complete negative resolution is an explicit A⊆ℕ and ε>0 for which U_A(N)/N^(1/2−ε) has liminf 0 (equivalently, no eventual positive lower constant exists). For Q2, a complete negative resolution is a proof that every A⊆ℕ has limsup or an eventual lower obstruction incompatible with U_A(N)=o(√N). The two questions must be audited independently because these outcomes are not logical complements across Q1 and Q2.

不构成完成：

- An upper bound U_A(N)≪_εN^(1/2+ε) for some A does not establish Q2.
- A lower bound U_A(N)≫_εN^(1/2−ε) does not refute Q2.
- A finite family A_N⊆[1,N] with U_{A_N}(N)=O(√N) does not supply one infinite A for Q2.
- A proof using ordered representations answers a different, trivialized convention.
- Numerical evidence over finite N, or a formalization that axiomatizes the principal construction or bound, is not a resolution.

正确性陷阱：

- Count unordered pairs a≤b, including doubles a=a; do not count (a,b) and (b,a) separately.
- Keep zero representations and representations of multiplicity at least two together in U_A(N).
- Fix whether all constants and thresholds may depend on A; a proof for a fixed A with uncontrolled dependence is not a uniform-in-A theorem.
- Respect the order of ∀A, ∀ε, ∃c, ∃N_0, ∀N.
- Do not infer that Q1 excludes Q2 without proving an Ω(√N)-type obstruction.
- An infinite construction must control every sufficiently large N for Q2, not only an infinite subsequence.

### 更新后的 AI 可解答性

- 等级: `low_candidate`
- 分数: `12/100`
- 信心: `medium`
- 结论: 在明确无序表示和量词后，这是一个定义清楚但长期且宽泛的加法组合问题；适合做结构性探索和严格的引理审计，不宜期待由有限计算直接解决。

支持理由：

- 存在可精确定义的表示函数、明确的渐近目标和可独立核验的有限引理。
- 已有有限 Sidon/quasi-Sidon 背景和接近 √N 的历史上界报道，说明问题不是纯粹无结构。
- Q1 与 Q2 分离后，研究者可选择一个明确目标而不混淆逻辑关系。

主要障碍：

- 两个核心断言长期未解，且已知的 N^{1/2±ε} 型信息留下宽广的对数与次幂缺口。
- 无限单集构造与逐个大 N 的控制远强于每个 N 单独选择有限集。
- 题面中的量词和常数依赖尚需人工确认；不同选择改变目标强度。
- 有限枚举不能证明渐近下界或构造单个无限反例。

Proof-first 路线：

- 先完成定义修复，并把 U_A 分解为缺失和与至少两次表示和；证明任何候选不等式在该分解下的精确形式。
- 从一个明确的局部结构引理出发，例如：若某尺度上的 A 有足够多的唯一和，则相邻尺度必须产生可量化的缺失或碰撞；只有得到可叠加的引理才进入全局渐近。
- 单独审计历史构造的参数和拼接机制，判断其是否能从 N^{1/2+ε} 改善到 o(√N)，而不把“有限每尺度构造”误当成无限构造。

需要验证：

- 获取并逐条核对 Erdős–Freud（1991）全文中有限问题的定义、范围和 2^{3/2} 常数。
- 获取 Erdős（1992）全文，核对无限构造、N^{1/3−ε} 无穷子列陈述与历史归属。
- 由题目维护者确认 Q1 中常数/阈值是否必须一致于 A。
- 若依赖 LeanGenius，下载其源文件并确认哪些引理实际被证明、哪些仅为公理。

### 审计限制与人工复核理由

- 主问题页和 LaTeX 页的直接打开返回内部错误；题面、历史页和论坛内容经搜索索引/历史页交叉取得。
- Erdős–Freud 原文的网页记录和摘要可访问，但全文级定理核对未完成；因此 2^{3/2} 常数和数据库所述有限陈述不能在本审计中称为由原文独立验证。
- Erdős（1992）下载链接超时、HAL 镜像拒绝访问；无法独立确认其构造和归属。
- 针对近期论文和 arXiv 的定向检索未找到直接进展，但搜索失败不是不存在结果的证明。
- LeanGenius 是第三方形式化工件；其“axiomatized”标记意味着它不能作为已形式化解决的证据。

- 须由题目维护者确认“one way”采用无序且允许重复，以及 Q1 常数/阈值是否允许依赖 A。
- 须取得并人工核对 Erdős–Freud（1991）与 Erdős（1992）全文，才能把数据库转述提升为已验证的精确历史定理。
- 开放状态具有中等而非高置信度：虽页面与定向检索一致，仍不能证明检索覆盖了全部最新文献。

<!-- DEEP_REVIEW:END -->
