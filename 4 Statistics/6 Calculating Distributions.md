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
z = \frac{X - \mu}{\sigma} \\
X = \text{datum} \\
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
### t-score formula
$$
\begin{aligned}
t = \frac{\bar X - \mu}{s/\sqrt n} \\
\bar X = \text{sample mean} \\
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
T \sim S(t, \text{d}) = P(T \le t) \\
T \sim S(a, b, \text{d}) = P(a \le T \le b) \\
t = \text{t-score} \\
\text{d} = \text{degrees of freedom} \\
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
t = S^{-1}(c, \text{d}) \\
c = \text{cumulative probability of success} \\
\text{d} = \text{degrees of freedom}
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
X \sim \chi^2(x, \text{d}) = P(X \ge x) \\
x = \text{$\chi^2$-score} \\
\text{d} = \text{degrees of freedom} 
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
U \sim \chi^2(f, \text{d}_{1}, \text{d}_{2}) = P(U \le u) \\
V \sim \chi^2(v, \text{d}_{1}, \text{d}_{2}) = P(V \le v) \\
F = \frac{U/\text{d}_{1}}{V/\text{d}_{2}} \\
u, v = \text{F-score} \\
\text{d} = \text{degrees of freedom} 
\end{aligned}
$$

---
