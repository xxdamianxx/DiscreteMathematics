# Exercise 1: Implement Euclid's Algorithm for finding the greatest common divisor of two integers
def gcd(a, b):

    while a != 0:
        (b, a) = (a, b % a)
    return b

print gcd(128, 60) # Expected output: 4


# Exercise 2: Consider the following representation of mathematical expressions: a list of tuples, where each tuple has exactly 2 elements, a coefficient and a term. For example, the expression:
# 2x + 5y - 3z is represented as [(2, x), (5, y), (-3, z)]
# We sometimes need to simplify expressions by grouping together like terms. For example:
# 2x + 5y + 4x = 6x + 5y

# Implement the function groupLikeTerms, where the input exp is a mathematical expression represented as a list of tuples, and it should return a simplified mathematical expression represented as a list of tuples.
def groupLikeTerms(exp):

    out = []

    for a in range(len(exp)):
    	found=False
    	for b in range(len(out)):	
    		if exp[a][1]==out[b][1]:
    			out[b]=(out[b][0]+exp[a][0], out[b][1])	
    			found=True
    	if not found:
    		out.append(exp[a])
    return out
    
print groupLikeTerms([(5, "x"), (5, "y"), (-3, "x")])
# Expected output: [(2, 'x'), (5, 'y')]


# Exercise 3: We sometimes need to substitute expressions into other expressions. For example if we have the expression 2x + 5y, and we know that x = 3a - b, we can substitute the expression for x into the original expression, resulting in: 6a - 2b + 5y.
# Implement the substitution function below. It should take an expression (list of tuples), a term, and another expression. It should substitute the occurences of term in exp, with value. The result should be in its simplest form, i.e. like terms should be grouped together 

# For example: substitute([(2, 5), (-1, 9)], 5, [(1, 23), (-2, 9)]) results in [(-5, 9), (2, 23)]
def substitute(exp, term, value):

	out = []

	for e in exp:
		if term == e[1]:
			for s in value:
				out.append((s[0]*e[0],s[1]))
		else:
			out.append(e)
	return groupLikeTerms(out)
            
print substitute([(2, 5), (-1, 9)], 5, [(1, 23), (-2, 9)])
# Expected output: [(-5, 9), (2, 23)]


# Exercise 4: Using the functions you implemented above, implement the Extended Euclidean Algorithm, which returns the GCD of two integers a, and b, as a linear combination of a and b.

# For example: extended_euclid(101, 23) results in (1, [(22, 23), (-5, 101)]), where the GCD is 1 and it can be expressed as 22*23 - 5*101
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


print extended_euclid(101, 23)
# Expected output: (1, [(22, 23), (-5, 101)])


# Exercise 5: Use the Extended Euclidean Algorithm to implement the function for multiplicative inverses. As you know, a multiplicative inverse n modulo m is guaranteed to exist if n and m are relatively prime. If they are not, your algorithm should return None (which is the null value of Python), otherwise, if n and m are relatively prime, you should return the inverse of n modulo m.
def inverse(n, m):

	ee=extended_euclid(n,m)
	if ee[0] != 1:
		return None
	return ee[1][1][0]

    
print inverse(23, 101)
# Expected output: 22