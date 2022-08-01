# Bài tập 4. (Fibonacci numbers)
import numpy as np
import sympy as sp


def Fibonacci(n):
    fibo_nums = np.array([0] * (n + 1))
    fibo_nums[1] = 1
    for i in range(2, n + 1):
        fibo_nums[i] = fibo_nums[i-1] + fibo_nums[i-2]

    return fibo_nums

if __name__ =="__main__":
    n = 100
    fibo_nums = Fibonacci(n)
    print(fibo_nums[26]) # 121393
    print(fibo_nums[10]) # 55