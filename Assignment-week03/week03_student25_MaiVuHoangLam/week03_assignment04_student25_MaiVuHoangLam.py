import numpy as np
import sympy as sp


def fibonacci_using_numpy(x):
    if x == 1 or x == 2:
        return 1
    else:
        return np.add(fibonacci_using_numpy(x - 1), fibonacci_using_numpy(x - 2))


print(fibonacci_using_numpy(10))

# using sympy
print(sp.fibonacci(10))





