### dot product
- scalar quantity of similarity between two vectors

---
### dot product formula
$$
\begin{aligned}
\vec x \cdot \vec y = x_1y_{1} + ... + x_ny_{n} = \sum_{i=1}^n x_iy_{i} \\
x, y = \text{coordinate} \\
n = \text{number of coordinates} \\
i = \text{index}
\end{aligned}
$$

---
### dot product formula
$$
\begin{aligned}
\vec x \cdot \vec y = (\| \vec x \|)(\| \vec y \|) \cos(\theta) \\
\vec x, \vec y = \text{vector} \\
\| \vec x \|, \| \vec y \| = \text{magnitude} \\
\theta = \text{direction}
\end{aligned}
$$

---
### dot product property
- commutative
- identity
- zero
- associative
- distributive

---
### dot product property formula
$$
\begin{aligned}
\vec x \cdot \vec y = \vec y \cdot \vec x \\
\vec x \cdot \vec x = \| \vec x \|^2 \ge 0 \\ 
\vec x \cdot \vec x = \vec 0 \iff \vec x = \vec 0 \\ 
c(\vec x \cdot \vec y) = (c\vec x) \cdot \vec y = \vec x \cdot (c\vec y) \\
\vec x \cdot (\vec y + \vec z) = (\vec x \cdot \vec y) + (\vec x \cdot \vec z) \\
(\vec x + \vec y) \cdot \vec z = (\vec x \cdot \vec z) + (\vec y \cdot \vec z)
\end{aligned}
$$

---
### unit vector property
- dot product of unit vector equal $\pm 1$ 

---
### unit vector property formula
$$
\begin{aligned}
-1 \le \vec x \cdot \vec y \le 1 \\
||\vec x|| = 1 \\
||\vec y|| = 1
\end{aligned}
$$

---
### cauchy schwarz inequality
- dot product of magnitudes equal upper boundary for magnitude of dot product

---
### cauchy schwarz inequality formula
$$
\begin{aligned}
|\vec x \cdot \vec y | \le (\| \vec x \|)(\| \vec y \|) \\
\vec x, \vec y = \text{vector} \\
\| \vec x \|, \| \vec y \| = \text{magnitude}
\end{aligned}
$$

---
### triangle inequality
- sum of magnitudes equal upper boundary for magnitude of sum

---
### minkowski’s inequality formula
$$
\begin{aligned}
\|\vec{x} + \vec{y}\| \le \|\vec{x}\| + \|\vec{y}\| \\
\vec x, \vec y = \text{vector} \\
\| \vec x \|, \| \vec y \| = \text{magnitude}
\end{aligned}
$$

---
### direction
- counterclockwise angle between two vectors 
---
### direction formula
$$
\begin{aligned}
\cos(\theta) = \frac{\vec x \cdot \vec y}{(|| \vec x ||)(|| \vec y ||)} \\
0 \le \theta \le \pi \\
\vec x, \vec y = \text{vector} \\
\| \vec x \|, \| \vec y \| = \text{magnitude}
\end{aligned}
$$

---
### direction property
- acute angle
- right angle
- obtuse angle
- parallel direction
- orthogonal direction

---
### direction property formula
$$
\begin{aligned}
0 \le \theta \le 90 \iff \vec x \cdot \vec y > 0 \\
\theta = 90 \iff \vec x \cdot \vec y = 0 \\
90 \le \theta \le 180 \iff \vec x \cdot \vec y < 0 \\
\vec x \parallel \vec y \iff \vec x \cdot \vec y = \pm (||\vec x ||)(||\vec y ||) \\
\vec x \perp \vec y \iff \vec x \cdot \vec y = 0
\end{aligned}
$$

---
### mutually orthogonal
- for every pair of distinct vectors the dot product equal zero

---
### mutually orthogonal formula
$$
\begin{aligned}
\forall i, j \in \{1, ..., k\}: i \ne j \implies \vec x_{i} \cdot \vec x_{j} = 0 \\
i = \text{row index} \\
j = \text{column index} \\
k = \text{number of vectors} \\
\vec x = \text{vector}
\end{aligned}
$$

---
### parallel projection
- parallel projection of $\vec y$ onto $\vec x$ equal vector component of $\vec y$ parallel $\vec x$ 

---
### parallel projection formula
$$
\begin{aligned}
\text{proj}_{x}(y\parallel) = (\frac{\vec x \cdot \vec y}{\|\vec x \|^2})\vec x \\
\vec x, \vec y = \text{vector} \\
\|\vec x \| = \text{magnitude}
\end{aligned}
$$

---
### orthogonal projection
- orthogonal projection of $\vec y$ onto $\vec x$ equal vector component of $\vec y$ orthogonal $\vec x$ 
---
### orthogonal projection formula
$$
\begin{aligned}
\text{proj}_{x}(y\perp) = \vec y - (\frac{\vec x \cdot \vec y}{\|\vec x \|^2})\vec x \\
\vec x, \vec y = \text{vector} \\
\|\vec x \| = \text{magnitude}
\end{aligned}
$$

---
