### bounded above

- there exist upper bound such that every element of set less or equal upper bound

---
### bounded above formula

$$
\begin{aligned}
S \subset \mathbb R, \exists u \in \mathbb R, \forall x \in S: x \le u \\
u = \text{upper bound} 
\end{aligned}
$$

---
### bounded below

- there exist lower bound such that every element of set greater or equal lower bound

---
### bounded below formula

$$
\begin{aligned}
S \subset \mathbb R, \exists w \in \mathbb R, \forall x \in S: w \le x \\
w = \text{lower bound} 
\end{aligned}
$$

---
###  bounded

- both bounded below and bounded above

---
### bounded formula

$$
\begin{aligned}
S \subset \mathbb R, \exists u, w \in \mathbb R, \forall x \in S: w \le x \le u \\
u = \text{upper bound} \\
w = \text{lower bound} 
\end{aligned}
$$

---
### unbounded

- either unbounded below or unbounded above

---
### unbounded formula

$$
\begin{aligned}
S \subset \mathbb R, \exists u, w \in \mathbb R, \exists x \in S: (x < w) \lor (x > u) \\
u = \text{upper bound} \\
w = \text{lower bound}
\end{aligned}
$$

---
### supremum

- least upper bound of bounded above set

---
### supremum formula

$$
\begin{aligned}
(S \subset \mathbb R, \exists u \in \mathbb R, \forall x \in S: x \le u) \land (\exists u' \in \mathbb R: u' < u \rightarrow \exists x \in S: x > u') \rightarrow u = \sup S \\
u = \text{supremum} \\
\end{aligned}
$$

---
### infimum

- greatest lower bound of bounded below set

---
### infimum formula

$$
\begin{aligned}
(S \subset \mathbb R, \exists w \in \mathbb R, \forall x \in S: w \le x) \land (\exists w' \in \mathbb R: w' > w \rightarrow \exists x \in S: x < w') \rightarrow w = \inf S \\
w = \text{infimum} \\
\end{aligned}
$$

---
### completeness property

- for every nonempty bounded above set there exists supremum
- for every nonempty bounded below set there exists infimum

---
### completeness property formula

$$
\begin{aligned}
S \subset \mathbb R, \exists u \in \mathbb R, \forall x \in S: x \le u \rightarrow \exists \sup S \in \mathbb R \\
S \subset \mathbb R, \exists w \in \mathbb R, \forall x \in S: w \le x \rightarrow \exists \inf S \in \mathbb R \\
u = \text{upper bound} \\
w = \text{lower bound} 
\end{aligned}
$$

---
### upper bound property

- epsilon upper bound
- sub upper bound

---
### upper bound property

$$
\begin{aligned}
S \subset \mathbb R, \forall \epsilon > 0, \exists x \in S: x > u - \epsilon \rightarrow u = \sup S \\
S_2 \subset S_1 \subset \mathbb R \rightarrow \sup S_2 \le \sup S_1 \\
\end{aligned}
$$

---
### supremum addition property

- supremum of non-empty sum equal sum of supremum

---
### supremum addition property formula

$$
\begin{aligned}
\sup(S_1 + S_2) = \sup S_1 + \sup S_2 \\
S = \text{bounded above set}
\end{aligned}
$$

---
### supremum union property

- supremum of non-empty union equal maximum of supremum

---
### supremum union property formula

$$
\begin{aligned}
\sup(S_1 \cup S_2) = \max \set{\sup S_1, \sup S_2} \\
S = \text{bounded above set}
\end{aligned}
$$

---
### archimedean property

- natural numbers are unbounded above

---
### archimedean property formula

$$
\begin{aligned}
\forall x \in \mathbb R^+, \forall y \in \mathbb R, \exists n \in \mathbb N: y < nx
\end{aligned}
$$

---
### density property

- between every two real numbers there exists rational number

---
### density property formula

$$
\begin{aligned}
(x, y \in \mathbb R) \land (x < y) \rightarrow \exists q \in \mathbb Q: x < q < y
\end{aligned}
$$

---
### nth root property

- for every positive real number there exists unique positive real number root for every natural number power

---
### nth root property formula

$$
\begin{aligned}
\forall x \in \mathbb R^+, \exists !y \in \mathbb R^+, \forall n \in \mathbb N: y^n = x \\
y = \text{nth root}
\end{aligned}
$$

---
