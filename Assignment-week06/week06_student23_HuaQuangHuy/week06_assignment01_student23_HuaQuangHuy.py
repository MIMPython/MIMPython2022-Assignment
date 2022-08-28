#  bai tap 1
from cProfile import label
from random import randint
import time
from turtle import color
import numpy as np
from matplotlib import pyplot as plt

#  ham tao mang 2 chieu


def generateArray(m, n):
    bigList = []
    for i in range(0, m):
        smallList = []
        for j in range(0, n):
            smallList.append(randint(0, 100))
        bigList.append(smallList)
    return bigList

# ham tinh list theo cot


def getSumByColumn(list):
    sumByColumnList = []
    for i in range(0, len(list[0])):
        sumColumn = 0
        for j in range(0, len(list)):
            sumColumn = sumColumn + list[j][i]
        sumByColumnList.append(sumColumn)

    return sumByColumnList

# ham tinh list theo hang


def getSumByRow(list):
    sumByRowList = []
    for i in range(0, len(list)):
        sumRow = 0
        for j in range(0, len(list[0])):
            sumRow = sumRow + list[i][j]
        sumByRowList.append(sumRow)

    return sumByRowList
# time execute sum list column manual


def getTimeColumnManual(list):
    startTime = time.time()
    getSumByColumn(list)
    endTime = time.time()

    return (endTime - startTime) * 1000  # miliseconds


def getTimeRowManual(list):
    startTime = time.time()
    getSumByRow(list)
    endTime = time.time()

    return (endTime - startTime) * 1000  # miliseconds


def getTimeColumnNumpy(list):
    startTime = time.time()
    array = np.array(list)
    array.sum(axis=1)
    endTime = time.time()

    return (endTime - startTime) * 1000  # miliseconds


def getTimeRowNumpy(list):
    startTime = time.time()
    array = np.array(list)
    array.sum(axis=0)
    endTime = time.time()

    return (endTime - startTime) * 1000  # miliseconds


if __name__ == '__main__':
    timeColumnManualWay = []
    timeRowManualWay = []

    timeColumnNumpyWay = []
    timeRowNumpyWay = []

    listSize = [*range(500, 1000, 20)]
    for k in range(500, 1000, 20):
        sumTimeColumnManual = 0
        sumTimeColumnNumpy = 0
        sumTimeRowManual = 0
        sumTimeRowNumpy = 0

        for u in range(0, 11):
            newList = generateArray(k, k)
            sumTimeColumnManual += getTimeColumnManual(newList)
            sumTimeColumnNumpy += getTimeColumnNumpy(newList)
            sumTimeRowManual += getTimeRowManual(newList)
            sumTimeRowNumpy += getTimeRowNumpy(newList)

        timeColumnManualWay.append(sumTimeColumnManual / 10)
        timeRowManualWay.append(sumTimeColumnNumpy / 10)

        timeColumnNumpyWay.append(sumTimeRowManual / 10)
        timeRowNumpyWay.append(sumTimeRowNumpy / 10)

    # plot 1
    plt.figure(figsize=(10, 15))  # size figure
    plt.plot(listSize, timeColumnManualWay, '-', color='red', label='manual')
    plt.plot(listSize, timeColumnNumpyWay, '-', color='blue', label='numpy')
    plt.xlabel('size of array', fontsize=16)
    plt.ylabel('Time execute', fontsize=16)
    plt.title('Compare time sum by column between manual vs numpy')
    plt.legend(fontsize=14)
    plt.grid()

    # plot 2
    plt.figure(figsize=(10, 15))  # size figure
    plt.plot(listSize, timeRowManualWay, '-', color='red', label='manual')
    plt.plot(listSize, timeRowNumpyWay, '-', color='blue', label='numpy')
    plt.xlabel('size of array', fontsize=16)
    plt.ylabel('Time execute', fontsize=16)
    plt.title('Compare time sum by Row between manual vs numpy')
    plt.legend(fontsize=14)
    plt.grid()
    plt.show()

    # khi ở muc du lieu nhỏ, numpy và cách xử lý thủ công có tốc độ ngang bằng nhau, nhưng với dữ liệu lớn hơn thì numpy nhanh hơn
