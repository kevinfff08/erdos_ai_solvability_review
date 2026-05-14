# Problem 642

## 基本信息

- 原始链接: https://www.erdosproblems.com/642
- LaTeX 页面: https://www.erdosproblems.com/latex/642
- 原始状态: `open`
- 奖金: `no`
- 主类别: `graph theory`
- 原始标签: `graph theory`, `cycles`
- 形式化状态: `no`
- OEIS: `possible`
- 原站备注字段: 无

## 原问题

Let $f(n)$ be the maximal number of edges in a graph on $n$ vertices such that all cycles have more vertices than chords. Is it true that $f(n)\ll n$?

## AI 完成可能性判断

- 结论: **AI 可能做出局部推进或搜索反例，但完整解决把握不足**
- 等级: `low_to_medium_candidate`
- 分数: `38/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 题面或备注出现有限对象/计算线索

### 主要障碍

- 题面含渐近/无限对象线索：\ll

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: cycles, graph theory
- 证明密集标签命中: 无
- 有限/计算线索: graph
- 渐近/无限线索: \ll
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。
