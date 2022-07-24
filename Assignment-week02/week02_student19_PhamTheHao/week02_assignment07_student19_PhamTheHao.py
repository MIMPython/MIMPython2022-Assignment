"""
Bài tập 7. (Mật mã Caesar)
Trong mã hóa, mật mã Caesar thay thế mỗi kí tự trong bảng chữ cái bởi một kí tự khác 
cũng trong bảng chữ cái đó ở vị trí cách nó một đoạn cố định.
ROT-13 là một trong những mã Caesar phổ biến nhất. Hãy viết chương trình mã hóa (chuyển 
từ thông điệp gốc sang thông điệp mã hóa) và chương trình giải mã (chuyển từ thông điệp 
mã hóa sang thông điệp gốc) cho ROT-13.
"""
upper = {chr(ascii) for ascii in range(65,91)}
lower = {chr(ascii) for ascii in range(97,123)}

def encrypt(string):
    result = ''
    for c in string:
        result.append(chr((ord(c) - 64 + 13) %26 + 64))
    return result

def decrypt(string):
    result = ''
    for c in string:
        result.append(chr((ord(c) - 64 - 13) %26 + 64))
    return result

str_1 = input("Nhap vao thong diep") 
print(f"Thong diep sau ma hoa {encrypt(str_1)}")
str_2 = input("Nhap vao thong diep ma hoa")
print(f"Thong diep {decrypt(str_2)}")

