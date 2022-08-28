print("Bài 1: Numpy")
print()

from cProfile import label
from time import perf_counter

#Câu a) Mảng ma trận hai chiều với m hàng và n cột

def matrix2D(m, n):
    A = []
    for i in range(m):
        B = []
        for j in range(n):
            B.append(int(input(f"Phần tử thứ {j} của hàng thứ {i} là: ")))
        A.append(B)
    # Ma trận cỡ mxn là:    
    return A
m = int(input("Nhập số hàng của ma trận: "))
n = int(input("Nhập số cột của ma trận: "))
haichieu = matrix2D(m, n)
print(haichieu)
print()

#Câu b) Tính tổng các số thuộc cùng một cột của ma trận
start1 = perf_counter()
def sum_of_column(haichieu):
    lst = []
    for column in range(n):
        sum = 0
        for row in range(m):
            sum += haichieu[row][column]
        lst.append(sum)
    print("result1 =", lst)
sum_of_column(haichieu)
end1 = perf_counter()
print()

#Câu c) Sử dụng kiểu dữ liệu numpy.ndarray để thực hiện tạo ma trận 2D
import numpy as np

arr = np.array(haichieu)
print(f"Mảng hai chiều qua thư viện numpy là: \n{arr}")
print()

start2 = perf_counter()
tong = arr.sum(axis = 0)
print("result2 =", tong)
end2 = perf_counter()
print()

#d) So sánh tốc độ thực hiện hai hàm tính tổng theo cột
d1 = end1 - start1
d2 = end2 - start2
print("Thời gian cách 1 chạy theo cột được là:", end1 - start1)
print("Thời gian cách 2 chạy theo cột được là:", end2 - start2)

import matplotlib.pyplot as plt

plt.bar(x = ["Thủ công cột", "Thư viện cột"], height = [d1, d2])
plt.title("SO SÁNH KHOẢNG THỜI GIAN THEO CỘT")
plt.xlabel("Các cách làm theo cột")
plt.ylabel("Khoảng thời gian theo cột")
plt.show()

print()
print()

#e) Tính tổng các số thuộc cùng một hàng

start3 = perf_counter()
def sum_of_row(haichieu):
    lst = []
    for row in range(m):
        sum = 0
        for column in range(n):
            sum += haichieu[row][column]
        lst.append(sum)
    print("result3 =", lst)
sum_of_row(haichieu)            #Tổng các phần tử theo hàng thủ công
end3 = perf_counter()
print()

start4 = perf_counter()
tong = arr.sum(axis = 1)        #Tổng các phần tử theo hàng thư viện
print("result4 =", tong)
end4 = perf_counter()
print()

d3 = end3 - start3
d4 = end4 - start4
print("Thời gian cách 1 chạy theo hàng được là:", end3 - start3)
print("Thời gian cách 2 chạy theo hàng được là:", end4 - start4)

plt.bar(x = ["Thủ công hàng", "Thư viện hàng"], height = [d1, d2])
plt.title("SO SÁNH KHOẢNG THỜI GIAN THEO HÀNG")
plt.xlabel("Các cách làm theo hàng")
plt.ylabel("Khoảng thời gian theo hàng")
plt.show()
