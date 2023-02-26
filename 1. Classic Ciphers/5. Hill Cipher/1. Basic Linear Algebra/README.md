# Basic Linear Algebra

Before we get into the ***Hill Cipher***, we first look around some of the basis about linear algebra : Matrices, categories of matrix, Matrix addition - subtraction - multiplication, determinants, traces, and systems of equations.

## Matrix (common notations)

We will use the notations throughout my notes :

+ The matrix $m \times n$ size, in $\mathbb{R}_{m \times n}$

+ Elements in the matrix :

	$$
	\begin{pmatrix}
		a_{11} & a_{12} & ... & a_{1n}\\
		a_{21} & a_{22} & ... & a_{2n}\\
		... & ... & ... & ...\\
		a_{m1} & a_{m2} & ... & a_{mn}\\
	\end{pmatrix}
	$$

+ If $m = n$, we say the matrix to be a ***square matrix***

## Special Matrix

### Identity matrix

+ ***Identity matrix*** is a ***square matrix*** where all elements in the main diagonal equals to ***1***, the rest equal to ***0***

$$
\begin{pmatrix}
		1 & 0 & ... & 0\\
		0 & 1 & ... & 0\\
		... & ... & ... & ...\\
		0 & 0 & ... & 1\\
\end{pmatrix}
$$

+ We notate this matrix $I$

### Triangular matrix

+ ***Upper triangular matrix*** is a ***square matrix*** whose all of the elements ***below*** the main diagonal are equal to ***0***. For example : (6 x 6 matrix)

$$
\begin{pmatrix}
		\textcolor{yellow}{1} & -9 & 6 & 0 & 4 & 0\\
		0 & \textcolor{yellow}{6} & 8 & 19 & 4 & 6\\
		0 & 0 & \textcolor{yellow}{10} & -4 & 4 & 7\\
		0 & 0 & 0 & \textcolor{yellow}{-8} & 4 & 3\\
		0 & 0 & 0 & 0 & \textcolor{yellow}{16} & 2\\
		0 & 0 & 0 & 0 & 0 & \textcolor{yellow}{23}\\
\end{pmatrix}
$$

+ ***Lower triangular matrix*** is a ***square matrix*** whose all of the elements ***above*** the main diagonal are equal to ***0***. For example : (6 x 6 matrix)

$$
\begin{pmatrix}
		\textcolor{yellow}{1} & 0 & 0 & 0 & 0 & 0\\
		0 & \textcolor{yellow}{6} & 0 & 0 & 0 & 0\\
		7 & 0 & \textcolor{yellow}{10} & 0 & 0 & 0\\
		0 & 0 & 8 & \textcolor{yellow}{-8} & 0 & 0\\
		-5 & 6 & 10 & -2 & \textcolor{yellow}{16} & 0\\
		5 & 4 & 12 & 1 & 1 & \textcolor{yellow}{23}\\
\end{pmatrix}
$$



### Symmetric matrix

***Symmetric matrix*** are matrices that remain the same after transposition, which means :  $A^T = A$. For example :

$$
A = 
\begin{pmatrix}
1 & 2 & 5 \\
2 & 10 & 7 \\
5 & 7 & 1 \\
\end{pmatrix}
\Longrightarrow A^T = A
$$

### Diagonal matrix

***Diagonal matrix*** are ***symmetric matrix*** with all the elements not on the main diagonal all equal to ***0***. For example :

$$
\begin{pmatrix}
		\textcolor{yellow}{1} & 0 & 0 & 0 & 0 & 0\\
		0 & \textcolor{yellow}{6} & 0 & 0 & 0 & 0\\
		0 & 0 & \textcolor{yellow}{10} & 0 & 0 & 0\\
		0 & 0 & 0 & \textcolor{yellow}{-8} & 0 & 0\\
		0 & 0 & 0 & 0 & \textcolor{yellow}{16} & 0\\
		0 & 0 & 0 & 0 & 0 & \textcolor{yellow}{23}\\
\end{pmatrix}
$$

## Matrix Operations

### Addition - Subtraction

When doing ***addition / subtraction***, you basically ***add / subtract*** each elements on the same position of the two matrices. For example :

$$
\begin{pmatrix}
8 & 1 & -9\\
5 & 2 & 1\\
\end{pmatrix}
+
\begin{pmatrix}
1 & 2 & 3\\
4 & 5 & 6\\
\end{pmatrix}
=
\begin{pmatrix}
8 + 1 & 1 + 2 & -9 + 3\\
5 + 4 & 2 + 5 & 1 + 6\\
\end{pmatrix}
=
\begin{pmatrix}
9 & 3 & -6\\
9 & 7 & 7\\
\end{pmatrix}
$$

The two matrix must be on the same size.

Addition and subtraction are called ***element-wise operations***

### Multiplication

Multiplication is more complex. Given 2 matrix $A \in \mathbb{R}_{m \times p}$ and $B \in \mathbb{R}_{p \times n}$ and define $C = A \times B $ or $C = AB$ :

+ $C_{ij} = \sum_{k = 1}^{p}a_{ik}*a_{kj}$
+ $C$ has a size of $m \times n$

## Matrix Transformations

When you apply a transformation on the matrix $A$, you basically do the multiplication : $A'=MA$, where $M$ is called ***transformation matrix*** (in this note, I will just present the $2 \times 2$ matrix)

### Rotation

$$
M = 
\begin{pmatrix}
	\cos{\theta} & -\sin{\theta} \\
	\sin{\theta} & \cos{\theta} \\
\end{pmatrix}
\\
$$

### Stretching

+ If you want to stretch along the ***x-axis*** :

$$
M = 
\begin{pmatrix}
	k & 0 \\
	0 & 1 \\
\end{pmatrix}
\\
$$

+ If you want to stretch along the ***y-axis*** :
$$
M = 
\begin{pmatrix}
    k & 0 \\
    0 & 1 \\
\end{pmatrix}
\\
$$

### Squeezing

$$
M = 
\begin{pmatrix}
    k & 0 \\
    0 & \dfrac{1}{k} \\
\end{pmatrix}
\\
$$

### Shearing

$$
M = 
\begin{pmatrix}
    1 & k \\
    0 & 1 \\
\end{pmatrix}
\\
$$

## Determinants

The ***determinant*** of a matrix is a ***scalar value*** that represents some of the properties of a matrix. It helps us in finding the ***inverse matrix***, solving a ***system of equations***,... Denoted as $det(A)$ or $|A|$.

The formal formula for calculating determinants is sited as follow :

Given $A_{m \times m} \in \mathbb{R}_{m \times m}$ . The ***determinant*** of A or $det(A)$ is defined as :

+ If $m = 1$, $det(A) = a_{11}$
+ If $m = 2$, $det(A) = a_{11}a_{22} - a_{12}a_{21}$
+ If $m > 2$, we choose an arbitrary $i \leq m$, then :
$det(A) = \sum_{j=1}^{m}(-1)^{i + j}a_{ij}det(A{i,j})$

***Note*** that only ***square matrix*** have ***determinant***

If a matrix has its determinant equals to ***0***, it is called a ***SINGULAR MATRIX***.

## Inverse matrix

An ***inverse matrix*** of a ***square matrix*** $A_{m \times m}$ is a matrix $A'_{m \times m}$ such that : 
$$
AA' = I \longrightarrow A' = A^{-1}
$$
The matrix has its inverse if its ***determinant*** is not zero.

So how can we calculate the inverse matrix ? ...

## Matrix Properties

+ ***Associative*** under ***addition/subtraction*** : $A \pm B = B \pm A$
+ ***Commutative*** under ***addition/subtraction/multiplication*** : 
  $$
  A + B + C = (A + B) + C = A + (B + C)\\
  ABC = A(BC) = (AB)C
  $$
  

## Solving system of equations



## SageMath For Matrix

Although Python has package `numpy`, which defines all necessary function and classes for matrices, I want to use a more powerful Python-based platform to manipulate matrix with equal difficulty but much more useful for future coding, that is ***SAGEMATH***.

### Declare a matrix

### Perform basic operations

### Solving system of equations

### Determinants and Inverse matrix

### Matrix under $\mathbb{Z}_n$



