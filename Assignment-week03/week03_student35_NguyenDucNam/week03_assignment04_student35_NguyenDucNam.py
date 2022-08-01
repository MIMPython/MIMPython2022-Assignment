import numpy as np
import sympy

N = int(input())
mat_1 = np.array([[0,1],[1,1]])
mat_2 = np.array([[1],[1]])
def numpy_fibonacci():
    result = mat_1.dot(mat_2)
    if N == 0:
        return 0
    if N == 1:
        return 1
    if N == 2:
        return result[0,0]
    i = 3
    while i <= N:
        result = mat_1.dot(result)
        i += 1
    return result[0,0]

def sympy_fibonacci():
    result = sympy.fibonacci(N)
    return result

if __name__ == '__main__':
    print(numpy_fibonacci())    
    print(sympy_fibonacci())