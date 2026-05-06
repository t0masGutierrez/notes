### simultaneity property
- solution of nth-order ode equal solution of system of $n$ 1st-order odes

---
### simultaneity property formula
$$
\begin{aligned}
a_{n}(t)\frac{d^ny}{dt^n} + a_{n-1}(t)\frac{d^{n-1}y}{dt^{n-1}} + \dots + a_0y = 0 \implies \begin{cases} \frac{dx_{1}}{dt} = x_{2} \\
\frac{dx_{2}}{dt} = x_{3} \\
\ \ \ \vdots \\
\frac{dx_{n-1}}{dt} = x_{n} \\
\frac{dx_{n}}{dt} = -(\frac{a_{n-1}(t)x_{n} + a_{n-2}(t)x_{n-1} + \dots + a_0x_{1}}{a_{n}(t)})
\end{cases} \\
x_{1}(t) = y \\
x_{2}(t) = \frac{dy}{dt} \\
\vdots \\
x_{n}(t) = \frac{d^{n-1}y}{dt^{n-1}}
\end{aligned}
$$

---
### linear system ode
- matrix equal system of $n$ 1st-order homogeneous linear constant coefficient odes

---
### linear system ode formula
$$
\begin{aligned}
\frac{d\vec x}{dt} = A\vec x(t) \\
\vec x = \text{solution} \\
t = \text{independent variable} \\
A = \text{coefficient matrix}
\end{aligned}
$$

---
### general solution of linear system ode
- eigensolution of matrix equal solution of linear system ode

---
### general solution of linear system ode formula
$$
\begin{aligned}
\frac{d\vec x}{dt} = A\vec x \implies \vec x(t) = \exp(\lambda t) \vec v \\
\vec x = \text{solution} \\
t = \text{independent variable} \\
A = \text{coefficient matrix} \\
\lambda = \text{eigenvalue} \\
\vec v = \text{eigenvector}
\end{aligned}
$$

---
### characteristic equation
- root of characteristic equation equal eigenvalue of matrix

---
### characteristic equation formula
$$
\begin{aligned}
\det(A - \lambda I) = 0 \\
A = \text{coefficient matrix} \\
\lambda = \text{eigenvalue} \\
I = \text{identity matrix}
\end{aligned}
$$

---
### distinct eigenvalues
- distinct roots of characteristic equation

---
### distinct eigenvalues formula
$$
\begin{aligned}
\vec x (t) = \sum_{i=1}^n C_ie^{\lambda_it} \vec v_{i} \\
\lambda = \text{eigenvalue} \\
t = \text{independent variable} \\
\vec v = \text{eigenvector}
\end{aligned}
$$

---
### complex eigenvalues
- complex roots of characteristic equation

---
### complex eigenvalues formula
$$
\begin{aligned}
\vec x(t) = C_1e^{\alpha t}(\vec p \cos\beta t - \vec q \sin\beta t) + C_2e^{\alpha t}(\vec p \sin\beta t + \vec q \cos\beta t) \\
\lambda = \alpha + \beta i \\
\vec v = \vec p + \vec q i \\
C = \text{constant} \\
\lambda = \text{eigenvalue} \\
\alpha, \vec p = \text{real part} \\
\beta, \vec q = \text{imaginary part} \\
t = \text{independent variable} \\
\vec v = \text{eigenvector}
\end{aligned}
$$

---
### defective matrix
- number of linearly independent eigenvectors lesser algebraic multiplicity of eigenvalue

---
### defective matrix formula
$$
\begin{aligned}
\dim \ker(A - \lambda I) < m \\
A = \text{coefficient matrix} \\
\lambda = \text{eigenvalue} \\
I = \text{identity matrix} \\
m = \text{algebraic multiplicity}
\end{aligned}
$$

---
### generalized eigenvector
- additional linearly independent eigenvector for defective matrix

---
### generalized eigenvector formula
$$
\begin{aligned}
(A - \lambda I) \vec v_{k} = \vec v_{k-1} \\
A = \text{coefficient matrix} \\
\lambda = \text{eigenvalue} \\
I = \text{identity matrix} \\
k = \text{generalized rank} \\
\vec w = \text{generalized eigenvector} \\
\vec v = \text{eigenvector}
\end{aligned}
$$

---
### repeated eigenvalues
- repeated roots of characteristic equation

---
### repeated eigenvalues formula
$$
\begin{aligned}
\vec x(t) = e^{\lambda t} \sum_{m=1}^k C_{m} \sum_{j=1}^{m} \frac{t^{m - j}}{(m - j)!}\vec v_{j} \\
\lambda = \text{eigenvalue} \\
t = \text{independent variable} \\
k = \text{number of generalized eigenvectors} \\
m = \text{generalized rank} \\
C = \text{constant} \\
\vec v = \text{generalized eigenvector} \\
A = \text{square matrix} \\
I = \text{identity matrix} 
\end{aligned}
$$

---
### matrix exponential
- general solution of linear system ode

---
### matrix exponential formula
$$
\begin{aligned}
e^{At} = \sum_{i=0}^n \frac{A^it^i}{i!} \implies \vec x(t) = e^{At}\vec x(0) \\
A = \text{coefficient matrix} \\
t = \text{independent variable} \\
\vec x = \text{solution}
\end{aligned}
$$

---
### fundamental matrix
- matrix whose columns form the fundamental set

---
### fundamental matrix formula
$$
\begin{aligned}
\Phi(t) = \begin{bmatrix} \vert & \vert & & \vert \\  
\vec{x}_{1}(t) & \vec{x}_{2}(t) & \cdots & \vec{x}_{n}(t) \\  
\vert & \vert & & \vert \end{bmatrix} \\
\vec x = \text{solution} \\
t = \text{independent variable} 
\end{aligned}
$$

---
### fundamental matrix property
- matrix whose columns equal the linearly independent eigensolutions

---
### fundamental matrix property formula
$$
\begin{aligned}
e^{At} = \Phi(t)\Phi^{-1}(0) \\
\Phi(t) = \text{fundamental matrix}
\end{aligned}
$$

---
