# Problem 15

## 基本信息

- 原始链接: https://www.erdosproblems.com/15
- LaTeX 页面: https://www.erdosproblems.com/latex/15
- 原始状态: `open`
- 奖金: `no`
- 主类别: `number theory`
- 原始标签: `number theory`, `primes`
- 形式化状态: `yes`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

Is it true that\[\sum_{n=1}^\infty(-1)^n\frac{n}{p_n}\]converges, where $p_n$ is the sequence of primes?

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `29/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- 题面或备注出现有限对象/计算线索
- 已有形式化陈述，可降低语义误读风险

### 主要障碍

- 所属标签偏证明密集：number theory, primes
- 题面含渐近/无限对象线索：infinitely many, prime, primes

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: number theory, primes
- 有限/计算线索: compute, finite, finitely
- 渐近/无限线索: infinitely many, prime, primes
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **有一定推进潜力，但不宜评为高可解候选。GPT-5.5 级别模型配合计算和形式化工具，较可能复现、组织和验证条件性路线，发现等价重述、数值证据和局部引理；但要无条件证明原级数收敛，核心仍落在精细的素数间隙与奇偶索引相关性控制上，远超常规自动化证明和反例搜索能力。**
- 等级: `low_to_medium_candidate`
- 分数: `42/100`
- 信心: `medium`
- 可能路线: 最现实的路线是把级数按相邻奇偶项配对，将收敛性转化为关于 n/p_n 的相邻差分求和问题；差分中自然出现素数间隙 p_{n+1}-p_n 与平均量 p_n/n 的偏差。模型可以用计算实验估计部分和漂移、用形式化工具验证代数变形和条件性引理，并尝试在强 Hardy-Littlewood 型假设下重构已有条件证明。若要无条件解决，则需要新的、足够强的素数间隙分布和奇偶位置相关性估计。

### 支持理由

- 题目短、结构清晰，适合模型进行代数重写、配对化、差分公式推导和数值实验。
- 备注已经指出 Erdős 认为计算探索有价值，这与工具增强模型的能力匹配。
- 备注还给出 Tao 在强 Hardy-Littlewood 素数元组猜想下证明收敛，说明存在明确的条件性解析路线可供模型复现、形式化或局部推广。
- 该问题已经标记 formalized=yes，因此至少问题陈述或相关对象具备形式化入口，模型可在证明助手中做定义、等价变换和有限验证。
- 反例搜索在这里可用于发现部分和的异常漂移或猜测所需误差项，虽然不能直接证明发散或收敛。

### 主要障碍

- 原问题是无条件收敛性，不能只靠 Dirichlet 或 Leibniz 判别法，因为 n/p_n 不是简单单调趋零的交错项序列。
- 配对后的项涉及素数间隙相对平均间隙的细微偏差，所需的是长期累积取消，而非单点估计。
- 现有备注显示强 Hardy-Littlewood 假设足以证明，暗示无条件证明可能需要当前素数分布理论中非常精细且尚不可得的输入。
- 计算只能覆盖有限范围；由于项约为 1/log n 量级，收敛或发散的数值迹象可能极慢，容易误导。
- 形式化证明工具可验证推导，但无法自动生成缺失的深层解析数论估计。

### 需要的验证

- 验证配对差分公式及其与原级数收敛性的等价关系。
- 进行大规模高精度部分和计算，记录不同截断、配对方式和误差控制下的稳定性。
- 复核条件性 Hardy-Littlewood 路线中实际需要的假设强度，并检查模型推导是否偷用了未证明的均匀性。
- 在证明助手中形式化基本定义、差分恒等式、收敛判据转换和任何条件性命题的依赖关系。
- 若模型声称无条件证明，必须由专家逐行审查关键素数间隙估计，尤其是奇偶索引相关性和误差项求和。

### 公开版思考摘要

该问题的可攻部分在于结构非常紧凑：交错求和可以通过相邻项配对转化为关于 n/p_n 差分的级数，而差分又直接连接到素数间隙。GPT-5.5 很可能能把这些关系整理成可验证的条件性框架，并用计算给出有价值的证据。不过，真正决定无条件收敛的是素数间隙偏差在奇偶索引上的长期抵消，这属于深层解析数论难点。因而它适合作为“工具增强模型可显著整理和验证条件路线”的候选，但不是强烈的“AI 可直接解决”候选。

### 免责声明

以上不是该 Erdős 问题的解答，也不声称证明了级数收敛或发散；它只是对 GPT-5.5 级别模型在工具辅助下可能推进该问题的可行性评估。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `confirmed_open`
- 状态信心: `medium`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_15.md](../../prompts/problem_15.md)

### 状态结论

该精确定义的原问题仍为公开未解问题。2024 年 Tao 已在一个足够强的 Hardy--Littlewood 素数 k-元组猜想下证明其收敛，但未给出无条件证明。问题页当前仍标记为 open，论坛未列出任何解答声明；截至审计日的定向检索未发现可核验的无条件证明或反例。

### 当前规范陈述

设 p_n 为递增排列的第 n 个素数（p_1=2）。令 S_N=\sum_{n=1}^N(-1)^n n/p_n。是否存在有限实数 L，使得当 N\to\infty 时 S_N\to L？

```text
Let p_n be the n-th prime in increasing order, with p_1=2. Define S_N := sum_{n=1}^N (-1)^n n/p_n. Does there exist a finite real number L such that lim_{N->infinity} S_N=L?
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 未发现能推翻字面命题的简单构造；该命题关于固定的素数序列，而非可自由选择的一般递增序列。交错级数判别法不能直接使用，因为 n/p_n 并不已知最终单调；这不是反例。
- 版本变化: 没有发现原主问题被更正或替换。Erdős 还提出了若干涉及相邻素数间隙的不同级数；它们是附加问题而非本题的修订。Tao 2024 的结果是原命题在强 Hardy--Littlewood 假设下的条件性肯定答案，并未把无条件目标缩小或解决。

陈述问题：

- 输入中的“p_n is the sequence of primes”应明确为按严格递增次序排列的第 n 个素数；否则索引约定不充分。
- “converges”必须指通常的实数级数收敛，即自然顺序部分和 S_N 收敛；不是 Cesàro、Abel、重排或数值正则化意义的收敛。
- 若收敛，它不是绝对收敛：由 p_n\sim n\log n，正项绝对值 n/p_n\sim1/\log n，其和发散。

需要固定的量词/约定：

- p_n is uniquely the n-th prime for every integer n>=1, ordered increasingly.
- Convergence means convergence of the ordinary sequence of natural-order partial sums (S_N)_{N>=1} in R.
- The question is unconditional: assuming Hardy--Littlewood, RH, or a probabilistic prime model does not resolve the stated target.

### 文献与当前边界

已核验的主要结果：

- Erdős提出无条件收敛问题；原始引用见问题页和 Tao 论文导言。
- Tao（2024，同行评审）在足够强的定量 Hardy--Littlewood 素数 k-元组猜想下证明该级数收敛。其工具包括 Banks--Ford--Tao 随机筛模型、Gallagher 型短区间素数元组计算、Bonferroni 界和二阶矩集中估计。
- Tao 记录了 Mustafa Said 的等价转换：原级数收敛当且仅当 \sum_{m\ge2}(-1)^{\pi(m)}/(m\log m) 收敛（改动有限个起点不影响结论）。
- 由分部求和可直接推出一个无条件充分目标：若 F(x)=\sum_{m\le x}(-1)^{\pi(m)}=O(x/(\log x)^\varepsilon)（某个 \varepsilon>0），则该级数收敛。这只是充分条件，尚未建立。
- Mantzakouras（2025，预印本）不构成对原问题的无条件解答；其摘要所述结果涉及不同的积分/阻尼设置，并且讨论 RH 假设。

最近相关工作：截至 2026-07-27，最晚发现的直接条目是 Erdős Problems 论坛中 2026-01-13 的非同行评审评论，提出短区间素数计数的奇偶混合或反集中作为可能的中间目标。最新已核验的同行评审主结果仍是 Tao 2024 的条件性定理。

剩余核心：无条件地证明或否证自然顺序部分和 \sum_{n\le N}(-1)^n n/p_n 的收敛。等价地，需要对 (-1)^{\pi(x)} 的加权平均获得足够强的抵消；仅有 \pi(x) 奇偶性的密度均分并不足以保证该加权级数收敛。

已使用方法：

- 将索引从第 n 个素数改写为素数计数函数 \pi(x) 的奇偶性。
- 通过分部求和把问题归结为 F(x)=\sum_{m\le x}(-1)^{\pi(m)} 的定量抵消。
- 在强定量 Hardy--Littlewood 输入下，用短区间 Poisson 行为、van der Corput 差分及随机筛模型制造奇偶抵消。
- 数值部分和可用于检验精确定义的启发式或寻找反常模式，但不能证明无穷级数收敛。

争议或不确定性：

- 搜索不能逻辑上排除未索引的新稿或未公开证明；因此开放状态置信度为中等而非绝对。
- 2025 Mantzakouras 预印本标题与原题相近，但其摘要未声称证明原无条件级数；在把它作为任何更强结论的依据前须人工逐页核查。
- 论坛中的 2026 中间猜想和路线是非同行评审研究建议，不应误报为已证定理。

### 证据来源

- [Erdős Problem #15](https://www.erdosproblems.com/15) — Thomas F. Bloom (database editor), date unknown; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 数据库将主问题列为 open，并把 Tao 的结果说明为依赖强 Hardy--Littlewood 素数元组猜想的条件性结果。页面自身明确提示其开放状态不是完整文献检索的替代品。
- [Erdős Problem #15 forum thread](https://www.erdosproblems.com/forum/thread/15?embed=1) — Erdős Problems contributors; Przemek Chojecki; Desmond Weisenberg, 2026-01-13; `forum`, `informal_claim`, directness=`direct`, reliability=`medium`. 线程仍显示 OPEN，且称没有评论中的部分或完整解答声明。其 2026 评论给出与 F(x)=\sum_{n\le x}(-1)^{\pi(n)} 有关的充分条件和研究建议；这些不是无条件证明。
- [The convergence of an alternating series of Erdős, assuming the Hardy–Littlewood prime tuples conjecture](https://doi.org/10.1090/cams/29) — Terence Tao, 2024-02-01; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. Tao 证明：在一个足够强的 Hardy--Littlewood 素数 k-元组猜想下，\sum_{n\ge1}(-1)^n n/p_n 收敛；该文仍将无条件问题称为 open。
- [The convergence of an alternating series of Erdős, assuming the Hardy--Littlewood prime tuples conjecture](https://arxiv.org/abs/2308.07205) — Terence Tao, 2023-08-14; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 可公开核对的预印本版本、摘要和修订记录；与已发表的 2024 论文对应。
- [The convergence of an alternating series of Erdős, assuming the Hardy–Littlewood prime tuples conjecture](https://terrytao.wordpress.com/2023/08/14/the-convergence-of-an-alternating-series-of-erdos-assuming-the-hardy-littlewood-prime-tuples-conjecture/) — Terence Tao, 2023-08-14; `author_page`, `informal_claim`, directness=`direct`, reliability=`high`. 作者解释了与 \sum (-1)^{\pi(m)}/(m\log m) 的等价、短区间素数计数奇偶性障碍、Gallagher 型计算以及随机筛模型在条件证明中的作用。
- [Holder continuity of an alternating Erdos series on prime K-tuples](https://arxiv.org/abs/2505.06242) — Nikos Mantzakouras, 2025-04-27; `preprint`, `preprint`, directness=`direct`, reliability=`medium`. 该未同行评审预印本研究的是 Riemann--Stieltjes 表示及带指数阻尼测试函数的积分，并在 RH 假设下讨论；摘要本身仍称原题 open，不能作为原无条件级数收敛的证明。
- [FormalConjectures: Erdős Problem 15](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/15.lean) — Formal Conjectures Authors, 2026-04-17; `formalization`, `formalized_artifact`, directness=`direct`, reliability=`high`. Lean 文件精确表达了以 0 索引 nth-prime 表示的 Summable 命题，但定理体为 sorry；这是待证陈述的形式化，而不是已核验的形式化证明。

### 完成标准

- 肯定出口: Provide a rigorous unconditional proof that the natural-order partial sums S_N=sum_{n<=N}(-1)^n n/p_n form a Cauchy sequence in R (equivalently, converge to a finite real limit). Every invoked estimate on primes must be proved or explicitly cited as an established unconditional theorem.
- 否定出口: Provide a rigorous unconditional proof that (S_N) does not converge in R, for example by proving two subsequences with distinct limits, or by proving unboundedness/another failure of the Cauchy criterion.

不构成完成：

- A proof conditional on Hardy--Littlewood, RH, a random-prime model, or any other unproved hypothesis.
- Numerical stabilization of partial sums, no matter how large the cutoff.
- Showing only that n/p_n tends to zero, or invoking the alternating-series test without proving eventual monotonicity of n/p_n.
- Proving equidistribution of pi(m) modulo 2 at density level only; it does not by itself control the weighted series.
- Proving convergence of a smoothed, damped, Cesàro/Abel-regularized, reordered, or different prime-gap series.
- A Lean statement containing sorry or an unchecked axiom.

正确性陷阱：

- Keep the sign and indexing fixed: p_1=2 and the first term is -1/2 under the stated convention.
- Distinguish ordinary convergence from absolute convergence; absolute convergence is ruled out by p_n~n log n.
- A bound for the mean of (-1)^{pi(n)} must be quantitatively strong enough after partial summation; qualitative cancellation or parity-density statements need not suffice.
- When using the equivalence with sum (-1)^{pi(m)}/(m log m), prove/control the error terms and note that changing finitely many initial terms is harmless.
- Do not silently replace the strong quantitative Hardy--Littlewood hypothesis used by Tao with the usual informal prime-tuples conjecture.
- Audit any claimed short-interval distribution result for its uniformity in tuple size, interval length, and error term.

### 更新后的 AI 可解答性

- 等级: `low_candidate`
- 分数: `12/100`
- 信心: `high`
- 结论: 这是表述良好且可独立核验的开放证明目标，但其核心要求对素数短区间计数奇偶性取得目前远超已知无条件技术的定量控制；AI 适合协助拆分、审计和形式化中间引理，不应把数值实验当作主路线。

支持理由：

- 目标具有清晰的二值完成标准，且有精确形式化陈述可供核对。
- Tao 的条件性证明及等价转换给出可审计的结构和若干可分离的中间引理。
- 任何真正推进都必须产生可验证的无条件解析数论估计，而不是仅给启发式。

主要障碍：

- 现有最强直接结果依赖强定量 Hardy--Littlewood 素数 k-元组输入。
- 所需抵消处在临界加权尺度；普通素数定理、项趋零或有限计算均不足。
- 近似的奇偶均分或弱平均界不能自动推出加权级数收敛。

Proof-first 路线：

- 首先完整重建并审计 Tao 的等价与分部求和链条，明确每个足够条件的最弱精确形式。
- 尝试证明一个独立、无条件且足以推出 F(x)=O(x/(\log x)^\varepsilon) 的短区间奇偶混合定理；若只能得到较弱界，严格量化其为何不足。
- 将可形式化的解析变换、有限起点处理和“某估计蕴含收敛”的引理送入证明助理，以缩小人工审计面。
- 最多使用一次计算任务，仅用于检验预先声明的有限尺度短区间奇偶性猜想或反例模式；不得将其结果提升为渐近证明。

需要验证：

- 对任何声称使用 RH 或素数元组猜想的证明，逐项确认其是假设还是已证定理。
- 对 2025 预印本的正文进行人工范围审计，确认其没有未在摘要中体现的原问题无条件结论。
- 若发现 2026 新稿或论坛声明，必须取得完整文本并由独立审稿者检查关键短区间误差估计。

### 审计限制与人工复核理由

- Erdős Problems 的主页面在本次抓取中返回 403；可访问的官方嵌入论坛页面、数据库搜索结果和问题输入内容相互一致，但这不是对主页面全文的独立抓取。
- 文献检索为定向而非逻辑穷尽，不能证明世界上不存在未索引、刚发布或未公开的证明。
- Tao 论文的条件性主结论已由期刊元数据、公开预印本和作者说明交叉核验；本审计没有逐行重审其 16 页证明。
- 2025 Mantzakouras 预印本仅依据公开元数据和摘要作范围判定，未作为数学正确性的正面证据。

- 应由数论专家对任何 2025--2026 近似标题的预印本或新声明做全文范围审计，特别是其是否真正针对无条件原级数。
- 若后续研究代理声称取得短区间素数奇偶混合估计，需独立专家核对量词、均匀性和分部求和所需的误差强度。
- 若把 Tao 的条件性论证用于新工作，必须人工确认所调用的 Hardy--Littlewood 版本与其定理中要求的定量版本完全匹配。

<!-- DEEP_REVIEW:END -->
