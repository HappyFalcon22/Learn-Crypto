# Implement Shift Cipher
import string
import random

# Define the alphabet
ALPHABET = string.printable

L = len(ALPHABET)

def encrypt(plaintext: str, k: int) -> str:
    ciphertext = ""
    for i in plaintext:
        ciphertext += ALPHABET[(ALPHABET.index(i) + k) % L]
    return ciphertext

def decrypt(ciphertext: str, k: int) -> str:
    plaintext = ""
    for i in ciphertext:
        plaintext += ALPHABET[(ALPHABET.index(i) - k) % L]
    return plaintext

# Bruteforce attack on Shift Cipher (ciphertext-only attack)
# Return all possible plaintext without the format argument
# Return all plaintexts that match the pattern in the format value
def bruteforce_attack(ciphertext: str, format="") -> str:
    L = len(ALPHABET)
    possible_plaintext = []
    for i in range(L):
        k = i
        p = decrypt(ciphertext, k)
        if format == "": # Empty argument
            possible_plaintext.append((k, p))
        else:
            if format in p:
                possible_plaintext.append((k, p))
    return possible_plaintext

m = "A human being is a part of a whole, called by us _universe_, a part limited in time and space. He experiences himself, his thoughts and feelings as something separated from the rest... a kind of optical delusion of his consciousness. This delusion is a kind of prison for us, restricting us to our personal desires and to affection for a few persons nearest to us. Our task must be to free ourselves from this prison by widening our circle of compassion to embrace all living creatures and the whole of nature in its beauty. (Albert Einstein)"
k = random.randint(0, L)
c = encrypt(m, k)
print(bruteforce_attack(c, "Albert Einstein"))