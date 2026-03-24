### dynamical system

- rule that describes the change of state over time

---
### dynamical system formula

$$
\begin{aligned}
\frac{dx}{dt} = f(x, y, c_1, \dots, c_n) \\
\frac{dy}{dt} = g(x, y, c_1, \dots, c_n) \\
x(t=0) = x_0 \\
y(t=0) = y_0 \\
t \ge 0 \\
x, y = \text{solution} \\
t = \text{time} \\
x_0, y_0 = \text{initial condition} \\
c = \text{parameter}
\end{aligned}
$$

---
### time view

- view solution as curve in the $(t, x)$-plane or $(t, y)$-plane
---
### time view formula

$$
\begin{aligned}
\frac{dx}{dt} = f(x, y) \\
\frac{dy}{dt} = g(x, y) \\
f, g = \text{slope} 
\end{aligned}
$$

---
### phase view

- view solution as moving point in the $(x, y)$-plane
---
### phase view formula

$$
\begin{aligned}
v = [f, g] \\
f, g = \text{velocity}
\end{aligned}
$$

---
### solvability property

- for every initial condition there exists unique solution of dynamical system
---
### solvability property formula

$$
\begin{aligned}
\forall (x_0, y_0) \in \mathbb R, \exists t \in (T_0, T_1): (x, y)(t) \in D = \{(x, y) \in \mathbb R| \exists! (\frac{dx}{dt}, \frac{dy}{dt})\} \\
(t \le T_0) \lor (t \ge T_1) \rightarrow (x, y)(t) \not\in D = \{(x, y) \in \mathbb R| \exists! (\frac{dx}{dt}, \frac{dy}{dt})\} \\
(x_0, y_0) \ne (\hat x_0, \hat y_0) \rightarrow \forall t \in (T_0, T_1): (x, y)(t) \ne (\hat x, \hat y)(t)
\end{aligned}
$$

---
### vector field

- collection of vectors for all points
---
### vector field formula

$$
\begin{aligned}
v(x, y) = \{(\frac{dx}{dt}, \frac{dy}{dt})| x, y \in D\} \\
\frac{dx}{dt}, \frac{dy}{dt} = \text{velocity} \\
\end{aligned}
$$

---
### direction field

- collection of signs for all points
---
### direction field formula

$$
\begin{aligned}
(f, g)(x, y) = \{(\hat x, \hat y)| x, y \in D\} \\
\hat x, \hat y = \text{unit vector}
\end{aligned}
$$

---
### nullcline curve

- set of points such that derivative equal zero
- equilibrium point equal intersection of nullcline curve

---
### nullcline curve formula

$$
\begin{aligned}
F(x, y) = \{(x, y)| \frac{dx}{dt} = 0\} \\
G(x, y) = \{(x, y) | \frac{dy}{dt} = 0\} \\
x, y = \text{solution} \\
t = \text{time} \\
\frac{dx}{dt}, \frac{dy}{dt} = \text{velocity} 
\end{aligned}
$$

---
### path equation

- system of ODEs that determine the path of moving point in the $(x, y)$-plane

---
### path equation formula

$$
\begin{aligned}
\frac{dy}{dx} = \frac{g(x, y)}{f(x, y)} \\
x, y = \text{solution} \\
f, g = \text{velocity}
\end{aligned}
$$

---
### first integral

- general solution of path equation constant along every trajectory

---
### first integral formula

$$
\begin{aligned}
\forall (x, y) \in D: \frac{dE}{dt}(x, y)(t) = 0 \rightarrow E(x, y)(t) = C \\
\frac{\partial}{\partial x}(\phi f) = \frac{\partial}{\partial y}(-\phi g) \rightarrow (\frac{\partial E}{\partial x} = -\phi g) \land (\frac{\partial E}{\partial y} = \phi f) \\
x, y = \text{solution} \\
t = \text{time} \\
D = \text{domain} \\
E = \text{first integral} \\
C = \text{constant} \\
\phi = \text{integrating factor}
\end{aligned}
$$

---
### equilibrium solution

- steady state solution of dynamical system equal zero

---
### equilibrium solution formula

$$
\begin{aligned}
\forall t \ge 0: (x, y)(t) = (x_*, y_*) \leftrightarrow f(x_*, y_*) = g(x_*, y_*) = 0 \\
x, y = \text{solution} \\
t = \text{time} \\
x_*, y_* = \text{equilibrium point} 
\end{aligned}
$$

---
### equilibrium stability

- behavior of solution near equilibrium point

---
### equilibrium stability formula

$$
\begin{aligned}
N_{\rho}(x_*, y_*) = (x_* - \rho, x_* + \rho) \times (y_* - \rho, y_* + \rho) \\
x_*, y_* = \text{equilibrium point} \\
\rho = \text{radius} 
\end{aligned}
$$

---
### asymptotic equilibrium stability

- sufficiently nearby solution remain arbitrarily nearby equilibrium point for all time
- sufficiently nearby solution eventually converge on equilibrium point
---
### asymptotic equilibrium stability formula

$$
\begin{aligned}
\forall \epsilon > 0, \exists \delta > 0, \forall t \ge 0: (x_0, y_0) \in N_{\delta}(x_*, y_*) \rightarrow (x, y)(t) \in N_{\epsilon}(x_*, y_*) \\
\land \forall x_0, y_0 \in \mathbb R: \lim_{t \rightarrow \infty} (x, y)(t) = (x_*, y_*) \\
x_0, y_0 = \text{initial condition} \\
N = \text{neighborhood} \\
x_*, y_* = \text{equilibrium point} \\
x, y = \text{solution} \\
t = \text{time} 
\end{aligned}
$$

---
### neutral equilibrium stability

- sufficiently nearby solution remain arbitrarily nearby equilibrium point for all time
- sufficiently nearby solution sometimes converge on equilibrium point
---
### neutral equilibrium stability formula

$$
\begin{aligned}
\forall \epsilon > 0, \exists \delta > 0, \forall t \ge 0: (x_0, y_0) \in N_{\delta}(x_*, y_*) \rightarrow (x, y)(t) \in N_{\epsilon}(x_*, y_*) \\
\land \exists x_0, y_0 \in \mathbb R: \lim_{t \rightarrow \infty} (x, y)(t) \ne (x_*, y_*) \\
x_0, y_0 = \text{initial condition} \\
N = \text{neighborhood} \\
x_*, y_* = \text{equilibrium point} \\
x, y = \text{solution} \\
t = \text{time} 
\end{aligned}
$$

---
### equilibrium instability

- every solution infinitely diverge off equilibrium point
---
### equilibrium instability formula

$$
\begin{aligned}
\exists \epsilon > 0, \forall \delta > 0, \forall t \ge 0: (x_0, y_0) \in N_{\delta}(x_*, y_*) \land (x, y)(t) \not\in N_{\epsilon}(x_*, y_*) \\
\land \forall x_0, y_0 \in \mathbb R: \lim_{t \rightarrow \infty} (x, y)(t) \ne (x_*, y_*) \\
x_0, y_0 = \text{initial condition} \\
N = \text{neighborhood} \\
x_*, y_* = \text{equilibrium point} \\
x, y = \text{solution} \\
t = \text{time} 
\end{aligned}
$$

---
### periodic solution

- repeating solution with closed orbit
---
### periodic solution formula

$$
\begin{aligned}
\forall t \ge 0: (x, y)(t + P) = (x, y)(t) \\
x, y = \text{solution} \\
t = \text{time} \\
P = \text{period}
\end{aligned}
$$

---
### asymptotic periodic stability

- sufficiently nearby solution remain arbitrarily nearby equilibrium point for all time
- sufficiently nearby solution eventually converge on periodic solution
---
### asymptotic periodic stability formula

$$
\begin{aligned}
\forall \epsilon > 0, \exists \delta > 0, \forall t \ge 0: (x_0, y_0) \in N_{\delta}(x_*, y_*) \rightarrow (x, y)(t) \in N_{\epsilon}(x_*, y_*) \\
\land \forall x_0, y_0 \in \mathbb R: \lim_{t \rightarrow \infty} (x, y)(t) = (x_*, y_*) \\
x_0, y_0 = \text{initial condition} \\
N = \text{neighborhood} \\
x_*, y_* = \text{equilibrium point} \\
x, y = \text{solution} \\
t = \text{time} 
\end{aligned}
$$

---
### neutral periodic stability

- sufficiently nearby solution remain arbitrarily nearby equilibrium point for all time
- sufficiently nearby solution sometimes converge on periodic solution
---
### neutral periodic stability formula

$$
\begin{aligned}
\forall \epsilon > 0, \exists \delta > 0, \forall t \ge 0: (x_0, y_0) \in N_{\delta}(x_*, y_*) \rightarrow (x, y)(t) \in N_{\epsilon}(x_*, y_*) \\
\land \exists x_0, y_0 \in \mathbb R: \lim_{t \rightarrow \infty} (x, y)(t) \ne (x_*, y_*) \\
x_0, y_0 = \text{initial condition} \\
N = \text{neighborhood} \\
x_*, y_* = \text{equilibrium point} \\
x, y = \text{solution} \\
t = \text{time} 
\end{aligned}
$$

---
### periodic instability

- every solution infinitely diverge off periodic solution
---
### periodic instability formula

$$
\begin{aligned}
\exists \epsilon > 0, \forall \delta > 0, \exists t \ge 0: (x_0, y_0) \in N_{\delta}(x_*, y_*) \land (x, y)(t) \not\in N_{\epsilon}(x_*, y_*) \\
\land \forall x_0, y_0 \in \mathbb R: \lim_{t \rightarrow \infty} (x, y)(t) \ne (x_*, y_*) \\
x_0, y_0 = \text{initial condition} \\
N = \text{neighborhood} \\
x_*, y_* = \text{equilibrium point} \\
x, y = \text{solution} \\
t = \text{time} 
\end{aligned}
$$

---
### linearity

- superposition
- matrix
- zero

---
### linearity formula

$$
\begin{aligned}
f(ax + by) = af(x) + bf(y) \\
\exists A \in \mathcal M: \frac{dv}{dt} = Av \\
f(0) = 0
\end{aligned}
$$

---
### linear system

- dynamical system with linearity

---
### linear system formula

$$
\begin{aligned}
(\frac{dx}{dt} = ax + by) \land (\frac{dy}{dt} = cx + dy) \rightarrow \frac{dv}{dt} = Av \\
A = \begin{bmatrix} 
a & b \\
c & d \\
\end{bmatrix} \\
v = [x, y] \\
x, y, v = \text{solution} \\
t = \text{time} \\
a, b, c, d = \text{coefficient} 
\end{aligned}
$$

---
### nondegenerate system

- nonzero determinant of coefficient matrix generate single equilibrium point 

---
### nondegenerate system formula

$$
\begin{aligned}
\det(A) \ne 0 \rightarrow \#v_* = 1 \\
A = \text{coefficient matrix} \\
v_* = \text{equilibrium point}
\end{aligned}
$$

---
### degenerate system

- zero determinant of coefficient matrix generate infinite equilibrium point

---
### degenerate system formula

$$
\begin{aligned}
\det(A) = 0 \rightarrow \#v_* = \infty \\
A = \text{coefficient matrix} \\
v_* = \text{equilibrium point}
\end{aligned}
$$

---
### distinct real eigenvalues

- general solution of linear system equal eigenvectors of coefficient matrix with distinct real eigenvalues

---
### distinct real eigenvalues formula

$$
\begin{aligned}
v(t) = C_1e^{\lambda_1 t}\hat u_1 + C_2e^{\lambda_2 t}\hat u_2 \\
v = [x, y] \\
A = \begin{bmatrix} 
a & b \\
c & d \\
\end{bmatrix} \\
v = \text{solution} \\
t = \text{time} \\
a, b, c, d = \text{coefficient} \\
\lambda = \text{eigenvalue} \\
\hat u = \text{eigenvector}
\end{aligned}
$$

---
### distinct real eigenvalues property

- two negative eigenvalues equal asymptotically stable node
- two opposite eigenvalues equal unstable saddle
- two positive eigenvalues equal unstable node
---
### distinct real eigenvalues property formula

$$
\begin{aligned}
\lambda_1, \lambda_2 < 0 \rightarrow \forall v_0 \in \mathbb R^2: \lim_{t \rightarrow \infty} v(t) = v_* \\
(\lambda_1 > 0) \land (\lambda_2 < 0) \rightarrow \forall v_0 \in \mathbb R^2: \lim_{t \rightarrow \infty} v(t) \ne v_* \\
\lambda_1, \lambda_2 > 0 \rightarrow \forall v_0 \in \mathbb R^2: \lim_{t \rightarrow \infty} v(t) \ne v_* 
\end{aligned}
$$

---
### repeated real eigenvalues

- general solution of linear system equal eigenvectors of coefficient matrix with repeated real eigenvalues
---
### repeated real eigenvalues formula

$$
\begin{aligned}
\hat u_1 \ne \hat u_2 \rightarrow v(t) = e^{\lambda t}(C_1\hat u_1 + C_2\hat u_2) \\
\hat u_1 = \hat u_2 \rightarrow v(t) = C_1 e^{\lambda t}\hat u + C_2e^{\lambda t}(\hat ut + \hat w) \land (A - \lambda I)\hat w = \hat u \\
v = [x, y] \\
A = \begin{bmatrix} 
a & b \\
c & d \\
\end{bmatrix} \\
v = \text{solution} \\
t = \text{time} \\
a, b, c, d = \text{coefficient} \\
\lambda = \text{eigenvalue} \\
\hat u = \text{eigenvector} \\
\hat w = \text{generalized eigenvector}
\end{aligned}
$$

---
### repeated real eigenvalues property

- single negative eigenvalue equal asymptotically stable node
- single positive eigenvalue equal unstable node 
- single eigenvector equal improper node

---
### repeated real eigenvalues property formula

$$
\begin{aligned}
\lambda < 0 \rightarrow \forall v_0 \in \mathbb R^2: \lim_{t \rightarrow \infty} v(t) = v_* \\
\lambda > 0 \rightarrow \forall v_0 \in \mathbb R^2: \lim_{t \rightarrow \infty} v(t) \ne v_* \\
\end{aligned}
$$

---
### complex eigenvalues

- general solution of linear system equal eigenvectors of coefficient matrix with complex eigenvalues
---
### complex eigenvalues formula

$$
\begin{aligned}
v(t) = C_1e^{\alpha t}(\gamma \cos\beta t - \lambda \sin\beta t) + C_2e^{\alpha t}(\gamma \cos\beta t + \lambda \sin\beta t) \\
\alpha = 0 \rightarrow v(t) = v_0 (\cos\beta t + \frac{A \sin \beta t}{\beta}) \\
v = \text{solution} \\
t = \text{time} \\
\alpha = \text{real eigenvalue part} \\
\beta = \text{imaginary eigenvalue part} \\
\gamma = \text{real eigenvector part} \\
\lambda = \text{imaginary eigenvector part} \\
A = \text{coefficient matrix} \\
v_0 = \text{initial condition} 
\end{aligned}
$$

---
### complex eigenvalues property

- negative real eigenvalue part equal asymptotically stable spiral
- zero real eigenvalue part equal neutrally stable center
- positive real eigenvalue part equal unstable spiral

---
### complex eigenvalues property formula

$$
\begin{aligned}
\alpha < 0 \rightarrow \forall v_0 \in \mathbb R^2: \lim_{t \rightarrow \infty} v(t) = v_* \\
\alpha = 0 \rightarrow \exists v_0 \in \mathbb R^2: \lim_{t \rightarrow \infty} v(t) \ne v_* \\
\alpha > 0 \rightarrow \forall v_0 \in \mathbb R^2: \lim_{t \rightarrow \infty} v(t) \ne v_* 
\end{aligned}
$$

---
