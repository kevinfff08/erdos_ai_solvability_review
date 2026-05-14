# Problem 172

## 基本信息

- 原始链接: https://www.erdosproblems.com/172
- LaTeX 页面: https://www.erdosproblems.com/latex/172
- 原始状态: `open`
- 奖金: `no`
- 主类别: `additive combinatorics`
- 原始标签: `additive combinatorics`, `ramsey theory`
- 形式化状态: `yes`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

Is it true that in any finite colouring of $\mathbb{N}$ there exist arbitrarily large finite $A$ such that all sums and products of distinct elements in $A$ are the same colour?

## AI 完成可能性判断

- 结论: **AI 可能做出局部推进或搜索反例，但完整解决把握不足**
- 等级: `low_to_medium_candidate`
- 分数: `39/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 题面或备注出现有限对象/计算线索
- 已有形式化陈述，可降低语义误读风险

### 主要障碍

- 所属标签偏证明密集：additive combinatorics
- 题面含渐近/无限对象线索：arbitrarily large

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: ramsey theory
- 证明密集标签命中: additive combinatorics
- 有限/计算线索: colouring, finite
- 渐近/无限线索: arbitrarily large
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **不宜判为可直接解决，但属于可被强力显著推进的中高价值候选题：GPT-5.5 级别模型配合证明检索、形式化库、有限反例搜索和专家式文献重构，可能发现从有理数结果到自然数版本的障碍位置、验证小规模强化命题，或给出可审计的条件性推进；完整证明的成功概率仍偏低。**
- 等级: `medium_candidate`
- 分数: `62/100`
- 信心: `medium`
- 可能路线: 最可能的路线不是蛮力搜索，而是重构 Alweiss 在 Q\{0} 上的任意大有限集定理与 Moreira 小构型定理，定位其中使用除法、缩放或有理参数的步骤是否能被整数化；同时用有限颜色、有限区间的 SAT/SMT 搜索寻找低阶反例或模式证据，并把可迁移的组合引理形式化为可检查的有限版本。若能证明某个强整数化引理或分母清除引理，才可能接近原命题。

### 支持理由

- 问题陈述短、目标结构明确：要求同色的 distinct finite sums 与 products，可拆成有限 Ramsey 型目标，适合形式化和有限模型验证。
- 已有相邻结果很强：Q\{0} 上已知任意大有限 A，自然数版本可能是整数化障碍而非完全无结构问题。
- Moreira 的三元构型结果说明加法与乘法同色现象在 N 上并非空泛，给模型提供了可复用的证明模板和局部基例。
- 问题已 formalized，这提高了机器检查候选引理、有限版本和证明草图一致性的可行性。
- 有限反例搜索可以审计小规模颜色数、集合大小和截断区间，虽不能证明原命题，但能快速排除错误强化命题。

### 主要障碍

- 从 Q 到 N 的迁移很可能是核心难点：有理数证明可能依赖缩放、倒数、稠密性或分母选择，这些在自然数着色下不保色。
- 目标要求任意大的有限 A，且同时控制所有 distinct sums 和 products；规模增大时组合约束迅速爆炸。
- 有限计算只能处理截断版本，若发现无反例也难以外推到无限自然数。
- 已有无限 A 版本可被 7 色反例否定，说明不能简单套用 Hindman 型无限 FS/FP 直觉。
- 开放状态表明常规工具和已知定理尚未直接闭合，模型容易产生产生貌似合理但无法检查的整数化跳步。

### 需要的验证

- 精确核对“all sums and products of distinct elements in A”在形式化版本中的定义，是二元和/积还是所有非空 distinct finite sums/products。
- 检索并逐行重构 Hindman、Moreira、Bowen-Sabok、Alweiss 相关证明，标注哪些步骤依赖有理数域结构。
- 建立有限搜索基准：固定颜色数、区间 [1,N]、目标 |A|=k，寻找避免同色 FS/FP 的 coloring 或证明不可避免。
- 对任何候选整数化引理做 Lean/Isabelle 或 SAT 辅助验证，避免隐藏的除法保色假设。
- 检查是否能从 Q\{0} 定理导出某些受限 N 版本，例如允许缩放后的整数集、稀疏子半环、同余类子集或特定颜色扩展。

### 公开版思考摘要

这个问题的可攻性来自两个事实：一方面，它已有非常接近的有理数域强结果和自然数域小构型结果；另一方面，目标是有限而非无限集合，理论上更适合紧致性、有限 Ramsey 化和计算验证。但核心困难也很清楚：有理数上的证明不自动尊重自然数着色，分母清除通常会改变 sums/products 的颜色。因此 GPT-5.5 级别系统最现实的贡献是定位精确障碍、验证有限版本、提出可检查的中间引理，而不是高置信度直接解决原命题。

### 免责声明

以上是 AI 可推进性评估，不是问题 172 的证明、反例或解决声明。

<!-- MODEL_REVIEW:END -->
