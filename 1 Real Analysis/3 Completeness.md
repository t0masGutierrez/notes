### bounded above
- there exist upper bound such that every element of set less or equal upper bound

---
### bounded above formula
$$
\begin{aligned}
S \subset \mathbb R, \exists u \in \mathbb R, \forall x \in S: x \le u \\
S = \text{bounded above set} \\
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
S = \text{bounded below set} \\
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
S = \text{bounded set} \\
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
S = \text{unbounded set} \\
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
(S \subset \mathbb R, \exists u \in \mathbb R, \forall x \in S: x \le u) \land (\exists u' \in \mathbb R: u' < u \implies \exists x \in S: x > u') \implies u = \sup S \\
S = \text{bounded above set} \\
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
(S \subset \mathbb R, \exists w \in \mathbb R, \forall x \in S: w \le x) \land (\exists w' \in \mathbb R: w' > w \implies \exists x \in S: x < w') \implies w = \inf S \\
S = \text{bounded below set} \\
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
S \subset \mathbb R, \exists u \in \mathbb R, \forall x \in S: x \le u \implies \exists \sup S \in \mathbb R \\
S \subset \mathbb R, \exists w \in \mathbb R, \forall x \in S: w \le x \implies \exists \inf S \in \mathbb R \\
S = \text{bounded set} \\
u = \text{upper bound} \\
w = \text{lower bound} 
\end{aligned}
$$

---
### supremum epsilon property
- set greater supremum subtraction with epsilon

---
### supremum epsilon property formula
$$
\begin{aligned}
S \subset \mathbb R, \forall \epsilon > 0, \exists x \in S: x > u - \epsilon \implies u = \sup S \\
S = \text{bounded above set} \\
u = \text{supremum}
\end{aligned}
$$

---
### supremum subset property
- subset of set equal subset of supremum

---
### supremum subset property formula
$$
\begin{aligned}
S_{2} \subset S_{1} \subset \mathbb R \implies \sup S_{2} \le \sup S_{1} \\
S = \text{bounded above set}
\end{aligned}
$$

---
### supremum addition property
- supremum of nonempty sum equal sum of supremum

---
### supremum addition property formula
$$
\begin{aligned}
\sup(S_{1} + S_{2}) = \sup S_{1} + \sup S_{2} \\
S = \text{bounded above set}
\end{aligned}
$$

---
### supremum union property
- supremum of nonempty union equal maximum of supremum

---
### supremum union property formula
$$
\begin{aligned}
\sup(S_{1} \cup S_{2}) = \max \set{\sup S_{1}, \sup S_{2}} \\
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
(x, y \in \mathbb R) \land (x < y) \implies \exists q \in \mathbb Q: x < q < y
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
