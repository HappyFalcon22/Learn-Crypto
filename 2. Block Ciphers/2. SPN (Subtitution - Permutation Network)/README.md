# Substitution - Permutation Network (SPN)

This is a special type of iterated ciphers.

## Basic Notations

As the name suggests, this network is divided into ***2 main component*** : ***substitution*** and ***permutation***.

These ciphers work on ***blocks***, which is simply a group of bits of the cipher/plaintext.

Assume : The ciphers work on binary data.

Assume $l$ and $m$ are 2 positive integers --> We define the ***block length*** of the cipher to be $l\times m$

The ***substitution component*** :
$$
\pi_s : \{0,1\}^l \longrightarrow \{0,1\}^l \\
$$
The ***permutation component*** :
$$
\pi_p : \left( 1, 2, ..., lm \right) \longrightarrow \left( 1, 2, ..., lm \right)\\
$$

## Remarks

+ $\pi_s$ is called the ***substitution box*** or simple ***S-Box***, which replaces $l$ bits with different $l$ bits.
+ $\pi_p$ permutates $l \times m$ bits.

## Definition

Let $l$ , $m$ and $Nr$ be positive integers, let :

+ The keyspace : $\mathscr{K} = \mathscr{C} = \{0, 1\}^{lm}$

+ The ***substitution component*** :
$$
\pi_s : \{0,1\}^l \longrightarrow \{0,1\}^l \\
$$

+ The ***permutation component*** :
  $$
  \pi_p : \{ 1, 2, ..., lm \} \longrightarrow \{ 1, 2, ..., lm \}\\
  $$
  

