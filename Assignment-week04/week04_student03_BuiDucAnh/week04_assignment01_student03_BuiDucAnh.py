A = [[1,2], [1, 1], [3,0,4], [2], [4,5]]

def sort(A):
    size_list = len(A)
    for i in range(0, size_list - 1):
        for j in range(0, size_list-2):
            if sum(A[j]) > sum(A[j+1]):
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp
    return A

print(sort(A))
