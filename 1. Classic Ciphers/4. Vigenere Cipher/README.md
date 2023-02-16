# Vigenere Cipher

This cipher does not need any math. But it is special compare to ***shift cipher, affine cipher*** and ***subtitution cipher***

## Definition

Let $m$ be a positive integer.

Define $\mathscr{P} = \mathscr{C} = \mathscr{K} = \left( \mathbb{Z}_{L} \right)^m$

The key $k = (k_1, k_2, ..., k_m)$

The encryption rule $e_k(x_1, x_2, ..., x_m) = (x_1 + k_1, x_2 + k_2, ..., x_m + k_m)$

The decryption rule $d_k(y_1, y_2, ..., y_m) = (y_1 - k_1, y_2 - k_2, ..., y_m - k_m)$

All operations are made under modulo $L$

## Remarks

It has a property of a ***stream cipher***, which means that it will create a key of the same length of the message.

It is special : soon you will see that

+ A letter can be encrypted to more than one letters.
+ Many different letters can be encrypted to just one letter.

$\longrightarrow$ It is called the ***POLYALPHABETIC CIPHER***, whereas the shift, subtitution and affine ciphers are called ***MONOALPHABETIC CIPHERS***

+ In practice, the length of the message does not count the `space`.

## Implementation

First, define our alphabet (which is just the lowercase letters)

```Python
import random
import string

# Generate the alphabet
ALPHABET = string.ascii_lowercase
L = len(ALPHABET)
```



Next, generate our key corresponding to the length of the message

```Python
# Generate the key according to the message
def generate_key(m: str) -> str:
    l = len(m)
    key = ""
    for i in range(l):
        key += ALPHABET[random.randint(0, L - 1)]
    return key
```



Now define the `encrypt` and `decrypt` functions :

```Python
def encrypt(m: str, k: str) -> str:
    c = ""
    for i in range(len(m)):
        if m[i] in ALPHABET:
            c += ALPHABET[(ALPHABET.index(m[i]) + ALPHABET.index(k[i])) % L]
        else:
            c += m[i]
    return c

def decrypt(c: str, k: str) -> str:
    m = ""
    for i in range(len(c)):
        if c[i] in ALPHABET:
            m += ALPHABET[(ALPHABET.index(c[i]) - ALPHABET.index(k[i])) % L]
        else:
            m += c[i]
    return m
```



Let's test it (do you know whose quote is that ? :) ) :

```Python
p = "rules are made to be broken, like buildings, or people."
# Get the key
key = generate_key(p)
# Encrypt
c = encrypt(p, key)
print("Encrypted :", c)
# Decrypt
m = decrypt(c, key)
print("Decrypted :", m)
```



## Tool

There are one best tool I know until now , which is [dcode.fr](https://www.dcode.fr/), it does more than just Vigenere Cipher, probably we wont need other tools for now.

## Attack

There are several ***COMPLEX*** attacks that are not suitable enough to ***efficiently*** break the cipher. So I will research them soon.

