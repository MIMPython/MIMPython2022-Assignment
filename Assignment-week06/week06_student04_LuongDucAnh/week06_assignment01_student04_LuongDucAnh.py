import numpy as np
from time import perf_counter
import pandas as pd

#Function to create m x n matrix of random integers
def randomMatrix(m, n):
    matrix = []
    for _ in range (m):
        row = []
        for _ in range (n):
            row.append(np.random.randint(100))
        matrix.append(row)
    return matrix
    
#Function to calculate sum of each column
def sumCol(matrix):
    result = []
    for i in range (len(matrix[0])):
        sumOfCol = 0
        for j in range (len(matrix)):
            sumOfCol += matrix[j][i]
        result.append(sumOfCol)
    return result

#Function to calculate sum of each row
def sumRow(matrix):
    result = []
    for i in range (len(matrix)):
        sumOfRow = 0
        for j in range (len(matrix[0])):
            sumOfRow += matrix[i][j]
        result.append(sumOfRow)
    return result
        
#Function to create m x n matrix of random integers using Numpy
def randomMatrixNumpy(m, n):
    return np.random.randint(100, size=(m, n))

#Function to calculate sum of each column using Numpy
def sumColNumpy(matrix):
    return matrix.sum(axis=0)

#Function to calculate sum of each row using Numpy
def sumRowNumpy(matrix):
    return matrix.sum(axis=1)
        
if __name__ == "__main__":
    data = {"sumCol" : [], "sumRow" : [], "sumColNumpy" : [], "sumRowNumpy" : []}
    for i in range (10):
        matrix = randomMatrixNumpy(1000, 1000)
        matrixL = matrix.tolist()
        
        start = perf_counter()
        sumCol(matrixL)
        end = perf_counter()
        data["sumCol"].append(end - start)
        
        start = perf_counter()
        sumRow(matrixL)
        end = perf_counter()
        data["sumRow"].append(end - start)
        
        start = perf_counter()
        sumColNumpy(matrix)
        end = perf_counter()
        data["sumColNumpy"].append(end - start)
        
        start = perf_counter()
        sumRowNumpy(matrix)
        end = perf_counter()
        data["sumRowNumpy"].append(end - start)
        
    table = pd.DataFrame(data)
    print(table)