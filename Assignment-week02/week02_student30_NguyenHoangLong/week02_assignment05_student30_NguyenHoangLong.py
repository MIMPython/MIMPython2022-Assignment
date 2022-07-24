A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
#a)
print("a)")
A[2] = A[2]**2
print(A)

#b)
print("b)")
#Cách 1:
A_new_1 = A.pop(2)
print(A)

#Cách 2:
del A[2]
print(A)

#c)
print("c)")
A.append(A[-1]**2)
print(A)

#d)
print("d)")
print(len(A))

#e)
print("e)")
print(sum(A))

#f)
print("f)")
print(A[1] + A[2] + A[3] + A[5])

#g)
print("g)")
#Cách 1
X = A[:]
X.reverse()
print(X)
#Cách 2
Y = []
for i in range(0,len(A)):
    Y.insert(0, A[i])
print(Y)

#h)
print("h)")
A_even = []
A_odd = []

for i in A:
    if i%2 == 0:
        A_even.append(i)
    else:
        A_odd.append(i)

print(A_odd)
print(A_even)

#i)
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

