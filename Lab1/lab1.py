#Question 1: Implement python functions for all logical operators:

# 1.1 AND (p and q)
def AND(p, q):
    # Provide solution here

# 1.2 OR (p or q)
def OR(p, q):
    # Provide solution here

# 1.3 IF (p -> q)
def IF(p, q):
    # Provide solution here

# 1.4 NOT (-p)
def NOT(p):
    # Provide solution here

# 1.5 IFF (p <-> q)    
def IFF (p, q):
    # Provide solution here


# Question 2:

# Give a prefix representation of a proposition, of the form prop = ('OR', True, False)
# Write a function named evaluate, which will evaluate the proposition
# You should use the functions defined in question 1
def evaluate(formula):
    # Provide solution here
        

# Question 3 (Challenge): Create a new version of your evaluate function, named evaluate_r, which also takes in a formula, but it is able to evaluate composite formulae, such as ('OR', ('NOT', True), ('AND', True, False))
# The example formula above is equivalent to (-True 'OR' (True 'AND' False)) in infix notation 
        
def evaluate_r(formula):
    # Provide solution here
    
    
# Test your functions with the following:

# Basic operations (Question 1)
print "Basic Operations Test"
print
p = True
q = False

print AND(p, q)
print OR(p, q)
print IF(p, q)
print IFF(p, q)
print NOT(p)
print NOT(q)

print 
print "*" * 40  
print

# Simple evaluation function (Question 2)
print "Simple Evaluation Function Test"
print
p = True
q = False   

print "p =", p
print "q =", q

print 
print "(p or q):   ", evaluate (('OR', p, q))
print "(p and q):  ",evaluate (('AND', p, q))
print "(p -> q):   ",evaluate (('IF', p, q))
print "(p <-> q):  ",evaluate (('IFF', p, q))
print "-p:         ",evaluate (('NOT', p))

print 
print "*" * 40  
print

# Recursive evaluation function (Question 3)
print "Recursive Evaluation Function Test"
print
p = False
q = False   

print "p =", p
print "q =", q

print
print "(p or q) or -p: ", evaluate_r(('OR', ('OR', p, q), ('NOT', p)))
print "(p or q) and -p: ", evaluate_r(('AND', ('OR', p, q), ('NOT', p)))

print 
print "*" * 40

