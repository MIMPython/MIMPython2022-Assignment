from copy import deepcopy

print("Bài 2: Solving Linear Equations")

"""
Tìm x để Ax = b với A là ma trận và b là vecto
"""

# Khởi tạo số hàng và số cột của ma trận A
m = int(input("Nhập số hàng ma trận A: "))
n = int(input("Nhập số cột ma trận A: "))

print("KHỞI TẠO MA TRẬN")
# Khởi tạo ma trận A cỡ mxn
A = []
for i in range(m):
    lt = []
    for j in range(n):
        element = int(input(f"Nhập phần tử thứ {j} của hàng thứ {i} là: "))
        lt.append(element)
    A.append(lt)
print(f"=> Ma trận A cỡ {m}x{n} là:")
print(A)
print()

"""
Giải thích:
+ Ma trận A có cỡ mxn --> Phương trình có m ẩn
+ Vecto b sẽ gồm m giá trị --> b(a1, a2, ..., am)
"""

# Khởi tạo vecto b có m tọa độ
b = []
for i in range(m):
    ele = int(input(f"Nhập tọa độ a{i} = "))
    b.append(ele)
print("Vecto b có tọa độ là: b=", b)
print()

Z = deepcopy(A)         # Copy y hệt Ma trận A

# Nhóm lại các ma trận để giải hệ phương trình tuyến tính
for i in range(m):
    A[i] += [b[i]]
lst = A 
print(lst)              # Đưa cả hai về dạng ma trận tuyến tính
"""
Khi đó ma trận lst sẽ có dạng m hàng, (n+1) cột
"""
print()

"""
Hướng đi:
+ Nếu ma trận A là ma trận vuông thì sẽ tồn tại nghiệm các nghiệm x
+ Nếu ma trận A là ma trận bất kỳ thì sẽ có vô số nghiệm của x
"""

# Giải hệ phương trình tuyến tính bằng phương pháp khử Gauss

print("GIẢI HPT TUYẾN TÍNH BẰNG PHƯƠNG PHÁP KHỬ GAUSS JORDAN")
#Duyệt từng cột
for k in range(n):
    #Tìm kiếm hàng cơ sở
    index = -1
    for i in range(k, m):
        if lst[i][k] != 0:
            index = i
            break 
    
    #Nếu là hàng cơ sở 
    if index != -1:
        #Hoán đổi vị trí hai hàng nếu phần tử đầu tiên có giá trị bằng 0
        if index != k:
            lst[k], lst[index] = lst[index], lst[k]
        #Phương pháp khử Guass
        for i in range(k+1, m):
            d = lst[i][k] / lst[k][k]
            for j in range(n+1):
                #Khử lần lượt từng hàng
                lst[i][j] -= lst[k][j] * d
print("Hệ phương trình sau khi đã khử Gauss là:",lst)
print()

# Tìm rank của ma trận
rankA = n 
d = 0
for i in range(m):
    if lst[i] == [0]*(n+1):
        d += 1

if m - d > rankA:
    print("Hệ phương trình vô nghiệm")
elif m - d < rankA:
    print("Hệ phương trình có vô số nghiệm")
else:
    # RankA = m
    print("Hệ phương trình có nghiệm duy nhất")
    # Khử Gauss Jordan
    for k in range(n-1, -1, -1):
        ind = -1
        for i in range(k, -1, -1):
            if lst[i][k] != 0:
                ind = i
                break
        
        if ind != -1:
            for i in range(k-1, -1, -1):
                d = lst[i][k] / lst[k][k]
                for j in range(n+1):
                    lst[i][j] -= lst[k][j] * d
    
    matrixA = []
    matrixB = []
    for i in range(m):
        Anew = []
        for j in range(n):
            xi = lst[i][j]
            Anew.append(xi)
        matrixA.append(Anew)
        matrixB.append(lst[i][n])
    print("matrixA =", matrixA)
    print("matrixB =", matrixB)

    # Tìm nghiệm của phương trình
    X = []
    for i in range(m):
        x = matrixB[i] / matrixA[i][i]
        X.append(x)
    print(X)
print()
print()

# Giải hệ phương trình tuyến tính bằng thư viện numpy
print("GIẢI HỆ PHƯƠNG TRÌNH TUYẾN TÍNH BẰNG THƯ VIỆN NUMPY")
import numpy as np

lstA = np.array(Z)      # Ma trận hệ số A
lstB = np.array(b)      # Ma trận hệ số B
print("lstA =", lstA)
print("lstB =", lstB)

try:
    X = np.linalg.solve(lstA, lstB)
    print(X)
except:
    print("Hệ phương trình không giải được nghiệm")


# So sánh thời gian thực thi
"""
Ta sử dụng thư viện numpy thường sẽ nhanh hơn cách sử dụng thủ công
"""
