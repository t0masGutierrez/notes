### eigen

- characteristic of the transformation

---
### eigenvalue

- scalar quantity that describes the magnitude of scalar multiplication with the corresponding eigenvector during transformation

---
### eigenvalue formula

$$
\begin{aligned}
\lambda \iff \exists\vec x: A\vec x = \lambda \vec x \\
\vec x \ne 0 \\
\lambda = \text{eigenvalue} \\
\vec x = \text{eigenvector} \\
A = \text{square matrix}
\end{aligned}
$$

---
### eigenvector

- vector quantity along the direction unchanged by the transformation

---
### eigenvector formula

$$
\begin{aligned}
\vec x \iff A\vec x = \lambda \vec x \\
\vec x \ne 0 \\
\lambda = \text{eigenvalue} \\
\vec x = \text{eigenvector} \\
A = \text{matrix}
\end{aligned}
$$

---
### eigenspace

- set of all eigenvectors for square matrix associated with eigenvalue

---
### eigenspace formula

$$
\begin{aligned}
E_{\lambda} = \{\vec x \in \mathbb R^n| A \vec x = \lambda \vec x, A \in \mathcal M_n, \lambda \in \mathbb R\} \\
\vec x = \text{eigenvector} \\
A = \text{matrix} \\
\lambda = \text{eigenvalue}
\end{aligned}
$$

---
### number of eigenvectors

- infinite number of eigenvectors

---
### number of eigenvectors formula

$$
\begin{aligned}
c\vec x \in E_{\lambda} \\
c = \text{scalar} \\
\vec x = \text{eigenvector} \\
E_{\lambda} = \text{eigenspace}
\end{aligned}
$$

---
### homogeneous system of linear equations

- constant matrix equal zero matrix

---
### homogeneous system of linear equations formula

$$
\begin{aligned}
(A - \lambda I)\vec x = 0 \\
\lambda = \text{eigenvalue} \\
I = \text{identity matrix} \\
A = \text{matrix} 
\end{aligned}
$$

---
### homogeneous solution set

- eigenvectors for corresponding eigenvalue equal nontrivial solutions of the homogeneous system of linear equations
- eigenspace for corresponding eigenvectors equal complete solution set of the homogeneous system of linear equations

---
### singular coefficient property

- nontrivial eigenvector if and only if singular coefficient matrix

---
### singular coefficient property formula

$$
\begin{aligned}
\vec x \ne 0 \iff |A - \lambda I| = 0 \\
\vec x = \text{eigenvector} \\
\lambda = \text{eigenvalue} \\
I = \text{identity matrix} \\
A = \text{matrix}
\end{aligned}
$$

---
### characteristic polynomial

- polynomial whose real roots equal the eigenvalues of matrix

---
### characteristic polynomial formula

$$
\begin{aligned}
p_A(\lambda) = |A - \lambda I| = 0 \\
\lambda = \text{eigenvalue} \\
I = \text{identity matrix} \\
A = \text{matrix}
\end{aligned}
$$

---
### diagonalization

- compute characteristic polynomial
- substitute eigenvalues into coefficient matrix
- form the reduced row echelon of the system
- fundamental solutions of homogeneous system equal fundamental eigenvectors
- test diagonalizability
- form eigenmatrix whose column vectors equal fundamental eigenvectors
- compute inverse eigenmatrix
- matrix multiplication equal diagonal matrix
- all entries along main diagonal of diagonal matrix equal eigenvalue 

---
### diagonalization formula

$$
\begin{aligned}
D = P^{-1}AP \iff A = PDP^{-1} \\
|A| = n \times n \\
\text{det}(P) \ne 0 \\
P = \text{eigenmatrix} \\
A = \text{matrix} \\
D = \text{diagonal matrix} \\
P^{-1} = \text{inverse eigenmatrix} 
\end{aligned}
$$

---
### similarity

- similar matrices represent the same transformation but different coordinate system
- similar matrices have the same size
- similar matrices are similar with themselves
- similar matrices are commutative
- similar matrices are transitive
- similar matrices with identity matrix equal identity matrix
- similar matrices have equal determinant
- similar matrices have equal characteristic polynomial

---
### similarity formula

$$
\begin{aligned}
A \sim D \iff \exists P: D = P^{-1}AP \\
|A| = n \times n \\
\text{det}(P) \ne 0 \\
P = \text{eigenmatrix} \\
A = \text{matrix} \\
D = \text{diagonal matrix} \\
P^{-1} = \text{inverse eigenmatrix} 
\end{aligned}
$$

---
### matrix exponentiation property

- square matrix exponentiation similar diagonal matrix exponentiation

---
### matrix exponentiation property formula

$$
\begin{aligned}
A^k = PD^kP^{-1} \\
P = \text{eigenmatrix} \\
D = \text{diagonal matrix} \\
k = \text{positive integer} \\
P^{-1} = \text{inverse eigenmatrix}
\end{aligned}
$$

---
### algebraic multiplicity

- power of eigenvalue

---
### algebraic multiplicity formula

$$
\begin{aligned}
p_A(x) = (x - \lambda)^{k_0}(x - \lambda)^{k_1}\dots(x - \lambda)^{k_n} \\
\lambda = \text{eigenvalue} \\
k = \text{algebraic multiplicity}
\end{aligned}
$$

---
### geometric multiplicity

- number of fundamental eigenvectors

---
### geometric multiplicity formula

$$
\begin{aligned}
k = \sum \dim (E_{\lambda}) \\
E = \text{eigenspace}
\end{aligned}
$$

---
### diagonalizability 

- geometric multiplicity equal number of columns if and only if diagonalizable

---
### diagonalizability formula

$$
\begin{aligned}
k = n \iff \exists P \\
\text{det}(P) \ne 0 \\
k = \text{geometric multiplicity} \\
n = \text{number of rows} \\
n = \text{number of columns} \\
P = \text{eigenmatrix}
\end{aligned}
$$

---
