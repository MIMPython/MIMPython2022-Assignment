# normal way to get nth Fibonacci number
fn = [0, 1]


def fibonacci_number(n):
    i = 1
    while i < n:
        fn.append(fn[i] + fn[i - 1])
        i += 1
    return fn[n]


print(fibonacci_number(21))
for j in range(20):
    print(fibonacci_number(j))
    j += 1

# getting nth Fibonacci number using sympy
from sympy import *

n_th_fibonacci_number = fibonacci(21)
print(n_th_fibonacci_number)

# getting nth Fibonacci number using numpy
import numpy


def fibonacci_number_2(n):
    n_th_fibonacci_number = int(
        numpy.rint(
            (((1 + numpy.sqrt(5)) / 2) ** n - ((1 - numpy.sqrt(5)) / 2) ** n)
            / (numpy.sqrt(5))
        )
    )
    # using Binet Formula
    return n_th_fibonacci_number


print(fibonacci_number_2(21))
