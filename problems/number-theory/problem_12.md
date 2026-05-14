# Problem 12

## 基本信息

- 原始链接: https://www.erdosproblems.com/12
- LaTeX 页面: https://www.erdosproblems.com/latex/12
- 原始状态: `open`
- 奖金: `no`
- 主类别: `number theory`
- 原始标签: `number theory`
- 形式化状态: `yes`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

Let $A$ be an infinite set such that there are no distinct $a,b,c\in A$ such that $a\mid (b+c)$ and $b,c>a$. Is there such an $A$ with\[\liminf \frac{\lvert A\cap\{1,\ldots,N\}\rvert}{N^{1/2}}>0?\]Does there exist some absolute constant $c>0$ such that there are always infinitely many $N$ with\[\lvert A\cap\{1,\ldots,N\}\rvert<N^{1-c}?\]Is it true that\[\sum_{n\in A}\frac{1}{n}<\infty?\]

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `26/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- 题面或备注出现有限对象/计算线索
- 已有形式化陈述，可降低语义误读风险

### 主要障碍

- 所属标签偏证明密集：number theory
- 题面含渐近/无限对象线索：\gg, \ll, density, infinitely many, liminf

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: number theory
- 有限/计算线索: finite, finitely
- 渐近/无限线索: \gg, \ll, density, infinitely many, liminf, prime
- 构造/存在性线索: construct, does there exist, is there

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。
