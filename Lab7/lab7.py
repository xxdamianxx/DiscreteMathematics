# In lectures we have worked with the 26 letters of the English alphabet, mapping a to 0, b to 1, ..., z to 25, thus working in modulo 26. The ASCII table of characters however has 95 printable characters. In addition to all upper case letters, there are also lower case letters, numbers from 0 to 9, and punctuation symbols. Therefore in labs we will work modulo 95, since there are 95 possible symbols. The 95 printable ASCII characters are numbered from 32 to 126, so we will be numbering them from 0 to 94, by subtracting 32 from each value. The two functions below handle conversions from strings of characters to lists of numbers, and vice versa.
# Convert a string of characters to a list of numbers by taking the ASCII value of the numbers - 32
def chars_to_nums(c):

    nums = []
    for i in c:
        nums.append(ord(i)-32)
    return nums

# Convert a list of numbers to a string of characters by converting the ASCII values + 32 to characters
def nums_to_chars(n):

    chars = ""
    for i in n:
        chars = chars + chr(i+32)
    return chars

  
# Using the functions above, complete the following exercises. You may also find it useful to bring in some functions implemented in previous labs.
# Exercise 1: Implement an encode procedure for the Caesar cipher. It should take in the plaintext as a string, the key as an integer, and a modulus as an integer, which corresponds to the size of the alphabet, and produce the appropriate ciphertext. In most cases the modulus will be 95, since there are 95 printable ASCII characters that we can use. The pair (key, mod) makes up the encryption key.
def caesar_encode(plaintext, key, mod):

    n = chars_to_nums(plaintext)
    encode=[]
    for i in n:
        encode.append((i+key)%mod)
    return nums_to_chars(encode)
    

# Exercise 2: Implement the decode procedure for the Caesar cipher. It should take in the ciphertext and the encryption key, and produce the plaintext.
def caesar_decode(ciphertext, key, mod):

    n = chars_to_nums(ciphertext)
    decode=[]
    for i in n:
        decode.append((i-key)%mod)
    return nums_to_chars(decode)
    
print caesar_decode("KHOOR", 3, 95)
print caesar_decode(caesar_encode("HELLO", 3, 95), 3, 95)


# Exercise 3: Assuming the following string was encoded with the Caesar cipher, using some unknown encryption key, recover the plaintext. Type your answer in the string 'ex_5_plaintext' below, do not include any characters in the string, other than the recovered plaintext:
ex_5_ciphertext = "VXSHUVHFUHW"

for key in range(1, 95):
    print caesar_decode(ex_5_ciphertext, key, 95)

ex_5_plaintext = caesar_decode(ex_5_ciphertext, 3, 95)
print ex_5_plaintext


# Exercise 4: Implement the encode function for the Affine cipher. It should take in the plaintext, along with an encryption key, and produce the ciphertext. In this case the encryption key is the 3-tuple (a, b, m), where m is the modulus, and a, b are integers as shown in lectuers. Remember, for the function to be invertible, a and m need to be relatively prime.
def affine_encode(plaintext, a, b, m):

    n = chars_to_nums(plaintext)
    encode=[]
    for i in n:
        encode.append((a*i+b)%m)
    return nums_to_chars(encode)
        
print affine_encode("HELLO", 7, 23, 95)

def extended_euclid(a, b):

    s=0
    t=1
    r=b
    olds=1
    oldt=0
    oldr=a
    while r!=0:
        q=oldr/r
        oldr,r = r, oldr-q*r
        olds,s = s, olds-q*s
        oldt,t = t, oldt-q*t
    return oldr,[(oldt,b),(olds,a)]

def inverse(n, m):

    ee=extended_euclid(n,m)
    if ee[0] != 1:
        return None
    return ee[1][1][0]

# Exercise 5: Implement the decode function for the Affine cipher. It should take in the ciphertext along with the encryption key, and produce the plaintext.
def affine_decode(ciphertext, a, b, m):

    ai=inverse(a,m)
    if ai==None:
        return ""
    n = chars_to_nums(ciphertext)
    decode=[]
    for i in n:
        decode.append((ai*(i-b))%m)
    return nums_to_chars(decode)
    
print affine_decode("2|NNc", 7, 23, 95)


# Exercise 6: Assuming the following string, stored in 'ex_8_ciphertext', was encoded with an Affine cipher and an unknown encryption key. Recover the plaintext and store it in the string variable 'ex_8_plaintext'

ex_8_ciphertext = "8YM8FlYPiiMl.YP[eYWP[P[P."

print "starting affine"
def allUpper(text):
    for i in text:
        if not ((i>='A' and i<='Z')):
            return False
    return True

for a in range(0, 95):
    for b in range(0, 95):
        if inverse(a,95) != None:
            decode=affine_decode(ex_8_ciphertext, a, b, 95) 
            print a, b, decode 

ex_8_plaintext = affine_decode(ex_8_ciphertext, 74, 94, 95)