# Problem 17

## 基本信息

- 原始链接: https://www.erdosproblems.com/17
- LaTeX 页面: https://www.erdosproblems.com/latex/17
- 原始状态: `open`
- 奖金: `no`
- 主类别: `number theory`
- 原始标签: `number theory`, `primes`
- 形式化状态: `yes`
- OEIS: `A038133`
- 原站备注字段: cluster primes

## 原问题

Are there infinitely many primes $p$ such that every even number $n\leq p-3$ can be written as a difference of primes $n=q_1-q_2$ where $q_1,q_2\leq p$?

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `27/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- 题面或备注出现有限对象/计算线索
- 已有形式化陈述，可降低语义误读风险
- 存在 OEIS 数据入口，利于实验与反例搜索

### 主要障碍

- 所属标签偏证明密集：number theory, primes
- 题面含渐近/无限对象线索：\ll, infinitely many, prime, primes

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: number theory, primes
- 有限/计算线索: finite, finitely
- 渐近/无限线索: \ll, infinitely many, prime, primes
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **低到中等候选。GPT-5.5 级别模型配合计算、形式化证明和文献检索，较可能在有限验证、等价重述、启发式建模和反例搜索上做出可靠推进；但直接证明存在无穷多个 cluster primes，或证明只有有限多个，仍很可能需要超出当前自动化能力的深层解析数论突破。**
- 等级: `low_to_medium_candidate`
- 分数: `32/100`
- 信心: `medium`
- 可能路线: 最现实路线是把性质转成可证书化的有限判定：对每个候选素数 p，验证所有偶数 n<=p-3 是否都有素数差表示，并为失败项给出缺失证据；同时用筛法、素数 k-元组启发式和覆盖同余/局部障碍搜索寻找可能的结构性原因。若尝试理论推进，较可行的是提出条件性结果、改进稀疏性上界的形式化复核，或建立更强的随机模型预测，而不是直接完成无穷性证明。

### 支持理由

- 问题谓词本身是有限可计算的：给定 p，只需检查 p 以内素数差是否覆盖指定偶数集合，因此适合高性能搜索、证书生成和形式化验证。
- Problem JSON 标注 formalized=yes，说明至少存在可形式化表达的基础，降低了机器检查有限实例和辅助证明的门槛。
- 已知第一例失败素数为 97，且有 OEIS 序列锚点，便于复现实验、回归测试和发现计算异常。
- 备注中的已有结果给出非常强的稀疏上界，这为模型建立启发式、寻找局部障碍和筛法改进提供了明确目标。
- 该问题不要求构造所有素数差，只要求某些 p 的前缀素数差集覆盖区间，因此存在通过计算发现模式或证伪某些猜想路线的空间。

### 主要障碍

- 核心无穷性命题是关于素数差覆盖的全局存在性，涉及随 p 增长的一族条件，不像固定长度素数模式那样可直接套用标准素数 k-元组启发式。
- 备注中的上界显示这类 p 若无穷多也极其稀疏；计算搜索很难区分“极稀疏无穷多”和“最终没有”。
- 筛法通常擅长上界和排除，而证明这类稀有素数结构的下界会碰到类似奇偶障碍和相关性控制问题。
- 靠形式化证明只能检查候选证明或有限计算，不能自动提供缺失的解析数论新思想。
- 若尝试证明有限性，也需要找到对所有足够大 p 有效的结构性缺口；目前从给定材料看没有明显的单一局部障碍。

### 需要的验证

- 复现给定事实：97 是第一个不满足性质的素数，并用独立程序检查 A038133 初段一致性。
- 为每个被判定满足性质的 p 保存完整 witness：每个偶数 n 对应一组 q1,q2<=p 的素数差表示。
- 为每个失败 p 保存最小未覆盖偶数 n，并形式化验证不存在合法素数对。
- 对搜索程序做双实现交叉验证，例如位集差集法与直接素数对枚举法互检。
- 若模型提出理论证明，需要用形式化工具或专家审查逐步验证筛法估计、量词范围、常数依赖和与既有上界是否相容。

### 公开版思考摘要

这个问题的计算层面很友好，但理论层面很硬。GPT-5.5 可以可靠地把有限判定、证书化搜索、反例定位和形式化检查做得很强，也可能帮助提出条件性命题或改进实验启发式；然而，证明无穷多这样的稀疏素数，或证明最终不存在，需要新的解析数论机制。给定已知强上界和增长条件族的复杂性，完整解决概率低于实验性推进概率。

### 免责声明

以上是对 AI 辅助可推进性的审查，不是该 Erdős 问题的解答，也不声称证明了 cluster primes 有无穷多个或只有有限多个。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `likely_open`
- 状态信心: `medium`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_17.md](../../prompts/problem_17.md)

### 状态结论

截至 2026-07-27，未发现可核验的解决或反例。Erdős Problems 当前页仍标为 open 且称评论区没有解答主张；Elsholtz 的已审论文将该问题称为 open。针对近三年、arXiv、形式化与精确题述的检索未找到后来解决文献，但这不是文献不存在的逻辑证明，故定为“likely_open”而非“confirmed_open”。

### 当前规范陈述

对素数 p>2，若对每个满足 2<=n<=p-3 的正偶整数 n，都存在不超过 p 的素数 q1,q2 使 n=q1-q2，则称 p 为 cluster prime。问题是：这样的素数是否无穷多；等价地，对每个实数 B，是否存在 cluster prime p>B。

```text
For a prime p>2, call p a cluster prime if, for every positive even integer n with 2<=n<=p-3, there exist primes q1,q2<=p such that n=q1-q2. Determine whether the set of cluster primes is infinite; equivalently, prove or disprove: for every real B there is a cluster prime p>B.
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `not_applicable`
- 检查说明: 核心断言是“无穷多个”，因此一个非-cluster prime 不能构成反例。已知 97 是最小非-cluster prime，但这只否定“所有素数均具该性质”。未发现能直接判定该无穷性断言的简单构造或反例。
- 版本变化: 未发现对核心无穷性问题的后来替换或分裂。需修复的是定义的正性边界与 OEIS 指向：A038133 为非-cluster primes，A038134 才是 cluster primes。Elsholtz（2003）将 BES99 的任意对数幂节省改进为 exp(-c(log log x)^2) 型上界；这不是对原问题的解决。

陈述问题：

- 原题的“every even number”未明说 n 为正数；若按全部偶整数（含任意负数）理解，命题不可能成立。原始文献明确采用“positive even integer”，从而唯一地确定了应审计的标准版本。
- 原题未排除 p=2；文献定义采用 p>2。该有限边界约定不影响“无穷多”问题。
- 输入及当前 Erdős Problems 页面把 A038133 说成 cluster primes 的序列，但 OEIS A038133 实为奇数非-cluster primes；cluster primes 对应 A038134。这是背景说明的转录错误，不改变核心问题。
- FormalConjectures 工件中的主命题及两个上界声明均含 sorry，不能作为已核验的形式化证明；其 Elsholtz 上界的单一常数对所有 c<1/8 的量词也可能强于论文逐个 c 的通常 Big-O 表述。

需要固定的量词/约定：

- p ranges over primes greater than 2.
- n ranges over positive even integers, not all even integers: 2<=n<=p-3.
- For each admissible n, q1 and q2 may depend on n; both are positive primes and both must be at most p.
- The order q1>=q2 follows from n>0 and need not be imposed separately.
- For a bound written C(x)=O_c(f_c(x)), the implied constant may depend on the fixed c; it is not automatically uniform as c approaches 1/8.
- The infinitude assertion means: for every B, some qualifying prime p exceeds B.

### 文献与当前边界

已核验的主要结果：

- Blecksmith–Erdős–Selfridge（1999，同行评审）证明：令 C(x) 为不超过 x 的 cluster primes 数，则对每个固定 A>0，C(x) <<_A x/(log x)^A；其结果也推出 cluster primes 倒数和收敛。该结果只说明极稀疏，不能推出有限性。
- Elsholtz（2003，同行评审）以 Montgomery–Vaughan 型大筛和素数 s-元组的上界计数改进为：对每个固定 0<c<1/8，C(x)=O_c(x exp(-c(log log x)^2))。论文的引言明确说无穷性仍开放；该上界仍与无穷集合相容。
- BES99 还进行过至 10^13 的计算。此类有限枚举仅描述初段，不能证明无穷性或最终不存在。
- 作为必要条件，cluster prime p 左侧短区间必须包含越来越多的素数；这解释了名称并支撑筛法上界，但目前未提供构造无穷多个 cluster primes 的下界机制。

最近相关工作：本次检索找到的最近一篇直接研究该定义并给出新定理的论文是 Elsholtz（2003）。对 2023–2026、arXiv、作者页、精确短语和形式化库的检索未找到后续解决或反例；当前 Erdős Problems 数据库与 MathWorld 仍报告其开放。此“未找到”应视为检索局限，而非完备文献证明。

剩余核心：证明或否定存在无穷多个素数 p，使得从 2 到 p-3 的每个正偶数都可表示为两个不超过 p 的素数之差。已知的稀疏上界、有限计算及有界素数间隔结果均没有给出这一全范围、随 p 增长的同时表示条件。

已使用方法：

- Brun 小筛与素数元组的上界筛（BES99）。
- Montgomery 大筛、Vaughan 引理和对短区间内素数模式的上界计数（Elsholtz 2003）。
- 递推式枚举/筛选 cluster primes 的有限计算（BES99）。

争议或不确定性：

- Erdős Problems 的 A038133 注释与 OEIS 直接冲突；应改为 A038134 才表示 cluster primes。
- Elsholtz 作者网页将期刊卷号列为 110，但期刊官方页和 EuDML 均为 109；本审计采用官方期刊记录的 109。
- FormalConjectures 的相关声明使用 sorry，且其对 c 的常数量词可能比论文标准表述更强，不能作为已形式化验证的定理。
- 未能从可公开访问的一手来源逐页重建 BES99 的完整证明；其定理陈述由当前数据库、Elsholtz 引言及二级资料交叉支持，但任何新工作应优先取得合法原文。

### 证据来源

- [Erdős Problem 17](https://www.erdosproblems.com/17) — Erdős Problems database, date unknown; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 当前记录标记该问题为 open，称评论中没有完整或部分解答主张，并列出 BES99 与 El03 上界。该页面同时重复了 A038133 的错误归属，故不能无保留采纳其 OEIS 注释。
- [Erdős Problem 17 LaTeX source](https://www.erdosproblems.com/latex/17) — Erdős Problems database, date unknown; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 提供现行题述与数据库所记录的两个定量上界；用于与原始论文和定义作比对。
- [Cluster Primes](https://www.tandfonline.com/doi/abs/10.1080/00029890.1999.12005005) — Richard Blecksmith, Paul Erdős, J. L. Selfridge, 1999; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 核验 BES99 的题名、作者、期刊、卷页与 DOI；该论文是 cluster-prime 定义、任意对数幂节省上界及有限计算背景的一手来源。
- [On cluster primes](https://www.math.tugraz.at/~elsholtz/WWW/papers/papers13clusteractarith.pdf) — Christian Elsholtz, 2003; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 直接给出 p>2、正偶数 n 的定义；明确称无穷性问题开放；证明以大筛/素数 s-元组计数得到 exp(-c(log log x)^2) 型上界，并在末页说明可取任意 c<1/8。
- [Acta Arithmetica 109(3): On cluster primes](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/109/3) — Institute of Mathematics, Polish Academy of Sciences; Christian Elsholtz, 2003; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 核验 Elsholtz 论文的权威书目信息：Acta Arithmetica 109(3), 281–284，DOI 10.4064/aa109-3-6；纠正作者网页列为卷 110 的冲突元数据。
- [OEIS A038133](https://oeis.org/A038133) — The OEIS Foundation, date unknown; `oeis`, `database_record`, directness=`direct`, reliability=`high`. 该条目明确为“odd primes that are not cluster primes”，故证实输入背景中 A038133 的方向写反。
- [OEIS A038134](https://oeis.org/A038134) — The OEIS Foundation, date unknown; `oeis`, `database_record`, directness=`direct`, reliability=`high`. 该条目是 cluster primes 的对应 OEIS 序列，用于修复 A038133/A038134 的混淆。
- [FormalConjectures.ErdosProblems.17](https://firsching.ch/formal-conjectures/src/FormalConjectures/ErdosProblems/%C2%AB17%C2%BB/) — Formal Conjectures Authors, 2025; `formalization`, `formalized_artifact`, directness=`direct`, reliability=`high`. 形式化了 cluster-prime 谓词和问题陈述，并将主问题标为 research open；页面明确显示 sorry，因此不是该问题或文献上界的核验证明。
- [Cluster Prime](https://mathworld.wolfram.com/ClusterPrime.html) — Eric W. Weisstein, date unknown; `secondary_index`, `database_record`, directness=`indirect`, reliability=`medium`. 独立二级资料仍称无穷多个 cluster primes 未知，并复述 BES99 的超对数幂稀疏性及倒数和收敛；仅作为当前状态的辅助证据。

### 完成标准

- 肯定出口: Prove that for every real B there exists a prime p>B such that, for every positive even integer n with 2<=n<=p-3, there are primes q1,q2<=p satisfying q1-q2=n.
- 否定出口: Prove that there exists a bound B such that every prime p>B fails the cluster-prime condition; explicitly, for each such p exhibit or prove the existence of a positive even n<=p-3 for which no pair of primes q1,q2<=p has q1-q2=n.

不构成完成：

- Verifying the condition for any finite range of p, even with exhaustive code and certificates.
- Proving C(x)=o(x/log x), any stronger upper bound that still tends to infinity, or convergence of the reciprocal sum.
- Showing infinitely many bounded prime gaps, twin primes, or a fixed prime tuple without proving every required difference for the same p.
- A probabilistic heuristic, numerical extrapolation, or a conditional result unless its assumptions are explicitly part of the claimed theorem.
- A Lean declaration containing sorry, an unchecked axiom, or a statement whose quantifiers differ from the target.

正确性陷阱：

- Quantify n over positive even integers only; do not accidentally include 0 or negative even integers.
- Check every n through the inclusive endpoint p-3, not merely a tested subset or asymptotically most n.
- Both q1 and q2 must be prime and at most p; q1,q2 may vary with n.
- Do not infer finiteness from a super-polynomial-in-log upper bound for C(x).
- Do not confuse A038133 (non-cluster primes) with A038134 (cluster primes).
- For a negative proof, establish an eventual obstruction for all sufficiently large prime p, not merely infinitely many failures.
- For an affirmative proof, verify that all required differences hold simultaneously for each produced p.

### 更新后的 AI 可解答性

- 等级: `low_candidate`
- 分数: `8/100`
- 信心: `medium`
- 结论: 这是定义清楚但极难的解析数论开放问题。AI 可协助文献核验、引理审计和有限证书检查，但在当前理论缺口下，独立解决的机会很低。

支持理由：

- 目标具有明确的二值完成条件，且每个候选 p 的有限验证可精确认证。
- 已有筛法给出强上界和清楚的必要局部素数聚集条件，为审计已有路线提供了结构。
- 核心仍是一个随 p 增长的全称表示条件；现有文献没有下界、构造或最终障碍。

主要障碍：

- 正向结论要求同一 p 同时覆盖线性数量的偶差，远强于仅有固定长度的素数模式或有界间隔。
- 负向结论需要对所有充分大 p 给出某个缺失差；现有稀疏性结果不提供这种最终排除。
- 有限计算没有能终止无穷性问题的界，且启发式不能替代统一估计。

Proof-first 路线：

- 先对 BES99/Elsholtz 的必要条件进行精确重建，辨明哪些局部密度约束只给上界、哪些可能导出最终矛盾。
- 分别寻找可证的充分构造条件与可证的必然缺失差条件，避免把有界间隔或固定元组误当作充分条件。
- 将任何候选新引理转化为带完整量词的命题，并先进行独立反例搜索和依赖定理审计。

需要验证：

- 合法取得并逐项核查 BES99 全文，特别是算法、数据表及对固定 A 的常数依赖。
- 核查 Elsholtz 所引 Habilitationsschrift 是否含有任何未在文章中明示的更强结果。
- 在提交任何状态更新前，重复检索 MathSciNet/zbMATH、arXiv、Crossref 和主要作者近年论文页。
- 若使用 FormalConjectures，确认无 sorry、无额外公理，并校正 c 与隐含常数的量词。

### 审计限制与人工复核理由

- 本审计只使用了题目 JSON 及公开网络来源；未查看周边仓库条目。
- BES99 的正式出版页可核验元数据，但本次无法从该出版商直接取得可逐页审读的全文；其定理陈述由 Elsholtz 引言、当前数据库与二级资料交叉支持。
- “未发现 2003 年后专门解决文献”来自有针对性的公开检索，而非 MathSciNet、zbMATH 或全部付费数据库的穷尽检索。
- 当前网页的 open 标签和二级百科条目均可能滞后，不能单独确证开放状态。

- 建议人工再用 MathSciNet、zbMATH、Crossref 及 Elsholtz 的完整近年论文目录进行一次可复现的文献检索，以把“likely_open”提升或调整为更强结论。
- 应向 Erdős Problems 维护者报告并确认 A038133/A038134 的序列注释错误。
- 若后续依赖 BES99 的精确技术细节或计算数据，应取得并审读其合法全文。

<!-- DEEP_REVIEW:END -->
