


A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
#a)
A[2] = A[2]**2
print(A)

#b)
del A[2]

A.remove(A[2])
print(A)

#c)
A.append(A[14]**2)
print(A)

#d)
print(len(A) )

#e)
sum = 0
for i in range(len(A)):
    sum = sum + A[i]

print(sum)

#f)
print(A[1] + A[2] + A[3] + A[5])

#g)
print(list(reversed(A)))
 
for i in range(len(A)):
    A[i] = A[(len(A)-1) - i]

print(A)

#h)

for i in range(len(A)):
    if(A[i] % 2 == 0):
        print( A[i])


for i in range(len(A)):
    if(A[i] % 2 != 0):
        print( A[i])


        





