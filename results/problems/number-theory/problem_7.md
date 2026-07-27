# Problem 7

## 基本信息

- 原始链接: https://www.erdosproblems.com/7
- LaTeX 页面: https://www.erdosproblems.com/latex/7
- 原始状态: `verifiable`
- 奖金: `no`
- 主类别: `number theory`
- 原始标签: `number theory`, `covering systems`
- 形式化状态: `yes`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

Is there a distinct covering system all of whose moduli are odd?

## AI 完成可能性判断

- 结论: **AI+计算/形式化工具有较高机会完成或显著推进**
- 等级: `high_candidate`
- 分数: `72/100`
- 建议路线: 优先搜索有限证书；若找到证书，再做独立程序验证和形式化复核。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 题面或备注出现有限对象/计算线索
- 已有形式化陈述，可降低语义误读风险

### 主要障碍

- 所属标签偏证明密集：number theory

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: covering systems
- 证明密集标签命中: number theory
- 有限/计算线索: covering system
- 渐近/无限线索: 无
- 构造/存在性线索: is there

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **低到中等候选。GPT-5.5 级别模型不应被期待直接完成全问题的存在性判定，但在工具配合下有现实机会显著推进：系统化反例/例子搜索、SAT/ILP/CRT 编码、形式化验证候选覆盖、以及复核或扩展关于 lcm 必须含有特定因子的有限排除结果。若目标是“找到显式奇数 distinct covering system”或“证明不存在”，难度仍然很高。**
- 等级: `low_to_medium_candidate`
- 分数: `42/100`
- 信心: `medium`
- 可能路线: 最可能路线是把奇数 distinct covering system 转化为有限可验证约束：固定一组奇数模数或固定 lcm 的素因子结构后，用中国剩余定理、覆盖密度约束、SAT/ILP/CP-SAT 搜索残余类；对候选覆盖用形式化证明或穷举模 lcm 验证；对不存在性则逐步证明某些 lcm 结构、最大模数范围或 squarefree/低幂情形不可行。模型更可能产生可复核的局部排除定理或搜索证据，而不是一次性解决完整开放问题。

### 支持理由

- 问题状态为 verifiable 且 formalized=yes，这使得候选构造、有限排除和证明片段可以被机器校验。
- 覆盖系统天然适合 CRT、SAT、ILP、精确覆盖、分支定界和模 lcm 穷举等计算工具。
- 已知结果给出强约束：若全为奇数，则仍至少要受 3 的整除性限制，并且 lcm 必须含有 9 或 15 的结构信息；这些可作为搜索剪枝和形式化引理。
- 更强的 odd squarefree 版本已知为否，说明相关技术能排除重要子类，AI 可尝试复现、简化或推广这类子类排除。
- 若存在显式例子，验证成本相对低：只需检查模数互异、全为奇数，并在共同 lcm 上覆盖所有剩余类。

### 主要障碍

- 完整存在性问题没有明显有限上界；搜索空间随模数集合、素因子幂次和残余类选择爆炸。
- 局部不可行证据很难外推为全局不存在性证明，尤其是在允许高素数幂和复杂 lcm 结构时。
- 覆盖系统有稀疏但高度耦合的约束，SAT/ILP 可能在大实例上给出不可解释的失败或依赖弱剪枝。
- 如果答案为存在，显式构造可能规模极大，普通启发式搜索未必能到达。
- 如果答案为不存在，证明可能需要新的结构性思想，而不仅是扩大既有计算范围。

### 需要的验证

- 任何显式候选必须由独立程序和形式化证明双重验证：模数互异、全奇数、每个整数类被至少一个同余类覆盖。
- 计算性排除必须给出完整的搜索边界、剪枝规则、证书格式和可重放脚本，避免只报告求解器结论。
- 若提出新的结构引理，需要在形式化系统中验证关键 CRT、密度、整除性和最小反例推理。
- 应独立复现已知约束作为 sanity check，例如 squarefree 子类不可能、以及 odd covering 若存在则 lcm 需含有相关因子结构。
- 若使用文献检索，必须确认问题当前状态未被更新；但本次判断只基于给定 JSON。

### 公开版思考摘要

这个问题的可机检性较强：一旦给出候选覆盖，验证很直接；对固定 lcm 或固定模数族的不可行性也可转成有限计算证书。因此 GPT-5.5 配合求解器和形式化工具有较大机会产出可靠的局部进展。然而完整问题要求在无限可能的奇数模数族中判定存在性，当前给定信息显示已知结果只排除了重要子类并给出必要条件，离全局解决仍有明显结构缺口。所以它不是高概率可完全解决的问题，但适合作为 AI 辅助搜索、证明压缩和验证推进的中等偏低候选。

### 免责声明

以上不是该 Erdős 问题的解答，也不声称存在或不存在这样的覆盖系统；只是评估 GPT-5.5 级别模型在工具辅助下对该单一问题的可推进性。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `confirmed_open`
- 状态信心: `high`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_7.md](../../prompts/problem_7.md)

### 状态结论

在通常且文献一致的约定（覆盖系有限、模数大于 1）下，问题仍为开放问题。2026 年初的非正式 Lean/附录“解答”明确依赖未证公理；论坛随后指出其早期筛法公理甚至为假，且维护者未将其采纳为解答。2025 年发表于 Discrete Mathematics 的相关论文仍将原问题称为中心开放问题，但研究的是“允许一个奇模数重复”的变体。

### 当前规范陈述

是否存在一个有限同余类族 {a_i (mod n_i)}_{i=1}^k，使得：k≥1；模数 n_i>1 且两两不同；所有 n_i 均为奇数；并且每个整数 x 都满足 x≡a_i (mod n_i)（对某个 i）？

```text
Does there exist a finite family of congruences a_i (mod n_i), for i=1,...,k, such that (i) k>=1; (ii) n_i are pairwise distinct integers with n_i>1; (iii) every n_i is odd; and (iv) for every x in Z there is an i with x ≡ a_i (mod n_i)?
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 在上述标准定义下，未找到简单反例或显式奇模数覆盖。已核查的边界漏洞是模数 1：若不排除它，{0 (mod 1)} 是平凡肯定例；因此 canonical statement 明确要求 n_i>1。
- 版本变化: 历史上同时提出过平方自由版本。Balister、Bollobás、Morris、Sahasrabudhe、Tiba 证明平方自由版本中必有偶模数（2021），故该更强版本已关闭；原始奇模数版本仍存。Hough–Nielsen（2019）证明任一不同模数覆盖至少有一个模数被 2 或 3 整除；因此假想的奇覆盖必须含 3 的倍数。BBMST（2022）给出更简单的相关筛法并记录原题的进一步必要限制。2026 年论坛中的候选证明未构成修订后的已证定理。

陈述问题：

- “covering system”必须明确为有限族；若允许无限族，论坛已指出可仅用奇模数构造无限覆盖，因而不是本题。
- 必须采用覆盖系统文献中 n_i>1 的约定。若容许模数 1，则单一同余类 0 (mod 1) 已给出平凡肯定答案；Hough–Nielsen 的正式定义及相关文献均排除此情形。
- “distinct”指模数两两不同，而非同余类两两不交、也非所有整数恰被覆盖一次。
- 题目的平方自由加强版“所有模数奇且平方自由”已被否定；这不解决原题，因为原题允许素数幂因子。

需要固定的量词/约定：

- The family is finite and nonempty.
- For every modulus n_i, n_i is an integer greater than 1; residues a_i may be taken modulo n_i.
- Pairwise distinct means n_i != n_j whenever i != j.
- The covering condition is forall x in Z, exists i in {1,...,k} such that n_i divides x-a_i.
- No disjointness, irredundancy, square-freeness, or divisibility-antichain hypothesis is part of the target.

### 文献与当前边界

已核验的主要结果：

- Hough–Nielsen（Duke Math. J., 2019）证明每个不同模数覆盖至少有一个模数被 2 或 3 整除。因此任何假想奇覆盖必有某个模数被 3 整除。
- Balister–Bollobás–Morris–Sahasrabudhe–Tiba（Algebra & Number Theory, 2021）证明：不同且平方自由的覆盖不可能全为奇模数。这是原问题一个严格更强假设下的否定结论，不能删除平方自由条件。
- Balister–Bollobás–Morris–Sahasrabudhe–Tiba（Invent. Math., 2022）发展并简化了适用于 covering systems 的概率测度/筛法，解决 Schinzel 猜想、改进最小模数问题，并对 Erdős–Selfridge 问题取得进一步限制。问题页据此记录：若奇覆盖存在，其模数 LCM 必被 9 或 15 整除。该具体必要条件在本审计中仅由问题页间接核验。
- 初等计数给出必要条件：若 L 是模数 LCM，则各类在 Z/LZ 中的覆盖计数蕴含 sum_{d|L,d>1} 1/d ≥ 1，等价于 sigma(L)≥2L；故 L 必为 abundant。对奇 L，这至少排除 L<945，但不排除一般情形。

最近相关工作：Bispels、Cohen、Harrington、Lowrance、Pontes、Schaumann、Wong 的《A further investigation on covering systems with odd moduli》先于 2025 年提交 arXiv，记录为 Discrete Mathematics 349 (2026) 115013。它明确仍称原奇覆盖问题开放，研究的是允许一个奇模数重复的不同变体，故不能当作原题的解答。

剩余核心：精确剩余核心是：在不要求平方自由、允许任意奇素数幂且仅要求模数两两不同的有限覆盖中，究竟能否覆盖全部整数。肯定解须给出明确有限覆盖；否定解须排除所有这类非平方自由系统。

已使用方法：

- 将有限覆盖化为模数 L 的有限群 Z/LZ 上的覆盖，并使用倒数和、除数和与丰数性障碍。
- Hough–Nielsen 的概率方法，含 Shearer 型局部引理/加权局部引理与按素数逐步处理的伪随机概率测度。
- BBMST 的筛法重述、二阶矩控制及有限小素数阶段的优化/可验证数值界。
- 平方自由情形的中国剩余定理几何化：把同余类转换为有限直积空间中的 hyperplanes，并控制其覆盖。

争议或不确定性：

- 2026 年 GitHub/Lean 候选证明不是无条件形式化：关键好纤维界被写为 axiom。论坛还记录了该项目较早版本中一个错误的筛积公理；不能据此改变开放状态。
- 数据库页面的“open”标签是高价值当前线索而非完备文献证明；本次检索未发现经同行评议或完整无公理形式化的原题解答。
- BBMST 的“LCM 被 9 或 15 整除”具体表述由当前问题页提供；应在后续研究开始前从 Inventiones 原文中逐条复核其精确假设与表述。

### 证据来源

- [Erdős Problems, Problem 7](https://www.erdosproblems.com/7) — Thomas F. Bloom (database page), 2026-01-22; `problem_page`, `database_record`, directness=`indirect`, reliability=`high`. 当前数据库将本题标为 open，给出原题、平方自由变体的否定结果、Hough–Nielsen 限制，以及论坛链接。数据库也明确提示其状态并非文献穷尽证明。
- [Covering systems with restricted divisibility](https://arxiv.org/abs/1703.02133) — Robert D. Hough; Pace P. Nielsen, 2019; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 定理：每个不同模数覆盖系都有一个模数可被 2 或 3 整除。arXiv 页面给出 Duke Mathematical Journal 168(17) (2019), 3261–3295 及 DOI 10.1215/00127094-2019-0058。
- [The Erdős-Selfridge problem with square-free moduli](https://arxiv.org/abs/1901.11465) — Paul Balister; Béla Bollobás; Robert Morris; Julian Sahasrabudhe; Marius Tiba, 2021; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 定理 1.1：任何具有两两不同平方自由模数的有限算术级数覆盖中，至少一个模数为偶数；即平方自由奇模数变体被否定。
- [On the Erdős Covering Problem: the density of the uncovered set](https://arxiv.org/abs/1811.03547) — Paul Balister; Béla Bollobás; Robert Morris; Julian Sahasrabudhe; Marius Tiba, 2022; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 论文明确将 Erdős–Selfridge 奇模数问题列为研究对象，发展概率测度/筛法并给出进一步进展；期刊版为 Inventiones Mathematicae 228 (2022), 377–414，DOI 10.1007/s00222-021-01087-5。
- [Erdős Covering Systems](https://www.cambridge.org/core/books/abs/surveys-in-combinatorics-2024/erdos-covering-systems/8C1FD7ABA25695B91DADC11251FB916D) — Paul Balister, 2024-05-23; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 2024 年同行评议综述概述 Hough 及 BBMST 的进展，并把平方自由问题和原始 covering-systems 文献清楚区分。
- [A further investigation on covering systems with odd moduli](https://arxiv.org/abs/2507.16135) — Chris Bispels; Matthew Cohen; Joshua Harrington; Joshua Lowrance; Kaelyn Pontes; Leif Schaumann; Tony W. H. Wong, 2026; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 论文摘要称奇覆盖问题仍是中心开放问题；其结果只涉及允许一个奇模数重复、其余模数不同的变体。arXiv 记录给出 Discrete Mathematics 349 (2026), Article 115013。
- [Erdős Problems forum thread for Problem 7](https://www.erdosproblems.com/forum/thread/7?order=newest) — Multiple forum participants; Thomas Bloom, 2026; `forum`, `informal_claim`, directness=`direct`, reliability=`medium`. 候选证明作者承认其 Lean 文件含两个公理。后续讨论指出早期筛积公理按其定义必为假；维护者要求任何后续声称只能以完整、自包含、无 sorry 且无外部公理的 Lean 形式提出。该线程也记录 LCM 必为 abundant 的必要条件及无限版本的非本题性。
- [spicylemonade/erdos-007 main.lean](https://raw.githubusercontent.com/spicylemonade/erdos-007/main/main.lean) — Repository contributors, 2026; `formalization`, `formalized_artifact`, directness=`direct`, reliability=`high`. 源文件的主定理显式假设 HoughNielsenFact，并把关键的 HoughNielsenGoodFibre 声明为 axiom；文件自身说明该量化筛界不能由前者推出。因此这不是原题的无条件 Lean 证明。
- [On integer covering systems with all moduli distinct](https://mathoverflow.net/questions/74644/on-integer-covering-systems-with-all-moduli-distinct) — Gerry Myerson; David E. Speyer; Pace Nielsen and others, 2011-09-06; `forum`, `informal_claim`, directness=`direct`, reliability=`medium`. 给出透明的必要条件：不同模数覆盖的 LCM 必为 abundant；若 L 为奇数则 L≥945。该条件不证明不存在奇覆盖。

### 完成标准

- 肯定出口: Exhibit a finite k, pairwise distinct odd integers n_i>1, and residues a_i, and prove that for every residue r modulo L=lcm(n_1,...,n_k), at least one congruence r≡a_i (mod n_i) holds. This finite verification is equivalent to coverage of all integers.
- 否定出口: Prove that every finite family of congruences with pairwise distinct odd moduli greater than 1 leaves at least one integer uncovered; equivalently, prove no object satisfying the canonical existential statement exists.

不构成完成：

- A proof only for square-free moduli, primitive/antichain systems, bounded numbers of primes, bounded LCM, or bounded number of congruences.
- A necessary condition such as divisibility by 3, 9, or 15, abundance of the LCM, or a reciprocal-sum inequality without an argument excluding all remaining systems.
- An exhaustive search without a rigorously proved finite reduction that covers every possible LCM and exponent pattern.
- A construction with a repeated modulus, modulus 1, an infinite family, or a cover of only a finite interval/density-one subset.
- A Lean theorem whose conclusion depends on an unproved axiom, sorry, admitted numerical certificate, or a theorem not shown to imply the stated target.

正确性陷阱：

- Check that every n_i is >1, odd, and pairwise distinct; distinct residue classes alone are irrelevant.
- Check universal coverage modulo the full LCM, not merely a sample range or a proper divisor of the LCM.
- Do not replace 'covering' by exact/disjoint/irredundant covering unless the reduction proves equivalence.
- For a negative proof, do not silently impose square-freeness or bound prime exponents.
- Audit every numerical sieve inequality, parameter range, rounding direction, and dependence on finite optimization data.
- If formalized, inspect the dependency graph for axioms and verify that the formal statement matches the finite, distinct, n_i>1 formulation.

### 更新后的 AI 可解答性

- 等级: `low_candidate`
- 分数: `14/100`
- 信心: `high`
- 结论: 这是定义清楚、可证伪也可构造的真实开放题，但属于长期难题；现有强筛法已处理平方自由情形和若干必要限制，剩余的非平方自由情形没有已知的小缺口。对通用 AI 而言，短期独立解决概率低。

支持理由：

- 目标是明确的一阶存在/不存在命题；肯定解可由有限证书完全核验，否定解也有清晰逻辑终点。
- 已有高质量主文献和严格的限制结果，提供可审计的背景、可分解引理及明确的失败模式。
- 2025–2026 的文献和被审查的候选证明均支持其仍为真实开放目标，而非数据库滞后。

主要障碍：

- 原题已抵抗数十年；平方自由结论不能自然外推到任意素数幂。
- 现有成功方法依赖精细的概率筛、二阶矩界和小素数阶段的优化；把这些界推广到一般幂次是实质性理论障碍。
- 无限搜索空间不能由直接计算覆盖；没有严格有限归约的计算不具决定性。
- 近期非正式“简单推广”主张已暴露出错误公理/缺失初始筛参数的风险。

Proof-first 路线：

- 尝试证明一个精确的幂次压缩或单调性引理：它必须把任意假想奇覆盖严格归约到已否定的平方自由或有限可检验模型；在声称前逐项核对覆盖、不同性和筛参数。
- 重新检查 BBMST/Hough–Nielsen 框架中指数出现的位置，寻找能控制非平方自由模数而不把必要条件误当充分条件的量化不等式。
- 仅可安排一个可选计算任务：在先证明的有限 LCM/指数界下，生成可复核的穷尽证书；停止条件必须是覆盖整个已证明有限空间或找到有效反例。

需要验证：

- 从 Inventiones 2022 原文核对“LCM divisible by 9 or 15”的精确命题、假设和证明位置。
- 核验 Bispels 等人 2026 期刊版的最终定理，确认其重复模数变体没有意外蕴含原题。
- 若有人再次提出 Lean 证明，编译固定版本并检查其所有 declarations 的 axiom/sorry 依赖以及外部数值证书。

### 审计限制与人工复核理由

- 本审计进行了针对性公开网页、arXiv、期刊/出版社页面、论坛和候选 Lean 源码检索，但不能逻辑上证明不存在未索引、付费墙后或未来发表的解答。
- Erdős Problems 的正文页面本身在直接抓取时返回 403；其最新页面内容通过搜索索引核对，并直接打开了论坛线程。
- Inventiones 2022 的“LCM 必被 9 或 15 整除”精确版本未能从原文 HTML 中逐句提取，故作为问题页的间接记录而非本审计独立复证明的主结论。
- GitHub 候选项目的完整附录没有逐行进行数学审稿；但其主 Lean 文件显式使用关键 axiom，已足以否定其作为无条件形式化解决方案的资格。

- 若后续研究将使用 BBMST 的 9/15 LCM 限制或任何数值筛界，专家应从原始论文逐条确认其假设、常数和计算证书。
- 任何声称把平方自由筛法推广至一般素数幂的工作都需要独立专家复核；2026 年论坛已出现过看似相近但错误的形式化/筛积翻译。
- 在投入大规模研究前，建议人工检索 MathSciNet/zbMATH、期刊最新卷和作者主页，以降低未索引近期论文遗漏风险。

<!-- DEEP_REVIEW:END -->
