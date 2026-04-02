### ordered basis
- ordered n-tuple of vectors such that the set of vectors equal basis of vector space

---
### ordered basis formula
$$
\begin{aligned}
B = (\vec x_{1}, \dots \vec x_{n}) \\
\vec x = \text{vector}
\end{aligned}
$$

---
### coordinatization
- represent vector in terms of coefficients with respect to ordered basis of vector space

---
### coordinatization formula
$$
\begin{aligned}
[\vec w ]_{B} = [c_{1}, \dots, c_{k}] \implies \vec w = c_{1} \vec x_{1} + \dots + c_{n} \vec x_{n} \\
\vec w, \vec x = \text{vector} \\
B = \text{basis} \\
c = \text{coordinate}
\end{aligned}
$$

---
### terminology
- coordinatization equal vector expressed as B-coordinates

---
### standard basis property
- coordinatization with respect to standard basis equal vector

---
### standard basis property formula
$$
\begin{aligned}
[\vec v]_{S} = \vec v \\
\vec v = \text{vector} \\
S = \text{standard basis}
\end{aligned}
$$

---
### coordinatization via row reduction
- generate augmented matrix whose left columns equal vectors of ordered basis and right column equal possible vector
- form the reduced row echelon of the system
- if consistent system then coordinates equal solutions
- if inconsistent system then impossible coordinatization 

---
### coordinatization via row reduction formula
$$
\begin{aligned}
B| \vec v \implies I| [\vec v]_{B} \\
B = \text{basis} \\
\vec v = \text{vector} \\
I = \text{identity matrix} \\
[\vec v]_{B} = \text{coordinatization} 
\end{aligned}
$$

---
### coordinatization property
- vector addition
- scalar multiplication
- linearity

---
### coordinatization property formula
$$
\begin{aligned}
[\vec v_{1} + \vec v_{2}]_{B} = [\vec v_{1}]_{B} + [\vec v_{2}]_{B} \\
[c\vec v]_{B} = c[\vec v]_{B} \\
[c_{1}\vec v_{1} + \dots + c_{k}\vec v_{k}]_{B} = c_{1}[\vec v_{1}]_{B} + \dots + c_{k}[\vec v_{k}]_{B}
\end{aligned}
$$

---
### change of coordinates
- convert coordinates from 1st ordered basis to 2nd ordered basis

---
### transition matrix
- generate augmented matrix whose left columns equal vectors of 2nd ordered basis and right columns equal vectors of 1st ordered basis
- form the reduced row echelon of the system
- right matrix excluding zero rows equal transition matrix 
- jth column of transition matrix equal jth vector of B expressed as C-coordinates

---
### transition matrix formula
$$
\begin{aligned}
C|B \implies I | P_{BC} \\
C = \text{2nd basis} \\
B = \text{1st basis} \\
I = \text{identity matrix} \\
P = \text{transition matrix}
\end{aligned}
$$

---
### multiplicative transition matrix property
- transition matrix multiplication with vector of 1st basis equal vector of 2nd basis

---
### multiplicative transition matrix property formula
$$
\begin{aligned}
P_{BC} \iff (B, C \in \mathcal V) \land (\forall \vec v \in \mathcal V: [\vec v]_{C} = P_{BC}[\vec v]_{B}) \\
B, C = \text{basis} \\
\mathcal V = \text{vector space} \\
\vec v = \text{vector} \\
P = \text{transition matrix} \\
[\vec v]_{B}, [\vec v]_{C} = \text{coordinatization} \\
\end{aligned}
$$

---
### transitive transition matrix property
- $n$th transition matrix multiplication with ($n-1$)th transition matrix equal vector of nth basis

---
### transitive transition matrix property formula
$$
\begin{aligned}
(B, C, D \in \mathcal V) \land ([\vec v]_{C} = P_{BC}[\vec v]_{B}) \land ([\vec v]_{D} = Q_{CD}[\vec v]_{C}) \implies ([\vec v]_{D} = Q_{CD}P_{BC}[\vec v]_{B}) \\
B, C, D = \text{basis} \\
[\vec v]_{B}, [\vec v]_{C}, [\vec v]_{D} = \text{coordinatization} \\
\mathcal V = \text{vector space} \\
\vec v = \text{vector} \\
P, Q = \text{transition matrix}
\end{aligned}
$$

---
### inverse transition matrix property
- inverse transition matrix multiplication with vector of 2nd basis equal vector of 1st basis

---
### inverse transition matrix property formula
$$
\begin{aligned}
(B, C \in \mathcal V) \land ([\vec v]_{C} = P_{BC}[\vec v]_{B}) \implies (|P| \ne 0) \land ([\vec v]_{B} = P_{BC}^{-1}[\vec v]_{C}) \\
B, C = \text{basis} \\
\mathcal V = \text{vector space} \\
[\vec v]_{B}, [\vec v]_{C} = \text{coordinatization} \\
\vec v = \text{vector} \\
P = \text{transition matrix} \\
|P| = \text{number of elements} \\
P^{-1} = \text{inverse transition matrix} 
\end{aligned}
$$

---
### diagonalization transition matrix
- diagonalize matrix
- set of fundamental eigenvectors equal ordered basis
- eigenmatrix equal transition matrix from B-coordinates to S-coordinates

---
### diagonalization transition matrix formula
$$
\begin{aligned}
[\vec v]_{S} = P[\vec v]_{B} \\
D[\vec v]_{B} = [A\vec v]_{B} \\
\vec v = \text{vector} \\
S = \text{standard basis} \\
B = \text{basis} \\
[\vec v]_{S}, [\vec v]_{B} = \text{coordinatization} \\
P = \text{eigenmatrix} \\
D = \text{diagonal matrix} \\
A = \text{matrix}
\end{aligned}
$$

---
