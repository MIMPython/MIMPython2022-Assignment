print("Nhập thông điệp để chuyển sang thông điệp mã hoá:")
string = str(input())
rot13 = str.maketrans(
    'ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz',
    'NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm')
print(f"Gốc sang mã hoá: {string} <-> {string.translate(rot13)}")

print("Nhập thông điệp đã mã hoá để trở về thông điệp gốc")
string2 = str(input())
rot13_ = str.maketrans(
    'NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm',
    'ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz')
print(f"Mã hoá về gốc: {string2} <-> {string2.translate(rot13_)}")
