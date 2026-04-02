### linear dependence
- zero vector expressible as nontrivial linear combination of the vectors of subset

---
### linear dependence formula
$$
\begin{aligned}
\vec x \ne \vec 0 \implies \text{Rank}(S) < n \\
S = \{\vec v_{1}, \dots, \vec v_{n}\} \subseteq \mathcal V \\
\vec x = \text{solution} \\
S = \text{subset} \\
n = \text{number of columns} 
\end{aligned}
$$

---
### linear independence
- zero vector not expressible as nontrivial linear combination of the vectors of subset

---
### linear independence formula
$$
\begin{aligned}
\vec x = \vec 0 \implies \text{Rank}(S) = n \\
S = \{\vec v_{1}, \dots, \vec v_{n}\} \subseteq \mathcal V \\
\vec x = \text{solution} \\
S = \text{subset} \\
n = \text{number of columns} 
\end{aligned}
$$

---
### empty set
- linearly independent set with zero elements

---
### empty set formula
$$
\begin{aligned}
\emptyset = \{\}
\end{aligned}
$$

---
### linear independence example
- standard unit vector
- standard unit polynomial
- standard unit matrix

---
### linear independence example formula
$$
\begin{aligned}
\vec e \\
\vec p \\
\psi
\end{aligned}
$$

---
### single linear independence property
- subset with single nonzero vector equal linearly independent subset

---
### single linear independence property formula
$$
\begin{aligned}
(S = \{\vec v\}) \land (\vec v \ne 0) \implies \text{Rank}(S) = n \\
S = \text{subset} \\
\vec v = \text{vector} \\
c = \text{scalar} \\
n = \text{number of columns}
\end{aligned}
$$

---
### scalar multiplicity property
- subset without scalar multiple of vector equal linearly independent subset

---
### scalar multiplicity property formula
$$
\begin{aligned}
(\vec 0 = \sum_{i=1}^n c_{i}\vec v_{i}) \land (\not\exists \vec v_{i} = c\vec v_{j}) \implies \text{Rank}(S) = n \\
S = \text{subset} \\
\vec v = \text{vector} \\
c = \text{scalar} \\
n = \text{number of columns}
\end{aligned}
$$

---
### zero vector property
- subset with zero vector equal linearly dependent subset

---
### zero vector property formula
$$
\begin{aligned}
\vec 0 \in S \implies \text{Rank}(S) < n \\
S = \text{subset} \\
n = \text{number of columns}
\end{aligned}
$$

---
### independence test
- generate matrix whose columns equal the vectors of subset
- form the reduced row echelon of the system
- if number of pivot columns equal number of columns then linearly independent subset
- if number of pivot columns not equal number of columns then linearly dependent subset

---
### size property
- for collection of $n$ vectors, each with linear combination of the same $m$ coordinates, if $n = m$ then linear independence
- for collection of $n$ vectors, each with linear combination of the same $m$ coordinates, if $n > m$ then linear dependence

---
### size property formula
$$
\begin{aligned}
(S = \{\vec v_{1} \dots, \vec v_{n}\}) \land (\vec v \in \mathbb R^m) \land (n = m) \implies \text{Rank}(S) = n \\
(S = \{\vec v_{1} \dots, \vec v_{n}\}) \land (\vec v \in \mathbb R^m) \land (n > m) \implies \text{Rank}(S) \ne n
\end{aligned}
$$

---
### redundant vector
- vector expressible as linear combination of other vectors of subset

---
### redundant vector formula
$$
\begin{aligned}
\vec v \iff \text{Span}(S) = \text{Span}(S - \{\vec v\})\\
\vec v = \text{redundant vector} \\
S = \text{subset}
\end{aligned}
$$

---
### redundancy property
- subset without redundant vector equal linearly independent subset

---
### redundancy property formula
$$
\begin{aligned}
\nexists \vec v \in S \implies \text{Rank}(S) = n \\
\forall (2 \le k \le n): \vec v_{k} \not\in \text{Span}(\{\vec v_{1} \dots \vec v_{k-1} \}) \\
\vec v = \text{redundant vector} \\
S = \text{subset} \\
n = \text{number of columns}
\end{aligned}
$$

---
### infinite linear independence property
- every finite subset of infinite subset equal linearly independent subset

---
### infinite linear independence property formula
$$
\begin{aligned}
\text{Rank}(S_{1}, \dots, S_{k}) = n \implies \text{Rank}(S) = n \\
S_{1} \dots S_{k} \subseteq S \subseteq \mathcal V \\
S = \text{infinite subset} \\
\mathcal V = \text{vector space} 
\end{aligned}
$$

---
### unique linear independence property
- for every element of the span of linearly independent subset there exists unique linear combination of the vectors of linearly independent subset

---
### unique linear independence property formula
$$
\begin{aligned}
\forall \vec v \in \text{Span}(S)\exists !(c_{1} \vec v_{1} + \dots c_{k} \vec v_{k}) \implies \text{Rank}(S) = n \\
\vec v = \text{vector} \\
S = \text{subset} \\
c = \text{scalar} \\
n = \text{number of columns}
\end{aligned}
$$

---
### summary
- zero coefficient
- no redundant vector
- finite subset linear independence
---
