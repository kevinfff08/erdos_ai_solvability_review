# Problem 1005

## 基本信息

- 原始链接: https://www.erdosproblems.com/1005
- LaTeX 页面: https://www.erdosproblems.com/latex/1005
- 原始状态: `open`
- 奖金: `no`
- 主类别: `number theory`
- 原始标签: `number theory`
- 形式化状态: `no`
- OEIS: `A386893`
- 原站备注字段: 无

## 原问题

Let $\frac{a_1}{b_1},\frac{a_2}{b_2},\ldots$ be the Farey fractions of order $n\geq 4$. Let $f(n)$ be the largest integer such that if $1\leq k<l\leq k+f(n)$ then $\frac{a_k}{b_k}$ and $\frac{a_l}{b_l}$ are similarly ordered - in other words,\[(a_k-a_l)(b_k-b_l)\geq 0.\]Estimate $f(n)$ - in particular, is there a constant $c>0$ such that $f(n)=(c+o(1))n$ for all large $n$?

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `24/100`
- 建议路线: 优先文献定位、特殊情形、数值实验和辅助引理搜索；完整证明需要新的数学思想。

## 判断依据

### 有利因素

- 存在 OEIS 数据入口，利于实验与反例搜索

### 主要障碍

- 所属标签偏证明密集：number theory
- 题面含渐近/无限对象线索：\gg, for all large, o(
- 缺少明显有限搜索入口。

### 公开版思考过程摘要

- 先识别问题类型：无限/渐近或抽象证明倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: number theory
- 有限/计算线索: 无
- 渐近/无限线索: \gg, for all large, o(
- 构造/存在性线索: is there

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5 with computation/formalization/literature tools`
- 结论: **这是一个中高潜力推进题，但不应判为可直接完整解决的高把握题。给定摘要已经有线性下界和线性上界，且核心对象是可计算的 Farey 序列局部排列问题；GPT-5.5 级别模型很可能能通过大规模枚举、极值结构猜测、几何/格点化重述和形式化验证，显著推进常数 c 的候选值或验证上界最优性相关命题。不过，要证明精确渐近常数，仍需要新的均匀结构定理，难度明显高于纯计算归纳。**
- 等级: `medium_candidate`
- 分数: `72/100`
- 信心: `medium`
- 可能路线: 较可能的路线是把 Farey 序列中索引相近的分数对转化为关于相邻 Farey 递推、连续分母对或可见格点路径的局部约束问题；先用精确枚举计算 f(n)/n 的数值极限行为，搜索达到上界约 n/4 的极值构型，再尝试证明这些构型给出下界，并把任意更长窗口必然含有一个非 similarly ordered 对的问题化为格点区域、连分数块或 Ford 圆邻接结构中的覆盖/间隔引理。形式化证明工具可用于验证递推、窗口性质和有限边界情形；计算可用于发现常数和反例模式。

### 支持理由

- 问题对象离散、有限且可精确生成：Farey fractions of order n、索引窗口和不等式条件都适合程序枚举与反例搜索。
- 已有结果给出线性量级，并且摘要中已经把范围缩到 (1/12-o(1))n 与 n/4+O(1) 之间，说明目标不是从零证明增长阶，而是聚焦常数和极值结构。
- 上界被 conjecture 为最优，AI 工具可以系统搜索接近 n/4 的构型，生成可检验的候选族，再反推证明所需的参数化结构。
- OEIS 条目存在，说明已有初值或计算数据可能可用于校验程序实现和猜测趋势，尽管本次判断不依赖外部条目内容。
- 该题没有显式依赖高深不可计算对象；计算、符号推导和有限情形证明可以直接服务于主问题。

### 主要障碍

- 精确渐近常数需要控制所有 Farey 局部窗口，而不是只构造大窗口；全局排序与局部分母/分子单调性的相互作用可能很复杂。
- 从数值发现到严格证明存在典型鸿沟：即使 f(n)/n 看似趋向 1/4，也需要证明任意长度超过 n/4+O(1) 的窗口必然失败，且误差项要足够均匀。
- Farey 序列的局部结构受互素性、连分数展开和边界效应共同影响，AI 可能容易提出漂亮但只适用于特殊子族的论证。
- 如果真实极限常数不是 1/4，单靠有限枚举可能被慢收敛或特殊 n 的构型误导。
- 形式化证明可验证局部引理，但主定理可能需要创造性的解析数论或几何数论估计，当前模型未必能独立完成。

### 需要的验证

- 实现独立的 Farey 序列生成与 f(n) 精确计算，并与已知初值或 OEIS A386893 数据交叉校验。
- 对较大 n 统计 f(n)/n、极值窗口位置、端点分母/分子模式，检查是否稳定接近 1/4 或存在其他候选常数。
- 自动搜索达到或接近上界的参数化窗口族，并验证其能给出无限多 n 或所有大 n 的下界。
- 把候选上界证明拆成可机器检查的局部引理，例如相邻 Farey 递推、窗口中必然出现分子增而分母降的对、边界修正项等。
- 对小 n 和过渡区间做穷举认证，避免渐近证明遗漏有限异常。

### 公开版思考摘要

该题适合 AI 工具链的原因是定义清楚、可计算、已有线性上下界且常数区间较窄。最现实的贡献不是立即给出完整闭合证明，而是通过精确枚举和结构发现，把 conjectured 上界最优性转化为明确的构造族和若干可验证引理。如果计算强烈支持 1/4，并能提炼出统一构型，GPT-5.5 有机会给出可发表级别的部分进展；但要无漏洞地证明 f(n)=(1/4+o(1))n 或给出其他精确常数，仍属中等偏高风险。

### 免责声明

以上是对 GPT-5.5 级别模型辅助研究可行性的评估，不是该 Erdős 问题的解答，也不声称已经证明 f(n) 的渐近常数。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `likely_open`
- 状态信心: `medium`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_1005.md](../../prompts/problem_1005.md)

### 状态结论

截至 2026-07-27，原问题仍很可能开放。Erdős Problems 当前页仍标为 OPEN，且页面显示没有评论中的解答主张；2025 年 van Doorn 的可检查 arXiv v1 给出严格改进的下界和显式上界，并明确提出精确公式猜想，而非声称解决。对精确题名、作者、arXiv 和 2026 年后续工作的定向检索未发现可核查的解决或反例。置信度只能为中等：开放性的负面检索不能证明不存在未索引结果，且最新关键结果尚为预印本。

### 当前规范陈述

对整数 n >= 4，令 F_n=(a_1/b_1,...,a_{N_n}/b_{N_n}) 为 n 阶 Farey 序列：它由区间 [0,1] 内所有既约分数 a/b（0 <= a <= b <= n，gcd(a,b)=1）按数值严格递增排列而成，并包含 0/1 与 1/1。两个既约分数 a/b、c/d 称为“同序”，若 (a-c)(b-d) >= 0。定义 f(n) 为最大的整数 m >= 0，使得对任意满足 1 <= k < l <= N_n 且 l-k <= m 的指标对，a_k/b_k 与 a_l/b_l 都同序。求 f(n) 的渐近行为；特别地，判定极限 lim_{n->infinity} f(n)/n 是否存在且为正数。当前更强的猜想是：对每个 n >= 92，f(n)=floor(n/4)+d_n，其中当 n 分别模 4 同余 0、1、2、3 时，d_n 分别为 1、2、2、4。

```text
For an integer n >= 4, let F_n=(a_1/b_1,...,a_{N_n}/b_{N_n}) be the finite Farey sequence of order n: all reduced fractions a/b in [0,1] with 0 <= a <= b <= n and gcd(a,b)=1, listed in strictly increasing numerical order (including 0/1 and 1/1). Two displayed reduced fractions a/b and c/d are similarly ordered when (a-c)(b-d) >= 0. Define f(n) to be the largest integer m >= 0 such that, for every pair of indices 1 <= k < l <= N_n with l-k <= m, the fractions a_k/b_k and a_l/b_l are similarly ordered. Determine the asymptotic behaviour of f(n), in particular decide whether the limit lim_{n->infinity} f(n)/n exists and is a positive constant. The sharper current conjecture is that for every n >= 92, f(n)=floor(n/4)+d_n, where d_n=1,2,2,4 respectively for n congruent to 0,1,2,3 modulo 4.
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 未发现能推翻经标准 Farey 约定补全后的字面命题的简单构造。反而 n=4 的直接例子表明定义正常：F_4 中 1/4 与 2/3 不同序，二者之间有两个项，因此 f(4)=2。该核查不构成对所有潜在转录问题的穷尽证明。
- 版本变化: 1942 年 Mayer 首先得到 f(n) 的发散性；1943 年 Erdős 证明线性下界。2025 年 van Doorn 将下界提高到 (1/12-o(1))n，并给出带模 4 常数项的显式上界。该工作没有修正或取代原问题，而是把原本宽泛的“估计”细化为一个逐 n 精确公式猜想；原问题的“是否存在渐近常数”仍未解决。

陈述问题：

- 原文没有把 Farey 序列的端点约定、既约表示和有限索引上界 l<=N_n 写明；按标准 Farey 序列约定及文献上下文可唯一补足。
- 原文的“Estimate f(n)”本身不是唯一可判定的完成标准；其后明确的“是否存在 c”是可判定子问题，而 2025 年论文又提出了严格更强的逐 n 精确公式猜想。
- 条件“l<=k+f(n)”若脱离隐含的 l<=N_n 会引用未定义的 a_l/b_l；规范表述必须同时限制 l<=N_n。
- n>=4 是实质性边界：此时才存在不同序的一对，从而最大整数定义非空且有界。

需要固定的量词/约定：

- The universal condition ranges over all valid index pairs 1 <= k < l <= N_n, not merely consecutive fractions.
- The distance condition is l-k <= m; a single non-similarly-ordered pair at distance d proves only f(n) <= d-1.
- All fractions are represented in lowest terms, so numerator and denominator are uniquely specified.
- The asymptotic notation means a statement as n tends to infinity through all positive integers n >= 4, not along a subsequence.

### 文献与当前边界

已核验的主要结果：

- Mayer（1942，同行评审）首先研究该量；据 van Doorn 对原文献的回顾，先证明 n>=5 时 f(n)>=3，随后证明 f(n)->infinity。
- Erdős（1943，同行评审）证明存在绝对 c>0，使 f(n)>cn；直接审阅的原文提出了该常数的最优化问题。van Doorn 复核其论证可取 c=1/400。
- Zaharescu（2006，同行评审）及 Meng–Zaharescu（2014，同行评审）研究线性形式/多变量推广；这些不是原 f(n) 的精确渐近解。
- van Doorn（2025，arXiv v1，非同行评审）证明 f(n)>=(n/12)(1-4n^(-1/3))，并对每个 n>=4 证明 f(n)<=floor(n/4)+d_n，其中 d_n 按 n mod 4 为 1,2,2,4。

最近相关工作：最相关且检索到的最新工作是 Wouter van Doorn 的 arXiv:2509.00121 v1（2025-08-28；arXiv 页面只列 v1）。该文提出 n>=92 时 f(n)=floor(n/4)+d_n 的猜想，报告验证至 5000；截至本审计日期，未找到其期刊定稿、后续修订版或能替代该猜想的 2026 年解答。

剩余核心：原始可判定核心是：f(n)/n 是否在全体 n->infinity 时收敛于正数。更尖锐且目前最自然的剩余目标是证明或反驳 van Doorn 的逐 n 精确公式；若证明该公式，则原问题以 c=1/4 获肯定解。现有 1/12 与 1/4 之间的线性常数缺口仍很大。

已使用方法：

- Farey 相邻项判据 bc-ad=1 与 n<b+d，用于显式构造距离约 n/4 的不同序项。
- 围绕小分母 Farey 分数的局部参数化，以及对跨越该分数的项进行同序性控制。
- Farey 分数局部计数/差异界（van Doorn 引用 Dress），结合相邻间隙 1/(b_i b_{i+1}) 的求和。
- 按小分母与大分母拆分区间，并以倒数和控制小分母贡献，得到 1/12 下界。

争议或不确定性：

- 2025 年关键改进是公开可读预印本，但未发现同行评审定稿；本审计读取了其证明与定理陈述，未作逐行形式化验证。
- “没有找到 2026 年解决”只是有针对性的检索结果，不排除未索引、不同术语或尚未公开的工作。
- 数据库、OEIS 与预印本一致地将精确公式作为猜想；没有发现相互冲突的解答主张。

### 证据来源

- [Erdős Problem 1005](https://www.erdosproblems.com/1005) — Thomas F. Bloom (database page), date unknown; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 当前页面标记为 OPEN，记录 Mayer、Erdős 与 van Doorn 的结果，且页面显示该题没有评论中的部分或完整解答主张、未形式化。数据库也明确提醒状态只是维护者的当前信念，不能替代文献核查。
- [LaTeX source for Erdős Problem 1005](https://www.erdosproblems.com/latex/1005) — Thomas F. Bloom (database page), date unknown; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 核对了输入转录的原始问题文字、n>=4 边界、参考文献以及数据库所列的 2025 上下界。
- [Improved bounds for the Mayer-Erdős phenomenon on similarly ordered Farey fractions](https://arxiv.org/abs/2509.00121) — Wouter van Doorn, 2025-08-28; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 可检查的 v1 证明：对所有 n>=4，f(n)<=floor(n/4)+d（d=1,2,2,4 取决于 n mod 4）；并证明 f(n)>=(n/12)(1-4/n^(1/3))。论文提出 n>=92 时上述上界取等的猜想，且只报告计算至 n<=5000，未声称解决。
- [HTML full text of van Doorn's preprint](https://arxiv.org/html/2509.00121v1) — Wouter van Doorn, 2025-08-28; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 用于直接审阅定义、精确上界构造、下界定理、猜想的量词与有限计算范围；该版本为 arXiv v1。
- [A Note on Farey Series](https://academic.oup.com/qjmath/article/os-14/1/82/1578311) — P. Erdős, 1943-01-01; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 给出 Erdős 1943 论文的正式书目信息。
- [A Note on Farey Series](https://www.renyi.hu/~p_erdos/1943-01.pdf) — P. Erdős, 1943-01-01; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 直接可读的原文定理证明存在绝对常数 c，使 n>ck 时相隔 k 的 Farey 项同序；文中还说明未找到最优常数。
- [A Mean Value Theorem Concerning Farey Series](https://academic.oup.com/qjmath/article-abstract/os-13/1/48/1520920) — A. E. Mayer, 1942-01-01; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 确认 Mayer 的原始论文、作者、期刊、卷页与年份；2025 年论文将其结果概述为先得 f(n)>=3（n>=5），后续另一篇 Mayer 论文证明 f(n)->infinity。
- [The Mayer-Erdős phenomenon](https://www.sciencedirect.com/science/article/pii/S0019357706800121) — Alexandru Zaharescu, 2006-03-27; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 确认该现象有 2006 年同行评审研究；2025 年预印本将其描述为对任意线性形式的推广，而不是对本原始 f(n) 的更强常数改进。
- [A multivariable Mayer-Erdős phenomenon](https://experts.illinois.edu/en/publications/a-multivariable-mayer-erdos-phenomenon) — Xianchang Meng and Alexandru Zaharescu, 2014; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 确认 2014 年多变量推广的同行评审书目信息及其为推广工作，而非本题精确渐近的解决。
- [A386893](https://oeis.org/A386893) — Wouter van Doorn (sequence author), 2025-09-03; `oeis`, `database_record`, directness=`indirect`, reliability=`medium`. 独立数据库记录给出该函数的小 n 值、2025 上下界及同一精确公式猜想；其本身不是证明来源。

### 完成标准

- 肯定出口: For the original explicit subquestion: prove that there is a real c>0 such that lim_{n->infinity} f(n)/n=c, with all Farey-sequence conventions stated. A stronger affirmative resolution is a proof that f(n)=floor(n/4)+d_n for every n>=92, where d_n is 1,2,2,4 for residues 0,1,2,3 modulo 4; this implies c=1/4.
- 否定出口: Disprove the asymptotic-constant question by proving that f(n)/n has no limit (for example, by rigorously separating its liminf and limsup), or disprove the sharper conjecture by giving a specific n>=92 with an exact certified value of f(n) different from floor(n/4)+d_n. A proposed counterexample must enumerate or certify the relevant Farey indices and show the defining universal condition fails or holds as claimed.

不构成完成：

- Checking the conjecture for any finite range, including extending n<=5000 computations.
- Only reproducing the known (1/12-o(1))n lower bound or n/4+O(1) upper bound.
- Proving a limit along one subsequence, or proving merely limsup f(n)/n<=1/4.
- Producing a different non-similarly-ordered pair without proving it improves the existing upper bound or refutes the exact residue-class formula.
- A proof confined to pairs on one side of 1/2, unless it also establishes the required global universal statement.

正确性陷阱：

- Quantify over every valid pair of Farey indices, not just adjacent pairs or a chosen local segment.
- Use reduced numerator-denominator representatives and include the endpoints consistently.
- Translate a bad pair at distance d correctly: it yields f(n)<=d-1, not f(n)<=d.
- Track the strict/non-strict convention: similarly ordered means product >=0; non-similarly ordered means product <0.
- Do not replace all-n asymptotics by a subsequence statement, and account for the four residue-dependent constants in the sharp conjecture.
- When citing the 2025 result, distinguish its proved finite-n inequalities from its computational evidence and conjecture.

### 更新后的 AI 可解答性

- 等级: `low_to_medium_candidate`
- 分数: `38/100`
- 信心: `medium`
- 结论: 这是定义清楚、已有明确线性缺口的研究型开放问题，适合进行严谨的 proof-first 探索，但不适合期待仅靠计算或局部模式快速解决。评分仅针对当前未解的渐近/精确公式目标。

支持理由：

- 对象有限、定义离散，候选引理和反例均可精确检验。
- 最近预印本将问题压缩到 1/12 与 1/4 的常数缺口，并给出强而具体的模 4 精确猜想。
- 已知证明暴露了可审查的局部 Farey 结构、分母和计数步骤，而非完全依赖未知深猜想。

主要障碍：

- 要把 1/12 提升至 1/4，必须对全部位置和全部不同序对获得接近最优的全局间距下界；现有局部密度估计尚有常数损失。
- 精确猜想包含有限阈值 92 与模 4 加性项，局部渐近启发式不足以证明它。
- 大量有限枚举会强化猜想但不能处理无穷量词；预印本中的计算也不是证明。

Proof-first 路线：

- 先把“最短不同序对”的结构性必要条件转化为可证明的分类引理，尤其分析跨越小分母分数与靠近 1/2 的情形。
- 尝试改善局部 Farey 区间内小分母项的倒数和界，明确指出每一步能改善的常数及其适用区间。
- 独立寻找无限族反例以测试 1/4 极限是否可信；任何候选族都应先给出符号计算和精确索引距离证明。

需要验证：

- 逐项核查 van Doorn 预印本的定理 1、定理 2 与其对 f(n) 的推论，特别是严格不等式和 off-by-one。
- 在投入证明前再次检索 arXiv、作者主页、MathSciNet/zbMATH 和期刊是否出现 2026 后续版本。
- 如使用精确小 n 数据，生成可复核的 Farey 序列与 f(n) 证书，而非只报程序输出。

### 审计限制与人工复核理由

- 本审计按要求进行了定向公共网络检索并直接阅读了 Erdős 原文与 van Doorn 预印本的相关定理段落，但没有逐行重新证明或形式化验证 2025 预印本。
- 未发现新结果是检索证据，不是数学上证明“无人解决”。未被索引的论文、不同语言标题、私人稿件或 2026-07-27 后的更新不在结论范围内。
- 未发现与本题相关的 Lean/GitHub 形式化；这与问题页的“未形式化”记录一致，但不能排除未被检索引擎收录的私人仓库。

- 关键最新结果是 arXiv 预印本；在授权研究前，人工应复核其完整证明、是否已有期刊版本或勘误。
- 若研究计划主张精确公式，人工应确认 2025 年后是否有作者更新、会议稿或未被通用搜索正确索引的后续工作。

<!-- DEEP_REVIEW:END -->
