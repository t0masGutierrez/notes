### basis
- spanning
- linearly independent

---
### basis formula
$$
\begin{aligned}
\text{Span}(B) = \mathcal V \\
\text{Rank}(B) = n
\end{aligned}
$$

---
### spanning independence property
- size of linearly independent set less or equal size of spanning set

---
### spanning independence property formula
$$
\begin{aligned}
(\text{Span}(S) = \mathcal V) \land (|S| \ne \infty) \land(\text{Rank}(T) = n) \implies (|T| \ne \infty) \land (|T| \le |S|) \\
S, T \subseteq \mathcal V \\
S, T = \text{subset} \\
\mathcal V = \text{vector space} \\
|S|, |T| = \text{number of elements} \\
n = \text{number of columns} \\
\end{aligned}
$$

---
### basis equality property
- all bases share the same number of elements

---
### basis equality property formula
$$
\begin{aligned}
(\text{Span}(B_{1}, B_{2}) = \mathcal V) \land (\text{Rank}(B_{1}, B_{2}) = n) \land (|B_{1}| \ne \infty) \implies |B_{1}| = |B_{2}| \\
B = \text{basis} \\
\mathcal V = \text{vector space} \\
n = \text{number of columns} \\
|B| = \text{number of elements} \\
\mathcal V = \text{vector space} 
\end{aligned}
$$

---
### dimension
- number of elements of basis

---
### dimension formula
$$
\begin{aligned}
\dim(\mathcal V) = |B| \\
\mathcal V = \text{vector space} \\
B = \text{basis} \\
|B| = \text{number of elements}
\end{aligned}
$$

---
### dimension example
- $\mathbb R^n$ 
- $\mathcal P_{n}$ 
- $\mathcal M_{mn}$ 

---
### dimension example formula
$$
\begin{aligned}
\dim(\mathbb R^n) = n \\
\dim(\mathcal P_{n}) = n+1 \\
\dim(\mathcal M_{mn}) = mn \\
\end{aligned}
$$

---
### trivial dimension
- empty set equal basis of trivial vector space

---
### trivial dimension formula
$$
\begin{aligned}
\dim(\{\vec 0\}) = 0
\end{aligned}
$$

---
### dimension property
- size of spanning set 
- size of linearly independent set 
- size of basis

---
### dimension property formula
$$
\begin{aligned}
|S| < \dim(\mathcal V) \implies \text{Span}(S) = \mathcal V \\
|T| > \dim(\mathcal V) \implies \text{Rank}(T) = n \\
(|S| = \dim\mathcal V) \lor (|T| = \dim\mathcal V) \iff (S = B) \lor (T = B) \\
S, T \subseteq \mathcal V
\end{aligned}
$$

---
### subspace dimension property
- dimension of subspace less or equal dimension of vector space

---
### subspace dimension property formula
$$
\begin{aligned}
\mathcal W \le \mathcal V \implies \dim(\mathcal W) \le \dim (\mathcal V) \\
\dim(\mathcal W) = \dim (\mathcal V) \iff \mathcal W = \mathcal V
\end{aligned}
$$

---
### diagonalization basis property
- every set of fundamental eigenvectors via diagonalization equal basis of $n$-dimensional real numbers

---
### diagonalization basis property formula
$$
\begin{aligned}
A = PDP^{-1} \implies B = \{\vec x | A\vec x = \lambda \vec x \} \\
A = \text{matrix} \\
P = \text{eigenmatrix} \\
P^{-1} = \text{inverse eigenmatrix} \\
D = \text{diagonal matrix} \\
B = \text{basis} \\
\vec x = \text{eigenvector} \\
\lambda = \text{eigenvalue}
\end{aligned}
$$

---
