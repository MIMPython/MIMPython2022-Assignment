import numpy as np
import time 

# not using numpy
import random
def randomArray(a,b):
    if a <= 0 or b <= 0:
        return "invalid number!"
    arr = []
    for i in range(0, a):
        list = []
        for i in range(0, b):
            i = random.randint(1000000,9999999)
            list.append(i)
        arr.append(list)
    return arr

# solution1: calculate sum not using library
def calculateSumOfAllColumns(array):
    sumOfAllColumns = []
    for j in range(0, len(array[0])):
        sumOfEachColumn = 0
        for i in range(0, len(array)):
            sumOfEachColumn += (array[i])[j]
        sumOfAllColumns.append(sumOfEachColumn)
    return sumOfAllColumns

# using library numpy
def createRandomarrayUsingNumpy(c,d):
    array = np.random.randint(1000000, 9999999, (c, d))
    return array

def calculateSumOfAllColumnsUsingNumpy(array):
    SumOfAllColumns = np.sum(array, axis = 0)
    return SumOfAllColumns

#CALCULATING TIME:
a = int(input("Enter row's number: "))
b = int(input("enter column's number: "))

#not using numpy:
startTime = time.time()
calculateSumOfAllColumns(randomArray(a, b))
endTime = time.time()
elapsedTime = endTime - startTime

# using numpy
startTimeUsingNumpy = time.time()
calculateSumOfAllColumnsUsingNumpy(createRandomarrayUsingNumpy(a,b))
endTimeUsingNumpy = time.time()
elapsedTimeUsingNumpy = endTimeUsingNumpy - startTimeUsingNumpy

#comparation
if elapsedTime < elapsedTimeUsingNumpy:
    print("not using numpy is faster than using numpy")
else:
    print("using numpy is faster than not using numpy")
    
#CÂU e tương tự, using numpy sẽ nhanh hơn