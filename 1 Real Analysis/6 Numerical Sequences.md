### sequence
- infinite list of ordered terms

---
### sequence formula
$$
\begin{aligned}
\{a_{n}\}_{n=1}^{\infty} = a: \mathbb N \rightarrow S \\
n \mapsto a_{n} \\
a_{n} = \text{term} \\
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
\exists L \in X: \lim_{n \rightarrow \infty}a_{n} = L \iff \forall \epsilon > 0, \exists N \in \mathbb N, \forall n \ge N: d(a_{n}, L) < \epsilon \\
\set {a_{n}} = \text{convergent sequence} \\
L = \text{sequential limit} 
\end{aligned}
$$

---
### divergent
- there exists no limit of sequence

---
### divergent formula
$$
\begin{aligned}
\not\exists L \in X: \lim_{n \rightarrow \infty}a_{n} = L \iff \exists \epsilon > 0, \forall N \in \mathbb N, \exists n \ge N: d(a_{n}, L) \ge \epsilon \\
\set {a_{n}} = \text{divergent sequence} \\
L = \text{sequential limit}
\end{aligned}
$$

---
### subsequence
- infinite sublist of ordered terms

---
### subsequence formula
$$
\begin{aligned}
\{a_{n_{k}}\}_{k=1}^{\infty} = a \circ n: \mathbb N \rightarrow S \\
k \mapsto a_{n_{k}} \\
\forall k \in \mathbb N: n_{k} < n_{k+1}  \\
\{a_{n_{k}}\} = \text{subsequence} 
\end{aligned}
$$

---
### cauchy
- all terms of cauchy sequence are eventually close

---
### cauchy formula
$$
\begin{aligned}
\forall \epsilon > 0, \exists N \in \mathbb N, \forall n, m \ge N: d(a_{n}, a_{m}) < \epsilon \\
\{_{c}a_{n}\} = \text{cauchy sequence}
\end{aligned}
$$

---
### complete
- every cauchy sequence of complete metric space equal convergent sequence 

---
### complete formula
$$
\begin{aligned}
\forall \{_{c}a_{n}\} \subset X, \exists L \in X: \lim_{n \rightarrow \infty} {}_{c}a_{n} = L \\
\{_{c}a_{n}\} = \text{cauchy sequence} \\
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
\{a_{n}\}^+ \subset \mathbb R \iff \forall n \in \mathbb N: a_{n} \le a_{n+1} \\
\{a_{n}\}^- \subset \mathbb R \iff \forall n \in \mathbb N: a_{n} \ge a_{n+1} \\
\{a_{n}\}^+ = \text{monotonically increasing sequence} \\
\{a_{n}\}^- = \text{monotonically decreasing sequence} 
\end{aligned}
$$

---
### limit superior
- supremum of derived set of subsequence

---
### limit superior formula
$$
\begin{aligned}
S = \{L \in \mathbb R|\lim_{k\rightarrow \infty} a_{n_{k}} = L\} \implies  \lim_{n\rightarrow \infty} \sup a_{n} = \sup S \\
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
S = \{L \in \mathbb R|\lim_{k\rightarrow \infty} a_{n_{k}} = L\} \implies \lim_{n\rightarrow \infty} \inf a_{n} = \inf S\\
S = \text{derived set} \\
\inf S = \text{limit inferior}
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
\lim_{n \rightarrow \infty} a_{n} = L \iff \forall \epsilon> 0, \exists N \in \mathbb N, \forall n \ge N: a_{n} \in N_{\epsilon}(L) \\
(\lim_{n \rightarrow \infty} a_{n} = L) \land (\lim_{n \rightarrow \infty} a_{n} = L') \implies L = L' \\
\lim_{n \rightarrow \infty} a_{n} = L \implies \{a_{n}\} \subset X, \exists \epsilon > 0: \{a_{n}\} \subset B_{\epsilon}(L) \\
(S \subset X) \land (L \in S') \implies \exists \{a_{n}\} \in S: \lim_{n \rightarrow \infty} a_{n} = L
\end{aligned}
$$

---
### limit property
- distance between $n$th term and limit approaches zero as $n$ approaches infinity

---
### limit property formula
$$
\begin{aligned}
\lim_{n \rightarrow \infty} a_{n} = L \implies \lim_{n \rightarrow \infty} d(a_{n}, L) = 0 \\
\set {a_{n}} = \text{sequence} \\
L = \text{sequential limit}
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
(a_{n}, b_{n} \in \mathbb C) \land (\lim_{n \rightarrow \infty}a_{n} = L) \land (\lim_{n \rightarrow \infty}b_{n} = K) \implies \lim_{n \rightarrow \infty}(a_{n} + b_{n}) = L + K \\
(a_{n}, b_{n} \in \mathbb C) \land (\lim_{n \rightarrow \infty}a_{n} = L) \land (\lim_{n \rightarrow \infty}b_{n} = K) \implies \lim_{n \rightarrow \infty}(a_{n} \cdot b_{n}) = L \cdot K \\
(a_{n} \in \mathbb C) \land (c \in \mathbb R) \land (\lim_{n \rightarrow \infty}a_{n} = L) \implies \lim_{n \rightarrow \infty}ca_{n} = c \cdot L \\
(a_{n} \in \mathbb C) \land (c \in \mathbb R) \land (\lim_{n \rightarrow \infty}a_{n} = L) \implies \lim_{n \rightarrow \infty}(c + a_{n}) = c + L \\
(a_{n} \in \mathbb C) \land (\lim_{n \rightarrow \infty}a_{n} = L) \implies \lim_{n \rightarrow \infty} \frac{1}{a_{n}} = \frac{1}{L} \\
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
(\vec x_{n}, \vec y_{n} \in \mathbb R^k) \land (\lim_{n \rightarrow \infty} \vec x_{n} = L) \land (\lim_{n \rightarrow \infty} \vec y_{n} = K) \implies \lim_{n \rightarrow \infty} (\vec x_{n} + \vec y_{n}) = L + K \\
(\vec x_{n}, \vec y_{n} \in \mathbb R^k) \land (\lim_{n \rightarrow \infty} \vec x_{n} = L) \land (\lim_{n \rightarrow \infty} \vec y_{n} = K) \implies \lim_{n \rightarrow \infty} (\vec x_{n} \cdot \vec y_{n}) = L \cdot K \\
(\vec x_{n} \in \mathbb R^k) \land (a_{n} \in \mathbb R) \land (\lim_{n \rightarrow \infty} \vec x_{n} = L) \land (\lim_{n \rightarrow \infty} a_{n} = K) \implies \lim_{n \rightarrow \infty} (a_{n} \cdot \vec x_{n}) = K \cdot L \\
(\vec a_{n} = [\alpha_{1n}, \dots, \alpha_{kn}]) \land (L = [\alpha_{1}, \dots, \alpha_{k}]) \land (\lim_{n \rightarrow \infty} \vec a_{n} = L) \iff \forall j \le k: \lim_{n \rightarrow \infty} \alpha_{jn} = \alpha_{j} 
\end{aligned}
$$

---
### closed subsequence property
- derived set of subsequence equal closed set

---
### closed subsequence property formula
$$
\begin{aligned}
S = \{L | \lim_{k\rightarrow \infty} a_{n_{k}} = L\} \implies S' \subset S \subset X \\
S = \text{closed set} \\
S' = \text{derived set} \\
L = \text{subsequential limit} \\
\set {a_{n_{k}}} = \text{subsequence} \\
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
\lim_{n \rightarrow \infty} a_{n} = L \implies \forall \epsilon > 0, \exists K \in \mathbb N, \forall n_{k} \ge n_{K} \ge N: d(a_{n_{k}}, L) < \epsilon \\
\set {a_{n}} = \text{convergent sequence} \\
L = \text{sequential limit} \\
\set {{a_{n_{k}}}} = \text{convergent subsequence} \\
\end{aligned}
$$

---
### cauchy property
- every convergent sequence of metric space equal cauchy sequence
- every cauchy sequence of compact set equal convergent sequence
- every cauchy sequence of k-dimensional real numbers equal convergent sequence

---
### cauchy property formula
$$
\begin{aligned}
\exists L \in X: \lim_{n\rightarrow \infty} a_{n} = L \implies \{a_{n}\} = \{_{c}a_{n}\} \\
\forall \set{Y_{i}} \subset X, \exists \{Y_{i_{1}}, \dots Y_{i_{n}}\} \subset \{Y_{i}\}: X \subset \bigcup_{k=1}^n Y_{i_{k}} \implies \forall \{_{c}a_{n}\} \subset X, \exists L \in X: \lim_{n\rightarrow \infty} {}_{c}a_{n} = L \\
\forall \{_{c}a_{n}\} \subset \mathbb R^k, \exists L \in \mathbb R^k: \lim_{n\rightarrow \infty} {}_{c}a_{n} = L \\
\end{aligned}
$$

---
### bounded monotonicity property
- every bounded monotonic sequence equal convergent sequence

---
### bounded monotonicity property formula
$$
\begin{aligned}
(\{a_{n}\} \subset X, \exists L \in X, \exists \epsilon > 0: B_{\epsilon}(L) \supset \{a_{n}\}) \land (\forall n \in \mathbb N: a_{n} \ge\le a_{n+1}) \implies \lim_{n \rightarrow \infty} a_{n} = L \\
\{a_{n}\} = \text{sequence} \\
X = \text{metric space} \\
L = \text{sequential limit} \\
B = \text{open ball}
\end{aligned}
$$

---
### limit exterior property
- membership
- eventual bound
- convergence

---
### limit exterior property formula
$$
\begin{aligned}
\sup S, \inf S \in S \\
L > \sup S \implies \exists N \in \mathbb N, \forall n \ge N: a_{n} < L \\
L < \inf S \implies \exists N \in \mathbb N, \forall n \ge N: a_{n} > L \\
\lim_{n \rightarrow \infty} a_{n} = L \iff \lim_{n\rightarrow \infty} \sup a_{n} = \lim_{n\rightarrow \infty} \inf a_{n} = L
\end{aligned}
$$

---
