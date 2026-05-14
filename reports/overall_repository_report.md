# Overall AI Solvability Review Report

- Generated: 2026-05-14
- Source snapshot: `data/source/erdos_problems_full.json`
- Reviewed unresolved/semi-open problems: 682
- Average AI-completability score: 32.6/100
- Score range: 6 to 81
- Medium-or-above candidates: 39

## Status Distribution

| Status | Count |
|---|---:|
| open | 629 |
| falsifiable | 27 |
| decidable | 9 |
| verifiable | 7 |
| not disprovable | 4 |
| not provable | 3 |
| independent | 3 |

## AI Capability Distribution

| Level | Count |
|---|---:|
| low_candidate | 490 |
| low_to_medium_candidate | 143 |
| medium_candidate | 28 |
| high_candidate | 11 |
| not_applicable_meta_mathematical | 10 |

## Primary Category Distribution

| Primary category | Count |
|---|---:|
| number theory | 341 |
| graph theory | 145 |
| geometry | 62 |
| additive combinatorics | 35 |
| analysis | 31 |
| combinatorics | 20 |
| set theory | 16 |
| irrationality | 8 |
| group theory | 5 |
| sidon sets | 3 |
| arithmetic progressions | 3 |
| hypergraphs | 3 |
| primes | 2 |
| polynomials | 1 |
| distances | 1 |
| primitive sets | 1 |
| discrepancy | 1 |
| covering systems | 1 |
| diophantine approximation | 1 |
| ramsey theory | 1 |
| algebra | 1 |

## Top Cross-Tags

| Tag | Count |
|---|---:|
| number theory | 342 |
| graph theory | 147 |
| ramsey theory | 68 |
| geometry | 64 |
| additive combinatorics | 52 |
| primes | 45 |
| distances | 39 |
| chromatic number | 34 |
| analysis | 32 |
| set theory | 28 |
| unit fractions | 22 |
| combinatorics | 21 |
| sidon sets | 20 |
| hypergraphs | 18 |
| arithmetic progressions | 16 |
| additive basis | 16 |
| binomial coefficients | 16 |
| divisors | 15 |
| turan number | 15 |
| irrationality | 13 |
| covering systems | 12 |
| cycles | 12 |
| factorials | 11 |
| polynomials | 11 |
| iterated functions | 8 |
| convex | 7 |
| probability | 7 |
| group theory | 5 |
| discrepancy | 5 |
| base representations | 4 |
| primitive sets | 4 |
| powers | 4 |
| complete sequences | 4 |
| squares | 3 |
| diophantine approximation | 2 |
| intersecting family | 1 |
| planar graphs | 1 |
| powerful | 1 |
| algebra | 1 |

## 综合分析

这批 682 个记录不是同一种意义上的“未解决”。`open` 是完全开放问题；`falsifiable/verifiable/decidable` 更适合 AI+计算工具做证书搜索、反例搜索或有限验证；`independent/not provable/not disprovable` 则应被视为元数学任务。
从标签看，number theory、graph theory、Ramsey theory、geometry、additive combinatorics 是主要板块。AI 的强项集中在：把有限结构转成可执行搜索，把候选构造转成验证程序，整理文献与等价表述，以及把已经清楚的陈述放入 Lean/Isabelle 等形式系统。AI 的弱项集中在：需要全新思想的渐近估计、素数分布、深层解析数论、无限组合原理和独立性证明。
因此，本仓库的结论应作为研究路线筛选器使用：优先查看 medium/high candidate，再按类别报告决定是否投入计算实验、形式化验证或文献审查。low candidate 并不表示不可能，只表示当前通用 AI 单独给出完整、可发表解答的风险很高。

## Medium-Or-Above Candidates

| # | Status | Score | Level | Tags | Problem file |
|---:|---|---:|---|---|---|
| 556 | decidable | 81 | high_candidate | graph theory, ramsey theory | [file](../problems/graph-theory/problem_556.md) |
| 835 | verifiable | 79 | high_candidate | graph theory, hypergraphs | [file](../problems/graph-theory/problem_835.md) |
| 551 | decidable | 77 | high_candidate | graph theory, ramsey theory | [file](../problems/graph-theory/problem_551.md) |
| 547 | decidable | 76 | high_candidate | graph theory, ramsey theory | [file](../problems/graph-theory/problem_547.md) |
| 7 | verifiable | 72 | high_candidate | number theory, covering systems | [file](../problems/number-theory/problem_7.md) |
| 647 | verifiable | 72 | high_candidate | number theory | [file](../problems/number-theory/problem_647.md) |
| 1020 | falsifiable | 72 | high_candidate | graph theory, hypergraphs | [file](../problems/graph-theory/problem_1020.md) |
| 23 | falsifiable | 71 | high_candidate | graph theory | [file](../problems/graph-theory/problem_23.md) |
| 366 | verifiable | 70 | high_candidate | number theory | [file](../problems/number-theory/problem_366.md) |
| 617 | falsifiable | 70 | high_candidate | graph theory | [file](../problems/graph-theory/problem_617.md) |
| 742 | decidable | 70 | high_candidate | graph theory | [file](../problems/graph-theory/problem_742.md) |
| 628 | falsifiable | 69 | medium_candidate | graph theory, chromatic number | [file](../problems/graph-theory/problem_628.md) |
| 19 | decidable | 67 | medium_candidate | graph theory, chromatic number | [file](../problems/graph-theory/problem_19.md) |
| 364 | verifiable | 67 | medium_candidate | number theory | [file](../problems/number-theory/problem_364.md) |
| 580 | decidable | 67 | medium_candidate | graph theory | [file](../problems/graph-theory/problem_580.md) |
| 723 | falsifiable | 67 | medium_candidate | combinatorics | [file](../problems/combinatorics/problem_723.md) |
| 548 | falsifiable | 65 | medium_candidate | graph theory | [file](../problems/graph-theory/problem_548.md) |
| 307 | verifiable | 64 | medium_candidate | number theory, unit fractions | [file](../problems/number-theory/problem_307.md) |
| 64 | falsifiable | 63 | medium_candidate | graph theory, cycles | [file](../problems/graph-theory/problem_64.md) |
| 128 | falsifiable | 63 | medium_candidate | graph theory | [file](../problems/graph-theory/problem_128.md) |
| 506 | decidable | 63 | medium_candidate | geometry | [file](../problems/geometry/problem_506.md) |
| 699 | falsifiable | 63 | medium_candidate | number theory, binomial coefficients | [file](../problems/number-theory/problem_699.md) |
| 242 | falsifiable | 62 | medium_candidate | number theory, unit fractions | [file](../problems/number-theory/problem_242.md) |
| 583 | falsifiable | 62 | medium_candidate | graph theory | [file](../problems/graph-theory/problem_583.md) |
| 993 | falsifiable | 62 | medium_candidate | graph theory | [file](../problems/graph-theory/problem_993.md) |
| 398 | falsifiable | 61 | medium_candidate | number theory, factorials | [file](../problems/number-theory/problem_398.md) |
| 672 | verifiable | 60 | medium_candidate | number theory | [file](../problems/number-theory/problem_672.md) |
| 167 | falsifiable | 59 | medium_candidate | graph theory | [file](../problems/graph-theory/problem_167.md) |
| 475 | decidable | 59 | medium_candidate | number theory, additive combinatorics | [file](../problems/number-theory/problem_475.md) |
| 488 | falsifiable | 59 | medium_candidate | number theory | [file](../problems/number-theory/problem_488.md) |
| 562 | open | 59 | medium_candidate | graph theory, ramsey theory, hypergraphs | [file](../problems/graph-theory/problem_562.md) |
| 743 | falsifiable | 59 | medium_candidate | graph theory | [file](../problems/graph-theory/problem_743.md) |
| 848 | decidable | 59 | medium_candidate | number theory | [file](../problems/number-theory/problem_848.md) |
| 108 | open | 58 | medium_candidate | graph theory, chromatic number, cycles | [file](../problems/graph-theory/problem_108.md) |
| 107 | falsifiable | 57 | medium_candidate | geometry, convex | [file](../problems/geometry/problem_107.md) |
| 564 | open | 57 | medium_candidate | graph theory, ramsey theory, hypergraphs | [file](../problems/graph-theory/problem_564.md) |
| 1041 | falsifiable | 57 | medium_candidate | analysis | [file](../problems/analysis/problem_1041.md) |
| 74 | open | 56 | medium_candidate | graph theory, chromatic number, cycles | [file](../problems/graph-theory/problem_74.md) |
| 287 | falsifiable | 56 | medium_candidate | number theory, unit fractions | [file](../problems/number-theory/problem_287.md) |
