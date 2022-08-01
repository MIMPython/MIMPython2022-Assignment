path = open("name.txt")
name = path.readline().split(",")
for i in range(len(name)):
    name[i] = name[i].strip().lower() #xóa khoảng trắng
    name[i] = name[i][1 : (len(name[i]) - 1)] # xóa dấu nháy kép

def convert (charr):
    sum = 0
    for i in range(len(charr)):
        sum = sum + ord(charr[i]) - 96  # chuyển về số và tính tổng các chữ cái
    return sum
sumData = 0
for i in range(len(name)):
    st = str(name[i])
    sumData = sumData + convert(st)*(i+1)
print (sumData)

#vd name.txt chứa "MARY","PATRICIA","LINDA","BARBARA","ELIZABETH","JENNIFER","MARIA","SUSAN","MARGARET","DOROTHY"
#thì kết quả 4112