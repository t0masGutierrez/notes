### perturbed equation

- equation containing small nonnegative parameter 

---
### perturbed equation formula

$$
\begin{aligned}
f(t, x, \epsilon) \\
0 \le \epsilon \ll 1 \\
f = \text{perturbed equation} \\
t = \text{time} \\
x = \text{solution} \\
\epsilon = \text{parameter}
\end{aligned}
$$

---
### algebraic equation

- equation involving functions of unknown solution

---
### algebraic equation formula

$$
\begin{aligned}
y = f(t, x, \epsilon) \\
f = \text{perturbed equation} \\
t = \text{time} \\
x = \text{solution} \\
\epsilon = \text{parameter}
\end{aligned}
$$

---
### differential equation

- equation involving derivatives of unknown solution

---
### differential equation formula

$$
\begin{aligned}
\frac{dx}{dt} = f(t, x, \epsilon) \\
x(t=0) = x_0 \\
t \ge 0 \\
f = \text{perturbed equation} \\
t = \text{time} \\
x = \text{solution} \\
\epsilon = \text{parameter}
\end{aligned}
$$

---
### regular

- every solution of perturbed equation with positive parameter equal solution of perturbed equation with zero parameter

---
### regular formula

$$
\begin{aligned}
\# f(t, x, \epsilon) = k, \epsilon > 0 \land \# f(t, x, \epsilon) = k, \epsilon = 0 \\
f = \text{perturbed equation} \\
t = \text{time} \\
x = \text{solution} \\
\epsilon = \text{parameter} \\
k = \text{number of solutions} 
\end{aligned}
$$

---
### singular

- there exists solution of perturbed equation with positive parameter that's not solution of perturbed equation with zero parameter

---
### singular formula

$$
\begin{aligned}
\# f(t, x, \epsilon) = k, \epsilon > 0 \land \# f(t, x, \epsilon) \ne k, \epsilon = 0 \\
f = \text{perturbed equation} \\
t = \text{time} \\
x = \text{solution} \\
\epsilon = \text{parameter} \\
k = \text{number of solutions} 
\end{aligned}
$$

---
### analytic

- there exists limit of power series near point

---
### analytic formula

$$
\begin{aligned}
f(t, x, \epsilon) = \sum_{i, j, k = 0}^{\infty}c_{ijk}(t-t_0)^i(x - x_0)^j(\epsilon - \epsilon_0)^k \\
|t-t_0| < \sigma, |x-x_0| < \eta, |\epsilon-\epsilon_0| < \rho \\
f = \text{perturbed equation} \\
t = \text{time} \\
x = \text{solution} \\
\epsilon = \text{parameter} \\
c = \text{coefficient} \\
\sigma, \eta, \rho = \text{radius of convergence}
\end{aligned}
$$

---
### analytic property

- complex analytic function
- complex analytic variable
- multivariable analytic function
- analytic operation

---
### analytic property formula

$$
\begin{aligned}
f \in \mathbb C \rightarrow f(t, x, \epsilon) \in C^{\omega} \\
x \in \mathbb C \rightarrow f(t, x, \epsilon) \in C^{\omega} \\
i \ge 1 \rightarrow  f(t, x_i, \epsilon) \in C^{\omega} \\
(+), (\cdot), (\circ), (\frac{df}{dx}), (\int dfdx) \in C^{\omega} 
\end{aligned}
$$

---
### function notation

- asymptotic behavior of function as parameter approaches limit

---
### function notation formula

$$
\begin{aligned}
f(\epsilon) = \sum_{n=0}^\infty c_n \epsilon^n \\
\frac{f(\epsilon)}{\epsilon^r} = \sum_{n=r}^\infty c_{n-r} \epsilon^{n-r} \\
f = \text{perturbed equation} \\
\epsilon = \text{parameter} \\
c = \text{sequence} 
\end{aligned}
$$

---
### big-O notation

- size of function less or equal big-O

---
### big-O notation formula

$$
\begin{aligned}
\lim_{\epsilon \rightarrow 0} |\frac{f(\epsilon)}{\epsilon^r}| \le C \rightarrow f(\epsilon) \le O(\epsilon^r) \\
f = \text{perturbed equation} \\
\epsilon = \text{parameter} \\
C = \text{constant} \\
O = \text{order} 
\end{aligned}
$$

---
### little-o notation

- size of function much less little-o

---
### little-o notation formula

$$
\begin{aligned}
\lim_{\epsilon \rightarrow 0} \frac{f(\epsilon)}{\epsilon^r} = 0 \rightarrow f(\epsilon) \ll o(\epsilon^r) \\
f = \text{perturbed equation} \\
\epsilon = \text{parameter} \\
o = \text{order} 
\end{aligned}
$$

---
### mclaurin series

- approximate function of parameter near zero as infinite polynomial

---
### mclaurin series formula

$$
\begin{aligned}
f(\epsilon) = \sum_{n=0}^\infty \frac{f^{(n)}(0)}{n!}\epsilon^n \\
f = \text{perturbed equation} \\
f^n = \text{nth derivative} \\
n! = \text{nth factorial} \\
\epsilon = \text{parameter}
\end{aligned}
$$

---
### regular algebraic equation

- series solution equal solution of algebraic equation
---
### regular algebraic equation formula

$$
\begin{aligned}
F(x, \epsilon) = 0 \\
x(\epsilon = 0) = x_0 \\
0 \le \epsilon \ll 1 \\
F = \text{regular algebraic equation} \\
x = \text{solution} \\
\epsilon = \text{parameter}
\end{aligned}
$$

---
### algebraic property

- for every regular, analytic algebraic equation there exists unique analytic solution

---
### algebraic property formula

$$
\begin{aligned}
(C^{\omega} \ni F(x_0, 0) = 0) \land (\frac{\partial F}{\partial x}(x_0, 0) \ne 0) \rightarrow \exists! x(\epsilon) \in C^{\omega} \\
C^{\omega} = \text{analyticity} \\
F = \text{algebraic equation} \\
x = \text{solution} \\
\epsilon = \text{parameter} 
\end{aligned}
$$

---
### simple root

- solution of algebraic equation equal integer power series

---
### simple root formula

$$
\begin{aligned}
\frac{\partial F}{\partial x}(x_0, 0) \ne 0 \rightarrow x(\epsilon) = \sum_{n=0}^{\infty} x_n\epsilon^n \\
x = \text{solution} \\
\epsilon = \text{parameter} 
\end{aligned}
$$

---
### multiple root

- solution of algebraic equation equal rational power series

---
### multiple root formula

$$
\begin{aligned}
\frac{\partial F}{\partial x}(x_0, 0)= 0 \rightarrow x(\delta) = \sum_{n =0}^{\infty} x_n\delta^n \\
\delta = \epsilon^{1/m} \\
x = \text{solution} \\
\epsilon = \text{parameter}  \\
m = \text{order} 
\end{aligned}
$$

---
### regular differential equation

- series solution equal solution of differential equation
---
### regular differential equation formula

$$
\begin{aligned}
\frac{du}{dt} = F(t, u, \epsilon) \\
u(t=0, \epsilon=0) = u_0 \\
0 \le \epsilon \ll 1 \\
t\ge 0 \\
F = \text{regular differential equation} \\
u(t, \epsilon ) = \text{solution} \\
\epsilon = \text{parameter}
\end{aligned}
$$

---
### differential property

- for every regular, analytic differential equation there exists unique analytic solution

---
### differential property formula

$$
\begin{aligned}
F(0, u_0, 0) \in C^{\omega} \rightarrow \exists! u(t, \epsilon) \in C^{\omega} \\
F = \text{regular differential equation} \\
C^{\omega} = \text{analyticity} \\
u(t, \epsilon) = \text{solution} \\
\epsilon = \text{parameter} 
\end{aligned}
$$

---
### secularity

- unbounded growth over time destroy the periodicity of solution

---
### secularity formula

$$
\begin{aligned}
f_1(t) \in \text{span}\set{\cos t, \sin t} \rightarrow x_1(t) = t(A \cos \omega t + B \sin \omega t) \\
f_1(t) = x_1'' + x_1 
\end{aligned}
$$

---
### poincare-lindstedt

- rescale time
- solve initial condition
- expand frequency in powers of epsilon
- expand solution in powers of epsilon
- substitute series solution
- collect coefficients of epsilon powers
- solve 1st order solution
- eliminate secularity with 1st frequency order such that coefficient of resonant term equal zero
- repeat for every $n$th order epsilon
- approximate periodic solution of nonlinear differential equation

---
### poincare-lindstedt formula

$$
\begin{aligned}
x''(t) + x(t) = \epsilon f(t, x, x'') \\
0 \le \epsilon \ll 1 \\
\tau = \omega(\epsilon)t \\
\omega(\epsilon) = \sum_{n=1}^{\infty} \omega_n\epsilon^n \\
x(t) = \sum_{n=1}^{\infty} x_n(\tau)\epsilon^n
\end{aligned}
$$

---
### outer problem

- reduced equation governing the slow varying behavior outside the boundary layer

---
### outer problem formula

$$
\begin{aligned}
\epsilon = 0 \rightarrow \phi(x)y' = f(x) \land y_{out}(x) = C \\
\epsilon y'' + \phi(x)y' = f(x) \\
\epsilon = \text{parameter} \\
y = \text{solution} 
\end{aligned}
$$

---
### inner problem

- rescaled equation governing the fast varying behavior inside the boundary layer
- choose scaling factor such that at least two terms of order unity

---
### inner problem formula

$$
\begin{aligned}
\tau = \frac{x}{\delta} \rightarrow \frac{1}{\delta}(\frac{d^2y}{d\tau^2} + \phi(x)\frac{dy}{d\tau}) = f(x) \\
\epsilon y'' + \phi(x)y' = f(x) \\
\delta = \epsilon^n \\ 
\epsilon = \text{parameter} \\
\delta = \text{scaling factor} \\
y = \text{solution} 
\end{aligned}
$$

---
### matching problem

- enforce agreement between inner solution and outer solution within overlapping region

---
### matching problem formula

$$
\begin{aligned}
\lim_{x\rightarrow 0^+} y_{out}(x) = \lim_{\tau\rightarrow \infty} y_{in}(\tau) \\
y_{out} = \text{outer solution} \\
y_{in} = \text{inner solution} 
\end{aligned}
$$

---
### singular differential equation

- solve the outer problem
- locate the outer boundary condition
- solve the inner problem
- ignore lower order term(s)
- solve the matching problem
- change of variable
- composite solution equal single equation with multiple scales

---
### singular differential equation formula

$$
\begin{aligned}
y(x) = y_{out}(x) + y_{in}(x) - y_{match}(x) \\
y_{out} = \text{outer solution} \\
y_{in} = \text{inner solution} \\
y_{match} = \text{matching solution} 
\end{aligned}
$$

---
