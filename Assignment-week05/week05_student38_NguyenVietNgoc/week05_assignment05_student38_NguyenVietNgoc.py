# a)
def infiniteLoop1 ():
    while 1: 1

# b)
def infiniteLoop2 ():
    infiniteList = [0]
    for i in infiniteList:
        infiniteList.append(i + 1)

# c)
