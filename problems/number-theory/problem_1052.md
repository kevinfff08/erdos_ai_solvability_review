# Problem 1052

## 基本信息

- 原始链接: https://www.erdosproblems.com/1052
- LaTeX 页面: https://www.erdosproblems.com/latex/1052
- 原始状态: `open`
- 奖金: `$10`
- 主类别: `number theory`
- 原始标签: `number theory`
- 形式化状态: `yes`
- OEIS: `A002827`
- 原站备注字段: unitary perfect numbers

## 原问题

A unitary divisor of $n$ is $d\mid n$ such that $(d,n/d)=1$. A number $n\geq 1$ is a unitary perfect number if it is the sum of its unitary divisors (aside from $n$ itself).

Are there only finite many unitary perfect numbers?

## AI 完成可能性判断

- 结论: **AI 可能做出局部推进或搜索反例，但完整解决把握不足**
- 等级: `low_to_medium_candidate`
- 分数: `39/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- 题面或备注出现有限对象/计算线索
- 已有形式化陈述，可降低语义误读风险
- 存在 OEIS 数据入口，利于实验与反例搜索

### 主要障碍

- 所属标签偏证明密集：number theory
- 原记录含奖金 $10，说明该题被长期视为高价值难题；这不是否定依据，但提高验证门槛。

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: number theory
- 有限/计算线索: finite
- 渐近/无限线索: 无
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。
