def readfile(path):
    file = open(path,"r" , encoding = 'utf-8')
    for line in file:
        data = line.strip() #xóa khoảng trắng dư thừa
    data1 = data.split(",")
    return(data1)
    
    file.close()
doc = readfile("names.txt")
print(doc)


