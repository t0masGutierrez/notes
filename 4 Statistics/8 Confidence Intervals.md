### estimator
- sample statistic capable of estimating the value of population parameter

---
### biased estimator
- mean of sample statistic not equal population parameter

---
### biased estimator formula
$$
\begin{aligned}
E[T] \ne \mathcal T \\
T = \text{sample statistic} \\
\mathcal T = \text{population parameter}
\end{aligned}
$$

---
### unbiased estimator
- mean of sample statistic equal population parameter

---
### unbiased estimator formula
$$
\begin{aligned}
E[T] = \mathcal T \\
T = \text{sample statistic} \\
\mathcal T = \text{population parameter}
\end{aligned}
$$

---
### critical value
- boundary point on probability distribution between rejection region and non-rejection region

---
### critical value formula
$$
\begin{aligned}
T < c^*_{L} \implies \text{reject} \\
T > |c^*_{2}| \implies \text{reject} \\
T > c^*_{R} \implies \text{reject} \\
\end{aligned}
$$

---
### critical z-value
- boundary point on normal distribution between rejection region and non-rejection region
---
### critical z-value formula
$$
\begin{aligned}
z^*_{L} = N^{-1}(\alpha, 0, 1) \\
z^*_{2} = N^{-1}(1-\frac{\alpha}{2}, 0, 1) \\
z^*_{R} = N^{-1}(1-\alpha, 0, 1) \\
\alpha = \text{significance level}
\end{aligned}
$$

---
### critical t-value
- boundary point on student distribution between rejection region and non-rejection region

---
### critical t-value formula
$$
\begin{aligned}
t_* = \frac{\bar X - \mu}{\frac{\sigma}{\sqrt n}} \\
\bar X = \text{sample mean} \\
\mu = \text{mean} \\
\sigma = \text{standard deviation} \\
n = \text{sample size}
\end{aligned}
$$

---
### critical chi-square-value
- boundary point on chi-square distribution between rejection region and non-rejection region
---
### critical chi-square-value formula
$$
\begin{aligned}
\chi_*^2 = \frac{(n-1)s^2}{\sigma^2} \\
n = \text{sample size} \\
s = \text{sample standard deviation} \\
\sigma = \text{standard deviation}
\end{aligned}
$$

---
### confidence interval
- range of guesses for the population parameter

---
### confidence interval formula
$$
\begin{aligned}
CI = T \pm (c^*)(SE) \\
T = \text{sample statistic} \\
c^* = \text{critical value} \\
SE = \text{standard error}
\end{aligned}
$$

---
### mean confidence interval formula
$$
\begin{aligned}
CI=\bar X \pm z^*(\frac{\sigma}{\sqrt n}) \\
CI=\bar X \pm t^*(\frac{s}{\sqrt n}) \\
\bar X = \text{mean} \\
z^*, t^* = \text{critical value} \\
\sigma = \text{standard deviation} \\
s = \text{sample standard deviation} \\
n = \text{sample size}
\end{aligned}
$$

---
### proportion confidence interval formula
$$
\begin{aligned}
CI=\hat p \pm z^* \sqrt {\frac{\hat p(1-\hat p)}{n}} \\
\hat p = \text{sample proportion} \\
z^* = \text{critical value} \\
n = \text{sample size}
\end{aligned}
$$

---
### standard deviation confidence interval formula
$$
\begin{aligned}
CI=\sqrt{\frac{(n-1)s^2}{\chi^2_{\alpha/2}}} \leq \sigma \leq \sqrt{\frac{(n-1)s^2}{\chi^2_{1-\alpha/2}}} \\
n = \text{sample size} \\
s = \text{sample standard deviation} \\
\chi^2_* = \text{critical value}
\end{aligned}
$$

---
### correct confidence interval
- 95% confidence that the population parameter lie inside the confidence interval

---
### incorrect confidence interval
- 95% chance that the population parameter lie outside the critical region
- 95% of sample statistic lie between lower boundary and upper boundary

---
### confidence level
- probability of the population parameter lying inside the confidence interval
---
### confidence level formula
$$
\begin{aligned}
\text{1-tail CI} = 1-2\alpha \\
\text{2-tail CI} = 1-\alpha \\
\alpha = \text{significance level}
\end{aligned}
$$

---
### margin of error
- maximum likely amount of error between statistic and parameter

---
### margin of error formula
$$
\begin{aligned}
E = (c^*)(SE) \\
c^* = \text{critical value} \\
SE = \text{standard error}
\end{aligned}
$$

---
### sample size
- number of observations as function of margin of error

---
### mean sample size formula
$$
\begin{aligned}
n = (\frac{z^*\sigma}{E})^2 \\
z^* = \text{critical z-value} \\
\sigma = \text{standard deviation} \\
E = \text{margin of error}
\end{aligned}
$$

---
### known proportion sample size formula
$$
\begin{aligned}
n = (\frac{z^*\sqrt {p(1- p)}}{E})^2 \\
z^* = \text{critical z-value} \\
p = \text{proportion} \\
E = \text{margin of error}
\end{aligned}
$$

---
### unknown proportion sample size formula
$$
\begin{aligned}
n = (\frac{0.5z^*}{E})^2 \\
p = 0.5 \\
z^* = \text{critical z-value} \\
p = \text{proportion} \\
E = \text{margin of error}
\end{aligned}
$$

---
### degrees of freedom
- number of sample data that can vary without changing estimate

---
### degrees of freedom formula
$$
\begin{aligned}
\text{d} = n-1 \\
n = \text{sample size}
\end{aligned}
$$

---
### point estimate
- single best guess for the population parameter

---
### point estimate formula
$$
\begin{aligned}
T \approx \mathcal T \\
T = \text{sample statistic} \\
\mathcal T = \text{population parameter} \\
\end{aligned}
$$

---
### sample mean
- point estimate of population mean

---
### mean confidence interval assumptions
- random sample
- independent observations
- normal population and large sample size
---
### construct mean confidence interval
- compute sample proportion
- compute standard error
- find critical value from confidence level
- compute margin of error
- $\bar X - E < \mu < \bar X + E$ 

---
### sample proportion
- point estimate of population proportion

---
### proportion confidence interval assumptions
- random sample
- independent trials
- sufficient number of observations $n\hat p, n\hat q \ge 10$ 

---
### construct proportion confidence interval
- compute sample proportion
- compute standard error
- find critical value from confidence level
- compute margin of error
- $\hat p - E < p < \hat p + E$ 

---
### sample standard deviation
- point estimate of population standard deviation

---
### standard deviation confidence interval requirements
- random samples
- independent trials
- normal population

---
### construct variance confidence interval
- compute sample variance
- compute standard error
- find both critical values from confidence level
- compute margin of error
- $\sqrt{\frac{(n-1)s^2}{\chi^2_{\alpha/2}}} \leq \sigma \leq \sqrt{\frac{(n-1)s^2}{\chi^2_{1-\alpha/2}}}$ 

---
### mean z-interval formula
$$
\begin{aligned}
\text{avgZ-int}(\sigma, \bar X, n, 1-\alpha) \\
\sigma = \text{standard deviation} \\
\bar X = \text{sample mean} \\
n = \text{sample size} \\
\alpha = \text{significance level}
\end{aligned}
$$

---
### mean t-interval formula
$$
\begin{aligned}
\text{avgZ-int}(\bar X, s, n, 1-\alpha) \\
\sigma = \text{standard deviation} \\
\bar X = \text{sample mean} \\
n = \text{sample size} \\
\alpha = \text{significance level}
\end{aligned}
$$

---
### proportion z-interval formula
$$
\begin{aligned}
\text{propZ-int}(x, n, 1-\alpha) \\
x = \text{number of successes} \\
n = \text{sample size} \\
\alpha = \text{significance level}
\end{aligned}
$$

---
