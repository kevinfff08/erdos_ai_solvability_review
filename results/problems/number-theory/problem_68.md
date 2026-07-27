# Problem 68

## 基本信息

- 原始链接: https://www.erdosproblems.com/68
- LaTeX 页面: https://www.erdosproblems.com/latex/68
- 原始状态: `open`
- 奖金: `no`
- 主类别: `number theory`
- 原始标签: `number theory`, `irrationality`
- 形式化状态: `yes`
- OEIS: `A331373`
- 原站备注字段: 无

## 原问题

Is\[\sum_{n\geq 2}\frac{1}{n!-1}\]irrational?

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `33/100`
- 建议路线: 优先文献定位、特殊情形、数值实验和辅助引理搜索；完整证明需要新的数学思想。

## 判断依据

### 有利因素

- 已有形式化陈述，可降低语义误读风险
- 存在 OEIS 数据入口，利于实验与反例搜索

### 主要障碍

- 所属标签偏证明密集：irrationality, number theory
- 缺少明显有限搜索入口。

### 公开版思考过程摘要

- 先识别问题类型：无限/渐近或抽象证明倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: irrationality, number theory
- 有限/计算线索: 无
- 渐近/无限线索: 无
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **低到中等候选。该问题陈述极短、对象可高精度计算且已形式化，适合 AI 配合计算和形式化工具做严密验证、反例式模式搜索、等价重写和部分引理推进；但要完整证明无理性，核心仍是一个缺少明显结构的经典数论无理性问题，现有信息没有给出可直接机械化的突破口。**
- 等级: `low_to_medium_candidate`
- 分数: `38/100`
- 信心: `medium`
- 可能路线: 最现实的路线不是直接猜出完整证明，而是围绕恒等式 1/(n!-1)=sum_{k>=1}(n!)^{-k} 建立可验证的归约：先形式化收敛、尾项界、截断有理近似与分母结构；再用计算搜索寻找可证明的整除、同余或线性递推结构；同时尝试把该数嵌入已知的 Mahler 型、Cantor 级数、快速收敛级数或 Erdős 式无理性准则框架中。若发现一个适配的无理性判据，GPT-5.5 级模型可能帮助补齐大量技术细节并用证明助手验证。

### 支持理由

- 级数定义简单，收敛极快，数值实验、连分数、Padé 近似、同余搜索和尾项界都容易自动化。
- 给出的双重级数展开提供了可操作的结构入口，可把问题转为关于 factorial-base 类稀疏展开或多重指数衰减项的无理性分析。
- 该条目标注为 formalized=yes，说明至少陈述层面适合进入 Lean/Isabelle 等环境；AI 可显著帮助把候选引理、截断误差和计算证书形式化。
- 若目标降为“显著推进或验证某个候选证明”，模型能力会比较有价值，尤其是在排查错误证明、生成精确尾界、验证大规模同余模式方面。

### 主要障碍

- 单靠快速收敛不足以证明无理性；截断有理数的误差大约与 factorial 尾项相关，但分母增长也极快，通常不能直接给出 Liouville 型矛盾。
- 分母 n!-1 之间没有简单的嵌套整除结构，和经典 Cantor 级数或 Engel 展开相比缺少直接可用的唯一展开判据。
- 备注中提到更强的超越性预期 sum 1/(n!+t)，说明该问题可能属于一个更深的未解决族，而不是只差常规技巧。
- 形式化证明只能验证已找到的数学思路，不能自动弥补核心无理性判据缺失；搜索得到的数值规律也可能只是有限范围伪模式。

### 需要的验证

- 对任何候选证明，必须形式化验证级数交换、绝对收敛和尾项估计，避免把启发式近似当作无理性证明。
- 需要用精确整数/有理数计算复查截断分母、连分数异常逼近、同余模式和可能的递推关系，而不是依赖浮点小数。
- 若使用某个已知无理性或超越性准则，必须逐条核对该级数满足准则的增长、整除、非周期性或代数独立条件。
- 需要独立检查由 AI 生成的文献映射和命题引用，因为本次判断只基于给定 problem JSON，不能把未核实的外部定理当作已知事实。

### 公开版思考摘要

这是一个 AI 工具链可以很好参与的开放数论问题：对象明确、计算友好、可形式化，且双重级数展开给出了一些可能的结构化切入点。GPT-5.5 级模型有机会提出并验证有价值的归约、排除错误路线、建立严密计算证书，甚至在碰到合适无理性判据时完成证明。但从给定信息看，核心难点是缺少能把 n!-1 分母结构转化为无理性的现成机制，因此完整解决概率不高，显著推进概率中等偏低。

### 免责声明

以上是可解性与工具辅助潜力评估，不是该级数无理性的证明，也不声称已经解决 Erdős problem 68。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `likely_open`
- 状态信心: `medium`
- 可行动性: `research_ready`
- 人工复核: `not_required`
- 独立研究 Prompt: [prompts/problem_68.md](../../prompts/problem_68.md)

### 状态结论

截至审计日，字面问题很可能仍开放。Erdős Problems 的当前条目将其列为 OPEN，并明确提示该标签仅代表维护者的当前认知；DeepMind Formal Conjectures 中对应条目也标为 research open，且主定理仍是 `answer(sorry)`，并非证明。对精确级数、其 t=-1 变体、近年 arXiv 和形式化库的定向检索未发现可审阅的解决或反例。由于“未检出文献”不能证明不存在遗漏，结论为 likely_open 而非 confirmed_open。

### 当前规范陈述

对每个整数 \(n\ge2\)，令 \(n!=1\cdot2\cdots n\)，并定义绝对收敛的正实级数 \[S:=\sum_{n=2}^{\infty}\frac1{n!-1}.\] 问题是判定 \(S\notin\mathbb Q\)，即该特定实数是否为无理数。

```text
Let \(n!=1\cdot2\cdots n\) for integers \(n\ge2\), and define the absolutely convergent positive real series \[S:=\sum_{n=2}^{\infty}\frac1{n!-1}.\] Determine whether \(S\notin\mathbb Q\). Equivalently, decide whether this particular real number is irrational.
```

### 陈述、量词与反例审计

- 歧义严重度: `none`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 未发现使精确字面命题失效的简单恒等式、有限截断或已发表反例。针对不同快速收敛级数的有理值构造不能转移到固定的分母 \(n!-1\)，故不构成反例。
- 版本变化: 未发现对本题本身的已确认改写或拆分。Erdős 1988 年提出的更强猜想是：对每个整数 \(t\)，\(\sum 1/(n!+t)\) 应超越；本题对应 \(t=-1\)，但“更强猜想”不是对本题的已证推广。2025 年的 Lean 文件将原命题精确形式化为从 \(n+2\) 开始的实数无理性断言，同时形式化了逐项几何级数恒等式；主问题仍以 `sorry` 占位。

陈述问题：

- “无理”应明确为不属于 \(\mathbb Q\)；原句虽简短，但在通常数论语境下无歧义。
- 原条目所述双重级数恒等式需要绝对收敛/非负项 Tonelli 定理来交换求和次序；它不是无理性的证明。

需要固定的量词/约定：

- The index ranges over every integer n >= 2.
- The sum is the ordinary limit of its real partial sums.
- The target is the single assertion S notin Q; no asymptotic parameter is present.
- All denominators are positive for n >= 2, and convergence follows, for example, by comparison with 2/n!.

### 文献与当前边界

已核验的主要结果：

- Erdős（1988）记录了本题，并提出对所有整数 \(t\) 的 \(\sum 1/(n!+t)\) 超越性猜想；对本题而言这是猜想背景，不是已证定理。
- Formal Conjectures 的 68.lean 已精确表达主问题，但主断言未证明；该文件仅证明了每个固定 \(n\) 的几何级数化简，并由此给出 n-先求和的恒等式。
- Schlage-Puchta（2011，预印本）在其他阶乘级数上使用均匀分布和数论方法得到无理性/线性无关结果；目前没有检出的论证把该结果推至 \(1/(n!-1)\)。
- Barreto、Kang、Kim、Kovač、Zhang（2026，预印本）为相邻乘积型快速收敛级数给出新无理性判据，但分母结构与 \(n!-1\) 不同。
- Crmarić、Kovač（2025，预印本）在不同的可变乘积型家族中构造有理和，警示不能只凭快速收敛作一般性推论。

最近相关工作：最接近的近期方法学文献是 Barreto 等人的 2026 年 arXiv 预印本（arXiv:2601.21442）。其定理涉及 \(\sum 1/(a_n\cdots a_{n+d-1})\)，没有涉及、也没有声称解决 \(\sum_{n\ge2}1/(n!-1)\)。定向精确检索未发现 2023–2026 年针对本常数的可审阅解决论文。

剩余核心：仍待解决的核心正是：严格证明 \(S=\sum_{n=2}^{\infty}1/(n!-1)\notin\mathbb Q\)，或（若猜想失败）证明 \(S\in\mathbb Q\) 并给出精确值。现有双重级数表示和数值小数均未建立任一结论。

已使用方法：

- 把每项展开为 \(1/(n!-1)=\sum_{k\ge1}(n!)^{-k}\)，并以非负项 Tonelli 定理控制双重求和。
- 假设有理后乘以适当整数，研究尾和到整数的距离；该路线必须同时解决分母 \(n!-1\) 缺乏阶乘整除嵌套的问题。
- 阶乘分母级数中的均匀分布、丢番图逼近和整数线性型方法可作背景，但尚无已验证的直接转移。
- 若出现新论证，可先将主定义和必要的绝对收敛/级数恒等式扩展到现有 Lean 形式化，再检验核心数论引理。

争议或不确定性：

- Erdős Problems 自身声明其 open 标签可能遗漏文献，因此它不能单独确认开放性。
- GitHub 议题被关闭只表示形式化条目工作流状态，而不是数学问题被解决；源文件仍把主定理标为 research open 且使用 `sorry`。
- 近期快速收敛级数论文的正面和反面结果均属不同分母家族，不能据此推断本题真伪。
- 未发现论坛中的解决声明；问题页报告 0 comments。检索未穷尽所有非数字化文献，故状态置信度为中等而非高。

### 证据来源

- [Erdős Problems — Problem 68](https://www.erdosproblems.com/68) — Thomas F. Bloom / Erdős Problems, date unknown; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 当前数据库条目将问题标作 OPEN，给出精确陈述、Weisenberg 的双重级数观察及 Erdős 1988 年参考；页面同时明言 open 标签仅代表维护者的认知并要求自行检索。检索结果显示该页最后编辑于 2025-09-28，且没有评论线程。
- [Erdős Problems — LaTeX for Problem 68](https://www.erdosproblems.com/latex/68) — Thomas F. Bloom / Erdős Problems, date unknown; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 复核了原始题面、双重级数表达式和唯一列出的文献 [Er88c] 的书目信息。
- [On the irrationality of certain series: problems and results](https://combinatorica.hu/~p_erdos/1988-22.pdf) — Paul Erdős, 1988; `primary_paper`, `unknown`, directness=`direct`, reliability=`high`. Erdős 1988 年在《New Advances in Transcendence Theory (Durham, 1986)》第 102–109 页发表的原始来源，可审阅其历史问题语境；数据库将本题及关于 \(\sum 1/(n!+t)\) 的更强超越性猜想归于该文。
- [Formal Conjectures — ErdosProblems/68.lean](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/68.lean) — Formal Conjectures Authors, 2025; `formalization`, `formalized_artifact`, directness=`direct`, reliability=`high`. 文件将主命题形式化为 \(\operatorname{Irrational}(\sum'_{n:\mathbb N}1/((n+2)!-1))\)，标注为 research open，主定理含 `answer(sorry)`，因此没有形式化解决。它还给出了逐个 \(n\) 的几何级数求和，从而形式化相应的 n-先求和恒等式。
- [Irrationality of rapidly converging series: a problem of Erdős and Graham](https://arxiv.org/abs/2601.21442) — Kevin Barreto, Jiwon Kang, Sang-hyun Kim, Vjekoslav Kovač, Shengtong Zhang, 2026-01-29; `preprint`, `preprint`, directness=`indirect`, reliability=`high`. 该文证明了另一类 \(\sum 1/(a_n\cdots a_{n+d-1})\) 快速收敛级数的无理性判据及某些反例；其对象不是固定的 \(1/(n!-1)\)，不能作为本题的解决，但说明相邻乘积型快速收敛级数在 2026 年仍有活跃且精细的研究。
- [On the irrationality of certain super-polynomially decaying series](https://arxiv.org/abs/2504.18712) — Tonći Crmarić, Vjekoslav Kovač, 2025-04-25; `preprint`, `preprint`, directness=`indirect`, reliability=`high`. 该文对另一类可变乘积分母级数构造了可取任意正实值的情形，说明“衰减极快”本身不足以推出无理性；其构造不适用于固定阶乘减一分母。
- [The irrationality of some number theoretical series](https://arxiv.org/abs/1105.1451) — Jan-Christoph Schlage-Puchta, 2011-05-07; `preprint`, `preprint`, directness=`indirect`, reliability=`high`. 提供了阶乘分母级数中结合初等/解析数论与均匀分布方法的已证结果；文中处理的系数型 \(1/n!\) 级数并非 \(1/(n!-1)\)，故只能作为方法学背景。

### 完成标准

- 肯定出口: Produce a complete rigorous proof that S = sum_{n=2}^infinity 1/(n!-1) is not rational. A formal Lean proof of the exact real-series statement, or a conventional proof whose every convergence, integrality, and limiting step can be checked, qualifies.
- 否定出口: Produce a complete rigorous proof that S is rational, including an exact pair of integers p,q with q>0 and S=p/q; a certified construction must prove equality to the infinite series, not merely fit numerical digits.

不构成完成：

- Computing more decimal digits of A331373, detecting no apparent period, or PSLQ on finite precision.
- Establishing an identity for a related sum, including sum 1/n!, sum 1/(q^n+r), or a different factorial series, without a valid exact reduction.
- Citing Erdős's stronger transcendence conjecture for sum 1/(n!+t) as though it were a theorem.
- Showing only the geometric expansion of each summand or only a finite truncation statement.
- An argument that bounds a tail but does not establish the required integrality of the scaled partial sum and scaled rational target.

正确性陷阱：

- Keep the lower index n=2; n=0 or n=1 makes n!-1 zero.
- Do not replace the fixed denominator n!-1 by n!, n!+1, or n!+t without proving an equivalence.
- If switching the n and k sums, invoke nonnegativity/absolute convergence explicitly.
- In a rationality contradiction, the multiplier must clear every finite partial denominator actually used; factorial divisibility does not automatically clear n!-1.
- A positive quantity being small is not contradictory unless it is also proved to be a nonzero integer or has a rigorously separated fractional part.
- The existing Lean file formalizes the conjecture and a geometric identity, not a proof of irrationality.

### 更新后的 AI 可解答性

- 等级: `low_candidate`
- 分数: `12/100`
- 信心: `medium`
- 结论: 这是定义清楚、可形式化但长期未解的单一数论无理性问题；适合进行严谨的探索性研究，但目前不应期待短期自动解决。评分只针对仍存的精确命题。

支持理由：

- 目标是单个明确的 \(S\notin\mathbb Q\) 断言，完成标准二元且可独立核验。
- 已有 Lean 陈述和几何级数辅助结果，可降低定义、收敛与部分代数验证成本。
- 近期相邻领域对快速收敛级数的进展提供可比较的技术图景。

主要障碍：

- 该题至少自 1988 年即被明确记录，精确检索未发现直接定理，表明朴素的阶乘尾项法很可能不足。
- \(n!-1\) 的分母没有 \(n!\) 那样的嵌套整除性，常见 Fourier 型乘阶乘论证不能直接套用。
- 数值计算难以给出有理性或无理性的有限证书；不同快速衰减家族甚至允许有理和。

Proof-first 路线：

- 优先寻找一个精确的“有理性假设 \(\Rightarrow\) 可验证整数/分数部分矛盾”引理，并先完整审计其分母清除和尾项界。
- 独立考察双重级数表示是否产生可控的阶乘基展开、模结构或线性型；任何重排必须由非负性/绝对收敛支持。
- 把文献中的快速收敛判据逐条与 \(n!-1\) 的实际分母比较；只有验证其假设后才可引用。
- 若出现候选证明，尽早将其关键引理在 Lean 中表达，以暴露类型、指数、求和次序和极限量词错误。

需要验证：

- 继续追踪 Erdős 1988 年文献的引文网络、MathSciNet/zbMATH 和作者主页，以降低遗漏旧文献的风险。
- 若有新预印本或论坛声称解决，必须逐行确认其对象恰为 \(\sum_{n\ge2}1/(n!-1)\)，并由独立审稿者检查。
- 在利用现有 Lean 文件前，确认所用提交版本已通过项目 CI，且不把 `sorry` 声明误作定理证明。

### 审计限制与人工复核理由

- 本审计进行了精确式、相关表述、形式化库和近年 arXiv 的定向公开检索，但不能穷尽未数字化论文、付费数据库全文或尚未索引的预印本。
- Erdős 1988 年 PDF 的可获得版本和数据库记录足以核对出处与问题背景；本审计没有把无法逐页复核的更广泛历史叙述当作本题已证结果。
- “likely_open”是基于正向开放标签与未发现可审阅解决的证据性判断，不是对全球文献不存在解决的逻辑证明。
- 近期预印本只被用作相邻方法和风险背景；没有将其结论外推到本题。

- 无

<!-- DEEP_REVIEW:END -->
