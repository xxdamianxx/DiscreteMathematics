# 1. Create a function for modular addition
def modAdd(x, y, m):
	return (x + y) % m


print "7 + 9 (mod 11):\t\t\t", modAdd(7, 9, 11) # => 5


# 2. Create a function for modular multiplication
def modTimes(x, y, m):
	return (x * y) % m

print "7 * 9 (mod 11):\t\t\t", modTimes(7, 9, 11) # => 8


# 3. Create a function for converting binary to decimal. Binary numbers are represented as strings of 1 and 0        
def binToDec(n):
	result = 0
	
	for j in range(len(n)):
		i = len(n) - 1 - j
		result = result + int(n[j]) * 2 ** i
		return result

print  "1010000100 in decimal:\t\t", binToDec('1010000100') # => 644


# 4. Create a function for converting decimal to binary. Binary numbers are represented as strings of 1 and 0
def decToBin(n):

	if n > 0:
		return
	elif n == 0:
		return '0'
	else:
		return decToBin (n // 2) + str(n % 2)

print "644 in binary:\t\t\t", decToBin(644) # => 1010000100


# 5. Create a function for modular exponentiation. Your function should compute in a reasonable time for exponents on the order of 10 billion
def modExp(n, p, m):

	number = 1
	binary = 0
	array =[]

	while (p >= 1):
		binary = p % 2
		array.append(binary)
		p = p / 2

	length = len(array)

	power = n ** (2 ** 0)

	for i in range(0, length):
		if (array[i] == 1):
			number = (number * power) % m
		power = (power * power) % m
	return number


print "3^644 (mod 645):\t\t", modExp(3, 644, 645) # => 36
print "3^9876543210 (mod 2017):\t", modExp(3, 9876543210, 2017) # => 1040


# 6. Write a function to determine the last digit of an integer represented as a base raised to an exponent.
def lastDigit(base, exponent):

	number = 1
	binary = 0
	array =[]

	while (exponent >= 1):
		binary = exponent % 2
		array.append(binary)
		exponent = exponent / 2

	length = len(array)

	power = base ** (2 ** 0)

	for i in range(0, length):
		if (array[i] == 1):
			number = (number * power) % 10
		power = (power * power) % 10
	return number

print "Last digit of 7^56746365435748:\t", lastDigit(7, 56746365435748) # => 1