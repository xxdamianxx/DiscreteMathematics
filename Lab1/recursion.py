
def factorial(n):
    if n == 0:
        return 1 # This is the base case, we can solve it directly
    else:
        return n * factorial(n-1)   # This is the recursive step, we express the problem 
                                    # as going from a smaller version of itself to the
                                    # size that we need it to be
        
print "Testing factorial(5):\t\t\t", factorial(5)

def fib(n): 
    if n == 0:         # Here we need two base cases since the recursive step requires
        return 1       # us to go back two sizes, that is (n-1) and (n-2)
    elif n == 1:
        return 1;
    else:
        return fib(n-1) + fib(n-2) # The resursive step
        
print "Testing fib(6):\t\t\t\t",fib(6)


myNums = [23, 54, 12, 657, 89, 908, 54, 34, 23, 534, 5]

# If I only knew the summation of [54,12,657,89,908,54,34,23,534,5]
# I could just add 23 to it, and arrive at the correct answer

def addUp(someList):
    if len(someList) == 1:  # Base case: we have only a single element to add, so the
        return someList[0]  # result is just that element itself
    else:
        return someList[0] + addUp(someList[1:])    # Adding up a list is simply adding the
                                                    # first element of the list, to the
                                                    # result of adding up the remaining elements
        
        
print "Testing addUp(myNums):\t\t\t", addUp(myNums)

# I know that the maximum value will be either 23, or whatever maximum is found in [54,12,657,89,908,54,34,23,534,5]

def findMax(someList):
    if len(someList) == 1:          # Finding the maximum in a list with a single element is easy
        return someList[0]          # It is just that element, since there can be no other choices
    else:
        remainderOfList = someList[1:]              # The maximum of the entire list is either the first element
        maxFromRemainder = findMax(remainderOfList) # or the maximum found by looking at the remaining elements
        if someList[0] > maxFromRemainder:
            return someList[0]
        else:
            return maxFromRemainder


print  "Testing findMax(myNums):\t\t", findMax(myNums)

# Sometimes we have lists of numbers that are not "flat", that is to say, some of the elements in the list are
# numbers, but some elements are themselves lists. These are also known as nested lists:

# Example: A = [1, 2, 3, [4, 5]]
# List A has 4 elements, which are A[0] = 1, A[1] = 2, A[2] = 3, A[3] = [4, 5]

# Our addUp function will not work with list A because the last element in it is not a number. Python does not know
# how to add a number with a list. So if we want to be able to add up nested lists, we need to treat elements that are\
# not numbers, a little differently. The way we treat them is as follows: 

# We have the same addUp procedure as before, but if we ever encounter an element which is a list, we call our 
# function to add it up, before we use it as a number. This works becasuse the result of adding up a list is a number.


def recursiveAddUp(someList):
    if len(someList) == 1:                  # Same base case as before, if we have a single element, it is the answer
        if type(someList[0]) == type(1):    # If that single element it a number (same type as the type of 1)
            return someList[0]              # then nothing changes, we simply return it
        else:
            return recursiveAddUp(someList[0]) # If however the single element we have is itself a list,
    else:                                      # we first add it up, and then return the result of that
        if type(someList[0]) == type(1):
            return someList[0] + recursiveAddUp(someList[1:])   # Again, if the first element is just a number, we can
        else:                                                   # add it to the result of adding up the rest of the list
            return recursiveAddUp(someList[0]) + recursiveAddUp(someList[1:])
                                                                # If however the first element is itself a list,
                                                                # we need to first add it up, before we proceed
                                                                # So now it is the result of adding up the first element
                                                                # added to the result of adding up the rest of the list


# Here is a highly nested list, which adds up to 25
myOtherNums = [[[[[[[[[[[1, [2, [[3], [4]]], [6, 4], 5]]]]]]]]]]]

print "Testing recursiveAddUp(myOtherNums):\t", recursiveAddUp(myOtherNums)
            