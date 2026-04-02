### heat equation
- mathematical model describing the spatiotemporal flow of heat

---
### heat equation formula
$$
\begin{aligned}
\frac{\partial u}{\partial t} = k\frac{\partial ^2 u}{\partial ^2 x} \\
u(0, t) = u(L, t) = 0 \\
u(x, 0) = f(x) \\
u = \text{heat} \\
t = \text{time} \\
k = \text{constant} \\
x = \text{space}
\end{aligned}
$$

---
### heat equation guess
- separation of temporal variable and spatial variable

---
### heat equation guess formula
$$
\begin{aligned}
u(x, t) = X(x)T(t) \\
x = \text{space} \\
t = \text{time}
\end{aligned}
$$

---
### system of heat equations
- system of ordinary differential equations for the spatiotemporal flow of heat

---
### system of heat equations formula
$$
\begin{aligned}
\frac{X''(x)}{X(x)} = \frac{T'(t)}{kT(t)} = -\lambda \implies \begin{cases} X''(x) + \lambda X(x) = 0 \\
T'(t) + \lambda kT(t) = 0 \\
\end{cases} \\
x = \text{space} \\
t = \text{time} \\
k = \text{constant} \\
\lambda = \text{constant}
\end{aligned}
$$

---
### general solution of spatial heat equation
- mathematical model describing the spatial flow of heat

---
### general solution of spatial heat equation formula
$$
\begin{aligned}
X(x) = \sin(\frac{n\pi}{L}x) \\
n = 1, 2, 3, \dots \\
x = \text{space} \\
L = \text{length} 
\end{aligned}
$$

---
### general solution of temporal heat equation
- mathematical model describing the temporal flow of heat

---
### general solution of temporal heat equation formula
$$
\begin{aligned}
T(t) = \exp(-k\frac{n^2\pi^2}{L^2}t) \\
k = \text{constant} \\
n = 1, 2, 3, \dots \\
L = \text{length} \\
t = \text{time} \\
\end{aligned}
$$

---
### general solution of heat equation
- superposition of eigenmodes

---
### general solution of heat equation formula
$$
\begin{aligned}
u(x, t) = \sum _{n = 1}^N C_{n} \sin(\frac{n\pi}{L}x) \exp(-k\frac{n^2\pi^2}{L^2}t) \\
C = \text{fourier sine series} \\
n = 1, 2, 3, \dots \\
x = \text{space} \\
L = \text{length} \\
k = \text{constant} \\
t = \text{time} \\
\end{aligned}
$$

---
### fourier sine series
- represent function on the interval from $x = 0$ to $x = L$ as infinite sum of sine functions

---
### fourier sine series formula
$$
\begin{aligned}
C_{n} = \frac{2}{L}\int_{0}^L f(x)\sin(\frac{n\pi}{L}x)dx \\
L = \text{length} \\
n = 1, 2, 3, \dots \\
x = \text{space} \\
L = \text{length} 
\end{aligned}
$$

---
