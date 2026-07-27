# Problem 778

## 基本信息

- 原始链接: https://www.erdosproblems.com/778
- LaTeX 页面: https://www.erdosproblems.com/latex/778
- 原始状态: `open`
- 奖金: `no`
- 主类别: `graph theory`
- 原始标签: `graph theory`
- 形式化状态: `no`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

Alice and Bob play a game on the edges of $K_n$, alternating colouring edges by red (Alice) and blue (Bob). Alice goes first, and wins if at the end the largest red clique is larger than any of the blue cliques.

Does Bob have a winning strategy for $n\geq 3$? (Erd\H{o}s believed the answer is yes.)

If we change the game so that Bob colours two edges after each edge that Alice colours, but now require Bob's largest clique to be strictly larger than Alice's, then does Bob have a winning strategy for $n>3$?

Finally, consider the game when Alice wins if the maximum degree of the red subgraph is larger than the maximum degree of the blue subgraph. Who wins?

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `37/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 题面或备注出现有限对象/计算线索

### 主要障碍

- 题面含渐近/无限对象线索：density

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: graph theory
- 证明密集标签命中: 无
- 有限/计算线索: colouring, graph
- 渐近/无限线索: density
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **有一定可推进性，但不宜评为高可解。该问题的核心是全体 n 的无穷族策略存在性，且已知进展只给出 Bob 胜利集合的正密度和相邻传递性质，说明剩余难点不是简单的小规模计算即可消掉。GPT-5.5 配合 QBF/SAT 策略搜索、图同构归约、形式化验证和文献检索，较可能在小 n 策略合成、反例排查、第三个最大度版本的结构化证明、以及把已有传递引理形式化方面取得实质推进；但直接完成三个问句的全局定理仍需要新的组合博弈策略或归纳不变量。**
- 等级: `medium_candidate`
- 分数: `6/100`
- 信心: `medium`
- 可能路线: 最现实路线是把问题分成有限策略搜索与无穷族归纳两层：先用图同构压缩的 minimax/QBF/SAT 搜索生成小 n 的精确胜负表和可读策略；再从策略表中猜测 Bob 的配对、镜像、分块或度平衡不变量；随后尝试把这些不变量推广成对所有 n 的归纳策略。对第一、第二个 clique 版本，需要结合 Ramsey 型估计与构造性 pairing strategy；对第三个最大度版本，更可能通过局部负载平衡、匹配/配对策略或势函数证明 Bob 至少追平 Alice 的最大度。最后用 Lean/Isabelle 或独立程序验证关键有限基例与策略转移引理。

### 支持理由

- 问题规则清晰、状态有限，适合用博弈树搜索、QBF 编码、SAT 证书和图同构削减来验证固定 n 的胜负与策略。
- 目标函数是最大 clique 或最大度，均可用成熟图算法精确计算，便于自动化反例搜索和策略验证。
- remarks 已给出强结构线索：若 Alice 在 n 获胜，则 Bob 在后续若干 n 获胜。这类相邻传递结论可能与归纳、嵌入或补点策略有关，适合模型辅助重构和形式化。
- 第三个最大度版本比 clique 版本更局部，GPT-5.5 较可能发现并验证负载平衡类策略，因此有望显著推进其中一个子问题。
- 即使不能证明全体 n，工具化搜索也能产出有价值的精确小规模数据、策略证书、潜在周期/模类规律和可审计的失败样例。

### 主要障碍

- 第一、第二个 clique 版本涉及全局 clique 数，局部应对策略未必能控制最终最大团大小，证明难度高。
- 完整博弈树随边数二次增长而迅速爆炸，即使用同构归约，小 n 之外仍需要高度结构化的数学思想。
- 已有结果只达到密度下界而非全体 n，暗示剩余 n 可能需要处理复杂的例外类或新的全局策略。
- Bob 的胜利条件在不同版本中有非对称严格性要求，简单的配对或复制策略可能只给平局，不能自动给严格优势。
- 从计算发现的策略推广到任意 n 是主要鸿沟；AI 生成的归纳不变量很容易在边界轮次、奇偶性或最后几步失效。

### 需要的验证

- 为固定 n 建立独立的 minimax/QBF/SAT 策略验证器，并用图同构 canonical labeling 避免重复状态。
- 生成并交叉验证小 n 胜负表，特别检查 n=3、4、5、6 等边界情况和奇偶边数影响。
- 对任何声称的 Bob 通用策略，需给出机器可检查的不变量：每一步如何响应、为何合法、为何最终满足 clique 或 degree 目标。
- 若使用文献中的 MaSp24 型传递引理，需要核对原文证明、定义和适用范围，并将其与新基例或新策略无缝拼接。
- 对第三个最大度版本，应单独验证最后一轮、Alice 先手、多余边数和严格不等式/非严格不等式的胜负判定。

### 公开版思考摘要

这是一个规则简单但无穷族很硬的组合博弈问题。GPT-5.5 最有价值的作用不是直接猜出完整答案，而是把固定 n 的策略搜索做成可审计证书，提取 Bob 的候选响应模式，并尝试证明可推广的不变量。最大度版本由于目标更局部，AI 可解或接近可解的概率高于最大 clique 版本；两个 clique 版本更可能得到显著推进而非完整解决。综合判断为中等候选。

### 免责声明

以上是对 GPT-5.5 级别模型可推进性的审查，不是该 Erdős 问题的解答，也未声称 Bob 或 Alice 的任一全局策略已经被证明。

<!-- MODEL_REVIEW:END -->
