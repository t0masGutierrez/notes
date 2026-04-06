### standardization
- convert from random variable to standardized random variable

---
### standardization formula
$$
\begin{aligned}
(X = x) \sim (\mu, \sigma) \implies (Y = y) \sim (\mu', \sigma ') \\
X = \text{random variable} \\
x = \text{real number} \\
Y = \text{standardized random variable} \\
y = \text{y-score}
\end{aligned}
$$

---
### normal
- probability as function of mean and standard deviation

---
### normal formula
$$
\begin{aligned}
X \sim N(x, \mu, \sigma) = P(X \le x) \\
X \sim N(a, b, \mu, \sigma) = P(a \le X \le b) \\
x = \text{number of successes} \\
\mu = \text{mean} \\
\sigma = \text{standard deviation} \\
a = \text{lower number of successes} \\
b = \text{upper number of successes} 
\end{aligned}
$$

---
### inverse normal
- value of random variable as function of cumulative distribution function

---
### inverse normal formula
$$
\begin{aligned}
x= N^{-1}(c, \mu, \sigma, \text{tail}) \\
c = \text{cumulative probability of success} \\
\mu = \text{mean} \\
\sigma = \text{standard deviation} \\
\text{tail} = \text{direction of accumulation}
\end{aligned}
$$

---
### z-score
- number of standard deviations from the mean

---
### z-score formula
$$
\begin{aligned}
z = \frac{x - \mu}{\sigma} \\
x = \text{datum} \\
\mu = \text{mean} \\
\sigma = \text{standard deviation}
\end{aligned}
$$

---
### standard normal
- probability as function of z-score

---
### standard normal formula
$$
\begin{aligned}
Z \sim N(x, 0, 1) = P(Z \le z) \\
Z \sim N(a, b, 0, 1) = P(a \le Z \le b) \\
z = \text{z-score} \\
a = \text{lower z-score} \\
b = \text{upper z-score}
\end{aligned}
$$

---
### inverse standard normal
- z-score as function of cumulative distribution function

---
### inverse standard normal formula
$$
\begin{aligned}
z = N^{-1}(c, 0, 1, \text{tail}) \\
c = \text{cumulative probability of success} \\
\text{tail} = \text{direction of accumulation}
\end{aligned}
$$

---
### t-score
- number of standard errors from the mean

---
### one sample t-score formula
$$
\begin{aligned}
t = \frac{\bar x - \mu}{s/\sqrt n} \\
\bar x = \text{sample mean} \\
\mu = \text{mean} \\
\sigma = \text{standard deviation}
\end{aligned}
$$

---
### two sample independent t-score formula
$$
\begin{aligned}
t = \frac{\bar x - \mu}{s/\sqrt n} \\
\bar x = \text{sample mean} \\
\mu = \text{mean} \\
\sigma = \text{standard deviation}
\end{aligned}
$$

---
### two sample dependent t-score formula
$$
\begin{aligned}
t = \frac{(\bar x_{1} - \bar x_{2}) - \mu}{s/\sqrt n} \\
\bar x = \text{sample mean} \\
\mu = \text{mean} \\
\sigma = \text{standard deviation}
\end{aligned}
$$

---
### student
- probability as function of t-score

---
### student formula
$$
\begin{aligned}
T \sim S(t, d) = P(T \le t) \\
T \sim S(a, b, d) = P(a \le T \le b) \\
t = \text{t-score} \\
d = \text{degrees of freedom} \\
a = \text{lower t-score} \\
b = \text{upper t-score} 
\end{aligned}
$$

---
### inverse student
- t-score as function of cumulative distribution function

---
### inverse student formula
$$
\begin{aligned}
t = S^{-1}(c, d) \\
c = \text{cumulative probability of success} \\
d = \text{degrees of freedom}
\end{aligned}
$$

---
### chi-square-score
- ratio between sample variance and population variance

---
### chi-square-score formula
$$
\begin{aligned}
\chi^2 = \frac{(n-1)s^2}{\sigma^2} \\
n = \text{sample size} \\
s = \text{sample standard deviation} \\
\sigma = \text{standard deviation}
\end{aligned}
$$

---
### chi-square
- probability as function of $\chi^2$-score

---
### chi-square formula
$$
\begin{aligned}
X \sim \chi^2(x,d) = P(X \ge x) \\
x = \text{$\chi^2$-score} \\
d = \text{degrees of freedom} 
\end{aligned}
$$

---
### F-score
- ratio between group mean square and error mean square

---
### F-score formula
$$
\begin{aligned}
F = \frac{MS_{\text{group}}}{MS_{\text{error}}} \\
MS = \text{mean square} 
\end{aligned}
$$

---
### F
- probability as function of F-score

---
### F formula
$$
\begin{aligned}
U \sim \chi^2(f, d_{1}, d_{2}) = P(U \le u) \\
V \sim \chi^2(v, d_{1}, d_{2}) = P(V \le v) \\
F = \frac{U/d_{1}}{V/d_{2}} \\
u, v = \text{F-score} \\
d = \text{degrees of freedom} 
\end{aligned}
$$

---
