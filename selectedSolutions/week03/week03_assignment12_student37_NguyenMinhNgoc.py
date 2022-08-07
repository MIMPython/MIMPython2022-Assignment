import math as m
import numpy as np
n = int(input("Enter an integer: "))
ans = []
if int(m.sqrt(n)) - m.sqrt(n) == 0:
    size = int(m.sqrt(n))
else:
    size = int(m.sqrt(n)) + 1
for i in range(size):
    ans.append([])
    for j in range (size):
        ans[i].append(0)
k = size * size
s = size
pos = 0
while (k > 0):
    for i in range (pos, s):
        ans[pos][i] = k
        k -= 1
    for i in range (pos + 1, s):
        ans[i][s - 1] = k
        k -= 1
    for i in range (pos, s - 1):
        ans[s - 1][pos + s - 2 - i] = k
        k -= 1
    for i in range (pos + 1, s - 1):
        ans[pos + s - 1 - i][pos] = k
        k -= 1
    pos += 1
    s -= 1
A = np.transpose(np.array(ans))
if size % 2 == 0:
    for i in range (size):
        for j in range(size):
            if A[i ,size - 1 - j] <= n:
                print(A[i, size - 1 - j], end = '\t')
            else:
                print('\t', end = ' ')
        print()
else:
    for i in range (size):
        for j in range(size):
            if A[size - 1 - i, j] <= n:
                print(A[size - 1 - i , j], end = '\t')
            else:
                print('\t', end = ' ')
        print()