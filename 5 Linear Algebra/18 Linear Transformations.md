### function
- map every element from A to 1 element of B

---
### function formula
$$
\begin{aligned}
f: A \to B \\
f(a) = b
\end{aligned}
$$

---
### domain
- if $f$ equal function from A to B then A equal domain of $f$ 

---
### codomain
- if $f$ equal function from A to B then B equal codomain of $f$ 

---
### preimage
- if $f(a) = b$ then *a* equal preimage of *b* 

---
### image
- if $f(a) = b$ then *b* equal image of *a* 

---
### range
- if $f$ equal function from A to B then subset of B equal range of $f$ 

---
### linear transformation
- function of vector space thats closed under vector addition and scalar multiplication

---
### linear transformation formula
$$
\begin{aligned}
L: \mathcal V \rightarrow \mathcal W \\
L(\vec v) = \vec w \\
L(\vec v_{1} + \vec v_{2}) = L(\vec v_{1}) + L(\vec v_{2}) \\
L(c\vec v) = cL(\vec v)
\end{aligned}
$$

---
### linear transformation property
- zero
- negation
- linearity

---
### linear transformation property formula
$$
\begin{aligned}
L(\vec 0_{\mathcal V}) = \vec 0_{\mathcal W} \\
L(-\vec v) = -L(\vec v) \\
L(c_{1}\vec v_{1} + \dots + c_{n}\vec v_{n}) = c_1L(\vec v_{1}) + \dots + c_nL(\vec v_{n}) \\
\end{aligned}
$$

---
### linear operator
- linear transformation whose domain equal codomain

---
### linear operator formula
$$
\begin{aligned}
L : \mathcal V \rightarrow \mathcal V \\
L = \text{linear transformation} \\
\mathcal V = \text{vector space}
\end{aligned}
$$

---
### identity linear operator
- linear transformation whose preimage equal image

---
### identity linear operator formula
$$
\begin{aligned}
i : \mathcal V \rightarrow \mathcal V \\
L(\vec v) = \vec v
\end{aligned}
$$

---
### translation
- translate vector along subspace

---
### translation formula
$$
\begin{aligned}
[v_{1}, \dots, v_{i}, \dots, v_{n}] \mapsto [v_{1}, \dots, v_{i} + c, \dots, v_{n}]
\end{aligned}
$$

---
### reflection
- reflect vector across subspace

---
### reflection formula
$$
\begin{aligned}
[v_{1}, \dots, v_{i}, \dots, v_{n}] \mapsto [v_{1}, \dots, -v_{i}, \dots, v_{n}]
\end{aligned}
$$

---
### contraction
- decrease vector along subspace

---
### contraction formula
$$
\begin{aligned}
[v_{1}, \dots, v_{i}, \dots, v_{n}] \mapsto [v_{1}, \dots, cv_{i}, \dots, v_{n}] \\
0 \le c \le 1
\end{aligned}
$$

---
### dilation
- increase vector along subspace

---
### dilation formula
$$
\begin{aligned}
[v_{1}, \dots, v_{i}, \dots, v_{n}] \mapsto [v_{1}, \dots, cv_{i}, \dots, v_{n}] \\
c > 1
\end{aligned}
$$

---
### projection
- project vector onto subspace

---
### projection formula
$$
\begin{aligned}
[v_{1}, \dots, v_{i}, \dots, v_{n}] \mapsto [v_{1}, \dots, 0, \dots, v_{n}]
\end{aligned}
$$

---
### rotation
- rotate vector about origin

---
### rotation formula
$$
\begin{aligned}
[v_{1}, \dots, v_{i}, \dots, v_{n}] \mapsto \begin{bmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{bmatrix} \begin{bmatrix} v_{1} \\ \vdots \\ v_{i} \\ \vdots \\ v_{n} \end{bmatrix} 
\end{aligned}
$$

---
### matrix transformation
- map every element from $\mathbb R^n$ to 1 element of $\mathbb R^m$ 

---
### matrix transformation formula
$$
\begin{aligned}
L : \mathbb R^n \rightarrow \mathbb R^m \\
L(\vec x) = A\vec x
\end{aligned}
$$

---
### composite transformation property
- composition of linear transformation equal linear transformation 

---
### composite transformation property formula
$$
\begin{aligned}
(L_{1}: \mathcal V_{1} \rightarrow \mathcal V_{2}) \land (L_{2}: \mathcal V_{2} \rightarrow \mathcal V_{3}) \implies L_{2} \circ L_{1} : \mathcal V_{1} \rightarrow \mathcal V_{3} \\
(L_{2} \circ L_{1})(\vec v) = L_{2}(L_{1}(\vec v))
\end{aligned}
$$

---
### subspace transformation property
- image of domain subspace equal subspace of codomain
- inverse image of codomain subspace equal subspace of domain

---
### subspace transformation property formula
$$
\begin{aligned}
(L : \mathcal V \rightarrow \mathcal W) \land (\mathcal V' \le \mathcal V) \implies L(\mathcal V') = \{L(\vec v) | \vec v \in \mathcal V'\} \le \mathcal W \\
(L : \mathcal V \rightarrow \mathcal W) \land (\mathcal W' \le \mathcal W) \implies L^{-1}(\mathcal W') = \{\vec v | L(\vec v) \in \mathcal W'\} \le \mathcal V
\end{aligned}
$$

---
