# Problem 404

## 基本信息

- 原始链接: https://www.erdosproblems.com/404
- LaTeX 页面: https://www.erdosproblems.com/latex/404
- 原始状态: `open`
- 奖金: `no`
- 主类别: `number theory`
- 原始标签: `number theory`, `factorials`
- 形式化状态: `no`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

For which integers $a\geq 1$ and primes $p$ is there a finite upper bound on those $k$ such that there are $a=a_1<\cdots<a_n$ with\[p^k \mid (a_1!+\cdots+a_n!)?\]If $f(a,p)$ is the greatest such $k$, how does this function behave?

Is there a prime $p$ and an infinite sequence $a_1<a_2<\cdots$ such that if $p^{m_k}$ is the highest power of $p$ dividing $\sum_{i\leq k}a_i!$ then $m_k\to \infty$?

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `23/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- 题面或备注出现有限对象/计算线索

### 主要障碍

- 所属标签偏证明密集：factorials, number theory
- 题面含渐近/无限对象线索：prime, primes

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: factorials, number theory
- 有限/计算线索: finite
- 渐近/无限线索: prime, primes
- 构造/存在性线索: is there

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。
