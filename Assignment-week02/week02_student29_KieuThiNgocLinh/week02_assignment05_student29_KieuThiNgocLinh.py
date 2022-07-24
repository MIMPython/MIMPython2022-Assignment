A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
A[4]=A[4]**2
print(A)

A.pop(4)
print(A) 

A.remove(A[4])
print(A)

A.append(A[14]**2)
print(A)

lenght= len(A)
print(lenght)

sumA = sum(A)
print(sumA)

A.reverse()
print(A)

