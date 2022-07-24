A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]

print("a)")
A[2] = A[2]**2
print(A)


print("b)")
#Cách 1:
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
A_new_1 = A.pop(2)
print(A)

#Cách 2:
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
del A[2]
print(A)


print("c)")
A.append(A[-1]**2)
print(A)


print("d)")
print(len(A))


print("e)")
print(sum(A))


print("f)")
print(A[1] + A[2] + A[3] + A[5])


print("g)")
#Cách 1
D = A[:]
D.reverse()
print(D)
#Cách 2
L = []
for i in range(0,len(A)):
    L.append(A[len(A) - i -1])
print(L)


print("h)")
A_chan = []
A_le = []

for i in A:
    if i%2 != 0:
        A_le.append(i)
    else:
        A_chan.append(i)

print(A_chan)
print(A_le)


print("i)")
B = sorted(A, reverse = True)
print(B)

#j
print("j)")
print(len(A) == len(B))

#k
print("k)")
C = A[:]
for i in B:
    C.append(i)
print(C)
