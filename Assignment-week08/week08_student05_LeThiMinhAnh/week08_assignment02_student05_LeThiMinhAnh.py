from random import randint
from time import perf_counter_ns
import numpy as np


def create_matrix(m, n):
    mat = [[randint(1, 20) for i in range(n)] for j in range(m)]
    return mat


def print_matrix(M):
    for row in M:
        print([round(x, 2)+0 for x in row])


def determinant(A, total=0):
    indices = list(range(len(A)))

    if len(A) == 2 and len(A[0]) == 2:
        return A[0][0] * A[1][1] - A[1][0] * A[0][1]

    for fc in indices:
        As = A[1:]
        height = len(As)

        for i in range(height):
            As[i] = As[i][0:fc] + As[i][fc+1:]

        sign = (-1) ** (fc % 2)
        sub_det = determinant(As)
        total += A[0][fc] * sign * sub_det

    return total


def check_squareness(A):
    if len(A) != len(A[0]):
        raise ArithmeticError("Matrix must be square.")


def check_non_singular(A):
    det = determinant(A)
    if det != 0:
        return det
    else:
        raise ArithmeticError("Matrix is singular!")


def solve_equations(A, B):

    check_squareness(A)
    check_non_singular(A)

    n = len(A)
    AM, BM = A, B

    indices = list(range(n))
    for fd in range(n):
        fdScaler = 1 / AM[fd][fd]
        for j in range(n):
            AM[fd][j] *= fdScaler
        BM[fd][0] *= fdScaler

        for i in indices[0:fd] + indices[fd+1:]:
            crScaler = AM[i][fd]
            for j in range(n):
                AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
            BM[i][0] = BM[i][0] - crScaler * BM[fd][0]
    return BM


def solving_equations_with_numpy(A, B):
    a = np.array(A)
    b = np.array(B)
    x = np.linalg.solve(a, b)
    return x


def main():
    print("A matrix")
    A = create_matrix(10, 10)
    print_matrix(A)
    print()

    print("B matrix")
    B = create_matrix(10, 1)
    print_matrix(B)
    print()

    print("Solve for X without Numpy")
    start = perf_counter_ns()
    X = solve_equations(A, B)
    end = perf_counter_ns()
    time1 = end - start
    print_matrix(X)
    print()

    print("Solve for X with Numpy")
    start = perf_counter_ns()
    x = solving_equations_with_numpy(A, B)
    end = perf_counter_ns()
    time2 = end - start
    print_matrix(x)
    print()

    print(f"Time of solving for X without Numpy: {time1} ns")
    print(f"Time of solving for X with Numpy: {time2} ns")
    print()


if __name__ == "__main__":
    main()
"""
A matrix
[15, 1, 20, 15, 15, 11, 7, 19, 3, 17]
[2, 18, 18, 4, 2, 13, 3, 1, 16, 13]
[4, 20, 15, 15, 11, 7, 11, 20, 15, 3]
[19, 16, 9, 10, 20, 16, 16, 13, 12, 17]
[3, 6, 20, 5, 2, 14, 11, 12, 12, 19]
[12, 8, 18, 6, 2, 8, 17, 15, 1, 18]
[2, 9, 10, 11, 16, 19, 8, 3, 15, 14]
[8, 9, 15, 7, 1, 11, 3, 16, 15, 11]
[18, 7, 5, 16, 1, 13, 11, 5, 7, 15]
[6, 18, 9, 14, 10, 19, 5, 11, 3, 4]

B matrix
[6]
[20]
[16]
[20]
[12]
[8]
[10]
[16]
[6]
[1]

Solve for X without Numpy
[2.84]
[-1.75]
[3.26]
[-1.67]
[0.11]
[1.59]
[2.22]
[-1.77]
[1.93]
[-4.82]

Solve for X with Numpy
[2.84]
[-1.75]
[3.26]
[-1.67]
[0.11]
[1.59]
[2.22]
[-1.77]
[1.93]
[-4.82]

Time of solving for X without Numpy: 3035571800 ns
Time of solving for X with Numpy: 239100 ns

"""
# Ham giai phuong trinh tuyen tinh duoc dung san trong numpy co do chinh xac tuong duong va thoi gian thuc thi ngan hon nhieu so voi ham da viet
