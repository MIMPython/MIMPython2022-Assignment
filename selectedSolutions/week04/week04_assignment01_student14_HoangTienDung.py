A = [[1,2], [3,0,4], [2], [4,5]]
def Sum(array):
	return sum(array)

A.sort(key = Sum)
print(A)