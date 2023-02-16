# Affine Cipher

Before we get into the definition of Affine Cipher, lets look at some basic math that are involved 

## Math

### Congruence

**Congruence** (đồng dư) is a concept that is used extensively throughout number theory, and one of the most basic one.

We say that $a$ is **_congruent_** to $b$ modulo $m$ if and only if : 

​																				$$a \equiv b \pmod m$$

or what we can easily understand :

+ $m\;|\;a - b $
+ $a\;mod\;m = b\;mod\;m$

### Greatest Common Divisor

Given two non-negative integer $a,b$ , the ***greatest common divisor (GCD)*** of $a, b$ is the **largest** integer $n$ that ***divides both a and b***, we can write this as a function :

​																			$$gcd(a, b) = n,\;\;n\;|\;a,b$$

You can find all of the properties of GCD in [Wikipedia](https://en.wikipedia.org/wiki/Greatest_common_divisor) , here, I will show some useful and important properties the GCD holds :

+ $gcd()$ is a ***commutative*** and an ***associative*** function 
+ $gcd(0, a) = a, \forall a \in \mathbb{N^*}$
+ $gcd(a, a) = a, \forall a \in \mathbb{N^*}$
+ If $gcd(a, b) = n$, there exists two integers $p,q$ such that : $n = ap + bq$ (Calculating $p,q$ can be efficient by usiwng [Extended Euclidean Algorithm](https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm))
+ Finding $gcd(a, b)$ is easy by using [Euclidean Algorithm](https://en.wikipedia.org/wiki/Euclidean_algorithm)

### Least Common Multiple

As the greatest common divisor is introduced, it would be a waste not to introduce the "sibling" of it : Least Common Multiple

Given two non-negative integers $a,b$, the ***least common multiple (LCM)*** of $a,b$ is the **smallest** integer $m$ that ***is divided by both a and b***, we can write this as a similar function :

​																			$$lcm(a,b)=m,\;\;a,b\;|\;m$$

As always, [Wikipedia](https://en.wikipedia.org/wiki/Least_common_multiple) has an apprehensive overview of this, and as our main focus is not the LCM, I will not show much of its properties here. Only one property is noticing :

​																			$$lcm(a, b) = \dfrac{ab}{gcd(a, b)}$$

### Multiplicative Inverse


Given $a$ modulo $n$, we say that an integer $a'$ modulo $n$ is a ***multiplicative inverse*** of $a$ modulo $n$ if :

​																			$$aa' \equiv a'a \equiv 1 \pmod n$$

We define the notation of $a'$ be $a^{-1}$

Finding the inverse is easy using [Extended Euclidean Algorithm](https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm).

One thing to consider is that :

+ If $n$ is not prime, then not all $a$ modulo $n$ has a multiplicative inverse. So if $gcd(a, n) = 1$, then $a$ has a unique multiplicative inverse
+ If $n$ is prime, then every $a$ modulo $n$ has a unique multiplicative inverse, and it turns out to be easier to calculate thanks to [Euler's Theorem](https://en.wikipedia.org/wiki/Euler%27s_theorem).

$$a^{n - 1} \equiv 1 \pmod{n}\;(Euler's\;Theorem)$$ 

$$a^{n-1} . a^{-1} \equiv a^{-1} \pmod{n}$$

$$a^{-1} = a' \equiv a^{n-2} \pmod{n}$$

##  Definition

We are now ready to the definition :

The ***affine cipher*** uses an ***affine function*** (or **linear function**) to encrypt the character in a message.

The length of the alphabet : $L$

The encryption rule $e_{k}(x) = ax+b \pmod L$

The decryption rule $d_k(y) = a^{-1}(y - b) \pmod L$

The key $k \in \mathbb{Z}_L \times \mathbb{Z}_L = (a, b)$

## Remarks

The key consists of 2 integers, so the key space is larger than that of the shift cipher, specifically $|\mathscr{K}| \leq L^2$

What the hell is the meaning of $<$ ? Well unfortunately, there are some conditions that the cipher is unusable. As we learnt about the ***multiplicative inverse***, we know that if $L$ is not prime, then not all integers has a multiplicative inverse, and that is the problem with the decryption rules. So in order to use this cipher, one thing to be consider is :

+ $$gcd(a, L) = 1$$ (it reduces the key space due to the fact that we cannot choose all $a$)
+ $$L$$ is prime (more effective), then $|\mathscr{K}| = L^2$

## Implementation

As usual, implementing the cipher is a must to understand it better.

First, let's define our alphabet (in this case, we just includes the lowercase letters), define the random key with the `gcd function` (observe my Python one line function :) )

```Python
import random
import string
from Crypto.Util.number import *

# Define the alphabet
ALPHABET = string.ascii_lowercase
l = len(ALPHABET)

# Define the gcd function
def gcd(a,b): return gcd(b % a,a) if a else b

# Generate a random key
b = random.randint(0,l)
while True:
    a = random.randint(0, l)
    if (gcd(a, l) == 1):
        break

key = (a, b)
```

Now let's define our `encrypt` and `decrypt` functions :

```Python
# Encrypt function
def encrypt(m: str, key) -> str:
    c = ""
    a, b = key[0], key[1]
    for i in m:
        if i in ALPHABET:
            c += ALPHABET[(a * ALPHABET.index(i) + b) % l]
        else:
            c += i
    return c

# Decrypt function
def decrypt(c: str, key) -> str:
    m = ""
    a, b = key[0], key[1]
    for i in c:
        if i in ALPHABET:
            m += ALPHABET[(inverse(a, l) * (ALPHABET.index(i) - b)) % l]
        else:
            m += i
    return m
```

Testing time ! 

```Python
# Test
m = "fortune doesnt favor fools"
c = encrypt(m, key)
print(c)
p = decrypt(c, key)
print(p)
```



## Attacks

### Bruteforce

The key space of affine cipher is still within the computational power of the computer, so bruteforcing the key is still feasible. And actually the attack is similar to the shift cipher.

```Python
# Brute force attack, more efficient if you know some "format" of the message
def bruteforce_attack(c: str, format:str):
    m_list = []
    for i in range(l):
        if gcd(i, l) == 1:
            for j in range(l):
                possible_plaintext = decrypt(c, (i, j))
                if (format in possible_plaintext):
                    m_list.append(((i, j), possible_plaintext))
    return m_list
```

