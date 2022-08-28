print("Bài 10: Gauss Elimination")

from time import perf_counter
import copy
#Khởi tạo ma trận vuông cấp n

n = int(input("Nhập kích cỡ của ma trận: "))
lst = []
for i in range(n):
    lt = []
    for j in range(n):
        element = int(input(f"Nhập phần tử thứ {j} của hàng thứ {i} là: "))
        lt.append(element)
    lst.append(lt)
print(f"=> Ma trận vuông cấp {n} là:")
print(lst)

ln = copy.deepcopy(lst)             #Ma trận vuông cỡ ban đầu 


#KHỬ GAUSS

start1 = perf_counter()
mu = 0
#Duyệt từng cột
for k in range(n-1):
    #Tìm kiếm hàng cơ sở
    index = -1
    for i in range(k, n):
        if lst[i][k] != 0:
            index = i
            break 
    
    #Nếu là hàng cơ sở 
    if index != -1:
        #Hoán đổi vị trí hai hàng nếu phần tử đầu tiên có giá trị bằng 0
        if index != k:
            lst[k], lst[index] = lst[index], lst[k]
            mu += 1
        #Phương pháp khử Guass
        for i in range(k+1, n):
            d = lst[i][k] / lst[k][k]
            for j in range(n):
                #Khử lần lượt từng hàng
                lst[i][j] -= lst[k][j] * d

print("Mảng sau khi đã khử Gauss là:",lst)
#Tìm định thức bằng phương pháp thủ công
if lst != []:
    t = 1
    for a in range(n):
        t *= lst[a][a]
    print("Định thức của ma trận thủ công là:",t*((-1)**mu))
end1 = perf_counter()
print()


#THƯ VIỆN NUMPY
import numpy as np
arr = np.array(ln)
print(arr)
#Tìm định thức ma trận qua numpy
start2 = perf_counter()
print("Định thức của ma trận thư viện là:",np.linalg.det(arr))
end2 = perf_counter()
print()


#Tìm độ chênh lệch giữa hai khoảng thời gian
print("Thời gian chạy ma trận thủ công là:", end1-start1)
print("Thời gian chạy ma trận thư viện là:", end2-start2)
