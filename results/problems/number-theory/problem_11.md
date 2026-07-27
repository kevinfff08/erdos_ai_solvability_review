# Problem 11

## 基本信息

- 原始链接: https://www.erdosproblems.com/11
- LaTeX 页面: https://www.erdosproblems.com/latex/11
- 原始状态: `open`
- 奖金: `no`
- 主类别: `number theory`
- 原始标签: `number theory`, `additive basis`
- 形式化状态: `yes`
- OEIS: `A001220`, `A377587`
- 原站备注字段: 无

## 原问题

Is every large odd integer $n$ the sum of a squarefree number and a power of 2?

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `36/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 已有形式化陈述，可降低语义误读风险
- 存在 OEIS 数据入口，利于实验与反例搜索

### 主要障碍

- 所属标签偏证明密集：number theory
- 题面含渐近/无限对象线索：prime, primes

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: additive basis
- 证明密集标签命中: number theory
- 有限/计算线索: 无
- 渐近/无限线索: prime, primes
- 构造/存在性线索: find

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **低到中等候选：GPT-5.5 级别模型很可能能在计算验证、反例搜索、形式化已有等价变换和局部筛法方面推进该题，但独立给出完整无条件证明的概率较低。**
- 等级: `low_to_medium_candidate`
- 分数: `42/100`
- 信心: `medium`
- 可能路线: 可行路线主要是工具增强的筛法与可验证计算：把反例条件转化为对所有可用指数 k，n-2^k 都被某个平方 p^2 整除；用覆盖同余类、SAT/ILP 搜索、模小素数平方的周期性、以及大范围分布实验寻找可能的结构性障碍；同时形式化“若存在反例则满足某些覆盖系统/局部约束”的引理，并复现或扩展已知到 2^50 的验证。若要接近证明，可能需要把几乎所有 n 的结果强化为全体大奇数，或证明不存在能覆盖所有 2^k 候选的平方因子系统。

### 支持理由

- 问题陈述短、判定结构清楚，适合把候选表示 n=q+2^k 转成可计算的 squarefree 检验与模 p^2 筛选。
- 已有大范围验证到 2^50，说明计算框架相对明确；AI 可帮助复现、优化、形式化验证证书，或寻找更强的覆盖排除证据。
- 该题已形式化，降低了工具增强模型在证明检查、引理拆分、代码到证明证书连接上的门槛。
- Erdos 已有 almost all 结果，说明存在解析数论入口；模型可尝试把例外集估计、局部筛和计算覆盖结合，获得条件性或半有效推进。

### 主要障碍

- 完整命题要求“每个充分大的奇数”，不能只靠密度为 1 的结果；必须控制极稀有例外，这通常是解析数论中最困难的部分。
- 备注指出该题与 Wieferich primes 密切相关，并且若命题成立会推出正比例非 Wieferich primes；这暗示完整证明可能牵涉目前很难的素数模 p^2 分布问题。
- 反例排除需要同时处理约 log n 个 2 的幂候选以及大量平方因子覆盖，局部计算证据不容易自然外推到无限范围。
- 若使用 SAT/覆盖系统搜索，只能证明某些有限模数或有限范围无反例；把有限证书升级为无条件全局证明需要新的理论界。

### 需要的验证

- 复现 2^50 以内验证或至少用独立实现验证关键区间，并给出可审计的代码、哈希和抽样交叉检查。
- 形式化核心等价：n 不能表示当且仅当对每个允许 k，n-2^k 非 squarefree，并把非 squarefree 条件拆成某个 p^2 整除。
- 对任何提出的新证明，必须检查是否隐含使用未证明的 Wieferich primes 分布、ABC 型假设、GRH 或随机模型假设。
- 若得到计算证书，需要验证覆盖的模周期、边界条件、k 的范围、2^0 是否计入 power of 2、以及 squarefree 的符号/正性约定。

### 公开版思考摘要

这个问题非常适合 AI+工具做严密实验和局部证明：表示失败有明确的模平方覆盖结构，已有计算验证和形式化基础也能被复用。但它的全局版本比“几乎所有”强得多，并且备注明确把它连接到 Wieferich primes 这类深层分布问题。因此我判断 GPT-5.5 更可能提供显著的计算、形式化和条件性推进，而不是直接完成最终无条件证明。

### 免责声明

以上是对 GPT-5.5 级别模型可推进性的审查，不是该 Erdős 问题的解答或证明。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `confirmed_open`
- 状态信心: `high`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_11.md](../../prompts/problem_11.md)

### 状态结论

该问题目前仍可确认地开放。Erdős Problems 页面于 2026-04-05 更新后仍标记为 OPEN；其论坛至 2026-01 的所谓“归约”被网站维护者明确指出不成立且没有解决问题。Hercher 的 2025 年同行评审论文将有限验证推进至所有奇数 n≤2^50，但没有渐近证明或反例。针对精确表述、作者、主论文及 2025–2026 文献的检索未发现已发表或可审查的解决。

### 当前规范陈述

当前页面文字的字面目标是：是否存在整数 N，使每个奇整数 n≥N 都能写成 n=s+2^k，其中 s 为正平方自由整数，k 为正整数？“平方自由”指对每个素数 p 都有 p²∤s。k≥1 的约定来自 Hercher 2025 年论文和 OEIS A377587 的明确表述；这些来源记载的历史较强版本是“每个奇数 n>1”，而不只是充分大者。

```text
Literal current-page target: does there exist an integer N such that every odd integer n >= N can be written n=s+2^k, where s is a positive squarefree integer and k is a positive integer? Here squarefree means that p^2 does not divide s for every prime p. The choice k>=1 follows the explicit convention in Hercher's 2025 paper and OEIS A377587; the historical stronger wording found there is “every odd n>1,” not merely eventual coverage.
```

### 陈述、量词与反例审计

- 歧义严重度: `material`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 未发现针对 k≥1 版本的简单反例。Hercher 的同行评审有限验证覆盖所有奇数 n≤2^50；因此也排除了该范围内的反例。此结论不把有限计算误作对“充分大”命题的证明，也不声称已对范围外作穷尽检查。
- 版本变化: Erdős Problems 的历史页显示，2025-10-20 的页面文字由“每个整数”改为“每个充分大的奇数”，现行版本自 2026-04-05 保持后者。另一方面，Hercher 2025、OEIS A377587 和未证明的 Formal Conjectures 声明均记录“每个奇数 n>1”的较强历史版本。审计将页面字面最终命题作为主目标，并将较强版本单独记录。

陈述问题：

- 页面的“large”按通常约定可形式化为“存在统一 N”，但它比 Hercher 论文、OEIS 与 Lean 文件中出现的“每个奇数 n>1”弱；两者不能混为同一已解决或未解决命题。
- “power of 2”未在页面定义。Hercher 的算法及 OEIS A377587 明确只用正指数 k≥1；Formal Conjectures 文件则令指数为自然数，可能包括 0。后者含有 sorry，不能用来决定历史约定。
- 输入页面曾在 2025-10-20 把显示问题由“every integer”修改为“every large odd integer”；这显示范围文字有修订史。
- Erdős 还问过“4∤n”版本和两个 2 的幂版本；它们均不是当前单幂、奇数、最终全称目标。

需要固定的量词/约定：

- There exists one fixed threshold N; the representation parameters s and k may depend on n.
- n ranges over positive odd integers, and s is positive.
- For the convention supported by the computational paper and OEIS, k is an integer with k>=1. A k=0 convention gives a different weaker problem and must be labelled separately.
- The representation need not be unique.

### 文献与当前边界

已核验的主要结果：

- Hercher（2025，同行评审）验证了所有奇数 n≤2^50 均可写为平方自由数加正指数 2 的幂；其论文给出 GPU 筛法与算法说明。这是有限范围结果。
- Hercher 的文献综述转述 Odlyzko 的 10^7 检查和 McCranie 的 1.4×10^9 检查；原始计算档案在本次未取得，因此只将该历史信息作为二手报道。
- Granville–Soundararajan（1998，同行评审）研究该问题与 ord_{p²}(2)、Wieferich 现象的联系；期刊元数据、页面和论坛均确认其相关性。论坛特别指出覆盖系统是实质性组合障碍，并否定了“仅由 Σ_p 1/ord_{p²}(2) 收敛即可推出全称猜想”的非正式声称。
- Erdős Problems 页面记录 Erdős 对单幂版本有“几乎所有”结果，并提到两个幂的变体；由于原始出处没有在本次完整核验中取得，不应将其升级为带精确误差项的定理。

最近相关工作：最直接的最新正式工作是 Hercher 在 Journal of Integer Sequences 于 2025-04-14 发表的论文（预印本最初提交于 2024-11-04）。检索至 2026-07-27 未找到后续的完整证明、无限反例构造，或无 sorry 的形式化证明。

剩余核心：对于每个足够大的奇数 n，证明至少有一个正指数 k 使 n−2^k 为正平方自由数；或构造任意大的奇数 n，使全部相关 n−2^k 均含某个素数平方因子。有限枚举、密度一结论和仅允许两个幂都不能完成该目标。

已使用方法：

- 平方因子筛法与对 n−2^k 的分段并行检测。
- 用 ord_{p²}(2) 描述同余类 2^k≡n (mod p²) 及其覆盖/相关性。
- 关于表示数的均值、二阶矩与“几乎所有”结果的筛法思路。
- 有限范围的可复现计算，但它只能证明预先指定的有限引理。

争议或不确定性：

- 页面当前摘要称全表示会蕴含正比例非-Wieferich 素数；未证明的 Lean 文件注释则把一个关于 Wieferich 素数无限性的陈述归于 Granville–Soundararajan。因该文件有 sorry，且 1998 论文全文本次受访问限制，研究者必须查看原文核对定理号、假设和逻辑方向。
- “充分大奇数”页面表述与“每个奇数 n>1”历史表述不同；两者目前都未被解决，但后续工作不能不加说明地交换它们。
- 论坛中的 2026 年条件归约已被明确撤回/否定；不能作为可用引理。

### 证据来源

- [Erdős Problems — Problem 11](https://www.erdosproblems.com/11) — Thomas F. Bloom / Erdős Problems contributors, 2026-04-05; `problem_page`, `database_record`, directness=`direct`, reliability=`high`. 当前条目将问题列为 open，给出“large odd integer”表述、有限验证信息、历史变体和与 Wieferich 素数的关联摘要。
- [Erdős Problem #11 — Discussion thread](https://www.erdosproblems.com/forum/thread/11) — Thomas Bloom and forum contributors, 2026-01-24; `forum`, `informal_claim`, directness=`direct`, reliability=`high`. 论坛明确标注 OPEN。2026 年一项声称由阶倒数和收敛推出猜想的 AI 辅助论证，被 Bloom 指出不成立；该讨论也强调 Granville–Soundararajan 的覆盖系统障碍。
- [On the Sum of a Squarefree Integer and a Power of Two](https://cs.uwaterloo.ca/journals/JIS/VOL28/Hercher2/hercher24.html) — Christian Hercher, 2025-04-14; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 论文在 Journal of Integer Sequences 28 (2025), Article 25.3.1 发表，报告以 GPU 算法验证所有奇数 n≤2^50，并明确将其定位为有限数值验证。
- [On the Sum of Squarefree Integers and a Power of Two](https://arxiv.org/abs/2411.01964) — Christian Hercher, 2024-11-04; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 预印本 v1 的摘要与后续期刊论文一致，说明其目标是把有限验证延伸至 2^50，而非解决一般猜想。
- [A Binary Additive Problem of Erdős and the Order of 2 mod p²](https://link.springer.com/article/10.1023/A%3A1009786614584) — Andrew Granville and K. Soundararajan, 1998-03; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. Springer 元数据核实该论文为 Ramanujan Journal 2 (1998), 283–298，DOI 为 10.1023/A:1009786614584；它是本问题与模 p² 下 2 的阶及 Wieferich 现象的主要理论来源。全文在本次访问中受限，故不把未经逐页核对的定理方向作为独立事实。
- [OEIS A377587](https://oeis.org/A377587) — Christian Hercher; OEIS contributors, 2024-11-02; `oeis`, `database_record`, directness=`indirect`, reliability=`medium`. 条目明确把历史猜想写成每个奇数 1<m 可表示为 s+2^k，k 为正整数；还记录没有额外项低于 2^50。它用于核对指数约定与有限计算背景，而非解决状态的主要证据。
- [Formal Conjectures — Erdős Problem 11](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/11.lean) — Formal Conjectures contributors, 2025; `formalization`, `formalized_artifact`, directness=`direct`, reliability=`high`. Lean 文件形式化了“每个奇数 n>1”的主命题和若干变体，但所有相关声明均以 sorry 结束。因此它是未证明的形式化陈述，不是正式证明；其中关于 Granville–Soundararajan 的注释也不能替代原论文核验。

### 完成标准

- 肯定出口: Prove that there exists an integer N such that every odd n>=N has a positive integer k with 2^k<n and n-2^k squarefree.
- 否定出口: Prove that there are arbitrarily large odd integers n such that, for every positive integer k with 2^k<n, n-2^k is not squarefree. This refutes the eventual statement.

不构成完成：

- Checking all odd n below any fixed bound, including 2^50.
- Proving the assertion for a density-one or “almost all” set of odd integers.
- Using k=0 when the positive-exponent version is the stated target, or allowing two powers of two.
- A heuristic independence calculation for the events p^2 | n-2^k.
- A conditional implication without proving its arithmetic hypothesis.

正确性陷阱：

- Keep the current eventual target separate from the stronger “every odd n>1” historical version.
- For fixed n, only exponents with 2^k<n can yield a positive squarefree summand.
- A covering argument must cover every relevant exponent k, not a fixed initial interval or merely a density of exponents.
- Do not treat congruences for different prime squares as independent without a proof.
- Check the exact theorem in Granville–Soundararajan before invoking a Wieferich-prime consequence; secondary summaries and the sorry-containing Lean comment conflict.

### 更新后的 AI 可解答性

- 等级: `low_candidate`
- 分数: `14/100`
- 信心: `high`
- 结论: 这是一个清晰但深度很高的开放目标。AI 可协助建立、核验或否定精确的局部引理，却不应把扩大计算或启发式概率当作主要解决路线。

支持理由：

- 最终命题与反例命题均有明确、可审计的量词形式。
- 局部同余、乘法阶和覆盖系统提供可独立验证的中间任务。
- 2025 年论坛已暴露一种常见但错误的“求和收敛即完成”推理，适合设置对抗性证明审查。

主要障碍：

- 候选幂只有对数多个，相关的平方整除同余却可能形成精细覆盖；密度估计不足以排除所有例外。
- 关键背景涉及模 p² 下的阶和 Wieferich 型未知问题，可能需要超出现有筛法的输入。
- 有限计算即使远超 2^50，也不能证明存在统一阈值。

Proof-first 路线：

- 先从原论文逐页提取并形式化已知定理，特别是覆盖系统和 ord_{p²}(2) 的精确作用，建立可验证的引理账本。
- 尝试证明坏整数所诱导的同余覆盖系统不可能存在，或构造并认证一个能覆盖全部相关指数的无限族。
- 研究如何把“几乎所有”型估计强化为对例外集合的结构性排除；每一步须给出统一量词。
- 唯一可选计算任务：仅在先声明有限模数/周期引理、输入范围、证书与停止条件后，搜索或反驳该引理。

需要验证：

- 取得并审读 Granville–Soundararajan（1998）全文，核对所有被引用定理的精确逻辑方向。
- 审计 Hercher 2025 的程序、硬件假设、区间拼接和独立可重复性；这影响有限结果可信度，不影响其非渐近性质。
- 在 MathSciNet、zbMATH、arXiv 和作者主页再检索 2025-01-01 至 2026-07-27 的更新。
- 若采用 Formal Conjectures 文件，应先把 sorry 声明与已验证定理严格区分。

### 审计限制与人工复核理由

- Erdős Problems 的主页面与 LaTeX URL 对自动直接抓取返回 403；审计通过其可索引条目、历史页和论坛核对了当前内容。
- Granville–Soundararajan 1998 的 Springer 页面提供了完整书目信息但本次未开放全文；因此没有把相冲突的二手定理陈述视为已核实的数学事实。
- “未发现 2025–2026 解决”是有针对性的检索结果，不是对所有未公开、未索引或未来更新的逻辑排除。
- Hercher 的有限验证已在同行评审论文中报告，但独立重跑代码和硬件级审计不在本次网页审计范围内。

- 必须取得并逐页核对 Granville–Soundararajan 1998 全文，特别是关于 Wieferich/非-Wieferich 与覆盖系统的定理方向；当前二手来源与 sorry 状态的 Lean 注释不一致。
- 若研究要使用“强历史版本”或 k=0，须先由人工决定采用哪一规范并在任务中明确它与页面最终版本的关系。
- 在实质投入前，建议用 MathSciNet、zbMATH、arXiv 和作者主页作一次人工更新核验，并审阅 Hercher 2025 的计算实现。

<!-- DEEP_REVIEW:END -->
