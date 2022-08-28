import random
import numpy as np

def random1(m:int, n:int):
    arr = np.zeros((m, n))
    for i in range(m):
        for j in range(n):
            arr[i][j] = random.randint(0,9)
    return arr

def sumarr(arr:[]):
    m = len(arr)
    n = len(arr[0])
    sum = np.zeros(n)
    for i in range(0, n):
        for j in range(0, m):
            sum[i] += arr[j][i]
    return sum
if __name__ == '__main__':
    arr1 = random1(5, 6)
    print(sumarr(arr1))

    arr2 = np.ndarray((5, 6), dtype=int)
    print(arr2.sum(axis=0))