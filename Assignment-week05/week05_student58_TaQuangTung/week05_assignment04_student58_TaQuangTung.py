print("Bài 4: Về bờ không khó")

from math import *
from random import randint
"""
Ngày bắt đầu 07/08/2022
Giá cố phiếu ban đầu F1 = 7.24*1000
Lãi suất theo ngày r thỏa mãn 93% <= r <= 107%
Hỏi thời điểm sớm nhất Fn >= 58.69*1000 ?

Bài toán lãi kép
F1 = 7.24*1000
F2 = F1*(1+r)
F3 = F2*(1+r) = F1*(1+r)**2
...
Fn = F1*(1+r)**t 

=> Fn >= F1*(1+r)**t
"""

def price_cophieu(F1, Fn, r):
    F = Fn/F1
    R = 1 + r
    t = log(F, R)
    if F1 >= 1000 and Fn >= 1000:
        if t == int(t):
            print(f"=> Sau {t} ngày thì giá cổ phiếu chạm mốc 58690 đồng")
        else:
            t = int(t) + 1
            print(f"=> Sau ít nhất {t} ngày thì giá cổ phiếu chạm mốc 58690 đồng")
    else:
        if t == int(t):
            print(f"=> Sau {t} ngày thì giá cổ phiếu chạm mốc 58.69 nghìn đồng")
        else:
            t = int(t) + 1
            print(f"=> Sau ít nhất {t} ngày thì giá cổ phiếu chạm mốc 58.69 nghìn đồng")
    
    day = 7
    month = 8
    year = 2022
    day += t 
    if day <= 31:
        print(f"Vào ngày {day}/{month}/{year} thì giá cổ phiếu đã chạm mốc")
    else:
        print(f"Vào ngày {day-31}/{month+1}/{year} thì giá cổ phiếu đã chạm mốc")

#Giá cổ phiếu là số thực
F1 = 7.24*1000
print(f"Giá cổ phiếu ban đầu là: F1 = {F1} đồng")
Fn = 58.69*1000
print(f"Giá cố phiểu cần đạt tới là: Fn = {Fn} đồng")
r = randint(94, 107)/100
print(f"Lãi suất theo ngày là: r = {r*100}%")

price_cophieu(F1, Fn, r)
print()

#Giá cổ phiếu là số thập phân có hai chữ số
F1 = 7.24
print(f"Giá cổ phiếu ban đầu là: F1 = {F1} nghìn đồng")
Fn = 58.69
print(f"Giá cố phiểu cần đạt tới là: Fn = {Fn} nghìn đồng")
r = randint(94, 107)/100
print(f"Lãi suất theo ngày là: r = {r*100}%")

price_cophieu(F1, Fn, r)