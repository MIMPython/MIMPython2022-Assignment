A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]

# a.
A[3] = A[3] * A[3]  # [70, 43, 7, 2116, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]

# b.
del A[3]
print(A)            # [70, 43, 7, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]

tmp = A[0]
A[0] = A[3]
A[3] = tmp
A.remove(A[0])
print(A)            # [43, 7, 70, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]

# c.
n = len(A)
A.insert(n, A[n-1] * A[n-1])
print(A)            # [43, 7, 70, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53, 2809]

# d.
print(len(A))       # 14

# e.
print(sum(A))       # 3288

# f.
sum = 0
for i in (1,2,3,5) :
    sum = sum + A[i]
print(sum)          # 189

# g.
A.reverse()
B = A
print(B)            # [2809, 53, 3, 53, 5, 1, 3, 49, 35, 80, 77, 70, 7, 43]
A.reverse()

C = []
n = len(A)
for i in range(0, n):
    C.insert(0, A[i])
print(C)            # [2809, 53, 3, 53, 5, 1, 3, 49, 35, 80, 77, 70, 7, 43]

# h.
odds = []
evens = []
for i in range(0, n) :
    if A[i] % 2 == 0 :
        evens.append(A[i])
    else : odds.append(A[i])

print(odds)         # [43, 7, 77, 35, 49, 3, 1, 5, 53, 3, 53, 2809]
print(evens)        # [70, 80]

# i. 
B = sorted(A, reverse=True) 
print(B)            # [2809, 80, 77, 70, 53, 53, 49, 43, 35, 7, 5, 3, 3, 1]

# j. 
print(len(B) == len(A)) # True 

# k.
C = []
for i in range(0, len(A) + len(B)):
    if i < len(A) :
        C.append(A[i])
    else : C.append(B[i-len(A)])

print(C)    


    