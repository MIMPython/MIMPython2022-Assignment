#Bài 5
import os 
"""
1 = Kéo
2 = Búa
3 = Bao
"""
a = int(input("Người thứ nhất nhập:"))
os.system("cls")
b = int(input("Người thứ hai nhập: "))
os.system("cls")
if 1<= a <= 3 and 1 <= b <= 3:
    if a > b: 
        if a == 3 and b == 1:
            print("Người thứ nhất thắng")
        else:
            print("Người thứ hai thắng")
    elif a < b: 
        if a == 1 and b == 3:
            print("Người thứ hai thắng")
        else:
            print("Người thứ nhất thắng")
    else: 
        print("Hòa")