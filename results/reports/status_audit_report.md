# Evidence-backed Status Audit

- Generated: 2026-08-04
- Audited: 104 / 682
- Source-status changes or revisions: 29

## Current status distribution

| Status | Count |
|---|---:|
| confirmed_open | 41 |
| likely_open | 34 |
| revised_open | 20 |
| disproved | 6 |
| solved | 2 |
| ambiguous | 1 |

## Complete source-to-audit matrix

| Source status | Audited status | Count |
|---|---|---:|
| decidable | likely_open | 1 |
| decidable | revised_open | 1 |
| falsifiable | confirmed_open | 3 |
| falsifiable | likely_open | 3 |
| falsifiable | revised_open | 1 |
| open | ambiguous | 1 |
| open | confirmed_open | 37 |
| open | disproved | 6 |
| open | likely_open | 30 |
| open | revised_open | 18 |
| open | solved | 2 |
| verifiable | confirmed_open | 1 |

## Source-to-audit conflicts and revised targets

| # | Source status | Audited status | Confidence | Summary |
|---:|---|---|---|---|
| 12 | open | revised_open | high | 该数据库条目原含三个问题。2026 年 4 月的可审查 Lean 形式化工件及其附带的人类可读论证已确认：第一个问题答案为“是”，第二个问题答案为“否”。因此原始复合条目不能再整体标为 open；唯一明确存留的开放核心是第三问：每个具有 Property P 的集合的倒数和是否必收敛。 |
| 18 | open | revised_open | medium | 原始 1981 年表述把非 practical 的 n 定义为 S(n)=0，因此若不限制 n 为 practical，"无穷多个 n" 版本平凡成立。当前 Erdős Problems 页面已将主问题修订为只量化 practical m，并仍标为 open；其余两个关于 n! 的问题是并列但逻辑上不同的开放变体。未发现可核验的解决或反例声明。 |
| 19 | decidable | revised_open | medium | 原命题尚不能标为完全证明：Kang、Kelly、Kühn、Methuku、Osthus 的同行评审论文证明了所有充分大的 n，但未覆盖的仅为有限多个 n。因而原始“对所有 n”命题已被实质性改写为一个有限剩余核；Erdős Problems 论坛也明确将其社区数据库状态称为“decidable rather than proved”。截至审计日，未找到覆盖全部 n 的可核验论文、形式化或反例。 |
| 32 | open | revised_open | medium | 该数据库条目把三个问题并列，但它们的状态不同：Ruzsa（1998）已证明任一覆盖所有充分大整数的加法补集均满足 liminf A(x)/log x≥e^γ>1，故第三问已肯定解决。其余核心仍是：是否存在 A 使 P+A 包含所有充分大整数且 A(x)=o((log x)^2)；更强地，能否做到 A(x)=O(log x)。2026年1月仍标为 open 的 Erdős Problems 页面与2011/2014文献均支持该判断；本次未找到可核验的后续解决论文或严肃反例。 |
| 33 | open | revised_open | medium | 输入把两个问题并列在同一条目中。第二问“对每个平方数加法补集，liminf 是否大于 1？”早已由 Moser 的 1965 年结果肯定解决，且后续工作给出 liminf≥4/π。仍然开放的精确目标是：在所有平方数加法补集中最小化增长常数 limsup A(N)/√N（严格说应取下确界）；截至本次检索未发现该常数的确定或匹配上下界。Erdős Problems 页面及其 2026-03 论坛讨论仍将该剩余优化问题标为 open。 |
| 65 | open | disproved | high | 按题面最自然的全称精确读法，第二问已被小参数可行性反例否定：n=5、kn=5 时不存在同时有 5 个顶点和 5 条边的完全二分图（其边数只能为 0、4 或 6），所以该极值不可能“由完全二分图取得”。第一问早已解决。题目的显然意图是一个需补足参数的精确极值猜想；Montgomery 2025 年同行评议综述报告该修正版在大 d 情形已有 forthcoming work 的精确证明，但本次未找到该工作的可审查论文或预印本，不能把该报告升级为已核验的完整解答。 |
| 75 | open | revised_open | medium | 当前精确版本应视为“修订后仍开放”：ZFC 中是否存在同时满足 \|V(G)\|=χ(G)=ℵ₁ 且所有大有限子图均有 n^{1-o(1)} 级独立集的图，未找到已核验的解决。此前漏掉 \|V(G)\|=ℵ₁ 条件的版本已由 Lambie-Hanson (2020) 的有限子图色数增长结果推出；因此该旧版本不能再作为开放题。CH 下已有更强的线性独立集构造，而 Komjáth–Shelah 给出了相关 ℵ₁-大小结论的一致性结果；二者均不是该无条件 ZFC 目标的解决。 |
| 78 | open | revised_open | medium | 题库当前页面及其论坛索引仍将第78题列为 open，且针对精确目标的检索未发现可核查的解决或反例。最新已核实的决定性进展是 Li 在 FOCS 2023 给出的显式 K-Ramsey 图，其中 K=log^{O(1)}N；这仍未达到 K=O(log N)。不过原文的“constructive proof”未规定算法模型：若只要求可计算而不要求效率，穷举图可把已知存在性结论机械化，因而会使题意失真。以下将尚存的、文献中通常意指的强显式版本作为修订后的开放目标。 |
| 80 | open | revised_open | medium | 原记录的字面参数域有缺陷：简单图中 c>=1/2 时不存在满足 e(G)>=cn^2 的图，故“最大 m”不定义。将其修复为固定 0<c<1/2、n 足够大后，c>=1/4 的量级已是线性；困难且仍开放的区间是 0<c<1/4。Fox–Loh 已否定原“正幂下界”猜想，但截至本次检索，固定 c<1/4 的对数下界及完整渐近估计仍未见可核验的解决。 |
| 84 | open | revised_open | high | 原记录把两个独立断言并列：上界断言 f(n)=o(2^n) 已由 Verstraëte（2004）证明，且被 Nenadov（2026）加强；尚存的精确定义良好的目标是证明 f(n)/2^{n/2}→∞。Nenadov 的同行评审论文明确称 Faudree 的 2^{n/2} 构造为“best known lower bound”，并称任何固定正指数改进都很有意义，支持该较弱剩余断言截至审计日仍未解决。 |
| 87 | open | revised_open | medium | 按字面量词，第一问已被一个初等反例否定：取 ε=2、任意充分大的偶数 k 及 G=K_k，则要求 R(k)>R(k)，矛盾。因此“ε>0”不能照字面保留。网页备注“ε≥3/4 时平凡”显示其显然意图是 0<ε<1；在这一修复下，及对独立的常数因子强版本，本次检索未找到已验证的解答，当前 Erdős Problems 讨论页仍标为 Open（2026-01-17 编辑、0 条评论）。故该记录只能作为需人工确认修复后的开放目标处理，而非照原文直接求解。 |
| 90 | open | disproved | high | 原命题已被否定，而非仍属开放问题。2026 年的可检查论文给出固定 ε>0 及无穷多个 n，使某些 n 点欧氏平面点集具有至少 n^{1+ε} 条单位距离对；这与“存在常数 C，使所有充分大的 n 均有 u(n)≤n^{1+C/log log n}”矛盾。Sawin 随后给出显式指数 1.014114 的版本。精确的 u(n) 增长率和 4/3 上界的改进仍开放，但它们不是输入中这条断言。 |
| 92 | open | disproved | high | 题目原文的两个渐近上界猜想均已被否定。2026 年的单位距离构造给出无穷多个 n 点集，单位距离对数至少为 n^{1+δ}；删去低度顶点可取到最小度为正幂的子图，而单位距离对正是每个顶点的一批等距邻点。因此得到无穷多个 m 使 f(m)≥m^α（某个 α>0），同时否定 f(n)≤n^{o(1)} 及更强的 n^{O(1/log log n)} 上界。 |
| 114 | falsifiable | revised_open | high | 原命题仍未被完整证明或反驳，但其研究形态已实质改变。Tao 的 2025 年预印本证明：对所有充分大的次数 n，z^n-1（允许平移和旋转）是唯一极大元；n=1 平凡，n=2 已由 Eremenko–Hayman 证明。因此严格剩余目标是 Tao 有效但未优化的阈值以下的有限个次数（其中 n>=3）的情形。论坛中有 n=3 的手稿以及 n<=14 的区间算术证书声明，但它们是未同行评审的作者/论坛材料；且证书历史上出现过 n=13 的实现错误并修补，不能据此将任何这些次数计为已独立验证闭合。 |
| 119 | open | revised_open | medium | 该条目包含三个层次的问题：前两问已分别由 Wagner（1980）与 Beck（1991）肯定解决；唯一明确存留的目标是第三问的全体大 n 累积下界。2026-07-20 起有媒体转述 GPT-5.6/Korsky 已解决第三问的说法，但审计时没有找到可检查的论文、预印本、完整论证或无 sorry 的形式化证明；Erdős Problems 的可访问当前索引副本仍标为 OPEN，论坛线程也仍无任何解答声明。因此应将其作为“已部分解决后剩余的开放目标”，而非已解决问题。 |
| 122 | open | ambiguous | high | 字面记录不是一个可唯一赋值真假的命题：它说“有无穷多个 x 使得一个仍依赖 x 的量趋于无穷”，但没有定义该极限沿何变量/子序列取得。因此不能把数据库的 open 标签直接转为一个可求解的开放题。1997 年 EPS 论文确实证明了关于 h(n)=n+ω(n) 的局部重复值和集中现象；数据库还报告 Erdős 称 τ、ω 满足更一般断言、φ、σ“probably fails”，但本审计未能取得 Er97/Er97e 正文来核对其精确量词。未发现 2023–2026 年解决该“任意 F 的分类”版本的可检查证明。 |
| 123 | open | disproved | high | 按网页当前的字面量词，命题已被反驳：允许底数 1，而 (a,b,c)=(1,5,7) 两两互素；相应集合正是 {5^l7^m:l,m≥0}。Erdős–Lewin 的两底数定理表明它仅在底数集合为 {2,3} 时才 d-完全，故该集合不是 d-完全。网站仍标为 open，但论坛已明确指出“≥1”是笔误，Lean 表述也改用 a,b,c>1；修正后的三底数全称猜想则未由本审计证实已解决。 |
| 124 | open | revised_open | high | 输入中的字面阈值误将每一项都写成 d_r：在严格递增且 d_1>=3 时，该条件根本没有可取的有限 bases，故字面两问均真空平凡。主文献 BEGL96 与当前 Formal Conjectures 记录均使用 sum_i 1/(d_i-1)>=1；修复后，允许 1 的 k=0 版本已解决，而 gcd=1、任意 k>=1 的 BEGL 版本仍开放。因此应将条目作为“需修复转录后可研究的剩余开放目标”，而非按输入字面尝试。 |
| 129 | open | disproved | high | 按可自然重建的字面命题，结论是假的。取 r=2，随机红蓝边染色可在 N=exp(cn) 个顶点上保证每个 n 顶点集同时含红三角形和蓝三角形，故 R(n;3,2)≥exp(cn)，与任何 C^{√n} 上界矛盾。Erdős Problems 页面及其论坛线程也明确记录了 Antonio Girão 的这一反驳。原始作者可能另有意图，但尚无可核验的修订题面；这不改变字面命题已被否定的状态。 |
| 131 | open | revised_open | high | 原题的具体 N^{1/2-o(1)} 下界已由非平均集上界否定，但估计 F(N) 的主问题仍开放，因此规范状态为 revised_open。 |
| 261 | open | revised_open | high | “无穷多个 n”已解决；原文把全体 n 与连续统表示两个不同问题并列，且历史上弱化成“两种表示”的版本会被简单恒等式平凡化，因此需修订。 |
| 278 | open | revised_open | high | Simpson 已用容斥证明所有 a_i 相等取得最小密度；最大密度仍开放，故为 revised_open。 |
| 569 | open | solved | medium | 字面问题已被 2026 年 Cambie 与 Freschi 的公开预印本解决。其定理对任意整数 t≥3 与任意无孤立点、m≥1 条边的图 H 给出 R(C_t,H)≤(t−1)m+1≤tm。代入 t=2k+1 得 R(C_{2k+1},H)≤(2k+1)m；取 H=K_2（m=1）时 R(C_{2k+1},K_2)=2k+1，故最优常数恰为 c_k=2k+1。Erdős Problems 页面仍标为 open，但其最后编辑于该预印本之前，属数据库滞后。 |
| 635 | open | revised_open | high | 原记录把两个不同强度的问题并列。对每个固定 t，渐近上界 F_t(N)≤(1/2+o_t(1))N 已被网站及讨论页明确标为已解决；但“如何大”的更精确问题仍开放，网站仍标记整个条目为 open。最自然的明确剩余靶标是：对每个固定 t≥2，证明或反驳 F_t(N)≤N/2+O_t(log N)。这与已知 t=2 的 N/2+c log N 下界匹配；不过 Tao 仅称这种精度“probably”是 Erdős 所求，故其作为原始问题的规范化残余目标仍需人工确认。 |
| 654 | open | revised_open | high | Aletheia 的两直线构造否定无一般位置条件的强猜想，但未触及较弱线性改进，也未否定附加无三点共线的强版本；规范目标取较弱开放核心。 |
| 655 | open | disproved | high | 按网页所写的字面命题，其真值已可由正 n 边形严格否定：正 n 边形满足“以配置中一点为圆心的任一圆至多含另外两点”，却仅确定 ⌊n/2⌋ 个全局不同距离。因此对任意 c>0，它都小于 (1+c)n/2。历史上原作者可能意图的附加一般位置/钉住距离版本并不唯一，不能把它们视为同一题。 |
| 786 | open | revised_open | high | 若允许重复，两个密度一问题均为否且有限密度有尖锐常数；只有互异元素版本仍开放，但原始来源对此约定存在实质歧义。 |
| 888 | open | solved | high | 2026 年公开证明给出与半素数下界匹配到常数因子的上界，原站于 2026-05-28 改为 SOLVED；按规则 V2 评分固定为 0 且不发布研究 prompt。 |
| 893 | open | revised_open | high | Kovač–Luca 已证明比值 limsup=∞，所以原“是否有有限极限”已否；剩余自然问题是扩展实数意义下是否趋于 +∞。 |
