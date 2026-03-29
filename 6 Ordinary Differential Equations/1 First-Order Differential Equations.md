### 1st order differential equation

- equation involving derivatives of unknown function and the highest derivative of the unknown function equal 1

---
### 1st order differential equation formula

$$
\begin{aligned}
\frac{dy}{dt} = f(t, y) \\
t = \text{independent variable} \\
y = \text{unknown function} 
\end{aligned}
$$

---
### general solution of differential equation

- family of functions with arbitrary constants that satisfy the differential equation

---
### particular solution of differential equation

- single function with initial conditions that satisfy the differential equation

---
### separable equation

- its possible to separate the variables

---
### separable equation formula

$$
\begin{aligned}
\frac{dy}{dt} = \frac{g(t)}{f(y)}
\end{aligned}
$$

---
### general solution of separable equation formula

$$
\begin{aligned}
\int f(y)dy = \int g(t) dt \\
t = \text{independent variable}
\end{aligned}
$$

---
### particular solution of separable equation formula

$$
\begin{aligned}
\int_{y_0}^y f(r) dr = \int_{t_0}^t g(s)ds \\
y = \text{unknown function} \\
r = \text{dummy variable} \\
t = \text{independent variable} \\
s = \text{dummy variable} \\
\end{aligned}
$$

---
### homogeneous

- RHS equal zero

---
### heterogeneous 

- RHS equal nonzero

---
### linear differential equation

- unknown function and its derivatives of order 1
- unknown function and its derivatives are not products
- unknown function and its derivatives are not independent variables of nonlinear function
- unknown function not independent variable of coefficients

---
### nonlinear differential equation

- unknown function and its derivatives of order >1
- unknown function and its derivatives are products
- unknown function and its derivatives are independent variables of nonlinear function
- unknown function independent variable of coefficients

---
### 1st order homogeneous linear differential equation formula

$$
\begin{aligned}
\frac{dy}{dt} + a(t)y(t) = 0 \\
y = \text{unknown function} \\
t = \text{independent variable} \\
a = \text{coefficient} \\
\end{aligned}
$$

---
### general solution of 1st order homogeneous linear differential equation formula

$$
\begin{aligned}
y(t) = c\exp(-\int a(t)dt) \\
c = \text{constant} \\
a = \text{coefficient} \\
t = \text{independent variable}
\end{aligned}
$$

---
### particular solution of 1st order homogeneous linear differential equation formula

$$
\begin{aligned}
y(t) = y(t_0)\exp(-\int_{t_0}^t a(r)dr) \\
t = \text{independent variable} \\
a = \text{coefficient} \\
r = \text{dummy variable}
\end{aligned}
$$

---
### integrating factor

- multiplication with 1st order heterogeneous linear differential equation such that the LHS equal the derivative of product therefore becoming integrable

---
### integrating factor formula

$$
\begin{aligned}
\frac{d\mu}{dt} = \mu(t)a(t) \\
\frac{d\mu}{\mu} = a(t)dt \\
\ln(\mu) = \int a(t)dt \\
\mu = \exp(\int a(t)dt) \\
\mu(t)\frac{dy}{dt} + \mu(t)a(t)y(t) \\
\mu(t)\frac{dy}{dt} + \frac{d\mu}{dt}y(t)
\end{aligned}
$$

---
### 1st order heterogeneous linear differential equation formula

$$
\begin{aligned}
\frac{dy}{dt} + a(t)y(t) = b(t) \\
y = \text{unknown function} \\
t = \text{independent variable} \\
a = \text{coefficient} \\
b \ne 0
\end{aligned}
$$

---
### general solution of 1st order heterogeneous linear differential equation formula

$$
\begin{aligned}
y(t) = \frac{1}{\mu(t)}(\int \mu(t) b(t)dt+c) = \exp(-\int a(t)dt)(\int \mu(t) b(t)dt+c) \\
\mu = \text{integrating factor} \\
t = \text{independent variable} \\
b \ne 0 \\
c = \text{constant} \\
a = \text{coefficient}
\end{aligned}
$$

---
### particular solution of 1st order heterogeneous linear differential equation formula

$$
\begin{aligned}
y(t) = \frac{1}{\mu(t)}[\mu(t_0)y(t_0) +\int_{t_0}^t \mu(r) b(r)dr] = \exp(-\int a(t)dt)[\mu(t_0)y(t_0)+\int_{t_0}^t \mu(r) b(r)dr] \\
\mu = \text{integrating factor} \\
t = \text{independent variable} \\
r = \text{dummy variable} \\
b \ne 0 \\
a = \text{coefficient}
\end{aligned}
$$

---
### exact equation

- equal partial derivatives

---
### exact equation formula

$$
\begin{aligned}
M(t, y)dt + N(t, y)dy = 0 \\
\frac{\partial M}{\partial y} = \frac{\partial N}{\partial t}
\end{aligned}
$$

---
### exact equation 1st method

- test exactness
- integrate $M(t, y)$ with respect to $t$
- integrate $N(t, y)$ with respect to $y$
- combine terms

---
### general solution of exact equation 1st method formula

$$
\begin{aligned}
\phi(t, y) = \int M(t, y)dt + \int N(t, y)dy + c \\
M = \frac{\partial \phi}{\partial t} \\
N = \frac{\partial \phi}{\partial y} \\
\phi = \text{potential function} \\
t = \text{independent variable} \\
y = \text{unknown function} \\
c = \text{constant} \\
\end{aligned}
$$

---
### exact equation 2nd method

- test exactness
- potential function equal integral of $M(t, y)$ with respect to $t$ 
- differentiate potential function with respect to $y$ 
- derivative of potential function subtraction with $N(t, y)$ equal constant of integration
- integrate the derivative of the constant of integration
- equate potential function with constant of integration
- solve in terms of unknown function

---
### general solution of exact equation 2nd method formula

$$
\begin{aligned}
\phi(t, y) = \int M(t, y)dt + \int \left(N(t, y) - \frac{\partial }{\partial y}\int M(t, y)dt \right) \\
M = \frac{\partial \phi}{\partial t} \\
N = \frac{\partial \phi}{\partial y} \\
\phi = \text{potential function} \\
t = \text{independent variable} \\
y = \text{unknown function} \\
c = \text{constant} \\
\end{aligned}
$$

---
### exact equation integrating factor

- multiplication with nonexact equation such that the partial derivatives equal therefore becoming integrable

---
### exact equation integrating factor formula

$$
\begin{aligned}
f(t) = \frac{\frac{\partial M}{\partial y} - \frac{\partial N}{\partial t}}{N} \implies \mu(t) = \exp(\int f(t)dt) \\
f(y) = \frac{\frac{\partial N}{\partial t} - \frac{\partial M}{\partial y}}{M} \implies \mu(y) = \exp(\int f(y)dy) \\
\end{aligned}
$$

---
### general solution of nonexact equation 1st method formula

$$
\begin{aligned}
\phi(t, y) = \int \mu(t \lor y)M(t, y)dt + \int \mu(t \lor y)N(t, y)dy + c \\
M = \frac{\partial \phi}{\partial t} \\
N = \frac{\partial \phi}{\partial y} \\
\phi = \text{potential function} \\
\mu(t \lor y) = \text{integrating factor} \\
t = \text{independent variable} \\
y = \text{unknown function} \\
c = \text{constant} \\
\end{aligned}
$$

---
### general solution of nonexact equation 2nd method formula

$$
\begin{aligned}
\phi(t, y) = \int \mu(t \lor y)M(t, y)dt + \int \left(N(t, y) - \frac{\partial }{\partial y}\int M(t, y)dt \right) \\
M = \frac{\partial \phi}{\partial t} \\
N = \frac{\partial \phi}{\partial y} \\
\phi = \text{potential function} \\
\mu(t \lor y) = \text{integrating factor} \\
t = \text{independent variable} \\
y = \text{unknown function} \\
c = \text{constant} \\
\end{aligned}
$$

---
