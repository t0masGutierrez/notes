### bijective linear transformation

- every element of codomain map to 1 element of domain
- one to one and onto

---
### bijective linear transformation formula

$$
\begin{aligned}
(L: \mathcal V \rightarrow \mathcal W) \leftrightarrow (\forall \vec v_1, \vec v_2 \in \mathcal V: L(\vec v_1) = L(\vec v_2) \rightarrow \vec v_1 = \vec v_2) \land (\forall \vec w \in \mathcal W, \exists \vec v \in \mathcal V: L(\vec v) = \vec w) \\
L = \text{bijective linear transformation} \\
\mathcal V = \text{domain vector space} \\
\mathcal W = \text{codomain vector space} \\
\vec v = \text{preimage vector} \\
\vec w = \text{image vector} 
\end{aligned}
$$

---
### isomorphism

- bijective linear transformation

---
### isomorphism formula

$$
\begin{aligned}
(L: \mathcal V \rightarrow \mathcal W) \leftrightarrow \forall \vec w \in \mathcal W, \exists! \vec v \in \mathcal V: L(\vec v) = \vec w \\
L = \text{isomorphism} \\
\mathcal V = \text{domain vector space} \\
\mathcal W = \text{codomain vector space} \\
\vec v = \text{preimage vector} \\
\vec w = \text{image vector} 
\end{aligned}
$$

---
### inverse linear transformation

- composition of linear transformation and inverse linear transformation equal preimage vector

---
### inverse linear transformation formula

$$
\begin{aligned}
(\exists L^{-1}: \mathcal W \rightarrow \mathcal V) \leftrightarrow (\forall \vec v \in \mathcal V: (L^{-1} \circ L)(\vec v) = \vec v) \land (\forall \vec w \in \mathcal W: (L \circ L^{-1})(\vec w) = \vec w) \\
L: \mathcal V \rightarrow \mathcal W \\
L = \text{linear transformation} \\
L^{-1} = \text{inverse linear transformation} \\
\mathcal V, \mathcal W = \text{vector space} \\
\vec v, \vec w = \text{vector} 
\end{aligned}
$$

---
### inverse isomorphism property

- for every isomorphism there exists inverse linear transformation

---
### inverse isomorphism property formula

$$
\begin{aligned}
L = \text{isomorphism} \leftrightarrow \exists L^{-1} \\
L: \mathcal V \rightarrow \mathcal W \\
L = \text{linear transformation} \\
L^{-1} = \text{inverse linear transformation} \\
\mathcal V, \mathcal W = \text{vector space} 
\end{aligned}
$$

---
### matrix isomorphism property

- for every isomorphism there exists nonsingular square matrix transformation

---
### matrix isomorphism property formula

$$
\begin{aligned}
L = \text{isomorphism} \leftrightarrow \det (A_{BC}) \ne 0 \\
L: \mathcal V \rightarrow \mathcal W \\
|A| = n \times n \\
L = \text{linear transformation} \\
A = \text{matrix transformation} \\
\end{aligned}
$$

---
### spanning independence property

- independent bijective preimage equal linearly independent image
- spanning bijective preimage equal spanning image

---
### spanning independence property

$$
\begin{aligned}
(L = \text{bijection}) \land (\text{rank}(T \subseteq \mathcal V) = n) \rightarrow \text{rank}(L(T) \subseteq \mathcal W) = n \\
(L = \text{bijection}) \land (\text{span}(S \subseteq \mathcal V) = \mathcal V) \rightarrow \text{span}(L(S) \subseteq \mathcal W) = \mathcal W \\
\end{aligned}
$$

---
### isomorphic vector space

- there exists isomorphism between both vector space

---
### isomorphic vector space formula

$$
\begin{aligned}
\mathcal V \cong \mathcal W \leftrightarrow \exists L: \mathcal V \rightarrow \mathcal W \\
\mathcal V = \text{domain vector space} \\
\mathcal W = \text{codomain vector space} \\
L = \text{isomorphism} \\
\end{aligned}
$$

---
### isomorphic dimension property

- equal dimension between isomorphic vector space

---
### isomorphic dimension property formula

$$
\begin{aligned}
\mathcal V \cong \mathcal W \leftrightarrow \dim(\mathcal V) = \dim(\mathcal W) \ne \infty \\
\mathcal V = \text{domain vector space} \\
\mathcal W = \text{codomain vector space} 
\end{aligned}
$$

---
### isomorphic n-dimensional property

- n-dimensional vector space isomorphic with n-dimensional real numbers

---
### isomorphic n-dimensional property formula

$$
\begin{aligned}
\dim(\mathcal V) = n \rightarrow \mathcal V \cong \mathbb R^n \\
\mathcal V = \text{vector space} \\
n = \text{dimension} \\
\end{aligned}
$$

---
### isomorphic preservation property

- vectors of matrix transformation kernel equal vectors of linear transformation kernel
- vectors of matrix transformation range equal vectors of linear transformation range
- dimension of matrix transformation kernel equal dimension of linear transformation kernel 
- dimension of matrix transformation range equal dimension of linear transformation range
---
### isomorphic preservation property formula

$$
\begin{aligned}
(L: \mathcal V \rightarrow \mathcal W) \land (L_1: \mathcal V \rightarrow \mathbb R^n) \land ([\vec w]_C = A_{BC}[\vec v]_B)\rightarrow L^{-1}_1(\ker \ A_{BC})= \ker(L) \subseteq \mathcal V \\
(L: \mathcal V \rightarrow \mathcal W) \land (L_2: \mathcal W \rightarrow \mathbb R^m) \land ([\vec w]_C = A_{BC}[\vec v]_B)\rightarrow L^{-1}_2(\text{range} \ A_{BC})= \text{range}(L) \subseteq \mathcal W \\
(L: \mathcal V \rightarrow \mathcal W) \land ([\vec w]_C = A_{BC}[\vec v]_B)\rightarrow \dim(\ker \ A_{BC}) = \dim(\ker  \ L) \\
(L: \mathcal V \rightarrow \mathcal W) \land ([\vec w]_C = A_{BC}[\vec v]_B)\rightarrow \dim(\text{range} \ A_{BC}) = \dim(\text{range} \ L) \\
\end{aligned}
$$

---
### summary

- one to one
- onto
- isomorphism
---
