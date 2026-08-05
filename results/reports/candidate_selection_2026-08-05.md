# Candidate Selection and Deep-Audit Batch — 2026-08-05

## Improved three-round screening

1. **Signal screen.** Start from uncovered problems with strong historical solvability signals, clear finite statements, formalization availability, or substantial partial results. Do not rank solely by the old score.
2. **Mathematical-readiness screen.** Remove famous frontier problems with no plausible intermediate obligations, duplicate problem families, and entries whose apparent tractability comes only from finite computation. Prefer targets with a stable statement, reusable prior work, and proof-level verification paths.
3. **Current conflict screen.** Check the current problem page, history, discussion, exact-statement searches, and direct recent papers. Quarantine unrefereed or AI-generated solution claims; repair wording before scoring; retain closed discoveries as audits but do not publish solve prompts.

## Batch outcome

- Audited: 20
- Prompts published: 18
- Statuses: confirmed_open=11, revised_open=4, likely_open=3, insufficient_evidence=1, solved=1

| # | Source status | Audited status | Confidence | V2 score | Prompt | Key audit result |
|---:|---|---|---|---:|---|---|
| 167 | falsifiable | confirmed_open | high | 44 | [prompt](../prompts/problem_167.md) | 该命题是标准 Tuza 猜想。近期论文仍将其作为未解决猜想，并只证明随机图、稠密图和若干特殊结构中的情形；未发现一般图上的完整证明或反例。 |
| 274 | open | confirmed_open | high | 36 | [prompt](../prompts/problem_274.md) | 这是 Herzog--Schönheim 猜想的规范形式。2025 年预印本解决了有限单群和对称群，既强化了开放性证据，也表明一般群情形尚未解决。 |
| 276 | open | revised_open | high | 46 | [prompt](../prompts/problem_276.md) | 原题字面只要求不存在一个整数同时与所有项有非平凡公因子；2014 年论文已经构造 gcd(x_0,x_1)=1 且全为合数的序列，从而解决该字面版本。文献真正尚未证明的是“不存在有限素数覆盖”的加强版。 |
| 307 | verifiable | confirmed_open | medium | 62 | [prompt](../prompts/problem_307.md) | 题面明确，当前题目页仍列为可验证开放问题。2026 年结构性预印本给出必要条件和唯一性约束，但没有构造解或证明不可能。 |
| 396 | open | likely_open | medium | 60 | [prompt](../prompts/problem_396.md) | 当前题目页仍将该全称存在性命题列为开放，并给出 Pomerance 关于单个因子及另一方向连续乘积的结果。未定位到直接关闭全部 k 的论文。 |
| 488 | falsifiable | confirmed_open | high | 55 | [prompt](../prompts/problem_488.md) | 原始资料曾把 multiples 误写成 non-multiples；当前规范版本已修正。2026 年讨论给出 /A/=2、min(A)=2 和若干三元族的部分证明，但一般有限 A 仍开放。 |
| 506 | decidable | revised_open | high | 58 | [prompt](../prompts/problem_506.md) | 原题只写“不全共圆”，允许全共线点集并使圆数退化为 0，因此字面版本无效。加入“不全共线”后，Elliott--Purdy--Smith 给出 n>393 的最优公式，剩余小 n 仍需核验。 |
| 545 | open | revised_open | high | 28 | [prompt](../prompts/problem_545.md) | 原始对所有 m 的断言已有小 m 反例，不能继续作为开放猜想。较自然的现行目标是充分大 m 的版本或完整极值分类；一般上界 2^{O(sqrt m)} 已由 Sudakov 证明，但远弱于确定极值图。 |
| 617 | falsifiable | confirmed_open | high | 64 | [prompt](../prompts/problem_617.md) | Erdős--Gyárfás 已证明 r=3,4，且 r^2 版本对无穷多个 r 失败。当前题目页仍把 r^2+1 的全体 r≥3 版本列为可否证开放问题，未发现一般解。 |
| 628 | falsifiable | confirmed_open | high | 38 | [prompt](../prompts/problem_628.md) | 该规范形式仍是 Erdős--Lovász Tihany 猜想。2026 年最新预印本证明 even-hole-free 图等新类别，但没有覆盖一般图。 |
| 647 | verifiable | confirmed_open | high | 78 | [prompt](../prompts/problem_647.md) | 这是纯存在/否定型可验证问题。题目页 2026 年仍列为开放且无解答声明；形式化仓库只有局部模约束，没有给出无条件见证或不存在性证明。 |
| 699 | falsifiable | likely_open | medium | 66 | [prompt](../prompts/problem_699.md) | Erdős--Szekeres 已知两二项式系数总有非平凡公因子，但素因子下界 p≥i 是额外要求。当前页面仍列为可否证问题；2026 年计算核验到 n≤100000，但没有全称证明。 |
| 742 | decidable | confirmed_open | high | 54 | [prompt](../prompts/problem_742.md) | Füredi 已证明充分大 n，Fan 证明 n≤24 及 n=26，许多结构类也已解决；2025 年论文仍把完整有限 n 版本称为长期猜想。 |
| 750 | open | insufficient_evidence | low | 0 | — | 题目主页面仍标 open，但 2026 年论坛出现一份主要由 GPT-5.5 生成、声称用广义 Mycielski 图解决问题的短注，并有依赖外部公理的 Lean 形式化声明。尚未获得同行评议或充分独立证明审计，因此当前证据不足以安全判为 solved，也不应继续发布求解 Prompt。 |
| 779 | falsifiable | likely_open | medium | 26 | [prompt](../prompts/problem_779.md) | 题面清楚，当前页面记录 n≤1000 已核验和强烈启发式，但没有引用直接理论进展；广泛检索未发现关闭该精确命题的论文，因此只能列 likely_open。 |
| 848 | decidable | solved | high | 0 | — | Sawhney 已证明对充分大 N，最大值由模 25 的 7 类取得，并给出近极值稳定性；这正是题目页面所问的充分大 N 版本，因此状态为 solved，V2 分数固定为 0，不生成 Prompt。 |
| 993 | falsifiable | confirmed_open | high | 70 | [prompt](../prompts/problem_993.md) | 2026 年多份直接工作明确说单峰猜想仍开放：一份证明两类非对数凹树族仍单峰，另一份核验所有至多 29 顶点的树并给出结构约化。 |
| 1016 | open | confirmed_open | high | 52 | [prompt](../prompts/problem_1016.md) | Bondy 的上下界相差 log_*n 量级；Griffin 给出已发表/预印的基础下界证明。近期随机图论文研究稀疏泛圈子图，但没有提升确定性最小 h(n) 到所问下界。 |
| 1041 | falsifiable | confirmed_open | high | 68 | [prompt](../prompts/problem_1041.md) | Erdős--Herzog--Piranian 证明某个连通分支含至少两个根。2026 年预印本证明四次情形，但一般次数仍未解决。 |
| 1082 | falsifiable | revised_open | high | 46 | [prompt](../prompts/problem_1082.md) | 题目原含两个层次：全局距离种数下界，以及更强的单点距离下界。Harborth 的 8 点配置已否证单点加强版，但不否证全局下界；因此把规范开放核心修订为第一问。 |
