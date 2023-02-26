# CRYPTOGRAPHY DEFINITION

These are the definitions and theorems that I encounter when learning Applied cryptography

## 1. Cryptosystem (Cipher)

A ***cryptosystem*** is a 5-tuple ($\mathscr{P, C, K, E, D}$), where :

+ $\mathscr{P}$ is a finite set of possible $plaintexts$
+ $\mathscr{C}$ is a finite set of possible $ciphertexts$
+ $\mathscr{K}$ is a finite set of possible $keys$, also called the $keyspace$
+ For each $K \in \mathscr{K}$, there is an $encryption\;rule$ $e_K \in \mathscr{E}$ and a ***CORRESPONDING*** $decryption\;rule$ $d_K \in \mathscr{D}$. Each $e_K : \mathscr{P} \longrightarrow \mathscr{C}$  and $d_K : \mathscr{C} \longrightarrow \mathscr{P}$ are functions such that $d_K(e_K(x)) = x$, $\forall x \in \mathscr{P}$.

***Remarks***
+ First learnt definition :)
+ The word ***CORRESPONDING*** is important.
+ Each encryption rule and decryption rule must be ***one-to-one*** functions

## 2. Cryptanalysis

***Cryptanalysis*** refers to the process of analyzing a cipher in order to understand hidden aspects of that cipher, the general goal is to ***find the secret key***.

There are total ***4 models*** for us to analyze a cipher :

### Ciphertext only attack

In this model, the attacker has only the ***ciphertext***. He has to find the key with just the ciphertext only.

### Known plaintext attack

In this model, the attacker has one or more pairs of ***plaintext-ciphertext***. He has to find the key from that pair.

### Chosen plaintext attack

In this model, the attacker has the access of ***the encryption rule***, which means he can choose an arbitrary plaintext and get the corresponding ciphertext.

### Chosen ciphertext attack

In this model, the attacker has the access of ***the decryption rule***, which means he can choose an arbitrary ciphertext and get the corresponding plaintext.

***Remarks***
+ In Ciphertext-only attack, the attacker can have ***multiple ciphertexts***.
+ The difference between Known-plaintext attack and all 2 Chosen attacks is that the attacker cannot chooose which pair of ciphertext-plaintext he is gonna get.