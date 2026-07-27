# Problem 128

## 基本信息

- 原始链接: https://www.erdosproblems.com/128
- LaTeX 页面: https://www.erdosproblems.com/latex/128
- 原始状态: `falsifiable`
- 奖金: `$250`
- 主类别: `graph theory`
- 原始标签: `graph theory`
- 形式化状态: `yes`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

Let $G$ be a graph with $n$ vertices such that every induced subgraph on $\geq \lfloor n/2\rfloor$ vertices has more than $n^2/50$ edges. Must $G$ contain a triangle?

## AI 完成可能性判断

- 结论: **AI 辅助完成有现实候选路线，但需要外部计算或严格验证**
- 等级: `medium_candidate`
- 分数: `63/100`
- 建议路线: 优先做反例搜索和小规模枚举；若没有反例，不能据此断言问题为真。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 题面或备注出现有限对象/计算线索
- 已有形式化陈述，可降低语义误读风险

### 主要障碍

- 原记录含奖金 $250，说明该题被长期视为高价值难题；这不是否定依据，但提高验证门槛。

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: graph theory
- 证明密集标签命中: 无
- 有限/计算线索: graph
- 渐近/无限线索: 无
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5 + 计算搜索/SDP-flag algebra/形式化证明/文献检索工具`
- 结论: **中等偏低候选。GPT-5.5 级别模型不太可能独立给出完整新证明，但有现实机会在该问题上做出可验证的显著推进：复现并改进已知常数、系统搜索反例结构、把形式化版本与计算证书连接起来，或缩小剩余极值构型。**
- 等级: `low_to_medium_candidate`
- 分数: `46/100`
- 信心: `medium`
- 可能路线: 最可行路线是把问题重写为三角形自由图的局部边密度极值问题，结合 flag algebra/半定规划证书、有限 blow-up 与稳定性分析、以及形式化证明检查。模型可负责提出结构化归约、生成 SDP/搜索代码、解释证书并把数值证据转成可审计证明草案；核心难点在于把接近最优常数 1/50 的数值或结构证据提升为严格定理。

### 支持理由

- 问题属于有限图极值问题，目标命题明确且可反驳，适合计算反例搜索、SDP 松弛、证书验证和形式化检查。
- 已有进展给出多个接近方向：常数 16、25、27/1024，以及在总边数额外条件下的结果，说明该问题有可分解的技术路径而不是完全无结构。
- 最佳可能常数由 C5 或 Petersen 图的 blow-up 见证，这给 AI 搜索稳定性结构、极值候选和边界情形提供了明确锚点。
- formalized=yes 提高了验证可行性：即使模型不能发现完整证明，也可能帮助把局部引理、有限检查或计算证书转为机器可审计对象。

### 主要障碍

- 目标常数 1/50 是猜想中的最佳阈值，现有摘录中的最好一般结果仍停在更强阈值 27/1024，距离最终常数仍有实质差距。
- 极值构型涉及三角形自由图的全局结构与大诱导子图局部密度约束，单纯随机搜索或局部改进很可能不足以处理所有 n 和所有近极值图。
- 若使用 flag algebra/SDP，数值证书到严格有理证书再到人类可读或形式化证明之间存在较高工程和数学门槛。
- 问题可能需要新的稳定性定理或结构分类，而这类创意性步骤仍是当前模型最不稳定的部分。

### 需要的验证

- 复现摘录中已知常数结果的关键计算或证明骨架，确认模型没有误解归一化常数与边数计数方式。
- 对三角形自由图进行系统反例搜索，包括 blow-up、Petersen/C5 附近扰动、有限 n 的 SAT/ILP/CP-SAT 搜索，并保存可复验日志。
- 若产生 SDP/flag algebra 证据，需要导出有理化证书并由独立程序验证正半定性、约束编码和目标常数。
- 若产生证明草案，需要把关键归约和不等式分解成可形式化检查的引理，尤其检查 floor(n/2)、严格不等号、有限小 n 情况。
- 需要与给定问题 JSON 中列出的已有结果逐项对齐，确保所谓推进不是已知定理的弱化或重新表述。

### 公开版思考摘要

这是一个清晰、可形式化、可计算辅助的三角形自由极值图问题，因此 GPT-5.5 配合工具有较好机会做严肃的验证和局部推进；但它逼近最佳常数，且已有强专家结果仍未达到目标，说明完整解决大概率需要新的结构性数学想法。综合看，适合作为 AI 辅助研究候选，但不应预期一次性自动解决。

### 免责声明

以上是对 AI 可推进性的审查，不是该 Erdős 问题的证明、反例或最终数学结论。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `likely_open`
- 状态信心: `medium`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_128.md](../../prompts/problem_128.md)

### 状态结论

截至 2026-07-27，未找到该命题的经核验解决或反例。Razborov 的 2022 年同行评审论文仍明确称该猜想“widely open”，并给出一般情形的 27/1024 上界及若干完整子类结果。对精确题句、题号、别名 half-graph conjecture、作者和 2023–2026 年文献的定向检索未发现后续直接解决；但“未检到”不能逻辑证明无人解决，故定为 likely_open（中等置信度），而非 confirmed_open。

### 当前规范陈述

对每个有限简单图 G=(V,E)，令 n=|V|。若每个满足 |S|≥⌊n/2⌋ 的顶点集 S⊆V 所诱导的子图 G[S] 都有严格多于 n²/50 条边，则 G 含有一个三角形（K₃）。等价地，每个 n 顶点的有限无三角形简单图 G 都存在恰有 ⌊n/2⌋ 个顶点的集合 S，使 e(G[S])≤n²/50。由于诱导边数随 S 扩大不减，只需检验大小恰为 ⌊n/2⌋ 的集合。

```text
For every finite simple graph G=(V,E), with n=|V|, if every vertex set S⊆V satisfying |S|≥⌊n/2⌋ spans strictly more than n²/50 edges in the induced graph G[S], then G contains a triangle (a copy of K₃). Equivalently, every finite triangle-free simple graph G on n vertices has a set S of exactly ⌊n/2⌋ vertices such that e(G[S])≤n²/50. It is enough to quantify over sets of exactly ⌊n/2⌋ vertices, since induced edge counts are monotone under enlarging S.
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 未发现能反驳字面命题的简单构造。C5 或 Petersen 图的适当 blow-up 是常数 1/50 的尖锐性见证：它们对应于允许“≤ n²/50”的无三角形例子，而不是满足所有半集都“> n²/50”的反例。因此它们不推翻严格不等式版本。小 n 时前提通常不可满足或结论平凡，没有产生反例。
- 版本变化: Erdős Problems 的历史页显示 2025-10-20 附近存在一次文字编辑的差分，但其渲染的删改标记不足以可靠重建全部旧措辞。当前页与输入相同，均为 induced-subgraph、⌊n/2⌋ 和 n²/50 的版本；未发现有文献将原问题替换为不同的已解决命题。Razborov 2022 把它称为 half-graph conjecture，并以 fractional-half 语言研究一个可用于原题的加强性表述，而非宣布原题被改写或解决。

陈述问题：

- 当前题句在采用组合学中的默认约定“graph=有限简单无向图”时是可形式化的；若允许重边、环或无限图，边数和结论不再是同一问题，因此规范表述须写明有限简单图。
- “每个大小至少为 ⌊n/2⌋ 的诱导子图”可无歧义地解释为对每个顶点集 S 计 e(G[S])，而非任意删边后的普通子图。
- 奇数 n 是实质性的边界条件：原题是离散的 ⌊n/2⌋ 顶点版本。Razborov 2022 使用允许一个顶点权重为 1/2 的 fractional half（β(G)）；其 β(G)≤1/50 结论足以推出原离散目标，但不能在未说明该单向推出时把两种定义直接等同。
- 阈值采用严格的假设 “> n²/50” 和弱的反面结论 “≤ n²/50”。等号例子只说明常数的尖锐性，不能反驳字面命题。

需要固定的量词/约定：

- Quantify over all finite simple graphs G and all vertex subsets S⊆V(G).
- Set n:=|V(G)| before evaluating the threshold n²/50; the threshold is real-valued, while e(G[S]) is integral.
- A triangle is a K₃ subgraph; therefore the contrapositive restricts G to triangle-free graphs.
- The asserted equivalent triangle-free form requires an S with |S|=⌊n/2⌋ and e(G[S])≤n²/50.
- For odd n, distinguish this discrete half from Razborov's fractional half. A proved fractional bound β(G)≤1/50 implies the discrete target by taking the integral part of a minimizing almost-0–1 half, but the converse is not automatic.

### 文献与当前边界

已核验的主要结果：

- Erdős–Faudree–Rousseau–Schelp（Discrete Mathematics 127, 1994, 153–161）证明更一般的局部密度判据：若每个至少 αn 顶点的集合诱导边数严格大于 α³n²/2，则图含三角形；取 α=1/2 给出 n²/16 阈值。这是目标 n²/50 的较弱常数。
- Krivelevich（JCTB 63, 1995, 245–260）给出早期边分布结果；Erdős Problems 条目概括为：把半数替换为 3n/5、把常数 50 替换为 25 时成立。
- Keevash–Sudakov（JCTB 96(4), 2006）证明：若无三角形图的总边数至多 n²/12 或至少 n²/5，则存在所需 sparse half。
- Norin–Yepremyan（JCTB 115, 2015；预印本摘要可检）将高密度一侧推进到平均度至少 (2/5−ε)n，并证明最小度至少 5n/14 及接近 Petersen 图的情形。
- Razborov（Sbornik: Mathematics 213(1), 2022）证明所有无三角形图的 fractional-half 界 β(G)≤27/1024，且证明目标常数 1/50 对 girth≥5、独立数至少 2n/5、strongly regular、无 induced matching 2K2 等类别成立。27/1024≈0.026367，大于目标 0.02。

最近相关工作：已定位的最新直接进展是 Razborov 的 2022 同行评审论文（预印本 2021）。该论文明确仍称猜想广泛开放。对 exact title、half-graph conjecture 和 2023–2026 的定向检索未出现后续直接论文或可审查的解决声明；这只能提供“未发现”的搜索证据。

剩余核心：证明对任意有限无三角形简单图 G，均有一个恰含 ⌊|V(G)|/2⌋ 顶点的诱导子图，其边数至多 |V(G)|²/50；或者给出一个有限无三角形图，使每个这样的半集边数严格大于该阈值。现有一般界与目标之间仍有 27/1024−1/50=161/25600 的常数差距。

已使用方法：

- 随机半集平均与局部边分布/邻域分割。
- 按总边数、最大/最小/平均度及独立数做结构性情形划分。
- 四环密度 C4 与 sparse-half 参数 β(G) 的不等式。
- flag algebra/graph-limit 不等式；Razborov 的部分证书使用有理半正定矩阵，且部分证明依赖 Maple 辅助计算。
- 对 girth、induced matching、strongly regular 或接近 Petersen 图等极端结构类别的稳定性和分类论证。

争议或不确定性：

- 未找到实质性论坛线程或有证明细节的“已解决/有反例”声明。
- Razborov 的 fractional-half 记号在奇数阶时不是原题离散表述的逐字同义词；其已证明的强方向可支持原题，但任何新论证都须单独处理该转换。
- 当前 Erdős Problems 页面标为 falsifiable，而不是明确的 solved/open 标签；它与原始论文和没有相反证据的检索相容，但不能单独把状态提升为 confirmed_open。

### 证据来源

- [128 | Erdős Problems](https://www.erdosproblems.com/latex/128) — Erdős Problems database, date unknown; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 给出当前离散题句及 EFRS、Krivelevich、Keevash–Sudakov、Norin–Yepremyan、Razborov 的既有结果索引；数据库状态本身未被当作解决状态的决定性证据。
- [History of Erdős Problem 128](https://www.erdosproblems.com/history/128) — Erdős Problems database, 2025-10-20; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 显示该条目曾有文字差分；当前版本仍是所审计的 induced-subgraph 命题。
- [More about sparse halves in triangle-free graphs](https://arxiv.org/abs/2104.09406) — Alexander A. Razborov, 2021-04-19; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 摘要明确陈述 half-graph conjecture、一般界 β(G)≤27/1024，以及 girth≥5、独立数≥2n/5 和 strongly regular 三类的完整结果。
- [More about sparse halves in triangle-free graphs](https://www.mathnet.ru/links/0062fe3a56efc9141ab3ee6dfdb710e6/sm9615_eng.pdf) — Alexander A. Razborov, 2022; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. Sbornik: Mathematics 213(1), 109–128，DOI 10.1070/SM9615。正文称猜想仍广泛开放，证明一般界 27/1024，并阐明 flag algebra、C4 计数、结构性子类和计算证书的作用。
- [Sparse halves in triangle-free graphs](https://www.sciencedirect.com/science/article/pii/S0095895605001644) — Peter Keevash and Benny Sudakov, 2006-07; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. JCTB 96(4), 614–620，DOI 10.1016/j.jctb.2005.11.003。摘要证明目标在 |E(G)|≤n²/12 或 |E(G)|≥n²/5 时成立。
- [Michael Krivelevich's Papers](https://www.math.tau.ac.il/~krivelev/papers.html) — Michael Krivelevich, 1995; `author_page`, `unknown`, directness=`indirect`, reliability=`high`. 核验 Krivelevich 的论文题名、期刊卷页：JCTB 63(2), 245–260 (1995)；该论文是早期关于无三角形图边分布的主要来源。
- [Sparse halves in dense triangle-free graphs](https://arxiv.org/abs/1311.5818) — Sergey Norin and Liana Yepremyan, 2013-11-22; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 摘要给出最小度至少 5n/14、平均度至少 (2/5−ε)n，以及 Petersen 图编辑距离邻域内的完整结果；该工作后以同名论文发表于 JCTB 115 (2015), 1–25。
- [FormalConjectures/ErdosProblems/128.lean](https://raw.githubusercontent.com/google-deepmind/formal-conjectures/main/FormalConjectures/ErdosProblems/128.lean) — Formal Conjectures contributors, 2025-07-20; `formalization`, `formalized_artifact`, directness=`direct`, reliability=`high`. Lean 文件形式化了一个等价的量词框架：2|S|+1≥n 时 50e(G[S])>n² 推出 ¬CliqueFree 3。该定理体仍含 sorry，故它是已合并的陈述形式化，不是机器核验的数学证明。
- [Erdős Problem 128, Pull Request #432](https://github.com/google-deepmind/formal-conjectures/pull/432) — rdivyanshu; Google DeepMind Formal Conjectures contributors, 2025-07-20; `formalization`, `formalized_artifact`, directness=`direct`, reliability=`high`. PR 已合并且检查通过，支持“形式化条目已加入”；不支持“命题已证明”。

### 完成标准

- 肯定出口: A complete affirmative resolution is a proof that for every finite simple triangle-free graph G on n vertices there is S⊆V(G) with |S|=⌊n/2⌋ and e(G[S])≤n²/50, including all parity and finite-size cases. Equivalently, prove the stated local-density implication for every finite simple graph.
- 否定出口: A complete negative resolution is one explicit finite simple triangle-free graph G on n vertices, together with an exact, independently checkable certificate that every S⊆V(G) of size ⌊n/2⌋ satisfies e(G[S])>n²/50. Equality at n²/50 is not a counterexample.

不构成完成：

- Proving only e(G[S])≤(1/50+ε)n², ≤27n²/1024, or any other weaker constant.
- Proving the claim only asymptotically without dispatching the finite remainder, or only for a density/girth/degree/regularity subclass.
- A numerical search that finds no counterexample without a theorem or exhaustive certificate with a verified stopping condition.
- A fractional-half claim for odd n without proving the required implication to a discrete subset of size ⌊n/2⌋.
- Showing C5/Petersen blow-ups attain or approach equality: this establishes sharpness, not falsity of the strict hypothesis.

正确性陷阱：

- Reverse neither the strict/weak inequality nor the contrapositive: the target is ≤n²/50 for some half, while a counterexample needs >n²/50 for every half.
- Use induced edges e(G[S]), not a freely chosen subgraph or crossing-edge count.
- Keep n as |V(G)| throughout; do not normalize a half by |S|² and silently change constants.
- Handle ⌊n/2⌋, especially odd n, explicitly; Razborov's weighted β convention requires a justified reduction.
- Verify any flag-algebra or SDP certificate exactly (rational matrices, PSD proof, coefficient identity, and finite-to-limit transfer), not only floating-point numerics.
- A purported extremal construction must be triangle-free and must certify every relevant subset, not merely sampled subsets.

### 更新后的 AI 可解答性

- 等级: `low_candidate`
- 分数: `12/100`
- 信心: `medium`
- 结论: 这是定义清楚、可进行证明优先研究的开放候选，但长期未解且一般常数仍有固定缺口；对当前 AI 而言属于低概率研究目标，而非适合依赖枚举快速攻克的问题。

支持理由：

- 目标、等价反面及成功/失败证书均可精确定义；已有完整形式化陈述可辅助审计。
- 文献已将可能困难区间收缩到若干结构/密度交界处，并给出可复核的 C4—β 不等式与 flag-algebra 框架。
- 存在多个不相容但可独立探索的证明方向，适合有限并行的证明优先调查。

主要障碍：

- 该猜想至少自 1990 年代持续未解，目标 1/50 与最强一般界 27/1024 相差固定常数，而非简单的有限规模误差。
- 已知极端候选（C5、Petersen）落在若干已解决子类中，说明剩余困难不是直接识别这两个图。
- 计算型 flag-algebra 证书的发现和验证不同：数值 SDP 不能替代精确可审查证明，且现有方法在 Clebsch 图处遇到自然障碍。
- 奇数 n 的离散/加权 half 转换、严格阈值和 blow-up 极限都容易造成看似微小但致命的错误。

Proof-first 路线：

- 先寻求一个可精确陈述的结构归约：假设最小反例，利用已知 girth、独立数、度数和 2K2 子类结果，推出其必须满足的相互兼容约束；只有归约闭合才算进展。
- 尝试证明能闭合常数缺口的 C4/局部密度不等式，随后与已知 β(G) 上界机械组合；每个候选不等式须先在 C5、Petersen、Clebsch 及其 blow-up 上做符号检验。
- 探索稳定性命题：若所有离散半集都稠密，则 G 必须接近某个有限模板；再直接证明该模板邻域含 sparse half 或产生三角形。
- 可选且至多一个计算任务：仅在先给出目标 flag-algebra/SDP 引理、有限 flag 集、精确有理化和 PSD 验证方案、以及“找到证书或排除该引理”停止条件后使用计算。

需要验证：

- 在投入长期研究前，人工复查 Razborov 2022 的 β 定义与原离散奇数阶命题间的单向推导，并核对每个引用子类的精确假设。
- 继续用 MathSciNet/zbMATH、作者最新论文页和 arXiv API 复查 2023-07 至 2026-07 的直接后续工作；本审计未取得这些付费/结构化索引的完整穷尽结果。
- 若依赖 FormalConjectures，确认目标版本与当前数据库的 floor/induced/strict conventions 一致，并注意文件仍含 sorry。

### 审计限制与人工复核理由

- 本审计遵守只使用题目 JSON 作为仓库输入；没有检查任何相邻仓库条目。
- Erdős Problems 页面本体和若干 PDF 的网页抓取曾超时或返回内部错误，故对其内容以检索到的 LaTeX 页面、历史页和 Razborov 的主论文交叉核验。
- 对 2023–2026 的检索覆盖精确题句、别名、作者及 arXiv/一般网页索引，但不是 MathSciNet、zbMATH、Google Scholar 全库或所有付费期刊的可证明穷尽；因此状态只能是 likely_open。
- 未找到该问题的实质论坛讨论，不能据此断言不存在非正式解答。
- Lean 条目仅验证为陈述形式化：当前源文件含 sorry，不能作为该猜想已被机器证明的证据。

- 应由熟悉该领域的研究者复查 Razborov 的 fractional-half 与原离散奇数阶命题间的精确转换，以及所有子类结果的原始假设。
- 在启动高成本研究前，建议使用 MathSciNet/zbMATH/Google Scholar 和相关作者最新论文页做一次人工的 2023-07 至 2026-07 增量文献核查。
- 数据库历史页的删改标记未能完全重建旧措辞；虽不影响当前规范命题，若需历史精确性应人工核对版本记录。

<!-- DEEP_REVIEW:END -->
