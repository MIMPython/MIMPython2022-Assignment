A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
print(A)
#a
A[3] = A[3]**2
#b
A.pop(2)
del A[2]
#c
A.append(A[-1]**2)
#d
print(len (A))
#e
print(sum(A))
#f
tong = A[1] + A[2] + A[3] + A[5]
print(tong)
#g
R1 = A[::-1]
print(R1)
R2 = reversed(A)
print(list(R2))
#h
even = []
odd = []
for i in range(0, len(A)):
	if (A[i]%2 == 0):
		even.append(A[i])
	else:
		odd.append(A[i])
print(even)
print(odd) 
#i
def sort(A):
	size = len(A)
	for i in range(0, size - 1):
		for j in range(i+1, size):
			if (A[i] < A[j]):
				temp = A[j]
				A[j] = A[i]
				A[i] = temp
	return A
B = sort(A)
print(B)
#j
print(A == B)
#k
C = A + B
print(C)