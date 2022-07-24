# Mật mã Caesar
#Chương trình mã hóa
#key = 'A B C D E F J H I J K L M N O P Q R S T U V W X Y Z'
# 26: Số chữ cái trong bảng chữ cái Latin
# 65: Mã ascii của chữ A
# 13: ROT-13
s = input("Nhap chuoi can ma hoa:")
a = ""
for x in s:
	a = a + chr((ord(x) - 13 - 65) % 26 + 65)
print(a)
# Chương trình giải mã:
v = input("Nhap chuoi can giai ma: ")
b = ""
for x in v:
    b = b + chr((ord(x) + 13 - 65) % 26 + 65)
print(b)