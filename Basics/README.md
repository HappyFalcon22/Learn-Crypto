
# Basic Knowledge to start on Crypto
This series covers some important concepts and provide codes to conveniently use in Python
Index table :
+ Data types 
+ Data types conversion 
+ JSON Format and Communicate through Netcat 
+ Data Format 
+ XOR Operation

### Integer (Base 10) ###

Integer, probably not gonna cover much here cause its quite obvious.
In Python, we declare as follow : 
```Python
some_int = 394463287463287623846238746723846723
print(type(some_int))
```

### Hex (Base 16) ###

Hex(or hexadecimal) has 6 additional digits : ```a b c d e f```
In Python, we add a little prefix ```0x``` or ```0X```:
```Python
some_hex = 0x1a384394afcce31c3e
print(type(some_hex))
```
However, Python will understand that ```some_hex``` variable's type is integer.

### Binary (Base 2) ###

Binary, the easiest one, contains only 0 and 1. 
In Python, we add a prefix ```0b``` or ```0B```:
```Python
some_bin = 0b0101010101010101000
print(type(some_bin)) #Still outputs as int
```
### Bytes (Base 256) ###

Bytes, the most common type that used in storing data, a byte's value is as the folling format : ```\x??``` (with ```??``` as the value in hex, so its gonna be 256 different values for a byte).
In Python, we wrap the byte in ```b""``` (double or single quotation marks both work fine)
```Python
some_byte = b"\x12\x2a\x10"
print(type(some_byte))
```
Some special values of a byte can be represented as a character in ASCII (use [ASCII table](https://www.asciitable.com/) as a reference).
### ASCII (Base 128) ###

Now you now bytes type, ASCII will be the easy one, in Python, it is represented as a string (wrapped in ```""```):
```Python
some_str = "Hello~"
print(type(some_str))
```
Note: An ASCII character needs 7 bits, not 8 as bytes.

### Base64 ###
Base64 is a common data type, learn it in [Base64 wiki](https://en.wikipedia.org/wiki/Base64) as a reference.
In Python, we can represent base64 as a string, there will be a tool that convert this Base64-wrapped-in-string:
```Python
some_b64 = "bGlnaHQgd29yay4="
```
The last character is quite important for newbie to detect a base64 string:
+ ```=``` : Number of padding is 1
+ ```==``` : Number of padding is 2
+ A character : No padding is needed
Remember why we need padding in base64 while learning it!

### Conversion ###

Okay, so we went through a handful of data types (binary, decimal, hexadecimal, base64, bytes, ASCII), now we are going to convert them.
+ Python is smart, if we use the prefix ```0x``` and ```0b``` on binary and hex, Python will secretly convert it to integer :
```Python
a = 0x1a
b = 0b1011
print(a + b) # Result is an integer. Try it!
```
+ What if we represent hex and binary in string format ? We have just a function to do this , it is ```int(str, base)```:
```Python
a = "011011010101"
b = "1a2a3a4a5a"
c = (int(a, 2), int(b, 16)) # c is a tuple
print(c)
```
+ How about base64 to ASCII ? You need to import a ```base64``` package to do this:
```Python
import base64
a = "bGlnaHQgd29yay4="
b = base64.b64decode(a)
print(b)
```
Some CTF challenges are as simple as these tasks.

+ How about int to ASCII character ? One thing to ensure is that the int value to ASCII should be readable. We can use ```chr(int)``` to convert an integer to ASCII character, the opposite direction is used by the ```ord(str)``` function:
```Python
a = 'y'
b = ord(a)
c = chr(b)
print(b, c)
```

+ In crypto, the number we are dealing with are kinda large (above 100 digits or so). One way to convert these large number is the function ```Long_to_bytes(longint)``` and ```bytes_to_long(bytes)``` functions (need to import a package):

```Python
a = 6734985634895643856345973465873465384658346583956348562983563984652398563948456438576349856347856349857643859734658347658743658932465923785634298563478563487563784628461247621846214816472136482364823461
b = long_to_bytes(a)
c = bytes_to_long(b)
print(b, c)
```
That's probably all the conversion techiques you will need, there are more ways to do conversions like these and I suggest choosing the conversions that you feel comfortable working with.
### JSON Format ###

JSON format is similar to JavaScript format and it is called a dict type in Python:
```{"str": value}```
The ```value``` can be a string, an array, a number, etc... Depend on how you use it.

### Netcat Communication ###

In CTF Crypto challenge, we will frequently deal with "communication" challenge, where we will interact to gather information to do attacks to solve the challenge. You can read the (Netcat reference)[https://en.wikipedia.org/wiki/Netcat].
In this section, I will cover the Python code for doing Netcat. Basically most Netcat message that we interract are in JSON Format:
```Python
#!/usr/bin/env python3

import telnetlib
import json

HOST = "socket.cryptohack.org"
PORT = 13370




def readline():
    return tn.read_until(b"\n")

def json_recv():
    line = readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    tn.write(request)

tn = telnetlib.Telnet(HOST, PORT)
# Your interaction code
tn.close()
```
There are of course many more methos to do netcat communication, but this method is particularly useful in dealing challenges in Cryptohack. And Cryptohack also has a challenge to teach you about using this method to solve challenges.

### XOR Operation ###

The first simplest operation we will learn in Crypto is XOR (or Exclusive-OR) $\xor$

### XOR Properties ###
### DER Format ###
### PEM Format ###
### PUB Format ###

