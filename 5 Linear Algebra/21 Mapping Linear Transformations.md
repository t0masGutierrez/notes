### injective linear transformation

- every element of domain map to 1 element of codomain
- one to one

---
### injective linear transformation formula

$$
\begin{aligned}
(L: \mathcal V \rightarrow \mathcal W) \leftrightarrow \forall \vec v_1, \vec v_2 \in \mathcal V: L(\vec v_1) = L(\vec v_2) \rightarrow \vec v_1 = \vec v_2 \\
L = \text{injective linear transformation} \\
\mathcal V = \text{domain vector space} \\
\mathcal W = \text{codomain vector space} \\
\vec v = \text{vector} 
\end{aligned}
$$

---
### surjective linear transformation

- every element of codomain map to $\ge1$ element of domain
- onto

---
### surjective linear transformation formula

$$
\begin{aligned}
(L: \mathcal V \rightarrow \mathcal W) \leftrightarrow \forall \vec w \in \mathcal W, \exists \vec v \in \mathcal V: L(\vec v) = \vec w \\
L = \text{surjective linear transformation} \\
\mathcal V = \text{domain vector space} \\
\mathcal W = \text{codomain vector space} \\
\vec v = \text{preimage vector} \\
\vec w = \text{image vector} 
\end{aligned}
$$

---
### dimension property

- dimension of injective kernel equal dimension of zero
- dimension of surjective range equal dimension of codomain

---
### dimension property formula

$$
\begin{aligned}
L = \text{injection} \leftrightarrow (\text{ker}(L) = \{\vec 0_{\mathcal V}\}) \lor (\text{dim(ker} \ L) = 0) \\
L = \text{surjection} \leftrightarrow (\text{range}(L) = \mathcal W) \lor (\text{dim(range} \ L) = \dim(\mathcal W) \ne \infty) \\
\end{aligned}
$$

---
### bijection property

- vector space with equal dimension must satisfy bijection

---
### bijection property formula

$$
\begin{aligned}
(L: \mathcal V \rightarrow \mathcal W) \land (\dim(\mathcal V) = \dim(\mathcal W) \ne \infty) \rightarrow L = \text{injection} \leftrightarrow L = \text{surjection} \\
L = \text{linear transformation} \\
\mathcal V = \text{domain vector space} \\
\mathcal W = \text{codomain vector space}
\end{aligned}
$$

---
### spanning independence property

- independent injective preimage equal independent image
- spanning surjective preimage equal spanning image

---
### spanning independence property

$$
\begin{aligned}
(L = \text{injection}) \land (\text{rank}(T \subseteq \mathcal V) = n) \rightarrow \text{rank}(L(T) \subseteq \mathcal W) = n \\
(L = \text{surjection}) \land (\text{span}(S \subseteq \mathcal V) = \mathcal V) \rightarrow \text{span}(L(S) \subseteq \mathcal W) = \mathcal W \\
\end{aligned}
$$

---
