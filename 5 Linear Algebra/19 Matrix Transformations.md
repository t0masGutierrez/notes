###  action

- if known action of linear transformation on domain basis then known action on domain because every vector equal linear combination of its basis vectors

---
### action formula

$$
\begin{aligned}
(L: \mathcal V \rightarrow \mathcal W) \land (B = \vec b_1, \dots, \vec b_n) \implies L(c_1\vec b_1 + \dots c_n\vec b_n) = \vec w \\
L = \text{linear transformation} \\
\mathcal V = \text{domain vector space} \\
\mathcal W = \text{codomain vector space} \\
B =\text{basis} \\
\vec b = \text{basis vector} \\
\vec w = \text{image vector} \\
c =\text{coordinate}
\end{aligned}
$$

---
### matrix transformation

- image as C-coordinates equal matrix multiplication with preimage as B-coordinates
- jth column of matrix transformation equal jth basis image vector expressed as C-coordinates

---
### matrix transformation formula

$$
\begin{aligned}
(L : \mathcal V \rightarrow \mathcal W) \land (B = \vec b_1, \dots, \vec b_n) \land (C = \vec c_1, \dots \vec c_m) \implies [\vec w]_C = A_{BC} [\vec v]_B \\
\dim (\mathcal V) = n \\
\dim (\mathcal W) = m \\
|A_{BC}| = m \times n \\
L = \text{linear transformation} \\
\mathcal V  = \text{domain vector space} \\
\mathcal W  = \text{codomain vector space} \\
B = \text{domain basis} \\
C = \text{codomain basis} \\
\vec b = \text{domain basis vector} \\
\vec c = \text{codomain basis vector} \\
\vec v = \text{preimage vector} \\
\vec w = \text{image vector} \\
[\vec w]_C, [\vec v]_B = \text{coordinatization} \\
A = \text{matrix transformation} 
\end{aligned}
$$

---
### terminology

- matrix $A_{BC}$ equal matrix $A$ of the linear transformation $L$ with respect to the domain basis $B$ and codomain basis $C$ 

---
### transitive matrix transformation property

- matrix transformation with change of coordinates

---
### transitive matrix transformation property formula

$$
\begin{aligned}
(L : \mathcal V \rightarrow \mathcal W) \land ([\vec v]_D = P_{BD}[\vec v]_B) \land ([\vec v]_E = Q_{CE}[\vec v]_C) \implies A_{DE} = Q_{CE}A_{BC}P_{BD}^{-1} \\
L = \text{linear transformation} \\
\mathcal V  = \text{domain} \\
\mathcal W  = \text{codomain} \\
B = \text{domain basis} \\
C = \text{codomain basis} \\
[\vec v]_B, [\vec v]_C, [\vec v]_D, [\vec v]_E = \text{coordinatization} \\
\vec v = \text{preimage vector} \\
P = \text{domain transition matrix} \\
Q = \text{codomain transition matrix} \\
A = \text{matrix transformation} 
\end{aligned}
$$

---
### linear operator similarity property

- linear operation on matrix respect to different bases equal similar matrices

---
### linear operator similarity property formula

$$
\begin{aligned}
(L : \mathcal V \rightarrow \mathcal V) \land ([\vec v]_D = A_{DD}[\vec v]_D) \land ([\vec v]_C = A_{CC}[\vec v]_C) \land ([\vec v]_C = P_{DC}[\vec v]_D) \implies A_{CC} \sim A_{DD} \\
A_{CC} =  P_{DC}A_{DD} P_{DC}^{-1} \\
A_{DD} =  P_{DC}^{-1}A_{CC}P_{DC} \\
L = \text{linear transformation} \\
\mathcal V = \text{vector space} \\
[\vec v]_C, [\vec v]_D = \text{coordinatization} \\
\vec v = \text{vector} \\
C, D = \text{basis} \\
P = \text{transition matrix} 
\end{aligned}
$$

---
### composite matrix transformation property

- composition of matrix transformation equal matrix transformation

---
### composite matrix transformation property formula

$$
\begin{aligned}
(L_1 : \mathcal V_1 \rightarrow \mathcal V_2) \land (L_2 : \mathcal V_2 \rightarrow \mathcal V_3) \implies L_2 \circ L_1 : \mathcal V_1 \rightarrow \mathcal V_3 \\
([\vec v_2]_C = A_{BC}[\vec v_1]_B) \land ([\vec v_3]_D = A_{CD}[\vec v_2]_C) \implies A_{BD} = A_{CD}A_{BC} \\
L = \text{linear transformation} \\
\mathcal V = \text{vector space} \\
\vec v = \text{vector} \\
B = \text{basis} \\
[\vec v_1]_B, [\vec v_2]_C, [\vec v_3]_D = \text{coordinatization} \\
A = \text{matrix transformation}
\end{aligned}
$$

---
