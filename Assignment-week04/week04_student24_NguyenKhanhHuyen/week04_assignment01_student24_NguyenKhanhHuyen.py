def sumOfList(list):
    return sum(list)

def swapPos(list, pos1, pos2):
     list[pos1], list[pos2] = list[pos2], list[pos1]
     return list

def sortList(list):
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if sumOfList(list[i])>sumOfList(list[j]):
                swapPos(list, i, j)

    return list

A = [[1,2], [3,0,4], [2], [4,5]]
print(sortList(A))
