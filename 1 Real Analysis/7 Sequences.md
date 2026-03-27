### eventual truth

- there exists natural number such that proposition true for all but finitely many natural number

---
### eventual truth formula

$$
\begin{aligned}
\exists N \in \mathbb  N, \forall n \ge N: P(n) \\
P = \text{proposition}
\end{aligned}
$$

---
### infinite truth

- proposition true for infinitely many natural number

---
### infinite truth formula

$$
\begin{aligned}
\forall N \in \mathbb  N, \exists n \ge N: P(n) \\
P = \text{proposition}
\end{aligned}
$$

---
### sequence

- infinite list of ordered terms

---
### sequence formula

$$
\begin{aligned}
\{a_n\}_{n=1}^{\infty} = a: \mathbb N \rightarrow S, \ n \mapsto a_n \\
a_n = \text{term} \\
S = \text{set}
\end{aligned}
$$

---
### convergent

- there exists limit of sequence

---
### convergent formula

$$
\begin{aligned}
\exists L \in X: \lim_{n \rightarrow \infty}a_n = L \leftrightarrow \forall \epsilon > 0, \exists N \in \mathbb N, \forall n \ge N: d(a_n, L) < \epsilon \\
a_n = \text{term} \\
L = \text{sequential limit} \\
d = \text{metric}
\end{aligned}
$$

---
### divergent

- there exists no limit of sequence

---
### divergent formula

$$
\begin{aligned}
\not\exists L \in X: \lim_{n \rightarrow \infty}a_n = L \leftrightarrow \exists \epsilon > 0, \forall N \in \mathbb N, \exists n \ge N: d(a_n, L) \ge \epsilon \\
a_n = \text{term} \\
L = \text{sequential limit} \\
d = \text{metric}
\end{aligned}
$$

---
### convergence property

- neighborhood convergence
- unique convergence
- bounded convergence
- limit convergence

---
### convergence property formula

$$
\begin{aligned}
\lim_{n \rightarrow \infty} a_n = L \leftrightarrow \forall \epsilon> 0, \exists N \in \mathbb N, \forall n \ge N: a_n \in N_{\epsilon}(L) \\
(\lim_{n \rightarrow \infty} a_n = L) \land (\lim_{n \rightarrow \infty} a_n = L') \rightarrow L = L' \\
\lim_{n \rightarrow \infty} a_n = L \rightarrow \{a_n\} \subset X, \exists \epsilon > 0: \{a_n\} \subset B_{\epsilon}(L) \\
(S \subset X) \land (L \in S') \rightarrow \exists \{a_n\} \in S: \lim_{n \rightarrow \infty} a_n = L
\end{aligned}
$$

---
### limit property

- distance between $n$th term and limit approaches zero as $n$ approaches infinity

---
### limit property formula

$$
\begin{aligned}
\lim_{n \rightarrow \infty} a_n = L \rightarrow \lim_{n \rightarrow \infty} d(a_n, L) = 0 \\
a_n = \text{term} \\
L = \text{sequential limit} \\
d = \text{metric}
\end{aligned}
$$

---
### complex limit property

- addition
- multiplication
- scalar multiplication
- scalar addition
- reciprocal

---
### complex limit property formula

$$
\begin{aligned}
(a_n, b_n \in \mathbb C) \land (\lim_{n \rightarrow \infty}a_n = L) \land (\lim_{n \rightarrow \infty}b_n = K) \rightarrow \lim_{n \rightarrow \infty}(a_n + b_n) = L + K \\
(a_n, b_n \in \mathbb C) \land (\lim_{n \rightarrow \infty}a_n = L) \land (\lim_{n \rightarrow \infty}b_n = K) \rightarrow \lim_{n \rightarrow \infty}(a_n \cdot b_n) = L \cdot K \\
(a_n \in \mathbb C) \land (c \in \mathbb R) \land (\lim_{n \rightarrow \infty}a_n = L) \rightarrow \lim_{n \rightarrow \infty}ca_n = c \cdot L \\
(a_n \in \mathbb C) \land (c \in \mathbb R) \land (\lim_{n \rightarrow \infty}a_n = L) \rightarrow \lim_{n \rightarrow \infty}(c + a_n) = c + L \\
(a_n \in \mathbb C) \land (\lim_{n \rightarrow \infty}a_n = L) \rightarrow \lim_{n \rightarrow \infty} \frac{1}{a_n} = \frac{1}{L} \\
\end{aligned}
$$

---
### vector limit property

- addition
- multiplication
- scalar multiplication
- coordinatewise convergence

---
### vector limit property formula

$$
\begin{aligned}
(\vec x_n, \vec y_n \in \mathbb R^k) \land (\lim_{n \rightarrow \infty} \vec x_n = L) \land (\lim_{n \rightarrow \infty} \vec y_n = K) \rightarrow \lim_{n \rightarrow \infty} (\vec x_n + \vec y_n) = L + K \\
(\vec x_n, \vec y_n \in \mathbb R^k) \land (\lim_{n \rightarrow \infty} \vec x_n = L) \land (\lim_{n \rightarrow \infty} \vec y_n = K) \rightarrow \lim_{n \rightarrow \infty} (\vec x_n \cdot \vec y_n) = L \cdot K \\
(\vec x_n \in \mathbb R^k) \land (a_n \in \mathbb R) \land (\lim_{n \rightarrow \infty} \vec x_n = L) \land (\lim_{n \rightarrow \infty} a_n = K) \rightarrow \lim_{n \rightarrow \infty} (a_n \cdot \vec x_n) = K \cdot L \\
(\vec a_n = [\alpha_{1n}, \dots, \alpha_{kn}]) \land (L = [\alpha_1, \dots, \alpha_k]) \land (\lim_{n \rightarrow \infty} \vec a_n = L) \leftrightarrow \forall j \le k: \lim_{n \rightarrow \infty} \alpha_{jn} = \alpha_j 
\end{aligned}
$$

---
### subsequence

- infinite sublist of ordered terms

---
### subsequence formula

$$
\begin{aligned}
\{a_{n_k}\}_{k=1}^{\infty} = a \circ n: \mathbb N \rightarrow S, \ k \mapsto a_{n_k} \\
\forall k \in \mathbb N: n_k < n_{k+1}  \\
\{a_{n_k}\} = \text{subsequence} \\
S = \text{set}
\end{aligned}
$$

---
### closed subsequence property

- derived set of subsequence equal closed set

---
### closed subsequence property formula

$$
\begin{aligned}
S = \{L | \lim_{k\rightarrow \infty} a_{n_k} = L\} \rightarrow S' \subset S \subset X \\
S = \text{closed set} \\
a_{n_k} = \text{subsequence} \\
L = \text{subsequential limit} \\
X = \text{metric space} 
\end{aligned}
$$

---
### limit subsequence property

- every limit of convergent sequence equal limit of subsequence

---
### limit subsequence property formula

$$
\begin{aligned}
\lim_{n \rightarrow \infty} a_n = L \rightarrow \forall \epsilon > 0, \exists K \in \mathbb N, \forall n_k \ge n_K \ge N: d(a_{n_k}, L) < \epsilon
\end{aligned}
$$

---
### cauchy sequence

- all terms of cauchy sequence are eventually close

---
### cauchy sequence formula

$$
\begin{aligned}
\forall \epsilon > 0, \exists N \in \mathbb N, \forall n, m \ge N: d(a_n, a_m) < \epsilon \\
\{_{c}a_n\} = \text{cauchy sequence} \\
d = \text{metric}
\end{aligned}
$$

---
### cauchy sequence property

- every convergent sequence of metric space equal cauchy sequence
- every cauchy sequence of compact set equal convergent sequence
- every cauchy sequence of k-dimensional real numbers equal convergent sequence

---
### cauchy sequence property formula

$$
\begin{aligned}
\exists L \in X: \lim_{n\rightarrow \infty} a_n = L \rightarrow \{a_n\} = \{_{c}a_n\} \\
\forall \set{Y_i} \subset X, \exists \{Y_{i_1}, \dots Y_{i_n}\} \subset \{Y_i\}: X \subset \bigcup_{k=1}^n Y_{i_k} \rightarrow \forall \{_{c}a_n\} \subset X, \exists L \in X: \lim_{n\rightarrow \infty} {}_{c}a_n = L \\
\forall \{_{c}a_n\} \subset \mathbb R^k, \exists L \in \mathbb R^k: \lim_{n\rightarrow \infty} {}_{c}a_n = L \\
\end{aligned}
$$

---
### complete

- every cauchy sequence of complete metric space equal convergent sequence 

---
### complete formula

$$
\begin{aligned}
\forall \{_{c}a_n\} \subset X, \exists L \in X: \lim_{n \rightarrow \infty} {}_{c}a_n = L \\
\{_{c}a_n\} = \text{cauchy sequence} \\
X = \text{complete metric space} \\
L = \text{sequential limit} \\
\end{aligned}
$$

---
### monotonic

- increasing
- decreasing

---
### monotonic formula

$$
\begin{aligned}
\{a_n\}^+ \subset \mathbb R \leftrightarrow \forall n \in \mathbb N: a_n \le a_{n+1} \\
\{a_n\}^- \subset \mathbb R \leftrightarrow \forall n \in \mathbb N: a_n \ge a_{n+1} \\
\{a_n\}^+ = \text{monotonically increasing sequence} \\
\{a_n\}^- = \text{monotonically decreasing sequence} 
\end{aligned}
$$

---
### bounded monotonicity property

- every bounded monotonic sequence equal convergent sequence

---
### bounded monotonicity property formula

$$
\begin{aligned}
(\{a_n\} \subset X, \exists L \in X, \exists \epsilon > 0: B_{\epsilon}(L) \supset \{a_n\}) \land (\forall n \in \mathbb N: a_n \ge\le a_{n+1}) \rightarrow \lim_{n \rightarrow \infty} a_n = L \\
\{a_n\} = \text{sequence} \\
X = \text{metric space} \\
L = \text{sequential limit} \\
B = \text{open ball}
\end{aligned}
$$

---
### limit superior

- supremum of derived set of subsequence

---
### limit superior formula

$$
\begin{aligned}
S = \{L \in \mathbb R|\lim_{k\rightarrow \infty} a_{n_k} = L\} \rightarrow  \lim_{n\rightarrow \infty} \sup a_n = \sup S \\
S = \text{derived set} \\
\sup S = \text{limit superior}
\end{aligned}
$$

---
### limit inferior

- infimum of derived set of subsequence

---
### limit inferior formula

$$
\begin{aligned}
S = \{L \in \mathbb R|\lim_{k\rightarrow \infty} a_{n_k} = L\} \rightarrow \lim_{n\rightarrow \infty} \inf a_n = \inf S\\
S = \text{derived set} \\
\inf S = \text{limit inferior}
\end{aligned}
$$

---
### complete limit property

- membership
- eventual bound
- convergence

---
### complete limit property formula

$$
\begin{aligned}
\sup S, \inf S \in S \\
L > \sup S \rightarrow \exists N \in \mathbb N, \forall n \ge N: a_n < L \\
L < \inf S \rightarrow \exists N \in \mathbb N, \forall n \ge N: a_n > L \\
\lim_{n \rightarrow \infty} a_n = L \leftrightarrow \lim_{n\rightarrow \infty} \sup a_n = \lim_{n\rightarrow \infty} \inf a_n = L
\end{aligned}
$$

---
### sequential limit example

- infinite base versus power
- infinite rational power
- infinite power
- infinite exponential
- infinite base versus infinite power
- infinite logarithm versus infinite base

---
### sequential limit example formula

$$
\begin{aligned}
\lim_{n \rightarrow \infty} \frac{n^p}{n^q} = \begin{cases} 
0 \quad p < q \\
\infty \quad p > q \\
\end{cases} \\
p > 0 \rightarrow \lim_{n \rightarrow \infty} p^{1/n} = 1 \\
x \in \mathbb R \rightarrow \lim_{n \rightarrow \infty} x^{n} = \begin{cases} 
0 \quad |x| < 1 \\
\infty \quad x > 1 \\
\end{cases} \\ 
\lim_{n \rightarrow \infty} (1+\frac{x}{n})^n = e^x \\
a > 1 \rightarrow \lim_{n \rightarrow \infty} \frac{n^k}{a^n} = 0 \\
p > 0 \rightarrow \lim_{n \rightarrow \infty} \frac{\log n}{n^p} = 0
\end{aligned}
$$

---
