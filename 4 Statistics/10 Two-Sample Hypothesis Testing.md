### 1-sample hypothesis test
- compare sample statistic with population parameter

---
### 2-sample hypothesis test
- compare population parameter between group 1 and group 2

---
### independent sample
- there exists no meaningful relationship between group 1 and group 2

---
### dependent sample
- there exists meaningful relationship between group 1 and group 2

---
### null hypothesis
- difference of population parameter equal zero  
- statement of equality

---
### null hypothesis formula
$$
\begin{aligned}
H_{0}: \mu_{1}-\mu_{2} = 0 \\
H_{0}: p_{1}-p_{2} = 0 \\
\end{aligned}
$$

---
### alternative hypothesis
- difference of population parameter not equal zero
- statement of inequality

---
### alternative hypothesis formula
$$
\begin{aligned}
H_{a}: \mu_{1} - \mu_{2} \ne 0 \\
H_{a}: p_{1} - p_{2} \ne 0 
\end{aligned}
$$

---
### standard error
- standard deviation of sampling distribution

---
### mean difference standard error formula
$$
\begin{aligned}
SE(\bar X_{1} - \bar X_{2}) = \sqrt{\frac{s^2}{n_{1}} + \frac{s^2}{n_{2}}} \\
s = \text{sample standard deviation} \\
n = \text{sample size}
\end{aligned}
$$

---
### proportion difference standard error formula
$$
\begin{aligned}
SE(\hat p_{1} - \hat p_{2}) = \sqrt{\frac{\hat p_{1}(1-\hat p_{1})}{n_{1}} + \frac{\hat p_{2}(1-\hat p_{2})}{n_{2}}} \\
\hat p = \text{sample proportion} \\
n = \text{sample size}
\end{aligned}
$$

---
### sample proportion
- point estimate of population proportion

---
### construct two proportion independent confidence interval
- compute sample proportion
- compute standard error
- find critical value
- compute margin of error
- $(\hat p_{1} - \hat p_{2}) - E < (\hat p_{1} - \hat p_{2}) < (\hat p_{1} - \hat p_{2}) + E$ 

---
### two proportion independent z-interval formula
$$
\begin{aligned}
\text{2propZ-int}(X_{1}, n_{1}, X_{2}, n_{2}, 1-\alpha) \\
X= \text{number of successes} \\
n = \text{sample size} \\
\alpha = \text{significance level}
\end{aligned}
$$

---
### conduct two proportion independent hypothesis test
- state hypotheses
- choose significance level  
- calculate test statistic  
- choose method
- reject or fail to reject null hypothesis  
- state conclusion

---
### two proportion independent z-test formula
$$
\begin{aligned}
\text{2propZ-test}(X_{1}, n_{1}, X_{2}, n_{2}, p_{1}) \\
X= \text{number of successes} \\
n = \text{sample size} \\
p_{1} = \text{alternative hypothesis}
\end{aligned}
$$

---
### sample mean
- point estimate of population mean

---
### construct two mean independent confidence interval
- compute sample mean
- compute standard error
- find critical value from confidence level
- compute margin of error
- $(\bar X_{1} - \bar X_{2}) - E < (\mu_{1} - \mu_{2}) < (\bar X_{1} - \bar X_{2}) + E$ 

---
### two mean independent t-interval formula
$$
\begin{aligned}
\text{2avgT-int}(\bar X_{1}, s_{1}, n_{1}, \bar X_{2}, s_{2}, n_{2}, \alpha, \text{pool}) \\
\bar X= \text{sample mean} \\
s = \text{sample standard deviation} \\
n = \text{sample size} \\
\alpha = \text{significance level} \\
\text{pool} = \text{if equal then yes}
\end{aligned}
$$

---
### conduct two mean independent hypothesis test
- definition

---
### two mean independent t-test formula
$$
\begin{aligned}
\text{2avgT-test}(\bar X_{1}, s_{1}, n_{1}, \bar X_{2}, s_{2}, n_{2}, \mu_{1} = \mu_{2}, \text{pool}) \\
\bar X= \text{sample mean} \\
s = \text{sample standard deviation} \\
n = \text{sample size} \\
\text{pool} = \text{no}
\end{aligned}
$$

---
### pool variance
- combination of two sample variance into single sample variance 
- population variance unknown and equal

---
### pool variance formula
$$
\begin{aligned}
s_{p}^2 = \frac{(n_{1} - 1)s_{1}^2 + (n_{2}-1)s_{2}^2}{n_{1}+n_{2}-2} \\
n = \text{sample size} \\
s = \text{sample standard deviation}
\end{aligned}
$$

---
### construct two mean dependent confidence interval
- find critical value  
- calculate margin of error
- $\Delta \bar X - E < µ < \Delta \bar X + E$ 

---
### two mean dependent t-interval formula
$$
\begin{aligned}
\text{2avgT-Int}(\text{data}, L_{3}, f, \alpha) \\
\end{aligned}
$$

---
### conduct two mean dependent hypothesis test
- definition

---
### two mean dependent t-test formula
$$
\begin{aligned}
\text{2avgT-Test} (\text{data}, \mu_{0}, L_{3}, f, \mu_{1})
\end{aligned}
$$

---
### sample variance
- point estimate of population variance

---
### construct two variance dependent confidence interval
- definition

---
### two variance dependent F-int formula
$$
\begin{aligned}
\text{2varF-Int}() 
\end{aligned}
$$

---
### conduct two variance dependent hypothesis test
- definition

---
### two variance dependent F-test formula
$$
\begin{aligned}
\text{2varF-Test}(s, n, \sigma_{1}) \\
s = \text{sample standard deviation} \\
n = \text{sample size} \\
\sigma_{1} = \text{alternative hypothesis}
\end{aligned}
$$

---
