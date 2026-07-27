# Problem 635

## 基本信息

- 原始链接: https://www.erdosproblems.com/635
- LaTeX 页面: https://www.erdosproblems.com/latex/635
- 原始状态: `open`
- 奖金: `no`
- 主类别: `number theory`
- 原始标签: `number theory`
- 形式化状态: `no`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

Let $t\geq 1$ and $A\subseteq \{1,\ldots,N\}$ be such that whenever $a,b\in A$ with $b-a\geq t$ we have $b-a\nmid b$. How large can $\lvert A\rvert$ be? Is it true that\[\lvert A\rvert \leq \left(\frac{1}{2}+o_t(1)\right)N?\]

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `27/100`
- 建议路线: 优先文献定位、特殊情形、数值实验和辅助引理搜索；完整证明需要新的数学思想。

## 判断依据

### 有利因素

- 目前只能依靠通用数学推理、文献归纳和特殊情形探索

### 主要障碍

- 所属标签偏证明密集：number theory
- 缺少明显有限搜索入口。

### 公开版思考过程摘要

- 先识别问题类型：无限/渐近或抽象证明倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: number theory
- 有限/计算线索: 无
- 渐近/无限线索: 无
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **高候选。对于题中的第二个渐近上界问题，给定备注已经指出存在肯定解法，并且可由 Elliott 的不等式较快推出；GPT-5.5 级别模型若配合文献检索、证明校验和小规模反例搜索，较可能重构、形式化检查并推广整理这一证明。对于更宽泛的“How large can |A| be?”即固定 t 下精确极值或次主项问题，则仍可能明显推进，但不应预期一次性完全解决。**
- 等级: `high_candidate`
- 分数: `82/100`
- 信心: `medium`
- 可能路线: 最可行路线是把条件改写为关于差 d=b-a 的禁用关系：若 d≥t 且 d|b，则不能同时选 b-d 与 b。随后按 d 或按整除结构建立双计数/筛型不等式，用 Elliott 型结果控制满足整除约束的差分对密度，推出固定 t 下 |A|≤(1/2+o_t(1))N。计算工具可用于枚举小 N、小 t 的极值结构，帮助发现 t=1、t=2 之外的构型；形式化工具可验证核心组合不等式与极限步骤。

### 支持理由

- 题目已有强提示：备注明确说第二个问题已有肯定解决，并且存在从 Elliott 不等式推出的较短路线，这使 AI 的任务更像证明重构、核查和规范化，而不是从零攻克未知难题。
- 问题结构相对具体：约束只涉及两点差 b-a 与整除关系 d|b，适合转化为图上的独立集、差分图、筛法或双计数问题，便于模型与计算工具协作探索。
- t=1 的精确答案和 t=2 的超半数下界给出清晰校准样例，可用于测试候选证明是否过强、是否误杀已知构造。
- 目标上界是主项级别的渐近命题，而非精确极值公式；这通常比求出所有极值构型更适合由已知解析数论不等式加组合论包装完成。
- 可验证性较好：小规模整数规划/最大独立集搜索能快速发现反例风险，证明助手可形式化有限图模型、极限符号和若干组合引理。

### 主要障碍

- 若要回答完整的“How large can |A| be?”，仅有主项 1/2 远远不够；t=2 已有 N/2+c log N 下界，说明次主项可能有非平凡结构。
- Elliott 不等式的精确适用条件、误差项和参数依赖需要非常小心；模型容易把平均型估计误用为逐点或均匀估计。
- o_t(1) 中 t 固定而 N 趋于无穷，证明中必须避免把 t 的依赖误写成对 t 一致的结论。
- 极值集合可能包含稀疏的偶数或高 2-adic 结构，简单奇偶划分不足以解释 t≥2 的现象。
- 若尝试形式化 Elliott 型解析数论输入，可能需要把深层不等式作为外部定理公理化，而不是完整形式化证明。

### 需要的验证

- 检索并核对备注中提到的 Elliott 不等式原文或可靠引用，确认定理陈述、常数和误差项足以推出所需 o_t(1) 上界。
- 把 AI 生成的证明拆成明确引理，逐条检查量词顺序：固定 t、N→∞、异常集合大小、误差项依赖。
- 对小 t 和中等 N 做整数规划或最大独立集枚举，确认候选上界证明没有与已知 t=2 构造或小规模最优解冲突。
- 若声称解决完整极值问题，需要额外验证次主项阶数、构造下界和上界是否匹配；否则只能声称解决主项渐近问题。
- 建议用 Lean/Isabelle 或至少可机检的证明脚本形式化组合图模型与双计数部分，把解析数论输入单独标记为外部定理。

### 公开版思考摘要

这个问题对 GPT-5.5 级别模型较友好，不是因为它简单，而是因为已有备注提供了明确的成功路径：第二个渐近问题可以由 Elliott 型不等式推出。模型最可能胜任的是重构证明、整理参数依赖、检查已知构造、用计算搜索排除明显错误，并把论证转成可审计的引理链。风险主要在于把“主项上界已经可证”误解为“完整极值函数已经解决”。因此我评为高候选，但只针对题中第二个渐近问题给出较高可完成度；完整极值问题仍属于更难的开放方向。

### 免责声明

以上是对 AI 工具辅助可解性和可验证性的评估，不是该 Erdős 问题的证明，也没有声称给出新的极值公式或完整解答。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `revised_open`
- 状态信心: `high`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_635.md](../../prompts/problem_635.md)

### 状态结论

原记录把两个不同强度的问题并列。对每个固定 t，渐近上界 F_t(N)≤(1/2+o_t(1))N 已被网站及讨论页明确标为已解决；但“如何大”的更精确问题仍开放，网站仍标记整个条目为 open。最自然的明确剩余靶标是：对每个固定 t≥2，证明或反驳 F_t(N)≤N/2+O_t(log N)。这与已知 t=2 的 N/2+c log N 下界匹配；不过 Tao 仅称这种精度“probably”是 Erdős 所求，故其作为原始问题的规范化残余目标仍需人工确认。

### 当前规范陈述

对整数 t,N≥1，令 F_t(N) 为满足下述条件的 A⊆[N]:={1,...,N} 的最大基数：对任意 a<b 且 a,b∈A，若 b−a≥t，则 (b−a) 不整除 b（等价地，不整除 a）。原条目包含：(i) 确定或给出 F_t(N) 的精确/锐渐近规模；(ii) 对每个固定 t，当 N→∞ 时是否有 F_t(N)≤(1/2+o_t(1))N。这里 o_t(1) 指可依赖固定 t、但随 N→∞ 而趋于零的量，并未要求 t 上一致。当前已核验的拆分是：(ii) 已获肯定解决；(i) 在更细误差尺度上仍开放。一个明确的修订研究靶标是：对每个固定 t≥2，证明或反驳对充分大的 N 有 F_t(N)≤N/2+C_t log N；这是由记录所暗示的靶标，尚不能说是已发表的独立猜想。

```text
For integers t,N≥1, let F_t(N) be the maximum cardinality of a set A⊆[N]:={1,...,N} such that for every a,b∈A with a<b and b−a≥t, one has (b−a)∤b (equivalently, (b−a)∤a). The original record asks (i) to determine, or give sharp asymptotics for, F_t(N), and (ii) whether, for every fixed t, F_t(N)≤(1/2+o_t(1))N as N→∞. Here o_t(1) means a quantity depending on the fixed parameter t that tends to 0 with N; no uniformity as t→∞ is asserted. The verified current split is: (ii) is resolved affirmatively; (i) remains open at the finer scale. A precise revised research target, motivated by the record rather than established as a separately published conjecture, is: for every fixed t≥2, prove or disprove F_t(N)≤N/2+C_t log N for all sufficiently large N.
```

### 陈述、量词与反例审计

- 歧义严重度: `material`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 未找到可直接否定原文字面第二问的简单反例。相反，记录给出 t=1 的精确值，并给出 t=2 的构造 F_2(N)≥N/2+c log N；后者否定了可能被误加的更强断言 F_t(N)≤N/2+O_t(1)，但并不否定原来的 (1/2+o_t(1))N 上界。
- 版本变化: 约 1980 年：Erdős 致 Ruzsa 信提出问题。2026-01-30 的论坛记录称 GPT-5.2 的论证（并有 Lean 形式化声称）解决了第二问；同日 Tao 指出该结论也可由 Elliott (1979) 的不等式很快导出。2026-01-31 Tao 进一步说明只应把第二部分标为已解，并将条目恢复为 open，因为更精确、约 N/2+O(log N) 的尺度远超 Elliott 型方法。当前网站仍为 OPEN。

陈述问题：

- “How large can |A| be?”未规定要精确公式、主项、误差阶还是仅上/下界，因此本身没有唯一的完成标准。
- 原条目的第二问仅固定 t 后取 N→∞；若把它误读为对随 N 增长的 t 一致成立，便是不同问题。
- 原条目是复合问题。已解决第二问并不解决第一问；将整个条目称为“solved”会掩盖精确误差项问题。
- 讨论中提及的 Lean 形式化没有给出可由本次检索直接审阅的公开工件链接；因此它可支持“存在形式化声称”，不能单独作为本审计对完整证明的独立验证。
- 把“预期精度约为 O(log N/N)”转为 F_t(N)≤N/2+O_t(log N) 是透明的代数重述，但 Tao 的措辞为“probably”，不是原始信件可审阅的正式规格。

需要固定的量词/约定：

- All variables are positive integers, with t fixed before N tends to infinity.
- The displayed condition need only be checked for ordered pairs a<b; the hypothesis b−a≥t already forces that order.
- Divisibility is integer divisibility by the positive integer b−a.
- A bound O_t(log N) means: for each fixed t there are C_t,N_t such that the bound holds for all N≥N_t.
- The t=1 case is exceptional and exact; the proposed sharp-error residual target is intended for t≥2.

### 文献与当前边界

已核验的主要结果：

- Erdős 的记录性观察：t=1 时 F_1(N)=floor((N+1)/2)，由 [N] 中全部奇数达到。
- Erdős 的记录性观察：t=2 时存在绝对常数 c>0，使 F_2(N)≥N/2+c log N；给出的集合为奇数与奇指数幂 2^k 的并。论坛评注指出该 t=2 构造自动对所有较大的 t 仍有效。
- 当前问题页和 Tao 的论坛说明支持：对每个固定 t，F_t(N)≤(1/2+o_t(1))N 已解决。论坛把其归于 GPT-5.2 的二阶矩式论证，并指出也可从 Elliott (1979) 的不等式导出。
- Tao 明确警告：该已解决的主项结论所得到的 o_t(1) 很慢，例如可类似 O(1/log log N)，不足以解决预期的 N/2+O(log N) 误差尺度。

最近相关工作：截至本次检索，最直接且最新的材料是 2026-01-30/31 的 #635 论坛讨论及 2026-02-01 更新的问题页；未检索到 2023–2026 年间以该问题或该精确独立集问题为对象、并给出更强误差项的可核验 arXiv/期刊论文。此为有针对性的未发现结果，不是不存在此类文献的证明。

剩余核心：在已知 F_t(N)=N/2+o_t(N) 后，确定固定 t≥2 时超出 N/2 的正确二级项。由 t=2（继而所有 t≥2）的 Ω(log N) 下界和 Tao 对预期精度的说明，一个可检验的核心靶标是 F_t(N)=N/2+Θ_t(log N)，其关键上界为 F_t(N)≤N/2+O_t(log N)。常数、精确公式及是否对每个 t 采用同一阶数仍未由本审计的来源确定。

已使用方法：

- 将 [N] 看作图的顶点，并在 b−a 整除 b（等价于整除 a）时连边；F_t(N) 是带短差过滤后的独立数。
- GPT 论证据论坛称使用二阶矩论证；Tao 认为其与 Elliott 的二阶矩方法几乎相同。
- Elliott 型均值不等式，以及与之相关的按素数整除性对算术函数均值作抽样比较的方法。
- 奇数加稀疏的二的幂的显式构造，用于给出 Ω(log N) 二级项下界。

争议或不确定性：

- 论坛中的 Lean 证明被报告为正确，但另一位评论者明确说对非形式化版本与 Lean 文件的对应关系未作彻底检查；且本次未取得该工件链接。因此不得把该报告当作完整可复核的正式发表证明。
- Elliott (1979) 是同期经典来源，但本次无法直接检查 Lemma 4.7 的原文及其到 #635 的全部推导。主项结论由网站与 Tao 的直接说明强力支持；对该推导的逐行独立验证仍待完成。
- “N/2+O(log N) 是原问题意图”的依据是 Tao 的概率性措辞，不是已核验的 Erdős 原信。后续研究应明确把它作为修订目标，而非悄然声称它就是原文的唯一形式化陈述。

### 证据来源

- [Erdős Problem #635](https://www.erdosproblems.com/635) — T. F. Bloom (database editor); original question attributed to Paul Erdős, 2026-02-01; `problem_page`, `database_record`, directness=`direct`, reliability=`high`. 给出原问题、t=1 精确值、t=2 的 N/2+c log N 构造，并明确写明第二问已获肯定解决而整个条目仍为 open。
- [635 Discussion Thread](https://www.erdosproblems.com/forum/thread/635?order=oldest) — Liam Price; StijnC; Nat Sothanaphan; Terence Tao, 2026-01-30; `forum`, `informal_claim`, directness=`direct`, reliability=`high`. Tao 明确说明只应标记第二部分为 solved，Elliott 型论证仅给出很慢的 o_t(1)，而预期的 O(log N/N) 精度远在其能力之外；帖子还报告了 GPT/Lean 证明但未提供本次可独立审阅的形式化工件。
- [Probabilistic Number Theory I: Mean-Value Theorems](https://link.springer.com/book/10.1007/978-1-4612-9989-9) — P. D. T. A. Elliott, 1979; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 论坛将第二问的替代性经典依据具体定位为该书 Lemma 4.7；本次可访问的出版页核实了书目存在与作者，但未能直接审阅该引理文字，故不把其精确推导作为独立复核完成。
- [254A, Notes 9 – second moment and entropy methods](https://terrytao.wordpress.com/2019/11/12/254a-notes-9-second-moment-and-entropy-methods/comment-page-1/) — Terence Tao, 2019-11-12; `author_page`, `informal_claim`, directness=`indirect`, reliability=`high`. 给出 Elliott 不等式所比较的均值与按素数整除性抽样的均值这一技术背景，并展示它与二阶矩方法的关系；不直接证明 #635。
- [Erdős Problems LaTeX page for #635](https://www.erdosproblems.com/latex/635) — T. F. Bloom / Erdős Problems, date unknown; `problem_page`, `database_record`, directness=`indirect`, reliability=`medium`. 按协议访问的 LaTeX 页面；本次网页抓取仅返回站点框架，未提供可供独立比对的题目源码。

### 完成标准

- 肯定出口: For the revised sharp-error target: prove that for every fixed integer t≥2 there exist constants C_t and N_t such that F_t(N)≤N/2+C_t log N for every N≥N_t. Together with the recorded t=2 construction, valid also for larger t, this yields F_t(N)=N/2+Θ_t(log N) for every fixed t≥2.
- 否定出口: Disprove the revised sharp-error target by proving that for some fixed t≥2 and a sequence N_j→∞, F_t(N_j)−N_j/2 is not O(log N_j); equivalently, for every C there are arbitrarily large N with F_t(N)>N/2+C log N.

不构成完成：

- Re-proving only F_t(N)≤(1/2+o_t(1))N; that subproblem is already recorded as resolved.
- Giving a finite computation of F_t(N) for bounded N without a theorem controlling all larger N.
- Producing another lower-bound construction of order N/2+c log N without a matching upper bound or a superlogarithmic counterexample.
- Proving a statement with t allowed to grow with N, unless its quantifiers also imply the required fixed-t assertion.
- Showing only an average-case or random-set statement rather than the extremal bound for every admissible A.

正确性陷阱：

- Check the direction and threshold exactly: prohibited pairs have a<b, b−a≥t, and b−a divides b.
- Use b−a|b iff b−a|a only after observing that b=a+(b−a).
- Keep constants and onset thresholds allowed to depend on fixed t; do not claim uniformity in t without proof.
- Treat t=1 separately: its exact answer does not imply the t≥2 secondary term.
- If using the t=2 construction for t>2, explicitly verify that relaxing the prohibited-pair condition preserves admissibility.
- Any invocation of Elliott's inequality must state its hypotheses, parameter range, truncations, and the quantitative loss; an unspecified citation cannot establish O_t(log N).

### 更新后的 AI 可解答性

- 等级: `low_to_medium_candidate`
- 分数: `30/100`
- 信心: `medium`
- 结论: 作为“证明锐误差上界 N/2+O_t(log N)”的修订目标，它是定义清楚但难度较高的研究候选；不应把已经解决的主项问题误计为可解决度。

支持理由：

- 目标可化为有限区间上明确算术图的独立数上界，结论具有可逐行审核的量词和常数结构。
- 有匹配量级的 Ω(log N) 构造，给出了清晰的基准并排除了仅证 N/2+O_t(1) 的错误目标。
- 已有 Elliott/二阶矩框架说明主项障碍已被突破，因而新的工作可聚焦于定量强化。

主要障碍：

- 当前已知 Elliott 型方法的损失远大于 log N；需要本质上新的定量输入或极端集结构理论。
- 文献中缺少本次可审阅的完整现代证明和明确的锐化猜想；研究开始前须先复核原始推导与历史文献。
- 短差豁免、t 依赖常数和稀疏例外可能使从平均边密度到最大独立集的推断失效。

Proof-first 路线：

- 首先将 Elliott 型不等式完整改写为关于任意候选 A 的定量引理，准确定位从 o_t(N) 到 O_t(log N) 损失的步骤；这可以证伪一条路线而非直接依赖计算。
- 探索极大/接近极大独立集的结构稳定性：若 |A| 超过 N/2+C log N，推出一个明确禁止的整除边。
- 将奇数主构造附近的偶数例外按二进制赋值或小素因子分层；每一层都须有可求和的注入、充电或匹配证书。
- 唯一可选计算应仅用于检验预先声明的小规模结构引理或搜寻其反例；须先给出搜索域、待证引理、证书格式及停止条件。

需要验证：

- 获得并审阅 #635 所称的公开 Lean 文件及人类可读证明，核对其实际定理是否正是固定 t 的 o_t(N) 上界。
- 直接核对 Elliott (1979) Lemma 4.7 的全文和从该引理到 #635 的所有参数选择。
- 检索/审阅原始 Erdős–Ruzsa 信或 Gu83、Ru99 所指二手来源，确定“how large”原意是否确实要求 O(log N) 级误差。
- 在宣称锐误差目标仍开放前，继续用 MathSciNet/zbMATH、arXiv、作者主页和引用追踪检索该精确图独立集问题。

### 审计限制与人工复核理由

- 当前 Erdős Problems 主页通过网页抓取返回异常；使用其可检索的讨论页嵌入内容与搜索索引交叉核验了页面状态、题目文字和更新说明。
- 已访问 LaTeX 页面，但抓取仅显示站点框架，未能取得题目源码。
- 未取得论坛所称 Lean 工件或人类可读证明的可审阅链接，不能独立验证其代码、定理陈述或与非形式化证明的对应关系。
- Elliott 书的出版信息已核验，但本次未能直接读取 Lemma 4.7；关于其足以推出第二问的数学结论依赖 Tao/论坛的直接说明。
- 对近期文献进行了精确措辞、作者、问题号和 arXiv 定向检索；未发现并不逻辑证明不存在后续更强结果。

- 需取得并核阅 Lean 工件与 Elliott Lemma 4.7，才可把第二问的现有证明视为完全独立验证。
- 需查原始 Erdős–Ruzsa 往来或 Gu83/Ru99，确认 O(log N) 级误差是否为历史问题的正式预期，而非合理但推断性的修订目标。
- 若后续研究要公开宣称“当前最强结果”，应由领域专家再做 MathSciNet/zbMATH 和引文链检索。

<!-- DEEP_REVIEW:END -->
