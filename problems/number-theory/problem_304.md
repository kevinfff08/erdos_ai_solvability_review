# Problem 304

## 基本信息

- 原始链接: https://www.erdosproblems.com/304
- LaTeX 页面: https://www.erdosproblems.com/latex/304
- 原始状态: `open`
- 奖金: `no`
- 主类别: `number theory`
- 原始标签: `number theory`, `unit fractions`
- 形式化状态: `yes`
- OEIS: `A097847`, `A097849`
- 原站备注字段: 无

## 原问题

For integers $1\leq a<b$ let $N(a,b)$ denote the minimal $k$ such that there exist integers $1<n_1<\cdots<n_k$ with\[\frac{a}{b}=\frac{1}{n_1}+\cdots+\frac{1}{n_k}.\]Estimate $N(b)=\max_{1\leq a<b}N(a,b)$. Is it true that $N(b) \ll \log\log b$?

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `34/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 已有形式化陈述，可降低语义误读风险
- 存在 OEIS 数据入口，利于实验与反例搜索

### 主要障碍

- 所属标签偏证明密集：number theory
- 题面含渐近/无限对象线索：\gg, \ll

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: unit fractions
- 证明密集标签命中: number theory
- 有限/计算线索: 无
- 渐近/无限线索: \gg, \ll
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。
