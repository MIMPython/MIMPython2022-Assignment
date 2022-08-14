print("Bài 6: Command Line Arguments")
import re

def hocvien(ten, tuan, baitap):
    ten = ten.strip()       #Xóa khoảng trắng dư thừa
    t = ten.split()
    tene = ""
    for i in t:
        tene += i
    
    #Chuyển đổi chữ có dấu thành không dấu
    patterns = {
        '[àáảãạăắằẵặẳâầấậẫẩ]': 'a',
        '[đ]': 'd',
        '[èéẻẽẹêềếểễệ]': 'e',
        '[ìíỉĩị]': 'i',
        '[òóỏõọôồốổỗộơờớởỡợ]': 'o',
        '[ùúủũụưừứửữự]': 'u',
        '[ỳýỷỹỵ]': 'y'
    }
    output = tene
    for regex, replace in patterns.items():
        output = re.sub(regex, replace, output)
        
    outp = output.split()
    l = ""
    for i in outp:
        l += i

    #In kết quả ra màn hình
    print(f"week{tuan}_assignment{baitap:02d}_{l}.py")

ten = input("Tên học viên: ")
tuan = int(input("STT tuần: "))
baitap = int(input("STT bài tập: "))
hocvien(ten, tuan, baitap)

#hocvien(Quang Tung, 2, 13) = week02_assignment13_QuangTung.py
