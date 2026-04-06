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
f^{(n)} = \text{nth derivative} 
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
\mathcal V = \text{domain}
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
- function associated with global maximum of functional

---
### absolute maximizer formula
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
- maximum norm of continuously differentiable function

---
### continuous differentiability norm formula
$$
\begin{aligned}
\|f(x)\|_{C^m} = \sum_{k=0}^m |\max_{a \le x \le b}f^{(k)}(x)| \\
f \in \mathcal V \subset C^n[a, b] \\
m \le n \\
f = \text{continuous function} \\
f^{(k)} = \text{kth derivative} \\
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
\mathcal V = \set{f \in C^n[a, b] | \forall j \in (1, \dots, J): G_{j}(f) = c_{j}} \\
\mathcal V_{0} = \set{h \in C^n[a, b] | \forall j \in (1, \dots, J): G_{j}(h) = 0} \\
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
\forall f \in N_\delta(f_*), \exists! h \in \mathcal V_{0}: f = f_* + h \iff \|h\| \le \delta \\
f, f_* = \text{admissible function} \\
\mathcal V, \mathcal V_{0} = \text{vector space} \\
h = \text{admissible variation}
\end{aligned}
$$

---
### variations
- one-parameter family of admissible functions

---
### variations formula
$$
\begin{aligned}
f_* + \epsilon h \in \mathcal V \\
\epsilon \in \mathbb R \\
f_* = \text{admissible function} \\
\epsilon = \text{parameter} \\
h = \text{admissible variation} 
\end{aligned}
$$

---
### first variation
- first derivative of functional equal slope of functional

---
### first variation formula
$$
\begin{aligned}
\partial F[f_*, h] = \left. \frac{d}{d\epsilon}F[f_* + \epsilon h]\right|_{\epsilon=0} \\
f_* = \text{admissible function} \\
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
f_* = \text{local extremizer} \\
h = \text{admissible variation}
\end{aligned}
$$

---
### second variation
- second derivative of functional equal curvature of functional

---
### second variation formula
$$
\begin{aligned}
\partial^2 F[f_*, h] = \left. \frac{d^2}{d\epsilon^2}F[f_* + \epsilon h]\right|_{\epsilon=0} \\
f_* = \text{admissible function} \\
\epsilon = \text{parameter} \\
h = \text{admissible variation}
\end{aligned}
$$

---
### second variation property
- second variation of local minimizer greater or equal zero
- second variation of local maximizer less or equal zero

---
### second variation property formula
$$
\begin{aligned}
\forall h \in \mathcal V_{0}: \partial^2 F[f_*, h] \ge 0 \implies \exists \delta > 0, \forall f \in N_\delta(f_*): F[f_*] \le F[f] \\
\forall h \in \mathcal V_{0}: \partial^2 F[f_*, h] \le 0 \implies \exists \delta > 0, \forall f \in N_\delta(f_*): F[f_*] \ge F[f] \\
f_* = \text{local extremizer} \\
h = \text{admissible variation}
\end{aligned}
$$

---
