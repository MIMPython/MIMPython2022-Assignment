def onlyNum(data):
    for i in listQuestion:
        for j in i:
            try:
                temp = float(j)
            except:
                return False
    return True

def checkNone(data):
    return data != [] and data != [[]for _ in range(len(data))]


def smallestSumByIndex(data):
    index = 0
    for i in range(len(data)):
        if sum(data[i])<sum(data[index]):
            index = i
    return index

def sortBySum(data):
    data = list(data)
    sortList = []
    length = len(data)
    for _ in range(length):
        index = smallestSumByIndex(data)
        sortList.append(data[index])
        data.pop(index)
    return sortList

def checkGoodList(data):
    if (checkNone(data) and checkNone(data)):
        if data == sortBySum(data):
            return True
    return False

if __name__ == "__main__":
    listQuestion = []
    length = int(input("Input number of list: "))
    for i in range(length):
        print("Input all value of {}/{} list (Spacing by a space)".format(i+1,length),end= ": ")
        smallList = map(float,input().split())
        listQuestion.append(list(smallList))
    
    isGood = checkGoodList(listQuestion) and " " or " not "
    print("Your list is{}a good list!".format(isGood))