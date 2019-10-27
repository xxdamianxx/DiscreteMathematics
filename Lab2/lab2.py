def cartesian_product(X, Y):
# provide your code here
	result=[]
	for r in range(len(X)):
		row=[]
		for c in range(len(Y)):
			cell=[X[r],Y[c]]
			row.append(cell)
		result.append(row)
	return result

X = [1, 2]
Y = ['a', 'b', 'c', 'd']

print cartesian_product(X, Y)

def power_helper(X, result):
	if len(X)==0:
		return
	result.append(X)
	for i in range(len(X)):
		subset=list(X)
		#print(subset, i)
		del subset[i]
		power_helper(subset, result)

def power_set(X):
	# provide your code here
	result=[]
	power_helper(X,result)
	result.append([])
	return result      
        
print power_set(Y)