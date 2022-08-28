import numpy as np
import time


def determinant(A):
    n = len(A)
    for i in range(n):
        for j in range(i + 1, n):
            if A[i][i] == 0:
                A[i][i] == 1.0e-18
            temp = A[j][i] / A[i][i]
            for k in range(n):
                A[j][k] = A[j][k] - temp * A[i][k]

    res = 1.0
    for i in range(n):
        res *= A[i][i]

    return res


if __name__ == "__main__":
    A = np.array([[12.0, 13.0, 3.0],
                  [4.0, 4.0, 2.0],
                  [5.0, 6.0, 7.0]])
    t1 = time.time()
    print(determinant(A))  # -29.999999999999975
    t2 = time.time()
    print(np.linalg.det(A))  # -29.99999999999996
    print(t2 - t1)  # 0.00035071372985839844
