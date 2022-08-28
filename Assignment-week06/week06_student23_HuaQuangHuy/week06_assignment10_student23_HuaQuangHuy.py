# bai 10: so sanh toc do thuc hien phep tinh dinh thuc cua ma tran bang phuong phap khu Gauss va thu vien numpy
import numpy as np

# create simple matrix random 3x3
size = 3
# matrix = np.random.randint(10, size=(size, size))
matrix = np.array([
    [0, 1, 2],
    [0, 2, 3],
    [2, 3, 3]
])
print(matrix)
# Determinant of matrix with numpy
detNumpy = np.linalg.det(matrix)
print(detNumpy)
