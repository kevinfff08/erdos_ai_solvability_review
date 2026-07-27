# Verification audit: literal Erdős Problem 655

## Definitions and canonical target

Let \(X\subset\mathbb R^2\) be a finite set of \(n\) distinct points. Define

\[
D(X)=\bigl|\{\|x-y\|:x,y\in X,\ x\ne y\}\bigr|.
\]

Say that \(X\) satisfies \(A_2\) if, for every \(x\in X\) and every \(r>0\),

\[
|\{y\in X\setminus\{x\}:\|x-y\|=r\}|\le2.
\]

The literal website question is whether

\[
\exists c>0\ \exists N\ \forall n\ge N\ \forall X\subset\mathbb R^2,
\quad |X|=n\ \wedge\ A_2(X)\ \Longrightarrow\ D(X)\ge(1+c)n/2.
\]

Audit the claimed disproof by regular \(n\)-gons. The target is not to solve a repaired conjecture or to infer Erdős's intended wording.

Sources: [current problem page](https://www.erdosproblems.com/655), [discussion thread](https://www.erdosproblems.com/forum/thread/655), and [current Formal Conjectures file](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/655.lean).

## Accepted background

The problem page records Zach Hunter's observation that equally spaced points on a circle disprove the literal statement. This is a database claim, not a substitute for the verification required here.

For a regular \(n\)-gon with vertices \(x_i=e^{2\pi i i/n}\), the candidate chord lengths are

\[
\|x_i-x_{i+m}\|=2\sin(\pi m/n),\qquad 1\le m\le n-1.
\]

The current Formal Conjectures file encodes the literal local condition and says the literal answer is false, but its visible theorem body contains `sorry`; do not cite it as a completed checked proof without inspecting the linked historical artifact and build result. A recent non-refereed overview, [Erdős Problem #655 and Its Natural Repairs](https://www.ulam.ai/research/erdos655-overview.pdf), contains a detailed account of the same construction but must likewise be checked rather than treated as authority.

The forum records multiple non-equivalent possible repairs (general position, convex position, and others). Those are historical leads only.

## Complete resolutions

A complete verification of the disproof must prove all of the following.

1. For every \(n\ge3\), the regular \(n\)-gon is a set of \(n\) distinct planar points satisfying \(A_2\).
2. Its distinct global distances are exactly
   \[
   \{2\sin(\pi m/n):1\le m\le\lfloor n/2\rfloor\},
   \]
   and hence \(D(X)=\lfloor n/2\rfloor\).
3. For every \(c>0\), every regular \(n\)-gon satisfies
   \[
   \lfloor n/2\rfloor<(1+c)n/2.
   \]
4. Explicitly negate the original quantifiers: this infinite family prevents the existence of any \(c>0\) and threshold \(N\).

A complete contrary audit result would have to identify a genuine failure in the \(A_2\) verification or distance count, or establish from a primary source that a different statement—not the literal target above—is the record that must be audited.

## What does not count as a solution

- Repeating an OPEN database label, a forum post, a source-code comment, or an uncompiled formalization.
- Checking only a few small values of \(n\), plotting a polygon, or using floating-point equality tests.
- Proving only \(D(X)\ge\lfloor n/2\rfloor\), which is compatible with the counterexample.
- Counting pinned distances from a vertex in place of global \(D(X)\) without saying so.
- Quietly changing the target to general position, no-three-collinear, no-four-cocircular, convex, or a sum/pinned variant.
- Claiming an historical repair is Erdős's intended one without primary-source evidence.

## Required correctness checks

- Define precisely whether distances are over unordered or ordered pairs; the set of numerical values is unchanged, but the proof must not mix this with multiplicities.
- Prove that \(m\mapsto\sin(\pi m/n)\) is strictly increasing for \(1\le m\le\lfloor n/2\rfloor\).
- Prove that equality of chord lengths occurs only between steps \(m\) and \(n-m\); for even \(n\), handle the unique antipodal step \(m=n/2\) separately.
- Deduce \(A_2\) for every possible centre vertex and radius, not merely for the circumcircle.
- Check the strict inequality and the quantifier order \(\forall c>0\), not just one selected \(c\).
- Separate the literal global claim from the historically nearby pinned claim \(\max_x |\{\|x-y\|:y\ne x\}|\).
- If assessing the Lean artifact, require a commit hash, dependency lock, successful build, no admitted axioms/sorries on the proof path, and a definition-by-definition comparison with this target.

## Required deliverables

1. A concise, self-contained proof-verification report with numbered claims for the four complete-resolution conditions.
2. An explicit quantifier-negation paragraph.
3. A source table with direct URLs, access dates, author/publication status, and a label for each statement as proved, database-reported, formalized, or informal.
4. A separate historical-ambiguity note that lists candidate repairs without selecting one unless primary sources justify it.
5. If formalization is inspected, a reproducibility log with the exact revision, command, compiler/dependency versions, build output, and any remaining admissions.
6. `research_state.md` recording checked sources, exact definitions used, proof obligations passed/failed, and unresolved historical questions.

## Dynamic Multiagent v2 protocol

Create a research root that maintains an approach registry containing: target statement, sources checked, claimed subresult, proof dependencies, status, and adversarial-review outcome. Run at most four agents concurrently.

Begin with independent approaches rather than fixed roles: agents may separately audit the elementary geometry, inspect source/formal-artifact status, and reconstruct quantifiers. Register overlap before merging results. After an agent resolves or falsifies a subclaim, immediately reuse that slot for the strongest remaining unverified dependency or an adversarial audit.

Use multiple waves. In each wave, the root compares evidence, resolves contradictions, and assigns only narrowly stated next claims. No agent may promote a database label or an informal assertion to a proof. At least one independent agent must adversarially check the final chord-length classification, \(A_2\) quantification, parity case, and quantifier negation.

Proof-first allocation is mandatory. At most one optional computational subtask may run at a time, and only after the registry states its exact lemma, hypotheses, finite search domain or certificate, and stopping condition. For this audit, a permitted computation would only test a symbolic finite lemma for a specified range as a debugging aid; it cannot establish the all-\(n\) trigonometric claim. Reassign that slot immediately once its declared question is answered.

## Persistence and resumability

Maintain `research_state.md` after every wave: canonical target, source URLs and access dates, exact claims checked, proof sketches or formal-build logs, unresolved items, and the approach registry. Preserve failed attempts and explain why they failed.

If a runtime boundary interrupts the investigation before every complete-resolution condition and adversarial check has been recorded, write `CHECKPOINT_NOT_FINAL` at the top of `research_state.md`, state the next smallest verification task, and stop without declaring the audit complete. On resumption, read that state first, revalidate any time-sensitive web status, and continue from the unresolved proof obligation.
