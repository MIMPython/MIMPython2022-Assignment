A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]

# 1a)
A[2] = A[2] * A[2]

# 1b) Cách 1 : A.pop(2)

# Cách 2:
A.remove(A[2])

# 1c)
A.append(A[len(A) - 1] * A[len(A) - 1])

# 1d)
print(len(A))

# 1e)
sum = 0
for i in A:
    sum += i

print(sum)

# 1f)
print(A[1] + A[2] + A[3] + A[5])


# 1g) Cách 1: reverse_list = reversed(A)
#     Cách 2:
reverse_list = []
i = len(A) - 1

while i >= 0:
    reverse_list.append(A[i])
    i -= 1

print(reverse_list)


# 1h)
odd_list = []
even_list = []
for i in A:
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)


# 1i)
B = sorted(reverse_list)

# 1j)
print(len(A) == len(B))

# 1k)
C = A
for i in B:
    C.append(i)











