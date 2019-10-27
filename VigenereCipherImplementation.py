# Vigenere Cipher Implementation from https://repl.it/OBOJ/15

def char_to_num(c):
    return ord(c)
    
def num_to_char(n):
    return chr(n)
    
def vig_encode(message, key):
    nums = []
    for c in message:
        nums.append(char_to_num(c))
    
    mlen = len(message)
    klen = len(key)
    
    d = mlen / klen
    r = mlen % klen

    if r > 0:
        if d == 0:
            for i in range(klen - mlen):
                nums.append(ord(" "))
        else:
            for i in range(klen - r):
                nums.append(ord(" "))
        
    loop = len(nums) / len(key)
    
    for i in range(loop):
        for j in range(len(key)):
            x = j+i*(len(key))
            nums[x] = (nums[x] + key[j]) % 256
            
    return nums   
    
def vig_decode(nums, key):
    loop = len(nums) / len(key)
    
    for i in range(loop):
        for j in range(len(key)):
            x = j+i*(len(key))
            nums[x] = (nums[x] - key[j]) % 256
            
    message = ""
    
    for i in nums:
        message = message + num_to_char(i)
        
    return message
    
    
print """To encode a message use:

vig_encode(message, key)

where message is a string of characters, and key is a list of numbers

To decode a message use:
  
vig_decode(ciphertext, key)

where cipher text is a list of numbers, and key is a list of numbers

"""