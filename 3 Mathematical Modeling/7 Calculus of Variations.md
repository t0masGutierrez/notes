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
### continuous differentiability
- vector space of functions with continuous derivatives

---
### continuous differentiability formula
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
### continuous differentiability norm
- norm of continuously differentiable function

---
### continuous differentiability norm formula
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
### continuous differentiability neighborhood
- region where there exists open ball around center
![](3%20Mathematical%20Modeling/Images/continuous%20differentiability%20neighborhood.png)

---
### continuous differentiability neighborhood formula
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
\partial F[f, h] = \left. \frac{d}{d\epsilon}F[f + \epsilon h]\right|_{\epsilon=0} \\
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
\forall h \in \mathcal V_{0}: \partial F[f_*, h] = 0 \\
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
\partial^2 F[f, h] = \left. \frac{d^2}{d\epsilon^2}F[f + \epsilon h]\right|_{\epsilon=0} \\
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
\forall h \in \mathcal V_{0}: \partial^2 F[f_*, h] \ge 0 \implies \exists \delta > 0, \forall f \in N_\delta(f_*): F[f_*] \le F[f] \\
\forall h \in \mathcal V_{0}: \partial^2 F[f_*, h] \le 0 \implies \exists \delta > 0, \forall f \in N_\delta(f_*): F[f_*] \ge F[f] \\
h = \text{admissible variation} \\
\mathcal V_{0} = \text{vector space} \\
F = \text{functional} \\
f_* = \text{local extremizer} \\
f = \text{admissible function} 
\end{aligned}
$$

---
### first-order type
- highest derivative equal first derivative

---
### first-order type formula
$$
\begin{aligned}
L(x, f, f') \\
L = \text{lagrangian} \\
x = \text{independent variable} \\
f, f' = \text{admissible function}
\end{aligned}
$$

---
### fixed-fixed type
- vector space satisfy both boundary condition

---
### fixed-fixed type formula
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
### variational
- problem of finding the extremum of first-order, fixed-fixed functional aka extremal

---
### variational formula
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
### euler-lagrange equation
- local extremal of functional must satisfy equation

---
### euler-lagrange equation formula
$$
\begin{aligned}
\frac{\partial L}{\partial f} - \frac{d}{dx}(\frac{\partial L}{\partial f'}) = 0 \\
f(a) = \alpha \\
f(b) = \beta \\
a < x < b \\
L = \text{lagrangian} \\
f, f' = \text{admissible function} \\
x = \text{independent variable} \\
\alpha, \beta = \text{constant}
\end{aligned}
$$

---
### legendre condition
- local minimizer of functional must satisfy condition
- local maximizer of functional must satisfy condition

---
### legendre condition formula
$$
\begin{aligned}
\frac{\partial^2 L}{\partial (f')^2} \ge 0 \\
\frac{\partial^2 L}{\partial (f')^2} \le 0 \\
\end{aligned}
$$

---
### analysis of candidate
- solve euler-lagrange equation for extremal candidate
- apply boundary condition for constant of integration
- solve legendre condition for sign of extremal candidate
- substitute unperturbed variation into functional
- integrate first variation by parts
- eliminate admissible variation term(s) with boundary condition
- eliminate coefficient of admissible variation integrand with euler-lagrange equation
- sign of functional difference equal sign of extremal candidate

---
### analysis of candidate formula
$$
\begin{aligned}

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
### term
- definition

---
### term
- definition

---
