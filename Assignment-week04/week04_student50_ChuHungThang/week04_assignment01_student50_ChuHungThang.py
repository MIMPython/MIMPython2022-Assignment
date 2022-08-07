def sortList(A):
    B = {}
    for i in A:
        sumOfEachList = sum(i)
        B.update({f'{i}':sumOfEachList})
    listItem = B.items()
    listItemSorted = sorted(listItem, key=lambda item: item[1])
    dictKetQua = dict(listItemSorted)
    listKetQua = dictKetQua.keys()
    list(listKetQua)
    print(listKetQua)
A = [[1,2], [3,0,4], [2], [4,5]]
sortList(A)
