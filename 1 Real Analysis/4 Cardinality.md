### convex
- every coordinate along segment equal coordinate of convex set

---
### convex formula
$$
\begin{aligned}
S \subset \mathbb R, \forall p, q \in S, \forall \lambda \in [0, 1]: \lambda p + (1 - q)\lambda \in S \\
S = \text{convex set}
\end{aligned}
$$

---
### interval
- convex region between endpoints

---
### interval formula
$$
\begin{aligned}
I \subset \mathbb R, \forall (x < y) \in I: [x, y] = \{z \in \mathbb R| x \le z \le y\} \subset I \\
I = \text{interval} 
\end{aligned}
$$

---
### nested interval
- sequence of subintervals

---
### nested interval formula
$$
\begin{aligned}
I_{1} \subset I_{2} \subset \dots \subset I_{n} \subset I_{n+1} \subset \dots \\
I = \text{interval}
\end{aligned}
$$

---
### nested interval property
- intersection of nested interval equal singleton set

---
### nested interval property formula
$$
\begin{aligned}
(\forall n \in \mathbb N: I_{n} = [a_{n}, b_{n}] \subset \mathbb R) \land (\lim_{n \rightarrow \infty}b_{n} - a_{n} = 0) \implies \exists x \in \mathbb R, \forall n \in \mathbb N: \bigcap_{n=1}^\infty I_{n} = \{x\} \\
I_{n} = \text{nested interval} \\
\end{aligned}
$$

---
### k-cell
- subset of k-dimensional euclidean space equal the cartesian product of interval

---
### k-cell formula
$$
\begin{aligned}
\forall (a < b) \in \mathbb R: \prod_{i=1}^k [a_{i}, b_{i}] = \{\vec q \in \mathbb R^k | a_{i} \le q_{i} \le b_{i} \} \\
a = \text{lower endpoint} \\
b = \text{upper endpoint}
\end{aligned}
$$

---
### open interval
- region between two exclusive endpoints

---
### open interval formula
$$
\begin{aligned}
(a, b) = \{x \in \mathbb R| a < x < b\} \\
a = \text{lower endpoint} \\
b = \text{upper endpoint} 
\end{aligned}
$$

---
### closed interval
- region between two inclusive endpoints

---
### closed interval formula
$$
\begin{aligned}
[a, b] = \{x \in \mathbb R| a \le x \le b\} \\
a = \text{lower endpoint} \\
b = \text{upper endpoint} 
\end{aligned}
$$

---
### cardinality
- size of set

---
### cardinality formula
$$
\begin{aligned}
\# A = \# B \iff f: A \rightarrow B, \forall b \in B, \exists !a \in A: f(a) = b \\
\# = \text{cardinality}
\end{aligned}
$$

---
### natural cardinality
- smallest possible size of infinite set

---
### natural cardinality formula
$$
\begin{aligned}
\aleph_{0} = \# \mathbb N \\
\# = \text{cardinality}
\end{aligned}
$$

---
### real cardinality
- smallest possible size of uncountable set

---
### real cardinality formula
$$
\begin{aligned}
2^{\aleph_{0}} = \# \mathbb R \\
\# = \text{cardinality}
\end{aligned}
$$

---
### union cardinality property
- size of set union equal sum of size subtraction with joint size

---
### union cardinality property formula
$$
\begin{aligned}
(\{0, 1,\dots, n\} \sim S) \land (S_{1}, \dots, S_{n}) \implies \# \bigcup_{i=1}^n S_{i} = \sum_{i=1}^n \# S_{i} - \# \bigcap_{i=1}^n S_{i} \\
\end{aligned}
$$

---
### finite
- there exists bijection between set and finite subset of natural numbers

---
### finite formula
$$
\begin{aligned}
\{0, 1, 2, 3, \dots, n\} \sim S\\
S = \text{finite set} 
\end{aligned}
$$

---
### infinite
- there exists no bijection between set and finite subset of natural numbers

---
### infinite formula
$$
\begin{aligned}
\{0, 1, 2, 3, \dots, n\} \not \sim S \\
S = \text{infinite set} 
\end{aligned}
$$

---
### countable
- there exists bijection between set and set of natural numbers

---
### countable formula
$$
\begin{aligned}
\mathbb N \sim S\\
S = \text{countable set} 
\end{aligned}
$$

---
### uncountable
- infinite and uncountable

---
### uncountable formula
$$
\begin{aligned}
(\{0, 1, 2, 3, \dots, n\} \not \sim S) \land (\mathbb N \not\sim S) \\
S = \text{uncountable set}
\end{aligned}
$$

---
### countable example
- naturals
- integers
- rationals

---
### countable example formula
$$
\begin{aligned}
\mathbb N \sim \mathbb N \\
\mathbb N \sim \mathbb Z \\
\mathbb N \sim \mathbb Q \\
\end{aligned}
$$

---
### uncountable example
- irrationals
- reals

---
### uncountable example formula
$$
\begin{aligned}
(\{0, 1, 2, 3, \dots, n\} \not \sim \mathbb R - \mathbb Q) \land (\mathbb N \not\sim \mathbb R - \mathbb Q) \\
(\{0, 1, 2, 3, \dots, n\} \not \sim \mathbb R) \land (\mathbb N \not\sim \mathbb R) 
\end{aligned}
$$

---
### countable subset property
- every subset of countable set equal countable set

---
### countable subset property formula
$$
\begin{aligned}
(\mathbb N \sim S) \land (S_{1} \subset S) \implies \mathbb N \sim S_{1} \\
S = \text{countable set} \\
S_{1} = \text{countable set}
\end{aligned}
$$

---
### countable infinity property
- every countable set equal infinite set

---
### countable infinity property formula
$$
\begin{aligned}
\mathbb N \sim S \implies \{0, 1, 2, 3, \dots, n\} \not\sim S \\
S = \text{countable set} 
\end{aligned}
$$

---
### countable union property
- every countable union of countable set equal countable set

---
### countable union property formula
$$
\begin{aligned}
(\mathbb N \sim S) \land (S_{1}, S_{2}, S_{3}, \dots = \aleph_{0}) \implies \mathbb N \sim \bigcup_{n=1}^\infty S_{n}\\
S = \text{countable set}
\end{aligned}
$$

---
### countable product property
- every countable product of countable set equal countable set

---
### countable product property formula
$$
\begin{aligned}
(\mathbb N \sim S) \land (S_{1}, S_{2}, S_{3}, \dots, S_{n}) \implies \mathbb N \sim S^n \\
S = \text{countable set}
\end{aligned}
$$

---
### uncountable interval property
- every interval of real numbers equal uncountable set

---
### uncountable interval property formula
$$
\begin{aligned}
[0, 1] = \{x \in \mathbb R| 0 \le x \le 1\} \implies \mathbb N \not\sim [0, 1]
\end{aligned}
$$

---
### countable function property
- if domain countable then range countable

---
### countable function property formula
$$
\begin{aligned}
(f: A \rightarrow B) \land (\mathbb N \sim A) \implies \mathbb N \sim f(A) \\
f = \text{function} \\
A = \text{domain} \\
B = \text{codomain} 
\end{aligned}
$$

---
### uncountable injection property
- if injective domain uncountable then injective codomain uncountable

---
### uncountable injection property formula
$$
\begin{aligned}
(f: A \rightarrow B) \land (\mathbb N \not\sim A) \implies \mathbb N \not\sim B \\
f = \text{injection} \\
A = \text{domain} \\
B = \text{codomain} 
\end{aligned}
$$

---
### uncountable surjection property
- if surjective codomain uncountable then surjective domain uncountable

---
### uncountable surjection property formula
$$
\begin{aligned}
(f: A \rightarrow B) \land (\mathbb N \not\sim B) \implies \mathbb N \not\sim A \\
f = \text{surjection} \\
A = \text{domain} \\
B = \text{codomain} 
\end{aligned}
$$

---
