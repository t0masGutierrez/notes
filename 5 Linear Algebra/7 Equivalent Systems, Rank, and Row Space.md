### system equivalent

- two systems of linear equations system equivalent if and only if they have the exact same solution set

---
### row equivalent

- two augmented matrices row equivalent if and only if they're equal by finite number of row operations

---
### existence and uniqueness

- there exists unique reduced row echelon form for every matrix
- same reduced row echelon form no matter the order of row operations

---
### inverse type I row operation

- row scaling

---
### inverse type I row operation formula

$$
\begin{aligned}
\langle i\rangle \implies (\frac{1}{c})\langle i\rangle  \\
i = \text{row index} \\
c = \text{scalar}
\end{aligned}
$$

---
### inverse type II row operation

- row replacement

---
### inverse type II row operation formula

$$
\begin{aligned}
\langle i\rangle \implies \langle i\rangle - c\langle j\rangle \\
i, j = \text{row index} \\
c = \text{scalar}
\end{aligned}
$$

---
### inverse type III row operation

- row swapping

---
### inverse type III row operation formula

$$
\begin{aligned}
\langle j \rangle \iff \langle i \rangle \\
i, j = \text{row index} \\
\end{aligned}
$$

---
### row equivalence property

- bidirectional
- transitive

---
### row equivalence property formula

$$
\begin{aligned}
C \sim D \implies D \sim C \\
(C \sim D) \land (D \sim E) \implies C \sim E
\end{aligned}
$$

---
### system equivalence property

- row equivalent system equal system equivalent system

---
### system equivalence property formula

$$
\begin{aligned}
C|D \sim A|B \implies CX = D \sim AX=B \\
A, C = \text{coefficient matrix} \\
D, B = \text{constant matrix} \\
X = \text{variable matrix}
\end{aligned}
$$

---
### RREF equality property

- row equivalent matrices share the same RREF

---
### RREF equality property formula

$$
\begin{aligned}
 A \sim B \iff \text{RREF}(A) = \text{RREF}(B) \\
 A, B = \text{matrix} \\
 \text{RREF} = \text{reduced row echelon form}
\end{aligned}
$$

---
### rank

- number of nonzero rows of RREF
- number of pivot columns of RREF

---
### rank property

- for the RREF if rank$(A)=n$ then every solution equal trivial solution
- for the RREF if rank$(A)<n$ then there exists nontrivial solution and therefore infinite solutions

---
### linear combination property

- if there exists consistent system of vector equations then there exists linear combination of $m$ vectors, each with $n$ coordinates
- number of coordinates must equal number of vectors

---
### linear combination property formula

$$
\begin{aligned}
\exists y \in \text{RREF}(A | \vec x) \implies \vec x \in \text{Row}(A) \\
y = \text{solution} \\
 \text{RREF} = \text{reduced row echelon form} \\
A = \text{coefficient matrix} \\
\vec x = \text{vector}
\end{aligned}
$$

---
### row space

- set of all possible linear combinations of the rows of matrix

---
### row space formula

$$
\begin{aligned}
\text{Row}(A) = \{\sum_{i=1}^m c_i\vec a_i | c \in \mathbb R, \vec a \in \mathbb R^n\} \\
m = \text{number of rows} \\
n = \text{number of columns} \\
c = \text{scalar} \\
\vec a = \text{row vector} 
\end{aligned}
$$

---
### row space equivalence property

- transitive
- equal

---
### row space equivalence property formula

$$
\begin{aligned}
(a \in \text{Row}P) \land (\forall p \in P: p \in \text{Row}Q) \implies a \in \text{Row}(Q) \\
A \sim B \implies \text{Row}(A) = \text{Row}(B)
\end{aligned}
$$

---
### zero vector property

- zero vector equal element of every row space

---
### zero vector property formula

$$
\begin{aligned}
\vec 0 = 0a_1 + \dots + 0a_m \\
a = \text{row} \\
m = \text{number of rows}
\end{aligned}
$$

---
### ith row vector property

- ith row vector equal element of every row space

---
### ith row vector property formula

$$
\begin{aligned}
\vec a_i = 0a_1 + \dots + 1a_i + \dots + 0a_m \\
a = \text{row} \\
i = \text{row index} \\
m = \text{number of rows} \\
\end{aligned}
$$

---
### row space test

- generate augmented matrix whose columns equal the vectors of set and whose constant matrix equal the possible element of row space
- form the reduced row echelon of the system
- if consistent system then element of row space
- if inconsistent system then not element of row space

---
