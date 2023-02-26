# Cryptanalysis of Hill Cipher

## Ciphertext only attack

Given the ciphertext only, it really depends on the size of the message and the size of the alphabet.

+ Assume the length of the message is $L_m$, and the length of the alphabet is $L_A$
+ The key will be the matrix of $L_m$ elements
+ So the key-space will be $L_m^{L_A}$

Normally, the computer will perform in reasonable time if the number of iteration is less than a billion (which is $10^{12}$). If the alphabet is large ($50$ or more based on my experience), then brute-force method is infeasible. 

Naturally, if you know that the alphabet is small, and the message is relatively small, then you can use brute-force method to retrieve the key.

## Known plaintext attack

You have the plaintext and the corresponding ciphertext :

+ Plaintext : $m$
+ Ciphertext : $c = mk$

You can completely retrieve the key by calculating :

$$
m^{-1}c = m^{-1}mk = k
$$

This attack is only feasible if $det(m) > 0$ and $gcd(det(m), L_A) = 1$

If these conditions are met, then using the above method cannot recover the key. So a generalized method is used :

### Attack

Assume the plaintext : 
$$
m = 
\left(
\begin{array}
	m_{11} & m_{12} & m_{13} & ... & m_{1n} \\
	m_{21} & m_{22} & m_{23} & ... & m_{2n} \\
	... & ... & ... & ... & ... \\
	m_{n1} & m_{n2} & m_{n3} & ... & m_{nn} \\
\end{array}
\right)
$$


Assume the ciphertext :
$$
c = 
\left(
\begin{array}
	c_{11} & c_{12} & c_{13} & ... & c_{1n} \\
	c_{21} & c_{22} & c_{23} & ... & c_{2n} \\
	... & ... & ... & ... & ... \\
	c_{n1} & c_{n2} & c_{n3} & ... & c_{nn} \\
\end{array}
\right)
$$
I will present the way to recover the ***i-th*** column of the key, the rest columns is similar :

+ Form an augmented matrix with the matrix $m$ and the ***i-th*** column $c_i$ :

$$
A_i =
\left(
\begin{array}
	m_{11} & m_{12} & m_{13} & ... & m_{1n} & | & c_{1i} \\
	m_{21} & m_{22} & m_{23} & ... & m_{2n} & | & c_{2i} \\
	... & ... & ... & ... & ... & | & ... \\
	m_{n1} & m_{n2} & m_{n3} & ... & m_{nn} & | & c_{ni} \\
\end{array}
\right)
$$

+ Solve the system of equations in modulo $L_A$, the result should be like this :

$$
A_i =
\left(
\begin{array}
	1 & 0 & 0 & ... & 0 & | & \textcolor{yellow}{k_{1i}} \\
	0 & 1 & 0 & ... & 0 & | & \textcolor{yellow}{k_{2i}} \\
	... & ... & ... & ... & ... & | & \textcolor{yellow}{...} \\
	0 & 0 & 0 & ... & 1 & | & \textcolor{yellow}{k_{ni}}
\end{array}
\right)
$$

+ Do this with $i \in [1, n]$, and we will get the complete key matrix



### Implementation

I have implemented the attack on [this file](Known Plaintext Attack.ipynb)

Feel free to explore.

## Chosen plaintext attack

So we get to choose one plaintext that we can think, and we will in turn get the corresponding ciphertext.

This is easy, we just need to send the ***identity matrix*** $I$, what we get is the key : 
$$
c = mk = Ik = k
$$
I probably dont need to implement this, it is too obvious

## Chosen ciphertext attack

In a similar manner to the Chosen Plaintext Attack, we can send the ***identity matrix*** $I$, what we get is the **inverse key** :
$$
m = ck^{-1} = Ik^{-1} = k^{-1}
$$

## Note

If in some challenges, we are forbidden to send the identity matrix to the server, just send some random matrix $m$ to the server, you will get the ciphertext $c$, which can totally be attacked by Known Plaintext Attack using the method I mentioned above.

