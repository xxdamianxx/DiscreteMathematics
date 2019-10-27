import copy

def cartesian_product(X, Y): # This is trivial
    ans = []
    for x in X:
        for y in Y:
            ans.append((x,y))
    return ans

X = [1, 2]
Y = ['a', 'b', 'c']

print cartesian_product(X, Y)

def power_set(X):           # Recursive solution offered here:
    if len(X) == 0:         # If the list is zero elements, then the powerset is just the empty list
        return [[]]         
    else:
        head = X[0]         # Otherwise if we have the powerset of the original list except for the first element
        tail = X[1:]        # We can incorporate the first element into the powerset by appending it to every existing element
        
        res = power_set(tail)
        ans = copy.deepcopy(res)
        
        for i in res:
 
            temp = copy.deepcopy(i)
            temp.insert(0, head)
 
            ans.append(temp)
        
            return ans
        
Z = ['a', 'b', 'c', 'd', 'e']   
     
P = power_set(Z)

print P
print len(P)