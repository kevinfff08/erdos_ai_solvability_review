# Problem 124

## 基本信息

- 原始链接: https://www.erdosproblems.com/124
- LaTeX 页面: https://www.erdosproblems.com/latex/124
- 原始状态: `open`
- 奖金: `no`
- 主类别: `number theory`
- 原始标签: `number theory`, `base representations`
- 形式化状态: `yes`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

For any $d\geq 1$ and $k\geq 0$ let $P(d,k)$ be the set of integers which are the sum of distinct powers $d^i$ with $i\geq k$. Let $3\leq d_1<d_2<\cdots <d_r$ be integers such that\[\sum_{1\leq i\leq r}\frac{1}{d_r-1}\geq 1.\]Can all sufficiently large integers be written as a sum of the shape $\sum_i c_ia_i$ where $c_i\in \{0,1\}$ and $a_i\in P(d_i,0)$?

If we further have $\mathrm{gcd}(d_1,\ldots,d_r)=1$ then, for any $k\geq 1$, can all sufficiently large integers be written as a sum of the shape $\sum_i c_ia_i$ where $c_i\in \{0,1\}$ and $a_i\in P(d_i,k)$?

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `34/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- 题面或备注出现有限对象/计算线索
- 已有形式化陈述，可降低语义误读风险

### 主要障碍

- 所属标签偏证明密集：number theory
- 题面含渐近/无限对象线索：sufficiently large

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: number theory
- 有限/计算线索: finite
- 渐近/无限线索: sufficiently large
- 构造/存在性线索: construct

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5 + 计算/形式化证明/文献检索/反例搜索工具`
- 结论: **中等候选。第一问在给定备注中已说明有简单正证明且已 Lean 形式化，因此 GPT-5.5 级模型很可能能复现、审计或扩展验证这一部分。真正开放核心是第二问：带 gcd 条件且去掉低次幂后，要求对所有满足条件的底数组给出最终覆盖证明；这更像需要新的结构性数论论证，模型可显著推进和验证大量特例，但不宜评为高概率完整解决。**
- 等级: `medium_candidate`
- 分数: `58/100`
- 信心: `medium`
- 可能路线: 可行路线是先把第一问的已形式化证明作为可审计基线，抽象出覆盖/贪心/密度递推机制；再针对第二问建立固定底数组的反例搜索与证明管线：枚举不可表示数、检查模障碍、构造有限自动机或动态规划证书，寻找足以推出“所有充分大整数”的有限验证条件。若能把 gcd 条件转化为可控制的低位修正机制，并证明高位 P(d_i,k) 的和集在所有大区间中无缺口，则可能得到一般性推进。

### 支持理由

- 对象定义离散且可计算：P(d,k) 是 base-d 中 0/1 数字的集合，表示性问题可用动态规划、生成函数截断、自动机和模检验系统搜索。
- 第一问已有正证明并已 Lean 形式化；这显著降低了审计与复现难度，也给模型提供了可形式化的局部目标。
- 第二问已有特例证明（给定备注中提到 {3,4,7}），说明问题不是完全不可接近；模型可围绕特例抽取可推广的不变量。
- 必要条件在备注中已给出方向，包括 reciprocal 条件和 gcd 条件；这有助于约束模型的反例搜索和证明结构。
- 工具辅助价值较高：可以生成大量底数组/k 的覆盖阈值数据，发现失败模式，输出可独立检查的有限证书，并尝试把证书迁移到 Lean。

### 主要障碍

- 第二问需要对任意满足条件的底数组和任意 k>=1 证明最终覆盖，参数空间无限，单纯实验不能替代统一论证。
- 去掉低次幂后，小模数和低位修正能力变弱；gcd=1 虽必要，但未必直接给出可控的表示算法。
- P(d,k) 的和集具有稀疏、非线性、跨底数相互作用的结构，常规密度启发可能不足以证明无穷尾部全覆盖。
- 备注中 statement 的 reciprocal 条件写作 1/(d_r-1)，而 remarks 又描述为 1/(d_i-1)；正式审计前必须澄清这是排版问题还是题意差异。
- 若需要完整解决第二问，关键可能是新的组合数论引理，而不是更大规模的计算搜索。

### 需要的验证

- 核对正式 LaTeX 与 Lean 形式化版本，确认第一问的精确定义、是否允许空和、以及 reciprocal 条件的下标。
- 复现第一问的形式化证明，检查它是否只覆盖 P(d,0)，以及是否依赖 statement 中的具体条件。
- 为第二问实现独立搜索器：对给定 d_i,k 枚举不可表示数、估计覆盖阈值，并记录可验证证书。
- 系统测试已知特例 {3,4,7}，确认计算证书与备注中的既有结果一致。
- 寻找并验证一般化引理：例如有限区间覆盖推出尾部覆盖、模类补偿机制、或高位块递归扩张规则。
- 若模型产出证明，应先用小参数反例搜索攻击每个引理，再尝试 Lean/Isabelle 或至少机器可检查的有限证书验证。

### 公开版思考摘要

这个问题的可攻性来自其数字表示结构和已有形式化第一问；模型可以很有效地做证明复现、特例搜索、阈值计算和有限证书生成。难点集中在第二问的全参数统一性：gcd 条件只排除显然模障碍，但要证明去掉低次幂后仍能覆盖所有充分大整数，需要比实验更强的结构性论证。因此我判断 GPT-5.5 级系统有中等概率显著推进，较低到中等概率独立完成完整开放部分。

### 免责声明

以上是 AI 可解性与推进潜力评估，不是该 Erdős 问题的数学解答，也不声称证明第二问为真或为假。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `revised_open`
- 状态信心: `high`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_124.md](../../prompts/problem_124.md)

### 状态结论

输入中的字面阈值误将每一项都写成 d_r：在严格递增且 d_1>=3 时，该条件根本没有可取的有限 bases，故字面两问均真空平凡。主文献 BEGL96 与当前 Formal Conjectures 记录均使用 sum_i 1/(d_i-1)>=1；修复后，允许 1 的 k=0 版本已解决，而 gcd=1、任意 k>=1 的 BEGL 版本仍开放。因此应将条目作为“需修复转录后可研究的剩余开放目标”，而非按输入字面尝试。

### 当前规范陈述

输入字面条件是：对 r>=1、3<=d_1<...<d_r，要求 r/(d_r-1)>=1。该条件没有任何可取的 bases，因为严格递增整数给出 d_r>=r+2，故 r/(d_r-1)<=r/(r+1)<1；因此输入字面两问均为真空平凡。经修复的标准记录为：令 A={d_1,...,d_r} 是有限个互异整数，且 d_i>=3。对 k>=0，P(d,k)={sum_{j∈F}d^j：F 是 {k,k+1,...} 的有限子集}，空和为 0。假设 sum_i1/(d_i-1)>=1。k=0 断言是每个充分大的非负整数均属于 P(d_1,0)+...+P(d_r,0)，现已解决。剩余的 BEGL 猜想为：若另有 gcd(d_1,...,d_r)=1，则对每个固定 k>=1，存在 N=N(A,k)，使所有 n>=N 属于 P(d_1,k)+...+P(d_r,k)。等价地可写作 n=sum_i c_i a_i，其中 c_i∈{0,1}、a_i∈P(d_i,k)；若 P 含 0，c_i 是冗余的。A 与 k 在选择 N 前固定，表示可随 n 改变。

```text
Literal supplied condition: for r>=1 and 3<=d_1<...<d_r, it requires r/(d_r-1)>=1. This has no admissible tuple, since d_r>=r+2, hence r/(d_r-1)<=r/(r+1)<1. Thus both literal questions are vacuous. The canonical repaired record is as follows. Let A={d_1,...,d_r} be a finite set of distinct integers d_i>=3. For k>=0 define P(d,k)={sum_{j in F}d^j : F is a finite subset of {k,k+1,...}}; the empty sum is 0. Assume sum_{i=1}^r 1/(d_i-1)>=1. The k=0 assertion is that every sufficiently large nonnegative integer belongs to P(d_1,0)+...+P(d_r,0); it is now proved. The surviving BEGL conjecture is: if additionally gcd(d_1,...,d_r)=1, then for every fixed k>=1 there exists N=N(A,k) such that every integer n>=N belongs to P(d_1,k)+...+P(d_r,k). Equivalently, n=sum_i c_i a_i with c_i in {0,1} and a_i in P(d_i,k); c_i is redundant when 0 is admitted in P. The choices of finite subsets, a_i, and c_i may depend on n, while A and k are fixed before N is chosen.
```

### 陈述、量词与反例审计

- 歧义严重度: `material`
- 简单反例检查: `not_applicable`
- 检查说明: 这里发现的不是反例而是字面参数域为空的直接算术审计：d_r>=r+2 导致 r/(d_r-1)<1。对修复后的有限-base BEGL k>=1 目标，未发现简单反例。gcd 条件的必要性直接成立：若 g=gcd(d_i)>1，则每个 d_i^j（j>=1）、每个 P(d_i,k) 元素及任何表示和均被 g 整除。
- 版本变化: BEGL96 将 Pow(A;s)（s>=1）定义为各 base 的高幂所成序列，并猜想其完备性当且仅当倒数和条件与 gcd=1 成立。该论文给出若干充分条件，并明确处理 {3,4,7} 的 s=1 情形。Erdős 1997 年的相关问题允许 1；论坛所载 Aristotle/Alexeev 证明和 Lean 检验针对这一较易的 k=0 版本。2025-12-01 后的当前问题页 remarks 因而将第一问列为已解、第二问保留为 open。输入转录仍保留 d_r 下标错误，须修复。

陈述问题：

- 输入的 sum_{1<=i<=r}1/(d_r-1)>=1 不是小笔误：它与严格递增、d_1>=3 不相容。因为 d_r>=r+2，左端至多 r/(r+1)<1，故参数域为空。
- BEGL96 的原始 conjecture 明确使用 sum_{a∈A}1/(a-1)>=1，且要求幂指数 s>=1；当前 Formal Conjectures 记录也将 k=0 和 k!=0 分成不同命题。
- 输入把已解决的 k=0 问题与仍开放的 k>=1 问题合在同一条 open 记录中；两者不可互推。
- Erdős 在 Er97/Er97e 的历史表述是否允许 d^0=1 存在来源歧义。论坛中明确指出 BEGL96 不允许 1，而 Er97/Er97e 允许 1。
- 应明确空和为 0、每个 a_i 使用有限个互异指数、i 遍历有限 base 集、以及“充分大”的阈值可依赖 A 和 k。

需要固定的量词/约定：

- The literal d_r-only hypothesis has no instances; it must not be silently treated as the BEGL hypothesis.
- For the repaired target, A is finite and fixed, k is fixed and at least 1, and N may depend on A and k.
- For each n>=N, the chosen finite exponent sets may depend on n.
- Repeated numerical values arising from powers of different bases are separate sequence entries; within each P(d_i,k), exponents are distinct.
- The repaired result concerns all integers in a tail, not density one, an arithmetic progression, or a finite checked interval.

### 文献与当前边界

已核验的主要结果：

- BEGL96（同行评审）定义了高幂序列 Pow(A;s)，s>=1，并猜想有限 A 的完备性恰由 sum_{a∈A}1/(a-1)>=1 与 gcd(A)=1 刻画。该论文说明：有限 A 若倒数和条件失败，则 Pomerance 所指的丢番图逼近结果给出上密度小于 1。
- BEGL96 的 Theorem 1 证明：当 A 是正密度的整数序列且 gcd(A)=1 时，对任意 s 可取有限 A_0 使 Pow(A_0;s) 完备；Theorem 2--3 给出连续整数区间 base 集的充分条件。它们不是固定任意有限 A 的猜想解答。
- BEGL96 明确写出 Σ(Pow({3,4,7};1)) 最大遗漏数为 581，并列出其他若干小集合的计算/证明性结论。当前 Erdős Problems 与 Formal Conjectures 记录把 {3,4,7} 作为高幂问题的已解特例；审计未从 BEGL96 全文独立抽取任意 k 的该特例证明，故后者应保留核验任务。
- Melfi 2004（同行评审）构造无限 A，反驳无限族版本中倒数和条件的必要性，同时明确说有限 A 的问题仍开放；它不构成有限-base BEGL 猜想的反例。
- 论坛中的 Aristotle/Alexeev 结果使用排序幂序列和 Brown 型子序列和判据，解决含 1 的 k=0 版本；它不允许推出删除低幂后的 k>=1 版本。

最近相关工作：2025 年末的 Erdős Problems 页面更新、论坛讨论和 Formal Conjectures 源码是最直接的近年状态记录：它们一致把 k=0 标为 solved、把 k>=1 标为 open。针对精确题名、Pow(A;s)、问题号、Brown criterion、arXiv 及 2023--2026 关键词的定向检索，未找到可审查的一般有限-base k>=1 解决论文或预印本；这只是未发现，不能证明不存在。

剩余核心：在有限 A={d_1,...,d_r}、d_i>=3、sum_i1/(d_i-1)>=1、gcd(A)=1 的条件下，是否对每个 k>=1，P(d_1,k)+...+P(d_r,k) 包含所有充分大整数。必须覆盖临界等号和严格不等式、任意有限 base 集及任意 k，而不只是 k=0、{3,4,7}、大区间 base 集或无限 A。

已使用方法：

- complete sequence / Brown 型相邻项判据：适合含 1 的 k=0 版本，但论坛说明其不能直接克服删除初始幂后的困难。
- 丢番图逼近与密度：BEGL96 用于有限 A 下倒数和失败的必要性方向；它不是充分性证明。
- BEGL96 的组合构造：正密度 base 序列、有限子集截取、等差级数和模 D 的完全剩余系。
- 小 base 集的精细指数估计与有限核查：BEGL96 对 {3,4,7} 提及 Mignotte--Waldschmidt 型估计。
- 无限 base 集构造：Melfi 说明其与有限族问题不同，不能拿来证明或反驳剩余目标。

争议或不确定性：

- 输入/当前网页题面仍显示 d_r 下标，然而 BEGL96 原文和 Formal Conjectures 采用 d_i。字面条件为空，故研究前必须明确采用修复后的 BEGL 命题。
- 关于 Aristotle 工作，论坛存在“solved a version, not the BEGL problem”的明确澄清；任何声称 Problem 124 整体已解的新闻或二手报道均不可靠。
- Formal Conjectures 的公开 statement 文件含 sorry；它不应被误报为机器检验了 k>=1 猜想或其特例。具体 Alexeev/Aristotle proof artifact 仍需人工运行/审阅。
- BEGL96 全文可直接确认 s=1 的 {3,4,7} 结论；当前数据库称其证明第二问的 {3,4,7} 情形，但本次没有逐行核验任意 k 的延伸。

### 证据来源

- [Erdős Problems — Problem 124](https://www.erdosproblems.com/124) — Thomas F. Bloom / Erdős Problems, 2025-12-01; `problem_page`, `database_record`, directness=`direct`, reliability=`high`. 当前记录将总体条目标为 open，但 remarks 明确区分：第一问 k=0 已由 Aristotle/Alexeev 的工作正面解决并形式化；第二问为 BEGL 猜想、仍开放；并记录有限族倒数和必要性及 Melfi 的无限族例外。
- [Erdős Problem #124 — discussion thread](https://www.erdosproblems.com/forum/thread/124?order=oldest) — Boris Alexeev, Thomas Bloom, Terence Tao, Desmond Weisenberg, and other forum contributors, 2025-11-29; `forum`, `informal_claim`, directness=`direct`, reliability=`medium`. 给出 Aristotle 所解版本的精确 Lean 定理、可读证明提纲及其与 BEGL96 高幂版本的区别；评论明确称 BEGL96 排除 1、Er97/Er97e 允许 1。论坛声明评论未经站点验证，故不能单独充当形式化证明的独立核验。
- [Complete sequences of sets of integer powers](https://matwbn.icm.edu.pl/ksiazki/aa/aa77/aa7722.pdf) — S. A. Burr, P. Erdős, R. L. Graham, W. Wen-Ching Li, 1996; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 主文献直接定义 Pow(A;s)（a∈A、幂指数 >=s>=1），陈述倒数和及 gcd=1 的“if and only if”猜想，说明有限 A 时倒数和失败会导致上密度小于 1，并给出若干充分条件。论文还明确称 Σ(Pow({3,4,7};1)) 的最大遗漏整数为 581。
- [IMPAN record for Complete sequences of sets of integer powers](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/77/2/109048/complete-sequences-of-sets-of-integer-powers) — Institute of Mathematics, Polish Academy of Sciences, 1996; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 出版方记录核对作者、期刊 Acta Arithmetica 77 (1996)、页码 133--138、DOI 10.4064/aa-77-2-133-138，并提供开放下载。
- [Formal Conjectures — Erdős Problem 124](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/124.lean) — Formal Conjectures contributors, 2025; `formalization`, `formalized_artifact`, directness=`direct`, reliability=`high`. 形式化源将 P(d,k) 定义为有限互异幂和，并明确分列 erdos124.zero（标记 research solved）、erdos124.ne_zero（标记 research open）和 {3,4,7} 特例。该文件中这些 lemma 仍含 sorry，故它是精确 statement/status 映射，不是所列结论本身的可执行证明。
- [On certain positive integer sequences](https://www.rivmat.unipr.it/fulltext/2004-3s/pdf/16.pdf) — Giuseppe Melfi, 2004; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 直接证明对任意 epsilon>0 存在无限 A，使倒数和很小而 Pow(A;s) 对每个 s>=1 完备；论文明确说明这推翻的是无限 A 情形的 only-if，而有限集合问题仍开放。
- [lean-proofs — Erdos124b](https://github.com/plby/lean-proofs/blob/main/ErdosProblems/Erdos124b.md) — Boris Alexeev / plby, 2025; `formalization`, `formalized_artifact`, directness=`indirect`, reliability=`medium`. 论坛指向的具体证明工件。由于本次网页读取未能展开其源文本且未在本环境实际运行 Lean，因此只作为需人工复验的形式化证据链接，而不将其视作已独立审阅的证明。

### 完成标准

- 肯定出口: For the repaired BEGL target, prove that for every finite A={d_1,...,d_r} of distinct integers at least 3 with sum_i 1/(d_i-1)>=1 and gcd(A)=1, and every k>=1, there exists N(A,k) such that every n>=N(A,k) belongs to sum_i P(d_i,k).
- 否定出口: Give one explicit finite A and k>=1 satisfying d_i>=3, sum_i 1/(d_i-1)>=1, and gcd(A)=1, together with a rigorous proof that arbitrarily large integers are absent from sum_i P(d_i,k).

不构成完成：

- Pointing out that the uncorrected d_r-only input is vacuous; that audits the transcription but does not resolve the repaired conjecture.
- Reproving the k=0 theorem or invoking Brown's criterion without handling the missing low powers.
- Proving only s=k=1 for {3,4,7}, or another fixed family.
- Checking a finite interval without a proof that it covers an infinite tail.
- Working with infinitely many bases, a base set depending on n, or a condition stronger than the canonical reciprocal-sum hypothesis.
- Showing positive density, upper density one, or coverage of selected residue classes without eventual coverage of all integers.

正确性陷阱：

- First verify the repaired condition is sum_i 1/(d_i-1)>=1, not r/(d_r-1)>=1.
- Keep A finite and fixed; distinctness and the lower bound d_i>=3 must be retained.
- For k>=1, no term d_i^j with j<k may be introduced by a carry, correction, or auxiliary expansion.
- A proof must quantify N after A and k, then cover every integer n>=N.
- A counterexample requires unbounded omissions, not a finite list of gaps.
- Do not infer the high-power theorem from a k=0 proof: deleting finitely many summands can change a complete sequence.
- If using the c_i notation, explicitly account for 0 in P(d_i,k) or retain c_i throughout.

### 更新后的 AI 可解答性

- 等级: `low_to_medium_candidate`
- 分数: `24/100`
- 信心: `medium`
- 结论: 字面输入无需研究而是平凡空域；在明确修复到 BEGL 高幂目标后，这是可检验但长期未解的加性数论问题。AI 可有效参与文献/形式化核验、特例结构提取和严格反例证书搜索，但独立给出一般证明或反例的概率仍低。

支持理由：

- 修订目标有严格的全称量词、清晰的正反完成条件和明确的有限对象。
- BEGL96 提供多种充分条件、{3,4,7} 边界实例及必要性工具，适合把探索拆成可审计引理。
- gcd 和模障碍为反例路线提供精确的有限证书候选。

主要障碍：

- k=0 的简单 Brown 型论证依赖于 1；k>=1 失去低幂后不能直接套用。
- 需要统一任意有限 A、任意 k 及倒数和等号情形；有限计算无法推出尾部全覆盖。
- 现有已知结果多针对大而结构化的 base 集或极少数特例，缺少可直接推广的统一机制。
- 任何研究若未先修复 d_r 下标，将在空参数域上产生伪结论。

Proof-first 路线：

- 先审读 BEGL96 的 Theorem 1--3 及 {3,4,7} 论证，提炼高幂截断仍保留的结构性引理，而非把 k=0 证明机械缩放。
- 尝试建立严格的尾部拼接/残差吸收定理：用 gcd=1 控制低位残差，同时确保每个 base 的指数始终 >=k。
- 反向寻找无限遗漏不变量：对小的候选 A,k 先提出一个精确模数或自动机不变量，再证明其在所有更高指数下封闭。
- 只允许一个计算任务：固定 A,k,m 后计算可达残差或有限状态图；预先声明要证明的周期/不变量及停止条件，完成后立即转回证明。

需要验证：

- 人工运行或逐行审阅论坛所链 Erdos124b Lean 工件，确认其 imports、无 sorry、定理量词与 k=0 断言一致。
- 阅读 BEGL96 中关于 {3,4,7} 的完整论证，核实当前数据库所谓“proved it for {3,4,7}”是否覆盖所有 s=k>=1。
- 以 MathSciNet、zbMATH、Google Scholar 和作者主页补做 2023--2026 检索；本次公共网页/arXiv 定向检索非穷尽。
- 由问题维护者确认 d_r 公式是网页/转录错误，并把问题拆为 k=0 solved 与 k>=1 open。

### 审计限制与人工复核理由

- 虽然已直接阅读 BEGL96 与 Melfi 原文、当前问题页索引、论坛和 Formal Conjectures 源码，Erdős Problems 主页面在一次直接打开时返回 403；其内容由搜索索引和同站论坛/形式化记录交叉核对。
- 未实际运行 Alexeev/Aristotle 的 Lean 工件；因此仅把 k=0 的解决状态视为当前数据库和论坛的强直接记录，不宣称已独立复现 typecheck。
- 未逐页验证 BEGL96 对 {3,4,7} 是否给出任意 k>=1 的证明；原文直接可见的是 s=1 的最大遗漏数陈述，当前数据库的更广 special-case 标签需人工核对。
- 2023--2026 的公开检索覆盖精确题名、关键符号、问题号、论坛、形式化与 arXiv，但不等同于 MathSciNet、zbMATH、Google Scholar 与所有付费期刊的完全穷尽。
- 未使用任何其他仓库条目；结论仅基于用户给定问题 JSON 与公开网页/论文/形式化来源。

- 应由维护者修正输入/网页题面中的 d_r 下标，并将状态拆分为“字面式平凡、k=0 已解、修复后的 k>=1 开放”。
- 应独立运行或审读 Erdos124b Lean 工件，避免将论坛所述 formalization 与含 sorry 的 Formal Conjectures statement 文件混淆。
- 应从 BEGL96 原文或作者/数据库核实 {3,4,7} 特例的完整 k 范围。
- 建议用 MathSciNet、zbMATH、Google Scholar 和相关作者主页补做最近三年的人工检索。

<!-- DEEP_REVIEW:END -->
