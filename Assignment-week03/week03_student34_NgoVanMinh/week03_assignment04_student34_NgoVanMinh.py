import numpy as np
import sympy as sp
#De quy
def Fibonacci(n: int):
    if n ==0:
        return 0
    elif n==1:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

#Khai trien binet
def fibonaci(nr):
    ratio = (1 + np.sqrt(5)) / 2
    return int(ratio ** nr / np.sqrt(5) + 0.5)


if __name__ == '__main__':
    print(Fibonacci(10))
    print(fibonaci(10))
    print(sp.fibonacci(10))     #Su dung sympy
