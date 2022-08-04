import numpy
from sympy import fibonacci

#numpy
def fib_1(n):
    return (numpy.matrix([[2,1],[1,1]])**(n//2))[0,(n+1)%2]
print(fib_1(7)) #13

#recursion
def fib_2(n):
    if n in {0, 1}:
        return n
    return fib_2(n-1) + fib_2(n-2)
print(fib_2(7)) #13

#sympy
def fib_3(n):
    return fibonacci(n)
print(fib_3(7)) #13