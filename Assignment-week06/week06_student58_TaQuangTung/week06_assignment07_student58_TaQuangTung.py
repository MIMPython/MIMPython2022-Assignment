from tkinter.tix import COLUMN


print("Bài 7: Largest Product In A Grid")

def docfile(path):
    lst = []
    file = open(path, 'r', encoding='utf-8')
    #Đọc file txt cơ bản
    for line in file:
        data = line.strip()
        data.split()
        lst.append(data)
    
    #Tách chuỗi vào mảng
    ln = []
    for ele in lst:
        k = ele.split()
        ln.append(k)
    return ln
    file.close()
lst = docfile(r"D:\MIM Python\week06_student58_TaQuangTung\additionalFolder\Largestproduct.txt")
print(lst)


#Ép kiểu thành số nguyên của mảng
A = []                          #Mảng 2D hoàn thiện các số nguyên
for mang in lst:
    B = []
    for element in mang:
        ele = int(element)
        B.append(ele)
    A.append(B)


#Xử lý theo hàng ngang
ngang = []
for row in range(20):
    for column in range(3, 20):
        tich = A[row][column-3] * A[row][column-2] * A[row][column-1] * A[row][column]
        ngang.append(tich)
print(max(ngang))           #Giá trị lớn nhất của các tích số theo hàng ngang


#Xử lý theo hàng dọc
doc = []
for column in range(20):
    for row in range(3, 20):
        tich = A[row-3][column] * A[row-2][column] * A[row-1][column] * A[row][column]
        doc.append(tich)
print(max(doc))             #Giá trị lớn nhất của các tích số theo hàng dọc


#Xử lý theo đường chéo chính
chinh = []
for row in range(3, 20):
    for column in range(3, 20):
        tich = A[row-3][column-3] * A[row-2][column-2] * A[row-1][column-1] * A[row][column]
        chinh.append(tich)
print(max(chinh))           #Giá trị lớn nhất của các tích số nằm trên đường chéo chính


#Xử lý theo đường chéo phụ
phu = []
for row in range(3, 20):
    for column in range(3, 20):
        tich = A[row-3][column] * A[row-2][column-1] * A[row-1][column-2] * A[row][column-3]
        phu.append(tich)
print(max(phu))

print("Vậy tích số lớn nhất của 4 số liên tiếp là:", max(max(ngang), max(doc), max(chinh), max(phu)))
