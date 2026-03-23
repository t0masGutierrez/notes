### finite linear combination

- linear combination of finite number of vectors

---
### finite linear combination formula

$$
\begin{aligned}
\vec v = c_1\vec v_1 + \dots + c_k\vec v_k \leftrightarrow \exists S' \subset S \subset \mathcal V \\
S' = \{\vec v_1, \dots , \vec v_k\} \\
S\prime = \text{finite subset} \\
S = \text{infinite subset} \\
\mathcal V = \text{vector space} \\
\vec v = \text{vector} \\
c = \text{scalar}
\end{aligned}
$$

---
### span

- set of all possible finite linear combinations of the vectors of subset
- smallest subspace of vector space with every vector of subset

---
### span formula

$$
\begin{aligned}
\text{Span}(S) = \{\sum_{i=1}^n c_i\vec v_i | c \in \mathbb R, \vec v \in S\} \\
S = \text{subset} \\
n = \text{dimension} \\
c = \text{scalar} \\
\vec v = \text{vector} 
\end{aligned}
$$

---
### terminology

- if span of subset equal vector space then vector space spanned by subset
- if span of subset equal vector space then subset spans vector space

---
### span example

- standard unit vector
- standard unit polynomial
- standard unit matrix

---
### span example formula

$$
\begin{aligned}
\text{Span}(\{\vec e_1, \dots , \vec e_n\}) = \mathbb R^n \\
\text{Span}(\{1, x, x^2, \dots , x^n\}) = \mathcal P\\
\text{Span}(\psi_{ij}) = \mathcal M_{mn} \\
\end{aligned}
$$

---
### empty span

- span of empty set

---
### empty span formula

$$
\begin{aligned}
\text{Span}(\emptyset) = \{\vec 0\}
\end{aligned}
$$

---
### span property

- subset
- subspace
- subset subspace
- intersection

---
### span property formula

$$
\begin{aligned}
S \subseteq \text{Span}(S) \\
\text{Span}(S) \le \mathcal V \\
(S \subseteq \mathcal W) \land (\mathcal W \le \mathcal V) \rightarrow \text{Span}(S) \subseteq \mathcal W \\
\text{Span}(S) = \bigcap \{\mathcal W \le \mathcal V| S \subseteq \mathcal W \}
\end{aligned}
$$

---
### span subset property

- span of subset equal subset of span

---
### span subset property formula

$$
\begin{aligned}
(S_1, S_2 \subseteq \mathcal V) \land (S_1 \subseteq S_2) \rightarrow \text{Span}(S_1) \subseteq \text{Span}(S_2) \\
S = \text{subset} \\
\mathcal V = \text{vector space} \\
\end{aligned}
$$

---
### row space

- set of all possible finite linear combinations of the rows of matrix equal the span of the set of rows of matrix

---
### row space formula

$$
\begin{aligned}
S = \set{\vec a_1, \dots, \vec a_n} \rightarrow \text{Row}(A) = \text{Span}(S) \\
\vec a = \text{row vector}
\end{aligned}
$$

---
### span test

- generate augmented matrix whose columns equal the vectors of set and whose constant matrix equal the possible member of span
- form the reduced row echelon of the system
- if consistent system then member of span
- if inconsistent system then not member of span

---
### span simplification

- generate matrix whose rows equal the vectors of subset
- form the reduced row echelon of the system
- nonzero rows of RREF equal the simple vectors of subset
- zero rows of RREF equal the redundant vectors of subset
- if number of nonzero rows equal number of rows then spanning set
- if number of nonzero rows not equal number of rows then nonspanning set

---
