# Problem 1

## 基本信息

- 原始链接: https://www.erdosproblems.com/1
- LaTeX 页面: https://www.erdosproblems.com/latex/1
- 原始状态: `open`
- 奖金: `$500`
- 主类别: `number theory`
- 原始标签: `number theory`, `additive combinatorics`
- 形式化状态: `yes`
- OEIS: `A276661`
- 原站备注字段: 无

## 原问题

If $A\subseteq \{1,\ldots,N\}$ with $\lvert A\rvert=n$ is such that the subset sums $\sum_{a\in S}a$ are distinct for all $S\subseteq A$ then\[N \gg 2^{n}.\]

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `23/100`
- 建议路线: 优先文献定位、特殊情形、数值实验和辅助引理搜索；完整证明需要新的数学思想。

## 判断依据

### 有利因素

- 已有形式化陈述，可降低语义误读风险
- 存在 OEIS 数据入口，利于实验与反例搜索

### 主要障碍

- 所属标签偏证明密集：additive combinatorics, number theory
- 题面含渐近/无限对象线索：\gg, for all large, o(
- 原记录含奖金 $500，说明该题被长期视为高价值难题；这不是否定依据，但提高验证门槛。
- 缺少明显有限搜索入口。

### 公开版思考过程摘要

- 先识别问题类型：无限/渐近或抽象证明倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: additive combinatorics, number theory
- 有限/计算线索: 无
- 渐近/无限线索: \gg, for all large, o(
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **低到中等候选。GPT-5.5 级别模型配合计算、形式化证明和文献检索工具，较可能复现、形式化并局部扩展现有下界方法，也可能推进小规模极值数据和反例/构造搜索；但要证明完整的 N \gg 2^n，需要跨越当前最佳 N\geq binom(n,floor n/2) 约等于 2^n/sqrt(n) 到常数倍 2^n 的根本缺口，完成概率偏低。**
- 等级: `low_to_medium_candidate`
- 分数: `32/100`
- 信心: `medium`
- 可能路线: 最现实路线是把问题转化为 [1,x] 中 dissociated 集合大小 F(x)<log_2 x+O(1)，先用形式化系统复核 DFX21 型精确二项式下界和实数间隔推广，再结合 SAT/ILP/CP-SAT 搜索 A276661 小 n 极值结构，提取候选稳定结构或禁用模式。若要尝试真正推进，应围绕熵压缩、Littlewood-Offord 型反集中、加法能量、压缩/移位、容器法或编码论观点寻找能排除 sqrt(n) 损失的新不变量。

### 支持理由

- 问题陈述短、对象离散、形式化状态为 yes，适合 proof assistant 复核定义、等价命题和已知定理链。
- 现有最佳下界是精确的 N\geq binom(n,floor n/2)，给 AI 一个清晰的可验证基线；可先检查是否有可局部强化的步骤。
- 子集和互异等价于无非平凡 {-1,0,1} 线性关系，适合用 SAT、整数规划、回溯和剪枝搜索小 n 极值例子。
- OEIS 序列和已有上界构造可为计算实验提供目标数据，用于发现结构、测试猜想和排除错误证明。
- 实数版本也被提到，说明问题有几何/间隔解释，可能允许 AI 在多个表述间迁移证明工具。

### 主要障碍

- 目标下界比当前 2^n/sqrt(n) 级别强一个 sqrt(n) 因子，不是简单常数优化。
- 已知中心二项式下界通常来自中层子集和计数/反链思想；要达到 2^n 级别，需要利用远超中层的全局结构。
- 上界已有约 0.22002*2^n 的构造，说明若命题为真，正确常数和极值结构可能很精细。
- 纯计算只能覆盖小 n，无法直接证明渐近 O(1) 级别的 F(x)-log_2 x 上界。
- AI 生成的组合证明很容易隐藏量词错误、边界损失或把平均情形误当最坏情形，必须强验证。

### 需要的验证

- 形式化核验：确认 dissociated、subset sums distinct、N\gg 2^n 与 F(x)<log_2 x+O(1) 的等价转换没有边界项错误。
- 复现基线：在 Lean/Isabelle 或类似系统中复核 N\geq binom(n,floor n/2) 的证明关键步骤。
- 计算验证：用独立 SAT/ILP/回溯程序重算小 n minimal N，并与 A276661 对齐。
- 候选引理压力测试：对任何 AI 提出的强化不等式，自动搜索小规模反例并检查是否被 Bohman/Conway-Guy 类型构造击穿。
- 文献检索：只在使用本题给出的参考线索时，核对 DFX21、Bohman、Elkies-Gleason 等结果的精确定理陈述和适用范围。

### 公开版思考摘要

这是一个表述极简但缺口很硬的加性组合问题。AI 的优势在于把多个等价表述、形式化证明、有限搜索和已知证明路线连接起来，发现局部错误或提出可检验猜想；短期最有价值成果可能是形式化已知最佳下界、扩大极值计算、或发现新的结构性必要条件。完整解决需要新的全局论证来消除 sqrt(n) 损失，因此不宜评为高候选。

### 免责声明

以上是对 GPT-5.5 级别模型辅助研究可行性的审查，不是该 Erdős 问题的证明，也未声称给出新的下界或构造。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `confirmed_open`
- 状态信心: `high`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_1.md](../../prompts/problem_1.md)

### 状态结论

原命题可按标准 Vinogradov 记号明确化，且仍为公开的未解问题。DFX 的同行评审结果给出精确下界 N≥C(n,⌊n/2⌋)，即 (√(2/π)-o(1))2^n/√n；尚未消除 √n 损失。2025 年 Bado 的非同行评审“解决”声称不能计作结论：其文中由逐个集合的正性推出全体可容许集合上一致正下界，逻辑不成立；该作者 2026 年后续稿也明确将获得 Erdős 界所需部分列为尚待证明。

### 当前规范陈述

证明存在绝对常数 c>0，使得对任意整数 n≥1、N≥1 及任意 n 元集合 A⊆{1,…,N}，若映射 S↦∑_{a∈S}a 在 A 的全部子集上单射（等价地，任意不同 S,T⊆A 的子集和不同），则 N≥c·2^n。等价地，令 m(n) 为所有 n 元、子集和两两不同的正整数集合 A 的 max A 的最小值，证明 m(n)=Ω(2^n)。

```text
There exists an absolute constant c>0 such that for every integer n>=1, every integer N>=1, and every n-element set A⊆{1,...,N}, if the subset-sum map S↦∑_{a∈S}a is injective on 2^A (equivalently, ∑_{a∈S}a≠∑_{a∈T}a for all distinct S,T⊆A), then N>=c·2^n. Equivalently, with m(n):=min{max A: A⊂Z_{>0}, |A|=n, and A has pairwise distinct subset sums}, prove m(n)=Ω(2^n).
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 未发现能否定字面命题的简单构造。2 的幂给出 max A=2^{n-1}，与命题相容；任一固定 n 的例子也不能否定绝对常数型渐近断言。已核查的有限精确值和 Conway–Guy/Bohman 构造同样不构成反例。
- 版本变化: 未发现原题被后来修正、分裂或取代。已知发展是下界常数的改进、DFX 的精确二项式下界、Conway–Guy 的更强精确猜想、实数 1-分离变体，以及 2025 年解决模 N 变体的工作；这些都不解决整数原题。2025 年有未经同行评审的完整解决声称，但其关键统一下界推论无效，且同作者 2026 年文本将关键解析步骤重新表述为未解决障碍。

陈述问题：

- 原句的 “N ≫ 2^n” 未把隐含常数及其量词写出；规范解释为存在与 n、N、A 无关的绝对 c>0。
- 原句没有说明是否只要求充分大的 n；这与上述全称版本等价：若一个绝对下界仅对充分大 n 成立，可调小 c 以吸收有限多个小 n。
- N 只是 A 所在区间的上界；因 A⊆{1,…,N}，可无损地取 N=max A。
- “F(2^k)=k+2”是 Conway–Guy 提出的更强的精确渐近猜想，并非本题 N≫2^n 的同义改写。实数、1-分离的版本也是另一变体。

需要固定的量词/约定：

- The implicit constant c in N≫2^n must be absolute: it cannot depend on n, N, or A.
- All subset pairs are quantified: S,T range over 2^A, and equality is forbidden whenever S≠T; the empty subset is included.
- N,n are positive integers. The formulation with all n>=1 is equivalent to an eventual asymptotic formulation after decreasing c if necessary.
- A counterexample to the conjecture must be a sequence A_j with |A_j|→∞ and max(A_j)/2^{|A_j|}→0, not one finite admissible set.

### 文献与当前边界

已核验的主要结果：

- 令 m(n)=min max A。平凡计数给 m(n)≥(2^n-1)/n；Erdős–Moser 给出数量级 2^n/√n 的下界。
- Dubroff、Fox、Xu（2021，同行评审）证明精确不等式 m(n)≥C(n,⌊n/2⌋)=(√(2/π)-o(1))2^n/√n。其一证明使用 Berry–Esseen 正态近似，另一证明使用 Harper 超立方体顶点等周不等式。
- Steinerberger（2023，同行评审）给出同一最佳下界的傅里叶积分/随机游走证明，并扩展到正实数且子集和 1-分离的变体。
- Conway–Guy 及 Bohman 的构造给 m(n)≤(0.22002+o(1))2^n；这说明目标的指数尺度正确，却留下 √n 因子的本质缺口。
- Cambie、Gao、Kim、Liu（2025，同行评审）解决了一个模 2^n+t 的变体，并在该变体中确定最佳常数 1/3；该结论不能直接转移到整数区间模型。

最近相关工作：截至审计日，直接针对原题的最新显著材料包括 Bado 的 2025 非审稿“解决”声称及其 2026 后续非审稿说明。前者有可定位的统一性逻辑缺口，后者明确保留得到 Erdős 界所需的解析障碍；因此它们不更新已验证最佳界。2025 年同行评审的模版本是最新已验证的紧邻变体进展。

剩余核心：证明或否定存在统一 c>0 使 m(n)≥c2^n。已知的 DFX/Steinerberger 论证只强制 m(n)≳2^n/√n；必须取得利用“全部子集和互异”的额外全局刚性，以消除 √n 损失，或构造一列 m(n)/2^n→0 的反例。

已使用方法：

- 随机符号和的二阶矩、方差与集中估计。
- Berry–Esseen/局部正态近似及格点奇偶性。
- 超立方体的 Harper 顶点等周不等式。
- 傅里叶积分、Parseval、余弦乘积和随机游走解释。
- Conway–Guy 型递归构造与 Bohman 的 sum-packing 构造。
- 模子集和的结构分析；该路线已有强变体结果，但尚未桥接回原问题。

争议或不确定性：

- 2025 年 Bado 文本声称解决，但不是同行评审结果；直接检查到的逐点正性→一致正性步骤无效，故不能作为解答。
- 网络检索不能逻辑证明不存在未索引的新证明；但已核查当前数据库、论坛、arXiv、期刊页面、OEIS、作者相关页面和该解决声称，未发现可接受的解决。
- 数据库的“Formalised statement? Yes”应理解为陈述已有 Lean 编码；所能访问的页面仍要求替换 sorry，不能理解为主猜想已有核验的 Lean 证明。

### 证据来源

- [Erdős Problem #1](https://www.erdosproblems.com/1) — Thomas F. Bloom / Erdős Problems contributors, 2026-01-23; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 当前数据库将本题标为 open，给出 DFX 下界、Bohman 构造、实数变体及 dissociated-set 等价表述；数据库亦提醒其状态不是文献完备性的证明。
- [LaTeX source for Erdős Problem #1](https://www.erdosproblems.com/latex/1) — Thomas F. Bloom / Erdős Problems contributors, 2026-01-23; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 直接提供本题的原始陈述、参考文献及“F(x)<log_2 x+O(1)”等价表述。
- [Erdős Problem #1 discussion thread](https://www.erdosproblems.com/forum/discuss/1) — Thomas F. Bloom and forum contributors, 2026-01-23; `forum`, `informal_claim`, directness=`direct`, reliability=`medium`. 页面仍标为 OPEN；讨论明确解释 ≫ 表示绝对常数，固定有限例子不能反驳该问题，并记录截至 2026 年 1 月的 DFX 注释。
- [A note on the Erdős distinct subset sums problem](https://arxiv.org/abs/2006.12988) — Quentin Dubroff, Jacob Fox, Max Wenqiang Xu, 2020-06-20; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 给出两种证明；第二种结合 Harper 顶点等周不等式推出 a_n≥C(n,⌊n/2⌋)，从而得到 (√(2/π)-o(1))2^n/√n。文中还说明 Bohman 的构造上界 0.22002·2^n。
- [A Note on the Erdős Distinct Subset Sums Problem](https://doi.org/10.1137/20M1385883) — Quentin Dubroff, Jacob Fox, Max Wenqiang Xu, 2021; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. DFX 结果的同行评审发表版本：SIAM Journal on Discrete Mathematics 35(1), 322–324。
- [Some remarks on the Erdős distinct subset sums problem](https://par.nsf.gov/biblio/10528280-some-remarks-erdos-distinct-subset-sums-problem) — Stefan Steinerberger, 2023-09-01; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 证明傅里叶积分/随机游走表述，并给出当前最佳渐近下界的另一证明；未解决消除 √n 因子的问题。
- [A sum packing problem of Erdős and the Conway–Guy sequence](https://doi.org/10.1090/S0002-9939-96-03653-2) — Tom Bohman, 1996; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 构造具有不同子集和的集合，给出 m(n)<0.22002·2^n 的上界；因此它支持而非否定猜想。
- [The Erdős distinct subset sums problem in a modular setting](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/en/publishing-house/journals-and-series/acta-arithmetica/all/217/4/115883/the-erdos-distinct-subset-sums-problem-in-a-modular-setting) — Stijn Cambie, Jun Gao, Younjin Kim, Hong Liu, 2025-02-06; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 解决模 N=2^n+t 的不同子集和变体：max A≥(1/3-o(1))N，且该变体常数 1/3 最优；不蕴含整数原题。
- [A276661: least endpoint for n-element distinct-subset-sum sets](https://oeis.org/A276661) — OEIS Foundation and contributors, 2026-06-12; `oeis`, `database_record`, directness=`direct`, reliability=`medium`. 定义 m(n) 的整数序列并列出 n≤10 的值以及相关文献和构造；有限数据不决定渐近问题。
- [Erdős Problem Bounty Platform: Problem 1](https://mathbounty.com/problems/1) — MathBounty, 2026; `formalization`, `formalized_artifact`, directness=`direct`, reliability=`medium`. 显示与规范量词相符的 Lean 4 目标定理。页面要求用完整证明替换 sorry，故这只能证明陈述已编码，不能证明猜想已经形式化解决。
- [A Resolution of Erdős's Distinct Subset Sums Conjecture via the Circle Method](https://www.researchgate.net/publication/392862783_A_RESOLUTION_OF_ERDOS%27S_DISTINCT_SUBSET_SUMS_CONJECTURE_VIA_THE_CIRCLE_METHOD) — Idriss Olivier Bado, 2025-06; `preprint`, `informal_claim`, directness=`direct`, reliability=`low`. 提出完整解决声称，但非同行评审。所示 Lemma 3.12 仅从每个 A 的 k(A)>0 推出存在统一 z>0；该推论不成立，因为逐点正性不排除 inf_A k(A)=0。
- [Fourier Rigidity and Modular Structure of Sum-Distinct Sets](https://www.researchgate.net/publication/405215338_FOURIER_RIGIDITY_AND_MODULAR_STRUCTURE_OF_SUM-DISTINCT_SETS) — Idriss Olivier Bado, 2026-05-24; `preprint`, `informal_claim`, directness=`direct`, reliability=`medium`. 同作者的后续未审稿文本明确说其目标是分离无条件可证内容与“仍需证明”才能得到 Erdős 界的内容；这与把 2025 稿视为已接受解决不相容。

### 完成标准

- 肯定出口: Prove, with an absolute explicit or non-explicit constant c>0, that every positive-integer n-element set A with pairwise distinct subset sums satisfies max(A)>=c·2^n. The proof must make c independent of n and must establish the assertion for all sufficiently large n (or all n after a finite adjustment).
- 否定出口: Construct and rigorously verify a sequence of positive-integer sum-distinct sets A_j with |A_j|→∞ and max(A_j)/2^{|A_j|}→0. This is equivalent to showing that no absolute c>0 can satisfy the asserted lower bound.

不构成完成：

- Reproving or marginally improving m(n)>=Theta(2^n/sqrt(n)) without removing the sqrt(n) factor.
- A result only for powers of two, a restricted 2-adic/modular class, random sets, real separated sets, or subset sums modulo N, unless it is rigorously transferred to every integer sum-distinct set.
- Any finite table of m(n), a heuristic computation, or one finite construction.
- An argument whose implied constant depends on n, on A, or on an auxiliary parameter that grows with n.
- A formal file that states the theorem but retains sorry, axioms equivalent to the target, or an unproved uniformity lemma.

正确性陷阱：

- Check injectivity for every pair of subsets, including unequal-cardinality pairs; equivalently, forbid every nonzero {-1,0,1}-relation among elements of A.
- Do not confuse the ambient endpoint N with max(A); reduction to N=max(A) is valid, but all quantifiers and constants must remain uniform.
- Track lattice spacing and parity carefully in probabilistic/local-limit arguments.
- An estimate holding for each fixed A does not automatically give a uniform positive lower bound over all n-element A.
- Do not infer the integer theorem from a modular or real-variable variant without a stated, proved transfer theorem.
- A finite computation cannot establish or refute this asymptotic uniform-constant claim.

### 更新后的 AI 可解答性

- 等级: `low_candidate`
- 分数: `12/100`
- 信心: `high`
- 结论: 这是定义严谨、可证伪且有强技术背景的开放问题，但核心 √n 缺口已长期抵抗多种方法；作为 AI 独立攻关目标，成功概率低。

支持理由：

- 目标、反例形式及等价极值函数都清楚，允许对候选引理进行精确审计。
- 已有 DFX、Steinerberger、模变体和构造工作提供可复用的基线与明确瓶颈。
- 存在可机器核验的有限构造、反例证书和辅助引理，但它们只能服务于具体证明问题。

主要障碍：

- 需要把当前最佳 2^n/√n 下界提升一个 √n 因子，非局部的主难点尚未被任何已验证方法克服。
- 现有正态近似、等周和傅里叶框架都自然产生 √n 尺度；不能把常数改进误当作指数尺度突破。
- 非同行评审的“解决”材料显示，统一性、极限交换和主弧覆盖是高度易错点。

Proof-first 路线：

- 首先隔离一个可独立证明且足以消除 √n 损失的结构引理，例如关于小球中符号和数量、模结构或非高斯性的统一二择。
- 对 DFX 两条证明逐行定位 √n 出现的唯一不可逆步骤，并寻找能使用全体 {-1,0,1}-关系禁绝条件强化它的命题。
- 将已解决的模版本视为结构启发，而非可直接引用的原题证明；任何提升必须显式给出从模信息到整数全局下界的桥接。

需要验证：

- 对任何声称的突破，优先检查常数是否独立于 n，以及逐点界是否被错误升级为一致界。
- 核查所有 Fourier/圆法主弧覆盖、重叠与误差项是否统一于 A 和 n。
- 若有形式化尝试，审计最终 Lean 定理是否忠实表达全称 c、N、A 和子集和单射，且无 sorry 或目标等价公理。

### 审计限制与人工复核理由

- 直接打开 Erdős Problems 主页面时遇到抓取 403，但其搜索索引、LaTeX 页面和专属论坛线程均可读取；结论未仅依赖数据库标签。
- 检索覆盖了原句、作者、DFX、近期 arXiv、期刊、OEIS、形式化入口、论坛及 2025 解决声称；这不能逻辑证明全球不存在未索引的新结果。
- 对 Bado 的解决声称作了针对性文本审计，定位到足以使其不构成证明的统一性缺口；未声称对其全部非核心引理作出了完整同行评审。
- 可访问的 Lean 平台证据只确认陈述编码和待填证明目标，不能据此推断已有完整形式化证明。

- 存在 2025 年未审稿的完整解决声称，虽已定位关键逻辑缺口，若要作公开的“彻底排除”声明仍宜由该领域专家复核。
- 当前开放状态基于强而非逻辑完备的文献搜索；对任何 2026 年 7 月后发布或未被索引的工作应重新检索。
- 若后续研究使用 Bado 的任何部分性引理或模变体桥接，需独立审计其量词、统一性和适用范围。

<!-- DEEP_REVIEW:END -->
