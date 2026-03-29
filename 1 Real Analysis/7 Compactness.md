### sequentially compact

- for every sequence of sequentially compact set there exists convergent subsequence

---
### sequentially compact formula

$$
\begin{aligned}
\forall \set {a_n} \subset S \subset X, \exists \set {a_{n_k}} \subset \set {a_n}, \exists L \in S:\lim_{k \rightarrow \infty} a_{n_k} = L \\
a_n = \text{sequence} \\
S = \text{set} \\
a_{n_k} = \text{subsequence} \\
X = \text{metric space} \\
L = \text{subsequential limit}
\end{aligned}
$$

---
### totally bounded compactness property

- every sequentially compact set equal totally bounded set

---
### totally bounded compactness property formula

$$
\begin{aligned}
\forall \set {a_n} \subset S \subset X, \exists \set {a_{n_k}} \subset \set {a_n}, \exists L \in S:\lim_{k \rightarrow \infty} a_{n_k} = L \implies \forall \epsilon > 0, \exists \set {a_i}_{i=1}^{n} \subset X: S \subset \bigcup_{i=1}^n B_{\epsilon}(x_i) \\
a_n = \text{sequence} \\
a_{n_k} = \text{subsequence} \\
X = \text{metric space} \\
L = \text{subsequential limit} \\
S = \text{totally bounded set} \\
a_n = \text{sequence} \\
B = \text{open ball} \\
x_i = \text{center}
\end{aligned}
$$

---
### open cover

- collection of open set whose union contain covered set

---
### open cover formula

$$
\begin{aligned}
S \subset \bigcup_{i \in I} Y_i \subset X \\
S = \text{covered set} \\
I = \text{index set} \\
Y = \text{open set} \\
\set{Y} = \text{open cover} \\
X = \text{metric space} 
\end{aligned}
$$

---
### topologically compact

- for every open cover of compact set there exists finite subcover

---
### topologically compact formula

$$
\begin{aligned}
\forall \set{Y_i}_{i\in I} \subset X, \exists \{Y_{i_j}\}_{j=1}^n \subset \{Y_i\}_{i\in I}: S \subset \bigcup_{j=1}^n Y_{i_j} \subset X \\
Y = \text{open set} \\
\set{Y} = \text{open cover} \\
I, J = \text{index set} \\
X = \text{metric space} \\
S = \text{compact set} 
\end{aligned}
$$

---
### compactness property

- topologically compact set of metric space equal sequentially compact set

---
### compactness property formula

$$
\begin{aligned}
\forall \set{Y_i} \subset X, \exists \{Y_{i_1}, \dots Y_{i_n}\} \subset \{Y_i\}: S \subset \bigcup_{k=1}^n Y_{i_k} \subset X \\
\iff \forall \set {a_n} \subset S \subset X, \exists \set {a_{n_k}} \subset \set {a_n}, \exists L \in S:\lim_{k \rightarrow \infty} a_{n_k} = L \\
S = \text{compact set} \\
Y = \text{open set} \\
\set{Y} = \text{open cover} \\
X = \text{metric space} \\
a_n = \text{sequence} 
\end{aligned}
$$

---
### closed bounded compactness property

- every compact set of metric space equal closed bounded set

---
### closed bounded compactness property formula

$$
\begin{aligned}
(S' \subset S \subset X ) \\
\land (S \subset X, \exists x_0 \in X, \exists r > 0: B_r(x_0) \supset S) \\
\implies \forall \set {a_n} \subset S \subset X, \exists \set {a_{n_k}} \subset \set {a_n}, \exists L \in S:\lim_{k \rightarrow \infty} a_{n_k} = L \\
\lor \forall \set{Y_i} \subset X, \exists \{Y_{i_1}, \dots Y_{i_n}\} \subset \{Y_i\}: S \subset \bigcup_{k=1}^n Y_{i_k} \subset X \\
S' = \text{derived set} \\
S = \text{compact set} \\
X = \text{metric space} \\
x_0 = \text{center} \\
r = \text{radius} \\
B = \text{open ball} \\
a_n = \text{sequence} \\
a_{n_k} = \text{subsequence} \\
L = \text{subsequential limit} \\
Y = \text{open set} \\
\set{Y} = \text{open cover} 
\end{aligned}
$$

---
### closure compactness property

- for every open cover of closure there exists finite subcover

---
### closure compactness property formula

$$
\begin{aligned}
\forall \set{Y_i}_{i\in I} \subset X, \exists \{Y_{i_j}\}_{j=1}^n \subset \{Y_i\}_{i\in I}: \overline S \subset \bigcup_{j=1}^n Y_{i_j} \subset X \\
Y = \text{open set} \\
\set{Y} = \text{open cover} \\
I, J = \text{index set} \\
X = \text{metric space} \\
\overline S = \text{closure}
\end{aligned}
$$

---
### compact closedness property

- compact set of metric space equal closed set

---
### compact closedness property

$$
\begin{aligned}
\forall \set{Y_i}_{i\in I} \subset X, \exists \{Y_{i_j}\}_{j=1}^n \subset \{Y_i\}_{i\in I}: S \subset \bigcup_{j=1}^n Y_{i_j} \subset X \implies S' \subset S \\
Y = \text{open set} \\
\set{Y} = \text{open cover} \\
I, J = \text{index set} \\
X = \text{metric space} \\
S = \text{closed set} \\
S' = \text{derived set}
\end{aligned}
$$

---
### closed compactness property

- closed subset of compact set equal compact set

---
### closed compactness property formula

$$
\begin{aligned}
S' \subset S \subset K \implies \forall \set{Y_i}_{i\in I} \subset X, \exists \{Y_{i_j}\}_{j=1}^n \subset \{Y_i\}_{i\in I}: S \subset \bigcup_{j=1}^n Y_{i_j} \subset X \\
S' = \text{derived set} \\
S = \text{closed set} \\
K = \text{compact set} \\
Y = \text{open set} \\
\set{Y} = \text{open cover} \\
I, J = \text{index set} \\
X = \text{metric space} \\
\end{aligned}
$$

---
### closed intersection property

- intersection between closed set and compact set equal compact set

---
### closed intersection property formula

$$
\begin{aligned}
(S' \subset S \subset X) \land (\forall \set{Y_i}_{i\in I} \subset X, \exists \{Y_{i_j}\}_{j=1}^n \subset \{Y_i\}_{i\in I}: K \subset \bigcup_{j=1}^n Y_{i_j} \subset X) \implies S \cap K \subset \bigcup_{j=1}^n Y_{i_j} \\
S' = \text{derived set} \\
S = \text{closed set} \\
K = \text{compact set} \\
Y = \text{open set} \\
\set{Y} = \text{open cover} \\
I, J = \text{index set} \\
X = \text{metric space} \\
\end{aligned}
$$

---
### finite intersection property

- for every finite subcollection of compact set there exists nonempty intersection
- for every collection of compact set there exists nonempty intersection

---
### finite intersection property formula

$$
\begin{aligned}
\bigcap_{j=1}^n S_{i_j} \ne \emptyset \implies \bigcap _{i} S_i \ne \emptyset \\
S = \text{compact set} 
\end{aligned}
$$

---
### infinite limit point property

- for every infinite subset of compact set there exists limit point of compact set

---
### infinite limit point property formula

$$
\begin{aligned}
(S \subset K) \land (|S| = \infty) \implies \exists x_0 \in S, \forall r > 0: N_r(x_0) \setminus \{x_0\} \cap S \ne \emptyset \\
K = \text{compact set} \\
X = \text{metric space} \\
r = \text{radius} \\
N = \text{neighborhood} \\
x_0 = \text{limit point}
\end{aligned}
$$

---
### interval intersection property

- intersection of nested interval equal nonempty set

---
### interval intersection property formula

$$
\begin{aligned}
(\{I_n\} \in \mathbb R) \land (\forall n \in \mathbb N: I_n \subset I_{n+1}) \implies \bigcap_{n=1}^\infty I_n \ne \emptyset \\
I = \text{interval}
\end{aligned}
$$

---
### k-cell intersection property

- intersection of nested k-cell equal nonempty set

---
### k-cell intersection property formula

$$
\begin{aligned}
(\{I_n\} \in \mathbb R) \land (\forall n \in \mathbb N: I_n \subset I_{n+1}) \implies \bigcap_{n=1}^\infty I_n \ne \emptyset \\
I = \text{k-cell}
\end{aligned}
$$

---
### k-cell compactness property

- every k-cell equal compact set

---
### k-cell compactness property formula

$$
\begin{aligned}
\forall \set{Y_i}_{i\in I} \subset X, \exists \{Y_{i_j}\}_{j=1}^n \subset \{Y_i\}_{i\in I}: \prod_{i=1}^k [a_i, b_i] \subset \bigcup_{j=1}^n Y_{i_j}  \subset X \\
Y = \text{open set} \\
\set{Y} = \text{open cover} \\
I, J = \text{index set} \\
X = \text{metric space} \\
\prod_{i=1}^k [a_i, b_i] = \text{k-cell} 
\end{aligned}
$$

---
### heine-borel property

- every compact set of k-dimensional real numbers equal closed bounded set

---
### heine-borel property formula

$$
\begin{aligned}
(S' \subset S \subset X ) \\
\land (S \subset X, \exists x_0 \in X, \exists r > 0: B_r(x_0) \supset S) \\
\iff \forall \set{Y_i}_{i\in I} \subset X, \exists \{Y_{i_j}\}_{j=1}^n \subset \{Y_i\}_{i\in I}: S \subset \bigcup_{j=1}^n Y_{i_j} \subset X \\
S = \text{compact set} \\
S' = \text{derived set} \\
X = \text{metric space} \\
x_0 = \text{center} \\
r = \text{radius} \\
B = \text{open ball} \\
Y = \text{open set} \\
\set{Y} = \text{open cover} \\
I, J = \text{index set} 
\end{aligned}
$$

---
### bolzano-weierstrass property

- for every infinite bounded set of k-dimensional real numbers there exists limit point of k-dimensional real numbers

---  
### bolzano-weierstrass property formula

$$  
\begin{aligned}  
(S \subset \mathbb R^k) \land (\set {0, 1, 2, 3, \dots, n} \not\sim S) \implies \exists x_0 \in \mathbb R^k, \forall r > 0: N_r(x_0) \setminus \{x_0\} \cap \mathbb R^k \ne \emptyset \\  
S = \text{bounded set} \\  
r = \text{radius} \\  
N = \text{neighborhood} \\  
x_0 = \text{limit point}  
\end{aligned} 
$$

---
### cantor set

- subset of the unit interval
- uncountable set
- compact set
- perfect set

---
### construct cantor set

- start with unit interval $C_0 = [0, 1]$ 
- remove the open middle third $C_1= [0, \frac{1}{3}] \cup [\frac{2}{3}, 1]$ 
- repeat the removal for the intersection $\mathcal C = \bigcap_{n=1}^\infty C_n$ 

---
