# Problem 39

## 基本信息

- 原始链接: https://www.erdosproblems.com/39
- LaTeX 页面: https://www.erdosproblems.com/latex/39
- 原始状态: `open`
- 奖金: `$500`
- 主类别: `number theory`
- 原始标签: `number theory`, `sidon sets`, `additive combinatorics`
- 形式化状态: `yes`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

Is there an infinite Sidon set $A\subset \mathbb{N}$ such that\[\lvert A\cap \{1\ldots,N\}\rvert \gg_\epsilon N^{1/2-\epsilon}\]for all $\epsilon>0$?

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `14/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- 题面或备注出现有限对象/计算线索
- 已有形式化陈述，可降低语义误读风险

### 主要障碍

- 所属标签偏证明密集：additive combinatorics, number theory, sidon sets
- 题面含渐近/无限对象线索：\gg, \ll, for all large, liminf, o(
- 原记录含奖金 $500，说明该题被长期视为高价值难题；这不是否定依据，但提高验证门槛。

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: additive combinatorics, number theory, sidon sets
- 有限/计算线索: finite
- 渐近/无限线索: \gg, \ll, for all large, liminf, o(
- 构造/存在性线索: construct, is there

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **低到中等候选。GPT-5.5 级别模型配合计算、形式化证明和文献检索，较可能系统化验证已知构造、发现局部改进线索或排除若干朴素方案，但直接构造满足 N^{1/2-o(1)} 计数下界的无限 Sidon 集的概率偏低。**
- 等级: `low_to_medium_candidate`
- 分数: `38/100`
- 信心: `medium`
- 可能路线: 最现实路线不是直接猜出完整构造，而是围绕现有三类信息做可验证推进：一是复现并形式化 Ruzsa 的 N^{sqrt(2)-1+o(1)} 构造，寻找参数损失来源；二是分析 Erdős-Rényi 的有界表示函数构造能否通过稀疏化、分层拼接或冲突消除转化为真正 Sidon 集；三是用计算搜索有限 Sidon 块和拼接规则，生成可证明的递归构造候选，再由证明助手验证跨块和块内唯一和条件。

### 支持理由

- 问题已有形式化状态，说明基本定义、目标陈述和部分相关理论可能适合机器检查与证明工程介入。
- 目标与有限 Sidon 集极值规模 N^{1/2} 同阶但允许 N^{-epsilon} 损失，理论上给了构造和分层参数优化的空间。
- 备注中给出清晰的已知进展链：贪心 N^{1/3}、AKS 的对数改进、Ruzsa 的 N^{sqrt(2)-1+o(1)}，模型可以围绕这些构造做局部审计和参数搜索。
- Erdős-Rényi 已有接近目标密度但只满足有界表示次数的构造，这提供了一个明确的候选桥梁：从 B_2[g] 型对象变为严格 Sidon。
- 计算工具可有效搜索有限块、冲突图、删点策略和递归拼接参数，帮助发现或否定一些自然转化方案。

### 主要障碍

- 严格 Sidon 条件要求所有两数和唯一，远强于有界表示函数；从 bounded multiplicity 到 multiplicity 1 的转化通常会造成密度损失。
- 无限集合要求对所有 N 同时保持近 N^{1/2} 的下界，不能只在稀疏尺度上达到好密度；跨尺度拼接会产生大量跨块和冲突。
- Erdős 已证明任意无限 Sidon 集的 |A∩[1,N]|/N^{1/2} 的 liminf 为 0，说明不能追求固定常数倍 N^{1/2}，构造必须精细控制缓慢损失。
- 当前最好指数 sqrt(2)-1 与 1/2 仍有明显差距；提升到 1/2-o(1) 很可能需要新的结构思想，而非简单参数优化。
- 有限计算搜索容易产生只在小 N 上成立的模式，外推风险高；形式化验证也只能验证给定构造，不能自动产生关键新构造。

### 需要的验证

- 若提出新构造，必须证明块内和、块间和、不同尺度间和都唯一，且覆盖所有 N 的计数下界。
- 需要给出明确的函数 c_epsilon 或等价渐近证明，说明对每个 epsilon>0 都有 |A∩[1,N]| >= c_epsilon N^{1/2-epsilon}。
- 需要与 Ruzsa 构造和 Erdős-Rényi bounded-representation 构造逐项对照，确认不是重新得到较弱已知结论。
- 需要用形式化证明或至少机器可检查的证明骨架验证关键组合引理，尤其是递归拼接和冲突删除步骤。
- 计算实验只能作为候选生成；最终必须有无限族构造和渐近证明，不能依赖有限范围验证。

### 公开版思考摘要

该问题有明确结构和可工具化入口，但核心难点是把接近最优密度与严格 Sidon 唯一和条件在无限尺度上同时维持。GPT-5.5 可望在证明整理、已知构造审计、参数优化、反例搜索和候选构造验证方面产生实质辅助；若要求完整解决，则需要突破当前最好指数到 1/2-o(1)，这超出常规 LLM+工具组合的可靠能力范围。

### 免责声明

以上是对 AI 辅助可解性和推进可能性的评估，不是该 Erdős 问题的解答，也不声称给出了满足条件的无限 Sidon 集构造。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `confirmed_open`
- 状态信心: `high`
- 可行动性: `research_ready`
- 人工复核: `not_required`
- 独立研究 Prompt: [prompts/problem_39.md](../../prompts/problem_39.md)

### 状态结论

截至 2026-07-27，题库页面仍将本题列为 open，论坛页没有任何解答或部分解答声称；2026 年 6 月 O'Bryant 的预印本仍明确称 Ruzsa 的指数 \(\sqrt2-1\) 构造为无限 Sidon 集合的纪录。检索未发现可审查的解决或反例。故原题是定义明确且仍开放的构造问题。

### 当前规范陈述

是否存在一个固定的无限集合 \(A\subseteq\mathbb N\)，满足： (i) \(A\) 是 Sidon（\(B_2\)）集合，即对任意 \(a,b,c,d\in A\)，若 \(a+b=c+d\)，则多重集 \(\{a,b\}=\{c,d\}\)；且 (ii) 对每个 \(0<\epsilon<1/2\)，存在常数 \(c_\epsilon>0\) 和 \(N_\epsilon\)，使得所有整数 \(N\ge N_\epsilon\) 都有 \(|A\cap[1,N]|\ge c_\epsilon N^{1/2-\epsilon}\)？集合 \(A\) 必须对所有 \(\epsilon\) 相同，但常数和起始阈值可依赖 \(\epsilon\)。

```text
Does there exist a single infinite set A ⊆ ℕ such that (i) A is a Sidon (B₂) set: for all a,b,c,d ∈ A, a+b=c+d implies {a,b}={c,d} as multisets; and (ii) for every ε with 0<ε<1/2, there are constants c_ε>0 and N_ε such that, for every integer N≥N_ε, |A∩[1,N]|≥c_ε N^(1/2−ε)? Equivalently, A(N):=|A∩[1,N]| is Ω_ε(N^(1/2−ε)) for every ε>0, with A fixed and the implied constants/thresholds allowed to depend on ε.
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 没有发现能否定上述规范化字面命题的简单构造。Erdős 的 \(\liminf A(N)/\sqrt N=0\) 上界，以及 O'Bryant 的 \(\liminf A(N)/\sqrt{N/\log N}\) 有界结论，都不与 \(A(N)\gg_\epsilon N^{1/2-\epsilon}\) 相矛盾。
- 版本变化: 未发现原题被后续文献替换、分裂或修正为非等价目标。2012/2014 年 Cilleruelo 给出了达到 Ruzsa 指数 \(\sqrt2-1\) 的显式构造，但没有提高指数；2026 年 O'Bryant 的工作改进了无限 Sidon/\(\gamma\)-Golomb ruler 的 liminf 型厚度上界，也未解决本题。Formal Conjectures 中存在陈述形式化文件，但该文件的主定理仍以 `sorry` 占位，不能当作证明。

陈述问题：

- 原文没有展开 Sidon 的约定。这里采用加法组合论的 \(B_2\) 约定，包含重复项（例如 \(a+a\)），且只允许交换加数造成的平凡等式。
- \(\gg_\epsilon\) 的标准渐近含义必须补足：隐含正常数与“充分大”的阈值均可依赖 \(\epsilon\)，但不能依赖 \(N\)；集合 \(A\) 不得随 \(\epsilon\) 改变。
- 字面上的“所有 \(\epsilon>0\)”可等价缩为 \(0<\epsilon<1/2\)：\(\epsilon\ge1/2\) 时要求由无限性自动满足。

需要固定的量词/约定：

- The existential quantifier over A is outside the universal quantifier over ε; one construction must work for every ε.
- For each fixed ε, the constants c_ε and N_ε may depend on ε, and the lower bound must hold for every integer N≥N_ε.
- Sidon means uniqueness of unordered two-term sums, including repetitions: a+b=c+d entails equality of the two multisets.

### 文献与当前边界

已核验的主要结果：

- 贪心法：逐步避开已有三元差 \(a_i+a_j-a_k\)，得到 \(A(N)\gg N^{1/3}\)。Cilleruelo 的论文给出了该计数的简短说明。
- Ajtai–Komlós–Szemerédi（1981，同行评审）构造 \(A(N)\gg(N\log N)^{1/3}\) 的无限 Sidon 序列。
- Ruzsa（1998，同行评审）以概率性方法首次越过 \(1/3\)，证明存在 \(A(N)=N^{\sqrt2-1+o(1)}\) 的无限 Sidon 序列。
- Cilleruelo（2012 预印本；2014 同行评审发表）以离散对数和删点给出同指数的显式构造。
- Erdős 的定理为每个无限 Sidon 集合给出 \(\liminf_{N\to\infty}A(N)/\sqrt N=0\)；这仅排除在所有尺度保持正的 \(\sqrt N\) 比例，未排除本题的任意固定幂损失。
- Cilleruelo–Kiss–Ruzsa–Vinuesa（2010，同行评审）证明了有界表示数 \(B_2[g]\) 的 \(N^{1/2-\epsilon}\) 类构造；因 \(g\) 一般大于 1，不能升级为 Sidon。

最近相关工作：O'Bryant，2026 年 6 月预印本《The Thickness of Infinite Sidon Sets》：以分块能量与 Cauchy 不等式证明每个 \(\gamma\)-Golomb ruler 的 \(\liminf A(N)/\sqrt{N/\log N}\) 有显式上界，并构造 limsup 为 \(\sqrt N\) 量级的例子。作者在引言中称 Ruzsa 的 \(\sqrt2-1\) 仍为无限 Sidon 的纪录；该论文处理的是不同的 liminf/limsup 厚度问题。

剩余核心：构造一个真正的 \(B_2\) 集合（不是固定 \(B_2[g]\), \(g>1\)），使同一个集合在每个足够大的尺度都达到 \(N^{1/2-o(1)}\) 的下界；已知指数 \(\sqrt2-1\approx0.4142\) 与目标 \(1/2\) 之间仍有实质缺口。

已使用方法：

- 贪心禁配与删点法。
- 概率构造及从近 Sidon 序列删除冲突。
- Ajtai–Komlós–Szemerédi 的图论/随机独立集方法。
- Ruzsa 的素数对数编码和概率参数选择。
- Cilleruelo 的有限域离散对数编码与显式冲突删除。
- 分块计数、加法能量与 Cauchy 型不等式（用于厚度上界）。

争议或不确定性：

- 题库自身明确警告其 open 标签只是维护者的当前判断；本审计通过近期预印本和定向检索予以交叉核验，但不能证明世界上不存在尚未公开或未被索引的证明。
- Erdős–Rényi 近满密度结果的表示函数上界是有界常数而非 1；将其误读为 Sidon 是本题最主要的文献陷阱。
- Formal Conjectures 文件虽然存在，但含 `sorry`，且其渐近量词编码应在任何形式化使用前逐项审查；它不提供已验证的证明。

### 证据来源

- [Erdős Problem #39 — Discussion thread](https://www.erdosproblems.com/forum/thread/39) — Thomas F. Bloom / Erdős Problems, 2026-04-06; `problem_page`, `database_record`, directness=`direct`, reliability=`high`. 页面将本题标为 OPEN，说明没有论坛中的完整或部分解答声称，并列出 Ruzsa 的 \(\sqrt2-1\) 纪录、Erdős 的 liminf 上界和 Erdős–Rényi 的有界表示函数近似结果。
- [An Infinite Sidon Sequence](https://www.sciencedirect.com/science/article/pii/S0022314X97921922) — Imre Z. Ruzsa, 1998-01; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 证明存在无限 Sidon 序列，其计数函数具有 \(N^{\sqrt2-1+o(1)}\) 量级；DOI 为 10.1006/jnth.1997.2192。
- [A Dense Infinite Sidon Sequence](https://www.sciencedirect.com/science/article/pii/S0195669881800145) — Miklós Ajtai, János Komlós, Endre Szemerédi, 1981; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 给出 \(\gg (N\log N)^{1/3}\) 的无限 Sidon 序列构造，是贪心 \(N^{1/3}\) 后的早期改进。
- [Infinite Sidon sequences](https://arxiv.org/abs/1209.0326) — Javier Cilleruelo, 2012-09-03; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 给出基于离散对数的显式无限 Sidon 序列，计数函数为 \(N^{\sqrt2-1+o(1)}\)；论文说明 Ruzsa 的同指数证明非构造性。该工作后来发表于 Advances in Mathematics 255 (2014)，DOI 10.1016/j.aim.2014.01.011。
- [Generalization of a theorem of Erdős and Rényi on Sidon sequences](https://onlinelibrary.wiley.com/doi/abs/10.1002/rsa.20350) — Javier Cilleruelo, Sándor Z. Kiss, Imre Z. Ruzsa, Carlos Vinuesa, 2010-10-21; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 对每个 \(h\ge2\) 与 \(\epsilon>0\)，构造表示数有界的序列且密度 \(\gg N^{1/h-\epsilon}\)；\(h=2\) 说明接近本题目标的有界表示函数版本并不等同于 Sidon 条件。
- [The Thickness of Infinite Sidon Sets](https://arxiv.org/abs/2606.28651) — Kevin O'Bryant, 2026-06-26; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 证明对 \(\gamma\)-Golomb ruler 的新 liminf 厚度上界；引言明确称 Ruzsa 1998 的 \(N^{\sqrt2-1}\) 构造仍是无限 Sidon 集合的纪录。该结论不蕴含本题的正面或负面答案。
- [FormalConjectures: Erdős Problem 39](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/39.lean) — Formal Conjectures Authors, 2025; `formalization`, `formalized_artifact`, directness=`direct`, reliability=`high`. 提供与本题相应的 Lean 命题接口，并标记为 research open；文件中的 theorem 证明为 `sorry`，因此它仅形式化陈述，绝非解决证明。

### 完成标准

- 肯定出口: Give a rigorous construction of one infinite B₂ set A⊆ℕ and prove: for every 0<ε<1/2 there exist cε>0 and Nε such that A(N)≥cεN^(1/2−ε) for all integers N≥Nε. The proof must establish uniqueness of all unordered two-term sums, including diagonal sums, across the entire infinite union.
- 否定出口: Prove that for every infinite Sidon set A⊆ℕ there exists ε∈(0,1/2) such that A(N) is not Ω(N^(1/2−ε)); equivalently, for every c>0 and N0 there is N≥N0 with A(N)<cN^(1/2−ε).

不构成完成：

- A construction depending on ε rather than one fixed A.
- A B₂[g] construction with any fixed g>1, or merely bounded convolution/representation function.
- A lower bound only along a subsequence of N, a limsup statement, or a finite family of intervals.
- Reproducing Ruzsa/Cilleruelo exponent √2−1 without a genuine exponent improvement or another route to the stated target.
- A numerical search without an infinite construction and a proof of its global Sidon property.
- Using Erdős's liminf A(N)/√N=0 as a disproof; it is compatible with the target.

正确性陷阱：

- Check a+b=c+d with a=b or c=d; distinct-only pair conventions are insufficient.
- Keep the quantifiers in the order ∃A ∀ε ∃cε,Nε ∀N≥Nε.
- Audit collisions between every pair of construction blocks, not only within a block or between adjacent blocks.
- If deletion is used, prove cumulative deletions preserve the claimed lower bound at every N, not only at block endpoints.
- Do not conflate an upper bound on liminf normalized by √N or √(N/log N) with failure of every N^(1/2−ε) lower bound.
- If invoking a formalization, verify the exact Lean statement and absence of axioms/placeholders such as `sorry`.

### 更新后的 AI 可解答性

- 等级: `low_candidate`
- 分数: `16/100`
- 信心: `medium`
- 结论: 这是清晰、长期开放且可证伪/可验证的构造问题，但现有指数与目标之间存在较大缺口；在没有新结构性想法时，AI 独立解决的可能性偏低。

支持理由：

- 目标和量词可精确定义，Sidon 性与渐近下界均可逐步审计。
- 已有多个可比较的构造范式和一个明确的当前指数纪录，便于对新引理作基准检查。
- 若提出具体分块构造，有限阶段的冲突控制和密度损失可被严格验证。

主要障碍：

- 该问题已持续数十年，Ruzsa/Cilleruelo 的 \(\sqrt2-1\) 与 \(1/2\) 之间尚无已知通用桥梁。
- 全局 Sidon 条件会造成跨尺度碰撞；局部或有限区间的高密度不能直接拼接。
- 有界表示函数 \(B_2[g]\) 的近 \(1/2\) 结果不能通过简单删点无损地转化为 \(g=1\)。
- 计算只能检验有限前缀，不能承担渐近结论。

Proof-first 路线：

- 先把任意候选分块/编码方案化为一个跨块碰撞引理；只有该引理给出可求和的删点代价时才继续密度分析。
- 研究能否把近 Sidon 的表示冲突组织为低度、可着色或可稀疏删除的超图，同时保持所有尺度的前缀下界。
- 探索有限域 Sidon 模型的嵌入或拼接是否可产生对所有跨块差值/和的确定性隔离；必须先证明一般拼接判据。
- 可选的一项计算仅用于测试一个已明确的有限块冲突引理或反例模式；应预先规定输入范围、需验证的命题和停止条件。

需要验证：

- 任何声称突破指数的工作都应核对其是否真为单一 \(B_2\) 集合、下界是否对全部充分大 \(N\) 成立，以及常数是否允许随 \(N\) 变化。
- 需由独立审稿者逐式检查跨块加法四元组、边界块和对角和。
- 若依赖近期预印本或网页状态，应在提交结论前再次检索 arXiv、期刊与 Erdős Problems 论坛。

### 审计限制与人工复核理由

- 本审计完成了题库页、论坛页、原始/后续论文、arXiv 和形式化仓库的定向检索，但文献检索不可能逻辑上排除所有未公开、未索引或访问受限的结论。
- O'Bryant 2026 是近期预印本，尚非同行评审；本审计仅将其用于“作者仍称 Ruzsa 为纪录”的近期文献状态佐证，不把其新定理用作本题的解决依据。
- 题库的 formalized 标签仅表示陈述文件存在。该文件公开可见 `sorry`，且没有经过本审计的 Lean 编译复核。

- 若后续研究需要把形式化陈述作为严格规范，应由 Lean 专家复核该文件中渐近量词的精确语义。
- 在正式发表任何新结论前，应再次检索 2026-07-27 之后的新预印本、期刊文章和论坛更新。

<!-- DEEP_REVIEW:END -->
