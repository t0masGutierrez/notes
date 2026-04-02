### multiplicative inverse
- square matrix multiplication with inverse matrix equal identity matrix

---
### multiplicative inverse formula
$$
\begin{aligned}
AA^{-1} = A^{-1}A = I \\
A = \text{matrix} \\
A^{-1} = \text{inverse matrix} \\
I = \text{identity matrix}
\end{aligned}
$$

---
### identity matrix
- diagonal matrix where all entries along main diagonal equal 1

---
### identity matrix formula
$$
\begin{aligned}
I = \begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1 
\end{bmatrix} \iff \forall (i \ne j): (a_{ij} = 0) \land \forall (i = j): (a_{ij} = 1) \\
i = \text{row index} \\
j = \text{column index}
\end{aligned}
$$

---
### nonsingular matrix
- invertible square matrix

---
### singular matrix
- noninvertible square matrix

---
### existence and uniqueness
- for every nonsingular matrix there exists unique inverse matrix

---
### existence and uniqueness formula
$$
\begin{aligned}
(AB=I) \land (AC=I) \implies B=C \\
A = \text{matrix} \\
B, C = \text{inverse matrix} \\
I = \text{identity matrix}
\end{aligned}
$$

---
### nonsingular matrix exponentiation property
- inverse
- inverse power
- multiplicative
- transpositive
- power
- multiplicative power
- additive power
- identity
- zero

---
### nonsingular matrix exponentiation property formula
$$
\begin{aligned}
(A^{-1})^{-1} = A \\
(A^{k})^{-1} = (A^{-1})^{k} = A^{-k} \\
(AB)^{-1} = B^{-1}A^{-1} \\
(A^T)^{-1} = (A^{-1})^{T} \\
A^k = (A^{k-1})(A) \\  
(A^s)^t = A^{st} = (A^t)^s \\  
 A^sA^t = A^{s+t} \\  
A^1 = A \\  
A^0 = I
\end{aligned}
$$

---
### 2x2 matrix inversion
- square matrix of size two multiplication with inverse matrix equal identity matrix

---
### 2x2 matrix inversion formula
$$
\begin{aligned}
A^{-1} = \begin{bmatrix} a & b \\ c & d \end{bmatrix}^{-1} = \frac{1}{\delta}\begin{bmatrix} d & -b \\ -c & a \end{bmatrix} \\
\delta = ad - bc \ne 0
\end{aligned}
$$

---
### nxn matrix inversion
- form the $n\times 2n$ augmented matrix whose left columns equal square matrix and right columns equal identity matrix
- convert augmented matrix into reduced row echelon form
- if left columns equal identity matrix then nonsingular matrix and right columns equal inverse matrix
- if left columns not equal identity matrix then singular matrix

---
### nxn matrix inversion formula
$$
\begin{aligned}
A|I \implies I|A^{-1} \\
A = \text{matrix} \\
I = \text{identity matrix} \\
A^{-1} = \text{inverse matrix}
\end{aligned}
$$

---
### nonsingular matrix property
- nonsingular matrix if and only if rank equal number of columns

---
### nonsingular matrix property formula
$$
\begin{aligned}
\exists A^{-1} \iff \text{rank}(A)= n \\
A^{-1} = \text{inverse matrix} \\
A = \text{matrix} \\
n = \text{number of columns}
\end{aligned}
$$

---
### coefficient matrix inversion
- if nonsingular coefficient matrix then single solution equal $A^{-1}B$ 
- if singular coefficient matrix then either zero solutions or infinite solutions
- unique solution if and only if coefficient matrix equal nonsingular matrix

---
