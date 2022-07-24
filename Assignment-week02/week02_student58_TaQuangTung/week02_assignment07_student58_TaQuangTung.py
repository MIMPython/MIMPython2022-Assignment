from http.client import LineTooLong

print("Bài 7: Mật mã Caesar")
Rot19 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
ma = input("Nhập các ký tự: ")
luong = len(Rot19) - 1
MA = ma.upper()     #In hoa chuỗi vừa nhập
lst = []            #Mảng gồm các ký tự hoa vừa nhập
for i in MA:
    lst.append(i)      

lt = []             #Mảng sau khi được mã hóa ROT-13
for j in lst:
    l = Rot19.index(j)
    z = l + 13
    if z > luong:
        sau = z - luong
        lt.append(Rot19[sau-1])
    else:
        lt.append(Rot19[z])

#Nối chuỗi
w = ""
for q in lt:
    w += q
print("Ký hiệu sau khi được mã hóa:", w)