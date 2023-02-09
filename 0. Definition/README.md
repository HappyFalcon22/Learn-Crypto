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