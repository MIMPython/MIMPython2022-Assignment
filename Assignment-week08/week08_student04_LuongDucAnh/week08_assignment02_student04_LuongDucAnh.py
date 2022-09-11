import numpy as np
from time import perf_counter

def gaussJordan(A, b):
    matrix = np.concatenate((A, b), axis=1)
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    for i in range(rows): 
        if matrix[i, i] == 0: 
            for j in range(i + 1, rows):
                if matrix[j, i] != 0:
                    matrix[[i, j]] = matrix[[j, i]]
                    break
        if matrix[i, i] != 1:
            matrix[i] = matrix[i]/matrix[i, i]
        for j in range (i+1, rows):
            if matrix[j, i] != 0:
                matrix[j] = matrix[j] - matrix[j, i] * matrix[i]
    

    for i in range(rows):
        for j in range(i + 1, cols - 1):
            if matrix[i, j] != 0:
                matrix[i] = matrix[i] - matrix[j] * matrix[i, j]
                
    return matrix

A = np.random.randint(100, size=(100, 100)).astype(np.float64)
b = np.random.randint(100, size=(100, 1)).astype(np.float64)

# A = np.array([[1,1,0],[1,-1,0], [1, -3, 0]]).astype(np.float64)
# b = np.array([[2],[0],[-2]]).astype(np.float64)

start1 = perf_counter()
method1 = gaussJordan(A, b)
end1 = perf_counter()

start2 = perf_counter()
method2 = np.linalg.solve(A, b)
end2 = perf_counter()

print (f"My method: {end1 - start1}")
print (f"Numpy method: {end2 - start2}")