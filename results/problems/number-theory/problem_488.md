# Problem 488

## 基本信息

- 原始链接: https://www.erdosproblems.com/488
- LaTeX 页面: https://www.erdosproblems.com/latex/488
- 原始状态: `falsifiable`
- 奖金: `no`
- 主类别: `number theory`
- 原始标签: `number theory`
- 形式化状态: `yes`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

Let $A$ be a finite set and\[B=\{ n \geq 1 : a\mid n\textrm{ for some }a\in A\}.\]Is it true that, for every $m>n\geq \max(A)$,\[\frac{\lvert B\cap [1,m]\rvert }{m}< 2\frac{\lvert B\cap [1,n]\rvert}{n}?\]

## AI 完成可能性判断

- 结论: **AI 辅助完成有现实候选路线，但需要外部计算或严格验证**
- 等级: `medium_candidate`
- 分数: `59/100`
- 建议路线: 优先做反例搜索和小规模枚举；若没有反例，不能据此断言问题为真。

## 判断依据

### 有利因素

- 题面或备注出现有限对象/计算线索
- 已有形式化陈述，可降低语义误读风险

### 主要障碍

- 所属标签偏证明密集：number theory
- 题面含渐近/无限对象线索：prime, primes

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: number theory
- 有限/计算线索: counterexample, finite
- 渐近/无限线索: prime, primes
- 构造/存在性线索: counterexample

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **这是一个中高可推进候选：题目结构有限、计数函数可完全计算且已经形式化，GPT-5.5 级模型配合反例搜索、整数规划/SMT、Lean/Isabelle 形式化和包含-排除实验，有现实机会给出证明、找到反例，或至少把问题大幅化约到可验证的有限/准有限情形。**
- 等级: `medium_candidate`
- 分数: `72/100`
- 信心: `medium`
- 可能路线: 最有希望的路线是把 A 先化为极小反链，即删除被其他元素整除的冗余元素，然后研究计数函数 f_A(t)=|B∩[1,t]|。工具可以系统枚举 A、n、m，寻找极值接近 2 的构造；同时用包含-排除或 lcm 格点表示 f_A(t)，把不等式转成关于 floor(t/q) 的有限分段线性问题。若能证明最坏情形只需检查 m 在若干 lcm 断点附近、或只需检查某类极小 A，则可由计算和形式化证明共同完成。

### 支持理由

- 题目对象是有限集合 A 和显式可计算的并集倍数计数函数，不涉及随机性、解析极限或不可计算对象，适合程序枚举、反例搜索和形式化验证。
- 不等式只含两个有限前缀密度 f_A(m)/m 与 f_A(n)/n，且约束 n>=max(A) 给出了强结构；所有候选反例都能被精确验证。
- 备注说明常数 2 最优，这提示问题可能有较短的极值型证明，而不是需要深层解析数论。
- 形式化状态为 yes，意味着陈述本身已有机器可读基础，GPT-5.5 可利用证明助手围绕已有形式化定义构建引理和自动检查。
- 若存在反例，模型配合高效枚举、SAT/SMT、CP-SAT 或分支限界搜索很可能较快发现小到中等规模证据；若长期找不到反例，实验数据也能指导可证明的归约。

### 主要障碍

- A 的规模和元素大小原则上无界，简单枚举不能构成证明，必须找到有效归约或单调性/极值结构。
- f_A(t) 是多个倍数集的并集，包含-排除涉及大量 lcm，A 较大时组合爆炸明显。
- floor 函数造成分段行为，密度 f_A(t)/t 不一定单调，证明全局 2 倍界需要处理许多局部跳变。
- 常数 2 是最佳可能，极值附近没有余量；任何证明都必须精细处理接近等号的单元素或类似构造。
- 如果问题仍开放，真正困难可能隐藏在把有限计算模式推广为一般定理这一步，而这正是当前模型最容易产生不严谨跳步的地方。

### 需要的验证

- 先实现精确计数器，按删除冗余元素后的 A 枚举大量范围，记录最大比值 R=(f_A(m)/m)/(f_A(n)/n) 并复核常数 2 附近案例。
- 用不同实现交叉验证搜索结果，例如直接筛法、lcm 包含-排除、SMT/整数规划编码，避免程序性漏报。
- 检查是否可证明只需考虑 A 为整除反链、m 或 n 位于倍数跳点附近、或 m/n 落在有限关键区间。
- 若发现候选证明，必须在证明助手中形式化关键引理，尤其是 floor/lcm/并集计数和极值归约部分。
- 若发现候选反例，需要给出具体 A,n,m，并用精确整数计算验证两个密度和严格不等式失败。

### 公开版思考摘要

该题不是靠模型直接灵感即可稳妥解决的类型，但它非常适合工具增强：对象有限、计数可精确、反例可证伪、陈述已形式化。GPT-5.5 最可能的贡献不是凭空写出完整人类级证明，而是通过枚举和符号化发现极值结构，再把问题压缩为若干可形式化的组合引理。因此我评为 medium_candidate，偏向“有明显推进或验证机会”，但不评为 high，因为无界 A、lcm 组合爆炸和最佳常数带来的零余量会使最终一般性证明仍有较高风险。

### 免责声明

以上不是该 Erdős 问题的解答或反例，只是基于给定 JSON 对 GPT-5.5 级工具增强模型可推进性的审查判断。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-08-05`
- 核验模型: `gpt-5.6-sol`
- 当前状态: `confirmed_open`
- 状态信心: `high`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [problem_488.md](../../prompts/problem_488.md)

### 状态结论

原始资料曾把 multiples 误写成 non-multiples；当前规范版本已修正。2026 年讨论给出 |A|=2、min(A)=2 和若干三元族的部分证明，但一般有限 A 仍开放。

### 当前规范陈述

设 A 为非空有限正整数集，B 为至少被 A 中一个元素整除的正整数集合。证明或否证：对所有 m>n≥max(A)，都有 |B∩[1,m]|/m < 2|B∩[1,n]|/n。

```text
Let A be a finite nonempty set of positive integers and B={t>=1: some a in A divides t}. Prove or disprove that for every m>n>=max(A), |B∩[1,m]|/m < 2|B∩[1,n]|/n.
```

### 陈述、量词与反例审计

- 歧义严重度: `material`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 错误的 non-multiples 版本有容易反例；修正后的 multiples 版本未发现反例，且小规模结构已有正面证明。
- 版本变化: 网站在 2025 年底修正题面；2026 年论坛证明两元素集、min(A)=2 及若干 split-core tripod 族。

陈述问题：

- B 必须是倍数并集，而不是不被任何 a 整除的补集。
- 可先把 A 化为 primitive antichain，但该化简需证明不改变 B。

需要固定的量词/约定：

- The inequality is strict and quantified over all integers m>n>=max(A).
- B is a union of divisibility classes.

### 文献与当前边界

已核验的主要结果：

- The constant 2 is asymptotically sharp already for singleton or two-element examples.
- The conjecture holds for every two-element A.
- Several structured primitive three-element families have been verified.

最近相关工作：2026-04 至 2026-06 的直接讨论仍把一般 primitive 集合大小至少 3 作为未解核心。

剩余核心：控制包含-排除中高度重叠的 lcm 项，证明任意尺度的密度涨幅小于 2，或构造反例。

已使用方法：

- inclusion-exclusion over the lcm lattice
- primitive-set reductions and floor-sum inequalities

争议或不确定性：

- 论坛中的 AI 辅助短注不是同行评议论文。
- 原题历史误植造成两种不同问题，引用时必须固定版本。

### 证据来源

- [Erdős Problem 488](https://www.erdosproblems.com/488) — Thomas F. Bloom (database editor); `problem_page`, `database_record`, reliability=`medium`. 核对当前题面、状态标签、备注、历史修订和评论声明。
- [LaTeX source for Erdős Problem 488](https://www.erdosproblems.com/latex/488) — Thomas F. Bloom (database editor); `problem_page`, `database_record`, reliability=`medium`. 核对公式、量词和原始引用键。
- [Erdős Problem 488 discussion](https://www.erdosproblems.com/forum/thread/488) — multiple contributors; edited by Thomas F. Bloom; `forum`, `preprint`, reliability=`medium`. 记录题面修正以及两元素集、min(A)=2 和三元族的直接部分结果。

### 完成标准

- 肯定出口: Prove the strict density-doubling inequality for every finite A.
- 否定出口: Give explicit A,n,m violating the strict inequality and certify all counts exactly.

不构成完成：

- Solving the non-multiples typo version.
- Only an asymptotic m->infinity bound with an unspecified constant.
- Proofs for |A|<=2 or a special tripod family.

正确性陷阱：

- Use exact floor counts at the strict boundary.
- Remove redundant divisibility elements before structural arguments.
- Do not lose the condition n>=max(A).

### 更新后的 AI 可解答性

- 等级: `medium_candidate`
- 分数: `55/100`
- 信心: `medium`
- 结论: 评分只针对核验后的规范开放核心，反映定义清晰度、可验证中间义务、已有方法入口和剩余理论跨度。

支持理由：

- 规范目标和完成标准可以明确写出。
- 已有结果提供可核验的技术入口或边界。

主要障碍：

- 论坛中的 AI 辅助短注不是同行评议论文。
- 原题历史误植造成两种不同问题，引用时必须固定版本。

Proof-first 路线：

- 证明 lcm 格上的交替取整误差统一下界。
- 把最小反例压缩到受控的 primitive 三元或小核结构。

需要验证：

- 逐条核验最终论证的量词、边界和等号情形。
- 复核外部定理的精确假设与引用版本。

### 审计限制与人工复核理由

- 联网检索覆盖题目页、历史、讨论及可定位论文，但不能证明不存在未索引、未公开或不同术语下的结果。
- 未对所有引用论文逐行形式化重证；论坛、AI 生成材料和未同行评议预印本按较低证据等级记录。

- 本批次尚未经过第二个独立强模型复审。

<!-- DEEP_REVIEW:END -->
