### induction

- instance prove general propositional function true for all positive integers
---
### induction formula

$$
\begin{aligned}
P(1) \\
P(k) \to P(k + 1) \\
\therefore \forall nP(n)
\end{aligned}
$$

---
### calculate induction

- prove statement true for the 1st element $S₁$
- assume $Sₖ$ true for all *n = k* by replacing *n* with *k*
- prove $Sₖ+₁$ true by substituting $(k + 1)$ into $S_k$
- solve and conclude $S_{k + 1}$ true for all positive integers

---
### basis step

- proof of $P(1)$ for proof by induction of $\forall nP(n)$

---
### inductive step

- proof of $P(k) → P(k + 1)$ for proof by induction of $\forall nP(n)$

---
### well ordering property

- every nonempty subset of nonnegative integers has least element

---
### strong induction

- instance prove general propositional function true for all positive integers less than *k*
---
### strong induction formula

$$
\begin{aligned}
P(1) \\
P(j) \to P(j + 1) \\
\therefore \forall nP(n) \\
j = 1, 2, ... k
\end{aligned}
$$

---
### calculate strong induction

- prove statement true for the 1st element $S₁$
- assume $Sₖ$ true for all $n \le k$ by replacing *n* with *k*
- prove $Sₖ+₁$ true by substituting $(k + 1)$ into $S_k$
- solve and conclude $S_{k + 1}$ true for all positive integers

---
