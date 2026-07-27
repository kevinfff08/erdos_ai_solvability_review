# Problem 41

## 基本信息

- 原始链接: https://www.erdosproblems.com/41
- LaTeX 页面: https://www.erdosproblems.com/latex/41
- 原始状态: `open`
- 奖金: `$500`
- 主类别: `number theory`
- 原始标签: `number theory`, `sidon sets`, `additive combinatorics`
- 形式化状态: `yes`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

Let $A\subset\mathbb{N}$ be an infinite set such that the triple sums $a+b+c$ are all distinct for $a,b,c\in A$ (aside from the trivial coincidences). Is it true that\[\liminf \frac{\lvert A\cap \{1,\ldots,N\}\rvert}{N^{1/3}}=0?\]

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `22/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- 题面或备注出现有限对象/计算线索
- 已有形式化陈述，可降低语义误读风险

### 主要障碍

- 所属标签偏证明密集：additive combinatorics, number theory, sidon sets
- 题面含渐近/无限对象线索：liminf
- 原记录含奖金 $500，说明该题被长期视为高价值难题；这不是否定依据，但提高验证门槛。

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: additive combinatorics, number theory, sidon sets
- 有限/计算线索: finite
- 渐近/无限线索: liminf
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **有一定推进潜力，但不应视为高概率可完全解决。该问题是三重 Sidon/B_3 集的奇数阶临界密度问题；给定材料显示 h=2、h=4 和所有偶数 h 已有结果，而 h=3 仍开放，说明主要困难不是计算规模，而是缺少适合奇数阶的结构性论证。GPT-5.5 级别模型配合工具较可能完成文献脉络重建、形式化已有引理、搜索有限模型和提出可检验的中间命题；直接给出完整证明的概率偏低。**
- 等级: `low_to_medium_candidate`
- 分数: `38/100`
- 信心: `medium`
- 可能路线: 较可行的路线是围绕 B_3 条件建立可形式化的计数不等式：把 A∩[1,N] 的三重和唯一性转化为受限超图或加性能量约束，尝试证明若 |A∩[1,N]| 长期保持 cN^{1/3} 的正下界，则在某些区间、模数或差分结构中必然产生非平凡三重和碰撞。工具可用于检验小规模极值构造、搜索潜在反例模式、形式化局部组合恒等式，并对偶数 h 证明中的可迁移部分做机器辅助重构。

### 支持理由

- 问题陈述短且形式化状态为 yes，适合把关键命题拆成 Lean/Isabelle 等可验证的局部引理。
- 已有 h=2、h=4 和所有偶数 h 的正面结果，说明存在相关证明技术可被模型系统性拆解、迁移和压力测试。
- B_3 条件具有明确的有限截断版本，计算工具可以搜索高密度有限 B_3 集、极端构造和碰撞模式，用于发现或否定候选引理。
- 目标是 liminf 为 0，不要求给出精确最大规模；这可能允许通过平均化、区间分解或稀疏化论证取得进展。

### 主要障碍

- h=3 是奇数阶情形，给定材料显示偶数阶已有统一结果但未覆盖它，暗示偶数证明可能依赖配对、二次型或对称化机制，不能直接迁移。
- liminf 结论涉及无限集合的全局分布，有限规模搜索只能提供启发，不能直接验证或反驳定理。
- 若存在接近 N^{1/3} 的随机或代数构造，其局部行为可能非常接近反例，使简单计数界难以达到严格矛盾。
- 完整证明很可能需要新的加性组合结构定理，而这类创造性瓶颈并非仅靠形式化或暴力搜索即可突破。

### 需要的验证

- 核查并形式化 B_3 条件下三重和“trivial coincidences”的精确定义，避免排列等价和重复元素情形造成漏洞。
- 重建 h=2、h=4、偶数 h 证明的核心引理，标注哪些步骤真正使用偶数性。
- 对候选证明中的每个密度递降、区间选择和极限交换步骤做形式化或半形式化检查。
- 运行有限 B_3 集极值搜索，检查任何提出的强中间引理是否已被小规模构造反驳。
- 如模型提出反例族，需要验证其确为无限 B_3 集，并证明其 liminf 归一化计数不为 0；这通常比有限验证难得多。

### 公开版思考摘要

这个问题的可攻性来自其定义清晰、已有相邻阶结果和可计算有限模型；难点在于 h=3 正好落在偶数方法之外，且目标是无限集的渐近下极限。GPT-5.5 级别系统很适合作为证明工程和猜想筛选工具，能显著整理路线、排除错误引理并可能证明受限版本；但要独立补上奇数阶核心新思想，成功率仍偏低。

### 免责声明

以上是对 AI 辅助可解性和推进潜力的审查，不是该 Erdős 问题的解答，也不声称给出了证明或反例。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `confirmed_open`
- 状态信心: `medium`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_41.md](../../prompts/problem_41.md)

### 状态结论

按标准的 B_3 定义，此问题仍可确认是开放的：Erdős Problems 的现行问题页和讨论串均在 2026-04-06 标为 open，且讨论串没有任何解答或部分解答声明。针对精确陈述、Helm 的 B_3 论文、近三年文献和形式化库的检索未发现可核验的证明或反例。该结论不是“绝无新结果”的逻辑证明；arXiv API 在本次审计中被网络拒绝，且 Helm 1996 全文未能取得，故置信度为中等。

### 当前规范陈述

对每个无限集合 A⊆N_{>0}，允许加数重复，并要求 B_3 性质：任取 A 中满足 a_1≤a_2≤a_3、b_1≤b_2≤b_3 的三元组，若 a_1+a_2+a_3=b_1+b_2+b_3，则 (a_1,a_2,a_3)=(b_1,b_2,b_3)。证明 liminf_{N→∞}|A∩{1,…,N}|/N^{1/3}=0；等价地，存在 N_j→∞ 使 |A∩[1,N_j]|=o(N_j^{1/3})。

```text
For every infinite set A subseteq N_{>0} satisfying the B_3 property (with repetitions allowed), namely: for all a_1<=a_2<=a_3 and b_1<=b_2<=b_3 in A, if a_1+a_2+a_3=b_1+b_2+b_3, then (a_1,a_2,a_3)=(b_1,b_2,b_3), prove that liminf_{N->infinity} |A cap {1,...,N}|/N^{1/3}=0. Equivalently, every such A has a sequence N_j->infinity on which |A cap [1,N_j]|=o(N_j^{1/3}).
```

### 陈述、量词与反例审计

- 歧义严重度: `material`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 未找到能推翻标准 B_3 陈述的简单构造。有限 B_3 集、贪心 B_3 序列数据、或仅有大 limsup 的无限集都不是反例；反例必须是一个单一无限 B_3 集，并满足其归一化计数函数的 liminf 严格为正。
- 版本变化: Erdős Problems 的历史页显示至少 2025-10-20 与 2026-04-06 的版本保留相同核心文字，未显示命题本身的修订。需作的修订是定义与元数据层面：显式写成允许重复的多重集 B_3 条件，并将“已形式化”改注为“已有较弱、遗漏重复项的形式化草稿”；偶数阶历史结果应引 Helm 1993（或另行核验 Jia 的正式版本），而非仅依赖 Chen 1996。

陈述问题：

- 原文的“aside from the trivial coincidences”未定义；标准且可与文献一致的含义是：三项和的表示只可由排列改变，重复加数仍被允许。
- 现有 Lean 文件并未形式化这个标准 B_3 条件：其 NtupleCondition 用基数为 3 的 Finset 表示三项，因而只检查三个互异加数，遗漏 a+a+b、3a 等允许重复的表示。数据库“formalised: yes”不能视为该标准问题已被正确形式化。
- 备注中“Chen 1996 证明所有偶数 h”的归因不可靠：该文可核对到的摘要给出的是带正对数因子的上界，单独并不推出 liminf A(n)/n^{1/(2k)}=0。所述偶数阶结论本身由 Helm 1993 的同行评审论文直接支持。

需要固定的量词/约定：

- The universal quantifier ranges over every infinite A subseteq N_{>0}.
- 'Trivial coincidences' must mean equality of the two multisets of three summands; after sorting, the triples are identical.
- Summands may repeat. Thus (a,a,b) and (c,d,e) are admissible representations to compare.
- N ranges over positive integers and tends to infinity; the ratio is nonnegative, so its being nonzero is equivalent to having positive liminf.
- The target is a liminf statement, not an upper-density or limsup statement.

### 文献与当前边界

已核验的主要结果：

- Erdős 的 h=2（Sidon）版本已解；当前问题页报告其结论为 liminf A(N)/N^(1/2)=0。
- Nash（1989）解决 h=4；Helm（1993）给出所有偶数 h=2k 的证明。Helm 的论证及摘要表明这不包含奇数 h=3。
- Helm（1996）针对 h=3 证明：若 A(N)~alpha N^(1/3)，则 A 不是 B_3；这只排除了具有正极限常数的规则增长，未排除 liminf>0 但计数函数振荡的情形。
- White（2024）改进有限 B_3[1] 集的极值常数上界，属于相关的有限问题；它不提供同一无限集合跨所有尺度的 liminf 控制。

最近相关工作：本次检索中最晚的相关同行评审工作是 White（2024），但它只处理有限 B_3[1] 极值常数。直接讨论本题无限 B_3 liminf 目标的最新已定位工作是 Helm（1996）。对近三年精确短语的网页搜索未找到解决论文；arXiv API 查询遭连接拒绝，故不能把这一否定搜索当作完备数据库证明。

剩余核心：证明或反驳：每个单一无限、允许重复加数的 B_3 集 A 是否必须在无穷多个尺度 N 上满足 A(N)=o(N^(1/3))。Helm 的 A(N)~alpha N^(1/3) 排除结果留下的核心是控制不规则或振荡的近临界增长。

已使用方法：

- 偶数阶的已知论证使用 B_{2k} 结构和计数/区块比较；其奇偶性依赖不能直接移植到三项和。
- Helm 1996 从 B_3 的表示唯一性导出必要条件，并排除精确幂律渐近。
- 有限 B_h[g] 研究使用卷积、自卷积范数、傅里叶分析与组合计数来改进极值常数；从有限常数到无限 liminf 需要额外的一致跨尺度论证。
- 形式化可用于核对定义和最终辅助引理，但当前 Lean 文件须先换成允许重数的 multisets/finsets-with-multiplicity 表述。

争议或不确定性：

- 站点的 open 标签是当前数据库判断而非文献完备性证明；站点本身也作出此警告。
- 输入备注把所有偶数 h 的结论归于 Chen 1996，但可核对的 Chen 摘要只给出含对数因子的界；Helm 1993 可直接支持该历史结论。
- “formalised: yes”具有误导性：现有形式化遗漏重复加数，且定理体均为 sorry。
- Helm 1996 的书目和作者摘要已核验，但本次未取得全文，故其“其他必要条件”的具体强度不应在本审计中夸大。

### 证据来源

- [41 Discussion Thread | Erdős Problems](https://www.erdosproblems.com/forum/thread/41) — T. F. Bloom / Erdős Problems community database, 2026-04-06 (last edited); `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 现行页将 #41 标为 OPEN，明确说明不能由有限计算解决；页面称无评论中的完整或部分解答声明，并警告状态只是站点所有者的当前判断。
- [Revision history of Erdős Problem 41](https://www.erdosproblems.com/history/41) — T. F. Bloom / Erdős Problems community database, date unknown; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 核对了现行陈述和历史版本；2025-10-20 与 2026-04-06 的核心问题文字相同。
- [A Complete Annotated Bibliography of Work Related to Sidon Sequences](https://www.combinatorics.org/ojs/index.php/eljc/article/download/DS11/pdf/) — Kevin O'Bryant, 2004; `secondary_index`, `peer_reviewed`, directness=`direct`, reliability=`high`. 列出 Helm 1996《On the distribution of B3-sequences》的作者摘要：它证明不存在 A(n)~alpha n^(1/3) 的 B_3 序列，并给出其他必要条件；该摘要仍将目标 liminf 命题称为 Erdős 猜想。还核对 Chen 1996 的实际对数因子结论。
- [On the distribution of B3-sequences](https://www.sciencedirect.com/science/article/pii/S0022314X96900694) — Martin Helm, 1996-05; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`medium`. 最直接的已知 h=3 进展：排除精确渐近 A(n)~alpha n^(1/3)，但没有证明所求 liminf 为零。题名、作者、卷期页码由 JNT 书目记录交叉核对；本次未取得全文。
- [On B_{2k}-sequences](https://eudml.org/doc/206528) — Martin Helm, 1993; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 摘要和全文可见：证明 Erdős 的 liminf 结论对所有偶数阶 B_{2k} 成立，并说明 h=4 的情形已由 Nash 得到。它支持“偶数 h 已解决”，但不适用于 h=3。
- [A note on B_{2k}-sequences](https://www.sciencedirect.com/science/article/pii/S0022314X96900013) — Sheng Chen, 1996-01; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`medium`. 书目与注释记录的结论为 liminf A(n)/(n^(1/(2k))(log n)^(1/(4k-4)))<infinity；这本身不蕴含无对数因子的 Erdős liminf 命题。
- [FormalConjectures/ErdosProblems/41.lean](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/41.lean) — Formal Conjectures Authors / Google DeepMind repository contributors, date unknown; `formalization`, `formalized_artifact`, directness=`direct`, reliability=`high`. 文件把三项条件定义为两个基数为 3 的 Finset 的和相等则集合相等，故只处理互异加数；目标和 pairwise 变体均为 sorry，未含证明。
- [An optimal L^2 autoconvolution inequality](https://www.cambridge.org/core/journals/canadian-mathematical-bulletin/article/an-optimal-l2-autoconvolution-inequality/8D109D51F271CC78EBDA2C99FB35612D) — Ethan Patrick White, 2024-03; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 近期有限 B_h[1] 研究：改进有限 B_3 与 B_4 集最大规模常数的上界；论文明确区分有限 R_h[g](N) 问题，未解决单一无限 B_3 集的 liminf 问题。
- [A096772: a greedy B3-sequence](https://oeis.org/A096772) — OEIS Foundation / Rick L. Shepherd and contributors, 2004; `oeis`, `database_record`, directness=`direct`, reliability=`medium`. 给出标准贪心 B_3 定义：比较 1<=i<=j<=k 的三项和，明确允许重复指标；它有助于消除“trivial coincidences”的定义歧义，但不是关于 liminf 的证明。

### 完成标准

- 肯定出口: A complete affirmative resolution is a rigorous proof that every infinite B_3 set A subseteq N_{>0}, where equal triple sums are identified only up to permutation and repetitions are allowed, satisfies liminf_{N->infinity} A(N)/N^{1/3}=0.
- 否定出口: A complete negative resolution is one explicit infinite set A subseteq N_{>0}, together with a proof of the full repeated-summand B_3 property and a proof that liminf_{N->infinity} A(N)/N^{1/3}>0.

不构成完成：

- Proving only that no B_3 set has A(N)~alpha N^{1/3} for a fixed alpha>0.
- Obtaining a bound along one finite interval, or constructing unrelated finite B_3 sets for infinitely many N.
- Showing a statement about limsup, upper density, or a logarithmically weakened upper bound without producing an N_j subsequence giving ratio 0.
- Citing an even-order B_{2k} theorem without a valid reduction from B_3 to an even-order problem.
- Checking the weaker distinct-summands-only condition formalized in the current Lean file.

正确性陷阱：

- Treat a+b+c and a permutation of its summands as the same representation, but do not exclude repeated summands such as a+a+b or 3a.
- For a claimed B_3 construction, test all sorted triples a_1<=a_2<=a_3, not merely triples of distinct elements.
- Keep the quantifier order: one fixed infinite A must work at every scale; finite extremizers cannot be pasted together without proving cross-block uniqueness.
- Distinguish a positive liminf from a positive limsup; the conjecture only needs a sparse subsequence of scales.
- Do not infer the h=3 case from the all-even-order theorem or infer the desired conclusion from Chen's logarithmically weakened bound.
- If using formal verification, encode triples as multisets or an equivalent multiplicity-aware object and prove equivalence to the sorted-triple definition.

### 更新后的 AI 可解答性

- 等级: `low_candidate`
- 分数: `10/100`
- 信心: `medium`
- 结论: 这是定义明确但长期停滞的开放证明目标；适合进行严格的文献复核、引理探索和形式化定义修复，但当前证据不支持把它视作高概率可由 AI 在短期内解决的问题。

支持理由：

- 目标是一个清晰的全称命题，肯定与否定都有可检查的证明证书。
- 已有 h=2、偶数 h 与 h=3 的精确幂律排除结果，提供了可审计的基线。
- 现有 B_3 形式化草稿可被修正后用于定义和局部引理检查。

主要障碍：

- h=3 是奇数阶遗留核心；偶数阶方法并未给出可直接复用的 h=3 化约。
- Helm 1996 之后直接针对无限 h=3 liminf 的可定位进展很少，表明剩余缺口并非简单技术细节。
- 有限 B_3 极值常数和小规模搜索无法控制单一无限集合的 liminf。
- 现有形式化遗漏重复项，不能直接作为正确性背书。

Proof-first 路线：

- 先从 Helm 1996 的已证必要条件精确重建其逻辑边界，寻找能把“正 liminf”而非“存在渐近常数”送入矛盾的引理。
- 独立探索跨尺度分解、三和表示唯一性与差集/卷积约束之间的可证明桥梁；任何候选桥梁须先给出可独立验证的定理陈述。
- 将标准 B_3 条件正确形式化，并只形式化已经手工证明的辅助等价和计数引理。

需要验证：

- 取得并逐项阅读 Helm 1996 全文，核对其全部必要条件及是否存在未被数据库摘要记录的强化。
- 在 MathSciNet、zbMATH 或出版社索引中补做 B_3/B_h 无限序列的 1996--2026 引文追踪；本次 arXiv API 连接失败。
- 若出现任何解答主张，先对重复加数、跨尺度量词和 liminf 三项做独立审稿，再更新状态。

### 审计限制与人工复核理由

- 本次不能取得 Helm 1996 全文；其核心摘要结论有高质量二级来源支持，但其他必要条件未逐条复核。
- arXiv API 查询因 WinError 10061 被拒绝；已用精确题名、作者、术语、问题页、论坛、出版社/书目和近三年网页检索补充，但无法声称 arXiv 搜索完备。
- 没有使用除用户提供的单一问题 JSON 以外的本地仓库资料。
- “未发现新解”是针对本次目标检索的证据判断，不是对全部未索引文献或未来发表物的证明。

- 在投入实质研究前，应由人工或有数据库权限者取得并阅读 Helm 1996 全文，确认其全部 h=3 必要条件及后续引文链。
- 应复核 Chen 1996 与 Helm 1993 的历史归因，并修正问题数据库的 remarks/形式化标记。
- 若后续有人依赖 Lean 文件，必须先以允许重数的定义重写并检查其与标准 B_3 定义的等价性。

<!-- DEEP_REVIEW:END -->
