### epsilon-delta limit

- function approaches limit as input point approaches limit point

---
### epsilon-delta limit formula

$$
\begin{aligned}
\lim_{x \rightarrow x_0} f(x) = L \iff \forall \epsilon > 0, \exists \delta > 0, \forall x \in S: d(x, x_0) < \delta \implies d(f(x), L) < \epsilon \\
f: S \subset X \rightarrow Y \\
x_0 = \text{limit point} \\
L = \text{limit} \\
d = \text{metric} \\
X, Y = \text{metric space} 
\end{aligned}
$$

---
### sequential limit

- function approaches limit as input term approaches sequential limit

---
### sequential limit formula

$$
\begin{aligned}
\lim_{x \rightarrow x_0} f(x) = L \iff \forall \set{a_n} \in S: \lim_{n\rightarrow \infty} a_n = x_0 \implies \lim_{n\rightarrow \infty} f(a_n) = L \\
f: S \subset X \rightarrow Y \\
x_0 = \text{sequential limit} \\
L = \text{limit} \\
\set{a_n} = \text{sequence} \\
X, Y = \text{metric space} 
\end{aligned}
$$

---
### limit property

- unique
- addition
- subtraction
- multiplication
- division

---
### limit property formula

$$
\begin{aligned}
(\lim_{x \rightarrow x_0} f(x) = L) \land (\lim_{x \rightarrow x_0} f(x) = K) \implies L = K \\
(\lim_{x \rightarrow x_0} f(x) = L) \land (\lim_{x \rightarrow x_0} g(x) = K) \implies \lim_{x \rightarrow x_0} (f+g)(x) = L + K \\
(\lim_{x \rightarrow x_0} f(x) = L) \land (\lim_{x \rightarrow x_0} g(x) = K) \implies \lim_{x \rightarrow x_0} (f-g)(x) = L - K \\
(\lim_{x \rightarrow x_0} f(x) = L) \land (\lim_{x \rightarrow x_0} g(x) = K) \implies \lim_{x \rightarrow x_0} (f \cdot g)(x) = L \cdot K \\
(\lim_{x \rightarrow x_0} f(x) = L) \land (\lim_{x \rightarrow x_0} g(x) = K \ne 0) \implies \lim_{x \rightarrow x_0} (\frac{f}{g})(x) = \frac{L}{K}
\end{aligned}
$$

---
### set property

- range
- inverse range
- range subset
- inverse range subset
- double range subset
- double inverse range subset
- range union
- inverse range complement

---
### set property formula

$$
\begin{aligned}
(f: A \subset X \rightarrow Y) \implies f(A) = \set{f(x) \in Y| x \in A} \\
(f: X \rightarrow B \subset Y) \implies f^{-1}(B) = \set{x \in X| f(x) \in B} \\
A' \subset A \implies f(A') \subset f(A) \\
B' \subset B \implies f^{-1}(B') \subset f^{-1}(B) \\
A \subset f^{-1}\circ f(A) \\
f\circ f^{-1}(B) \subset B \\
f(\bigcup_i A_i) = \bigcup_i f(A_i) \\
f^{-1}(B^c) = f^{-1}(B)^c 
\end{aligned}
$$

---
### continuity

- for every epsilon distance between continuous function at point there exists delta distance between input at point

---
### continuity formula

$$
\begin{aligned}
\forall \epsilon > 0, \exists \delta > 0, \forall x \in S: d(x, x_0) < \delta \implies d(f(x), f(x_0)) < \epsilon \\
f: S \subset X \rightarrow Y \\
d = \text{metric} \\
x_0 = \text{continuous point} \\
f = \text{continuous function} \\
X, Y = \text{metric space} 
\end{aligned}
$$

---
### limit continuity property

- continuous function at input point approaches continuous function at limit point as input point approaches limit point

---
### limit continuity property formula

$$
\begin{aligned}
\lim_{x\rightarrow x_0}f(x) = f(x_0) \\
f: X \rightarrow Y \\
x_0 = \text{limit point} \\
f = \text{continuous function} \\
X, Y = \text{metric space} 
\end{aligned}
$$

---
### open inverse continuity property

- inverse continuous function of codomain open set equal domain open set

---
### open inverse continuity property formula

$$
\begin{aligned}
\lim_{x\rightarrow x_0}f(x) = f(x_0) \iff \forall y \in S, \exists \epsilon > 0: N_{\epsilon}(y) \subset S \\
\implies \forall x \in f^{-1}(S), \exists \epsilon > 0: N_{\epsilon}(x) \subset f^{-1}(S) \\
f:  X \rightarrow S \subset Y \\
x_0 = \text{limit point} \\
x, y = \text{interior point} \\
f = \text{continuous function} \\
N = \text{neighborhood} \\
S, f^{-1}(S) = \text{open set} \\
X, Y = \text{metric space} 
\end{aligned}
$$

---
### closed inverse continuity property

- inverse continuous function of codomain closed set equal domain closed set

---
### closed inverse continuity property formula

$$
\begin{aligned}
\lim_{x\rightarrow x_0}f(x) = f(x_0) \iff S'\subset S \subset Y  \implies f^{-1}(S)' \subset f^{-1}(S) \subset X \\
f:  X \rightarrow S \subset Y \\
x_0 = \text{limit point} \\
f = \text{continuous function} \\
S, f^{-1}(S) = \text{closed set} \\
S', f^{-1}(S)' = \text{derived set} \\
X, Y = \text{metric space}
\end{aligned}
$$

---
### composite continuity property

- composition of continuous function equal continuous function

---
### composite continuity property formula

$$
\begin{aligned}
\lim_{x\rightarrow x_0}f(x) = f(x_0) \land \lim_{x\rightarrow x_0}g(f(x)) = g(f(x_0)) \implies \lim_{x\rightarrow x_0}(g \circ f)(x) = (f \circ g)(x_0) \\
f: X \rightarrow Y \\
g: Y \rightarrow Z \\
g \circ f: X \rightarrow Z \\
x_0 = \text{limit point} \\
f, g = \text{continuous function} \\
X, Y, Z = \text{metric space} 
\end{aligned}
$$

---
### operation continuity property

- addition
- subtraction
- multiplication
- division

---
### operation continuity property

$$
\begin{aligned}
\lim_{x\rightarrow x_0}f(x) = f(x_0) \land \lim_{x\rightarrow x_0}g(x) = g(x_0) \implies \lim_{x\rightarrow x_0}(f+g)(x) = (f+g)(x_0) \\
\lim_{x\rightarrow x_0}f(x) = f(x_0) \land \lim_{x\rightarrow x_0}g(x) = g(x_0) \implies \lim_{x\rightarrow x_0}(f-g)(x) = (f-g)(x_0) \\
\lim_{x\rightarrow x_0}f(x) = f(x_0) \land \lim_{x\rightarrow x_0}g(x) = g(x_0) \implies \lim_{x\rightarrow x_0}(f\cdot g)(x) = (f\cdot g)(x_0) \\
\lim_{x\rightarrow x_0}f(x) = f(x_0) \land \lim_{x\rightarrow x_0}g(x) = g(x_0) \ne 0 \implies \lim_{x\rightarrow x_0}(\frac{f}{g})(x) = (\frac{f}{g})(x_0) \\
\end{aligned}
$$

---
### vector continuity property

- continuous vector equal coordinatewise continuous function

---
### vector continuity property formula

$$
\begin{aligned}
\forall i \le k: \lim_{x\rightarrow x_0}f_i(x) = f_i(x_0) \\
\vec f:X \rightarrow \mathbb R^k = [f_1(x), \dots, f_k(x)] \\
x_0 = \text{limit point} \\
f = \text{continuous function} \\
X, Y = \text{metric space} 
\end{aligned}
$$

---
### compact continuity property

- continuous function of compact domain equal compact range

---
### compact continuity property formula

$$
\begin{aligned}
\forall \set{A_i}_{i\in I} \subset Y, \exists \{A_{i_j}\}_{j=1}^n \subset \{A_i\}_{i\in I}: f(X) \subset \bigcup_{j=1}^n A_{i_j} \subset Y \\
f: X \rightarrow Y \\
A = \text{open set} \\
\set{A} = \text{open cover} \\
I, J = \text{index set} \\
f = \text{continuous function} \\
X, f(X) = \text{compact set}
\end{aligned}
$$

---
### locally bounded

- every domain of locally bounded function within finite distance

---
### locally bounded formula

$$
\begin{aligned}
\forall x_0 \in X, \exists \epsilon > 0, \exists M \in \mathbb R: d(x, x_0) < \epsilon \implies f(x) \le M \\
f: S \subset X \rightarrow \mathbb R \\
f = \text{locally bounded function} \\
X = \text{metric space} 
\end{aligned}
$$

---
### globally bounded

- every codomain of bounded function within finite distance

---
### globally bounded formula

$$
\begin{aligned}
\exists M \in \mathbb R, \forall x \in S: |f(x)| \le M \\
f: S \subset X \rightarrow \mathbb R \\
f = \text{bounded function} \\
X = \text{metric space} 
\end{aligned}
$$

---
### closed bounded continuity property

- continuous function of compact domain equal closed bounded range of k-dimensional real numbers and bounded function of k-dimensional real numbers
- continuous function of noncompact domain equal unbounded function of real numbers

---
### closed bounded continuity property formula

$$
\begin{aligned}
f(X)' \subset f(X) \subset \mathbb R^k \land \exists M \in \mathbb R: |f(X)| \le M \\
f: X \rightarrow \mathbb R^k \\
f = \text{continuous function} \\
f = \text{bounded function} \\
f(x_0) = \text{minimum} \\
f(x_1) = \text{maximum} \\
X = \text{compact set} \\
f(X) = \text{closed bounded set} 
\end{aligned}
$$

---
### extreme continuity property

- for every continuous function of compact domain there exists supremum and infimum
- continuous bounded function of noncompact domain equal incomplete function of real numbers

---
### extreme continuity property formula

$$
\begin{aligned}
\exists \sup f(X), \inf f(X) \in  Y: \inf f(X) \le f(X) \le \sup f(X) \\
f: X \rightarrow Y \\
f = \text{continuous function} \\
X = \text{compact set} \\
Y = \text{metric space} \\
\end{aligned}
$$

---
### compact inverse continuity property

- for every injective continuous function of compact domain there exists inverse continuous function

---
### compact inverse continuity property formula

$$
\begin{aligned}
\forall f(x), \exists f^{-1}(y): \lim_{y\rightarrow y_0}f^{-1}(y) = f^{-1}(y_0) \\
f: X \rightarrow Y \\
f = \text{injective function} \\
f, f^{-1} = \text{continuous function} \\
y_0 = \text{limit point} \\
X = \text{compact set} \\
Y = \text{metric space}
\end{aligned}
$$

---
### homeomorphism 

- bijective continuous function with continuous inverse function

---
### homeomorphism formula

$$
\begin{aligned}
f: X \rightarrow Y, X \simeq Y \\
f, f^{-1} = \text{continuous function} \\
f = \text{bijection} 
\end{aligned}
$$

---
### compact homeomorphism property

- bijective continuous function with compact domain equal homeomorphism

---
### compact homeomorphism property formula

$$
\begin{aligned}
f: X \rightarrow Y, X \simeq Y \\
f = \text{continuous function} \\
f = \text{bijection} \\
X = \text{compact set}
\end{aligned}
$$

---
### uniform continuity

- for every epsilon distance between continuous function at every point there exists delta distance between every point

---
### uniform continuity formula

$$
\begin{aligned}
\forall \epsilon > 0, \forall x_1, x_2 \in S: d(x_1, x_2) < \delta \implies d(f(x_1), f(x_2)) < \epsilon \\
f: S \subset X \rightarrow Y \\
x_1, x_2 = \text{continuous point} \\
f = \text{continuous function} \\
X, Y = \text{metric space} 
\end{aligned}
$$

---
### compact uniform continuity property

- continuous function of compact domain equal uniformly continuous function
- continuous bounded function of unbounded noncompact set of real numbers equal nonuniform continuous function

---
### compact uniform continuity property formula

$$
\begin{aligned}
\forall \epsilon > 0, \forall x_1, x_2 \in S: d(x_1, x_2) < \delta \implies d(f(x_1), f(x_2)) < \epsilon \\
f: X \rightarrow Y \\
f = \text{continuous function} \\
f = \text{uniformly continuous function} \\
x_1, x_2 = \text{continuous point} \\
X = \text{compact set} \\
Y = \text{metric space} 
\end{aligned}
$$

---
### separated

- every point of 1st subset equal isolated point of 2nd subset and vice versa

---
### separated formula

$$
\begin{aligned}
A, B \subset X \implies \overline A \cap B = A \cap \overline B = \emptyset \\
A, B = \text{separated set} \\
\overline A, \overline B = \text{closure} \\
X = \text{metric space}
\end{aligned}
$$

---
### disconnected

- there exists union of nonempty separated set

---
### disconnected formula

$$
\begin{aligned}
\exists A, B \in X: S = A \cup B \\
A, B = \text{separated set} \\
X = \text{metric space} \\
S = \text{disconnected set} 
\end{aligned}
$$

---
### continuous connected property

- continuous function of connected set equal connected set

---
### continuous connected property formula

$$
\begin{aligned}
\not\exists A, B \in Y: f(X) = A \cup B \\
f: X \rightarrow Y \\
A, B = \text{separated set} \\
Y = \text{metric space} \\
f = \text{continuous function} \\
X, f(X) = \text{connected set} 
\end{aligned}
$$

---
### real connected property

- connected set of real numbers contain every intermediate real number of set

---
### real connected property formula

$$
\begin{aligned}
S \subset \mathbb R, \forall x, y \in S: x < y \implies [x, y] \subset S \\
S = \text{connected set}
\end{aligned}
$$

---
### intermediate connected property

- continuous function on interval contain every intermediate value on interval

---
### intermediate connected property formula

$$
\begin{aligned}
f(a) < c < f(b) \implies \exists x \in (a, b): f(x) = f(c) \\
f: [a, b] \rightarrow Y \\
f = \text{continuous function} \\
Y = \text{metric space} 
\end{aligned}
$$

---
### path

- continuous function connecting coordinate

---
### path formula

$$
\begin{aligned}
\gamma(0) = x_0 \land \gamma(1) = x_1 \\
\gamma: [0, 1] \rightarrow X \\
\gamma = \text{continuous function} \\
x_0, x_1 = \text{coordinate} \\
X = \text{metric space} 
\end{aligned} 
$$

---
### path connected

- for every coordinate of path connected set there exists continuous function connecting coordinate

---
### path connected formula

$$
\begin{aligned}
\forall x_0, x_1 \in S: \gamma(0) = x_0 \land \gamma(1) = x_1 \\
\gamma: [0, 1] \rightarrow S \subset X \\
x_0, x_1 = \text{coordinate} \\
S  = \text{path connected set} \\
\gamma = \text{continuous function} \\
X = \text{metric space} 
\end{aligned} 
$$

---
### path connected property

- path connected set equal connected set

---
### path connected property formula

$$
\begin{aligned}
\forall x_0, x_1 \in S: \gamma(0) = x_0 \land \gamma(1) = x_1 \implies \not\exists A, B \in X: S = A \cup B \\
\gamma: [0, 1] \rightarrow S \subset X \\
x_0, x_1 = \text{coordinate} \\
S  = \text{connected set} \\
\gamma = \text{continuous function} \\
A, B = \text{separated set} \\
X = \text{metric space} 
\end{aligned}
$$

---
