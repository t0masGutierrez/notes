### joint random variable
- function of sample space outcome equal real vector

---
### joint random variable formula
$$
\begin{aligned}
(X, Y): \Omega \rightarrow \mathbb R^2 \\
X(\omega), Y(\omega) = (x, y) \\
X, Y = \text{random variable} \\
\Omega = \text{sample space} \\
x, y = \text{real number} \\
\omega = \text{outcome}
\end{aligned}
$$

---
### joint cumulative distribution function
- cumulative probability as function of joint random variable
![](2%20Probability/Images/joint%20cumulative%20distribution%20function.png)

---
### joint cumulative distribution function formula
$$
\begin{aligned}
F_{X,Y}(x, y) = P(X \le x, Y \le y) \\
1 - F_{X}(x) - F_{Y}(y) + F_{X,Y}(x, y) = P(X > x, Y > y) \\
F_{X}(x) - F_{X, Y} = P(X \le x, Y > y) \\
F_{Y}(x) - F_{X, Y} = P(X > x, Y \le y) \\
\end{aligned}
$$

---
### joint probability mass function
- probability as function of joint discrete random variable

---
### joint probability mass function formula
$$
\begin{aligned}
P(a \le X \le b, c \le Y \le d) = \sum_{a\le x_{i} \le b} \sum_{c\le y_{i} \le d} P(X = x_{i}, Y = y_{j}) \\  
P(X \le x, Y \le y) = \sum_{x_{i}\le x}\sum_{y_{j}\le y} P(X = x_{i}, Y = y_{j}) \\
P(X, Y) = \sum_{i}\sum_{j} P(X = x_{i}, Y = y_{j}) = 1 \\  
P(X = x, Y = y) = P(X \le x, Y \le y) - \\
P(X \le x-1, Y \le y) - \\
P(X \le x, Y \le y-1) + \\
P(X \le x-1, Y \le y-1)
\end{aligned}
$$

---
### joint probability density function
- probability as function of joint continuous random variable

---
### joint probability density function formula
$$
\begin{aligned}
P(X=a,Y=b) = 0 \\  
P(X \in \mathbb{R},Y \in \mathbb{R}) = \int_{-\infty}^{\infty}\int_{-\infty}^{\infty} f_{X,Y}(x,y)dy dx = 1 \\  
P(X \le a, Y \le b) = \int_{-\infty}^{a}\int_{-\infty}^{b} f_{X,Y}(x,y)dydx = F_{X,Y}(a, b) \\
P(a \le X \le b, c \le Y \le d) = \int_{a}^b \int_{c}^d f_{X,Y}(x,y)dydx = F_{X,Y}(b,d) - \\
F_{X,Y}(a,d) - \\
F_{X,Y}(b,c) + \\
F_{X,Y}(a,c)
\end{aligned}
$$

---
### marginal probability mass function
- probability as function of single discrete random variable

---
### marginal probability mass function formula
$$
\begin{aligned}
P(X = x) = \sum_{y} P(X = x, Y = y) \\
P(Y=y) = \sum_{x} P(X = x, Y = y) \\
X, Y = \text{random variable} \\
x, y = \text{real number}
\end{aligned}
$$

---
### marginal probability density function
- probability as function of single continuous random variable

---
### marginal probability density function formula
$$
\begin{aligned}
f_{X}(x) = \int_{-\infty}^\infty f_{X,Y}(x, y)dy \\
f_{Y}(y) = \int_{-\infty}^\infty f_{X,Y}(x, y)dx \\
X, Y = \text{random variable} \\
x, y = \text{real number}
\end{aligned}
$$

---
### independent random variable
- 1st random variable cannot influence the outcome 2nd random variable

---
### independent random variable formula
$$
\begin{aligned}
P(X = x, Y = y) = P(X = x)P(Y = y) \\
f_{X,Y}(x, y) = f_{X}(x)f_{Y}(y) 
\end{aligned}
$$

---
### dependent random variable
- 1st random variable can influence the outcome 2nd random variable

---
### dependent random variable formula
$$
\begin{aligned}
P(X \in A, Y \in B) = P(X \in A\mid Y \in B)P(Y \in B) \\
X, Y = \text{random variable} \\
x, y = \text{real number}
\end{aligned}
$$

---
### conditional probability 
- likelihood random variable X will occur given random variable Y already occur

---
### conditional probability formula
$$
\begin{aligned}
P(X = x \mid Y = y) = \frac{P(X = x, Y = y)}{P(Y = y)} \\
f_{X\mid Y}(x \mid y) = \frac{f_{X,Y}(x, y)}{f_{Y}(y)}
\end{aligned}
$$

---
### conditional expectation
- mean of joint conditional random variable

---
### conditional expectation formula
$$
\begin{aligned}
E[X] = E(E[X \mid Y]) \\
X, Y = \text{random variable}
\end{aligned}
$$

---
### conditional variation
- variance of joint conditional random variable around mean

---
### conditional variation formula
$$
\begin{aligned}
\text{Var}(X) = E[\text{Var}(X\mid Y)] + \text{Var}(E[X\mid Y]) \\
X, Y = \text{random variable}
\end{aligned}
$$

---
### iid 
- independent and identically distributed

---
### iid formula
$$
\begin{aligned}
\forall i, j \in (1, \dots, m): P(X_{i} \in A, X_{j} \in B) = P(X_{i} \in A)P(X_{j} \in B) \\
\forall i \in (1, \dots, m): X_{i} \sim N(\mu, \sigma^2) \\
X, Y = \text{random variable} \\
m = \text{number of random variables} \\
N = \text{arbitrary probability distribution}
\end{aligned}
$$

---
### convolution
- probability as function of sum of independent random variable

---
### convolution formula
$$
\begin{aligned}
F_{X+Y}(z) = \int_{-\infty}^\infty F_{X}(z-y)f_{Y}(y)dy \\
F_{X+Y}(z) = \int_{-\infty}^\infty F_{Y}(z-x)f_{X}(x)dx \\
P(X + Y = z) = \sum_{x} P(X = x)P(Y = z-x) \\
f_{X+Y}(z) = \int_{-\infty}^\infty f_{X}(x)f_{Y}(z-x)dx \\
f_{X+Y}(z) = \int_{-\infty}^\infty f_{Y}(y)f_{X}(z-y)dy 
\end{aligned}
$$

---
### iid convolution expectation
- expectation of sum of iid random variable

---
### iid convolution expectation formula
$$
\begin{aligned}
E[\sum_{i=1}^n X_{i}] = n\mu \\
X = \text{random variable} \\
n = \text{number of random variables} \\
\mu = \text{mean}
\end{aligned}
$$

---
### iid convolution variation
- variation of sum of iid random variable

---
### iid convolution variation formula
$$
\begin{aligned}
\text{Var}(\sum_{i=1}^n X_{i}) = n\sigma^2 \\
X = \text{random variable} \\
n = \text{number of random variables} \\
\sigma = \text{standard deviation}
\end{aligned}
$$

---
