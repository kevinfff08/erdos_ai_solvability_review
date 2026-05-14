# Problem 876

## 基本信息

- 原始链接: https://www.erdosproblems.com/876
- LaTeX 页面: https://www.erdosproblems.com/latex/876
- 原始状态: `open`
- 奖金: `no`
- 主类别: `additive combinatorics`
- 原始标签: `additive combinatorics`
- 形式化状态: `no`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

Let $A=\{a_1<a_2<\cdots\}\subset \mathbb{N}$ be an infinite sum-free set - that is, there are no solutions to\[a=b_1+\cdots+b_r\]with $b_1<\cdots<b_r<a\in A$. How small can $a_{n+1}-a_n$ be? Is it possible that $a_{n+1}-a_n<n$?

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `17/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- 题面或备注出现有限对象/计算线索

### 主要障碍

- 所属标签偏证明密集：additive combinatorics
- 题面含渐近/无限对象线索：\gg, \ll, density, for all large, o(

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: additive combinatorics
- 有限/计算线索: finite
- 渐近/无限线索: \gg, \ll, density, for all large, o(
- 构造/存在性线索: construct

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。
