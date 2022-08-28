import numpy as np
import time


def myDet(array):
    for i in range(len(array)):
        if array[i][i] == 0:
            return print("Error.")
        for j in range(i + 1, len(array[0]), 1):
            r = array[j][i] / array[i][i]
            for k in range(len(array[0])):
                array[j][k] = array[j][k] - r * array[i][k]

    detArray = array[0][0]
    for i in range(1, len(array), 1):
        detArray *= array[i][i]
    return detArray


def random2DArray(rowsNumber, lowerBound, upperBound):
    return np.random.randint(lowerBound, upperBound, size=(rowsNumber, rowsNumber))


def numpyDet(array):
    return np.rint(np.linalg.det(array))


exMetric = random2DArray(100, 1, 2**15)
exMetric2 = exMetric[:]

startTimeDet2 = time.time()
print(numpyDet(exMetric2))
stopTimeDet2 = time.time()
timeDet2 = stopTimeDet2 - startTimeDet2

startTimeDet1 = time.time()
print(myDet(exMetric))
stopTimeDet1 = time.time()
timeDet1 = stopTimeDet1 - startTimeDet1


print(f"My method: {timeDet1}")
print(f"Numpy method: {timeDet2}")


with open(
    ".\\additionalFolder\\week06_assignment10_student28_MaiThanhLiem_data.md", "a"
) as function:
    """
    |       My method       |     Numpy method      |
    | :-------------------: | :-------------------: |
    """
    function.write(f"|{timeDet1}|{timeDet2}|\n")
