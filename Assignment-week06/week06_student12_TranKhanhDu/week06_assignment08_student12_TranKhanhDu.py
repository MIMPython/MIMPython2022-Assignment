import numpy as np 
import random
a = int(input("Enter row's number: "))
b = int(input("Enter column's number: "))

def inputArray(a, b):
    array = np.zeros((a + 2, b + 2), dtype = int)
    for i in range(1, array.shape[0] - 1):
        for j in range(1, array.shape[1] - 1):
            array[i, j] = random.randint(0, 1)
    return array
unchangedArray = inputArray(a, b)

print("original array: ")
def showArray(array):
    arrayToShow = np.zeros((array.shape[0] - 2, array.shape[1] - 2), dtype = int)
    for row in range(1, array.shape[0] - 1) :
        for column in range(1, array.shape[1] - 1):
            arrayToShow[row - 1, column - 1] = array[row, column]
    return arrayToShow

print(showArray(unchangedArray))
print("array after change: ")
 
def conwayGameOfLife(array):
    arrayAfterConverted = np.zeros((array.shape[0] - 2, array.shape[1] - 2), dtype = int)    
    for row in range(1, array.shape[0] - 1) :
        for column in range(1, array.shape[1] - 1):
            sum = array[row - 1, column - 1] + array[row - 1, column] + array[row - 1, column + 1] + array[row, column + 1] + array[row + 1, column + 1] + array[row + 1, column] + array[row +1, column - 1] + array[row, column - 1]
            if sum == 3 and array[row, column] == 0:
                arrayAfterConverted[row - 1, column - 1] = 1
            elif sum < 2 and array[row, column] == 1:
                arrayAfterConverted[row - 1, column - 1] = 0
            elif sum > 3 and array[row, column] == 1:
                arrayAfterConverted[row - 1, column - 1] = 0
            else:
                arrayAfterConverted[row - 1, column - 1] = array[row, column]
    return arrayAfterConverted
print(conwayGameOfLife(unchangedArray))

