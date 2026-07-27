# Problem 65

## 基本信息

- 原始链接: https://www.erdosproblems.com/65
- LaTeX 页面: https://www.erdosproblems.com/latex/65
- 原始状态: `open`
- 奖金: `no`
- 主类别: `graph theory`
- 原始标签: `graph theory`, `cycles`
- 形式化状态: `no`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

Let $G$ be a graph with $n$ vertices and $kn$ edges, and $a_1<a_2<\cdots $ be the lengths of cycles in $G$. Is it true that\[\sum\frac{1}{a_i}\gg \log k?\]Is the sum $\sum\frac{1}{a_i}$ minimised when $G$ is a complete bipartite graph?

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `29/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 题面或备注出现有限对象/计算线索

### 主要障碍

- 题面含渐近/无限对象线索：\gg, asymptotic, o(, sufficiently large

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: cycles, graph theory
- 证明密集标签命中: 无
- 有限/计算线索: graph
- 渐近/无限线索: \gg, asymptotic, o(, sufficiently large
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **有中等偏高的可推进性，但不应期待一次性完全解决。第一问在给定备注中已由已有结果解决；真正剩余的是“完全二部图是否给出最小值”的精确极值结构问题。GPT-5.5 级别模型配合计算、文献检索、反例搜索和证明助理，更可能在整理已知证明、检验小规模反例、提出稳定化/极值候选框架方面显著推进，而不是直接给出完整无缺的开放问题证明。**
- 等级: `medium_candidate`
- 分数: `68/100`
- 信心: `medium`
- 可能路线: 可行路线是先把问题转化为“固定 n 与平均边数 k 时，出现的不同圈长集合的倒数和”的极值问题；用文献检索复核 GKS84、LiMo20 及备注中提到的后续工作是否已改变第二问状态；再用反例搜索枚举小图和稠密图模型，比较完全二部图、近完全二部图、随机图、分层构造和删边构造的圈长谱；最后尝试证明稳定性命题：若倒数和接近下界，则图的结构必须接近完全二部或某类二部极值图。形式化证明工具可用于验证圈长谱计算、极小反例归约和若干有限配置排除。

### 支持理由

- 给定备注表明第一问已有强结果：不仅有 \gg \log k 的下界，还有渐近尖锐的 \geq (1/2-o(1))\log k，因此剩余问题有清晰的研究边界。
- 问题的对象是圈长集合而非圈数量，适合用计算枚举和 SAT/ILP/图搜索工具寻找小规模反例或支持性证据。
- 完全二部图的圈长结构相对显式，模型可以较可靠地计算其候选值，并与理论下界的常数项关系进行比较。
- 已有渐近下界为证明精确极值或稳定性提供了入口，AI 可围绕现有证明寻找可加强的步骤，而不是从零处理一个完全无结构的问题。
- 问题属于极值图论中的结构型开放问题，GPT-5.5 配合检索和形式化检查有机会产出有价值的 lemma、归约、实验数据或错误候选排除。

### 主要障碍

- 第二问要求全局极值结构，不只是渐近下界；可能需要精细处理低阶项、有限 k、n 与 k 的关系以及极值唯一性。
- 圈长集合的倒数和对少量短圈非常敏感，局部改动可能显著改变目标函数，导致常规平均度或扩张性论证不够精细。
- 给定备注中关于完全二部图的“minimised”与后续工作“maximised”的表述存在方向上的潜在张力，需要先澄清原始文献或页面是否有误写、语境差异或不同约束。
- 如果第二问仍开放，完整证明很可能依赖深层极值图论技术；模型容易生成貌似合理但无法覆盖所有稠密/非均匀构造的证明草图。
- 形式化证明当前缺失，且图论极值证明通常包含复杂的正则性、扩张或吸收型论证，自动形式化成本较高。

### 需要的验证

- 核查当前文献，确认第二问截至审查时是否仍开放，以及备注中提到的后续工作是否已发表并改变问题状态。
- 计算完全二部图在相关参数范围内的精确 \sum 1/a_i，并明确 n、k、部大小取值对候选最小值的影响。
- 进行小规模穷举或约束搜索，验证是否存在比完全二部图更小的圈长倒数和，并记录所有极值或近极值图。
- 复现或阅读 GKS84 与 LiMo20 的关键证明步骤，判断哪些不等式可能被加强到结构稳定性。
- 若提出证明，需要用独立脚本、证明助理或专家审阅检查每个归约是否保持“不同圈长集合”的目标函数。

### 公开版思考摘要

这个问题的可攻性来自已有强下界和显式候选构造：第一问已由给定备注中的结果解决，第二问集中在完全二部图是否极小这一结构判断上。GPT-5.5 级别系统不太可能仅靠生成式推理直接闭合完整证明，但很适合做四类工作：文献状态核查、候选值精确计算、小图反例搜索、以及把已有渐近下界推向稳定性命题。若计算实验长期支持完全二部图，并能定位现有证明中损失常数或低阶项的来源，则有实际推进空间。

### 免责声明

以上是对 AI 辅助可解性和可推进性的审查，不是该 Erdős 问题的证明或反例。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `disproved`
- 状态信心: `high`
- 可行动性: `closed_verification_only`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_65.md](../../prompts/problem_65.md)

### 状态结论

按题面最自然的全称精确读法，第二问已被小参数可行性反例否定：n=5、kn=5 时不存在同时有 5 个顶点和 5 条边的完全二分图（其边数只能为 0、4 或 6），所以该极值不可能“由完全二分图取得”。第一问早已解决。题目的显然意图是一个需补足参数的精确极值猜想；Montgomery 2025 年同行评议综述报告该修正版在大 d 情形已有 forthcoming work 的精确证明，但本次未找到该工作的可审查论文或预印本，不能把该报告升级为已核验的完整解答。

### 当前规范陈述

字面重建（为假）：对每个有限简单图 G，若 |V(G)|=n、e(G)=kn，令 C(G)={a_1<a_2<⋯} 为 G 出现的所有不同简单环长，L(G)=∑_{ℓ∈C(G)}1/ℓ。第二问断言：在全部这类 n 顶点、kn 边图中，L 的最小值由某个完全二分图取得。上下文要求该完全二分图也具有同样的 n 和 kn，但题面没有量化可行的 n,k，也没有要求此参数下存在完全二分图。Montgomery 综述所报告的修正版是：对整数 d（至少 d 足够大，且 1≤d≤n/2），若 n 顶点图 G 满足 e(G)≥d(n-d)，则 L(G)≥L(K_{d,n-d})=1/2(H_d-1)，并且等号仅由 K_{d,n-d} 取得；综述称该结论在充分大的 d 已有 forthcoming work 证明。

```text
Literal reconstruction (false): for every finite simple graph G with |V(G)|=n and e(G)=kn, let C(G)={a_1<a_2<...} be its set of distinct simple-cycle lengths and L(G)=sum_{ell in C(G)}1/ell. The second question asserts that the minimum of L over all such n-vertex, kn-edge graphs is attained by a complete bipartite graph. Context forces that putative complete bipartite graph to have the same n and kn, but the statement neither quantifies admissible n,k nor requires that a complete bipartite graph with those parameters exist. The repaired exact target reported by Montgomery is: determine whether, for every integer d (at least some threshold, and 1<=d<=n/2), every n-vertex graph G with e(G)>=d(n-d) satisfies L(G)>=L(K_{d,n-d})=1/2(H_d-1), with equality exactly for K_{d,n-d}; the survey states this for all sufficiently large d as forthcoming work.
```

### 陈述、量词与反例审计

- 歧义严重度: `fatal`
- 简单反例检查: `counterexample_found`
- 检查说明: 取 n=5、k=1，并取 G=C5；它有 n=5 个顶点和 kn=5 条边。任何 5 顶点完全二分图同构于 K_{s,5-s}，其边数 s(5-s) 只能是 0、4 或 6，绝不为 5。因此在该参数类中完全二分图根本不是候选者，字面的“最小值由完全二分图取得”断言为假。此反例针对题面未加可行性限制的全称读法，不否定其显然意图的修正版。
- 版本变化: 1984 年 Gyárfás–Komlós–Szemerédi 证明 L(G)≫log 平均密度，解决第一问的量级下界。Liu–Montgomery（JAMS 2023）将所有环长的下界提升为渐近锋利的 (1/2-o(1))log d。Montgomery（EMS Magazine 2025）报告 Milojević–Pokrovskiy–Sudakov–Montgomery 的 forthcoming exact theorem：对充分大 d、e(G)≥d(n-d)，唯一极小图为 K_{d,n-d}。Erdős Problems 页面在 2026 年 2 月仍标为 open，并把该结果误写为 maximised；其论坛评论引用综述并指出应为 minimised。

陈述问题：

- “图有 kn 条边”没有说明 k 的取值域、整数性或可行性；通常只能理解为 kn=e(G) 为整数。
- “当 G 是完全二分图时最小”没有说明二分部大小，亦没有限制到存在满足相同 n 和边数的完全二分图的参数。
- 网页题面写 minimised，但同页备注写 forthcoming work 证明 maximised；Montgomery 的原综述明确写的是 minimised，因此网页备注中的 maximised 是可核验的方向性转录错误。
- “minimised”还缺少是对 e(G)=kn 还是 e(G)≥kn 优化的约定。Montgomery 综述报告的精确版本使用 e(G)≥d(n-d)。
- 第一问的 Vinogradov 符号应理解为存在绝对常数 c>0 和阈值 k0，使 L(G)≥c log k；它不是固定常数 1 的不等式。

需要固定的量词/约定：

- Graphs are finite, undirected, and simple; cycle lengths are lengths of simple cycles and are counted once each, not by number of cycles.
- For the literal extremal sentence, the candidate must belong to the same feasible class: a complete bipartite K_{s,n-s} must satisfy s(n-s)=kn.
- The natural exact repaired parameterization is integers n,d with 1<=d<=n/2 and e(G)>=d(n-d), not arbitrary real k.
- For K_{d,n-d}, C(K_{d,n-d})={4,6,...,2d} (with the empty set for d=1), so L(K_{d,n-d})=sum_{j=2}^d 1/(2j)=1/2(H_d-1).
- The reported exact equality assertion is only an author-reported forthcoming result for sufficiently large d; it was not independently verified from its proof in this audit.

### 文献与当前边界

已核验的主要结果：

- Gyárfás、Komlós、Szemerédi（J. Graph Theory, 1984）证明：平均密度/平均度足够大时，L(G)≥c log d（常数 c>0）。其引言将 f(a)=inf{L(G):e(G)≥a|V(G)|} 写出，并以等部完全二分图说明对数级是正确量级。
- Liu、Montgomery（JAMS, 2023）证明平均度 d 图满足 L(G)≥(1/2-o_d(1))log d；Montgomery 的 2025 综述明确称该常数渐近最优。
- 对 K_{d,n-d}（d≤n/2），可直接枚举不同环长为 4,6,...,2d，故 L(K_{d,n-d})=1/2(H_d-1)=(1/2)log d+O(1)。这解释了 1/2 常数。
- Montgomery 的 2025 同行评议综述报告：存在 d0，使 d≥d0 时，在 n 顶点且至少 d(n-d) 边的图中，L 的唯一极小者是 K_{d,n-d}。此为作者的明确数学报告，但其称工作 forthcoming；本次没有找到该四作者版本的论文、预印本或可检查证明。

最近相关工作：Hou、Jin、Yang、Yang 的 arXiv:2407.01625 于 2026-05 更新，研究 K_{s,t}-free 图的对应下界，并再次记录 Liu–Montgomery 的一般图锋利下界。它没有更新或证明 Milojević–Montgomery–Pokrovskiy–Sudakov 的精确极值声称。就该精确声称而言，本次可直接核验的最新来源仍是 Montgomery 的 2025 综述。

剩余核心：字面问题已由 n=5、e=5 的可行性反例关闭。若采纳修正版，尚需先取得并审查 forthcoming 大 d 定理的完整证明；然后才是其未覆盖的小 d、边数阈值（= 还是 ≥）、整数/取整以及所有 n 的精确极值问题。公开证据不足以断言这些残余问题确实未解，只能确认未发现可检查的完整解决文献。

已使用方法：

- Gyárfás–Komlós–Szemerédi：从高平均度抽取高最小度子图，结合环长分布和分层结构给出对数下界。
- Liu–Montgomery：子线性扩张子图、在受控区间内构造连续偶环长，并对倒数求和。
- 近期 K_{s,t}-free 推广：平衡团细分与子线性扩张；其机制支持下界而不自动给出精确极值或唯一性。

争议或不确定性：

- Erdős Problems 题面中的 maximised 与 Montgomery 原综述中的 minimised 直接冲突；原综述和其论坛逐字引文支持后者。
- 大 d 精确定理在同行评议综述中被作者报告为 forthcoming，但审计没有找到可读取的证明。因此它是强有力的未验证声称，不应当作已独立确认的已发表解答。
- “complete bipartite graph”在原题面未指定部大小，也未限制参数可行性；这既产生 n=5 的字面反例，也阻止将网页 open 标签直接当作单一精确命题的状态。

### 证据来源

- [Erdős Problems — Problem 65](https://www.erdosproblems.com/65) — Thomas F. Bloom (database); original problem attributed to Erdős and Hajnal, 2026-02-08; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 当前数据库题面、open 标签、GKS84 与 Liu–Montgomery 引用，以及“minimised/maximised”同页矛盾。页面自身警告其 open 标签并非完备文献结论。
- [On the distribution of cycle lengths in graphs](https://www.renyi.hu/~gyarfas/Cikkek/20_GyarfasKomlosSzemeredi_OnTheDistributionOfCycleLengthsInGraphs.pdf) — András Gyárfás, János Komlós, Endre Szemerédi, 1984; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 定义 L(G) 和密度极小函数，并证明对充分大平均密度的 L(G)≥c log d；同时说明平衡完全二分图给出对数级上界。
- [A solution to Erdős and Hajnal’s odd cycle problem](https://doi.org/10.1090/jams/1018) — Hong Liu, Richard Montgomery, 2023-03-31; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 该论文是 Liu–Montgomery 的同行评议 JAMS 论文；其结果及后续综述支持平均度 d 下 L(G)≥(1/2-o_d(1))log d 的渐近锋利结论。
- [Warwick repository record for A solution to Erdős and Hajnal’s odd cycle problem](https://wrap.warwick.ac.uk/id/eprint/171505/) — Hong Liu, Richard Montgomery, 2023-03-31; `author_page`, `peer_reviewed`, directness=`direct`, reliability=`high`. 独立书目记录确认论文发表在 Journal of the American Mathematical Society 36 (2023), 1191–1234，且为同行评议。
- [Cycles and expansion in graphs](https://ems.press/content/serial-article-files/52107) — Richard Montgomery, 2025; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`medium`. 明确陈述所有环长的渐近下界及方法；第 8 页报告四位作者的 forthcoming exact theorem，使用“minimised exactly”、e(G)≥d(n-d) 和 K_{d,n-d}，从而证实网页的 maximised 是错误方向。该文没有给出 forthcoming theorem 的证明。
- [Erdős Problems forum thread for Problem 65](https://www.erdosproblems.com/forum/thread/65?embed=1) — Jake Mallen, ebarschkis, StijnC; site forum, 2026-02-04; `forum`, `informal_claim`, directness=`indirect`, reliability=`medium`. 论坛评论逐字转引 Montgomery 综述的 forthcoming 精确结论，并指出第二问仅在大 d 范围被声称解决；这不是独立证明。
- [Balanced clique subdivisions and cycles lengths in K_{s,t}-free graphs](https://arxiv.org/abs/2407.01625) — Jianfeng Hou, Yindong Jin, Donglei Yang, Fan Yang, 2026-05-15; `preprint`, `preprint`, directness=`indirect`, reliability=`medium`. 近期文献重复引用 Liu–Montgomery 的 (1/2-o_d(1))log d 锋利下界，并说明其基于子线性扩张与长连续偶环区间；不证明精确极值结论。

### 完成标准

- 肯定出口: For the literal statement, the decisive negative result is already complete: give n=5, k=1, and G=C5; no 5-vertex complete bipartite graph has 5 edges, so a complete bipartite graph cannot attain the minimum in that class. For the repaired target, an affirmative resolution requires a fully checkable proof that for every stated admissible n,d, e(G)>=d(n-d) implies L(G)>=1/2(H_d-1), together with the exact equality classification.
- 否定出口: For the repaired target, a negative resolution is an explicitly specified admissible pair (n,d) and simple graph G with e(G)>=d(n-d) but L(G)<1/2(H_d-1), or equality with a non-isomorphic graph when uniqueness is claimed. If historical sources impose a different parameter convention, the audit must instead document that convention before judging the n=5 counterexample.

不构成完成：

- Proving only L(G)>=c log d, or even the asymptotic (1/2-o(1))log d bound.
- Checking finite examples without a theorem that reduces all remaining parameters to that finite list.
- Invoking the 2025 survey’s phrase 'forthcoming work' without obtaining and auditing the proof.
- Showing K_{d,n-d} has the displayed value but not proving global minimality.
- Proving an extremal result for e(G)=d(n-d) while silently substituting it for the e(G)>=d(n-d) version, or conversely.

正确性陷阱：

- Distinguish distinct cycle lengths from the number of cycles.
- Enforce feasibility: K_{s,n-s} has exactly s(n-s) edges; arbitrary kn need not have this form.
- Use d as the smaller bipartition size only under 1<=d<=n/2.
- For K_{d,n-d}, the cycle lengths are 2j for 2<=j<=d, so L=1/2(H_d-1), not H_d or a sum over all individual cycles.
- Check equality and uniqueness separately from the lower bound.
- Do not reverse 'minimised' to 'maximised'; the latter is contradicted by the author survey and is incompatible with the lower-bound context.

### 更新后的 AI 可解答性

- 等级: `not_applicable_closed_or_invalid`
- 分数: `0/100`
- 信心: `high`
- 结论: 字面命题已因参数可行性反例而关闭，故按协议 AI 解题评分为 0；这不评估修正版精确极值猜想的难度。

支持理由：

- n=5、e=5 的简单可核查反例使原题面的全称极值表述为假。
- 题面还遗漏完全二分候选的部大小和边数可行性，且备注反向写成 maximised。

主要障碍：

- 修正版的大 d 精确结论目前只找到作者在同行评议综述中的 forthcoming 报告，未取得证明。
- 修正版属于深度精确极值图论问题；渐近倒数和下界并不推出有限参数的唯一极值结构。

Proof-first 路线：

- 对于后续修复审计，首先取得并逐引理核验 forthcoming 手稿，明确 d0、n 的范围、e≥/e= 的版本与等号分类。
- 仅在明确固定 (n,d) 并给出要证的有限分类引理和穷尽停止条件后，才可用计算搜索小 d 的反例或候选极小图。

需要验证：

- 联系作者或检索正式论文/预印本，以获得 Milojević–Montgomery–Pokrovskiy–Sudakov 结论的完整证明。
- 核对原始 Erdős 文献的精确量词，决定修复应使用 f(a) 的 e≥a|V| 版本，还是固定 n、m 的版本。
- 若主张小 d 已解决，需给出覆盖全部 n 的证明而非实验。

### 审计限制与人工复核理由

- 本审计使用公开网络检索，无法逻辑上排除未公开手稿、未被索引的论文或作者私下流通版本。
- Montgomery 综述中的 forthcoming 精确定理没有在本次检索中找到可检查的证明；因此其大 d 范围只能列为强作者报告，不能列为独立核验的解决。
- 原始 Erdős–Hajnal 文献的完整历史措辞未在本次审计中直接取得；修正版的 e≥d(n-d) 取自 Montgomery 的明确表述。
- 字面反例依赖通常的有限简单图与固定参数极值语义；若原始作者另有未写出的可行性/取整约定，应以其原始文字重新界定修正版，但不能追溯性挽救网页的未限定字面陈述。

- 应取得并审查 Milojević–Montgomery–Pokrovskiy–Sudakov forthcoming 工作，以确认其是否已公开、其阈值和精确适用范围。
- 应核对原始 Erdős–Hajnal 来源，决定应维护何种修正版（固定 n,m 还是 e≥d(n-d)）以及小参数是否已有已知处理。
- 网页状态仍标 open 且备注误写 maximised；维护者需要据此更新题面，至少加入参数可行性和精确大 d 结果的状态说明。

<!-- DEEP_REVIEW:END -->
