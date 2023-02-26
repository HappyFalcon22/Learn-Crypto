# Typical Iterated Cipher

Before we get into the definition of a generic block cipher, we will look into its smaller component : ***iterated ciphers***

***Iterated ciphers*** are not used as a complete cipher, they are rather used as a part of a block cipher.

## Definition

Let $K$ be a ***random binary key*** of some length $L$. We use $K$ to construct $Nr$ ***round keys*** $\left( K_1, K_2, ..., K_{Nr} \right)$. This process is called ***key schedule***, and it is done by some ***fixed, public algorithms***.

In specific notations, let's define the ***round function*** $g$ :

+ Inputs : the ***round key*** $K_i$, the ***state*** $w_i$

+ Outputs : the ***next state*** $w_{i + 1}$

We will define an iterated cipher using notations :

+ ***General state*** : $w_i$, where $i \in [1, Nr]$
+ ***Plaintext*** : $m = w_0$
+ ***Ciphertext*** : $c = w_{Nr}$

The iterated cipher is defined by the algorithm of encryption / decryption :

## Encryption


$$
w_0 = m \\
w_1 = g(w_0, K_1) \\
w_2 = g(w_1, K_2) \\
w_3 = g(w_2, K_3) \\
... \\
w_{i+1} = g(w_i, K_{i+1}) \\
... \\
w_{Nr} = g(w_{Nr-1}, K_{Nr}) \\
c = w_{Nr}\\
$$

## Decryption

$$
w_{Nr} = c \\
w_{Nr-1} = g^{-1}(w_{Nr}, K_{Nr-1}) \\
w_{Nr-2} = g^{-1}(w_{Nr-1}, K_{Nr-2}) \\
w_{Nr-3} = g^{-1}(w_{Nr-2}, K_{Nr-3}) \\
... \\
w_1 = g(w_2, K_1) \\
... \\
w_0 = g(w_1, K_0) \\
m = w_0\\
$$



## Remarks

+ The nature of the cipher is the loop, hence the name "iterated".
+ The security of the cipher is dependent on the ***round function*** $g$
+ Reminder : the function $g$ should be fixed and publicly known.
+ When we say ***state***, it can be the current state of the plaintext or ciphertext, depending on which scheme, encryption or decryption, we mention.
+ The round function $g$ must be a ***one-to-one function***, specifically :
  $$
  \exists g^{-1} : g^{-1}(g(w, y), y) = w
  $$
  
