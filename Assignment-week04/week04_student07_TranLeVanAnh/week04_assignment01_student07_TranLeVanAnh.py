#Bài 1
A = [[1,2],[3,0,4],[2],[4,5]]

for i in range(len(A)-1):
    for j in range(i+1,len(A)-1):
        if sum(A[i]) > sum(A[j]):
            c = A[i]
            A[i] = A[j]
            A[j] = c
print(A)