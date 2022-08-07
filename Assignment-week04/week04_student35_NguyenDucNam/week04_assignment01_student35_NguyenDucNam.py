mixedList = [[1,2],[0,3],[3,0,4],[2,1,4],[2],[5,3,1],[4,5]] #input

#Function return 1 if list is OK, rest return 0
def checkList():
    a = 1
    for item in mixedList:
        for i in item: 
            if isinstance(i,int) == False: #Check type of numbers
                a = 0
                break    
    return a

#Function add sorting criteria    
def addition(index):
    return(sum(index),index[0])

#Function print sorted list            
def sortedList():
    if checkList() == 0:
        print('Input is not OK')
    if checkList() == 1:
        initialSort = sorted(mixedList,key=lambda key: sum(key)) #Sort list by each sum
        additionSort = sorted(mixedList,key=addition) #Sort list by each sum and the first number
    print(initialSort)  #output1
    print(additionSort) #output2

if __name__ == '__main__':
    sortedList()
        

