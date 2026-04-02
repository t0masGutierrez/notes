###  action
- if known action of linear transformation on domain basis then known action on domain because every vector equal linear combination of its basis vectors

---
### action formula
$$
\begin{aligned}
(L: \mathcal V \rightarrow \mathcal W) \land (B = \vec b_{1}, \dots, \vec b_{n}) \implies L(c_{1}\vec b_{1} + \dots c_{n}\vec b_{n}) = \vec w \\
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
(L : \mathcal V \rightarrow \mathcal W) \land (B = \vec b_{1}, \dots, \vec b_{n}) \land (C = \vec c_{1}, \dots \vec c_{m}) \implies [\vec w]_{C} = A_{BC} [\vec v]_{B} \\
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
[\vec w]_{C}, [\vec v]_{B} = \text{coordinatization} \\
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
(L : \mathcal V \rightarrow \mathcal W) \land ([\vec v]_{D} = P_{BD}[\vec v]_{B}) \land ([\vec v]_{E} = Q_{CE}[\vec v]_{C}) \implies A_{DE} = Q_{CE}A_{BC}P_{BD}^{-1} \\
L = \text{linear transformation} \\
\mathcal V  = \text{domain} \\
\mathcal W  = \text{codomain} \\
B = \text{domain basis} \\
C = \text{codomain basis} \\
[\vec v]_{B}, [\vec v]_{C}, [\vec v]_{D}, [\vec v]_{E} = \text{coordinatization} \\
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
(L : \mathcal V \rightarrow \mathcal V) \land ([\vec v]_{D} = A_{DD}[\vec v]_{D}) \land ([\vec v]_{C} = A_{CC}[\vec v]_{C}) \land ([\vec v]_{C} = P_{DC}[\vec v]_{D}) \implies A_{CC} \sim A_{DD} \\
A_{CC} =  P_{DC}A_{DD} P_{DC}^{-1} \\
A_{DD} =  P_{DC}^{-1}A_{CC}P_{DC} \\
L = \text{linear transformation} \\
\mathcal V = \text{vector space} \\
[\vec v]_{C}, [\vec v]_{D} = \text{coordinatization} \\
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
(L_{1} : \mathcal V_{1} \rightarrow \mathcal V_{2}) \land (L_{2} : \mathcal V_{2} \rightarrow \mathcal V_{3}) \implies L_{2} \circ L_{1} : \mathcal V_{1} \rightarrow \mathcal V_{3} \\
([\vec v_{2}]_{C} = A_{BC}[\vec v_{1}]_{B}) \land ([\vec v_{3}]_{D} = A_{CD}[\vec v_{2}]_{C}) \implies A_{BD} = A_{CD}A_{BC} \\
L = \text{linear transformation} \\
\mathcal V = \text{vector space} \\
\vec v = \text{vector} \\
B = \text{basis} \\
[\vec v_{1}]_{B}, [\vec v_{2}]_{C}, [\vec v_{3}]_{D} = \text{coordinatization} \\
A = \text{matrix transformation}
\end{aligned}
$$

---
