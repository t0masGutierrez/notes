### 1x1 determinant

- linear transformation of the length of line

---
### 1x1 determinant formula

$$
\begin{aligned}
A = \begin{bmatrix} 
a_{11}
\end{bmatrix} \rightarrow 
|A| = a_{11} \\
A = \text{matrix} \\
a = \text{entry} \\
|A| = \text{determinant} 
\end{aligned}
$$

---
### 2x2 determinant

- linear transformation of the area of parallelogram

---
### 2x2 determinant formula

$$
\begin{aligned}
A = \begin{bmatrix} 
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{bmatrix} \rightarrow 
|A| = a_{11}a_{22} - a_{12}a_{21} \\
A = \text{matrix} \\
a = \text{entry} \\
|A| = \text{determinant} 
\end{aligned}
$$

---
### 3x3 determinant

- linear transformation of the volume of parallelepiped

---
### 3x3 determinant formula

$$
\begin{aligned}
A = \begin{bmatrix} 
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{bmatrix} \rightarrow 
|A| = a_{11}a_{22}a_{33} + a_{12}a_{23}a_{31} + a_{13}a_{21}a_{32} - a_{13}a_{22}a_{31} - a_{11}a_{23}a_{32} - a_{12}a_{21}a_{33} \\
A = \text{matrix} \\
a = \text{entry} \\
|A| = \text{determinant} 
\end{aligned}
$$

---
### nxn determinant

- linear transformation of the size of shape

---
### nxn determinant formula

$$
\begin{aligned}
|A| = \text{det}(A) \\
A = \text{matrix} \\
\end{aligned}
$$

---
### submatrix

- matrix formed by deleting all entries of the ith row and jth column 

---
### submatrix formula

$$
\begin{aligned}
A_{ij} = A - (a_{i*} + a_{*j}) \\
\forall n \ge 2: |A_{ij}| = (n - 1) \times (n - 1) \\
A = \text{matrix} \\
a_{i*} = \text{ith row} \\
a_{*j} = \text{jth column} \\
\end{aligned}
$$

---
### minor

- determinant of submatrix

---
### minor formula

$$
\begin{aligned}
|A_{ij}| = \text{det}(A_{ij}) \\
A_{ij} = \text{submatrix}
\end{aligned}
$$

---
### number of minors

- for every entry of matrix there exists minor

---
### number of minors formula

$$
\begin{aligned}
N = n^2 \\
n = \text{number of rows} \\
n = \text{number of columns}
\end{aligned}
$$

---
### cofactor

- minor multiplication with $\pm 1$ depending on the parity of exponent

---
### cofactor formula

$$
\begin{aligned}
\mathcal A_{ij} = (-1)^{i+j}|A_{ij}| \\
i = \text{row index} \\
j = \text{column index} \\
|A_{ij}| = \text{minor}
\end{aligned}
$$

---
### nxn determinant

- cofactor expansion along row or column of square matrix

---
### nxn determinant formula

$$
\begin{aligned}
|A| = a_{i1}\mathcal A_{i1} + a_{i2}\mathcal A_{i2} + \dots + a_{in}\mathcal A_{in} \\
|A| = a_{1j}\mathcal A_{1j} + a_{2j}\mathcal A_{2j} + \dots + a_{nj}\mathcal A_{nj} \\
\forall (1 \le i \le n) \\
\forall (1 \le j \le n) \\
A = \text{matrix} \\
a_{i*} = \text{ith row} \\
a_{*j} = \text{jth column} \\
\mathcal A = \text{cofactor} \\
n = \text{number of rows} \\
n = \text{number of columns}
\end{aligned}
$$

---
###  type I row operation on determinant

- determinant scaling

---
### type I row operation on determinant formula

$$
\begin{aligned}
|R_1(A)| = c|A| \\
R_1 = \text{type I row operation} \\
c = \text{scalar} \\
|A| = \text{determinant}
\end{aligned}
$$

---
### type II row operation on determinant

- determinant equality

---
### type II row operation on determinant formula

$$
\begin{aligned}
|R_2(A)| = |A| \\
R_2 = \text{type II row operation} \\
|A| = \text{determinant}
\end{aligned}
$$

---
### type III row operation on determinant

- determinant negation

---
### type III row operation on determinant formula

$$
\begin{aligned}
|R_3(A)| = -|A| \\
R_3 = \text{type III row operation} \\
|A| = \text{determinant}
\end{aligned}
$$

---
### upper triangular matrix determinant

- determinant of upper triangular matrix equal product of entries along the main diagonal

---
### upper triangular matrix determinant formula

$$
\begin{aligned}
A \in \mathcal U \rightarrow |A| = a_{11}a_{22} \dots a_{nn} \\
a = \text{entry}
\end{aligned}
$$

---
### determinant via gaussian elimination

- perform gaussian elimination until square matrix equal upper triangular matrix
- determinant of upper triangular matrix equal product of entries along the main diagonal
- determinant division with scalar

---
### determinant via gaussian elimination formula

$$
\begin{aligned}
B = R_k( \dots R_1(A)\dots ) \in \mathcal U \rightarrow |A| = \frac{1}{c}|B| \\
R = \text{row operation} \\
A = \text{matrix} \\
|A| = \text{determinant} \\
c = \text{scalar}
\end{aligned}
$$

---
### zero determinant

- zero row or zero column
- identical row or identical column

---
### singularity property

- nonsingular if and only if nonzero determinant

---
### singularity property formula

$$
\begin{aligned}
\text{det}(A) \ne 0 \leftrightarrow |A| \ne 0 \\
A = \text{matrix} \\
\end{aligned}
$$

---
### rank property

- rank equal size of square matrix if and only if nonzero determinant

---
### rank property formula

$$
\begin{aligned}
\text{rank}(A) = n \leftrightarrow |A| \ne 0 \\
A = \text{matrix} \\
n = \text{number of rows} \\
n = \text{number of columns}
\end{aligned}
$$

---
### singularity summary

- nonsingular
- rank equal size of square matrix
- nonzero determinant
- matrix row equivalent with identity matrix
- every solution equal trivial solution for homogeneous system
- there exists unique solution for heterogeneous system
---
### identity matrix determinant

- product of 1's along the main diagonal

---
### identity matrix determinant formula

$$
\begin{aligned}
|I| = 1
\end{aligned}
$$

---
### scalar multiplication determinant

- determinant of scalar quantity multiplication with square matrix

---
### scalar multiplication determinant formula

$$
\begin{align}
|cA| = c^n|A| \\
A = \text{matrix} \\
c = \text{scalar} \\
n = \text{number of rows} \\
n = \text{number of columns}
\end{align}
$$

---
### matrix multiplication determinant

- determinant multiplication with determinant

---
### matrix multiplication determinant formula

$$
\begin{aligned}
|AB| = (|A|)(|B|) \\
A, B = \text{matrix} \\
|A| = \text{determinant}
\end{aligned}
$$

---
### matrix inversion determinant

- reciprocal of determinant

---
### matrix inversion determinant formula

$$
\begin{aligned}
|A^{-1}| = \frac{1}{|A|} \\
|A| \ne 0 \\
A = \text{matrix} \\
|A| = \text{determinant}
\end{aligned}
$$

---
### matrix transposition determinant

- identity
- multiple identity
- transpositive

---
### matrix transposition determinant formula

$$
\begin{aligned}
|R(I)| = |(R(I))^T| \\
|R_k( \dots R_1(I)\dots )| = |(R_k( \dots R_1(I)\dots ))^T| \\
|R(B)| = |(R(B))^T| \\
\end{aligned}
$$

---
### symmetric determinant

- determinant of square matrix equal determinant of transposed square matrix

---
### symmetric determinant formula

$$
\begin{aligned}
|A| = |A^T| \\
A = \text{matrix} \\
T = \text{transposition}
\end{aligned}
$$

---
