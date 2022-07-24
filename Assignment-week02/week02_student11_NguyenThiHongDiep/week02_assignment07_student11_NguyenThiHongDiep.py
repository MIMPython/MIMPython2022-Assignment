def Encrypt(PlainText, key): # Hàm mã hoá
    CipherText = "" # Khai báo văn bản thô là một văn bản rỗng
    
    for i in PlainText:
        if i != ' ':
            number = ord(i) - 65; # ord trả về vị trí của ký tự trong bảng mã ASCII, chữ A trong bảng mã ASCII là 65
            number = (number + key) % 26 # Bảng chữ cái có 26 chữ cái
            CipherText = CipherText + chr(number + 65) # (number + 65) trả về vị trí của ký tự đó trong bảng mã ASCII, chr trả về ký tự ứng với vị trí đó
        else:
            CipherText = CipherText + i
    return CipherText

def Decrypt(CipherText, key): # Hàm giải mã
    PlainText = "" # Khai báo văn bản mật mã là một văn bản rỗng
    
    for i in CipherText:
        if i != ' ':
            number = ord(i) - 65
            number = (number - key + 26) % 26 # Cộng thêm 26 vì tránh trường hợp (number - key) là một số âm
            PlainText = PlainText + chr(number + 65)
        else:
            PlainText = PlainText + i 
    return PlainText

def main():
    p = input("Nhap thong diep can ma hoa: ")
    p = p.upper(); # Viết hoa thông điệp cần mã hoá
    key = 13 # Mã Caesar ROT-13
    
    print("Thong diep sau khi ma hoa:", Encrypt(p, key))
    print("Thong diep sau khi giai ma:", Decrypt(Encrypt(p, key), key))

if __name__ == '__main__':
    main()

# Nhap thong diep can ma hoa: Python
# Thong diep sau khi ma hoa: CLGUBA
# Thong diep sau khi giai ma: PYTHON

# Nhap thong diep can ma hoa: nguyen thi hong diep
# Thong diep sau khi ma hoa: ATHLRA GUV UBAT QVRC
# Thong diep sau khi giai ma: NGUYEN THI HONG DIEP

# Nhap thong diep can ma hoa: MIM Python
# Thong diep sau khi ma hoa: ZVZ CLGUBA
# Thong diep sau khi giai ma: MIM PYTHON
