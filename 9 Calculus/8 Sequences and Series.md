### sequence

- unordered collection of numbers

---
### sequence formula

$$
\begin{aligned}
\{a_n\}_{n = 1}^{\infty} = a_1, a_2, ... a_n ... \\
n = \text{index}
\end{aligned}
$$

---
### explicit function

- general term as function of index

---
### explicit function formula

$$
\begin{aligned}
a_n = f(n)
\end{aligned}
$$

---
### implicit function

- general term as function of preceding term(s)

---
### implicit function formula

$$
\begin{aligned}
a_{n + 1} = f(a_n)
\end{aligned}
$$

---
### arithmetic sequence

- add each term of sequence with common difference

---
### arithmetic sequence formula

$$
\begin{aligned}
a_n = a_1 + (n - 1)d \\
a_1 = \text{1st term} \\
d = \text{common difference}
\end{aligned}
$$

---
### geometric sequence

- multiply each term of sequence with common ratio

---
### geometric sequence formula

$$
\begin{aligned}
a_n = a_1r^{n - 1} \\
a_1 = \text{1st term} \\
r = \text{common ratio}
\end{aligned}
$$

---
### limit of sequence

- $a_n$ behavior as n approaches infinity
---
### limit of sequence formula

$$
\begin{aligned}
\lim_{n \to \infty} a_n = L \\
\lim_{n \to \infty} b_n = K
\end{aligned}
$$

---
### composite limit of sequence

- replace function argument with limit of sequence

---
### composite limit of sequence formula

$$
\begin{aligned}
\lim_{n \to \infty} a_n = L \land \lim_{n \to L} f(n) = L \to \lim_{n \to \infty} f(a_n) = f(L)
\end{aligned}
$$

---
### convergent sequence

- limit of sequence does exist

---
### divergent sequence

- limit of sequence does not exist

---
### squeeze theorem of sequence

- approximate limit by squeezing $f(n)$ between two functions 
- $g(n) ≤ f(n) ≤ h(n)$ for all *x* near *n*
- $\lim_{n \to \infty} g(n) = \lim_{n \to \infty} h(n) = L$
- if both conditions met then $\lim_{x \to n}f(x) = L$
---
### absolute value theorem of sequence

- absolute value of convergent sequence also converges but converse not always true

---
### absolute value formula of sequence

$$
\begin{aligned}
\lim_{n \to \infty} a_n = L \to \lim_{n \to \infty} |a_n| = |L|
\end{aligned}
$$

---
### increasing sequence

- every term greater than or equal preceding term

---
### increasing sequence formula

$$
\begin{aligned}
\forall (n \in N)(a_n \le a_{n + 1})
\end{aligned}
$$

---
### decreasing sequence

- every term less than or equal preceding term

---
### decreasing sequence formula

$$
\begin{aligned}
\forall (n \in N)(a_n \ge a_{n + 1})
\end{aligned}
$$

---
### monotone sequence

- sequence either increasing or decreasing

---
### monotone sequence formula

$$
\begin{aligned}
\forall (n \in N)(a_n \le a_{n + 1}) \lor \forall (n \in N)(a_n \ge a_{n + 1})
\end{aligned}
$$

---
### lower bound sequence

- every term greater than or equal some number

---
### lower bound sequence formula

$$
\begin{aligned}
\forall (n \in N)(a_n > m) \\
m = \text{lower bound}
\end{aligned}
$$

---
### upper bound sequence

- every term less than or equal some number

---
### upper bound sequence formula

$$
\begin{aligned}
\forall (n \in N)(a_n < M) \\
M = \text{upper bound}
\end{aligned}
$$

---
### bound sequence

- there exists upper bound and lower bound

---
### bound sequence formula

$$
\begin{aligned}
\exists (n \in N)(a_n > m) \land \exists (n \in N)(a_n < M)
\end{aligned}
$$

---
### bound monotone sequence theorem

- if bound monotone sequence then convergent sequence

---
### series

- sum of terms from sequence

---
### series formula

$$
\begin{aligned}
\sum_{n = 1}^{\infty} a_n = a_1 + a_2 + ... + a_n ... \\
n = \text{index}
\end{aligned}
$$

---
### nth partial sum

- sum of the first *n* terms from sequence

---
### nth partial sum formula

$$
\begin{aligned}
S_n = \sum_{k = 1}^{n} a_k = a_1 + a_2 + ... + a_n \\
n = \text{number of terms} \\
k = \text{index}
\end{aligned}
$$

---
### limit of nth partial sum

- $S_n$ behavior as *n* approaches infinity
---
### limit of nth partial sum formula

$$
\begin{aligned}
\lim_{n \to \infty} S_n = \lim_{n \to \infty} \sum_{k = 1}^{n} a_k = S 
\end{aligned}
$$

---
### convergent series

- limit of nth partial sum does exist

---
### convergent series formula

$$
\begin{aligned}
\lim_{n \to \infty} S_n = S \to \sum_{n = 1}^{\infty} a_n = S
\end{aligned}
$$

---
### divergent series

- limit of nth partial sum does not exist

---
### divergent series formula

$$
\begin{aligned}
\lim_{n \to \infty} S_n \ne S \to \sum_{n = 1}^{\infty} a_n \ne S
\end{aligned}
$$

---
### harmonic series

- sum of terms from harmonic sequence

---
### harmonic series formula

$$
\begin{aligned}
\sum_{n = 1}^{\infty} \frac{1}{n} = 1 + \frac{1}{2} + ... + \frac{1}{n} ...
\end{aligned}
$$

---
### geometric series

- sum of terms from geometric sequence

---
### geometric series formula

$$
\begin{aligned}
|r| < 1 \to \sum_{n = 1}^{\infty} a_1r^{n - 1} = \frac{a_1}{1-r} \\
|r| \ge 1 \to \sum_{n = 1}^{\infty} a_1r^{n - 1} \ne S \\
a_1 = \text{1st term} \\
r = \text{common ratio}
\end{aligned}
$$

---
### telescoping series

- series where most terms of nth partial sum cancel and some first terms and some last terms remain

---
### telescoping series formula

$$
\begin{aligned}
\sum_{n = 1}^{\infty} (a_n - a_{n + 1}) = a_1 - \lim_{n \to \infty} a_{n + 1} \\
\end{aligned}
$$

---
### convergent series theorem

- if $\sum_{n = 1}^{\infty} a_n$ converges then $\lim_{n \to \infty} a_n$ equal zero

---
### nth term divergence test

- contrapositive of convergent series theorem

---
### nth term divergence test formula

$$
\begin{aligned}
\lim_{n \to \infty} a_n \ne 0 \to \sum_{n = 1}^{\infty} a_n \ne S
\end{aligned}
$$

---
### integral test

- if integral converges then series converges and inverse
- $f(x)$ continuous, $f(x)$ positive, and $f(x)$ decreasing such that $\forall n f(n) = a_n$

---
### integral test formula

$$
\begin{aligned}
\int_n^{\infty} f(x)dx = S \to \sum_{n = 1}^{\infty} a_n = S \\
\int_n^{\infty} f(x)dx \ne S \to \sum_{n = 1}^{\infty} a_n \ne S
\end{aligned}
$$

---
### p series

- sum of terms from harmonic power sequence

---
### p series formula

$$
\begin{aligned}
p > 1 \to \sum_{n = 1}^{\infty} \frac{1}{n^p} = \frac{1}{1^p} + \frac{1}{2^p} + ... + \frac{1}{n^p} ... = S \\
p \le 1 \to \sum_{n = 1}^{\infty} \frac{1}{n^p} = \frac{1}{1^p} + \frac{1}{2^p} + ... + \frac{1}{n^p} ... \ne S \\
p = \text{power}
\end{aligned}
$$

---
### comparison test

- if larger series converges then smaller series converges
- if smaller series diverges then larger series diverges

---
### comparison test formula

$$
\begin{aligned}
\forall n(a_n \le b_n) \sum_{n=1}^\infty b_n = S \to \sum_{n=1}^\infty a_n = S \\
\forall n(a_n \le b_n) \sum_{n=1}^\infty a_n \ne S \to \sum_{n=1}^\infty b_n \ne S \\
\end{aligned}
$$

---
### limit comparison test

- if limit of series ratio does exist then both series either converge or diverge

---
### limit comparison test formula

$$
\begin{aligned}
\lim_{n \to \infty} \frac{a_n}{b_n} = 0 \le L \le \infty \to \sum_{n = 1}^{\infty} a_n, b_n = S \ \ \lor \sum_{n = 1}^{\infty} a_n, b_n \ne S \\
\lim_{n \to \infty} \frac{a_n}{b_n} = 0 \ \ \land \sum_{n = 1}^{\infty} b_n = S \to \sum_{n = 1}^{\infty} a_n = S \\
\lim_{n \to \infty} \frac{a_n}{b_n} = \infty \ \ \land \sum_{n = 1}^{\infty} b_n \ne S \to \sum_{n = 1}^{\infty} a_n \ne S
\end{aligned}
$$

---
### alternating series

- series whose terms alternate between positive and negative

---
### alternating series test

- if absolute value of non increasing terms approach zero then series converges
---
### alternating series test formula

$$
\begin{aligned}
\forall n(a_{n + 1} \le a_n) \land \lim_{n \to \infty} a_n = 0 \to \sum_{n = 1}^{\infty} a_n(-1)^{n + 1} = S \\
\end{aligned}
$$

---
### absolutely convergent series

- absolute value of series converges
- possible rearrangement of terms without changing sum of series

---
### conditionally convergent series

- series converges but absolute value of series diverges
- impossible rearrangement of terms without changing sum of series

---
### absolute convergence theorem

- if $\sum_{n = 1}^{\infty} |a_n|$ converges then $\sum_{n = 1}^{\infty} a_n$ converges
- if $\sum_{n = 1}^{\infty} a_n$ diverges then $\sum_{n = 1}^{\infty} |a_n|$ diverges

---
### ratio test

- if absolute value of series ratio $<1$ then series converges
- if absolute value of series ratio $>1$ then series diverges

---
### ratio test formula

$$
\begin{aligned}
\lim_{n \to \infty} |\frac{a_{n + 1}}{a_n}| < 1 \to \sum_{n = 1}^{\infty} a_n = S \\
\lim_{n \to \infty} |\frac{a_{n + 1}}{a_n}| > 1 \to \sum_{n = 1}^{\infty} a_n \ne S \\
\lim_{n \to \infty} |\frac{a_{n + 1}}{a_n}| = 1 \to \sum_{n = 1}^{\infty} a_n = \ ? \\
\end{aligned}
$$

---
### root test

- if absolute value of series nth root $<1$ then series converges
- if absolute value of series nth root $>1$ or equal $\infty$ then series diverges

---
### root test formula

$$
\begin{aligned}
\lim_{n \to \infty} |\sqrt[n]{a_n}| < 1 \to \sum_{n = 1}^{\infty} a_n = S \\
\lim_{n \to \infty} |\sqrt[n]{a_n}| > 1 \ \ \lor \lim_{n \to \infty} |\sqrt[n]{a_n}| = \infty \to \sum_{n = 1}^{\infty} a_n \ne S \\
\lim_{n \to \infty} |\sqrt[n]{a_n}| =<= 1 \to \sum_{n = 1}^{\infty} a_n = ? \\
\end{aligned}
$$

---
### test summary

- divergence
- geometric series
- telescoping series
- p series
- alternating series
- integral
- root
- ratio
- comparison
- limit comparison
---
### taylor polynomial

- polynomial approximation of $f(x)$ about point *c* by finitely summing derivatives of $f(x)$
- higher degree polynomials better approximate $f(x)$ 
---
### taylor polynomial formula

$$
\begin{aligned}
P_n(x) = f(c) + f'(c)(x - c) + \frac{f''(c)}{2!}(x - c)^2 + ... + \frac{f^{n'}(c)}{n!}(x - c)^n \\
c = \text{center}
\end{aligned}
$$

---
### mclaurin polynomial

- polynomial approximation of $f(x)$ about point 0 by finitely summing derivatives of $f(x)$

---
### mclaurin polynomial formula

$$
\begin{aligned}
P_n(x) = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + ... + \frac{f^{n'}(0)}{n!}x^n \\
c = 0
\end{aligned}
$$

---
### power series

- series of powers

---
### power series formula

$$
\begin{aligned}
f(x) = \sum_{n = 1}^{\infty} a_n(x - c)^n
\end{aligned}
$$

---
### domain of power series

- set of all *x* where power series converges
---
### power series convergence theorem

- series converges for all *x* 
- series converges for $|x - c| < R$ 
- series converges for $x = c$ 

---
### interval of convergence

- interval about center where power series converges including endpoint(s)
---
### radius of convergence

- $\pm$ number about center where power series converges
---
### calculate radius of convergence

- ratio test or root test
- if radius of convergence equal finite number then test endpoint convergence
---
### endpoint convergence

- substitute $x = c \pm R$ into power series
- simplify power series into the form $\sum_{n = 1}^{\infty} a_n$
- apply series test
- if series converges at endpoint then close interval 

---
### power series differentiation property

$$
\begin{aligned}
f'(x) = \sum_{n = 1}^\infty [n a_n(x - c)^{n - 1}] \\
\end{aligned}
$$

---
### power series integration property

$$
\begin{aligned}
\int f(x)dx = \sum_{n = 1}^\infty [\frac{a_n}{n + 1}(x - c)^{n+1}]
\end{aligned}
$$

---
### operations with power series

- constant multiple
- power
- sum difference
---
### function conversion power series

- replace function with power series

---
### function conversion power series formula

- harmonic
- geometric
- natural logarithm
- natural exponential
- sine
- cosine
- arctangent
- arcsine
- binomial
---
### taylor series

- polynomial approximation of $f(x)$ about point *c* by infinitely summing derivatives of $f(x)$

---
### taylor series formula

$$
\begin{aligned}
P_n(x) = \sum_{n = 1}^\infty \frac{f^{n'}(c)}{n!}(x - c)^n \\
c = \text{center}
\end{aligned}
$$

---
