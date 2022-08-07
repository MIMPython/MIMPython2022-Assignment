# This assignment may hard with many student, 
# but it only hard if you don't know to input by reading a file in python
def caculateSumlist(sortedContent):
    sumlist = []
    for StringContent in (sortedContent):
        valueChar = []
        for char in str(StringContent).upper():
            valueChar.append(ord(char)-64) #The first letter start at 65 in ASCII Code so we must subtract 64 unit
    sumlist.append(sum(valueChar))
    return sumlist

def nameScore(sumlist):
    for index in range(len(sumlist)):
        sumlist[index]*=index
    return sumlist
if __name__=="__main__":

    openFile = open("names.txt",mode = 'r',encoding = 'utf-8')
    textContent = openFile.read()
    listContent = (textContent.replace("\"","")).split(",")
    openFile.close()

    sortedContent = sorted(listContent)

    sumlist = caculateSumlist(sortedContent)

    
    #Caculate each name score
    nameScoreAnswer = nameScore(sortedContent)
    print(nameScoreAnswer) #871198282
    