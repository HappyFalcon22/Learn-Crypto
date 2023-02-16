import random
import string
from Crypto.Util.number import *

# Define the alphabet
ALPHABET = string.ascii_lowercase
l = len(ALPHABET)

# Define the gcd function
def gcd(a,b): return gcd(b%a,a) if a else b

# Generate a random key
b = random.randint(0,l)
while True:
    a = random.randint(0, l)
    if (gcd(a, l) == 1):
        break

key = (a, b)

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

# Test
m = "fortune doesnt favor fools"
c = encrypt(m, key)
print(bruteforce_attack(c, "for"))