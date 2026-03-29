### epsilon-delta limit

- function approaches limit as input point approaches limit point

---
### epsilon-delta limit formula

$$
\begin{aligned}
\lim_{x \rightarrow x_0} f(x) = L \leftrightarrow \forall \epsilon > 0, \exists \delta > 0, \exists x_0 \in X, \forall x \in S: d(x, x_0) < \delta \rightarrow \exists L \in Y: d(f(x), L) < \epsilon \\
f: S \subset X \rightarrow Y \\
x_0 = \text{limit point} \\
L = \text{limit} \\
X = \text{domain} \\
Y = \text{codomain} \\
d = \text{metric} 
\end{aligned}
$$

---
### sequential limit

- function approaches limit as input term approaches sequential limit

---
### sequential limit formula

$$
\begin{aligned}
\lim_{x \rightarrow x_0} f(x) = L \leftrightarrow \forall \set{a_n} \in S: \lim_{n\rightarrow \infty} a_n = x_0 \rightarrow \lim_{n\rightarrow \infty} f(a_n) = L \\
f: S \subset X \rightarrow Y \\
x_0 = \text{sequential limit} \\
L = \text{limit} \\
\set{a_n} = \text{sequence} \\
X = \text{domain} \\
Y = \text{codomain} 
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
### unique limit property formula

$$
\begin{aligned}
(\lim_{x \rightarrow x_0} f(x) = L) \land (\lim_{x \rightarrow x_0} f(x) = L') \rightarrow L = L' \\
(\lim_{x \rightarrow x_0} f(x) = L) \land (\lim_{x \rightarrow x_0} g(x) = K) \rightarrow \lim_{x \rightarrow x_0} (f+g)(x) = L + K \\
(\lim_{x \rightarrow x_0} f(x) = L) \land (\lim_{x \rightarrow x_0} g(x) = K) \rightarrow \lim_{x \rightarrow x_0} (f-g)(x) = L - K \\
(\lim_{x \rightarrow x_0} f(x) = L) \land (\lim_{x \rightarrow x_0} g(x) = K) \rightarrow \lim_{x \rightarrow x_0} (f \cdot g)(x) = L \cdot K \\
(\lim_{x \rightarrow x_0} f(x) = L) \land (\lim_{x \rightarrow x_0} g(x) = K \ne 0) \rightarrow \lim_{x \rightarrow x_0} (\frac{f}{g})(x) = \frac{L}{K}
\end{aligned}
$$

---
### continuity

- definition

---
### continuity formula

$$
\begin{aligned}

\end{aligned}
$$

---
### term

- definition

---
### separated

- every point of 1st subset equal isolated point of 2nd subset and vice versa

---
### separated formula

$$
\begin{aligned}
A, B \subset X \rightarrow \overline A \cap B = A \cap \overline B = \emptyset \\
A, B = \text{separated set} \\
X = \text{metric space}
\end{aligned}
$$

---
### disconnected

- there exists union of separated set

---
### disconnected formula

$$
\begin{aligned}
S \subset X \rightarrow S = A \cup B \\
S = \text{disconnected set} \\
X = \text{metric space} \\
A, B = \text{separated set} 
\end{aligned}
$$

---
### real connected property

- connected subset of real numbers contain every intermediate real number

---
### real connected property formula

$$
\begin{aligned}
(S \subset \mathbb R) \land (x, y \in \mathbb R) \land (x < z < y) \rightarrow z \in \mathbb R \\
S = \text{connected set}
\end{aligned}
$$

---
