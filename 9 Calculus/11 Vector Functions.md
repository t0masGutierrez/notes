### space curve

- set of parametric equation triples that define spatial curve
---
### space curve formula

$$
\begin{aligned}
\overrightarrow{r}(t) = x(t)\hat{i} + y(t)\hat{j} + z(t)\hat{k} \\
x = \text{x position} \\
y = \text{y position} \\
z = \text{z position} \\
t = \text{parameter}
\end{aligned}
$$

---
### vector function

- function whose domain equal set of real numbers and range equal set of vectors

---
### limit

- $\overrightarrow r(t)$ behavior as *t* approaches value

---
### limit formula

$$
\begin{aligned}
\lim_{t \to n} \overrightarrow r(t) = \lim_{t \to n} x(t) \hat i + \lim_{t \to n} y(t) \hat j + \lim_{t \to n} z(t) \hat k
\end{aligned}
$$

---
### discontinuity

- hole
- jump
- infinite

---
### continuity

$$
\begin{aligned}
\lim_{t \to n} \overrightarrow r(t) = \overrightarrow r(n) \\
\lim_{t \to n^-} \overrightarrow r(t) = \lim_{t \to n^+}  \overrightarrow r(t) \\
\lim_{t \to n} \overrightarrow r(t) \ne \pm \infty
\end{aligned}
$$

---
### instantaneous rate of change

- slope of tangent vector

---
### instantaneous rate of change formula

$$
\begin{aligned}
\overrightarrow r \ '(n) = \lim_{t \to n} \frac{\overrightarrow r(t) - \overrightarrow r(n)}{t - n}
\end{aligned}
$$

---
### derivative

- slope of secant vector as $\Delta t$ approaches zero
---
### derivative formula

$$
\begin{aligned}
\frac{d}{dt}\overrightarrow r(t) = \lim_{\Delta t \to 0} \frac{\overrightarrow r(t + \Delta t) - \overrightarrow r(n)}{\Delta t}
\end{aligned}
$$

---
### differentiable

- function continuous and derivative exists

---
### non differentiable

- discontinuity
- vertical tangent vector
- sharpness

---
### definite integration

- operation of finding the area under spatial curve between two limits of integration

---
### definite integral formula

$$
\begin{aligned}
\int_a^b \overrightarrow r(t)dt = \overrightarrow R(b) - \overrightarrow R(a) \\
\int_a^b \overrightarrow r(t)dt = \hat i \int_a^b x(t)dt + \hat j \int_a^b y(t)dt + \hat k \int_a^b z(t)dt
\end{aligned}
$$

---
### integrable

- function continuous

---
### non integrable

- discontinuity

---
### arc length

- distance between two points along arc

---
### unit tangent vector

- vector with magnitude of 1 that specify tangent direction of vector quantity 

---
### unit tangent vector

$$
\begin{aligned}
\overrightarrow T(t) = \frac{\overrightarrow r \ '(t)}{r'(t)}
\end{aligned}
$$

---
### unit normal vector

- vector with magnitude of 1 that specify normal direction of vector quantity

---
### unit normal vector

$$
\begin{aligned}
\overrightarrow N(t) = \frac{\overrightarrow T \ '(t)}{T'(t)}
\end{aligned}
$$

---
### unit binormal vector

- vector with magnitude of 1 that specify binormal direction of vector quantity

---
### unit binormal vector

$$
\begin{aligned}
\overrightarrow B(t) = \overrightarrow T(t) \times \overrightarrow N(t) 
\end{aligned}
$$

---
### curvature

- rate of direction change along curve

---
### curvature formula

$$
\begin{aligned}
\kappa(t) = \frac{T'(t)}{r'(t)}
\end{aligned}
$$

---
### acceleration component

- tangential acceleration and normal acceleration

---
### acceleration component formula

$$
\begin{aligned}
\overrightarrow a(t) = a_T \overrightarrow T + a_N \overrightarrow N 
\end{aligned}
$$

---
### tangential acceleration formula

$$
\begin{aligned}
a_T = \frac{\overrightarrow r \ '(t) \cdot \overrightarrow r \ ''(t)}{r'(t)}
\end{aligned}
$$

---
### normal acceleration formula

$$
\begin{aligned}
a_N = \frac{r'(t) \times r''(t)}{r'(t)}
\end{aligned}
$$

---
### arc length

- distance between two points along arc

---
### arc length formula

$$
\begin{aligned}
r(t) = \int_a^t \sqrt{(\frac{dx}{dt})^2 + (\frac{dy}{dt})^2 + (\frac{dz}{dt})^2}dt = \int_a^t \overrightarrow r \ '(u)du
\end{aligned}
$$

---
