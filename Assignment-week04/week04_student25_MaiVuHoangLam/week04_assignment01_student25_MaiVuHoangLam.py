A = [[1, 2], [3, 0, 4], [2], [4, 5]]  # input


def sum_of_element(list):
    sum = 0
    for elenemnt in list:
        sum += elenemnt
    return sum


for i in range(0, len(A) - 1):
    for j in range(i + 1, len(A)):
        if sum_of_element(A[i]) > sum_of_element(A[j]):
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
        if sum_of_element(A[i]) == sum_of_element(A[j]):
            if len(A[i]) < len(A[j]):
                temp = A[i]
                A[i] = A[j]
                A[j] = A[i]


print(A)  # output : [[2], [1, 2], [3, 0, 4], [4, 5]]






