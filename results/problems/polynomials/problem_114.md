# Problem 114

## 基本信息

- 原始链接: https://www.erdosproblems.com/114
- LaTeX 页面: https://www.erdosproblems.com/latex/114
- 原始状态: `falsifiable`
- 奖金: `$250`
- 主类别: `polynomials`
- 原始标签: `polynomials`, `analysis`
- 形式化状态: `no`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

If $p(z)\in\mathbb{C}[z]$ is a monic polynomial of degree $n$ then is the length of the curve $\{ z\in \mathbb{C} : \lvert p(z)\rvert=1\}$ maximised when $p(z)=z^n-1$?

## AI 完成可能性判断

- 结论: **AI 可能做出局部推进或搜索反例，但完整解决把握不足**
- 等级: `low_to_medium_candidate`
- 分数: `49/100`
- 建议路线: 优先做反例搜索和小规模枚举；若没有反例，不能据此断言问题为真。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序

### 主要障碍

- 所属标签偏证明密集：analysis
- 题面含渐近/无限对象线索：\ll, o(
- 原记录含奖金 $250，说明该题被长期视为高价值难题；这不是否定依据，但提高验证门槛。

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: polynomials
- 证明密集标签命中: analysis
- 有限/计算线索: 无
- 渐近/无限线索: \ll, o(
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **中等偏高候选。按给定备注，充分大 n 的极值情形已由 Tao 证明，且已有 n=2、局部极大、线性上界和渐近上界等强结构结果。因此 GPT-5.5 配合符号计算、数值反例搜索、区间验证和形式化证明工具，更可能在“把剩余有限范围有效化/验证化”或“验证既有证明链”上取得实质进展；但直接给出完全原创解析证明仍有明显风险。**
- 等级: `medium_candidate`
- 分数: `72/100`
- 信心: `medium`
- 可能路线: 可行路线不是从零证明全猜想，而是围绕已有结果做有效化和验证：先把 lemniscate 长度写成可计算/可估计的表达式，复核 z^n-1 的长度行为；再抽取 Fryntov-Nazarov 的局部极大和 Tao 的充分大 n 唯一极大证明中可量化的常数，尝试得到明确阈值 N；对 n<N 的剩余情况，用低维参数化、数值全局优化、反例搜索、区间算术、半代数/实代数几何或 proof assistant 形式化来排除反例或定位漏洞。

### 支持理由

- 问题有强先验结构：单项式扰动、lemniscate 几何、长度泛函和极值多项式 z^n-1 都很明确，适合计算实验与局部变分分析。
- 给定备注显示已有逐步逼近全猜想的结果：n=2 已解、z^n-1 是局部极大、f(n) 有 2n+O(n^{7/8}) 渐近上界，且充分大 n 的唯一极大已被证明。
- 如果 Tao 的“充分大 n”证明可有效化，则剩余任务可能转化为有限多个 n 的验证问题，这类任务更适合 GPT-5.5 调度计算、形式化和文献抽取工具协作推进。
- 问题状态为 falsifiable，反例搜索有明确目标：寻找某个小或中等 n 的 monic 多项式，其单位 lemniscate 长度超过 z^n-1；这使数值优化和 interval certification 有实际价值。
- 已有上界常数从 4πn、9.173n、2πn 到渐近 2n+O(n^{7/8})，说明该领域已有可继承的估计框架，AI 不必完全发明新技术。

### 主要障碍

- 长度泛函依赖复平面代数曲线的几何，存在临界点、多个分支、奇异/近奇异 lemniscate 等情况，数值结果很难直接变成严格证明。
- 若 Tao 的充分大 n 结果没有给出可操作阈值，或阈值巨大，则“有限剩余验证”可能仍然不可行。
- 对一般 n 的全局极值问题是无限维连续参数空间上的非凸优化；即使低度数也可能有复杂局部极值。
- 形式化证明难度高：需要复分析、几何测度/曲线长度、渐近估计、稳定性分析以及计算机辅助实数不等式的严谨接口。
- z^n-1 的唯一性允许旋转和平移等等价变换，自动化验证时需要正确处理归一化和退化情形。

### 需要的验证

- 核查 Tao 结果的精确定理形式：是否证明原问题的全局极大、是否给出有效阈值、唯一性中的旋转和平移归一化如何表述。
- 为 lemniscate 长度实现可靠数值计算，并用已知 n=2 情形和 z^n-1 长度渐近作基准测试。
- 对小 n 进行大规模反例搜索，包括随机多项式、临界点附近扰动、根聚类结构和局部极大附近扰动。
- 若发现候选反例或边界情形，需要用区间算术或可验证积分给出严格上/下界，而不是只依赖浮点长度。
- 若走完成证明路线，需要把大 n 定理的常数有效化，并为剩余有限 n 建立可审计的计算证明或形式化证明脚本。

### 公开版思考摘要

这个问题对 GPT-5.5 级别模型不是典型的“从空白处解决未解难题”，因为给定备注表明已有结果几乎锁定了大 n 情形，并且低阶、局部和渐近理论都很强。AI 最有希望的贡献是整合这些结果，将充分大 n 的论证变成明确阈值，再把剩余有限情形转化为可验证计算任务。最大不确定性在于现有证明是否可有效化，以及连续极值问题能否被可靠地离散化和证书化。

### 免责声明

以上只是对 GPT-5.5 配合工具推进该问题的可行性评估，不是该 Erdős 问题的证明，也没有声称已验证或解决任何剩余情形。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `revised_open`
- 状态信心: `high`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_114.md](../../prompts/problem_114.md)

### 状态结论

原命题仍未被完整证明或反驳，但其研究形态已实质改变。Tao 的 2025 年预印本证明：对所有充分大的次数 n，z^n-1（允许平移和旋转）是唯一极大元；n=1 平凡，n=2 已由 Eremenko–Hayman 证明。因此严格剩余目标是 Tao 有效但未优化的阈值以下的有限个次数（其中 n>=3）的情形。论坛中有 n=3 的手稿以及 n<=14 的区间算术证书声明，但它们是未同行评审的作者/论坛材料；且证书历史上出现过 n=13 的实现错误并修补，不能据此将任何这些次数计为已独立验证闭合。

### 当前规范陈述

对每个整数 n>=1 及每个次数为 n 的首一复系数多项式 p(z)，令 L(p):=H^1({z∈C:|p(z)|=1})，其中 H^1 为一维 Hausdorff 测度；这等价于该代数曲线作为集合的总可求长弧长，奇点或自交点不按分支重数重复计数。标准 EHP 猜想为 L(p)<=L(z^n-1)=2^(1/n)B(1/2,1/(2n))。原猜想只断言该不等式对所有 n 成立，不单独断言唯一性。Tao 已证明当 n 充分大时，等号仅在 p(z)=(z-a)^n-e^(iθ)（a∈C，θ∈R）时成立。

```text
For every integer n >= 1 and every monic polynomial p(z) in C[z] of degree n, let L(p):=H^1({z in C: |p(z)|=1}), where H^1 is one-dimensional Hausdorff measure (equivalently the total rectifiable arclength, with singular/self-intersection points counted as a set, not with multiplicity). Then L(p) <= L(z^n-1). The benchmark length is L(z^n-1)=2^(1/n) B(1/2,1/(2n)). The conjecture asserts this inequality for every n; it does not, by itself, assert uniqueness. Tao proves that for all sufficiently large n equality holds only for p(z)=(z-a)^n-e^(i theta), with a in C and theta in R.
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 未发现能反驳上述精确上界的简单构造。论坛中的 p(z)=z^k-R（R→∞）使长度趋于 0，反驳的是一个不同的“固定连通分支数时正下界”猜想，并不涉及本题的上界。
- 版本变化: 1958 年 EHP 提出全次数上界猜想；1999 年 n=2 被证明；2009 年得到局部极大与渐近误差界；2025 年 Tao 将全局猜想证明到所有充分大 n，并说明常数有效可计算但未给出优化阈值。因此当前正确研究对象不是“任意 n 的完全未知猜想”，而是有限但未明示范围内的低/中次数补洞及其严格验证。

陈述问题：

- 输入中的“length of the curve”未说明奇点、自交或多个分支的计数约定。Tao 将其明确写作 ℓ(∂E_1(p))；以一维 Hausdorff 测度/曲线作为集合的总弧长重构可消除该歧义。
- “maximised when”表达的是所有首一 p 的不等式，不应被误读为原命题包含唯一性；唯一性只是 Tao 在充分大 n 下额外证明的结论。
- n 必须量化为正整数。n=1 的情形是平移后的单位圆；n=2 已闭合。

需要固定的量词/约定：

- Quantify n over all integers n >= 1 and p over all monic complex polynomials of exactly degree n.
- Interpret length as H^1 of the level set, not as an algebraic or parametrized length with branch multiplicity.
- The global inequality permits additional equality cases; uniqueness up to translation and rotation is verified only in Tao's sufficiently-large-degree theorem.
- Translation and rotation preserving monicity send z^n-1 to (z-a)^n-e^(i theta).

### 文献与当前边界

已核验的主要结果：

- Eremenko 与 Hayman（Michigan Math. J., 1999）证明 n=2 的完整猜想；并证明一般上界 L(p)<9.173n，及极大元可取使其 lemniscate 连通且包含全部临界点。
- Fryntov 与 Nazarov（AMS Translations, 2009；预印本 2008）证明 z^n-1 是局部极大元，并得到 L(p)<2n+o(n)；数据库记录给出其更具体的 O(n^(7/8)) 形式。
- Tao（arXiv:2512.12455v2，2025）将上界依次改进为 2n+O(sqrt(n))、2n+O(1)、2n+4 log 2+o(1)，最后证明对充分大 n 达到精确极值及唯一性。
- 旧的线性界（Dolženko、Danchenko 等）已被更强结果超越，对当前剩余核心不具决定性。

最近相关工作：Tao 的 2025 年预印本是决定性最新工作；作者网页在本审计日期将其列为将发表于 Journal d'Analyse Mathematique。2026 年论坛中的有限次数计算证书和三次手稿是待验证声明，不应与该预印本的可读证明混同。

剩余核心：证明或反驳：对 Tao 定理所保证的某个有效可计算阈值 N0 以下、且 n>=3 的每个剩余整数 n，是否皆有 L(p)<=L(z^n-1)。论文没有给出可直接引用的数值 N0；因此后续工作首先须从证明中提取可审计的阈值，或针对固定次数给出解析证明/可检验证书。若出现同长的非标准极大元，原不等式仍成立，但会影响强化的唯一性说法。

已使用方法：

- Eremenko--Hayman 的极值归约：存在极大元，并可令其 lemniscate 连通、含临界点，再作平移/旋转规范化。
- Fryntov--Nazarov 与 Tao 的 Stokes/面积积分弧长表示及对对数导数的估计。
- Tao 对三角不等式缺陷、临界点离散度与“origin repulsion”的定量控制，配合 Riesz 势、Rouché 定理、Bezout 型计数和区域分解。
- 固定低次数的可能路线包括极值归约后降低参数维度；论坛声称三次情形可用 Chebyshev/Joukowski 化为一维不等式，但该论证尚未独立核验。

争议或不确定性：

- Tao 的结果是预印本；虽有完整公开证明且作者页称将发表，审计没有进行逐引理的独立同行级验证。
- “充分大”的有效阈值在论文中未优化也未在摘要/主定理中数值化；不能把论坛覆盖的 n<=14 与高次数定理拼接成完整证明。
- 论坛声称 n=3 及 n<=14 的结论，但其 n=13 曾有实现错误；即使更新档案存在，也需独立检查问题参数化、区间算术、全域覆盖、哈希与验证器可信基。
- 搜索没有发现 2026 年同行评审论文或正式预印本完整解决剩余有限次数，亦没有发现反例；这支持 revised_open 而非证明其逻辑上必然开放。

### 证据来源

- [The maximal length of the Erdős--Herzog--Piranian lemniscate in high degree](https://arxiv.org/abs/2512.12455) — Terence Tao, 2025-12-22; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 主定理证明所有充分大 n 的 EHP 上界，并给出等号仅为平移、旋转的 z^n-1；还称全部隐常数有效可计算，但没有优化阈值。
- [The maximal length of the Erdős--Herzog--Piranian lemniscate in high degree, full PDF](https://arxiv.org/pdf/2512.12455) — Terence Tao, 2025-12-22; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 可直接检查的 56 页证明文本给出精确猜想、标准多项式的 Beta 函数长度公式、主定理，以及“剩余为有效有界次数”的限定和有限计算不能自动判定相等的警告。
- [Papers and preprints — Terence Tao](https://teorth.github.io/tao-web/papers.html) — Terence Tao, 2026; `author_page`, `informal_claim`, directness=`direct`, reliability=`high`. 作者论文页将该工作列为“to appear, Journal d'Analyse Mathematique”；这支持其当前投稿/待刊状态，但不替代独立同行评审核验。
- [On the length of lemniscates](https://arxiv.org/abs/0805.2295) — Alexandre Eremenko; Walter Hayman, 2008-05-15; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 该公开版本对应 Michigan Mathematical Journal 46 (1999), 409--415；其摘要和正文陈述 n=2 的极值结论以及一般的 9.173n 上界。
- [New estimates for the length of the Erdos-Herzog-Piranian lemniscate](https://arxiv.org/abs/0808.0717) — Alexander Fryntov; Fedor Nazarov, 2008-08-05; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 对应 2009 年 AMS Translations 论文；证明 z^n-1 为局部极大元并给出渐近尖锐的 2n+o(n) 上界。Tao 的参考文献将发表版本定位为 AMS Translations Series 2, vol. 226, pp.49--60。
- [Erdős Problem #114](https://www.erdosproblems.com/114) — Thomas F. Bloom / Erdős Problems, 2026-01-23; `problem_page`, `database_record`, directness=`indirect`, reliability=`medium`. 当前数据库记录列出 EHP、Eremenko--Hayman、Fryntov--Nazarov 和 Tao 的结果，并仍将记录保留为可证伪问题；数据库不是当前状态的决定性证明来源。
- [Erdős Problem #114 discussion thread](https://www.erdosproblems.com/forum/thread/114) — dahlkebj; Kenneth Mendoza; Erdős Problems forum users, 2026-05-21; `forum`, `informal_claim`, directness=`direct`, reliability=`low`. 记录 n=3 手稿及 n<=14 区间证书的声明，也明确披露早期 n=13 的空分支限界错误和重跑。未见同行评审论文、形式化证明或已独立复现的完整证书审查，故这些不是闭合证据。

### 完成标准

- 肯定出口: Establish, with a rigorous proof, that L(p)<=L(z^n-1) for every monic p of every remaining degree 3<=n<N0, where N0 is an explicit threshold legitimately extracted from Tao's theorem; combine this with n=1, n=2, and Tao's n>=N0 theorem. A proof for an individual fixed remaining n is an affirmative resolution only of that fixed-degree subproblem.
- 否定出口: Exhibit a specific integer n in the unresolved finite range and a specific monic polynomial p of degree n, together with a rigorous arclength computation or certificate proving L(p)>L(z^n-1). This disproves the original global EHP inequality.

不构成完成：

- Showing only L(p)<=2n+O(1), 2n+4 log 2+o(1), or any other asymptotic upper bound.
- Numerical optimization, plots, floating-point quadrature, or heuristic search that has no globally valid error and coverage certificate.
- Proving local maximality of z^n-1, or proving a statement only for polynomials near it.
- Verifying selected degrees without a proven bridge to every remaining degree.
- Finding a nonstandard polynomial with equal length: this may disprove a uniqueness strengthening, but it does not disprove the stated inequality.
- Citing an unreviewed forum post or an archived computation without auditing its domain reduction, interval enclosures, and checker.

正确性陷阱：

- Use H^1/arclength of the level-set as a set; singular crossings must not be accidentally counted with algebraic multiplicity.
- Preserve monicity under every normalization and account exactly for translation and rotation symmetries.
- Do not infer the original all-degree inequality from Tao's asymptotic estimates alone; only Theorem 1.1(iv) supplies exact extremality, and only for sufficiently large n.
- If using a finite certificate, prove compactness/domain reduction first, include all boundary and critical-value strata, use outward-rounded certified intervals, and independently verify the certificate.
- Separate inequality from uniqueness: equality cases beyond the symmetry orbit leave the original question affirmatively answered but refute a stronger claim.
- A claimed numerical N0 must be derived with explicit constants from Tao's proof, not guessed from experiments.

### 更新后的 AI 可解答性

- 等级: `low_to_medium_candidate`
- 分数: `24/100`
- 信心: `medium`
- 结论: 这是一个定义良好但难度很高的“有限补洞”目标。高次数已由长篇新预印本处理，低次数并未由可独立确认的统一结果覆盖；AI 可协助提取显式常数、审计有限证书或攻击固定次数，但短期内完整解决剩余范围的概率偏低。

支持理由：

- 剩余对象有明确逻辑完成条件：有限范围内每个次数的全局不等式或一个严格反例。
- Tao 的有效性声明原则上把无限问题降至有限补洞，且 Eremenko--Hayman 的极值归约显著收缩了优化空间。
- 固定 n 的结论可以通过解析不等式或严格证书独立检验，适合分层的证明审计。

主要障碍：

- Tao 的可计算阈值未数值化，实际有限范围可能很大；从隐常数提取到可用 N0 本身可能极其困难。
- 弧长是含临界点/拓扑变化的全局非代数优化泛函，低次数也不能可靠地由采样解决。
- 现有论坛计算曾暴露实现错误，说明“区间算术”标签本身不能替代对参数空间覆盖和验证器的审计。
- Tao 的高次数论证复杂，直接下推到小次数不具明显可行性。

Proof-first 路线：

- 先从 Tao 的证明逐常数提取一个明确 N0，并建立其依赖链；只有得到有限目标后才决定固定次数策略。
- 对单个最小未闭合次数，先严格复核 Eremenko--Hayman 规范化与临界点约束，寻找可将极大元参数空间降维的解析引理。
- 将论坛中的 n=3 手稿仅作为待审计候选：逐步验证其从一般首一三次到一维不等式的每个等价变换和端点情况。
- 至多允许一个计算分支，且只能在先证明紧致规范参数域、目标函数的可验证包络和明确停止条件后，用于证明一个指定固定次数。

需要验证：

- 对 Tao 预印本主定理及“有效可计算常数”作人工数学审稿级检查，并确认截至审计日期的发表状态。
- 独立下载并审查 Zenodo/代码证书：版本、哈希、参数化、区间库、覆盖树、n=13 修补前后的差异、以及独立小型检查器。
- 若采用 n=3 手稿，检查其作者身份、文件版本、完整证明与是否已被期刊/预印本服务器收录。
- 检索 Tao 预印本之后的勘误、引用论文和作者公告，特别是是否公布了显式阈值或完成有限补洞。

### 审计限制与人工复核理由

- 本审计只使用用户提供的单条问题记录作为仓库输入，并进行了公开网页检索；没有读取或比较任何其他仓库条目。
- 已直接检查 Tao 预印本的题目、主定理、剩余有限范围说明及部分证明结构，但没有在本审计中逐行复核其 56 页证明，因此“已证明充分大 n”依赖该公开预印本的数学正确性。
- Zenodo API/DOI 页面在本次检索中未能抓取；有限次数声明仅以可见论坛文本记录，未对档案、源代码、二进制、哈希或区间证书作独立执行验证。
- 未找到 2026 年 7 月 27 日前完整解决剩余次数的同行评审论文或可靠反例；这是基于定向搜索的证据结论，不是不存在此类结果的逻辑证明。
- 作者网页的“to appear”状态可能在审计日期后变化；应在人类复核时刷新出版社记录。

- 应由复杂分析专家对 Tao 预印本的主证明、有效常数与实际发表状态作独立核验。
- 应由可复现计算/形式化专家审计论坛所引有限次数证书，特别是完整参数覆盖、可信基和已披露的 n=13 修补。
- 若研究任务要求精确有限清单，必须先从 Tao 证明中提取并验证数值阈值 N0；当前公开主定理只给出“充分大”。

<!-- DEEP_REVIEW:END -->
