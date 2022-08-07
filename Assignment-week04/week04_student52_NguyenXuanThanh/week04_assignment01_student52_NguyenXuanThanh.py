A = [[1,2],[3,4,6,10], [3,0,4,0,0], [2], [4,5]]

def check_prime_number(A,B):
    #flag = 1 => A > B
    #flag = 0 => A & B không là 2 list ổn định, A < B
    if(len(B) == 0 and len(A) == 0):
        flag = 0
        return flag
    sum_1 = 0
    sum_2 = 0
    for i in B:
        sum_2 += i
    for i in A:
        sum_1 += i
    print(sum_1)
    print(sum_2)
    if(sum_1 > sum_2 ):
        flag = 1
        return flag
    else: return 0

def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if (check_prime_number(A[j],A[j+1]) == 1):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
bubbleSort(A)

# input : A = [[1,2],[3,4,6,10], [3,0,4,0,0], [2], [4,5]]
print(A) # [[2], [1, 2], [3, 0, 4, 0, 0], [4, 5], [3, 4, 6, 10]]