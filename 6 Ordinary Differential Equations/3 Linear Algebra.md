### simultaneity property
- solution of nth order differential equation equal solutions of $n$ 1st order differential equations

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
### eigensolution 
- solution of system of differential equations

---
### eigensolution formula
$$
\begin{aligned}
\frac{d\vec x}{dt} = A\vec x \implies \vec x(t) = \exp(\lambda t) \vec v \\
\vec x = \text{eigensolution} \\
t = \text{independent variable} \\
A = \text{square matrix} \\
\lambda = \text{eigenvalue} \\
\vec v = \text{eigenvector}
\end{aligned}
$$

---
### complex eigenvalue 
- complex root of characteristic polynomial

---
### complex eigensolution formula
$$
\begin{aligned}
\lambda = \alpha + \beta i \implies \vec x(t) = e^{\alpha t}(\vec v_{1} \cos\beta t - \vec v_{2} \sin\beta t + i\vec v_{1} \cos\beta t + i\vec v_{2} \sin\beta t) \\
\lambda = \text{eigenvalue} \\
\alpha = \text{real part} \\
\beta = \text{imaginary part} \\
i = \sqrt {-1} \\
\vec x = \text{eigensolution} \\
t = \text{independent variable} \\
\vec v = \text{eigenvector}
\end{aligned}
$$

---
### repeated eigenvalue
- repeated root of characteristic polynomial

---
### repeated eigenvalue formula
$$
\begin{aligned}
(x - \lambda)^p\vec v \implies (\vec v = (A - \lambda I)^{p+k}) \land (\vec x_{k}(t) = e^{\lambda t} \sum_{j=0}^{k-1}\frac{t^j}{j!}\vec v_{k-j}) \\
1 < k \le p \\
x = \text{independent variable} \\
\lambda = \text{eigenvalue} \\
p = \text{power} \\
\vec v = \text{generalized eigenvector} \\
A = \text{square matrix} \\
I = \text{identity matrix} 
\end{aligned}
$$

---
### fundamental matrix solution
- matrix whose columns equal the linearly independent eigensolutions

---
### fundamental matrix solution formula
$$
\begin{aligned}
\phi(t) = \begin{bmatrix}
\vec x_{1} & \dots & \vec x_{n} \\
\vdots & \vdots & \vdots 
\end{bmatrix} \implies e^{At} = \phi(t)\phi^{-1}(0) \\
\phi(t) = \text{fundamental matrix solution}
\end{aligned}
$$

---
