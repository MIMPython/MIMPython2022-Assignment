import numpy as np
from time import perf_counter
inputArray = np.array([1,3,4,5,7,6,10,11,1,2,3,4,5,6,7,8,9,10])
#Function mean
""" The mean function is used to calculate the average of the elements in the array. For example, array A = [1,2,3], the mean function returns the average value of 2"""
def meanByHand(a):
    sumA = 0
    for i in range(0,len(a)):
        sumA += a[i]
    result = sumA / len(a)
    return result
    
sTime1 = perf_counter()
print(meanByHand(inputArray))
eTime1 = perf_counter()
print (eTime1 - sTime1, "[sec]")

def meanByNumpy(a):
    result = np.mean(a)
    return result

sTime2 = perf_counter()
print(meanByNumpy(inputArray))
eTime2 = perf_counter()
print (eTime2 - sTime2,"[sec]")

"""Numpy's average execution speed is slower than manual method"""

#Function median
"""The median function is used to calculate the median of the array. For example, array A = [1,2,3], the median function returns the median value of 2"""
def medianByHand(a):
    sortedArray = sorted(a)
    if len(sortedArray)%2 == 0:
        idx = int(len(sortedArray)/2)
        result = (sortedArray[idx]+sortedArray[idx-1])/2
        return result
    else:
        idx = len(sortedArray)//2
        result = sortedArray[idx]
        return result

sTime3 = perf_counter()
print(medianByHand(inputArray))
eTime3 = perf_counter()
print (eTime3 - sTime3, "[sec]")

def medianByNumpy(a):
    result = np.median(a)
    return result

sTime4 = perf_counter()
print(medianByNumpy(inputArray))
eTime4 = perf_counter()
print (eTime4 - sTime4, "[sec]")   

"""Numpy's medium execution speed is slower than manual method"""






