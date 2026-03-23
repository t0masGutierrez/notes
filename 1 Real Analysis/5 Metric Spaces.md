### absolute value

- nonnegativity operation on real number equal distance between real numbers

---
### absolute value formula

$$
\begin{aligned}
x \in \mathbb R \rightarrow |x| \ge 0
\end{aligned}
$$

---
### absolute value property

- negative
- multiplication
- addition
- subtraction

---
### absolute value property formula

$$
\begin{aligned}
|-x| = |x| \\
|x \cdot y| = (|x|)(|y|) \\
|x + y| \le |x| + |y| \\
||x| + |y|| \le |x - y| \\
|x - y| \le |x| + |y| \\
\end{aligned}
$$

---
### metric

- distance between coordinates of set

---
### metric formula

$$
\begin{aligned}
d: X \times X \rightarrow \mathbb R = [0, \infty)
\end{aligned}
$$

---
### metric space

- set whose distance between coordinates equal real number

---
### metric space formula

$$
\begin{aligned}
x = y \leftrightarrow \text{d}(x, y) = 0 \\
x \ne y \rightarrow \text{d}(x, y) > 0 \\
\text{d}(x, y) = \text{d}(y, x) \\
\text{d}(x, y) \le \text{d}(x, z) + \text{d}(z, y) 
\end{aligned}
$$

---
### open ball

- sphere with finite radius from center

---
### open ball formula

$$
\begin{aligned}
B_r(x_0) = \{x \in X |\text{d}(x, x_0) < r\} \\
x = \text{point} \\
\text{d} = \text{metric} \\
x_0 = \text{center} \\
r = \text{radius}
\end{aligned}
$$

---
### neighborhood

- region where there exists open ball around center

---
### neighborhood formula

$$
\begin{aligned}
N \subset X, \exists r > 0: x_0 \in B_r(x_0) \subset N_r(x_0) \\
N = \text{neighborhood} \\
X = \text{metric space} \\
r = \text{radius} \\
x_0 = \text{center} \\
B = \text{open ball}
\end{aligned}
$$

---
### limit point

- every neighborhood around limit point contain point of set

---
### limit point formula

$$
\begin{aligned}
S \subset X, \forall r > 0: N_r(x_0) \setminus \{x_0\} \cap S \ne \emptyset \\
X = \text{metric space} \\
r = \text{radius} \\
N = \text{neighborhood} \\
x_0 = \text{limit point}
\end{aligned}
$$

---
### interior point

- every point of neighborhood around interior point equal point of set

---
### interior point formula

$$
\begin{aligned}
S \subset X, \exists r > 0: N_r(x_0) \subset S \\
X = \text{metric space} \\
r = \text{radius} \\
N = \text{neighborhood} \\
x_0 = \text{interior point}
\end{aligned}
$$

---
### open

- every point of open set equal interior point of open set

---
### open formula

$$
\begin{aligned}
S \subset X, \forall x \in S, \exists r > 0: N_r(x) \subset S \\
S = \text{open set} \\
X = \text{metric space} \\
x = \text{interior point} \\
r = \text{radius} \\
N = \text{neighborhood}
\end{aligned}
$$

---
### relatively open

- every point of relatively open set equal interior point of relatively open set

---
### relatively open formula

$$
\begin{aligned}
S \subset Y \subset X, \forall x \in S, \exists r > 0: N_r(x) \cap Y \subset S \\
S = \text{relatively open set} \\
X = \text{metric space} \\
r = \text{radius} \\
N = \text{neighborhood} \\
x = \text{interior point}
\end{aligned}
$$

---
### closed

- every limit point of closed set equal point of closed set

---
### closed formula

$$
\begin{aligned}
S' \subset S \subset X \\
S' = \text{derived set} \\
S = \text{closed set} \\
X = \text{metric space}
\end{aligned}
$$

---
### perfect

- closed set and every point of perfect set equal limit point of perfect set

---
### perfect formula

$$
\begin{aligned}
S' = S \subset X \\
S' = \text{derived set} \\
S = \text{perfect set} \\
X = \text{metric space}
\end{aligned}
$$

---
### interior

- largest open subset of the set

---
### interior formula

$$
\begin{aligned}
S^{\circ} = \{x \in X|\exists r > 0: N_r(x) \subset S\} \\
x = \text{interior point} \\
X = \text{metric space} \\
N = \text{neighborhood}
\end{aligned}
$$

---
### closure

- smallest closed superset of the set

---
### closure formula

$$
\begin{aligned}
\overline S = S \cup S' \\
S' = \text{derived set}
\end{aligned}
$$

---
### closure property

- derived closure
- equal closure
- sub closure

---
### closure property formula

$$
\begin{aligned}
\overline S' \subset \overline S \subset X \\
S' \subset S \subset X \leftrightarrow \overline S = S \\
(S \subset K) \land (K' \subset K \subset X) \rightarrow \overline S \subset K
\end{aligned}
$$

---
### supremum closure property

- there exists supremum of closure

---
### supremum closure property formula

$$
\begin{aligned}
S \subset X \rightarrow \exists \sup \overline S \\
X = \text{metric space} \\
\overline S = \text{closure}
\end{aligned}
$$

---
### boundary

- intersection of set and complement of set

---
### boundary formula

$$
\begin{aligned}
\partial S = \overline S \setminus S^{\circ} = \overline S \cap \overline {S^c} = \set {x \in X| \forall r > 0: N_r(x) \cap S \ne \emptyset \land N_r(x) \cap S^c \ne \emptyset}\\
\overline S = \text{closure} \\
S^{\circ} = \text{interior} \\
c = \text{complement} \\
N = \text{neighborhood}
\end{aligned}
$$

---
### dense

- every point of metric space equal point of closure

---
### dense formula

$$
\begin{aligned}
S \subset \overline S = X \\
S = \text{dense set} \\
\overline S = \text{closure} \\
X = \text{metric space} \\
\end{aligned}
$$

---
### bounded

- every point of bounded set within finite radius from center

---
### bounded formula

$$
\begin{aligned}
S \subset X, \exists x_0 \in X, \exists r > 0: S \subset B_r(x_0) \\
S = \text{bounded set} \\
X = \text{metric space} \\
x_0 = \text{center} \\
r = \text{radius} 
\end{aligned}
$$

---
### totally bounded

- every point of totally bounded set within finite cover of open ball

---
### totally bounded formula

$$
\begin{aligned}
S \subset X, \forall \epsilon > 0, \exists \set {a_i}_{i=1}^{n} \subset X: S \subset \bigcup_{i=1}^n B_{\epsilon}(x_i) \\
S = \text{totally bounded set} \\
X = \text{metric space} \\
a_n = \text{sequence} \\
B = \text{open ball} \\
x_i = \text{center}
\end{aligned}
$$

---
### totally bounded property

- forward
- reverse
- complete

---
### totally bounded property formula

$$
\begin{aligned}
S \subset X, \forall \epsilon > 0, \exists \set {x_i}_{i=1}^{n} \subset X: S \subset \bigcup_{i=1}^n B_{\epsilon}(x_i) \rightarrow \exists x_0 \in X, \exists r > 0: S \subset B_r(x_0) \\
S \subset X, \exists x_0 \in X, \exists r > 0: S \subset B_r(x_0) \not\rightarrow \forall \epsilon > 0, \exists \set {x_i}_{i=1}^{n} \subset X: S \subset \bigcup_{i=1}^n B_{\epsilon}(x_i) \\
S \subset \mathbb R^k, \forall \epsilon > 0, \exists \set {x_i}_{i=1}^{n} \subset \mathbb R^k: S \subset \bigcup_{i=1}^n B_{\epsilon}(x_i) \leftrightarrow \exists x_0 \in \mathbb R^k, \exists r > 0: S \subset B_r(x_0)
\end{aligned}
$$

---
### cover property

- empty set equal both open set and closed set
- metric space equal both open set and closed set

---
### cover property formula

$$
\begin{aligned}
\forall x \in \emptyset, X, \exists r > 0: N_r(x) \subset \emptyset, X \\
\emptyset', X' \subset \emptyset, X 
\end{aligned}
$$

---
### interval limit point property

- every point of interval equal limit point including endpoint

---
### interval limit point property

$$
\begin{aligned}
(a, b) = S \subset X \rightarrow S' = [a, b] \\
S = \text{interval} \\
S' = \text{derived set} \\
X = \text{metric space}
\end{aligned}
$$

---
### infinite limit point property

- every neighborhood around limit point contain infinite point of set

---
### infinite limit point property formula

$$
\begin{aligned}
\{0, 1, \dots, n\} \not\sim S \subset X \rightarrow \forall r > 0, \forall x_0 \in S': |N_r(x_0) \setminus \{x_0\} \cap S| = \infty \\
S = \text{infinite set} \\
X = \text{metric space} \\
r = \text{radius} \\
x_0 = \text{limit point} \\
N = \text{neighborhood} 
\end{aligned}
$$

---
### finite limit point property

- every point of finite set equal isolated point of finite set

---
### finite limit point property formula

$$
\begin{aligned}
\{0, 1, \dots, n\} \sim S \subset X \rightarrow \forall r > 0, \forall x \in S: N_r(x) \setminus \{x\} \cap S = \{x\} \\
S = \text{finite set} \\
X = \text{metric space} \\
r = \text{radius} \\
x = \text{isolated point} \\
N = \text{neighborhood} 
\end{aligned}
$$

---
### join complement property

- complement of set union equal intersection of set complement

---
### join complement property formula

$$
\begin{aligned}
(\bigcup_{i} S_i)^c = \bigcap_{i} (S_i^c) \\
c = \text{complement}
\end{aligned}
$$

---
### cover complement property

- closed set equal complement of open set
- open set equal complement of closed set

---
### cover complement property formula

$$
\begin{aligned}
S' \subset S \subset X \leftrightarrow \forall x \in S^c, \exists r > 0: N_r(x) \subset S^c \\
S \subset X, \forall x \in S, \exists r > 0: N_r(x) \subset S \leftrightarrow (S')^c \subset S^c \subset X \\
S' = \text{derived set} \\
c = \text{complement} \\
r = \text{radius} \\
N = \text{neighborhood} 
\end{aligned}
$$

---
### join cover property

- union of open set equal open set
- intersection of closed set equal closed set
- finite intersection of open set equal open set
- finite union of closed set equal closed set

---
### join cover property formula

$$
\begin{aligned}
S \subset X, \forall x \in S, \exists r > 0: N_r(x) \subset S \rightarrow N_r(x) \subset \bigcup_{i} S_i \\
S' \subset S \subset X  \rightarrow S' \subset \bigcap_{i} S_i   \\
S \subset X, \forall x \in S, \exists r > 0: N_r(x) \subset S \rightarrow N_r(x) \subset \bigcap_{i=1}^n S_i \\
S' \subset S \subset X  \rightarrow S' \subset \bigcup_{i}^n S_i  \\
\end{aligned}
$$

---
