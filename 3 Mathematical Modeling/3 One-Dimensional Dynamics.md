### dynamical system

- rule that describes the change of state over time

---
### dynamical system formula

$$
\begin{aligned}
\frac{du}{dt} = f(u, c_1, \dots, c_n), u(t=0) = u_0, t \ge 0 \\
u = \text{solution} \\
t = \text{time} \\
u_0 = \text{initial condition} \\
c = \text{parameter}
\end{aligned}
$$

---
### time view

- view solution as graph in the $(t, u)$-plane
---
### time view formula

$$
\begin{aligned}
\frac{du}{dt} = f(u) \\
f = \text{slope} 
\end{aligned}
$$

---
### phase view

- view solution as moving point along $u$-axis
---
### phase view formula

$$
\begin{aligned}
\frac{du}{dt} = f(u) \\
f = \text{velocity}
\end{aligned}
$$

---
### solvability property

- for every initial condition there exists unique solution of dynamical system

---
### solvability property formula

$$
\begin{aligned}
\forall u_0 \in \mathbb R, \exists t \in (T_0, T_1): u(t) \in D = \{u \in \mathbb R| \exists \frac{du}{dt}\} \\
(t \le T_0) \lor (t \ge T_1) \rightarrow u(t) \not\in D = \{u \in \mathbb R|\exists \frac{du}{dt}\} \\
u_0 \ne \hat u_0 \rightarrow \forall t \in (T_0, T_1): u(t) \ne \hat u(t)
\end{aligned}
$$

---
### equilibrium solution

- steady state solution of dynamical system equal zero

---
### equilibrium solution formula

$$
\begin{aligned}
\forall t \ge 0: u(t) = u_* \leftrightarrow f(u_*) = 0 \\
u = \text{solution} \\
t = \text{time} \\
u_* = \text{equilibrium point}
\end{aligned}
$$

---
### monotonicity property

- sign of initial slope equal monotonicity of solution

---
### monotonicity property formula

$$
\begin{aligned}
f(u_0) > 0 \rightarrow \forall t: f(u) > 0 \\
f(u_0) = 0 \rightarrow \forall t: f(u) = 0 \\
f(u_0) < 0 \rightarrow \forall t: f(u) < 0 \\
\end{aligned}
$$

---
### equilibrium stability

- behavior of solution near equilibrium point

---
### equilibrium stability formula

$$
\begin{aligned}
I(\rho) = (u_* - \rho, u_* + \rho) \\
u_* = \text{equilibrium point}
\end{aligned}
$$

---
### asymptotic stability

- if nearby initial condition then nearby solution converge on equilibrium point
---
### asymptotic stability formula

$$
\begin{aligned}
\exists \delta > 0: |u_0 - u_*| < \delta \rightarrow (\forall \epsilon > 0, \forall t \ge 0: |u(t) - u_* | < \epsilon) \land (\forall u_0 \in \mathbb R: \lim_{t \rightarrow \infty} u(t) = u_*) \\
u_0 = \text{initial condition} \\
u_* = \text{equilibrium point} \\
u = \text{solution} \\
t = \text{time} \\
\end{aligned}
$$

---
### neutral stability

- if nearby initial condition then nearby solution sometimes converge on equilibrium point
---
### neutral stability formula

$$
\begin{aligned}
\exists \delta > 0: |u_0 - u_*| < \delta \rightarrow (\forall \epsilon > 0, \forall t \ge 0: |u(t) - u_* | < \epsilon) \land (\exists u_0 \in \mathbb R: \lim_{t \rightarrow \infty} u(t) \ne u_*) \\
u_0 = \text{initial condition} \\
u_* = \text{equilibrium point} \\
u = \text{solution} \\
t = \text{time} \\
\end{aligned}
$$

---
### instability

- if far initial condition then far solution diverge off equilibrium point
---
### instability formula

$$
\begin{aligned}
(\forall \delta > 0: |u_0 - u_*| < \delta) \land (\exists \epsilon > 0, \exists t \ge 0: |u(t) - u_* | \ge \epsilon) \land (\forall u_0 \in \mathbb R: \lim_{t \rightarrow \infty} u(t) \ne u_*) \\
u_0 = \text{initial condition} \\
u_* = \text{equilibrium point} \\
u = \text{solution} \\
t = \text{time} \\
\end{aligned}
$$

---
### stability derivative test

- sign of derivative at equilibrium point equal stability of equilibrium point

---
### stability derivative test formula

$$
\begin{aligned}
f'(u_*) < 0 \rightarrow \lim_{t \rightarrow \infty} u(t) = u_* \\
f'(u_*) > 0 \rightarrow \lim_{t \rightarrow \infty} u(t) \ne u_* \\
\end{aligned}
$$

---
### bifurcation

- quantitative change of parameter cause qualitative change of phase

---
### bifurcation formula

$$
\begin{aligned}
\Delta h \rightarrow \Delta (h \times u_*)
\end{aligned}
$$

---
### bifurcation example

- $f(u) = u^3 - uh$ 
- $u_* = 0, \pm \sqrt h$ 

---
### bifurcation example formula

$$
\begin{aligned}
h \le 0 \rightarrow f'(0) > 0 \\
h > 0 \rightarrow f'(0) < 0 \\
h > 0 \rightarrow f'(\sqrt h) > 0 \\
h > 0 \rightarrow f'(-\sqrt h) > 0 \\
\end{aligned}
$$

---
### bifurcation diagram

- find equilibrium point
- determine stability of equilibrium point
- find parameter where the stability of equilibria change
- graph the equilibrium point versus the parameter
---
### bifurcation diagram formula

$$
\begin{aligned}
h \times u_* = \{(h, u_*)| f(h, u_*) = 0\} \\
h = \text{parameter} \\
u_* = \text{equilibrium point} 
\end{aligned}
$$

---
### saddle-node bifurcation

- creation or destruction of two equilibria

---
### saddle-node bifurcation formula

$$
\begin{aligned}
\frac{du}{dt} = h - u^2
\end{aligned}
$$

---
### transcritical bifurcation

- two equilibria intersect and exchange stability

---
### transcritical bifurcation formula

$$
\begin{aligned}
\frac{du}{dt} = hu - u^2
\end{aligned}
$$

---
### pitchfork bifurcation

- single equilibrium split into three equilibria

---
### pitchfork bifurcation formula

$$
\begin{aligned}
\frac{du}{dt} = hu - u^3
\end{aligned}
$$

---
