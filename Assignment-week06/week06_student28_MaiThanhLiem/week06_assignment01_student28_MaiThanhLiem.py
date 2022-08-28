import numpy, time

# a
def random2DArray(rowsNumber, columnsNumber, upperBound):
    return numpy.random.randint(upperBound, size=(rowsNumber, columnsNumber))


# b
def columnSums(arrayA):
    resultA = []
    sumOfColumn = 0
    numberOfArrayRows = len(arrayA)
    numberOfArrayColumns = len(arrayA[0])

    for i in range(numberOfArrayColumns):
        for j in range(numberOfArrayRows):
            sumOfColumn += arrayA[j][i]
        resultA.append(sumOfColumn)
        sumOfColumn = 0

    return resultA


# c
def ndarrayRandomArray(rowsNumber, columnsNumber, upperBound):
    return numpy.ndarray(
        shape=(rowsNumber, columnsNumber),
        dtype=int,
        buffer=numpy.random.randint(upperBound, size=(rowsNumber, columnsNumber)),
    )


def ndarrayColumnSums(arrayB):
    resultB = numpy.ndarray.sum(arrayB, axis=0, dtype=int)
    return resultB


# e
def rowSums(arrayA):
    resultA = []
    sumOfRow = 0
    numberOfArrayRows = len(arrayA)
    numberOfArrayColumns = len(arrayA[0])

    for i in range(numberOfArrayRows):
        for j in range(numberOfArrayColumns):
            sumOfRow += arrayA[i][j]
        resultA.append(sumOfRow)
        sumOfRow = 0

    return resultA


def ndarrayRowSums(arrayB):
    resultB = numpy.ndarray.sum(arrayB, axis=1, dtype=int)
    return resultB


# d
startTimeCreating1 = time.time()
array1 = random2DArray(100, 100, 2**31)
stopTimeCreating1 = time.time()
timeCreating1 = stopTimeCreating1 - startTimeCreating1

startTimeColSums1 = time.time()
result1_1 = columnSums(array1)
stopTimeColSums1 = time.time()
timeSums1_1 = stopTimeColSums1 - startTimeColSums1

startTimeRowSums1 = time.time()
result1_2 = rowSums(array1)
stopTimeRowSums1 = time.time()
timeSums1_2 = stopTimeRowSums1 - startTimeRowSums1


startTimeCreating2 = time.time()
array2 = ndarrayRandomArray(100, 100, 2**31)
stopTimeCreating2 = time.time()
timeCreating2 = stopTimeCreating2 - startTimeCreating2

startTimeColSums2 = time.time()
result2_1 = ndarrayColumnSums(array2)
stopTimeColSums2 = time.time()
timeSums2_1 = stopTimeColSums2 - startTimeColSums2

startTimeRowSums2 = time.time()
result2_2 = ndarrayRowSums(array2)
stoptimeRowSums2 = time.time()
timeSums2_2 = stoptimeRowSums2 - startTimeRowSums2


print("Method 1:", timeCreating1, "\t", timeSums1_1, "\t", timeSums1_2)
print("Method 2:", timeCreating2, "\t", timeSums2_1, "\t", timeSums2_2)


with open(
    ".\\additionalFolder\\week06_assignment01_student28_MaiThanhLiem_data.md", "a"
) as function:
    """
    | Creating |         | Columns Sum |          | Rows Sum |          |
    | :------: | :-----: | :---------: | :------: | :------: | :------: |
    | Method1  | Method2 |  Method 1   | Method 2 | Method 1 | Method 2 |

    """
    function.write(
        f"|{timeCreating1}|{timeCreating2}|{timeSums1_1}|{timeSums2_1}|{timeSums1_2}|{timeSums2_2}\n"
    )
