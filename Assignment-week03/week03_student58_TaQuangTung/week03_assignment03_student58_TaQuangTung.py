#Xử dụng file names.txt
print("Bài 3: Name scores")

#Đọc file
def docfile(path):
    file = open(path,'r', encoding='utf-8')
    for line in file:
        data = line.strip()
    
    dulieu = data.split(",")
    return (dulieu)
    file.close()
doc = docfile("names.txt")

#Sắp xếp phần tử theo bảng chữ cái
def sapxep(doc):
    doc.sort()
    return doc
sap = sapxep(doc)

#Giá trị của từng số
def giatri(sap):
    arr = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    tichso = 0
    for a in sap:
        tong = 0
        #Tính tổng của từng số (tong)
        for i in a:
            if i in arr:
                chi_so = arr.index(i) + 1
                tong += chi_so
        
        #Vị trí của chuỗi từ (lan)
        lan = sap.index(a) + 1
        tichso += tong*lan
    return tichso
print("Tổng các điểm trong tên tệp là:",giatri(sap))