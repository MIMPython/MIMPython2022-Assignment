# chưa hoàn thành

import numpy as np

file = open('./additionalFolder/numbers.txt', 'r')
lines = file.read().splitlines()
data = []
for i in lines:
    for j in i.split(' '):
        data.append(int(j))
# change list into a matrix size 20x20
data = np.asarray(data)
data.resize(20, 20)
# function calculating product of four adjacent numbers
def productOfFourNumbers(numList, index):
    res = 1
    for i in range(index, index+4):
        res *= numList[i]
    return res
print(productOfFourNumbers(data[0], 0)) # 34144 (8*2*22*97)
# product of four adjacent numbers in the same direction left
def theLargestProductInLeft(data):
    products = []
    for i in range(len(data)):
        for j in range(len(data)-4):
            products.append(productOfFourNumbers(data[i], j))
    return max(products)

print(theLargestProductInLeft(data)) # 48477312