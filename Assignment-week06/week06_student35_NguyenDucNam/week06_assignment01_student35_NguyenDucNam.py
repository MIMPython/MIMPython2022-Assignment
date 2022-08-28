from time import perf_counter
import random
import numpy as np
import matplotlib.pyplot as plt
def getMatrixByHand(m,n):
    matrix = []
    for i in range(0,m):
        matrix.append([])
        for j in range(0,n):
            x = np.random.randint(1000)
            matrix[i].append(x)
    return matrix

def getSumColByHand(matrix):
    result = []
    for i in range(0,len(matrix[0])):
        sumA = 0
        for j in range(0,len(matrix)):
            sumA += matrix[j][i]
        result.append(sumA)
    return result

def getSumRowByHand(matrix):
    result = []
    for i in range(0,len(matrix)):
        sumA = 0
        for j in range(0,len(matrix[0])):
            sumA += matrix[i][j]
        result.append(sumA)
    return result

def getMatrixByNumpy(m,n):
    result = np.random.randint(1000, size = (m,n))
    return result

def getSumColByNumpy(matrix):
    result = matrix.sum(axis=0)
    return result

def getSumRowByNumpy(matrix):
    result = matrix.sum(axis=1)
    return result

if __name__ == '__main__':
    matrix = getMatrixByNumpy(100,100)

    startTime1 = perf_counter()
    getMatrixByHand(100,100)
    endTime1 = perf_counter()
    time1 = endTime1-startTime1
    print(time1)

    startTime2 = perf_counter()
    getMatrixByNumpy(100,100)
    endTime2 = perf_counter()
    time2 = endTime2-startTime2
    print(time2)

    startTime3 = perf_counter()
    getSumColByHand(matrix)
    endTime3 = perf_counter()
    time3 = endTime3-startTime3
    print(time3)

    startTime4 = perf_counter()
    getSumColByNumpy(matrix)
    endTime4 = perf_counter()
    time4 = endTime4-startTime4
    print(time4)

    startTime5 = perf_counter()
    getSumRowByHand(matrix)
    endTime5 = perf_counter()
    time5 = endTime5-startTime5
    print(time5)

    startTime6 = perf_counter()
    getSumRowByNumpy(matrix)
    endTime6 = perf_counter()
    time6 = endTime6-startTime6
    print(time6)

def draw_bar():
    names = np.array(['byHand','byNumpy'])
    getMatrix = np.array([time1,time2])
    getSumCol = np.array([time3,time4])
    getSumRow = np.array([time5,time6])
    bar_width = 0.4
    plt.bar(names  ,getMatrix,color='red', width = bar_width, label = 'getMatrix')
    plt.bar(names,getSumCol,color='green', width = bar_width,label = 'getSumCol')
    plt.bar(names , getSumRow, width=bar_width,label = 'getSumRow')
    plt.legend(['getMatrix','getSumCol','getSumRow'])
    plt.show()

draw_bar()
