### joint expectation
- mean of joint random variable

---
### joint expectation formula
$$
\begin{aligned}
E[g(X, Y)] = \sum_{x} \sum_{y} g(x, y)P(X = x, Y = y) \\
E[g(X, Y)] = \int_{-\infty}^\infty \int_{-\infty}^\infty g(x, y)f(x, y)dydx \\
X, Y = \text{random variable} \\
x, y = \text{real number}
\end{aligned}
$$

---
### expectation multiplication property
- expectation of independent product equal product of expectation

---
### expectation addition property formula
$$
\begin{aligned}
P(X \in A, Y \in B) = P(X \in A)P(Y \in B) \implies E[XY] = E[X]E[Y] \\
X, Y = \text{random variable} \\
\end{aligned}
$$

---
### joint variation
- variance of joint random variable around mean

---
### joint variation formula
$$
\begin{aligned}
\text{Var}(X, Y) = \begin{bmatrix} \text{Var}(X) & \text{Cov}(X, Y) \\
\text{Cov}(Y, X) & \text{Var}(Y) \end{bmatrix} \\
X, Y = \text{random variable}
\end{aligned}
$$

---
### variation addition property
- variance of random variable equal sum of joint variance of two random variable

---
### variation addition property formula
$$
\begin{aligned}
\text{Var}(X+Y) = \text{Var}(X) + \text{Var}(Y) + 2\text{Cov}(X, Y) \\
X, Y = \text{random variable}
\end{aligned}
$$

---
### covariation
- joint variance of two random variable around mean

---
### covariation formula
$$
\begin{aligned}
\text{Cov}(X, Y) = E[(X - E[X])(Y - E[Y])] = E[XY] - E[X]E[Y] \\

\end{aligned}
$$

---
### covariation property
- symmetry
- identity
- linearity
- independence

---
### covariation property formula
$$
\begin{aligned}
\text{Cov}(X, Y) = \text{Cov}(Y, X) \\
\text{Cov}(X, X) = \text{Cov}(X) \\
\text{Cov}(aX + bY, Z + c) = a \text{Cov}(X, Z) + b\text{Cov}(Y, Z) \\
P(X \in A, Y \in B) = P(X \in A)P(Y \in B) \implies \text{Cov}(X, Y) = 0 
\end{aligned}
$$

---
### term
- definition

---
### term
- definition

---
### term
- definition

---
