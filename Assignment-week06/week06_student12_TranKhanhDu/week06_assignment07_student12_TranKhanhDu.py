import numpy as np
filePath = "D:\\VisualCode\\Python\\MIM2022Python\\NumberFile.txt"
with open(filePath) as fileObject:
    reader = fileObject.read().splitlines()
print(reader)

#initialize an array:
arr = np.zeros((20,20), dtype = int)
# store value for array
count = 0
for line in reader:
    listOfNumbers = line.split()
    arr[count] = listOfNumbers
    count += 1
print(arr)
#calculate product
listOfProduct = []
for i in range(0 ,16 ,1):
    for j in range(0, 16, 1):
        product = arr[i,j]*arr[i+1,j+1]*arr[i+2,j+2]*arr[i+3,j+3]
        listOfProduct.append(product)
for i in range(19, 3, -1):
    for j in range(0, 16, 1):
        product = arr[i,j]*arr[i-1,j+1]*arr[i-2,j+2]*arr[i-3,j+3]
        listOfProduct.append(product)
max = max(listOfProduct)
print(max)