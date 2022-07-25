def foo(x):
    return x**2

A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]

#a
A[2] = foo(A[2])

#b
A.pop(2)
del A[2]

#c
A.append(foo(A[12]))

#d
a1 = len(A)
print(a1)

#e
a2 = sum(A)
print(a2)

#f
if i>0 and i<4 or i=5
    sum1 += A[i]

print(sum1)

#g
A.reverse()
print(A)



