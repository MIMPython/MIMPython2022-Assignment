#a
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
A[2] = A[2]*A[2]                    
print("List after changes", A) 

#b
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
del A[2]
print("List after changes", A)

A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
lov = A.pop(2)
print("List after changes", A)

#c
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
A.append(A[len(A)-1]*A[len(A)-1])
print("List after changes", A)

#d 
print("Number of elements",len(A))

#e
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
sum=0
for i in range(len(A)): 
    sum = sum + A[i]
print("Sum of elements in A = ", sum)

#f
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
print("Sum of elements 1st, 2nd, 3rd, 5th is ", A[0] + A[1] + A[2] + A[4])

#g
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
A.reverse()
print("List after changes", A)

A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
midd = 0
for i in range(len(A)//2):
    midd = A[i]
    A[i] = A[-i-1]
    A[-i-1] = midd
print("List after changes", A)

#h
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
A1 = [] 
j=0
A2 = [] 
k=0
for i in range(len(A)):
    if A[i] % 2 == 0:
        A1[j] = A[i]
        j = j+1
    else:
        A2[k] = A[i]
        k = k+1
