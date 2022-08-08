
def sortList():
    list = []
    size = int(input())

    for i in range (size):
        sub_list = []
        size_of_sublist = int(input())
        for j in range (size_of_sublist):
            value = int (input())
            sub_list.append(value)
        list.append(sub_list)
    print (list)

    print (sorted(list, key = sum))

sortList()

