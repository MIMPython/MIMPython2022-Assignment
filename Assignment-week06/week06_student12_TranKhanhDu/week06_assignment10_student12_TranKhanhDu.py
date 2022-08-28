#bài này thuật toán chắc chắn đúng nhưng có điều khi em 
#khử gauss xong thì nó cứ bị làm tròn số trong mảng thành ra kết quả chỉ gần đúng thôi ạ
# ANH CHỊ NÀO ĐỌC THÌ GIÚP EM VỚI Ạ HMU HMU
import random
import numpy as np
def inputArray(size, lowerbound, upperbound):
    
    list = []
    for a in range(0,size):
        list2 = []
        for b in range(0, size):
            randomNumber = random.randint(lowerbound, upperbound)
            list2.append(randomNumber)
        list.append(list2)
    
    #create array
    array = np.array(list)
    return array

def subtractingBetweenTwoRow(array, row1, row2, column):
    newRow =[]
    for index in range(0, array.shape[0]):
        if array[row2, column] == 0:
            quotient = 0
        else:
            quotient = float(array[row1, column]/array[row2, column])
        result = round((float(array[row1][index]) - float(quotient)*float(array[row2][index])), 5) 
        newRow.append(result)
    return newRow

def changePositionBetweenTwoRow(array, row1, row2):
    temp = []
    for index in array[row1]:
        temp.append(index)
    array[row1] = array[row2]
    array[row2] = temp

def gaussElimination(array):
    for row in range(0, array.shape[0]):
        if array[row, row] == 0:
            #find another row if its number differnt from 0
            for index in range(row + 1, array.shape[0]):
                if array[index, row] != 0:
                    changePositionBetweenTwoRow(array, row, index)
                    break
        #subtracting
        for index in range(row + 1, array.shape[0]):    
            array[index] = subtractingBetweenTwoRow(array, index, row, row)
    return array

def calculatingDeterminant(array):
    determinant = 1
    for index in range(0, array.shape[0]):
        determinant *= array[index, index]
    return determinant

array = inputArray(3, 0, 100)
print(array)
print(subtractingBetweenTwoRow(array, 0,1,1))
print("**********************")
print(gaussElimination(array))
print("Determinant of matrix is: " + str(calculatingDeterminant(array)))

                    
                    


