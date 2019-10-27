# Algorithm for Diffie-Hellman Key Decoding
g=5
A=1218
p=9433

for a in range(1,p):
    if (A == g**a % p):
        print a 