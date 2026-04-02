### absolute value
- nonnegativity operation on real number equal distance between real numbers

---
### absolute value formula
$$
\begin{aligned}
x \in \mathbb R \implies |x| \ge 0
\end{aligned}
$$

---
### absolute value property
- negative
- multiplication
- addition
- subtraction
- absolute subtraction
- subtraction

---
### absolute value property formula
$$
\begin{aligned}
|-x| = |x| \\
|x \cdot y| = (|x|)(|y|) \\
|x + y| \le |x| + |y| \\
|x - y| \le |x| + |y| \\
||x| - |y|| \le |x - y| \\
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
x = y \iff d(x, y) = 0 \\
x \ne y \implies d(x, y) > 0 \\
d(x, y) = d(y, x) \\
d(x, y) \le d(x, z) + d(z, y) 
\end{aligned}
$$

---
### open ball
- sphere with finite radius from center

---
### open ball formula
$$
\begin{aligned}
B_{r}(x_{0}) = \{x \in X |d(x, x_{0}) < r\} \\
x = \text{point} \\
d = \text{metric} \\
x_{0} = \text{center} \\
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
N \subset X, \exists r > 0: x_{0} \in B_{r}(x_{0}) \subset N_{r}(x_{0}) \\
N = \text{neighborhood} \\
X = \text{metric space} \\
r = \text{radius} \\
x_{0} = \text{center} \\
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
S \subset X, \forall r > 0: N_{r}(x_{0}) \setminus \{x_{0}\} \cap S \ne \emptyset \\
X = \text{metric space} \\
r = \text{radius} \\
N = \text{neighborhood} \\
x_{0} = \text{limit point}
\end{aligned}
$$

---
### interior point
- every point of neighborhood around interior point equal point of set

---
### interior point formula
$$
\begin{aligned}
S \subset X, \exists r > 0: N_{r}(x_{0}) \subset S \\
X = \text{metric space} \\
r = \text{radius} \\
N = \text{neighborhood} \\
x_{0} = \text{interior point}
\end{aligned}
$$

---
### open
- every point of open set equal interior point of open set

---
### open formula
$$
\begin{aligned}
S \subset X, \forall x \in S, \exists r > 0: N_{r}(x) \subset S \\
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
S \subset Y \subset X, \forall x \in S, \exists r > 0: N_{r}(x) \cap Y \subset S \\
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
S^{\circ} = \{x \in X|\exists r > 0: N_{r}(x) \subset S\} \\
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
### boundary
- intersection of set and complement of set

---
### boundary formula
$$
\begin{aligned}
\partial S = \overline S \setminus S^{\circ} = \overline S \cap \overline {S^c} = \set {x \in X| \forall r > 0: N_{r}(x) \cap S \ne \emptyset \land N_{r}(x) \cap S^c \ne \emptyset}\\
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
S \subset X, \exists x_{0} \in X, \exists r > 0: S \subset B_{r}(x_{0}) \\
S = \text{bounded set} \\
X = \text{metric space} \\
x_{0} = \text{center} \\
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
S \subset X, \forall r > 0, \exists \set {a_{i}}_{i=1}^{n} \subset X: S \subset \bigcup_{i=1}^n B_{r}(x_{i}) \\
S = \text{totally bounded set} \\
r = \text{radius} \\
X = \text{metric space} \\
a_{n} = \text{sequence} \\
B = \text{open ball} \\
x_{i} = \text{center}
\end{aligned}
$$

---
### interval limit point property
- every point of interval equal limit point including endpoint

---
### interval limit point property
$$
\begin{aligned}
(a, b) = S \subset X \implies S' = [a, b] \\
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
\{0, 1, \dots, n\} \not\sim S \subset X \implies \forall r > 0, \forall x_{0} \in S': |N_{r}(x_{0}) \setminus \{x_{0}\} \cap S| = \infty \\
S = \text{infinite set} \\
X = \text{metric space} \\
r = \text{radius} \\
x_{0} = \text{limit point} \\
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
\{0, 1, \dots, n\} \sim S \subset X \implies \forall r > 0, \forall x \in S: N_{r}(x) \setminus \{x\} \cap S = \{x\} \\
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
(\bigcup_{i} S_{i})^c = \bigcap_{i} (S_{i}^c) \\
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
S' \subset S \subset X \iff \forall x \in S^c, \exists r > 0: N_{r}(x) \subset S^c \\
S \subset X, \forall x \in S, \exists r > 0: N_{r}(x) \subset S \iff (S')^c \subset S^c \subset X \\
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
S \subset X, \forall x \in S, \exists r > 0: N_{r}(x) \subset S \implies N_{r}(x) \subset \bigcup_{i} S_{i} \\
S' \subset S \subset X  \implies S' \subset \bigcap_{i} S_{i}   \\
S \subset X, \forall x \in S, \exists r > 0: N_{r}(x) \subset S \implies N_{r}(x) \subset \bigcap_{i=1}^n S_{i} \\
S' \subset S \subset X  \implies S' \subset \bigcup_{i}^n S_{i}  \\
\end{aligned}
$$

---
### special cover property
- empty set equal both open set and closed set
- metric space equal both open set and closed set

---
### special cover property formula
$$
\begin{aligned}
\forall x \in \emptyset, X, \exists r > 0: N_{r}(x) \subset \emptyset, X \\
\emptyset', X' \subset \emptyset, X 
\end{aligned}
$$

---
### uncountable perfection property
- nonempty perfect set of k-dimensional real numbers equal uncountable set

---
### uncountable perfection property formula
$$
\begin{aligned}
\emptyset \ne S' = S \subset \mathbb R^k \implies (\{0, 1, 2, 3, \dots, n\} \not \sim S) \land (\mathbb N \not\sim S) \\
S = \text{perfect set} \\
S' = \text{derived set} 
\end{aligned}
$$

---
### closure property
- derived closure
- equal closure
- sup closure
- sub closure
- union closure

---
### closure property formula
$$
\begin{aligned}
\overline S' \subset \overline S \subset X \\
S' \subset S \subset X \iff \overline S = S \\
S \subset \mathbb R, \exists x_{0} \in \mathbb R, \exists r > 0:  S \subset B_{r}(x_{0}) \implies \exists \sup S \in \overline S \\ 
(S \subset K) \land (K' \subset K \subset X) \implies \overline S \subset \overline K = K \\
\overline {\bigcup_{i} A_{i}} = \bigcup_{i} \overline A_{i} \\
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
S \subset X, \forall r > 0, \exists \set {x_{i}}_{i=1}^{n} \subset X: S \subset \bigcup_{i=1}^n B_{r}(x_{i}) \implies \exists x_{0} \in X, \exists r > 0: S \subset B_{r}(x_{0}) \\
S \subset X, \exists x_{0} \in X, \exists r > 0: S \subset B_{r}(x_{0}) \not\implies  \forall r > 0, \exists \set {x_{i}}_{i=1}^{n} \subset X: S \subset \bigcup_{i=1}^n B_{r}(x_{i}) \\
S \subset \mathbb R^k, \forall r > 0, \exists \set {x_{i}}_{i=1}^{n} \subset \mathbb R^k: S \subset \bigcup_{i=1}^n B_{r}(x_{i}) \iff \exists x_{0} \in \mathbb R^k, \exists r > 0: S \subset B_{r}(x_{0})
\end{aligned}
$$

---
