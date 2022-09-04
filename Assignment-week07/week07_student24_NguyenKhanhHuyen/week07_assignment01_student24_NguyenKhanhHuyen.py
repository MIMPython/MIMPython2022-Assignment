def mean(list):
    try:
        sum = 0
        for element in list:
            sum += element
            
        meanVal = sum/len(list)
        
    except ZeroDivisionError:
        print("List đã cho là list rỗng")

    else:
        return meanVal

list = []
print(mean(list))
