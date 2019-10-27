# Recursive algorithms demo

# Factorial is the "Hello World" of recursive functions
# It is defined as; n! = n * (n-1)!, where 0! = 1

def factorial(n):
    if n == 0:      # The base case of 0!
        return 1    # the answer is 1
    else:           # If n > 0, we compute factorial in terms of smaller factorials
        return n * factorial(n-1)

# Test our function above with the input 5        
print "factorial(5):\t\t\t\t", factorial(5) 
    
#----------------------------------------------------------------------------------

# Here is another recurrence relation, f(n) = 3 * f(n-1) - 1, f(0) = 1   
def f(n):
    if n == 0:      # Base case when n = 0
        return 1    # the answer is 1
    else:           # Otherwise execute recursive step
        return 3 * f(n-1) - 1 

# Test our function above with the input 5         
print "f(5):\t\t\t\t\t", f(5)
        
#----------------------------------------------------------------------------------

# The functions above were simply translations of known recurrence relations into
# a programming language (Python).

# We can also use recursion to solve problems. We can apply the divide and conquer
# principle to a wide variety of problems. The steps of divide and conquer are:
# 1. Split the problem into smaller sub-problems, that are easier to solve
# 2. Solve the sub-problems (possibly by applying divide and conquer to them as well)
# 3. Combine the solutions of the sub-problems to obtain an overall solution

# A recursive function to raise a number to an exponent.
# We apply the divide and conquer principles here by recognizing that it is easy
# to raise something to the power of 0. The answer is one, no matter what the base is.
# This is the base case, which is trivial to solve.
# We also recognize that solving the problem for exponent n is easier if we knew
# what the solution for n-1 is. That is x^n = x * x^(n-1). So if we know what x^(n-1)
# is, we can just multiply it by x and obtain a solution for x^n.        
def power(x, n):
    if n == 0:      # If the exponent is 0 then it is easy
        return 1    # The answer is 1 (anything to the power of 0 is 1)
    else:
        return x * power(x,n-1)     # If the exponent is more than 0, we use the
                                    # fact that x^n = x * x^(n-1)
        
# Test our function above by computing 2^3        
print "power(2, 3):\t\t\t\t", power(2, 3)

#----------------------------------------------------------------------------------

# Recursion is naturally suited to solving problems involving lists because
# typically the problem that we are trying to solve for a list, is very easy
# to solve for a list of a single element. This is naturally the base case.

# The recursive step is usually taking the first element of a list and integrating
# it into the solution of the problem for the remainder of the list. That is to say
# we integrate the head into the solution of the tail.

# This strategy can be applied for the following algorithms dealing with lists

# This list will be used to test the functions we develop
myList = [5, 7, 1, 6, 3, 8, 2, 4]

# Add up the elements of a list
# Here we recognize that in the base case we have a list made up of 1 element.
# Adding up such a list is trivial. The sum is equal to the element itself.

# If we assume that we can solve the problem for (n-1) elements, incorporating
# another element is accomplished by just adding it to the result. In other words
# the solution for adding up a list of n elements is to add the first element (head)
# to the result of adding up the rest of the list (tail).

def add(list):
    if len(list) == 1:      # Base case, our list has one element, so we return it
        return list[0]
    else:
        return list[0] + add(list[1:])  # Add the first element to the result of 
                                        # adding up the tail of the list
        
# Test our function above by adding up [5, 7, 1, 6, 3, 8, 2, 4]
print "add([5, 7, 1, 6, 3, 8, 2, 4]):\t\t", add(myList)

#----------------------------------------------------------------------------------

# Find a specific element in the list

# We can apply divide and conquer here by recognizing that if the list is empty
# then it can not possibly contain the element we are searching for. This is a
# good base case. You can also have a base case where the length of the list is 1,
# then you would have to check if that one element is the one you are looking for
# but it is easier to just have lists of length 0 as the base case.

# If we have more than 0 elements, then check if the first one (the head) is the one
# we are looking for. If it is then we can return True, otherwise we should search
# for the element in the remainder of the list.

def search (element, list):
    if len(list) == 0:  # An easy base case
        return False    # No empty list can contain the element we are looking for
    else:
        if list[0] == element:  # If the list has elements, is the first of them
            return True         # the one we are looking for? If so, return True
        else:
            return search(element, list[1:]) # Otherwise, we look for it in the tail

# Try to find the number 3 in the list [5, 7, 1, 6, 3, 8, 2, 4]          
print "search(3, [5, 7, 1, 6, 3, 8, 2, 4]):\t", search(3, myList)

#----------------------------------------------------------------------------------

# Here is an alternative solution to the searching problem. It requires us to have
# a base case where the list is one element long. If the element is the one we seek,
# we can return true, otherwise we can return false, since if the list has only one
# element and it is not the one we are looking for, then we know for sure that list
# does not contain our element.

# In case the list has more than one element, we simply split it in half and we
# search each half saparately. If we find it in the first half, or we find it in
# the second half, then we should return true. If on the other hand, we fail to
# find it in the first half and we fail to find it in the second half, we will
# return false

def search2 (element, list):
    if len(list) == 1:          # The base case, where the list has only one element
        if list[0] == element:  # If that element is the one we are looking for
            return True         # Then return true
        else:                   # Otherwise
            return False        # return false
    else:                       # In the case that we have more than one element
        mid = len(list)/2       # Split the list in two halves
        first = list[:mid]      # Search each half separately
        second = list[mid:]     # Return the OR of the results of the two subproblems
        return search2(element, first) or search2(element, second)
        # Why the OR? Because the OR expression will be true if either of the searches
        # are successful, and false if both searches are unsuccessful

# Try to find the number 27 in the list [5, 7, 1, 6, 3, 8, 2, 4]        
print "search2(27, [5, 7, 1, 6, 3, 8, 2, 4]):\t", search2(27, myList)
    
#----------------------------------------------------------------------------------

# Sort the elements of the list in acsending order

# Divide and conquer is also applicable to sorting numbers in order. In fact some of
# the most famous sorting algorithms are divide and conquer algorithms, eg. mergesort

# The idea is that we can sort a list with one element very easily, the list is already
# sorted, so we return it unchanged. This is the base case.

# If we have more than one element, say n elements, let us assume that we can sort (n-1)
# elements. If I have a sorted list of (n-1) elements, how can I incorporate the last
# element in the solution? For example, consider the list [3, 4, 6, 7] and insert 5.
# When inserting, we have to maintain the list sorted, so I can't put the 5 in the
# beginning or at the end of the list. I need to put it between the 4 and the 6.
# In other words, I have to insert it before the first element that is bigger than it.

# Here is a function that can do that

def loop_insert(element, sorted):
    index = 0;  # Assume the position where I need to insert is 0
    while (index < len(sorted) and sorted[index] < element): 
        # As long as I have not hit the end of the list and the element I am
        # currently looking at is smallet than the one I want to insert,
        # I keep increasing the value of index
        index = index + 1
    # At the end of the loop, the value of index will correcpond to the position
    # of the first element in the list which is larger than the element I am inserting
    # So I should insert the element in that place
    sorted.insert(index, element)
    # And return the new list
    return sorted
        
        
# We can also come up with a recursive solution for the insertion into a sorted list
# Remember the requirement that when we insert, the list has to remain sorted.
# A suitable base case is when we insert into an empty list. We just insert the element
# and we end up with a list of one element, which is by definition sorted. So we have
# fulfilled the requirement of maintaining sorted order after the insertion.

# For the recursive step we recognize the following: If the number I want to insert is
# smaller than the first element in the list, then I need to insert my number at the 
# beginning. If that is not the case, the solution is then to take a list made up of the
# first element only, and concatenate it to the result of inserting the element in the
# tail of the list.

# Here is the code that does this:
def insert(element, sorted):

    if len(sorted) == 0:    # If we have an empty list, inserting something in sorted order
        return [element]    # is easy, just make a list containing only the element
    else:                   # If we have more than an empty list, we look at the firts element
        if sorted[0] >= element:    # If it is greater, then we need to insert to position 0
            new_copy = sorted[:]    # Make a copy of the sorted list (!!!You have to do this!!!)
            new_copy.insert(0, element) # Insert the element in position 0 of the newly copied list
            return new_copy             # Return the new list
        else:
            # If the element does not belong in the first position (position 0), then the 
            # solution is to take a list made up of the firts element, and concatenate this to the
            # result of inserting the element into the tail of the list.
            return [sorted[0]] + insert(element, sorted[1:])

# Now that we have a way of inserting an element into an ordered list and maintaining that order,
# we can easily sort a list of numbers

# First recognize that sorting a list of only one element is trivial. So do it for the base case.
# Then simply take the tail of the list, sort it, and then insert the head into the sorted tail.

def sort(list):
    if len(list) == 1:  # This is tha base case
        return list
    else:
        head = list[0]  # Split the list into a head and a tail
        tail = list[1:]
        
        temp = sort(tail)   # Sort the tail
                            # Insert the head in the sorted tail
                            
        # We have two versions of the insert method above. The recursive one is called insert
        # and the iterative one is called loop_insert. You can comment out one or the other,
        # the end results will be the same.
        return insert(head, temp)
        #return loop_insert(head, temp)
        
# Try sorting the list [5, 7, 1, 6, 3, 8, 2, 4]
print "sort([5, 7, 1, 6, 3, 8, 2, 4]):\t\t", sort(myList)