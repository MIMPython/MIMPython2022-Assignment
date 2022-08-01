print("Bài 6: Probability Of Coprime Integers")
print()
#Số nguyên tố cùng nhau là những số có UCLN = 1

from random import *
from math import pi

#Câu a: Hàm tìm UCLN của a và b
def ucln(a, b):
    while a != b:
        if a > b:
            a -= b 
        else:
            b -= a
    return a 

n = int(input("Nhập N = "))
#Lấy ngẫu nhiên hai số tự nhiên không quá N
a = randint(1,n)
b = randint(1,n)
print("Số a là:",a)
print("Số b là:",b)
A = a 
B = b 
print("Vậy ước chung lớn nhất của hai số a và b là:", ucln(a,b))  
print()

#Câu b: Tìm xác suất để hai số nguyên tố cùng nhau
#Cách 1: Kiểm tra tính nguyên tố
k = ucln(a,b)
if k == 1:
    print("a và b là hai số nguyên tố cùng nhau")
else:
    print("a và b không nguyên tố cùng nhau")

#Cách 2: Đếm cặp số nguyên tố
lst = []
for i in range(1, n+1):
    tup = ()
    for j in range(i, n+1):
        tup = (i, j)
        lst.append(tup)
print(lst)

d = 0
omega = len(lst)            #Số lượng các cặp số tự nhiên
for element in lst:
    o1 = element[0]
    o2 = element[1]
    if ucln(o1, o2) == 1:
        d += 1
print("Số cặp số nguyên tố cùng nhau là:", d)
P = d/omega
print("Xác suất để chọn ra cặp số nguyên tố cùng nhau là:", P)


#Câu c: Mối liên hệ giữa giá trị của P và pi ==> P = a/(pi**b) với a, b thuộc N*
print("P*(pi**b) = a")
"""
P*(pi**0) == a0
P*(pi**1) == a1
P*(pi**2) == a2
P*(pi**3) == a3
...
P*(pi**b) == a
"""

for qb in range(10**6):
    qa = P*(pi**qb)
    if qa == int(qa):
        print("Với a =",int(qa))
        print("Với b =",qb)
        break
