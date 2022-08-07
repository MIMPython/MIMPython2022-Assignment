# Cách 1
import math

xA = int(input("xA = "))
yA = int(input("yA = "))
xB = int(input("xB = "))
yB = int(input("yB = "))
xC = int(input("xC = "))
yC = int(input("yC = "))

a = math.sqrt((xC - xB)**2 + (yC - yB)**2)
b = math.sqrt((xC - xA)**2 + (yC - yA)**2)
c = math.sqrt((xB - xA)**2 + (yB - yA)**2)

# Kiểm tra ba cạnh có tạo thành một tam giác không
if (a + b > c) and (a + c > b) and (b + c > a):
    print("Ba diem A, B, C tao thanh tam giac.")
# Tính diện tích tam giác
    p = (a + b + c)/2
    s = math.sqrt(p*(p - a)*(p - b)*(p - c))
    print("Dien tich la %.2f" %s)
else:
    print("Ba diem A, B, C khong tao thanh tam giac.")
"""
xA = -6
yA = 23
xB = 15
yB = -11
xC = 6
yC = -2
Ba diem A, B, C tao thanh tam giac.
Dien tich la 58.50
"""

"""
xA = 1
yA = 2
xB = 3
yB = 4
xC = 5
yC = 6
Ba diem A, B, C khong tao thanh tam giac.
"""

# Cách 2
