### why natural numbers

- cardinality
- ordinality
- infinity

---
### why natural numbers formula

$$
\begin{aligned}
S = \emptyset \rightarrow |S| \not\in S \\ 
S = \emptyset \rightarrow x_n \not \in x_{n+1} \\
S = \emptyset \rightarrow \infty \not \in S \\
\end{aligned}
$$

---
### natural numbers

- set of whole numbers from 0 to positive infinity

---
### natural numbers formula

$$
\begin{aligned}
\mathbb N = \{0, 1, 2, \dots, \infty\}
\end{aligned}
$$

---
### peano axioms

- zero
- success
- distinct 
- induct

---
### peano axioms

$$
\begin{aligned}
0 \in \mathbb N \\
S(n) = n + 1 \rightarrow \forall n \in \mathbb N: S(n) \in \mathbb N \\
S(n) = S(m) \rightarrow n = m \\
(K \subset \mathbb N) \land (0 \in K) \land (\forall n \in K: S(n) \in K) \rightarrow K = \mathbb N
\end{aligned}
$$

---
### construct natural numbers

- initialize zero as the empty set
- successor equal the union of natural number with singleton set containing natural number
- natural numbers equal the set of successors

---
### construct natural numbers formula

$$
\begin{aligned}
0 &= \emptyset \\
1 &= S(0) = 0 \cup \{0\} = \{0\} \\
2 &= S(1) = 1 \cup \{1\} = \{0\} \cup \{1\} = \{0, 1\} \\
3 &= S(2) = 2 \cup \{2\} = \{0, 1\} \cup \{2\} = \{0, 1, 2\} \\
\vdots \\ 
\mathbb N &= \{S(n) | 0 \le n \le \infty\}
\end{aligned}
$$

---
### why integers

- subtraction

---
### why integers formula

$$
\begin{aligned}
\forall(m>n) \in \mathbb N: n - m \not\in \mathbb N
\end{aligned}
$$

---
### integers

- set of natural numbers and negative natural numbers

---
### integers formula

$$
\begin{aligned}
\mathbb Z = \{n - m| n, m \in \mathbb N \}
\end{aligned}
$$

---
### integer arithmetic

- addition
- multiplication

---
### integer arithmetic formula

$$
\begin{aligned}
[(m, n)] + [(m', n')] = [(m + m', n + n')] \\
[(m, n)] \cdot [(m', n')] = [(mm' + nn', mn' + nm')]
\end{aligned}
$$

---
### construct integers

- equivalence relation equal natural pairs with equal difference
- equivalence class equal the set of natural pairs with equal difference
- integers equal the set of equivalence classes

---
### construct integers formula

$$
\begin{aligned}
(m, n) \sim (m', n') \leftrightarrow m + n' = m' + n \\
[(m, n)] = \{(m', n') \in \mathbb N \times \mathbb N |(m, n) \sim (m', n')\} \\
\mathbb Z = \{[(m, n)] | (m, n) \in \mathbb N \times \mathbb N\}
\end{aligned}
$$

---
### why rational numbers

- division

---
### why rational numbers

$$
\begin{aligned}
\exists p, q \in \mathbb Z, q \ne 0: \frac{p}{q} \not\in \mathbb Z
\end{aligned}
$$

---
### rational numbers

- set of ratios of integers

---
### rational numbers formula

$$
\begin{aligned}
\mathbb Q = \{\frac{p}{q}| p, q \in \mathbb Z, q \ne 0\} \\
\end{aligned}
$$

---
### rational arithmetic

- addition
- multiplication

---
### rational arithmetic formula

$$
\begin{aligned}
[(p, q)] + [(p', q')] = [(pq' + qp', qq')] \\
[(p, q)] \cdot [(p', q')] = [(pp', qq')]
\end{aligned}
$$

---
### construct rational numbers

- equivalence relation equal integer pairs with equal quotient
- equivalence class equal the set of integer pairs with equal quotient
- rational numbers equal the set of equivalence classes

---
### construct rational numbers formula

$$
\begin{aligned}
(p, q) \sim (p', q') \leftrightarrow pq' = qp' \\
[(p, q)] = \{(p', q') \in \mathbb Z \times \mathbb Z |(p, q) \sim (p', q')\} \\
\mathbb Q = \{[(p, q)] | (p, q) \in \mathbb Z \times \mathbb Z\}
\end{aligned}
$$

---
### why real numbers

- irrationality

---
### why real numbers formula

$$
\begin{aligned}
\exists p, q \in \mathbb Z, q \ne 0: \frac{p}{q} \not\in \mathbb Q
\end{aligned}
$$

---
### real numbers

- set of rational numbers and irrational numbers

---
### real numbers formula

$$
\begin{aligned}
\mathbb R = \mathbb Q \cup \{\mathbb R ∖ \mathbb Q \}
\end{aligned}
$$

---
### set ordinality

- trichotomy
- transitivity

---
### set ordinality formula

$$
\begin{aligned}
x, y \in S \rightarrow (x < y) \lor (x = y) \lor (y < x) \\
(x, y, z \in S) \land (x < y) \land (y < z) \rightarrow x < z 
\end{aligned}
$$

---
### field

- set with two binary operations that satisfy the 9 field axioms

---
### field formula

$$
\begin{aligned}
(+) : F \times F \rightarrow F \\
(\cdot ) : F \times F \rightarrow F
\end{aligned}
$$

---
### field axioms

- additive commutativity
- additive associativity
- additive identity
- additive inverse
- distributivity
- multiplicative commutativity
- multiplicative associativity
- multiplicative identity
- multiplicative inverse

---
### field axioms formula

$$
\begin{aligned}
x + y = y + x \\
x + (y + z) = (x + y) + z \\
x + (-x) = 0 \\
x + 0 = x \\
x\cdot (y + z) = x \cdot y + x \cdot z \\
x \cdot y = y \cdot x \\
x \cdot (y \cdot z) = (x \cdot y) \cdot z \\
x \cdot (\frac{1}{x}) = 1 \\
x \cdot 1 = x \\
\end{aligned}
$$

---
### field ordinality

- addition
- multiplication
- reciprocal
- square
- negative

---
### field ordinality formula

$$
\begin{aligned}
(x, y, z \in F) \land (x < y) \rightarrow x + z < y + z \\
(x, y \in F) \land (x < y) \land (z > 0) \rightarrow x \cdot z < y \cdot z \\
0 < x < y \rightarrow 0 < \frac{1}{y} < \frac{1}{x} \\
x \ne 0 \rightarrow 0 < x^2  \\
x > 0 \leftrightarrow -x < 0 
\end{aligned}
$$

---
### field addition property

- equality
- identity
- inverse

---
### field addition property formula

$$
\begin{aligned}
x + y = x + z \rightarrow y = z \\
x + y = x \rightarrow y = 0 \\
x + y = 0 \rightarrow y = -x 
\end{aligned}
$$

---
### field multiplication property

- zero
- nonzero
- single negative
- double negative
- equality
- identity
- single inverse
- double inverse

---
### field multiplication property formula

$$
\begin{aligned}
0 \cdot x = 0 \\
(x \ne 0) \land (y \ne 0) \rightarrow x \cdot y \ne 0 \\
(-x) \cdot y = -(x \cdot y) = x \cdot (-y) \\
(-x) \cdot (-y) = x \cdot y \\
(x \ne 0) \land (x \cdot y = x \cdot z) \rightarrow y = z \\
(x \ne 0) \land (x \cdot y = x) \rightarrow y = 1 \\
(x \ne 0) \land (x \cdot y = 1) \rightarrow y = \frac{1}{x} \\
x \ne 0 \rightarrow \frac{1}{1/x} = x \\
\end{aligned}
$$

---
### complex number

- ordered pair of real numbers

---
### complex number formula

$$
\begin{aligned}
z = a + bi \\
a = \text{real part} \\
b = \text{imaginary part} \\
i = \sqrt {-1}
\end{aligned}
$$

---
### complex number property

- zero
- conjugate
- multiplication
- addition
- real

---
### complex number property formula

$$
\begin{aligned}
|z| > 0 \leftrightarrow z \ne 0 \\
|\overline z| = |z| \\
|zw| = (|z|)(|w|) \\
|z + w| \le |z| + |w| \\
|\text{Re}(z)| \le |z| 
\end{aligned}
$$

---
### complex conjugate

- ordered pair of real numbers with negative imaginary part

---
### complex conjugate formula

$$
\begin{aligned}
\overline z = a - bi \\
a = \text{Re}(z) \\
b = \text{Im}(z) \\
i = \sqrt {-1}
\end{aligned}
$$

---
### complex conjugate property

- conjugate addition
- conjugate multiplication
- real sum
- imaginary difference
- real product

---
### complex conjugate property formula

$$
\begin{aligned}
\overline {z + w} = \overline z + \overline w \\
\overline {z \cdot w} = \overline z \cdot \overline w \\ 
z + \overline z = \text{Re}(z) \\
z - \overline z = \text{Im}(z) \\
z \cdot \overline z \in \mathbb R^+ \leftrightarrow z \ne 0
\end{aligned}
$$

---
