A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]

# a
A[2] = A[2] ** 2
print(A)

# b
A.pop(2)
print(A)
del A[2]
print(A)

# c
A.append(A[-1] ** 2)
print(A)

# d
print(len(A))

# e
sum = 0
for index in range(len(A)):
    sum += A[index]
print(sum)

# f
sumf = 0
indexf = (1, 2, 3, 5)
for i in indexf:
    sumf += A[i]
print(sumf)

# g
A1 = list(reversed(A))
print(A1)
reversed_list = A[::-1]
print(reversed_list)

# h
even_list = []
odd_list = []
for i in range(len(A)):
    if A[i] % 2 == 0:
        even_list.append(A[i])
    else:
        odd_list.append(A[i])
print(even_list)
print(odd_list)

# i
B = sorted(A)[::-1]
print(B)

# j
print(len(B) - len(A) == 0)

# k
C = A[::]
for index in range(len(B)):
    C.append(B[index])
print(C)
