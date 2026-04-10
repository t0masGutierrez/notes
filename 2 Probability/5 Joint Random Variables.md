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
P(a \le X \le b, c \le Y \le d) = \sum_{i=a}^b \sum_{j=c}^d P(X = x_{i}, Y = y_{j}) \\  
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
P(X=x,Y=y) = 0 \\  
P(X,Y \in \mathbb{R}^2) = \int_{-\infty}^{\infty}\int_{-\infty}^{\infty} f_{X,Y}(x,y)dy dx = 1 \\  
P(X < a, Y \le b) = \int_{-\infty}^{a}\int_{-\infty}^{b} f_{X,Y}(x,y)dydx = F_{X,Y}(a, b) \\
P(a < X \le b, c \le Y \le d) = \int_{a}^b \int_{c}^d f_{X,Y}(x,y)dydx = F_{X,Y}(b,d) - \\
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
P(X \in A, Y \in B) = P(X \in A)P(Y \in B) \\
P(X = x, Y = y) = P(X = x)P(Y = y) \\
F_{X,Y}(x, y) = F_{X}(x)F_{Y}(y) \\
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
P(X \in A, Y \in B) = P(X \in A|Y \in B)P(Y \in B) \\
X, Y = \text{random variable} \\
x, y = \text{real number}
\end{aligned}
$$

---
### term
- definition

---
### term
- definition

---
