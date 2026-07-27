# Problem 10

## 基本信息

- 原始链接: https://www.erdosproblems.com/10
- LaTeX 页面: https://www.erdosproblems.com/latex/10
- 原始状态: `open`
- 奖金: `no`
- 主类别: `number theory`
- 原始标签: `number theory`, `additive basis`, `primes`
- 形式化状态: `yes`
- OEIS: `A387053`
- 原站备注字段: 无

## 原问题

Is there some $k$ such that every large integer is the sum of a prime and at most $k$ powers of 2?

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `36/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 题面或备注出现有限对象/计算线索
- 已有形式化陈述，可降低语义误读风险
- 存在 OEIS 数据入口，利于实验与反例搜索

### 主要障碍

- 所属标签偏证明密集：number theory, primes
- 题面含渐近/无限对象线索：density, infinitely many, prime

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: additive basis
- 证明密集标签命中: number theory, primes
- 有限/计算线索: finite, finitely
- 渐近/无限线索: density, infinitely many, prime
- 构造/存在性线索: is there

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **低候选。GPT-5.5 级别模型配合计算和形式化工具，较可能做出有限范围验证、反例搜索、条件性归约、文献脉络整理和已有密度结果的形式化复核；但要无条件证明存在某个固定 k，或证明不存在这样的 k，仍需要突破深层的素数分布与稀疏加法基障碍，短期内不宜期待完整解决。**
- 等级: `low_candidate`
- 分数: `22/100`
- 信心: `medium`
- 可能路线: 最现实路线不是直接求解，而是构建可审计的计算与理论辅助框架：枚举给定 k 下的例外整数，复核类似 1117175146 的小 k 障碍；把问题转化为对集合 n-2^{a_1}-...-2^{a_j} 中素数命中的覆盖问题；形式化 Gallagher 型“密度趋近 1”结果的局部版本；检索和整理关于 prime plus powers of two、Romanoff 型定理、Goldbach with powers of two 的已知条件性结果；在 GRH、Hardy-Littlewood 或 Granville-Soundararajan 猜想下验证可推出的 k 界。

### 支持理由

- 问题表述短且形式化状态为 yes，适合模型把目标拆成可计算命题、有限验证任务和形式化证明子目标。
- 已有 Gallagher 结果说明“几乎所有整数”方向已经可达，模型可以尝试把密度型论证机械化、优化参数或寻找可验证的补强。
- 给定 k 的反例搜索相对明确，可用筛法、分段素性测试、位集卷积或 SAT/SMT 风格编码进行大规模验证。
- Granville-Soundararajan 关于少量 2 的幂的猜想给出强目标，模型可在条件假设下整理推导链并测试数值证据。
- 形式化证明工具适合检查有限覆盖、模障碍、归约步骤和计算证书，能降低实验性结论中的错误风险。

### 主要障碍

- 核心难点是无条件控制大量稀疏平移集合中的素数命中；这远超普通计算搜索或局部筛法。
- 若结论为否定，需要构造无限多个整数避开所有 prime plus bounded powers of 2 的表示，这同样需要强全局结构，而不是有限反例。
- 若结论为肯定，需要把“密度 1”提升为“所有充分大整数”，通常要排除极稀疏例外集，这是解析数论中非常硬的步骤。
- 小 k 的计算反例不能直接说明任意固定 k 的不存在；大 k 的有限验证也不能证明最终全覆盖。
- 问题已有评论显示权威判断高度不确定，且 Erdős 曾称其可能不可攻击，说明当前已知方法与目标之间存在实质缺口。

### 需要的验证

- 对每个计算声称生成可复验代码、参数、区间、素性测试方法和哈希化结果文件。
- 对有限验证给出独立实现交叉检查，尤其是 powers of 2 重复使用、至多 k 项、奇偶限制和边界条件。
- 若提出条件性定理，必须明确依赖的未证猜想及其推出 k 的逻辑步骤。
- 若声称显著推进，应由解析数论专家审查筛法估计、误差项、例外集处理和从密度到全覆盖的跳跃。
- 形式化部分应至少覆盖问题定义、有限搜索证书验证器、关键组合归约和可机械检查的引理。

### 公开版思考摘要

这个问题对 AI 友好的部分在于目标极简、可形式化、可做大规模搜索，并且已有密度型定理提供了可复核的理论支点。困难在于最终命题要求“所有充分大整数”，不是“几乎所有”；从密度结果或计算证据跨到全覆盖，正是素数分布与稀疏加法基中的硬障碍。因此 GPT-5.5 更可能产出严谨的辅助成果、反例数据库、条件性证明和形式化验证框架，而不是独立完成无条件解答。

### 免责声明

以上是对 GPT-5.5 级别模型辅助研究可行性的评估，不是该 Erdős 问题的证明或反例。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `confirmed_open`
- 状态信心: `high`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_10.md](../../prompts/problem_10.md)

### 状态结论

问题 #10 仍可高置信度地视为开放。2026-04 更新的 Erdős Problems 页面仍标为 OPEN，且其论坛页没有已声明的解答；Google DeepMind Formal Conjectures 中相应主命题仍以 `sorry` 占位，只有形式化陈述而无证明。检索到的 2026 年 Johnston–Trudgian 工作改进的是“两个素数加固定个 2 的幂”的 Linnik–Goldbach 问题，不能推出本题的“一个素数”结论。

### 当前规范陈述

令 \(S_k=\{p+\sum_{i=1}^{r}2^{a_i}:p\text{ 为素数},\ 0\le r\le k,\ a_i\in\mathbb Z_{\ge0}\}\)。问题是是否存在 \(k\) 与 \(N_0\)，使得每个 \(n\ge N_0\) 都属于 \(S_k\)。允许重复的 2 的幂；但把两个相同幂合并为下一幂不会增加项数，故等价地可要求指数互异。约定 \(2^0=1\)，且素数允许为 \(2\)。

```text
Let \(S_k=\{p+\sum_{i=1}^{r}2^{a_i}: p\text{ is a prime},\ 0\le r\le k,\ a_i\in\mathbb Z_{\ge0}\}\). Determine whether \(\exists k\in\mathbb Z_{\ge0}\,\exists N_0\in\mathbb N\,\forall n\ge N_0,\ n\in S_k\). Repeated powers are allowed, but may be merged in pairs, so one may equivalently require distinct exponents. Here \(2^0=1\), and the prime may be \(2\).
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 未发现能否定“存在某个固定 k”的简单构造。Grechuk 的 \(1117175146\notin S_3\) 只排除 \(k=3\)，不能排除较大的 \(k\)。Crocker 型覆盖同余结果对很小的项数给出障碍，也不否定全称存在某个 \(k\) 的命题。
- 版本变化: 历史上 Erdős 在 1980 年曾带着“trepidation”猜测肯定答案，而 Erdős–Graham 的书中倾向否定答案；Granville–Soundararajan（1998）又提出更强的具体猜测：所有奇数 \(>1\) 至多需 3 项，进而所有正偶数至多需 4 项。该具体猜测仍不是本题已证明的替代版本。

陈述问题：

- 原句的 “large” 未显式给出阈值；按数论惯例应为“存在 \(N_0\)，对所有 \(n\ge N_0\)”。
- “powers of 2” 必须包含 \(2^0=1\)，并须说明是否可重复。Formal Conjectures 使用指数多重集；重复项可通过二进制进位消去，因此不影响存在固定 \(k\) 的问题。
- 该形式化文件把目标写成所有 \(n\ge2\) 都可表示，而非最终所有。两者在此等价：每个固定小整数都可用 \(p=2\) 加 \(n-2\) 的二进制展开表示，有限个例外可吸收进较大的固定 \(k\)。

需要固定的量词/约定：

- The required order is \(\exists k\,\exists N_0\,\forall n\ge N_0\,\exists p,r,a_1,\ldots,a_r\); neither \(k\) nor \(N_0\) may depend on \(n\).
- A negative resolution is \(\forall k\,\forall N_0\,\exists n\ge N_0\) with no such representation.
- The empty sum is permitted when \(r=0\); it handles prime integers but is immaterial asymptotically.

### 文献与当前边界

已核验的主要结果：

- Gallagher（1975，同行评审）证明：任意 \(\epsilon>0\) 时存在 \(k(\epsilon)\)，使 \(S_{k(\epsilon)}\) 的下密度至少为 \(1-\epsilon\)。这是“几乎全部”结论，量词不足以推出一个 \(S_k\) 包含所有充分大整数。
- Crocker（1971，同行评审）对两个 2 的幂构造无穷不可表示整数，说明小 \(k\) 的覆盖同余障碍真实存在；它没有给出对任意 \(k\) 的统一反例构造。
- Granville–Soundararajan（1998，同行评审）提出所有奇数 \(>1\) 至多用 3 个 2 的幂表示的猜测，从而偶数至多 4 个；这是比原题的肯定答案更强的未证猜测。
- Grechuk 的具体偶数 \(1117175146\notin S_3\) 排除不分奇偶地取 \(k=3\)，但对 \(k\ge4\) 没有结论。

最近相关工作：最接近的近期工作是 Johnston–Trudgian（arXiv:2605.17825，2026 年预印本）：它将 GRH 下 Linnik–Goldbach 的“两素数”界改进到 6 个 2 的幂，并更新 Romanov 常数；这反映了相关筛法的进展，但不触及本题的一个素数全覆盖。未找到 2023–2026 年已发表或可审查预印本声称解决本题。

剩余核心：证明或否定存在统一常数 \(k\)，使单一素数与至多 \(k\) 个二进制幂之和覆盖所有充分大整数。正向需要从 Gallagher 的接近满密度升级到零例外集；反向需要对每个固定 \(k\) 构造任意大的不可表示整数。

已使用方法：

- 筛法与素数在等差数列中的分布（Gallagher/Romanov 路线）。
- 覆盖同余与 \(2\) 在模数下的阶，用以制造小 \(k\) 的不可表示数。
- 圆法和二进制幂指数和的大值集控制；这些在两素数 Linnik–Goldbach 问题中非常有效，但不能自动移植到单素数问题。
- 有限高度的位计数/素性计算，可验证候选反例或序列数据，但没有渐近终止证书。

争议或不确定性：

- Erdős Problems 的当前页面和 Formal Conjectures 均支持开放状态；检索中出现的“DISPROVED (LEAN)”摘要经追溯属于聚合页中其他题目的相邻文本，不是 #10 的可审计证明。
- OEIS A387053 的一条 2026 注记似乎把 Johnston–Trudgian 的两素数定理误投射到单素数序列；本审计不采用该注记。
- Crocker 文献中“正指数”与统一规范中的 \(2^0\) 约定需要逐一核读其边界情形；这不影响其仅为小 \(k\) 障碍、不能解决主问题的结论。

### 证据来源

- [Erdős Problem 10](https://www.erdosproblems.com/10) — Thomas F. Bloom (database editor), date unknown; `problem_page`, `database_record`, directness=`direct`, reliability=`high`. 页面检索记录显示该题仍标为 OPEN，页面最后编辑为 2026-04-11；其备注陈述 Gallagher 的密度定理、Granville–Soundararajan 的猜测及 Grechuk 的 \(k=3\) 反例。
- [Erdős Problem #10 discussion thread](https://www.erdosproblems.com/forum/discuss/10) — Erdős Problems forum, date unknown; `forum`, `informal_claim`, directness=`direct`, reliability=`medium`. 检索缓存显示论坛页称该题已被形式化，并且没有已声称的部分或完整解答；该页本身不是数学证明。
- [Primes and powers of 2](https://link.springer.com/article/10.1007/BF01390190) — P. X. Gallagher, 1975; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. Gallagher 的已发表结果是：对每个 \(\epsilon>0\)，存在 \(k(\epsilon)\) 使 \(S_{k(\epsilon)}\) 的下密度至少为 \(1-\epsilon\)；这不是最终覆盖全部大整数。
- [A Binary Additive Problem of Erdős and the Order of 2 mod p²](https://link.springer.com/article/10.1023/A:1009786614584) — Andrew Granville, K. Soundararajan, 1998; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 该文提出所有奇数 \(>1\) 可由一个素数和至多 3 个 2 的幂表示的猜测；这是猜测而非本题的证明。
- [On the Sum of a Prime and Two Powers of Two](https://projecteuclid.org/journals/pacific-journal-of-mathematics/volume-36/issue-1/On-the-sum-of-a-prime-and-two-powers-of-two/10.2140/pjm.1971.36.103.full) — R. C. Crocker, 1971; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. Crocker 给出两个 2 的幂情形的无穷障碍；它说明小固定项数会失败，但并不决定是否存在某个更大的固定 \(k\)。
- [Formal Conjectures: Erdős Problem 10 Lean statement](https://raw.githubusercontent.com/google-deepmind/formal-conjectures/main/FormalConjectures/ErdosProblems/10.lean) — The Formal Conjectures Authors, 2025; `formalization`, `formalized_artifact`, directness=`direct`, reliability=`high`. 文件精确采用“素数加至多 \(k\) 个 \(2^a\)”的多重集定义，但主命题及相关变体均以 `sorry` 结束；它是陈述形式化，不是已核验的 Lean 证明。
- [An update on the Linnik--Goldbach and Romanov problems](https://arxiv.org/abs/2605.17825) — Daniel R. Johnston, Tim Trudgian, 2026-05-18; `preprint`, `preprint`, directness=`indirect`, reliability=`high`. 该预印本研究两个素数加固定个 2 的幂，并讨论 Romanov 问题；其结果不处理本题所需的单个素数加有界个 2 的幂。
- [A387053: least number of powers of 2 needed after subtracting a prime](https://oeis.org/A387053) — David A. Corneth; OEIS contributors, 2025-09-20; `oeis`, `database_record`, directness=`indirect`, reliability=`medium`. 该序列将最少项数编码为 \(a(n)\)，并给出可复现实验程序。其关于 Johnston–Trudgian 的一条 GRH 注记与该预印本的“两素数”定理不匹配，不能作为本题进展的依据。

### 完成标准

- 肯定出口: Prove that there are fixed integers k,N0 such that every integer n >= N0 has n = p + sum_{i=1}^r 2^{a_i}, where p is prime, 0 <= r <= k, and all a_i >= 0.
- 否定出口: Prove that for every fixed k and every N0 there is an n >= N0 for which no representation n = p + sum_{i=1}^r 2^{a_i} with p prime, r <= k, and a_i >= 0 exists.

不构成完成：

- Showing that S_k has positive density, or even lower density 1, without proving eventual containment.
- Finding one counterexample for a particular k, including k=3.
- Verifying the claim through any finite bound, however large, without a theorem that closes the tail.
- Proving a theorem for two primes plus powers of 2, or for only one parity class unless the other class is also settled.
- Treating an unproved Lean declaration containing sorry as a formal proof.

正确性陷阱：

- Keep the quantifier order fixed: k must be independent of n.
- Allow 2^0=1 and the prime 2; explicitly justify any conversion to distinct exponents.
- Do not confuse an asymptotic density statement with an all-sufficiently-large statement.
- Audit every covering-congruence construction against all sums of at most k powers, including repeated powers and the p=2 case.
- If using a formal proof, build the full dependency closure and reject sorry, admit, axioms added for the target, and unverifiable computational oracles.

### 更新后的 AI 可解答性

- 等级: `low_candidate`
- 分数: `8/100`
- 信心: `high`
- 结论: 这是定义清楚、可验证但极难的开放解析数论问题；当前 AI 独立完整解决的机会很低。

支持理由：

- 肯定与否定方向都有精确的量词形式和可审计的完成标准。
- 已有密度定理、覆盖同余障碍和具体小 \(k\) 数据提供了明确的中间检验点。
- 重复幂的规范化和有限计算证书可被机械核查。

主要障碍：

- 核心差距是从“近乎所有”升级到“所有充分大整数”，或对每个 \(k\) 构造无穷障碍；两者都超出现有结果。
- 两素数 Linnik–Goldbach 的近期改进不能替代单素数问题，错误迁移是主要风险。
- 有限计算无法决定任一方向，且筛法常受 parity barrier 与例外集控制限制。

Proof-first 路线：

- 首先寻找能把任意固定 \(k\) 的全部二进制和覆盖为有限模条件、并迫使剩余数合数的统一覆盖同余引理；若失败，应明确记录其不能扩展的原因。
- 正向路线须提出一个严格的例外集消除引理，而非仅改进 Gallagher 的密度常数；先验证该引理是否与已知素数分布定理相容。
- 唯一可选计算任务只能服务于一个预先声明的模覆盖/候选反例引理，并输出可独立复验的素性与穷尽证书。

需要验证：

- 任何新文献或论坛的解决声称均需获得完整论文或无 `sorry` 的形式化工件后才可改变状态。
- 若使用 Crocker 型结果，须核实指数从正整数到非负整数以及 \(p=2\) 的边界处理。
- 应由数论专家检查是否存在未索引的 2023–2026 论文，特别是涉及 Romanov 问题、覆盖系统或极值加法基的工作。

### 审计限制与人工复核理由

- Erdős Problems 主页与论坛页在浏览器工具中返回 403；状态与论坛无解答信息来自同日搜索索引的页面摘录，而不是页面正文抓取。
- 未能取得 Gallagher、Crocker 和 Granville–Soundararajan 全文的每一页；其书目信息和本审计所用结论由期刊记录、可访问的相关正文摘录及当前问题页交叉核对。
- “未找到近期解决”是针对所列检索的证据判断，不是逻辑上排除所有未索引论文、私人手稿或未来勘误。

- 应由解析数论专家复核 Crocker 的指数约定与 \(p=2\) 边界是否完全对应当前规范化陈述。
- 若要将状态从 confirmed_open 改为 closed，必须取得并独立编译无 `sorry` 的形式化证明或审阅完整书面证明。
- 建议人工补做 MathSciNet/zbMATH/Google Scholar 的引文追踪，以覆盖未被一般网页索引的 2023–2026 文献。

<!-- DEEP_REVIEW:END -->
