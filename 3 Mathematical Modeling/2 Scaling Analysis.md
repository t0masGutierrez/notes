### scale

- size of scaling factor influence the graph of unit-free equation
---
### scale formula

$$
\begin{aligned}
D = \{(t, y) \in [-a, a] \times [-b, b]| p_1a \le t \le p_2b, q_1a \le y \le q_2b\} \\
y = f(t, c_1, \dots, c_n) \\
p_1, p_2, q_1, q_2 \in \mathbb Z \\
[a] = [t] \\
[b] = [y] \\
D = \text{domain} \\
t, y = \text{variable} \\
a, b = \text{scaling factor} \\
c = \text{parameter} 
\end{aligned}
$$

---
### scale example

- $y = c_1t^2 + c_2\sin(\frac{2\pi t}{c_3})$ 
- $c_1 = 2\frac{\text{m}}{\text{s}^2}$ 
- $c_2 = 0.01 \text{m}$ 
- $c_3 = 0.01\text{s}$ 
---
### scale example formula

$$
\begin{aligned}
\{a, b\} = \{0.001 \text{s}, 0.005\text{m}\}, \{0.02\text{s}, 0.02\text{m}\}, \{0.15 \text{s}, 0.10 \text{m}\}, \{10 \text{s}, 200 \text{m}\}
\end{aligned}
$$

---
### scale transformation

- change of variables from domain to scaled, normalized domain
---
### scale transformation formula

$$
\begin{aligned}
(\bar t = \frac{t}{a}) \land (\bar y = \frac{y}{b}) \rightarrow \bar D = \{(\bar t, \bar y) \in [-1, 1] \times [-1, 1]| p_1 \le \bar t \le p_2, q_1 \le \bar y \le q_2\} \\
\bar y = \frac{1}{b}f(a \bar t, c_1, \dots, c_N) = \bar f(\bar t, a, b, c_1, \dots, c_n) \\
p_1, p_2, q_1, q_2 \in \mathbb Z \\
[a] = [\bar t] \\
[b] = [\bar y] \\
\bar D = \text{domain} \\
\bar t, \bar y = \text{variable} \\
a, b = \text{scaling factor} \\
c = \text{parameter} 
\end{aligned}
$$

---
### scale transformation example

- $y = c_1t^2 + c_2\sin(\frac{2\pi t}{c_3})$ 
- $c_1 = 2\frac{\text{m}}{\text{s}^2}$ 
- $c_2 = 0.01 \text{m}$ 
- $c_3 = 0.01\text{s}$ 
---
### scale transformation example formula

$$
\begin{aligned}
\{a, b\} = \{-1, 1\}
\end{aligned}
$$

---
### scale derivative property

- kth derivative of scaled function equal kth power of scaling denominator

---
### scale derivative property formula

$$
\begin{aligned}
(\bar t = \frac{t}{a}) \land (\bar y = \frac{y}{b}) \rightarrow\frac{d^k \bar y}{d \bar t^k} = (\frac{a^k}{b})(\frac{d^k y}{d t^k}) \\
\bar t, \bar y = \text{variable} \\
a, b = \text{scaling factor} 
\end{aligned}
$$

---
### characteristic scale

- typical size of scale equal input

---
### characteristic scale formula

$$
\begin{aligned}
b = \max_{t \in I}|y| \\
a = \frac{b}{\max_{t \in I}|\frac{dy}{dt}|}
\end{aligned}
$$

---
### associative scale

- output equal true size of scale

---
### associative scale formula

$$
\begin{aligned}
(a = \prod_{i=1}^n c_i^{\alpha_i}) \land ([a] = [t]) \leftrightarrow \Delta_a = A \alpha = \Delta_t \\
(b = \prod_{i=1}^n c_i^{\beta_i}) \land ([b] = [y]) \leftrightarrow \Delta_b = A \beta = \Delta_y \\
A = [\Delta_{c_1}, \dots, \Delta_{c_n}] \in \mathcal M_{m\le n} \\
\vec \alpha = [\alpha_1, \dots, \alpha_n] \\
\vec \beta = [\beta_1, \dots, \beta_n] \\
t, y = \text{variable} \\
a, b = \text{scaling factor} \\
\alpha, \beta = \text{parameter exponent} \\
c = \text{parameter}
\end{aligned}
$$

---
### scaling property

- scale transformation under natural scale equal equivalent function with smaller dimensionless argument

---
### scaling property formula

$$
\begin{aligned}
(\bar t = \frac{t}{a}) \land (\bar y = \frac{y}{b}) \rightarrow \bar y = \phi(\bar t, \mu_1, \dots, \mu_m) \\
[\mu] = 1 \\
t, y, = \text{variable} \\
a, b = \text{scaling factor} \\
\mu = \text{parameter} \\
\end{aligned}
$$

---
