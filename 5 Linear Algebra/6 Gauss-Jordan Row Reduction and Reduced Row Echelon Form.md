### gauss-jordan row reduction
- gaussian elimination and all entries above pivot entry equal zero

---
### reduced row echelon form
- first nonzero entry of each row equal 1
- first nonzero entry of each successive row equal larger column index
- all entries below first nonzero entry of each row equal 0
- all entries above first nonzero entry of each row equal 0
- rows with all zeros are the final rows of matrix

---
### homogeneous system of linear equations
- constant matrix equal zero matrix

---
### homogeneous system of linear equations formula
$$
\begin{aligned}
AX = 0 \\
A = \text{cofficient matrix} \\
X = \text{variable matrix} \\
0 = \text{constant matrix}
\end{aligned}
$$

---
### homogeneous solution set
- if every column equal pivot column then every solution equal trivial solution
- if there exists nonpivot column then there exists nontrivial solution

---
### heterogeneous system of linear equations
- constant matrix equal nonzero matrix

---
### heterogeneous system of linear equations formula
$$
\begin{aligned}
AX \ne 0 \\
A = \text{cofficient matrix} \\
X = \text{variable matrix} \\
0 = \text{constant matrix}
\end{aligned}
$$

---
### heterogeneous solution set
- if there exists pivot entry for every column then single solution
- if there exists row with all zeros except final entry then zero solutions
- if there exists nonpivot column then infinite solutions

---
### trivial solution
- every solution equal zero

---
### nontrivial solution
- there exists nonzero solution

---
### fundamental solution of system of linear equations
- single independent variable equal 1 and remaining variables equal 0
- number of independent variables equal number of fundamental solutions

---
### fundamental solution set
- set of linearly independent n-vectors such that every solution of system of linear equations expressible as linear combination of these n-vectors

---
### fundamental solution set formula
$$
\begin{aligned}
\{\sum_{i}^k c_{i}\vec x_{i} | c \in \mathbb R, \vec x \in \mathbb R^n\} \\
i = \text{independent variable index} \\
k = \text{number of independent variables} \\
c = \text{scalar} \\
\vec x = \text{vector}
\end{aligned}
$$

---
### simultaneous matrix
- combine augmented matrices with same coefficient matrices but different constant matrices 

---
### simultaneous matrix formula
$$
\begin{aligned}
A | B | B' = \left[\begin{array}{cccc|c|c}
a_{11} & a_{12} & \cdots & a_{1n} & b_{1} & b_{1}' \\
a_{21} & a_{22} & \cdots & a_{2n} & b_{2} & b_{2}' \\
\vdots & \vdots & \ddots & \vdots & \vdots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn} & b_{m} & b_{m}'
\end{array}\right]
\end{aligned}
$$

---
### size property
- for collection of $m$ linear equations, each with linear combination of the same $n$ variables, if $m = n$ then every solution equal trivial solution
- for collection of $m$ linear equations, each with linear combination of the same $n$ variables, if $m < n$ then there exists nontrivial solution and therefore infinite solutions

---
