### ordinary differential equation
- equation involving unknown function and its derivatives

---
### ordinary differential equation formula
$$
\begin{aligned}
f(t, y, \frac{dy}{dt}, \dots, \frac{d^ny}{dt^n}) = 0 \\
t = \text{independent variable} \\
y = \text{function} 
\end{aligned}
$$

---
### 1st order differential equation
- ordinary differential equation where the highest derivative equal 1

---
### 1st order differential equation formula
$$
\begin{aligned}
\frac{dy}{dt} = f(t, y) \\
t = \text{independent variable} \\
y = \text{solution} 
\end{aligned}
$$

---
### general solution of 1st order ode
- family of functions with arbitrary constants that satisfy the differential equation

---
### general solution of 1st order ode formula
$$
\begin{aligned}
y = \phi(t, C) \\
t = \text{independent variable} \\
C = \text{constant}
\end{aligned}
$$

---
### particular solution of 1st order ode
- single function with initial conditions that satisfy the differential equation

---
### particular solution of 1st order ode formula
$$
\begin{aligned}
y = \phi(t, t_{0}, y_{0}) \\
t = \text{independent variable} \\
t_{0}, y_{0} = \text{initial condition}
\end{aligned}
$$

---
### separable ode
- its possible to separate the variables on different sides of the equation

---
### separable ode formula
$$
\begin{aligned}
\frac{dy}{dt} = \frac{g(t)}{f(y)} \\
y = \text{solution} \\
t = \text{independent variable}
\end{aligned}
$$

---
### general solution of separable ode formula
$$
\begin{aligned}
\int f(y)dy = \int g(t) dt \\
y = \text{solution} \\
t = \text{independent variable}
\end{aligned}
$$

---
### particular solution of separable ode formula
$$
\begin{aligned}
\int_{y_{0}}^y f(r) dr = \int_{t_{0}}^t g(s)ds \\
y = \text{solution} \\
r, s = \text{dummy variable} \\
t = \text{independent variable} 
\end{aligned}
$$

---
### homogeneous ode
- RHS equal zero

---
### homogeneous ode formula
$$
\begin{aligned}
f(t, y, \frac{dy}{dt}) = 0 \\
t = \text{independent variable} \\
y = \text{solution} 
\end{aligned}
$$

---
### heterogeneous ode
- RHS equal nonzero

---
### heterogeneous ode formula
$$
\begin{aligned}
f(t, y, \frac{dy}{dt}) \ne 0 \\
t = \text{independent variable} \\
y = \text{solution} 
\end{aligned}
$$

---
### linear ode
- unknown function and its derivatives of degree 1
- unknown function and its derivatives are not products
- unknown function and its derivatives are not independent variables of nonlinear function
- unknown function is dependent variable of coefficients

---
### nonlinear ode
- unknown function and its derivatives of degree >1
- unknown function and its derivatives are products
- unknown function and its derivatives are independent variables of nonlinear function
- unknown function is independent variable of coefficients

---
### 1st order homogeneous linear ode formula
$$
\begin{aligned}
\frac{dy}{dt} + a(t)y(t) = 0 \\
y = \text{unknown function} \\
t = \text{independent variable} \\
a = \text{coefficient} \\
\end{aligned}
$$

---
### general solution of 1st order homogeneous linear ode formula
$$
\begin{aligned}
y(t) = C\exp(-\int a(t)dt) \\
C = \text{constant} \\
a = \text{coefficient} \\
t = \text{independent variable}
\end{aligned}
$$

---
### particular solution of 1st order homogeneous linear ode formula
$$
\begin{aligned}
y(t) = y(t_{0})\exp(-\int_{t_{0}}^t a(r)dr) \\
t_{0} = \text{initial condition} \\
t = \text{independent variable} \\
a = \text{coefficient} \\
r = \text{dummy variable}
\end{aligned}
$$

---
### integrating factor
- ode multiplication with integrating factor equal derivative of product

---
### integrating factor formula
$$
\begin{aligned}
\mu = \exp(\int a(t)dt) \implies \frac{d}{dt}[\mu y] = \mu(t)\frac{dy}{dt} + \mu(t)a(t)y(t) \\
\mu = \text{integrating factor} \\
t = \text{independent variable} \\
a = \text{coefficient} \\
y = \text{solution} 
\end{aligned}
$$

---
### 1st order heterogeneous linear ode formula
$$
\begin{aligned}
\frac{dy}{dt} + a(t)y(t) = b(t) \\
y = \text{unknown function} \\
t = \text{independent variable} \\
a = \text{coefficient} 
\end{aligned}
$$

---
### general solution of 1st order heterogeneous linear ode formula
$$
\begin{aligned}
y(t) = \frac{1}{\mu(t)}(C + \int \mu(t) b(t)dt) \\
\mu = \text{integrating factor} \\
t = \text{independent variable} \\
C = \text{constant} 
\end{aligned}
$$

---
### particular solution of 1st order heterogeneous linear ode formula
$$
\begin{aligned}
y(t) = \frac{1}{\mu(t)}[y(t_{0}) +\int_{t_{0}}^t \mu(r) b(r)dr] \\
\mu = \text{integrating factor} \\
t = \text{independent variable} \\
t_{0} = \text{initial condition} \\
r = \text{dummy variable} 
\end{aligned}
$$

---
### exact ode
- ode with equal partial derivatives

---
### exact ode formula
$$
\begin{aligned}
\frac{\partial M}{\partial y} = \frac{\partial N}{\partial t} \\
M(t, y)dt + N(t, y)dy = 0 
\end{aligned}
$$

---
### exact ode 1st method
- test exactness
- integrate $M(t, y)$ with respect to $t$
- integrate $N(t, y)$ with respect to $y$
- combine terms

---
### general solution of exact ode 1st method formula
$$
\begin{aligned}
\Phi(t, y) = \int M(t, y)dt + \int N(t, y)dy + C \\
M = \frac{\partial \Phi}{\partial t} \\
N = \frac{\partial \Phi}{\partial y} \\
\Phi = \text{potential function} \\
t = \text{independent variable} \\
y = \text{solution} \\
C = \text{constant} 
\end{aligned}
$$

---
### exact ode 2nd method
- test exactness
- potential function equal integral of $M(t, y)$ with respect to $t$ 
- differentiate potential function with respect to $y$ 
- derivative of potential function subtraction with $N(t, y)$ equal constant of integration
- integrate the derivative of the constant of integration
- equate potential function with constant of integration
- solve unknown function

---
### general solution of exact ode 2nd method formula
$$
\begin{aligned}
\Phi(t, y) = \int M(t, y)dt + \int \left(N(t, y) - \frac{\partial }{\partial y}\int M(t, y)dt \right) \\
M = \frac{\partial \Phi}{\partial t} \\
N = \frac{\partial \Phi}{\partial y} \\
\Phi = \text{potential function} \\
t = \text{independent variable} \\
y = \text{solution} \\
C = \text{constant} \\
\end{aligned}
$$

---
### exact ode integrating factor
- nonexact ode multiplication with integrating factor such that the partial derivatives equal therefore becoming integrable

---
### exact ode integrating factor formula
$$
\begin{aligned}
f(t) = \frac{\frac{\partial M}{\partial y} - \frac{\partial N}{\partial t}}{N} \implies \mu(t) = \exp(\int f(t)dt) \\
f(y) = \frac{\frac{\partial N}{\partial t} - \frac{\partial M}{\partial y}}{M} \implies \mu(y) = \exp(\int f(y)dy) \\
\end{aligned}
$$

---
### general solution of nonexact ode 1st method formula
$$
\begin{aligned}
\Phi(t, y) = \int \mu(t \lor y)M(t, y)dt + \int \mu(t \lor y)N(t, y)dy + C \\
M = \frac{\partial \Phi}{\partial t} \\
N = \frac{\partial \Phi}{\partial y} \\
\Phi = \text{potential function} \\
\mu = \text{integrating factor} \\
t = \text{independent variable} \\
y = \text{unknown function} \\
C = \text{constant} \\
\end{aligned}
$$

---
### general solution of nonexact ode 2nd method formula
$$
\begin{aligned}
\Phi(t, y) = \int \mu(t \lor y)M(t, y)dt + \int \left(N(t, y) - \frac{\partial }{\partial y}\int M(t, y)dt \right) \\
M = \frac{\partial \Phi}{\partial t} \\
N = \frac{\partial \Phi}{\partial y} \\
\Phi = \text{potential function} \\
\mu = \text{integrating factor} \\
t = \text{independent variable} \\
y = \text{unknown function} 
\end{aligned}
$$

---
