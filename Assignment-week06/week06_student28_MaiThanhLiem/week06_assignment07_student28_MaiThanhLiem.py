import numpy as np


with open(
    ".\\additionalFolder\\week06_assignment07_student28_MaiThanhLiem_data.txt", "r"
) as f:
    data = f.read().splitlines()

for i in range(len(data)):
    data[i] = data[i].split()
    for j in range(len(data[i])):
        data[i][j] = int(data[i][j])

data = np.array(data)
f.close()


def colProdMax(data):
    colProd = []
    for i in range(len(data) - 3):
        for j in range(len(data[0])):
            colProd.append(
                data[i][j] * data[i + 1][j] * data[i + 2][j] * data[i + 3][j]
            )
            
    return max(colProd)


def rowProdMax(data):
    rowProd = []
    for j in range(len(data[0]) - 3):
        for i in range(len(data)):
            rowProd.append(
                data[i][j] * data[i][j + 1] * data[i][j + 2] * data[i][j + 3]
            )

    return max(rowProd)


def diagProdMax(data):
    diagProd = []
    for i in range(len(data) - 3):
        for j in range(len(data[0]) - 3):
            diagProd.append(
                data[i][j]
                * data[i + 1][j + 1]
                * data[i + 2][j + 2]
                * data[i + 3][j + 3]
            )
        
    for i in range(len(data) - 3):
        for j in range(len(data[0]), 3, -1):
            diagProd.append(
                data[i][len(data[0]) - j]
                * data[i + 1][len(data[0]) - j - 1]
                * data[i + 2][len(data[0]) - j - 2]
                * data[i + 3][len(data[0]) - j - 3]
            )
        
    return max(diagProd)


allProds = [colProdMax(data), rowProdMax(data), diagProdMax(data)]
print(max(allProds))  # 70600674
