### 2nd order differential equation

- equation involving derivatives of unknown function and the highest derivative of the unknown function equal two

---
### 2nd order differential equation formula

$$
\begin{aligned}
\frac{d^2y}{dt^2} = f(t, y, \frac{dy}{dt}) \\
t = \text{independent variable} \\
y = \text{unknown function}
\end{aligned}
$$

---
### 2nd order homogeneous linear differential equation formula

$$
\begin{aligned}
y''(t) + p(t)y'(t) + q(t)y(t) = 0 \\
p = \text{coefficient} \\
q = \text{coefficient} \\
y = \text{unknown function} \\
t = \text{independent variable} 
\end{aligned}
$$

---
### general solution of 2nd order homogeneous linear differential equation formula

$$
\begin{aligned}
y = c_1y_1 + c_2y_2 \\
c = \text{constant} \\
y_1 = \text{solution} \\
y_2 = \text{solution} 
\end{aligned}
$$

---
### existence and uniqueness

- there exists unique particular solution of 2nd order homogeneous linear differential equation on the interval where coefficient continuous

---
### existence and uniqueness formula

$$
\begin{aligned}
y'(t_0) = y_1 \\
y(t_0) = y_0 
\end{aligned}
$$

---
### wronskian

- nonzero wronskian equal linear independence

---
### wronskian formula

$$
\begin{aligned}
W[y_1, y_2](t) = \begin{vmatrix} y_1(t) & y_2(t) \\ y_1’(t) & y_2’(t) \end{vmatrix} = y_1(t)y_2’(t) - y_2(t)y_1’(t) \\
y_1 = \text{solution} \\
y_2 = \text{solution} \\
t = \text{independent variable}
\end{aligned}
$$

---
### linear transformation

- function of vector space thats closed under vector addition and scalar multiplication

---
### linear transformation formula

$$
\begin{aligned}
L[y](t) = y''(t) + p(t)y'(t) + q(t)y(t) \\
p = \text{coefficient} \\
q = \text{coefficient} \\
y = \text{unknown function} \\
t = \text{independent variable} 
\end{aligned}
$$

---
### linear operator property

- scalar multiplication
- vector addition

---
### linear operator property formula

$$
\begin{aligned}
L[cy] = cL[y] \\
L[y_1 + y_2] = L[y_1] + L[y_2]
\end{aligned}
$$

---
### constant coefficient equation

- coefficient of 2nd order homogeneous linear differential equation equal real number

---
### constant coefficient equation formula

$$
\begin{aligned}
ay''(t) + by'(t) + cy(t) = 0 \\
a, b, c = \text{constant} \\
y = \text{unknown function} \\
t = \text{independent variable} 
\end{aligned}
$$

---
### general solution of constant coefficient equation formula

$$
\begin{aligned}
ar^2\exp(rt) + br\exp(rt) + c\exp(rt) = 0
\begin{cases}
y'' = r^2\exp(rt) \\
y' = r\exp(rt) \\
y = \exp(rt) \\
\end{cases} \\
\exp(rt) = \text{guess} \\
a, b, c = \text{constant} \\
r = \text{root}
\end{aligned}
$$

---
### characteristic polynomial

- substitute differential with guess

---
### characteristic polynomial formula

$$
\begin{aligned}
ar^2 + br + c = 0
\end{aligned}
$$

---
### general solution of characteristic polynomial

- quadratic formula equal roots of characteristic polynomial

---
### general solution of characteristic polynomial formula

$$
\begin{aligned}
r = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} \\
a, b, c = \text{constant}
\end{aligned}
$$

---
### distinct real roots

- positive discriminant 

---
### distinct real roots formula

$$
\begin{aligned}
y = c_1\exp(r_1t) + c_2\exp(r_2t) \\
c = \text{constant} \\
r = \text{root} \\
t = \text{independent variable}
\end{aligned}
$$

---
### repeated real roots

- zero discriminant

---
### repeated real roots formula

$$
\begin{aligned}
y = \exp(rt)(c_1 + c_2t) \\
c = \text{constant} \\
r = \text{root} \\
t = \text{independent variable}
\end{aligned}
$$

---
### complex roots

- negative discriminant 

---
### complex roots formula

$$
\begin{aligned}
y = \exp(\alpha t)(c_1\cos\beta t + c_2\sin \beta t) \\
r = \text{root} \\
c = \text{constant} \\
\alpha = \text{real part} \\
\beta = \text{imaginary part} \\
t = \text{independent variable}
\end{aligned}
$$

---
### undetermined coefficients

- method of solving the general solution of heterogeneous linear constant coefficient differential equation

---
### undetermined coefficients formula

$$
\begin{aligned}
b(t) = \exp(ct) \implies y_p = A\exp(ct) \\
b(t) = \sin ct \lor \cos ct \implies y_p = A_0\cos(ct) + A_1\sin(ct) \\
b(t) = P_n(t) \implies y_p = A_0 + A_1t + \dots + A_nt^n \\
\end{aligned}
$$

---
### calculate judicious guessing

- solve the homogeneous solution of heterogeneous linear constant coefficient differential equation
- judiciously guess the unknown function of particular solution
- if guess equal homogeneous solution then guess multiplication with independent variable until guess not equal homogeneous solution
- substitute guess and its derivatives into the differential equation
- general solution equal homogeneous solution addition with particular solution

---
### variation of parameters

- method of solving the general solution of heterogeneous linear constant coefficient differential equation

---
### variation of parameters formula

$$
\begin{aligned}
y_p = u_1y_1 + u_2y_2 \\
u_1 = -\int\frac{b(t)y_2(t)}{W[y_1, y_2]} \\
u_2 = \int\frac{b(t)y_1(t)}{W[y_1, y_2]} \\
u = \text{coefficient} \\
b(t) \ne 0 \\
y_1 = \text{solution} \\
y_2 = \text{solution} \\
W = \text{wronskian} 
\end{aligned}
$$

---
### calculate variation of parameters

- solve the homogeneous solution of 2nd order heterogeneous linear constant coefficient differential equation
- replace constant coefficients with variable coefficients
- solve the variable coefficients
- substitute variable coefficients into the particular solution
- general solution equal homogeneous solution addition with particular solution

---
### series solution

- method of solving the general solution of heterogeneous linear variable coefficient differential equation

---
### series solution formula

$$
\begin{aligned}
y = \sum_{n=0}^\infty a_n(x−x_0)^n \\
y' = \sum_{n=1}^\infty a_nn(x−x_0)^{n-1} \\
y'' = \sum_{n=1}^\infty a_nn(n-1)(x−x_0)^{n-2}
\end{aligned}
$$

---
### calculate series solution

- compute derivatives as power series
- substitute derivatives into differential equation
- reindex such that all powers of $x$ equal
- reindex all coefficients
- equate all coefficients with zero
- solve for the recurrence relation

---
