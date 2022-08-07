import numpy as np
import sympy as sp

def getFibonacciLoop(n): #Tính dãy Fibonacci sử dụng vòng lặp
    u0, u1 = 0, 1
    un = u0 + u1
    if n<0:
        return -1
    elif n == 0 or n == 1:
        return n
    else:
        for i in range (2, n):
            u0 = u1
            u1 = un
            un = u0 + u1
        return un

def getFibonacciRecursion(n): #Tính dãy Fibonacci sử dụng đệ quy
    if n<0:
        return -1
    elif n == 0 or n == 1:
        return n
    else:
        return getFibonacciRecursion(n-1) + getFibonacciRecursion(n-2)

def getFibonacciNumpy(n): #Tính dãy Fibonacci sử dụng thư viện numpy
    sqrt5 = np.sqrt(5)
    return np.rint((1/sqrt5)*(((1+sqrt5)/2)**n - ((1-sqrt5)/2)**n)) #np.rint dùng để lấy phần nguyên

def getFibonacciSympy(n): #Tính dãy Fibonacci sử dụng thư viện numpy
    return sp.fibonacci(n)

print (getFibonacciLoop(10))
print (getFibonacciRecursion(10))
print (getFibonacciNumpy(10))
print (getFibonacciSympy(10))