import numpy as np
from sympy import fibonacci

# Cách 1


def fibonacci1(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci1(n-1) + fibonacci1(n-2)


print("F8 =", fibonacci1(8))  # F8 = 21

# Cách 2


def fibonacci2(n):
    alpha = (1 + np.sqrt(5)) / 2
    beta = (1 - np.sqrt(5)) / 2
    return np.rint((alpha**n - beta**n)*(1/np.sqrt(5)))


print("F10 =", fibonacci2(10))  # F10 = 55.0


def fibonacci3(n):
    return fibonacci(n)


print("F11 =", fibonacci3(11))  # F11 = 89
