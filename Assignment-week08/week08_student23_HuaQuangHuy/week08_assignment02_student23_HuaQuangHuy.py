#  bai tap 2
#  giai he phuong trinh tuyen tinh Ax = b, A la ma tran
from random import randint
import time
import numpy as np
from matplotlib import pyplot as plt


def solveEqualtion(matrix, b):
    iteratorStep = 10
    k = 1
    rows = len(matrix)
    cols = len(matrix[0])

    # x is list of No, init x = []
    x = []
    for i in range(0, cols):
        x.append(0)
    while k < iteratorStep:
        for i in range(0, rows):
            sum = 0
            for j in range(0, cols):
                if j != i:
                    sum += matrix[i][j] * x[j]

            x[i] = (1 / matrix[i][i]) * (b[i] - sum)

        k = k + 1

    return x


def getTimeManualSolve(matrix, b):
    startTime = time.time()
    solveEqualtion(matrix, b)
    endTime = time.time()
    return (endTime - startTime) * 1000


def getTimeNumpySolve(matrix, b):
    startTime = time.time()
    x = np.linalg.solve(matrix, b)
    # print(x)
    endTime = time.time()
    return (endTime - startTime) * 1000


if __name__ == "__main__":

    # A = [[2, 1], [5, 7]]
    # b = [11, 13]
    # matrix = np.array(A, dtype=float)
    # bN = np.array(b, dtype=float)
    # print(solveEqualtion(A, b))
    # getTimeNumpySolve(matrix, bN)
    timeOfManual = []
    timeOfNumpy = []

    for size in range(3, 300, 5):
        sumTimeManual = 0
        sumTimeNumpy = 0
        for i in range(0, 10):
            matrix = np.random.rand(size, size)
            b = np.random.rand(size)
            sumTimeManual += getTimeManualSolve(matrix, b)
            sumTimeNumpy += getTimeNumpySolve(matrix, b)

        timeOfManual.append(sumTimeManual / 10)
        timeOfNumpy.append(sumTimeNumpy / 10)

    # plot
    listSize = range(3, 300, 5)
    plt.figure(figsize=(10, 15))  # size figure
    plt.plot(listSize, timeOfManual, '-', color='red', label='manual')
    plt.plot(listSize, timeOfNumpy, '-', color='blue', label='numpy')
    plt.xlabel('size of matrix', fontsize=16)
    plt.ylabel('Time execute', fontsize=16)
    plt.title('Compare time sum by column between manual vs numpy')
    plt.legend(fontsize=14)
    plt.grid()
    plt.show()
