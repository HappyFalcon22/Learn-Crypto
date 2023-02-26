# Subtitution Cipher

## Definition

Moving on to a more secure cipher, let :

+ $\mathscr{P} = \mathscr{C} = \mathbb{Z}_{26}$
+ $\mathscr{K}$ consists of all possible permutations of the alphabet $\longrightarrow \left| \mathscr{K} \right| = 26!$
+ For each permutation $\pi \in \mathscr{K}$, define :
	+ $e_\pi(x) = \pi(x)$
	+ $d_\pi(y) = \pi^{-1}(y)$ ($\pi^{-1}$ is called an ***inverse permutation***)

## Remarks

This cipher has a really big key space : $26!$. Although quantum computers nowadays can still bruteforcing 26!, normal modern computers cannot do this in reasonable time.

## Implementation

First, generate the alphabet and a random key (which is the permutaion of the alphabet)

```Python
import random
import string

# Creating the alphabet
ALPHABET = string.ascii_lowercase
key_list = list(ALPHABET)

# Generate the key
random.shuffle(key_list)
key = "".join(i for i in key_list)
```



Next, define the `encrypt` and `decrypt` function

```Python
def encrypt(m: str, key: str) -> str:
    ciphertext = ""
    for i in message:
        if i in ALPHABET:
            ciphertext += key[ALPHABET.index(i)]
        else:
            ciphertext += i
    return ciphertext

def decrypt(c:str, key: str) -> str:
    plaintext = ""
    for i in c:
        if i in ALPHABET:
            plaintext += ALPHABET[key.index(i)]
        else:
            plaintext += i
    return plaintext
```



Testing time !

```Python
message = "I am Trinh Cao Thang and I own google.com"
message = message.lower()
c = encrypt(message, key)
print(c)
p = decrypt(c, key)
print(p)
```

In my implementation, I didn't preserve the uppercase of the original message, will improve my code soon !









