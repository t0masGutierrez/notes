### mathematical model

- equation that express relationship between given quantity(s) of interest

---
### unit

- scale of measurement

---
### unit example

- meter
- second
- kilogram
- kelvin

---
### dimension

- type of measurement

---
### dimension formula

$$
\begin{aligned}
[q] = \prod_{i=1}^m D_i^{a_i} \leftrightarrow \Delta_q = [a_1, \dots, a_m] \in \mathbb R^m \\
q = \text{quantity} \\ 
D = \text{dimension} \\
a = \text{dimensional exponent}
\end{aligned}
$$

---
### dimension example

- length
- time
- mass
- temperature

---
### dimension example formula

- $q = 3 \frac{kg \cdot m^2}{s^2}$ 
- $D = \set{L, T, M, \theta}$ 
- $[q] = ML^2T^{-2}$ 
- $\Delta_q = [2, -2, 1, 0]$ 

---
### dimensional basis

- spanning
- linearly independent

---
### dimensional basis formula

$$
\begin{aligned}
\text{Span}(D) = \mathcal V \\
\text{Rank}(D) = m
\end{aligned}
$$

---
### dimension property

- addition
- multiplication
- division
- exponentiation
- integration
- differentiation

---
### dimension property formula

$$
\begin{aligned}
[p \pm q] \in D \leftrightarrow [p] = [q] \\
[p \cdot q] = [p] \cdot [q] \\
[\frac{p}{q}] = \frac{[p]}{[q]} \\
[q^k] = [q]^k \\
[\int p \cdot dq] = [p] \cdot [q] \\
[\frac{d^kp}{dq^k}] = \frac{[p]}{[q]^k}
\end{aligned}
$$

---
### exponent property

- multiplication
- division
- exponentiation

---
### exponent property formula

$$
\begin{aligned}
\Delta_{pq} = \Delta_p + \Delta_q \\
\Delta_{p/q} = \Delta_p - \Delta_q \\
\Delta_{q^k} = k\Delta_q
\end{aligned}
$$

---
### dimensionless

- dimension equal 1
- dimensional exponent equal 0

---
### dimensionless formula

$$
\begin{aligned}
[q] = 1 \leftrightarrow \Delta_q = 0 \\
q = \text{pure number}
\end{aligned}
$$

---
### change of units

- convert unit of quantity with respect to dimensional basis

---
### change of units formula

$$
\begin{aligned}
q' = q\prod_{i=1}^m \lambda_i^{a_i} \\
q = \text{quantity} \\
\lambda = \text{unit conversion factor} \\
a = \text{dimensional exponent}
\end{aligned}
$$

---
### change of units example

- $q = 9.8 \frac{m}{s^2}$ 
- $U = \set{\text{m}, \text{s}}$ 
- $U' = \set{\text{km}, \text{min}}$ 

---
### change of units example formula

$$
\begin{aligned}
q' = (9.8\frac{\text{m}}{\text{s}^2})(\frac{1\text{ km}}{1000\text{ m}})(\frac{60\text{ s}}{1\text{ min}})^{2} = 35.28 \frac{\text{km}}{\text{min}^2}
\end{aligned}
$$

---
### unit-free equation

- every quantity of equation equal dimensionless quantity

---
### unit-free equation formula

$$
\begin{aligned}
q_1 = f(q_2, \dots, q_n) \rightarrow q_1' = f'(q_2', \dots, q_n')
\end{aligned}
$$

---
### unit-free example

- define the dimensions
- define the change of units
- substitute the change of units into equation
- dimensional exponent of unit conversion factor equal negative dimensional exponent of quantity such that sum of corresponding dimensional exponent equal zero

---
### unit-free example formula

- $x = \frac{1}{2}gt^2$ 
- $D = \set{L, T}$ 
- $[x] = L, [t] = T, [g] = LT^{-2}$ 
- $x' = x\lambda_1, t' = t\lambda_2, g' = g\lambda_1\lambda_2^{-2}$ 
- $(x'\lambda_1^{-1}) = \frac{1}{2}(g'\lambda_1^{-1}\lambda_2^2)(t'\lambda_2^{-1})^2$ 
- $x'\lambda_1^{-1}\lambda_1^{1} = \frac{1}{2}g't'^2\lambda_2^2\lambda_2^{-2}$ 
- $\lambda \not\in x'$ 

---
### dimensionless power product

- product of power of quantity with respect to quantitative exponent

---
### dimensionless power product formula

$$
\begin{aligned}
\pi = \prod_{i=1}^n q_i^{b_i} > 0 \\
q = \text{quantity} \\
b = \text{quantitative exponent}
\end{aligned}
$$

---
### buckingham pi property

- calculate units
- form matrix whose columns equal units
- convert matrix into reduced row echelon form
- back substitute for the fundamental solution set
- dimensional exponent of first target dimensionless power product equal 1 and dimensional exponent of additional target dimensionless power product equal 0
- every physically meaningful equation expressible as relationship between $n-m-1$ dimensionless power product

---
### buckingham pi property formula

$$
\begin{aligned}
q_1 = f(q_2, \dots, q_n) \sim \pi_1 = \phi (\pi_2, \dots, \pi_{n-m-1}) \\
[\pi] = 1 \leftrightarrow \Delta_\pi = \sum_{i=1}^n b_i\Delta_{q_i} = A\vec b = 0 \\
A = [\Delta q_1, \dots, \Delta q_n] \in \mathcal M_{mn} \\
\vec b = [b_1, \dots, b_n] \in \mathbb R^n \\
q = \text{quantity} \\
\pi = \text{dimensionless power product} \\
b = \text{quantitative exponent}
\end{aligned}
$$

---
