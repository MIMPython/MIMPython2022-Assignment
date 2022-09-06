
def main(lista):
    try:
        sumList = 0
        for i in range(0,len(lista)):
            sumList += lista[i]
        meanList = sumList/len(lista)
        print(meanList)
    except ZeroDivisionError:
        print("Empty list") 
    except TypeError:
        print("List contain non-numeric characters")
    
if __name__ == '__main__':  
    input = []
    main(input)
