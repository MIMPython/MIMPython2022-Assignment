# Bai tap 1

list = [[1, 2], [3, 0, 4], [2], [4, 5]]
sortedList = sorted(list, key=lambda e: sum(e))
print(sortedList)

# đặt thêm tiêu chí: tích các phần tử


def getMultiply(list):
    result = 1
    for element in list:
        result *= element
    return result


sortedList2 = sorted(list, key=lambda e: getMultiply(e))
print(sortedList2)
