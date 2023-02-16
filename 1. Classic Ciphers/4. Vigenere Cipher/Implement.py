import random
import string

# Generate the alphabet
ALPHABET = string.ascii_lowercase
L = len(ALPHABET)

# Generate the key according to the message
def generate_key(m: str) -> str:
    l = len(m)
    key = ""
    for i in range(l):
        key += ALPHABET[random.randint(0, L - 1)]
    return key

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

p = "rules are made to be broken, like buildings, or people."
# Get the key
key = generate_key(p)
# Encrypt
c = encrypt(p, key)
print("Encrypted :", c)
# Decrypt
m = decrypt(c, key)
print("Decrypted :", m)