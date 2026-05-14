# Problem 671

## 基本信息

- 原始链接: https://www.erdosproblems.com/671
- LaTeX 页面: https://www.erdosproblems.com/latex/671
- 原始状态: `open`
- 奖金: `$250`
- 主类别: `analysis`
- 原始标签: `analysis`
- 形式化状态: `no`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

Given $a_{i}^n\in [-1,1]$ for all $1\leq i\leq n<\infty$ we define $p_{i}^n$ as the unique polynomial of degree $n-1$ such that $p_{i}^n(a_{i}^n)=1$ and $p_{i}^n(a_{i'}^n)=0$ if $1\leq i'\leq n$ with $i\neq i'$. We similarly define\[\mathcal{L}^nf(x) = \sum_{1\leq i\leq n}f(a_i^n)p_i^n(x),\]the unique polynomial of degree $n-1$ which agrees with $f$ on $a_i^n$ for $1\leq i\leq n$ (that is, the sequence of Lagrange interpolation polynomials).

Is there such a sequence of $a_i^n$ such that for every continuous $f:[-1,1]\to \mathbb{R}$ there exists some $x\in [-1,1]$ where\[\limsup_{n\to \infty} \sum_{1\leq i\leq n}\lvert p_{i}^n(x)\rvert=\infty\]and yet\[\mathcal{L}^nf(x) \to f(x)?\]Is there such a sequence such that\[\limsup_{n\to \infty} \sum_{1\leq i\leq n}\lvert p_{i}^n(x)\rvert=\infty\]for every $x\in [-1,1]$ and yet for every continuous $f:[-1,1]\to \mathbb{R}$ there exists $x\in [-1,1]$ with\[\mathcal{L}^nf(x) \to f(x)?\]

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `22/100`
- 建议路线: 优先文献定位、特殊情形、数值实验和辅助引理搜索；完整证明需要新的数学思想。

## 判断依据

### 有利因素

- 目前只能依靠通用数学推理、文献归纳和特殊情形探索

### 主要障碍

- 所属标签偏证明密集：analysis
- 题面含渐近/无限对象线索：limsup
- 原记录含奖金 $250，说明该题被长期视为高价值难题；这不是否定依据，但提高验证门槛。
- 缺少明显有限搜索入口。

### 公开版思考过程摘要

- 先识别问题类型：无限/渐近或抽象证明倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: analysis
- 有限/计算线索: 无
- 渐近/无限线索: limsup
- 构造/存在性线索: is there

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。
