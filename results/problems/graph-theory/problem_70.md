# Problem 70

## 基本信息

- 原始链接: https://www.erdosproblems.com/70
- LaTeX 页面: https://www.erdosproblems.com/latex/70
- 原始状态: `open`
- 奖金: `no`
- 主类别: `graph theory`
- 原始标签: `graph theory`, `ramsey theory`, `set theory`
- 形式化状态: `no`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

Let $\mathfrak{c}$ be the ordinal of the real numbers, $\beta$ be any countable ordinal, and $2\leq n<\omega$. Is it true that $\mathfrak{c}\to (\beta, n)_2^3$?

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `35/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序

### 主要障碍

- 所属标签偏证明密集：set theory

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: graph theory, ramsey theory
- 证明密集标签命中: set theory
- 有限/计算线索: 无
- 渐近/无限线索: 无
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **低到中等候选。GPT-5.5 级别模型配合文献检索、形式化证明和证明搜索，较可能对该问题做出可靠的背景整理、已知特例验证、定义形式化和局部推广尝试；但直接解决完整命题的概率不高。**
- 等级: `low_to_medium_candidate`
- 分数: `38/100`
- 信心: `medium`
- 可能路线: 可行路线是先把分割关系 \(\mathfrak c\to(\beta,n)^3_2\) 精确定义为序型/基数版本，复现备注中 \(\mathfrak c\to(\omega+n,4)^3_2\) 的证明结构，再尝试对有限 \(n\)、较小可数序数 \(\beta\) 或具有简单 Cantor normal form 的 \(\beta\) 做归纳推广；同时检索是否存在已知的反例、独立性结果或更强的 Erdős-Rado 型定理。

### 支持理由

- 题面短、结构清楚，适合模型先完成形式化定义、符号消歧和已知定理复现。
- 备注给出一个强相关的已知正结果，可作为证明模板或基准验证对象。
- 问题涉及可数序数与有限 Ramsey 目标，存在可分解为许多特例的空间，模型工具链可能在小特例、归纳引理和证明草图检查上有贡献。
- 该问题不依赖大规模数值实验，主要瓶颈是理论结构；文献检索和形式化校验能减少重复错误并发现已有分割演算工具。

### 主要障碍

- 完整命题属于无限分割演算和集合论 Ramsey 理论，证明可能需要高度专门的序数归纳、树/闭无界集技巧、精细 coloring 构造或独立性分析。
- \(\mathfrak c\) 的集合论背景可能受连续统大小、公理环境或记号约定影响，模型容易在基数、初始序数和实数序型之间混淆。
- 反例搜索几乎不能靠有限计算直接验证，因为目标是三元组 coloring 的不可数结构。
- 现有自动定理证明器对未形式化的高阶集合论分割关系支持有限，形式化成本高，且很难自动发现核心组合引理。
- 若问题真实需要新的 forcing/一致性或精细基数不变量技术，当前模型很可能只能产出不充分的证明草图。

### 需要的验证

- 核对题中 \(\mathfrak c\) 的精确定义：是连续统基数的初始序数，还是某种给定的实数良序序型。
- 系统检索并确认该分割关系在相关公理体系下是否已有部分结果、等价改写、独立性结果或已知失败案例。
- 逐行验证 Erdős-Rado 已知结果的证明，明确哪些步骤可推广到任意可数 \(\beta\) 和有限 \(n\)。
- 对模型提出的任何归纳引理进行形式化或半形式化检查，特别是极限序数步骤、颜色交换、同质集序型保持和基数使用。
- 若声称反例或独立性，需要给出完整 coloring/forcing 构造，并由集合论专家或形式化系统独立审查。

### 公开版思考摘要

这个问题的优势是题面集中、已有备注结果可作为入口，适合 AI 做严谨的文献定位、符号澄清、特例复现和局部推广。但它的核心难度在不可数分割关系和可数序数目标的高阶组合结构，计算实验作用有限，形式化工具也难以自动发明关键证明。因此更合理的预期是显著推进理解和验证局部结果，而不是高概率一次性解决完整开放问题。

### 免责声明

以上是对 GPT-5.5 级别模型可推进性的审查判断，不是该 Erdős problem 的解答，也不声称证明或反驳原命题。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `confirmed_open`
- 状态信心: `medium`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_70.md](../../prompts/problem_70.md)

### 状态结论

按通常约定将 \(\mathfrak c=2^{\aleph_0}\) 视为其初始序数后，该问题是一个明确的 ZFC 分割关系问题。当前 Erdős Problems 页面仍标为 open，且 2018 年后的定向检索未发现已验证的证明或反例。已知结果已覆盖 \(\beta\leq\omega\cdot2+1\) 的若干关键情形，但“所有可数 \(\beta\)、所有有限 \(n\)”仍未解决。

### 当前规范陈述

在 ZFC 中，并将连续统基数 \(\mathfrak c=2^{\aleph_0}\) 识别为其初始序数。对任意可数序数 \(\beta<\omega_1\)、任意整数 \(n\ge2\)，以及任意二染色 \(d:[\mathfrak c]^3\to\{0,1\}\)，是否必存在：\(0\) 色齐次集 \(A\subseteq\mathfrak c\)，其继承序型为 \(\operatorname{otp}(A)=\beta\)；或 \(1\) 色齐次集 \(B\subseteq\mathfrak c\)，满足 \(|B|=n\)？即，是否对所有此类 \(\beta,n\) 都有 \(\mathfrak c\to(\beta,n)^3_2\)？

```text
Work in ZFC and identify \(\mathfrak c=2^{\aleph_0}\) with the initial ordinal of cardinality continuum. For every countable ordinal \(\beta<\omega_1\), every integer \(n\ge2\), and every coloring \(d:[\mathfrak c]^3\to\{0,1\}\), must there exist either (i) a set \(A\subseteq\mathfrak c\) of inherited order type \(\operatorname{otp}(A)=\beta\) such that \(d\upharpoonright[A]^3\equiv0\), or (ii) a set \(B\subseteq\mathfrak c\) with \(|B|=n\) such that \(d\upharpoonright[B]^3\equiv1\)? Equivalently, is \(\mathfrak c\to(\beta,n)^3_2\) for all \(\beta<\omega_1\) and finite \(n\ge2\)?
```

### 陈述、量词与反例审计

- 歧义严重度: `material`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 未找到能否定按上述规范化字面陈述的简单染色。已核对的“真空”小参数只说明 \(n=2,3\) 不构成难点，并非反例。文献中存在对更强对称关系或不同线序的负结果；它们不能直接否定这里的不对称、以初始序数 \(\mathfrak c\) 为资源的命题。
- 版本变化: Erdős Problems 的公开历史页只显示 2025-10-20 与当前版本同文，未记录实质性改写。文献发展则给出实质性“残余目标”收缩：1956 年实序结果覆盖 \(\omega+m\) 与蓝色 4；1991 年得到 \(\omega_1\to(\omega\cdot2+1,4)^3\)；2018 年 Jones 将该结论的有限目标推广为任意有限 \(n\)。这些是已证定的特例扩张，不是对原问题的替代定义。

陈述问题：

- 原文“\(\mathfrak c\) 是实数的 ordinal”并非标准表述：\(\mathfrak c\) 通常是连续统的基数，而箭头关系右侧含序数目标时，左侧须明确为该基数的初始序数。
- “任意可数 \(\beta\)”与“\(2\le n<\omega\)”应置于全称量词下；箭头关系还须明确颜色 0 对应 \(\beta\)、颜色 1 对应 \(n\)。
- 当 \(n=2\) 时，\([B]^3=\varnothing\)，故第二个齐次条件真空成立；当 \(n=3\) 时该情形也直接平凡。真正非平凡的范围从 \(n=4\) 开始。
- “实数的序型”若意指通常实数线性序 \(\mathbb R\)，则不是与初始序数 \(\mathfrak c\) 相同的对象；Erdős–Rado 的 real-order 定理正使这一历史意图需要人工核对。这里的规范命题遵从给出的符号 \(\mathfrak c\) 的标准基数解释。

需要固定的量词/约定：

- The assertion is a ZFC scheme universally quantified over every countable ordinal \(\beta<\omega_1\), every finite integer \(n\ge2\), and every two-coloring of unordered triples of the initial ordinal \(\mathfrak c\).
- In \(\kappa\to(\beta,n)^3_2\), the first alternative is color 0 and requires order type exactly \(\beta\); the second is color 1 and requires a set of cardinality \(n\).
- For finite \(n\), cardinality and order type \(n\) coincide; the order on a subset of \(\mathfrak c\) is inherited from the ordinal order.
- The cases \(n=2\) and \(n=3\) are vacuous/trivial for triple colorings, so any substantive proof must address \(n\ge4\).

### 文献与当前边界

已核验的主要结果：

- Erdős–Rado（1956）：对 real orders 的三元组不对称分割给出 \(X\to(\alpha,4)^3\)（\(\alpha<\omega+\omega\)）；这解释了数据库所引的 \(\omega+m\) 级别结论，但其资源是特定线序类别，不能不经说明与初始序数 \(\mathfrak c\) 混同。
- Milner–Prikry（1991，同行评议）：证明 \(\omega_1\to(\omega\cdot2+1,4)^3\) 于 ZFC。由于 \(\omega_1\leq\mathfrak c\)，限制任何 \([\mathfrak c]^3\) 染色到 \(\omega_1\) 即得 Problem 70 对 \(\beta\leq\omega\cdot2+1,n=4\) 的正解。
- Jones（2007，同行评议）：证明 \(\omega_1\to(\omega+m,n)^3\) 对所有有限 \(m,n\) 成立，并建立偏序推广；这把有限第二目标推进到任意 \(n\)，但当时 0 色序型只到 \(\omega+m\)。
- Jones（2018，同行评议）：证明 \(\omega_1\to(\omega\cdot2+1,n)^3\) 对每个有限 \(n\)。由左侧单调性，这也为规范化 Problem 70 覆盖所有 \(\beta\leq\omega\cdot2+1\) 和所有有限 \(n\)。
- 可直接推出而非单独引用的事实：若 \(\kappa\to(\beta,n)^3_2\) 且 \(\lambda\geq\kappa\) 为序数，则 \(\lambda\to(\beta,n)^3_2\)，因为可将染色限制到 \(\kappa\)。因此上述 \(\omega_1\) 结果自动给出 \(\mathfrak c\) 的对应特例。

最近相关工作：直接推进此三元组问题的最新已核实论文是 Jones（2018）。2023–2026 的精确题名、箭头关系、arXiv 与近期问题清单检索未发现更强的同行评议定理、预印本证明或反例；2025 年的 Komjáth MathOverflow 回答仍将全体可数序数版本表述为猜想。

剩余核心：字面目标要求对每个可数 \(\beta\) 与有限 \(n\) 都成立。已验证文献覆盖至 \(\beta=\omega\cdot2+1\)。因此任何未覆盖的 \(\beta\)（例如 \(\omega\cdot2+2\)）与 \(n\ge4\) 是实际剩余范围；但本审计未找到一篇 2018 年后专门证明“\(\omega\cdot2+2,4\) 是最小公开未解实例”的权威论文，故该“最小性”须由后续研究者再核对。

已使用方法：

- Erdős–Rado 的线序/分割演算方法及对 real orders 的结构性分析。
- Milner–Prikry：先在 ccc 强迫模型中结合 \(MA_{\omega_1}\) 获得正关系，再利用绝对性消去附加假设。
- Jones：将结果组织为非特殊线序或偏序上的分割关系，并使用模型论式/偏序结构方法。
- 递降到 \(\omega_1\) 后再以左侧单调性抬升到 \(\mathfrak c\)；这是一条透明归约，而非新定理。

争议或不确定性：

- “\(\mathfrak c\) 是实数的 ordinal”可能意在连续统的初始序数，也可能误把实数线序与其基数混称；两者不等价，且影响哪些历史定理可直接援引。
- Erdős Problems 的 open 标签是有价值的最新数据库记录，但页面本身明示其并非完备文献证明。
- 2018 论文摘要足以核验其主定理；本次未能取得全文，因此不应把未检查的内部引理、最小开放实例或方法细节当作已独立审计。

### 证据来源

- [Erdős Problems — Problem 70](https://www.erdosproblems.com/70) — T. F. Bloom (database editor), 2026-01-23; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 当前条目将该命题标为 open；列出原始来源 Er87、Va99 §7.83，说明不存在论坛中的解答或部分解答声称，并记录 Erdős–Rado 的 \(\mathfrak c\to(\omega+n,4)^3_2\) 结果。
- [A Partition Calculus in Set Theory](https://www.renyi.hu/~p_erdos/1956-02.pdf) — Paul Erdős; Richard Rado, 1956-09; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 分割演算及箭头记号的原始论文；后续 Jones 论文明确归因于此文的 real-order 三元组定理。
- [A partition relation for triples using a model of Todorčević](https://doi.org/10.1016/0012-365X(91)90336-Z) — E. C. Milner; Karel Prikry, 1991-12-03; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 证明 \(\omega_1\to(\omega\cdot2+1,4)^3\)；论文摘要说明先在满足 \(MA_{\omega_1}+2^\omega=\omega_2\) 的模型中证明，再由绝对性推出 ZFC 定理。
- [More on partitioning triples of countable ordinals](https://doi.org/10.1090/S0002-9939-06-08538-8) — Albin L. Jones, 2007; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 证明 \(\omega_1\to(\omega+m,n)^3\)（所有有限 \(m,n\)），并将若干结论推广到满足相应非特殊性条件的偏序；其引言准确综述 Erdős–Rado 与 Milner–Prikry 的先前结果。
- [Even more on partitioning triples of countable ordinals](https://doi.org/10.1090/proc/13503) — Albin L. Jones, 2018; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 摘要陈述证明 \(\omega_1\to(\omega+\omega+1,n)^3\) 对每个有限 \(n\) 成立；因此也给出规范化 Problem 70 在 \(\beta\leq\omega\cdot2+1\) 的相应已证定特例。
- [A short proof of a partition relation for triples](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v7i1r24) — Albin L. Jones, 2000-03-11; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 给出 Erdős–Rado real-order 定理的短证明，并明确指出其适用对象是没有嵌入 \(\omega_1\) 或 \(\omega_1^*\) 的不可数线序，故有助于识别“实数的 ordinal”措辞的潜在混淆。
- [Are infinite Ramsey numbers completely known?](https://mathoverflow.net/questions/448855/are-infinite-ramsey-numbers-completely-known/488725) — Péter Komjáth (answer), 2025-08-05; `forum`, `informal_claim`, directness=`indirect`, reliability=`medium`. 近期专家性二手综述仍将 \(\omega_1\to(\alpha,n)^3\)（所有可数 \(\alpha\)、有限 \(n\)）称为猜想，并列出 Milner–Prikry 与 Jones 的特例；它支持“未发现近期解答”的判断，但不是证明。
- [The Erdős–Hajnal Problem List](https://www.cambridge.org/core/journals/bulletin-of-symbolic-logic/article/abs/erdoshajnal-problem-list/9FBE6099BE9441516445D0B95F4B1208) — Péter Komjáth, 2025-09; `secondary_index`, `peer_reviewed`, directness=`indirect`, reliability=`medium`. 2025 年同行评议的问题清单仍将 Jones 2018、Milner–Prikry 1991 和 Erdős–Rado 1956 列入相关分割演算文献；其可访问部分未给出本题的解决声明。

### 完成标准

- 肯定出口: A complete affirmative resolution is a ZFC proof that for every countable ordinal beta, every finite n >= 2, and every d:[c]^3 -> 2, one of the two stated homogeneous alternatives exists. The proof must explicitly use c as the initial ordinal of continuum and must cover beta beyond omega*2+1 and n >= 4.
- 否定出口: A complete negative resolution is a ZFC construction of a specific countable beta and finite n >= 4 together with a coloring d:[c]^3 -> 2 having neither a color-0 homogeneous subset of order type beta nor a color-1 homogeneous n-set. If the intended objective is ZFC decidability rather than truth in the ambient universe, an independence resolution requires rigorously verified models establishing opposite outcomes for the canonical statement.

不构成完成：

- Proving only the already known cases beta <= omega*2+1, or only n <= 3.
- Proving the relation on the real line as a linear order without showing that it is the canonical initial-ordinal statement about c.
- Producing a coloring of a different domain, a coloring of pairs rather than triples, a symmetric Ramsey counterexample, or a counterexample for a stronger target.
- Obtaining a result only under MA, CH, PFA, or another hypothesis without either eliminating it or explicitly establishing an independence result.
- Finite searches, heuristic arguments, or an unverified claim that a known theorem 'obviously' transfers from a real order to c.

正确性陷阱：

- Distinguish cardinality, initial ordinal, and the usual order on R; use the exact domain specified by the canonical target.
- For the beta alternative, verify inherited order type exactly beta, not merely cardinality aleph_0 or an arbitrary countably infinite subset.
- Check the asymmetric color assignment and remember that the n-set alternative is vacuous for n < 3 and trivial for n = 3.
- Do not infer a statement at c from a theorem about an arbitrary real order, or conversely, without a valid embedding/restriction argument.
- If invoking forcing plus absoluteness, specify the formula, parameters, and absoluteness theorem sufficiently to transfer the desired ZFC statement.

### 更新后的 AI 可解答性

- 等级: `low_candidate`
- 分数: `8/100`
- 信心: `high`
- 结论: 这是定义良好但极难的开放分割演算问题；对当前 AI 而言，获得完整新证明或反例的概率很低。可行贡献更可能是严谨的文献—陈述核查、已知证明的形式化分解，以及对首个未覆盖小序型的受限引理探索。

支持理由：

- 目标具有清晰的量词、可审计的二值结果和明确的反例证书格式。
- 已有从 \(\omega+m\) 到 \(\omega\cdot2+1\) 的连续理论进展，给出了可复用的结构与基准。
- 所有有限 \(n\) 的已知边界使任何新推进可精确地表述为超越 \(\omega\cdot2+1\) 的引理。

主要障碍：

- 该问题在 Erdős–Rado 时代即出现，核心广义猜想在近期仍被视为未解。
- 关键技术涉及不可数序数、强迫、绝对性和非特殊偏序，不能由有限枚举或局部模式归纳可靠替代。
- 原始措辞中的 \(\mathfrak c\)/实数线序歧义会诱发把不等价定理错误移植到目标上。

Proof-first 路线：

- 先完成一个精确的“资源归约图”：逐条证明哪些 \(\omega_1\) 结论可由单调性移到 \(\mathfrak c\)，并标出不能从 real-order 结论推出的边。
- 把 \(\beta=\omega\cdot2+2,n=4\) 作为诊断性未覆盖实例，先寻找可验证的局部扩张引理或障碍，而非宣称其必为全局最小开放实例。
- 审计 Milner–Prikry 的强迫—绝对性转移与 Jones 的偏序推广，定位“\(+1\)”到“\(+2\)”的具体失效步骤；只有形成精确引理后再尝试新方法。

需要验证：

- 人工核对 Er87 与 Vajda（1999）§7.83 的原始措辞，判定其究竟指初始序数 \(\mathfrak c\) 还是实数线序。
- 获取并逐页审阅 Jones（2018）全文，以核实其方法、边界陈述以及是否讨论 \(\omega\cdot2+2\)。
- 若出现新证明，需由具备强迫/绝对性专长的审稿人独立核验每个模型论和序型步骤。

### 审计限制与人工复核理由

- 本审计只使用了题目给定 JSON 与公开网络资料；未读取任何周边仓库条目。
- Erdős Problems 的 open 标签和未发现近期论文并非“不存在解答”的逻辑证明，因此状态置信度为 medium。
- Jones（2018）全文未能在本次环境中取得；主定理由 DOI/摘要与 2025 同行评议书目交叉核验，但其内部技术细节及最小未解实例仍需人工阅读原文。
- 原始 Er87 与 Vajda（1999）§7.83 未获全文核查，故历史意图中 \(\mathfrak c\) 是否被误作实数线序仍需人工裁定。

- 需要由集合论专家核对原始来源对 \(\mathfrak c\) 的语义，避免将 real-order 版本与初始序数版本混同。
- 需要获取并审阅 Jones（2018）全文，以核实所有边界、证明方法和 2018 年后未覆盖范围。
- 任何声称解决该题的论证均应接受具备强迫、绝对性与序数分割关系专长的独立证明审计。

<!-- DEEP_REVIEW:END -->
