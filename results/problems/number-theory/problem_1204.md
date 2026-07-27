# Problem 1204

## 基本信息

- 原始链接: https://www.erdosproblems.com/1204
- LaTeX 页面: https://www.erdosproblems.com/latex/1204
- 原始状态: `open`
- 奖金: `no`
- 主类别: `number theory`
- 原始标签: `number theory`
- 形式化状态: `no`
- OEIS: `A008407`, `A023193`, `A135311`, `possible`
- 原站备注字段: 无

## 原问题

We call a sequence of integers $0\leq a_1<\cdots <a_k$ admissible if it is missing at least one congruence class modulo every prime $p$. Let $A(k)=\min a_k$. Estimate $A(k)$ - in particular, is it true that\[A(k)\sim k\log k?\]Estimate\[B(k)=\min \frac{a_1+\cdots+a_k}{k}.\]

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `22/100`
- 建议路线: 优先文献定位、特殊情形、数值实验和辅助引理搜索；完整证明需要新的数学思想。

## 判断依据

### 有利因素

- 存在 OEIS 数据入口，利于实验与反例搜索

### 主要障碍

- 所属标签偏证明密集：number theory
- 题面含渐近/无限对象线索：o(, prime, primes
- 缺少明显有限搜索入口。

### 公开版思考过程摘要

- 先识别问题类型：无限/渐近或抽象证明倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: number theory
- 有限/计算线索: 无
- 渐近/无限线索: o(, prime, primes
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **低到中等候选。主猜想 A(k)∼k log k 很可能需要超出现有筛法和素数 k-tuples/短区间素数计数相关的新思想，GPT-5.5 级别模型不应被期待直接解决。但该问题定义清楚、已有上下界链条明确，适合用计算搜索、整数规划/约束建模、已知证明形式化、有限范围验证和条件性命题整理来显著推进周边证据。**
- 等级: `low_to_medium_candidate`
- 分数: `38/100`
- 信心: `medium`
- 可能路线: 最现实路线不是直接证明 A(k)∼k log k，而是把 admissible k-tuple 的条件转化为有限素数模约束，进行反例搜索、最优构造搜索和已知上下界的机器验证；同时形式化 Elliott 下界、Davenport 型上界以及 B(k) 的平均值推论。若要冲击主猜想，更可能是先证明条件性结果：在给定素数计数短区间上界或 prime tuples conjecture 形式假设下推出 A(k) 的 1 常数下界。

### 支持理由

- 问题陈述短且结构化，admissible 条件可被精确编码为模素数覆盖约束，适合 SAT/ILP/CP-SAT、穷举剪枝和证书验证。
- 已有结果给出 (1/2+o(1))k log k 到 (1+o(1))k log k 的夹逼，模型可围绕已知证明做形式化、常数追踪、低阶项复核和有限 k 数据生成。
- B(k) 与 A(j) 的关系直接，平均值界的推导较适合自动证明检查；构造侧也可由“取大于 k 的前 k 个素数”机械验证。
- 备注中已经指出 prime tuples conjecture 加短区间素数计数型上界可推出期望下界，这给模型提供了可审计的条件性证明目标。
- OEIS 线索和 greedy admissible sequence 方向适合计算实验，可能产出新数据、猜想修正或小 k 最优证书。

### 主要障碍

- 主问题的核心常数从 1/2 提升到 1 似乎触及深层筛法障碍；仅靠模式匹配或常规搜索很难突破渐近下界。
- 如果无条件证明 A(k)∼k log k，可能需要接近 prime tuples conjecture 或强短区间素数分布的思想；这些远超普通自动定理证明范围。
- 有限 k 搜索即使很强，也很难外推到渐近命题；需要可推广的不变量或证书族。
- admissibility 是对所有素数的条件，虽然大素数可简化，但严谨截断、等价化和证书生成必须小心。
- B(k) 的精确渐近依赖 A(k) 的常数下界；若 A(k) 主猜想不解决，B(k) 也多半只能获得条件性或有限范围进展。

### 需要的验证

- 建立可复现的搜索程序，证明只需检查哪些素数模数，并为每个小 k 最优值输出可独立验证的证书。
- 对已知上下界证明进行逐行重构，最好在 Lean/Isabelle 或可检查的 LaTeX 证明脚本中形式化关键引理。
- 验证 Davenport 构造、Elliott 下界、Hensley-Richard 低阶项相关表述是否与当前问题定义完全一致。
- 对条件性路线明确列出假设形式，例如短区间素数计数上界和 prime tuples conjecture 的精确版本，并检查推出 A(k)≥(1-o(1))k log k 的每一步。
- 对 greedy admissible sequence 和 B(k) 生成公开数据表，交叉检查 OEIS 线索，避免把启发式最优误报为证明。

### 公开版思考摘要

这个问题对 AI 的可操作性较好，因为约束离散、定义短、已有上下界和构造清楚；GPT-5.5 可以较可靠地做形式化整理、条件性证明、有限搜索和证书验证。但主渐近 A(k)∼k log k 的无条件证明看起来依赖新的深层数论输入，尤其是把现有 1/2 常数下界提升到 1 的障碍。因此我评为低到中等候选：适合显著推进证据和验证框架，不适合作为短期内直接攻克的高概率目标。

### 免责声明

以上是对 GPT-5.5 级别模型可推进性的审查，不是 Erdős problem 1204 的解答，也未声称证明 A(k)∼k log k 或 B(k)∼(1/2)k log k。

<!-- MODEL_REVIEW:END -->
