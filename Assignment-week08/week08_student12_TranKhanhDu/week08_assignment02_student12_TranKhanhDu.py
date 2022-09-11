import numpy as np
import random
def inputArray(size, lowerbound, upperbound):
    list = []
    for a in range(0,size):
        list2 = []
        for b in range(0, size):
            randomNumber = random.randint(lowerbound, upperbound)
            list2.append(randomNumber)
        list.append(list2)
    
    #create array
    array = np.array(list, dtype = float)
    return array

def subtractingBetweenTwoRow(array, row1, row2, column):
    newRow =[]
    for index in range(0, array.shape[1]):
        if array[row2, column] == 0:
            quotient = 0
        else:
            quotient = float(array[row1, column]/array[row2, column])
        result = (float(array[row1][index]) - float(quotient)*float(array[row2][index])) 
        newRow.append(result)
    return newRow

def changePositionBetweenTwoRow(array, row1, row2):
    temp = []
    for index in array[row1]:
        temp.append(index)
    array[row1] = array[row2]
    array[row2] = temp

def gaussElimination(array):

    for row in range(0, array.shape[1] - 1):
        if array[row, row] == 0:
            #find another row if its number differnt from 0
            for index in range(row + 1, array.shape[0]):
                if array[index, row] != 0:
                    changePositionBetweenTwoRow(array, row, index)
                    break

        #subtracting
        for index in range(row + 1, array.shape[0]):    
            array[index] = subtractingBetweenTwoRow(array, index, row, row)
        for index in range(0, row):
            array[index] = subtractingBetweenTwoRow(array, index, row, row)
    return array

def roundingElementsInVectors(vector):
    for index in range(0, len(vector)):
        vector[index] = round(vector[index], 2)
    return vector

def findVectorX(array, vector):
    if array.shape[1] != len(vector):
        return "invalid variables"
    else:
        if array.shape[0] < len(vector):
            return "equals has innumberable solutuion"
        else:    
            list1 = []
            for row in range(0, array.shape[0]):
                list2 = []
                for column in range(0, array.shape[1]):
                    list2.append(array[row, column])
                list2.append(vector[row])
                list1.append(list2)
            newArray = np.array(list1)
            gaussElimination(newArray)
            vectorX = []
            for number in range(0, newArray.shape[0]):
                quotient = round((newArray[number, newArray.shape[1] - 1]/newArray[number, number]), 3)
                vectorX.append(quotient)
            return vectorX

array = inputArray(4, 0, 100)
vector = [random.randint(0, 100) for i in range(4)]
print('array: ')
print(array)
print('vector: ')
print(vector)

print("vector x: ")
print(findVectorX(array, vector))

            





