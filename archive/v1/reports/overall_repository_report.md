# Overall AI Solvability Review Report

This report is based on the GPT-5.5 one-problem-per-call review layer.

- Reviewed unresolved/semi-open problems: 682
- Remaining without model review: 0
- Average model score: 45.3/100
- Score range: 4 to 88
- Medium-or-above candidates: 218
- Detailed model-call report: `reports/model_review_report.md`

## Model Level Distribution

| Level | Count |
|---|---:|
| low_to_medium_candidate | 431 |
| medium_candidate | 206 |
| low_candidate | 30 |
| high_candidate | 12 |
| not_applicable_meta_mathematical | 3 |

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

## 综合分析

GPT-5.5 逐题复审后的分布比规则首版更乐观：多数问题落在 `low_to_medium_candidate`，说明模型认为很多开放题并非完全不可接触，而是可以通过计算实验、形式化复核、特殊情形、反例搜索或文献路线整理产生研究价值。真正的 `high_candidate` 很少，集中在可有限验证、可计算搜索或已有明确证书路线的问题；这类问题最适合作为下一步 AI+工具流水线的优先对象。

低分问题主要来自深数论、渐近估计、素数分布、集合论/独立性或缺乏有限证书入口的题目。这些题仍可能被 AI 辅助推进，但应把目标设为局部引理、失败路线排查和严格验证，而不是直接求最终证明。

因此，这个仓库现在可以作为筛选器使用：先看 `reports/model_review_report.md` 中的 high/medium，再进入对应类别报告，最后打开单题文件查看 GPT-5.5 的支持理由、障碍和验证需求。

## Medium-Or-Above Candidates

| # | Status | Score | Level | Confidence | Tags | Problem file |
|---:|---|---:|---|---|---|---|
| 655 | open | 88 | high_candidate | high | geometry; distances | [problems/geometry/problem_655.md](../../../results/problems/geometry/problem_655.md) |
| 848 | decidable | 88 | high_candidate | high | number theory | [problems/number-theory/problem_848.md](../../../results/problems/number-theory/problem_848.md) |
| 684 | open | 86 | high_candidate | medium | number theory; primes; binomial coefficients | [problems/number-theory/problem_684.md](../../../results/problems/number-theory/problem_684.md) |
| 742 | decidable | 83 | high_candidate | medium | graph theory | [problems/graph-theory/problem_742.md](../../../results/problems/graph-theory/problem_742.md) |
| 36 | open | 82 | high_candidate | medium | number theory; additive combinatorics | [problems/number-theory/problem_36.md](../../../results/problems/number-theory/problem_36.md) |
| 545 | open | 82 | high_candidate | medium | graph theory; ramsey theory | [problems/graph-theory/problem_545.md](../../../results/problems/graph-theory/problem_545.md) |
| 635 | open | 82 | high_candidate | medium | number theory | [problems/number-theory/problem_635.md](../../../results/problems/number-theory/problem_635.md) |
| 647 | verifiable | 82 | high_candidate | medium | number theory | [problems/number-theory/problem_647.md](../../../results/problems/number-theory/problem_647.md) |
| 776 | open | 82 | high_candidate | medium | combinatorics | [problems/combinatorics/problem_776.md](../../../results/problems/combinatorics/problem_776.md) |
| 872 | open | 82 | high_candidate | medium | number theory; primitive sets | [problems/number-theory/problem_872.md](../../../results/problems/number-theory/problem_872.md) |
| 1155 | open | 82 | high_candidate | medium | graph theory | [problems/graph-theory/problem_1155.md](../../../results/problems/graph-theory/problem_1155.md) |
| 813 | open | 78 | high_candidate | medium | graph theory | [problems/graph-theory/problem_813.md](../../../results/problems/graph-theory/problem_813.md) |
| 114 | falsifiable | 72 | medium_candidate | medium | polynomials; analysis | [problems/polynomials/problem_114.md](../../../results/problems/polynomials/problem_114.md) |
| 488 | falsifiable | 72 | medium_candidate | medium | number theory | [problems/number-theory/problem_488.md](../../../results/problems/number-theory/problem_488.md) |
| 556 | decidable | 72 | medium_candidate | medium | graph theory; ramsey theory | [problems/graph-theory/problem_556.md](../../../results/problems/graph-theory/problem_556.md) |
| 625 | open | 72 | medium_candidate | medium | graph theory; chromatic number | [problems/graph-theory/problem_625.md](../../../results/problems/graph-theory/problem_625.md) |
| 1005 | open | 72 | medium_candidate | medium | number theory | [problems/number-theory/problem_1005.md](../../../results/problems/number-theory/problem_1005.md) |
| 65 | open | 68 | medium_candidate | medium | graph theory; cycles | [problems/graph-theory/problem_65.md](../../../results/problems/graph-theory/problem_65.md) |
| 423 | open | 68 | medium_candidate | medium | number theory | [problems/number-theory/problem_423.md](../../../results/problems/number-theory/problem_423.md) |
| 475 | decidable | 68 | medium_candidate | medium | number theory; additive combinatorics | [problems/number-theory/problem_475.md](../../../results/problems/number-theory/problem_475.md) |
| 521 | open | 68 | medium_candidate | medium | analysis; polynomials; probability | [problems/analysis/problem_521.md](../../../results/problems/analysis/problem_521.md) |
| 551 | decidable | 68 | medium_candidate | medium | graph theory; ramsey theory | [problems/graph-theory/problem_551.md](../../../results/problems/graph-theory/problem_551.md) |
| 580 | decidable | 68 | medium_candidate | medium | graph theory | [problems/graph-theory/problem_580.md](../../../results/problems/graph-theory/problem_580.md) |
| 699 | falsifiable | 68 | medium_candidate | medium | number theory; binomial coefficients | [problems/number-theory/problem_699.md](../../../results/problems/number-theory/problem_699.md) |
| 749 | open | 68 | medium_candidate | medium | additive combinatorics | [problems/additive-combinatorics/problem_749.md](../../../results/problems/additive-combinatorics/problem_749.md) |
| 779 | falsifiable | 68 | medium_candidate | medium | number theory; primes | [problems/number-theory/problem_779.md](../../../results/problems/number-theory/problem_779.md) |
| 1016 | open | 68 | medium_candidate | medium | graph theory; cycles | [problems/graph-theory/problem_1016.md](../../../results/problems/graph-theory/problem_1016.md) |
| 1045 | open | 68 | medium_candidate | medium | analysis | [problems/analysis/problem_1045.md](../../../results/problems/analysis/problem_1045.md) |
| 1194 | open | 68 | medium_candidate | medium | additive combinatorics; additive basis; sidon sets | [problems/additive-combinatorics/problem_1194.md](../../../results/problems/additive-combinatorics/problem_1194.md) |
| 132 | open | 67 | medium_candidate | medium | distances | [problems/distances/problem_132.md](../../../results/problems/distances/problem_132.md) |
| 261 | open | 67 | medium_candidate | medium | number theory | [problems/number-theory/problem_261.md](../../../results/problems/number-theory/problem_261.md) |
| 734 | open | 66 | medium_candidate | medium | combinatorics | [problems/combinatorics/problem_734.md](../../../results/problems/combinatorics/problem_734.md) |
| 885 | open | 66 | medium_candidate | medium | number theory; divisors | [problems/number-theory/problem_885.md](../../../results/problems/number-theory/problem_885.md) |
| 906 | open | 66 | medium_candidate | medium | analysis; iterated functions | [problems/analysis/problem_906.md](../../../results/problems/analysis/problem_906.md) |
| 19 | decidable | 64 | medium_candidate | medium | graph theory; chromatic number | [problems/graph-theory/problem_19.md](../../../results/problems/graph-theory/problem_19.md) |
| 374 | open | 64 | medium_candidate | medium | number theory | [problems/number-theory/problem_374.md](../../../results/problems/number-theory/problem_374.md) |
| 415 | open | 64 | medium_candidate | high | number theory | [problems/number-theory/problem_415.md](../../../results/problems/number-theory/problem_415.md) |
| 503 | open | 64 | medium_candidate | medium | geometry; distances | [problems/geometry/problem_503.md](../../../results/problems/geometry/problem_503.md) |
| 547 | decidable | 64 | medium_candidate | medium | graph theory; ramsey theory | [problems/graph-theory/problem_547.md](../../../results/problems/graph-theory/problem_547.md) |
| 854 | open | 64 | medium_candidate | medium | number theory | [problems/number-theory/problem_854.md](../../../results/problems/number-theory/problem_854.md) |
| 942 | open | 64 | medium_candidate | medium | number theory | [problems/number-theory/problem_942.md](../../../results/problems/number-theory/problem_942.md) |
| 993 | falsifiable | 64 | medium_candidate | medium | graph theory | [problems/graph-theory/problem_993.md](../../../results/problems/graph-theory/problem_993.md) |
| 1113 | open | 64 | medium_candidate | medium | number theory; covering systems | [problems/number-theory/problem_1113.md](../../../results/problems/number-theory/problem_1113.md) |
| 1186 | open | 64 | medium_candidate | medium | additive combinatorics; arithmetic progressions | [problems/additive-combinatorics/problem_1186.md](../../../results/problems/additive-combinatorics/problem_1186.md) |
| 203 | open | 63 | medium_candidate | medium | primes; covering systems | [problems/primes/problem_203.md](../../../results/problems/primes/problem_203.md) |
| 301 | open | 63 | medium_candidate | medium | number theory; unit fractions | [problems/number-theory/problem_301.md](../../../results/problems/number-theory/problem_301.md) |
| 413 | open | 63 | medium_candidate | medium | number theory; iterated functions | [problems/number-theory/problem_413.md](../../../results/problems/number-theory/problem_413.md) |
| 568 | open | 63 | medium_candidate | medium | graph theory; ramsey theory | [problems/graph-theory/problem_568.md](../../../results/problems/graph-theory/problem_568.md) |
| 616 | open | 63 | medium_candidate | medium | graph theory | [problems/graph-theory/problem_616.md](../../../results/problems/graph-theory/problem_616.md) |
| 883 | open | 63 | medium_candidate | medium | number theory; graph theory | [problems/number-theory/problem_883.md](../../../results/problems/number-theory/problem_883.md) |
| 888 | open | 63 | medium_candidate | medium | number theory; squares | [problems/number-theory/problem_888.md](../../../results/problems/number-theory/problem_888.md) |
| 949 | open | 63 | medium_candidate | medium | ramsey theory | [problems/ramsey-theory/problem_949.md](../../../results/problems/ramsey-theory/problem_949.md) |
| 963 | open | 63 | medium_candidate | medium | number theory | [problems/number-theory/problem_963.md](../../../results/problems/number-theory/problem_963.md) |
| 12 | open | 62 | medium_candidate | medium | number theory | [problems/number-theory/problem_12.md](../../../results/problems/number-theory/problem_12.md) |
| 97 | falsifiable | 62 | medium_candidate | medium | geometry; distances; convex | [problems/geometry/problem_97.md](../../../results/problems/geometry/problem_97.md) |
| 100 | open | 62 | medium_candidate | medium | geometry; distances | [problems/geometry/problem_100.md](../../../results/problems/geometry/problem_100.md) |
| 106 | falsifiable | 62 | medium_candidate | medium | geometry | [problems/geometry/problem_106.md](../../../results/problems/geometry/problem_106.md) |
| 112 | open | 62 | medium_candidate | medium | graph theory; ramsey theory | [problems/graph-theory/problem_112.md](../../../results/problems/graph-theory/problem_112.md) |
| 143 | open | 62 | medium_candidate | medium | primitive sets | [problems/primitive-sets/problem_143.md](../../../results/problems/primitive-sets/problem_143.md) |
| 172 | open | 62 | medium_candidate | medium | additive combinatorics; ramsey theory | [problems/additive-combinatorics/problem_172.md](../../../results/problems/additive-combinatorics/problem_172.md) |
| 273 | open | 62 | medium_candidate | medium | number theory; covering systems | [problems/number-theory/problem_273.md](../../../results/problems/number-theory/problem_273.md) |
| 276 | open | 62 | medium_candidate | medium | number theory; covering systems | [problems/number-theory/problem_276.md](../../../results/problems/number-theory/problem_276.md) |
| 278 | open | 62 | medium_candidate | medium | number theory; covering systems | [problems/number-theory/problem_278.md](../../../results/problems/number-theory/problem_278.md) |
| 302 | open | 62 | medium_candidate | medium | number theory; unit fractions | [problems/number-theory/problem_302.md](../../../results/problems/number-theory/problem_302.md) |
| 307 | verifiable | 62 | medium_candidate | medium | number theory; unit fractions | [problems/number-theory/problem_307.md](../../../results/problems/number-theory/problem_307.md) |
| 319 | open | 62 | medium_candidate | medium | number theory; unit fractions | [problems/number-theory/problem_319.md](../../../results/problems/number-theory/problem_319.md) |
| 332 | open | 62 | medium_candidate | medium | number theory | [problems/number-theory/problem_332.md](../../../results/problems/number-theory/problem_332.md) |
| 396 | open | 62 | medium_candidate | medium | number theory; binomial coefficients | [problems/number-theory/problem_396.md](../../../results/problems/number-theory/problem_396.md) |
| 409 | open | 62 | medium_candidate | medium | number theory; iterated functions | [problems/number-theory/problem_409.md](../../../results/problems/number-theory/problem_409.md) |
| 410 | open | 62 | medium_candidate | medium | number theory; iterated functions | [problems/number-theory/problem_410.md](../../../results/problems/number-theory/problem_410.md) |
| 436 | open | 62 | medium_candidate | medium | number theory | [problems/number-theory/problem_436.md](../../../results/problems/number-theory/problem_436.md) |
| 451 | open | 62 | medium_candidate | medium | number theory | [problems/number-theory/problem_451.md](../../../results/problems/number-theory/problem_451.md) |
| 472 | open | 62 | medium_candidate | medium | number theory | [problems/number-theory/problem_472.md](../../../results/problems/number-theory/problem_472.md) |
| 477 | open | 62 | medium_candidate | medium | number theory | [problems/number-theory/problem_477.md](../../../results/problems/number-theory/problem_477.md) |
| 489 | open | 62 | medium_candidate | medium | number theory | [problems/number-theory/problem_489.md](../../../results/problems/number-theory/problem_489.md) |
| 506 | decidable | 62 | medium_candidate | medium | geometry | [problems/geometry/problem_506.md](../../../results/problems/geometry/problem_506.md) |
| 514 | open | 62 | medium_candidate | medium | analysis | [problems/analysis/problem_514.md](../../../results/problems/analysis/problem_514.md) |
| 638 | open | 62 | medium_candidate | medium | graph theory; ramsey theory | [problems/graph-theory/problem_638.md](../../../results/problems/graph-theory/problem_638.md) |
| 642 | open | 62 | medium_candidate | medium | graph theory; cycles | [problems/graph-theory/problem_642.md](../../../results/problems/graph-theory/problem_642.md) |
| 654 | open | 62 | medium_candidate | medium | geometry; distances | [problems/geometry/problem_654.md](../../../results/problems/geometry/problem_654.md) |
| 757 | open | 62 | medium_candidate | medium | geometry; distances; sidon sets | [problems/geometry/problem_757.md](../../../results/problems/geometry/problem_757.md) |
| 786 | open | 62 | medium_candidate | medium | number theory | [problems/number-theory/problem_786.md](../../../results/problems/number-theory/problem_786.md) |
| 817 | open | 62 | medium_candidate | medium | additive combinatorics | [problems/additive-combinatorics/problem_817.md](../../../results/problems/additive-combinatorics/problem_817.md) |
| 819 | open | 62 | medium_candidate | medium | additive combinatorics | [problems/additive-combinatorics/problem_819.md](../../../results/problems/additive-combinatorics/problem_819.md) |
| 887 | open | 62 | medium_candidate | medium | number theory; divisors | [problems/number-theory/problem_887.md](../../../results/problems/number-theory/problem_887.md) |
| 893 | open | 62 | medium_candidate | medium | number theory; divisors | [problems/number-theory/problem_893.md](../../../results/problems/number-theory/problem_893.md) |
| 933 | open | 62 | medium_candidate | medium | number theory | [problems/number-theory/problem_933.md](../../../results/problems/number-theory/problem_933.md) |
| 935 | open | 62 | medium_candidate | medium | number theory | [problems/number-theory/problem_935.md](../../../results/problems/number-theory/problem_935.md) |
| 938 | open | 62 | medium_candidate | medium | number theory | [problems/number-theory/problem_938.md](../../../results/problems/number-theory/problem_938.md) |
| 1002 | open | 62 | medium_candidate | medium | analysis; diophantine approximation | [problems/analysis/problem_1002.md](../../../results/problems/analysis/problem_1002.md) |
| 1017 | open | 62 | medium_candidate | medium | graph theory | [problems/graph-theory/problem_1017.md](../../../results/problems/graph-theory/problem_1017.md) |
| 1035 | open | 62 | medium_candidate | medium | graph theory | [problems/graph-theory/problem_1035.md](../../../results/problems/graph-theory/problem_1035.md) |
| 1040 | open | 62 | medium_candidate | medium | analysis | [problems/analysis/problem_1040.md](../../../results/problems/analysis/problem_1040.md) |
| 1060 | open | 62 | medium_candidate | medium | number theory | [problems/number-theory/problem_1060.md](../../../results/problems/number-theory/problem_1060.md) |
| 1061 | open | 62 | medium_candidate | medium | number theory | [problems/number-theory/problem_1061.md](../../../results/problems/number-theory/problem_1061.md) |
| 1063 | open | 62 | medium_candidate | medium | number theory | [problems/number-theory/problem_1063.md](../../../results/problems/number-theory/problem_1063.md) |
| 1082 | falsifiable | 62 | medium_candidate | medium | geometry; distances | [problems/geometry/problem_1082.md](../../../results/problems/geometry/problem_1082.md) |
| 1094 | open | 62 | medium_candidate | medium | number theory; binomial coefficients | [problems/number-theory/problem_1094.md](../../../results/problems/number-theory/problem_1094.md) |
| 1100 | open | 62 | medium_candidate | medium | number theory; divisors | [problems/number-theory/problem_1100.md](../../../results/problems/number-theory/problem_1100.md) |
| 1110 | open | 62 | medium_candidate | medium | number theory | [problems/number-theory/problem_1110.md](../../../results/problems/number-theory/problem_1110.md) |
| 1119 | independent | 62 | medium_candidate | medium | analysis; set theory | [problems/analysis/problem_1119.md](../../../results/problems/analysis/problem_1119.md) |
| 1131 | open | 62 | medium_candidate | medium | analysis; polynomials | [problems/analysis/problem_1131.md](../../../results/problems/analysis/problem_1131.md) |
| 267 | open | 61 | medium_candidate | medium | irrationality | [problems/irrationality/problem_267.md](../../../results/problems/irrationality/problem_267.md) |
| 469 | open | 61 | medium_candidate | medium | number theory; divisors | [problems/number-theory/problem_469.md](../../../results/problems/number-theory/problem_469.md) |
| 831 | open | 61 | medium_candidate | medium | geometry | [problems/geometry/problem_831.md](../../../results/problems/geometry/problem_831.md) |
| 33 | open | 60 | medium_candidate | medium | number theory; additive basis | [problems/number-theory/problem_33.md](../../../results/problems/number-theory/problem_33.md) |
| 346 | open | 60 | medium_candidate | medium | number theory; complete sequences | [problems/number-theory/problem_346.md](../../../results/problems/number-theory/problem_346.md) |
| 404 | open | 60 | medium_candidate | medium | number theory; factorials | [problems/number-theory/problem_404.md](../../../results/problems/number-theory/problem_404.md) |
| 509 | open | 60 | medium_candidate | medium | analysis | [problems/analysis/problem_509.md](../../../results/problems/analysis/problem_509.md) |
| 614 | open | 60 | medium_candidate | medium | graph theory | [problems/graph-theory/problem_614.md](../../../results/problems/graph-theory/problem_614.md) |
| 809 | open | 60 | medium_candidate | medium | graph theory; ramsey theory | [problems/graph-theory/problem_809.md](../../../results/problems/graph-theory/problem_809.md) |
| 820 | open | 60 | medium_candidate | medium | number theory | [problems/number-theory/problem_820.md](../../../results/problems/number-theory/problem_820.md) |
| 864 | open | 60 | medium_candidate | medium | number theory; sidon sets; additive combinatorics | [problems/number-theory/problem_864.md](../../../results/problems/number-theory/problem_864.md) |
| 1056 | open | 60 | medium_candidate | medium | number theory | [problems/number-theory/problem_1056.md](../../../results/problems/number-theory/problem_1056.md) |
| 18 | open | 58 | medium_candidate | medium | number theory; divisors; factorials | [problems/number-theory/problem_18.md](../../../results/problems/number-theory/problem_18.md) |
| 23 | falsifiable | 58 | medium_candidate | medium | graph theory | [problems/graph-theory/problem_23.md](../../../results/problems/graph-theory/problem_23.md) |
| 25 | open | 58 | medium_candidate | medium | number theory | [problems/number-theory/problem_25.md](../../../results/problems/number-theory/problem_25.md) |
| 64 | falsifiable | 58 | medium_candidate | medium | graph theory; cycles | [problems/graph-theory/problem_64.md](../../../results/problems/graph-theory/problem_64.md) |
| 78 | open | 58 | medium_candidate | medium | graph theory; ramsey theory | [problems/graph-theory/problem_78.md](../../../results/problems/graph-theory/problem_78.md) |
| 84 | open | 58 | medium_candidate | medium | graph theory; cycles | [problems/graph-theory/problem_84.md](../../../results/problems/graph-theory/problem_84.md) |
| 85 | open | 58 | medium_candidate | medium | graph theory | [problems/graph-theory/problem_85.md](../../../results/problems/graph-theory/problem_85.md) |
| 99 | open | 58 | medium_candidate | medium | geometry; distances | [problems/geometry/problem_99.md](../../../results/problems/geometry/problem_99.md) |
| 104 | open | 58 | medium_candidate | medium | geometry | [problems/geometry/problem_104.md](../../../results/problems/geometry/problem_104.md) |
| 111 | open | 58 | medium_candidate | medium | graph theory; chromatic number; set theory | [problems/graph-theory/problem_111.md](../../../results/problems/graph-theory/problem_111.md) |
| 123 | open | 58 | medium_candidate | medium | number theory | [problems/number-theory/problem_123.md](../../../results/problems/number-theory/problem_123.md) |
| 124 | open | 58 | medium_candidate | medium | number theory; base representations | [problems/number-theory/problem_124.md](../../../results/problems/number-theory/problem_124.md) |
| 153 | open | 58 | medium_candidate | medium | sidon sets | [problems/sidon-sets/problem_153.md](../../../results/problems/sidon-sets/problem_153.md) |
| 168 | open | 58 | medium_candidate | medium | additive combinatorics | [problems/additive-combinatorics/problem_168.md](../../../results/problems/additive-combinatorics/problem_168.md) |
| 176 | open | 58 | medium_candidate | medium | additive combinatorics; arithmetic progressions; discrepancy | [problems/additive-combinatorics/problem_176.md](../../../results/problems/additive-combinatorics/problem_176.md) |
| 196 | open | 58 | medium_candidate | medium | arithmetic progressions | [problems/arithmetic-progressions/problem_196.md](../../../results/problems/arithmetic-progressions/problem_196.md) |
| 197 | open | 58 | medium_candidate | medium | arithmetic progressions | [problems/arithmetic-progressions/problem_197.md](../../../results/problems/arithmetic-progressions/problem_197.md) |
| 264 | open | 58 | medium_candidate | medium | irrationality | [problems/irrationality/problem_264.md](../../../results/problems/irrationality/problem_264.md) |
| 269 | open | 58 | medium_candidate | medium | irrationality | [problems/irrationality/problem_269.md](../../../results/problems/irrationality/problem_269.md) |
| 272 | open | 58 | medium_candidate | medium | additive combinatorics; arithmetic progressions | [problems/additive-combinatorics/problem_272.md](../../../results/problems/additive-combinatorics/problem_272.md) |
| 274 | open | 58 | medium_candidate | medium | group theory; covering systems | [problems/group-theory/problem_274.md](../../../results/problems/group-theory/problem_274.md) |
| 291 | open | 58 | medium_candidate | medium | number theory; unit fractions | [problems/number-theory/problem_291.md](../../../results/problems/number-theory/problem_291.md) |
| 295 | open | 58 | medium_candidate | medium | number theory; unit fractions | [problems/number-theory/problem_295.md](../../../results/problems/number-theory/problem_295.md) |
| 359 | open | 58 | medium_candidate | medium | number theory | [problems/number-theory/problem_359.md](../../../results/problems/number-theory/problem_359.md) |
| 390 | open | 58 | medium_candidate | medium | number theory; factorials | [problems/number-theory/problem_390.md](../../../results/problems/number-theory/problem_390.md) |
| 400 | open | 58 | medium_candidate | medium | number theory; factorials | [problems/number-theory/problem_400.md](../../../results/problems/number-theory/problem_400.md) |
| 411 | open | 58 | medium_candidate | medium | number theory; iterated functions | [problems/number-theory/problem_411.md](../../../results/problems/number-theory/problem_411.md) |
| 421 | open | 58 | medium_candidate | medium | number theory | [problems/number-theory/problem_421.md](../../../results/problems/number-theory/problem_421.md) |
| 468 | open | 58 | medium_candidate | medium | number theory; divisors | [problems/number-theory/problem_468.md](../../../results/problems/number-theory/problem_468.md) |
| 510 | open | 58 | medium_candidate | medium | analysis | [problems/analysis/problem_510.md](../../../results/problems/analysis/problem_510.md) |
| 513 | open | 58 | medium_candidate | medium | analysis | [problems/analysis/problem_513.md](../../../results/problems/analysis/problem_513.md) |
| 522 | open | 58 | medium_candidate | medium | analysis; polynomials; probability | [problems/analysis/problem_522.md](../../../results/problems/analysis/problem_522.md) |
| 536 | open | 58 | medium_candidate | medium | number theory | [problems/number-theory/problem_536.md](../../../results/problems/number-theory/problem_536.md) |
| 538 | open | 58 | medium_candidate | medium | number theory | [problems/number-theory/problem_538.md](../../../results/problems/number-theory/problem_538.md) |
| 600 | open | 58 | medium_candidate | medium | graph theory | [problems/graph-theory/problem_600.md](../../../results/problems/graph-theory/problem_600.md) |
| 629 | open | 58 | medium_candidate | medium | graph theory; chromatic number | [problems/graph-theory/problem_629.md](../../../results/problems/graph-theory/problem_629.md) |
| 634 | open | 58 | medium_candidate | medium | geometry | [problems/geometry/problem_634.md](../../../results/problems/geometry/problem_634.md) |
| 660 | open | 58 | medium_candidate | medium | geometry; distances; convex | [problems/geometry/problem_660.md](../../../results/problems/geometry/problem_660.md) |
| 661 | open | 58 | medium_candidate | medium | geometry; distances | [problems/geometry/problem_661.md](../../../results/problems/geometry/problem_661.md) |
| 671 | open | 58 | medium_candidate | medium | analysis | [problems/analysis/problem_671.md](../../../results/problems/analysis/problem_671.md) |
| 686 | open | 58 | medium_candidate | medium | number theory | [problems/number-theory/problem_686.md](../../../results/problems/number-theory/problem_686.md) |
| 691 | open | 58 | medium_candidate | medium | number theory | [problems/number-theory/problem_691.md](../../../results/problems/number-theory/problem_691.md) |
| 700 | open | 58 | medium_candidate | medium | number theory; binomial coefficients | [problems/number-theory/problem_700.md](../../../results/problems/number-theory/problem_700.md) |
| 731 | open | 58 | medium_candidate | medium | number theory; binomial coefficients | [problems/number-theory/problem_731.md](../../../results/problems/number-theory/problem_731.md) |
| 788 | open | 58 | medium_candidate | medium | additive combinatorics | [problems/additive-combinatorics/problem_788.md](../../../results/problems/additive-combinatorics/problem_788.md) |
| 790 | open | 58 | medium_candidate | medium | additive combinatorics | [problems/additive-combinatorics/problem_790.md](../../../results/problems/additive-combinatorics/problem_790.md) |
| 866 | open | 58 | medium_candidate | medium | number theory; additive combinatorics | [problems/number-theory/problem_866.md](../../../results/problems/number-theory/problem_866.md) |
| 911 | open | 58 | medium_candidate | medium | graph theory; ramsey theory | [problems/graph-theory/problem_911.md](../../../results/problems/graph-theory/problem_911.md) |
| 931 | open | 58 | medium_candidate | medium | number theory | [problems/number-theory/problem_931.md](../../../results/problems/number-theory/problem_931.md) |
| 939 | open | 58 | medium_candidate | medium | number theory | [problems/number-theory/problem_939.md](../../../results/problems/number-theory/problem_939.md) |
| 945 | open | 58 | medium_candidate | medium | number theory; divisors | [problems/number-theory/problem_945.md](../../../results/problems/number-theory/problem_945.md) |
| 956 | open | 58 | medium_candidate | medium | geometry; distances; convex | [problems/geometry/problem_956.md](../../../results/problems/geometry/problem_956.md) |
| 959 | open | 58 | medium_candidate | medium | geometry; distances | [problems/geometry/problem_959.md](../../../results/problems/geometry/problem_959.md) |
| 1004 | open | 58 | medium_candidate | medium | number theory | [problems/number-theory/problem_1004.md](../../../results/problems/number-theory/problem_1004.md) |
| 1011 | open | 58 | medium_candidate | medium | graph theory | [problems/graph-theory/problem_1011.md](../../../results/problems/graph-theory/problem_1011.md) |
| 1038 | open | 58 | medium_candidate | medium | analysis | [problems/analysis/problem_1038.md](../../../results/problems/analysis/problem_1038.md) |
| 1066 | open | 58 | medium_candidate | medium | graph theory; planar graphs | [problems/graph-theory/problem_1066.md](../../../results/problems/graph-theory/problem_1066.md) |
| 1074 | open | 58 | medium_candidate | medium | number theory | [problems/number-theory/problem_1074.md](../../../results/problems/number-theory/problem_1074.md) |
| 1084 | open | 58 | medium_candidate | medium | geometry; distances | [problems/geometry/problem_1084.md](../../../results/problems/geometry/problem_1084.md) |
| 1093 | open | 58 | medium_candidate | medium | number theory; binomial coefficients | [problems/number-theory/problem_1093.md](../../../results/problems/number-theory/problem_1093.md) |
| 1111 | open | 58 | medium_candidate | medium | graph theory | [problems/graph-theory/problem_1111.md](../../../results/problems/graph-theory/problem_1111.md) |
| 1112 | open | 58 | medium_candidate | medium | additive combinatorics | [problems/additive-combinatorics/problem_1112.md](../../../results/problems/additive-combinatorics/problem_1112.md) |
| 1120 | open | 58 | medium_candidate | medium | analysis | [problems/analysis/problem_1120.md](../../../results/problems/analysis/problem_1120.md) |
| 1122 | open | 58 | medium_candidate | medium | number theory | [problems/number-theory/problem_1122.md](../../../results/problems/number-theory/problem_1122.md) |
| 1132 | open | 58 | medium_candidate | medium | analysis; polynomials | [problems/analysis/problem_1132.md](../../../results/problems/analysis/problem_1132.md) |
| 1162 | open | 58 | medium_candidate | medium | group theory | [problems/group-theory/problem_1162.md](../../../results/problems/group-theory/problem_1162.md) |
| 1177 | open | 58 | medium_candidate | medium | set theory; chromatic number; hypergraphs | [problems/set-theory/problem_1177.md](../../../results/problems/set-theory/problem_1177.md) |
| 1182 | open | 58 | medium_candidate | medium | graph theory; ramsey theory | [problems/graph-theory/problem_1182.md](../../../results/problems/graph-theory/problem_1182.md) |
| 1188 | open | 58 | medium_candidate | medium | number theory; covering systems | [problems/number-theory/problem_1188.md](../../../results/problems/number-theory/problem_1188.md) |
| 1207 | open | 58 | medium_candidate | medium | geometry; distances | [problems/geometry/problem_1207.md](../../../results/problems/geometry/problem_1207.md) |
| 1210 | open | 58 | medium_candidate | medium | number theory | [problems/number-theory/problem_1210.md](../../../results/problems/number-theory/problem_1210.md) |
| 1212 | open | 58 | medium_candidate | medium | number theory; primes | [problems/number-theory/problem_1212.md](../../../results/problems/number-theory/problem_1212.md) |
| 361 | open | 57 | medium_candidate | medium | number theory | [problems/number-theory/problem_361.md](../../../results/problems/number-theory/problem_361.md) |
| 675 | open | 57 | medium_candidate | medium | number theory | [problems/number-theory/problem_675.md](../../../results/problems/number-theory/problem_675.md) |
| 524 | open | 56 | medium_candidate | medium | analysis; probability; polynomials | [problems/analysis/problem_524.md](../../../results/problems/analysis/problem_524.md) |
| 550 | open | 56 | medium_candidate | medium | graph theory; ramsey theory | [problems/graph-theory/problem_550.md](../../../results/problems/graph-theory/problem_550.md) |
| 730 | open | 56 | medium_candidate | medium | number theory; binomial coefficients; base representations | [problems/number-theory/problem_730.md](../../../results/problems/number-theory/problem_730.md) |
| 1059 | open | 56 | medium_candidate | medium | number theory; primes | [problems/number-theory/problem_1059.md](../../../results/problems/number-theory/problem_1059.md) |
| 50 | open | 55 | medium_candidate | medium | number theory | [problems/number-theory/problem_50.md](../../../results/problems/number-theory/problem_50.md) |
| 195 | open | 55 | medium_candidate | medium | arithmetic progressions | [problems/arithmetic-progressions/problem_195.md](../../../results/problems/arithmetic-progressions/problem_195.md) |
| 256 | open | 55 | medium_candidate | medium | analysis | [problems/analysis/problem_256.md](../../../results/problems/analysis/problem_256.md) |
| 470 | open | 55 | medium_candidate | medium | number theory; divisors | [problems/number-theory/problem_470.md](../../../results/problems/number-theory/problem_470.md) |
| 567 | open | 55 | medium_candidate | medium | graph theory; ramsey theory | [problems/graph-theory/problem_567.md](../../../results/problems/graph-theory/problem_567.md) |
| 617 | falsifiable | 55 | medium_candidate | medium | graph theory | [problems/graph-theory/problem_617.md](../../../results/problems/graph-theory/problem_617.md) |
| 669 | open | 55 | medium_candidate | medium | geometry | [problems/geometry/problem_669.md](../../../results/problems/geometry/problem_669.md) |
| 750 | open | 55 | medium_candidate | medium | graph theory; chromatic number | [problems/graph-theory/problem_750.md](../../../results/problems/graph-theory/problem_750.md) |
| 766 | open | 55 | medium_candidate | medium | graph theory; turan number | [problems/graph-theory/problem_766.md](../../../results/problems/graph-theory/problem_766.md) |
| 792 | open | 55 | medium_candidate | medium | additive combinatorics | [problems/additive-combinatorics/problem_792.md](../../../results/problems/additive-combinatorics/problem_792.md) |
| 953 | open | 55 | medium_candidate | medium | geometry; distances | [problems/geometry/problem_953.md](../../../results/problems/geometry/problem_953.md) |
| 1041 | falsifiable | 55 | medium_candidate | medium | analysis | [problems/analysis/problem_1041.md](../../../results/problems/analysis/problem_1041.md) |
| 1101 | open | 55 | medium_candidate | medium | number theory | [problems/number-theory/problem_1101.md](../../../results/problems/number-theory/problem_1101.md) |
| 1104 | open | 55 | medium_candidate | medium | graph theory; chromatic number | [problems/graph-theory/problem_1104.md](../../../results/problems/graph-theory/problem_1104.md) |
| 158 | open | 52 | medium_candidate | medium | sidon sets | [problems/sidon-sets/problem_158.md](../../../results/problems/sidon-sets/problem_158.md) |
| 827 | open | 52 | medium_candidate | medium | geometry | [problems/geometry/problem_827.md](../../../results/problems/geometry/problem_827.md) |
| 865 | open | 52 | medium_candidate | medium | number theory; additive combinatorics | [problems/number-theory/problem_865.md](../../../results/problems/number-theory/problem_865.md) |
| 428 | open | 48 | medium_candidate | medium | number theory; primes | [problems/number-theory/problem_428.md](../../../results/problems/number-theory/problem_428.md) |
| 180 | open | 6 | medium_candidate | medium | graph theory; turan number | [problems/graph-theory/problem_180.md](../../../results/problems/graph-theory/problem_180.md) |
| 348 | open | 6 | medium_candidate | medium | number theory; complete sequences | [problems/number-theory/problem_348.md](../../../results/problems/number-theory/problem_348.md) |
| 354 | open | 6 | medium_candidate | medium | number theory | [problems/number-theory/problem_354.md](../../../results/problems/number-theory/problem_354.md) |
| 778 | open | 6 | medium_candidate | medium | graph theory | [problems/graph-theory/problem_778.md](../../../results/problems/graph-theory/problem_778.md) |
| 1033 | open | 6 | medium_candidate | medium | graph theory | [problems/graph-theory/problem_1033.md](../../../results/problems/graph-theory/problem_1033.md) |
| 1117 | open | 6 | medium_candidate | medium | analysis | [problems/analysis/problem_1117.md](../../../results/problems/analysis/problem_1117.md) |
| 1143 | open | 6 | medium_candidate | medium | number theory; primes | [problems/number-theory/problem_1143.md](../../../results/problems/number-theory/problem_1143.md) |
| 1151 | open | 6 | medium_candidate | medium | analysis; polynomials | [problems/analysis/problem_1151.md](../../../results/problems/analysis/problem_1151.md) |
