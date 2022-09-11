"""
Solving a System of Linear Equations (AX = B) with Numpy
"""

import numpy as np


def solving_linear_equations(list_A, list_B):
    try:
                
        A = np.array(list_A)
        B = np.array(list_B)

        inverse_A = np.linalg.inv(A)
        X = inverse_A.dot(B)

        print(X)
    except ValueError:
        print("The number of columns of the first matrix must match the number of rows in the second matrix.")

list_A = [[2,-2,1],[1,3,-2],[3,-1,-1]]
list_B = [-3,1,2]

solving_linear_equations(list_A, list_B)