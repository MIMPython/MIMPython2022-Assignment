from xmlrpc.client import boolean


A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]

#a
print("a)")
A[2] *= A[2]
print (A)

#b
print("b)")
A.pop(2)
print(A)
del A[2]
print(A)

#c
print("c)")
A.append(A[ len(A) -1 ]**2)
print(A)

#d
print("d)")
print("Tổng số phần tử của A là:",len(A))

#e
print("e)")
sumA = sum(A)
print("Tổng các phần tử của A là:", sumA)

#f
print("f)")
sum = A[1] + A[2] + A[3] +A[5]
print("tổng của các phần tử có chỉ số (index) 1, 2, 3, 5 trong list:", sum)

#g
print("g)")
print(list(reversed(A)))

newA = A[:: -1]
print(newA)

#h
print("h)")
even = list()
odd = list()
for i in A:
    if (i % 2 == 0):
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)

#i
print("i)")
B = list()
for i in A:
    B.append(i)
B.sort()
B.reverse()
print(B)

#j
print("j)")
print(boolean( len(B) == len(A)))

#k
print("K)")
C = A + B
print(C)