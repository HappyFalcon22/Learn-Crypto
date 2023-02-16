import random
import string

# Creating the alphabet
ALPHABET = string.ascii_lowercase
key_list = list(ALPHABET)

# Generate the key
random.shuffle(key_list)
key = "".join(i for i in key_list)

message = "I am Trinh Cao Thang and I own google.com"
message = message.lower()

def encrypt(m: str, key: str) -> str:
    ciphertext = ""
    for i in m:
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

p = "In packet 14 sent from laptop to server, there is a Client Key Exchange. Either RSA, various types of DHKE (Diffie-Hellmann Key Exchange), or PSK (Pre-Shared Key) algorithms can be used for key exchange. If RSA is used, then the client generates a random value called the premaster secret, encrypts it using the public key from the certificate sent by the server, and sends this to the server. Both laptop and server now have the means to calculate the master secret and therefore the shared session key, by combining the premaster secret with random values. If Diffie-Hellman is used as the key exchange algorithm, the client and server send each other their Diffie-Hellmann public values, allowing the same premaster secret to be calculated by both sides. TLS 1.3 completely removed the Client Key Exchange step. It is no longer needed thanks to the more limited set of supported algorithms. Only Ephemeral Diffie Hellman key exchanges are supported (plus the much less commonly used PSK). The client now guesses which cipher suite the server will accept, and sends the Diffie-Hellman parameters in the Client Hello. Ultimately this saves a full network roundtrip when establishing a connection, making TLS 1.3 noticeably faster when browsing the Internet."
p = p.lower()
print(p)
c = encrypt(m=p, key=key)
print(c)


