print("Bài 12: Ma trận dạng xoắn ốc ra ngoài")
from math import sqrt

from sympy import false, true
n = int(input("n = "))

mangnho = []
manglon = []
for a in range(n):
    if a**2 <= n:
        mangnho.append(a) 
    else:
        manglon.append(a)

#Thuật toán kiểm tra số chính phương
def sochinhphuong(n):
    for i in range(1,n):
        ig = i
        if n / i == ig:
            return 1
            break
scp = sochinhphuong(n)

if scp == 1:
    dodai = max(mangnho)
else:
    dodai = min(manglon) 

#Tạo bảng ma trận bằng lst
lst = []
for i in range(dodai):
    A = []
    for j in range(dodai):
        k = 0
        A.append(k)
    lst.append(A)



#Thuật toán ma trận xoắn ốc
vti = 0
vtj = dodai-1
kt = 1

for l in range(dodai**2, 0, -1):
    lst[vti][vtj] = l

    #Đi xuống dưới
    if kt == 1:
        if vti == dodai-1 or lst[vti+1][vtj] != 0:
            vtj -= 1
            kt = 2
            continue
        else:
            vti += 1
    
    #Đi sang bên trái
    if kt == 2:
        if vtj == 0 or lst[vti][vtj-1] != 0:
            vti -= 1
            kt = 3
            continue
        else:
            vtj -= 1

    #Đi lên trên
    if kt == 3:
        if vti == 0 or lst[vti-1][vtj] != 0:
            vtj += 1
            kt = 4
            continue
        else:
            vti -= 1

    #Đi sang phải
    if kt == 4:
        if lst[vti][vtj+1] != 0:
            vti += 1
            kt = 1
            continue
        else:
            vtj += 1


if scp == 1:
    for t in lst:
        print(t)
else:
    supermang = []
    hieu = dodai**2 - n 
    for giatri in range(1,hieu+1):
        ptubo = n+giatri
        supermang.append(ptubo)
        for x in range(dodai):
            for y in range(dodai):
                if lst[x][y] == ptubo:
                    lst[x][y] *= 0
    for pt in lst:
        print(pt)
