"""
Bài tập 5. Cho list A với các giá trị dưới đây
"""

import os
import math

A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]

#(a) Thay giá trị tại vị trí thứ 3 của list A bởi bình phương của chính giá trị đó.
print("(a)")
A[2] = A[2] ** 2
print(A)
os.system("pause")

#(b) Xóa phần tử thứ 3 của list A bằng ít nhất hai cách khác nhau (gợi ý: sử dụng 
#    hàm pop hoặc hàm delete).
print("(b)")   
# Cách 1: Dùng del
#del A[2]
#print(A)
# Cách 2: Dùng pop
popped_A = A.pop(2)
print(popped_A)
print(A)
os.system("pause")

#(c) Thêm vào phía cuối list A một phần tử có giá trị bằng với bình phương của phần tử 
#    cuối cùng của list A.
print("(c)")
A.append(A[-1] ** 2)
print(A)
os.system("pause")

#(d) Tính số phần tử trong list.
print("(d)")
print(f"Số phần tử trong list A là {len(A)}")
os.system("pause")

#(e) Tính tổng các phần tử trong list.
print("(e)")
sum_of_A = 0
for x in A:
    sum_of_A += x
print(f"Tổng các phần tử trong A là {sum_of_A}")
os.system("pause")

#(f) Tính tổng của các phần tử có chỉ số (index) 1, 2, 3, 5 trong list.
print("(f)")
sum_1235 = A[1] + A[2] + A[3] +A[5]
print(f"Tổng của các phần tử có chỉ số 1, 2, 3, 5 trong list là {sum_1235}")
os.system("pause")

#(g) Tạo ra một list mới có thứ tự các phần tử đảo ngược với một list đã cho 
#    (bằng ít nhất hai cách khác nhau).
print("(g)")

# Cách 1:
print(A)
reversed_1 = []
for n in A:
    reversed_1.append(n)
reversed_1.reverse()
print(reversed_1)

# Cách 2: Dùng slicing
reversed_2 = []
for n in A:
    reversed_2.append(n)
reversed_2[::-1]
print(reversed_2)

# Cách 3:
reversed_3 = []
for n in A:
    reversed_3.append(n)
n = len(A)
for i in range(n):
    reversed_3.append(A[n-1-i])
print(reversed_3)
os.system("pause")

#(h) Tách list ban đầu thành hai list, một chỉ chứa các số chẵn, một chỉ chứa các số lẻ.
print("(h)")
even_list = []
odd_list = []

for i in range(n):
    if A[i] % 2 == 0:
        even_list.append(A[i])
    else:
        odd_list.append(A[i])
print(f"List các số chẵn: {even_list}")
print(f"List các số lẻ: {odd_list}")
os.system("pause")

#(i) Tạo một list B gồm các phần tử của list A được sắp xếp theo thứ tự giảm dần từ trái 
#    qua phải.
print("(i)")
B = []
for n in A:
    B.append(n)
B.sort(reverse=True)
print(B)
os.system("pause")

#(j) So sánh độ dài của hai list A và list B để thấy rằng sau khi sắp xếp, số phần tử 
#    của một list không thay đổi.
print("(j)")
if len(A) == len(B):
    print("Độ dài 2 list A và B bằng nhau. Vậy sau khi sắp xếp, số phần tử của một list không thay đổi")
else:
    print("Độ dài thay đổi")
os.system("pause")

#(k) Ghép hai list A và list B lại với nhau thành list C.
print("(k)")
C = A + B
print(C)

