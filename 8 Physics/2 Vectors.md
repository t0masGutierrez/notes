---
output:
  pdf_document: default
  html_document: default

---
### scalar

- quantity with magnitude

---
### vector

- quantity with both magnitude and direction
---
### unit vector

- vector with magnitude of 1 that specify direction without scaling

---
### unit vector formula

$$
\begin{aligned}
\hat{i} = \frac{\overrightarrow{A_x}}{A_x} \\ 
\hat{j} = \frac{\overrightarrow{A_y}}{A_y}
\end{aligned}
$$

---
### component

- horizontal change equal *x* component
- vertical change equal *y* component
---
### scalar component formula

$$
\begin{aligned}
A_x = A \cos (\theta) \\
A_y = A \sin (\theta) \\
A = \text{magnitude} \\
\theta = \text{direction}
\end{aligned}
$$

---
### vector component formula

$$
\begin{aligned}
\overrightarrow{A} = A_x\hat{i} + A_y\hat{j} \\
A_x = \text{x scalar component} \\
\hat{i} = \text{x direction} \\
A_y = \text{y scalar component} \\
\hat{j} = \text{y direction}
\end{aligned}
$$

---
### magnitude

- distance from origin

---
### magnitude formula

$$
\begin{aligned}
A = \sqrt{A_x^2 + A_y^2} \\
A_x = \text{x scalar component} \\
A_y = \text{y scalar component}
\end{aligned}
$$

---
### direction

- counterclockwise angle between axis and vector
- left right up down

---
### direction formula

$$
\begin{aligned}
\theta = \arctan (\frac{A_y}{A_x}) \\
A_x = \text{x scalar component} \\
A_y = \text{y scalar component}
\end{aligned}
$$

---
### inverse tangent range

- $[\frac{-\pi}{2} \le \theta \le \frac{\pi}{2}] = [-90 \le \theta \le 90] = Q_1 \lor Q_4$  
- negative $A_x$ equal 180 addition with direction
---
### vector equality

- equal magnitude and equal direction

---
### vector equality formula

$$
\begin{aligned}
\overrightarrow{A} = \overrightarrow{B} \leftrightarrow
\begin{cases}
A_x = B_x \\
A_y = B_y
\end{cases}
\end{aligned}
$$

---
### vector property

- commutative
- associative
- additive identity
- additive inverse
- distributive
- multiplicative identity
- multiplicative zero

---
### vector property formula

$$
\begin{aligned}
\overrightarrow A + \overrightarrow B = \overrightarrow B + \overrightarrow A \\
(\overrightarrow A + \overrightarrow B) + \overrightarrow C = \overrightarrow A + (\overrightarrow B + \overrightarrow C) \\
\overrightarrow A + 0 = \overrightarrow A \\
\overrightarrow A + (-\overrightarrow A) = 0 \\
c(\overrightarrow A + \overrightarrow B) = c\overrightarrow A + c\overrightarrow B \\
1(\overrightarrow A) = \overrightarrow A \\
0(\overrightarrow A) = 0\end{align*}
$$

---
### scalar multiplication

- scalar quantity multiplication with vector component
- negative scalar quantity equal 180 addition with direction or negative vector component

---
### scalar multiplication formula

$$
\begin{aligned}
a\overrightarrow{A} = aA_x\hat{i} + aA_y\hat{j} \\
a = \text{scalar quantity} \\
A_x \hat i = \text{x vector component} \\
A_y \hat j = \text{y vector component}
\end{aligned}
$$

---
### vector addition

- vector *A* component(s) addition with corresponding vector *B* component(s) 

---
### vector addition formula

$$
\begin{aligned}
\overrightarrow{R} = (A_x + B_x)\hat{i} + (A_y + B_y)\hat{j} \\
A_x = \text{x scalar component} \\
\hat i = \text{x direction} \\
A_y = \text{y scalar component} \\
\hat j = \text{y direction} \\
\end{aligned}
$$

---
### graphical vector addition

- vector *B* starts where vector *A* ends
- vector sum *C* equal diagonal from where vector *A* starts to where vector *B* ends
---
### parallelogram vector addition

- both vectors start via origin
- construct two parallel vectors
- vector sum *C* equal diagonal from origin to where parallel vectors intersect
---
### graphical vector subtraction

- anti parallel vector *B* starts where vector *A* ends
- vector sum equal diagonal from where vector *A* starts to where anti parallel vector *B* ends
---
### dot product

- scalar quantity of similarity between two vectors
- aka scalar product
---
### dot product formula

$$
\begin{aligned}
\overrightarrow{A} \cdot \overrightarrow{B} = AB \cos (\theta) \\
A = \text{magnitude} \\
\theta = \text{angle between vectors}
\end{aligned}
$$

---
### dot product formula

$$
\begin{aligned}
\overrightarrow{A} \cdot \overrightarrow{B} = A_xB_x + A_yB_y + A_zB_z \\
A_x = \text{x scalar component} \\
A_y = \text{y scalar component} \\
A_z = \text{z scalar component}
\end{aligned}
$$

---
### unit vector dot product formula

$$
\begin{aligned}
\hat{i} \cdot \hat{j} = \hat{j} \cdot \hat{k} = \hat{k} \cdot \hat{i} = 0 \\
\hat i = \text{x direction} \\
\hat j = \text{y direction} \\
\hat k = \text{z direction}
\end{aligned}
$$

---
### calculate dot product

- acute angle equal positive dot product
- obtuse angle equal negative dot product
- parallel vectors equal $AB$ 
- anti parallel vectors equal negative $AB$
- perpendicular vectors equal 0
- same vectors equal $A^2$ 

---
### cross product

- vector quantity of dissimilarity between two vectors
- aka vector product
---
### cross product formula

$$
\begin{aligned}
|\overrightarrow{A} \times \overrightarrow{B}| = AB \sin (\theta) \\
A = \text{magnitude} \\
\theta = \text{angle between vectors}
\end{aligned}
$$

---
### cross product formula

$$
\begin{aligned}
\overrightarrow{A} \times \overrightarrow{B} = (A_yB_z - A_zB_y)\hat{i} + (A_zB_x - A_xB_z)\hat{j} + (A_xB_y - A_yB_x)\hat{k} \\
A_x = \text{x scalar component} \\
\hat i = \text{x direction} \\
A_y = \text{y scalar component} \\
\hat j = \text{y direction} \\
A_z = \text{z scalar component} \\
\hat k = \text{z direction}
\end{aligned}
$$

---
### unit vector cross product formula

$$
\begin{aligned}
\hat{i} \times \hat{j} = \hat{k} \\
\hat{j} \times \hat{k} = \hat{i} \\
\hat{k} \times \hat{i} = \hat{j} \\
\hat i = \text{x direction} \\
\hat j = \text{y direction} \\
\hat k = \text{z direction}
\end{aligned}
$$

---
### calculate cross product

- right angle equal $AB$ 
- parallel vectors equal 0
- anti parallel vectors equal 0
- same vectors equal 0

---
### right hand rule

- point hand to vector *A*
- curl palm to vector *B*
- point thumb to vector $A \times B$
---







