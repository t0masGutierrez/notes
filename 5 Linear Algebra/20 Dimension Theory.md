### kernel
- subset of domain vectors that map to the codomain zero vector

---
### kernel formula
$$
\begin{aligned}
(L: \mathcal V \rightarrow \mathcal W) \implies \text{ker}(L) = \{\vec v \in \mathcal V | L(\vec v) = \vec 0_{\mathcal W}\} \\
L = \text{linear transformation} \\
\mathcal V = \text{domain vector space} \\
\mathcal W = \text{codomain vector space} \\
\vec v = \text{vector}
\end{aligned}
$$

---
### range
- subset of codomain vectors that map to domain vector

---
### range formula
$$
\begin{aligned}
(L: \mathcal V \rightarrow \mathcal W) \implies \text{range}(L) = \{L(\vec v)| \vec v \in \mathcal V \} \\
L = \text{linear transformation} \\
\mathcal V = \text{domain vector space} \\
\mathcal W = \text{codomain vector space} \\
\vec v = \text{vector}
\end{aligned}
$$

---
### subspace property
- kernel equal subspace of domain
- range equal subspace of codomain

---
### subspace property formula
$$
\begin{aligned}
(L: \mathcal V \rightarrow \mathcal W) \implies (\text{ker}(L) \le \mathcal V) \land (\text{range}(L) \le \mathcal W) \\
L = \text{linear transformation} \\
\mathcal V = \text{domain vector space} \\
\mathcal W = \text{codomain vector space} 
\end{aligned}
$$

---
### linear transformation kernel
- subset of domain vectors that solve the homogeneous system 

---
### linear transformation kernel formula
$$
\begin{aligned}
(L: \mathbb R^n \rightarrow \mathbb R^m) \land (\vec x \mapsto A\vec x) \implies \text{ker}(L) = \{\vec x \in \mathbb R^n| A\vec x = 0\} \\
|A| = m \times n \\
L = \text{linear transformation} \\
A = \text{matrix transformation} \\
\vec x = \text{vector}
\end{aligned}
$$

---
### linear transformation range
- linear combination of matrix transformation columns with domain

---
### linear transformation range formula
$$
\begin{aligned}
(L: \mathbb R^n \rightarrow \mathbb R^m) \land (\vec x \mapsto A\vec x) \implies \text{range}(L) = \{A\vec x \in \mathbb R^m | \vec x \in \mathbb R^n\} \\
|A| = m \times n \\
L = \text{linear transformation} \\
A = \text{matrix transformation} \\
\vec x = \text{vector}
\end{aligned}
$$

---
### kernel basis
- form the reduced row echelon of the matrix transformation
- fundamental solutions for homogeneous system equal basis vectors for kernel

---
### range basis
- basis via independence test

---
### dimension property
- range dimension
- kernel dimension

---
### dimension property formula
$$
\begin{aligned}
(L: \mathcal V \rightarrow \mathcal W) \land ([\vec w]_{C} = A_{BC} [\vec v]_{B} ) \implies \dim(\text{range} \ L) = \text{Rank}(A) \\
(L: \mathcal V \rightarrow \mathcal W) \land ([\vec w]_{C} = A_{BC} [\vec v]_{B} ) \implies \dim(\text{ker} \ L) = n - \text{Rank}(A) 
\end{aligned}
$$

---
### dimension theorem
- domain dimension equal kernel dimension addition with range dimension

---
### dimension theorem formula
$$
\begin{aligned}
(L: \mathcal V \rightarrow \mathcal W) \land (\dim(\mathcal V) \ne \infty)\implies  (\dim(\mathcal W) \ne \infty) \land (\dim(\text{ker} \ L) + \dim(\text{range} \ L) = n)
\end{aligned}
$$

---
### rank property
- matrix rank equal matrix transposition rank
- row space dimension equal column space dimension

---
### rank property formula
$$
\begin{aligned}
\text{Rank}(A) = \text{Rank}(A^T) \\
\dim(\text{Row} \ A) = \dim(\text{Col} \ A) \\
A = \text{matrix transformation} 
\end{aligned}
$$

---
