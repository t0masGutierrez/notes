### vector space
- nonempty set thats closed under vector addition and scalar multiplication

---
### vector space formula
$$
\begin{aligned}
\vec x, \vec y \in \mathcal V \implies \vec x + \vec y \in \mathcal V \\
(c \in \mathbb R) \land (\vec x \in \mathcal V) \implies c \vec x \in \mathcal V
\end{aligned}
$$

---
### continuous differentiable
- vector space of functions with continuous derivatives

---
### continuous differentiable formula
$$
\begin{aligned}
C^n[a, b] = \set{f:[a, b] \rightarrow \mathbb R| \lim_{x\rightarrow x_{0}}f^{(n)}(x)=f^{(n)}(x_{0})} \\
f = \text{continuous function} \\
f^{(n)} = \text{nth derivative} \\
x = \text{independent variable} 
\end{aligned}
$$

---
### functional
- mapping from function to real number

---
### functional formula
$$
\begin{aligned}
F: \mathcal V \rightarrow \mathbb R \\
\mathcal V = \set{f: [a, b] \rightarrow \mathbb R| f(a) = \alpha, f(b) = \beta} \\
F = \text{functional} \\
\mathcal V = \text{domain} \\
\alpha, \beta = \text{constant}
\end{aligned}
$$

---
### extremum
- minimum of functional or maximum of functional

---
### extremum formula
$$
\begin{aligned}
\min(F) \lor \max(F) \\
F = \text{functional}
\end{aligned}
$$

---
### extremizer
- function associated with the extremum of functional

---
### extremizer formula
$$
\begin{aligned}
\min(F[f]) \lor \max(F[f]) \\

F = \text{functional} \\
f = \text{extremizer}
\end{aligned}
$$

---
### global minimizer
- function associated with absolute minimum of functional

---
### global minimizer formula
$$
\begin{aligned}
\forall f \in \mathcal V: F[f_*] \le F[f] \\
F : \mathcal V \subset C^n[a, b] \rightarrow \mathbb R \\
f = \text{continuous function} \\
\mathcal V = \text{domain} \\
F = \text{functional} \\
f_* = \text{global minimizer} 
\end{aligned}
$$

---
### global maximizer
- function associated with absolute maximum of functional

---
### global maximizer formula
$$
\begin{aligned}
\forall f \in \mathcal V: F[f_*] \ge F[f] \\
F : \mathcal V \subset C^n[a, b] \rightarrow \mathbb R \\
f = \text{continuous function} \\
\mathcal V = \text{domain} \\
F = \text{functional} \\
f_* = \text{global maximizer} 
\end{aligned}
$$

---
### norm
- magnitude of vector

---
### norm formula
$$
\begin{aligned}
\|v\| \ge 0 \\
\|v\| = 0 \iff v = 0 \\
c \in \mathbb R \implies \|cv\| = (\|c\|)(\|v\|) \\
\|v_{1} + v_{2}\| \le \|v_{1}\| + \|v_{2}\|
\end{aligned}
$$

---
### continuous differentiable norm
- norm of continuously differentiable function

---
### continuous differentiable norm formula
$$
\begin{aligned}
\|f\|_{C^m} = \sum_{k=0}^m |\max_{a \le x \le b}f^{(k)}(x)| \\
f \in \mathcal V \subset C^n[a, b] \\
m \le n \\
f = \text{continuous function} \\
f^{(k)} = \text{kth derivative} \\
x = \text{independent variable} \\
\mathcal V = \text{domain}
\end{aligned}
$$

---
### continuous differentiable neighborhood
- region where there exists open ball around center
![](3%20Mathematical%20Modeling/Images/continuous%20differentiable%20neighborhood.png)

---
### continuous differentiable neighborhood formula
$$
\begin{aligned}
N_\delta(f_*) = \set{f \in \mathcal V| \|f - f_*\|_{C^m} < \delta} \\
f = \text{continuous function} \\
\mathcal V = \text{domain} \\
f_* = \text{center} 
\end{aligned}
$$

---
### local minimizer
- function associated with relative minimum of functional

---
### local minimizer formula
$$
\begin{aligned}
\exists \delta > 0, \forall f \in N_\delta(f_*): F[f_*] \le F[f] \\
F : \mathcal V \subset C^n[a, b] \rightarrow \mathbb R \\
f = \text{continuous function} \\
N = \text{neighborhood} \\
f_* = \text{local minimizer} \\
F = \text{functional}
\end{aligned}
$$

---
### local maximizer
- function associated with relative maximum of functional

---
### local maximizer formula
$$
\begin{aligned}
\exists \delta > 0, \forall f \in N_\delta(f_*): F[f_*] \ge F[f] \\
F : \mathcal V \subset C^n[a, b] \rightarrow \mathbb R \\
f = \text{continuous function} \\
N = \text{neighborhood} \\
f_* = \text{local maximizer} \\
F = \text{functional}
\end{aligned}
$$

---
### admissibility
- vector space of admissible functions
- vector space of admissible variations

---
### admissibility formula
$$
\begin{aligned}
\mathcal V = \set{f \in C^n[a, b] \mid G_{j}[f] = c_{j}} \\
\mathcal V_{0} = \set{h \in C^n[a, b] \mid G_{j}[h] = 0} \\
G: C^n[a, b] \rightarrow \mathbb R \\
c \in \mathbb R \\
\mathcal V, \mathcal V_{0} = \text{vector space} \\
f, h = \text{continuous function} \\
G = \text{functional} \\
c = \text{constant}
\end{aligned}
$$

---
### admissibility property
- admissible function under admissible variation equal admissible function

---
### admissibility property formula
$$
\begin{aligned}
\forall f \in N_\delta(f_*), \exists! h \in \mathcal V_{0}: f = f_* + h \in \mathcal V \\
\|h\| \le \delta \\
f, f_* = \text{admissible function} \\
\mathcal V, \mathcal V_{0} = \text{vector space} \\
h = \text{admissible variation}
\end{aligned}
$$

---
### variation
- one-parameter family of admissible functions

---
### variation formula
$$
\begin{aligned}
f + \epsilon h \in \mathcal V \\
f = \text{admissible function} \\
\epsilon = \text{parameter} \\
h = \text{admissible variation} 
\end{aligned}
$$

---
### first variation
- first derivative of functional equal slope of functional
- 1st-order epsilon

---
### first variation formula
$$
\begin{aligned}
\delta F[f, h] = \frac{d}{d\epsilon}F[f + \epsilon h]_{\epsilon=0} \\
F = \text{functional} \\
f = \text{admissible function} \\
\epsilon = \text{parameter} \\
h = \text{admissible variation}
\end{aligned}
$$

---
### first variation property
- first variation of local extrema equal zero

---
### first variation property formula
$$
\begin{aligned}
\forall h \in \mathcal V_{0}: \delta F[f_*, h] = 0 \\
h = \text{admissible variation} \\
\mathcal V_{0} = \text{vector space} \\
F = \text{functional} \\
f_* = \text{local extremizer} 
\end{aligned}
$$

---
### second variation
- second derivative of functional equal curvature of functional
- 2nd-order epsilon

---
### second variation formula
$$
\begin{aligned}
\delta^2 F[f, h] = \frac{d^2}{d\epsilon^2}F[f + \epsilon h]_{\epsilon=0} \\
F = \text{functional} \\
f = \text{admissible function} \\
h = \text{admissible variation} \\
\epsilon = \text{parameter}
\end{aligned}
$$

---
### second variation property
- second variation of local minimizer greateq zero
- second variation of local maximizer lesseq zero

---
### second variation property formula
$$
\begin{aligned}
\forall h \in \mathcal V_{0}: \delta^2 F[f_*, h] \ge 0 \implies \exists \delta > 0, \forall f \in N_\delta(f_*): F[f_*] \le F[f] \\
\forall h \in \mathcal V_{0}: \delta^2 F[f_*, h] \le 0 \implies \exists \delta > 0, \forall f \in N_\delta(f_*): F[f_*] \ge F[f] \\
h = \text{admissible variation} \\
\mathcal V_{0} = \text{vector space} \\
F = \text{functional} \\
f_* = \text{local extremizer} \\
f = \text{admissible function} 
\end{aligned}
$$

---
### variational calculus
- solve euler-lagrange equation for extremal
- apply boundary condition for constant of integration
- substitute unperturbed variation into functional
- integrate first variation by parts
- eliminate admissible variation term with boundary condition
- sign of functional difference equal sign of extremal

---
### variational calculus formula
$$
\begin{aligned}
F[f] - F[f_*] \le 0 \implies f_* = \max(F) \\
F[f] - F[f_*] \ge 0 \implies f_* = \min(F) \\
h = f - f_* \\
f = \text{admissible function} \\
F = \text{functional} \\
f_* = \text{local extremizer} \\
h = \text{admissible variation}
\end{aligned}
$$

---
### first-order
- highest derivative equal first derivative

---
### first-order formula
$$
\begin{aligned}
L(x, f, f') \\
L = \text{lagrangian} \\
x = \text{independent variable} \\
f, f' = \text{admissible function}
\end{aligned}
$$

---
### fixed-fixed
- vector space satisfy both boundary condition

---
### fixed-fixed formula
$$
\begin{aligned}
\mathcal V = \set{f \in C^2[a, b] \mid f(a) = \alpha, f(b) = \beta} \\
\mathcal V_{0} = \set{h \in C^2[a, b] \mid h(a) = 0, h(b) = 0} \\
\mathcal V, \mathcal V_{0} = \text{vector space} \\
f = \text{admissible function} \\
h = \text{admissible variation} \\
\alpha, \beta = \text{constant}
\end{aligned}
$$

---
### first-order fixed-fixed variational
- problem of finding the extremal of first-order, fixed-fixed functional

---
### first-order fixed-fixed variational formula
$$
\begin{aligned}
F[f] = \int_{a}^b L(x, f, f')dx \\
F = \text{functional} \\
f, f' = \text{admissible function} \\
L = \text{lagrangian} \\
x = \text{independent variable} 
\end{aligned}
$$

---
### first-order fixed-fixed euler-lagrange equation
- local extremal of functional must satisfy equation

---
### first-order fixed-fixed euler-lagrange equation formula
$$
\begin{aligned}
\frac{\partial L}{\partial f} - \frac{d}{dx}(\frac{\partial L}{\partial f'}) = 0 \\
L = \text{lagrangian} \\
f, f' = \text{admissible function} \\
x = \text{independent variable} 
\end{aligned}
$$

---
### first integral
- general solution of euler-lagrange equation constant along every trajectory

---
### first integral formula
$$
\begin{aligned}
L = L(x, f') \implies \forall f \in C^2[a, b]: \frac{\partial L}{\partial f'}(x, f') = A \\
L = L(f, f') \implies \forall f \in C^2[a, b]: L(f, f') - f'\frac{\partial L}{\partial f'}(f, f') = A \\ 
L = \text{lagrangian} \\
x = \text{independent variable} \\
f, f' = \text{admissible function}
\end{aligned}
$$

---
### fundamental lemma property
- global zero equal leading coefficient zero

---
### fundamental lemma property formula
$$
\begin{align}
\forall h \in C^n[a, b]: \int_{a}^b \phi(x)h(x)dx = 0 \implies \forall x \in [a, b]: \phi(x) = 0 \\
h^{(k)}(a) = h^{(k)}(b) = 0 \\
k = 0, \dots, \mu \le n \\
h = \text{admissible variation} \\
\phi = \text{continuous function} \\
x = \text{independent variable} 
\end{align}
$$

---
### sign lemma property
- global sign equal leading coefficient sign

---
### sign lemma property formula
$$
\begin{aligned}
I(h)\ge 0 \implies \forall x\in [a,b]: \phi_{\nu\nu}(x)\ge 0 \\
I(h)=\int_{a}^b \sum_{i=0}^{\nu}\sum_{j=0}^{\nu}\phi_{ij}(x)h^{(i)}(x)h^{(j)}(x)dx \\
h^{(k)}(a) = h^{(k)}(b) = 0 \\
k = 0, \dots, \mu \\
h = \text{admissible variation} \\
\phi = \text{continuous function} \\
x = \text{independent variable}
\end{aligned}
$$

---
### first-order
- highest derivative equal first derivative

---
### first-order formula
$$
\begin{aligned}
L(x, f, f') \\
L = \text{lagrangian} \\
x = \text{independent variable} \\
f, f' = \text{admissible function}
\end{aligned}
$$

---
### fixed-free
- vector space satisfy single boundary condition

---
### fixed-free formula
$$
\begin{aligned}
\mathcal V = \set{f \in C^2[a, b] \mid f(a) = \alpha} \\
\mathcal V_{0} = \set{h \in C^2[a, b] \mid h(a) = 0} \\
\mathcal V, \mathcal V_{0} = \text{vector space} \\
f = \text{admissible function} \\
h = \text{admissible variation} \\
\alpha = \text{constant}
\end{aligned}
$$

---
### fixed-free variational
- problem of finding the extremal of first-order, fixed-free functional

---
### fixed-free variational formula
$$
\begin{aligned}
F[f] = \int_{a}^b L(x, f, f')dx + [G(f)]_{x=b} \\
F = \text{functional} \\
f, f' = \text{admissible function} \\
L = \text{lagrangian} \\
x = \text{independent variable} \\
G = \text{free-end}
\end{aligned}
$$

---
### fixed-free essential boundary condition
- boundary condition associated with the fixed-end

---
### fixed-free essential boundary condition formula
$$
\begin{aligned}
f(a) = \alpha \\
f = \text{admissible function} \\
\alpha = \text{constant}
\end{aligned}
$$

---
### fixed-free natural boundary condition
- boundary condition associated with the free-end

---
### fixed-free natural boundary condition formula
$$
\begin{aligned}
[\frac{\partial G}{\partial f} + \frac{\partial L}{\partial f'}]_{x = b} = 0 \\
[\frac{\partial G}{\partial f} - \frac{\partial L}{\partial f'}]_{x = a} = 0 \\
L = \text{lagrangian} \\
f, f' = \text{admissible function} \\
G = \text{free-end}
\end{aligned}
$$

---
### second-order
- highest derivative equal second derivative

---
### second-order formula
$$
\begin{aligned}
L(x, f, f', f'') \\

L = \text{lagrangian} \\
x = \text{independent variable} \\
f, f', f'' = \text{admissible function} \\
h = \text{admissible variation}
\end{aligned}
$$

---
### fixed-fixed
- vector space satisfy both boundary condition

---
### fixed-fixed formula
$$
\begin{aligned}
\mathcal V = \set{f \in C^4[a, b] \mid f(a) = \alpha, f'(a) = \gamma, f(b) = \beta, f'(b) = \eta} \\
\mathcal V_{0} = \set{h \in C^4[a, b] \mid h(a) = 0, h'(a) = 0, h(b) = 0, h'(b) = 0 } \\
\mathcal V, \mathcal V_{0} = \text{vector space} \\
f = \text{admissible function} \\
h = \text{admissible variation} \\
\alpha, \beta, \gamma, \eta = \text{constant}
\end{aligned}
$$

---
### second-order variational
- problem of finding the extremal of first-order, fixed-fixed functional

---
### second-order variational formula
$$
\begin{aligned}
F[f] = \int_{a}^b L(x, f, f', f'')dx \\
F = \text{functional} \\
f, f', f'' = \text{admissible function} \\
L = \text{lagrangian} \\
x = \text{independent variable} 
\end{aligned}
$$

---
### second-order euler-lagrange equation
- local extremal of functional must satisfy equation

---
### second-order euler-lagrange equation formula
$$
\begin{aligned}
\frac{\partial L}{\partial f} - \frac{d}{dx}(\frac{\partial L}{\partial f'}) + \frac{d^2}{dx^2}(\frac{\partial L}{\partial f''}) = 0 \\
L = \text{lagrangian} \\
f, f' = \text{admissible function} \\
x = \text{independent variable}
\end{aligned}
$$

---
### second-order essential boundary condition
- boundary condition associated with the fixed-end

---
### second-order essential boundary condition formula
$$
\begin{aligned}
f(a) = \alpha \\
f'(a) = \gamma \\
f, f' = \text{admissible function} \\
\alpha, \gamma = \text{constant}
\end{aligned}
$$

---
### second-order natural boundary condition
- boundary condition associated with the free-end

---
### second-order natural boundary condition formula
$$
\begin{aligned}
f(a) = \text{free} \implies [\frac{\partial L}{\partial f'} - \frac{d}{dx}(\frac{\partial L}{\partial f''})]_{x=a} = 0 \\
f'(a) = \text{free} \implies [\frac{\partial L}{\partial f''}]_{x=a} = 0 \\
f(b) = \text{free} \implies [\frac{\partial L}{\partial f'} - \frac{d}{dx}(\frac{\partial L}{\partial f''})]_{x=b} = 0 \\
f'(b) = \text{free} \implies [\frac{\partial L}{\partial f''}]_{x=b} = 0 
\end{aligned}
$$

---
### lagrange-multiplier
- allowable movement along constraint

---
### lagrange-multiplier formula
$$
\begin{aligned}
\begin{bmatrix}  
\dfrac{\partial \widetilde F}{\partial \varepsilon_{1}}(0,0)  
+  
\lambda  
\dfrac{\partial \widetilde G}{\partial \varepsilon_{1}}(0,0) \\
\dfrac{\partial \widetilde F}{\partial \varepsilon_{2}}(0,0)  
+  
\lambda  
\dfrac{\partial \widetilde G}{\partial \varepsilon_{2}}(0,0) \\
\end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix} \\
\tilde F = F[f_* + \epsilon_1h_{1} + \epsilon_2h_{2}] \\
\tilde G = G[g_* + \epsilon_1h_{1} + \epsilon_2h_{2}] \\
F, G = \text{objective functional} \\
G = \text{constraint functional} \\
f_* = \text{local extremizer} \\
\epsilon = \text{parameter} \\
h = \text{admissible variation} 
\end{aligned}
$$

---
### constraint variational
- problem of finding the extremal of constraint functional

---
### constraint variational formula
$$
\begin{aligned}
F[f] = \int_{a}^b L(x, f, f')dx \\
G[f] = \int_{a}^b M(x, f, f')dx = k\\
N = L + \lambda M \\
F = \text{objective functional} \\
G = \text{constraint functional} \\
L, M, N= \text{lagrangian} \\
k = \text{constraint} \\
\lambda = \text{lagrange multiplier} \\
f, f' = \text{admissible function} \\
x = \text{independent variable} 
\end{aligned}
$$

---
### constraint euler-lagrange equation
- local extremal of functional must satisfy equation

---
### constraint euler-lagrange equation formula
$$
\begin{aligned}
\frac{\partial N}{\partial f} - \frac{d}{dx}(\frac{\partial N}{\partial f'}) = 0 \\
N = \text{lagrangian} \\
f, f' = \text{admissible function} \\
x = \text{independent variable} 
\end{aligned}
$$

---
### constraint essential boundary condition
- boundary condition associated with the fixed-end

---
### constraint essential boundary condition formula
$$
\begin{aligned}
f(a) = \alpha \\
G[f] = k \\
\lambda \in \mathbb R
\end{aligned}
$$

---
### constraint natural boundary condition
- boundary condition associated with the free-end

---
### constraint natural boundary condition formula
$$
\begin{aligned}
f(a), f(b) = \text{free} \implies [\frac{\partial L}{\partial f'} + \lambda \frac{\partial M}{\partial f'}]_{x=a} = [\frac{\partial L}{\partial f'} + \lambda \frac{\partial M}{\partial f'}]_{x=b} = 0 \\
L, M = \text{lagrangian} \\
f' = \text{admissible function} \\
\lambda = \text{lagrange multiplier} 
\end{aligned}
$$

---
