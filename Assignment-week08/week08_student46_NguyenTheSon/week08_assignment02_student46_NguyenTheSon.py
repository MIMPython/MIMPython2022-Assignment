# Bài 2:
from unittest import result
import numpy as np
def det_matrix(array):
    if np.shape(array) == (1, 1):
        return array[0][0]
    else:    
        det = 0
        for row in range(len(array)):
            for column in range(len(array[0])):
                if row == 0:
                    array_del = np.delete(np.delete(array, 0, axis = 0), column, axis = 1)
                    det += (- 1) ** (row + column) * array[0][column] * det_matrix(array_del)
        return det 

def solving_linear_equations(A, b):
    A = np.array(A)
    b = np.array(b)
    """
    Hàm này giải nhiểm của phương trình tuyến tính Ax = b.
    Với A là ma trận và b la vecto với kích thước phù hợp cho trước.
    Th1: A không khả nghịch --> phương trình Ax = b vô nghiệm 
    Th2: A khả nghịch --> phương trình Ax = b có 1 nghiệm duy nhất là 
    x = (A ** (-1)) * b
    """
    if det_matrix(A) == 0:
        return f'Phương trình {A}x = {b} vô nghiệm.'
    else:
        A_1 = np.zeros((len(A), len(A[0])))
        for row in range(len(A)):
            for column in range(len(A[0])):
                matrix_after_del = np.delete(np.delete(A, row, axis = 0), column, axis = 1)
                A_1[row][column] += (- 1) ** (row + column) * det_matrix(matrix_after_del)
        A_1_T = A_1.T
        inverse_A = (1 / det_matrix(A)) * A_1_T
        result = inverse_A.dot(b)
        return result

print(solving_linear_equations([[1, 2, 2], [3, 3, 1], [2, 4, 1]], [[2],[3],[2]]))
print(solving_linear_equations([[1, 2], [3, 1]], [[2],[3]]))
