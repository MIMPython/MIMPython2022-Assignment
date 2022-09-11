import numpy as np
def Gauss_elimination(A, b):
    n = len(A)
    x = [0] * n
    for i in range(n):
        if A[i][i] == 0:
            for j in range(n):
                if A[j][i] != 0:
                    for k in range (n):
                        A[i][k] += A[j][k]
                    b[i] += b[j]
                    break
    for i in range(n - 1):
        for j in range(i + 1, n):
            ratio = A[j][i] / A[i][i]
            for k in range(n):
                A[j][k] = A[j][k] - ratio * A[i][k]
            b[j] = b[j] - ratio * b[i]
    x[n - 1] = b[n - 1] / A[n - 1][n - 1]
    for i in range(n - 2, -1, -1):
        x[i] = b[i]
        for j in range(i + 1, n):
            x[i] = x[i] - A[i][j] * x[j]
        x[i] = x[i] / A[i][i]
    return x
if __name__ == '__main__':
    A = [[0, 2, 5], [4, 5, 2], [1, 6, 7]]
    b = [19, 20, 34]
    print('Gauss elimination\'s solution:')
    print('x = ' + str(Gauss_elimination(A, b)))
    A = [[0, 2, 5], [4, 5, 2], [1, 6, 7]]
    b = [19, 20, 34]
    print('numpy\'s solution:')
    print('x = ' + str(np.linalg.solve(A, b)))
    A = [[1, 2], [4, 5]]
    b = [3, 9]
    print('Gauss elimination\'s solution:')
    print('x = ' + str(Gauss_elimination(A, b)))
    A = [[1, 2], [4, 5]]
    b = [3, 9]
    print('numpy\'s solution:')
    print('x = ' + str(np.linalg.solve(A, b)))