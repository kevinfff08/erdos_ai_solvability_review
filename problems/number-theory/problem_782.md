# Problem 782

## 基本信息

- 原始链接: https://www.erdosproblems.com/782
- LaTeX 页面: https://www.erdosproblems.com/latex/782
- 原始状态: `open`
- 奖金: `no`
- 主类别: `number theory`
- 原始标签: `number theory`
- 形式化状态: `no`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

Do the squares contain arbitrarily long quasi-progressions? That is, does there exist some constant $C>0$ such that, for any $k$, the squares contain a sequence $x_1,\ldots,x_k$ where, for some $d$ and all $1\leq i<k$,\[x_i+d\leq x_{i+1}\leq x_i+d+C.\]Do the squares contain arbitrarily large cubes\[a+\left\{ \sum_i \epsilon_ib_i : \epsilon_i\in \{0,1\}\right\}?\]

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `26/100`
- 建议路线: 优先文献定位、特殊情形、数值实验和辅助引理搜索；完整证明需要新的数学思想。

## 判断依据

### 有利因素

- 目前只能依靠通用数学推理、文献归纳和特殊情形探索

### 主要障碍

- 所属标签偏证明密集：number theory
- 题面含渐近/无限对象线索：arbitrarily large
- 缺少明显有限搜索入口。

### 公开版思考过程摘要

- 先识别问题类型：无限/渐近或抽象证明倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: number theory
- 有限/计算线索: 无
- 渐近/无限线索: arbitrarily large
- 构造/存在性线索: does there exist

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **不太可能由 GPT-5.5 级别模型独立完成无条件解决；较可能做出有价值的文献梳理、条件性论证复核、有限规模反例搜索与形式化框架搭建。**
- 等级: `low_to_medium_candidate`
- 分数: `35/100`
- 信心: `medium`
- 可能路线: 最现实的路线是把两个问题分开处理：第一问转化为平方数序列中有界误差近似等差结构的丢番图约束，针对固定 C,k 做计算搜索和局部障碍分析；第二问沿 Hilbert cube in squares 的代数曲线/高维簇路线，复核“Bombieri-Lang 蕴含否定答案”的条件性证明，并尝试在低维 cube 或额外非退化条件下给出无条件排除。GPT-5.5 可作为工具编排者推进这些局部任务，但要给出完整无条件定理大概率需要新的深层数论思想。

### 支持理由

- 题目已经关联经典事实：平方数不含长度 4 的等差数列，说明严格等差结构很硬；准等差只放宽到统一常数 C，仍然保持强丢番图约束。
- 第二问关于平方数中任意大 Hilbert cube，备注中已有 Solymosi 猜测为否，且 Cilleruelo-Granville 只在 Bombieri-Lang 猜想下得到否定答案，暗示无条件证明可能触及深层算术几何。
- GPT-5.5 配合计算可以系统搜索小 C、小维数 cube、小长度 quasi-progression，发现模式、验证边界案例，并自动生成可复核的 Sage/PARI/Lean 辅助材料。
- 模型可以显著推进形式化层面：精确定义 quasi-progression、证明第一问肯定推出第二问的组合构造、整理条件性否定证明中的依赖假设。
- 若存在反例型证据，例如某些固定 C 不可能产生很长序列，计算和自动证明工具有机会给出可验证的有限证书或低维定理。

### 主要障碍

- 核心量词是存在某个全局常数 C 使任意 k 成立；计算只能覆盖固定 C,k，无法直接排除所有 C 或构造无限族。
- 准等差允许误差，削弱了传统“平方数无 4 项等差数列”的直接障碍，导致简单模运算或局部同余方法可能不足。
- 第二问的已知条件性否定依赖 Bombieri-Lang，这通常不是当前模型可绕开的技术壁垒。
- 若要证明肯定答案，需要构造任意长平方数序列，其相邻差都落在长度 C+1 的固定窗口内；这相当于控制平方根增量的细微整数逼近，构造难度高。
- 若要证明否定答案，需要建立对所有常数 C 的统一上界，这比固定参数搜索或局部筛法强很多。

### 需要的验证

- 核查 Brown-Erdos-Freedman、Solymosi、Cilleruelo-Granville 三条备注来源中的精确定理表述，避免误解第一问与第二问的逻辑关系。
- 为固定 C,k 编写可复现搜索，记录搜索空间、剪枝条件、同余筛和是否穷尽。
- 形式化证明第一问肯定推出第二问的组合步骤，至少在 Lean/Isabelle 或严谨手稿中给出无歧义版本。
- 对低维 Hilbert cube in squares 复核已知无条件限制，区分退化 cube、重复和非退化情形。
- 若提出新结论，需要独立验证是否真正处理了“存在某个 C 对所有 k”的全局量词，而不只是实验上未找到长例子。

### 公开版思考摘要

这个问题不像单纯计算搜索问题；它位于平方数的加性结构、近似等差结构和 Hilbert cube 的交界处。备注显示第二问已有强猜想和基于 Bombieri-Lang 的条件性否定，因此完整无条件解决的门槛很高。GPT-5.5 级模型比较适合做局部推进：整理已知条件性路线、形式化蕴含关系、搜索小参数、发现并验证低维障碍；但不应预期它可靠地产生突破性无条件证明。

### 免责声明

以上是对 AI 工具辅助可解决性的评估，不是该 Erdős 问题的解答，也未声称证明肯定或否定答案。

<!-- MODEL_REVIEW:END -->
