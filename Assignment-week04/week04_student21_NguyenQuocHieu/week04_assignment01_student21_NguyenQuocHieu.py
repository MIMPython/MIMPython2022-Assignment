A = [[1,2], [3,0,4], [2], [4,5]]
def sortList(A):
    B = []
    dictAB = {}
    index = 0
    while index < len(A):
        dictAB[sum(A[index])] = index
        index = index + 1
    sorted_dict = sorted(dictAB.keys())
    for key in sorted_dict:
        i = dictAB[key]
        B.append(A[i])
    return B
def sum(A):
    s = 0
    for element in A:
        s = s + element
    return s    