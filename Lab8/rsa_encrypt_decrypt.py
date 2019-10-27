def toNumber(c):
    s = ""
    for i in c:
        n = ord(i)-32
        if n < 10:
            s = s + "0" + str(n)
        else:
            s = s + str(n)
    return int(s)

def toString(n):
    t = str(n)
    s = ""
    if len(t) % 2 == 1:
        f = t[0]
        t = t[1:]
        s = chr(int(f) + 32)
    
    for i in range(0, len(t), 2):
        curr = t[i] + t[i+1]
        s = s + chr(int(curr) + 32)
    return s

plain = "Remember, Peace is a lie."
plain = "Pedro Damian Sanchez Jr"

m=toNumber(plain)

# Alice's Key
e=65537L
p=295232799039604140847618609643520000097L
q=8683317618811886495518194401280000037L
n=p*q
toc=(p-1)*(q-1)

# Bob's Key
'''
e=123456789076561
n=578407404780183533635353826919582007028875793327832179789390998726409257859019
'''
c=(m**e)%n

print m,c