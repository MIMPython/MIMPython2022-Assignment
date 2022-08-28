import numpy as np
from time import perf_counter

"""
    numpy.mean: Trả về giá trị trung bình của mảng

    Examples of numpy.mean
    a = np.array([[1, 2, 3], [4, 5, 6]])
    print(np.mean(a)) 
    # 3.5
    print(np.mean(a, axis=0)) 
    # [2.5 3.5 4.5]
    print(np.mean(a, axis=1)) 
    # [2. 5.]
"""
# Function to calculate the average of the array elements
def getMean(array, axis = None):
    if axis == None:
        sumOfArray = 0
        for i in range (array.shape[0]):
            for j in range (array.shape[1]):
                sumOfArray += array[i, j]
        return sumOfArray/(array.shape[0]*array.shape[1])
    elif axis == 0:
        result = []
        for i in range (array.shape[1]):
            sumCol = 0
            for j in range (array.shape[0]):
                sumCol += array[j, i]
            result.append(sumCol/array.shape[0])
        return np.array(result)
    elif axis == 1:
        result = []
        for i in range (array.shape[0]):
            sumRow = 0
            for j in range (array.shape[1]):
                sumRow += array[i, j]
            result.append(sumRow/array.shape[1])
        return np.array(result)
    else:
        raise Exception("Out of bounds")

"""   
    a = np.array([[1, 2, 3], [4, 5, 6]])
    print (getMean(a)) 
    # 3.5
    print (getMean(a, axis=0)) 
    # [2.5 3.5 4.5]
    print (getMean(a, axis=1)) 
    # [2. 5.]
"""
a = np.random.rand(1000, 1000)
start = perf_counter()
npResult = np.mean(a, axis=0)
end = perf_counter()
# print(npResult)
print(f"Execution time of numpy.mean: {end - start}")

start = perf_counter()
myResult = getMean(a, axis=0)
end = perf_counter()
# print(myResult)
print(f"Execution time of my Function: {end - start}")
