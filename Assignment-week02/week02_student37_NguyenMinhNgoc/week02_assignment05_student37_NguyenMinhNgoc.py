import re


A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]

# a) Thay giá trị tại vị trí thứ 3 của list A bởi bình phương của chính giá trị đó.
A[2] = A[2]**2
print(A[2])

# b) Xóa phần tử thứ 3 của list A bằng ít nhất hai cách khác nhau
popped1 = A.pop(2)
print(popped1)
#Cách 2
#del A[2]
#print(A)

# C) Thêm vào phía cuối list A một phần tử có giá trị bằng với bình phương của phần tử cuối cùng của list A.
K = A.append(A[len(A) - 1] ** 2)
print(K)

# d) tính số phần tử trong list:
len(A)
print(len(A))

# e) Tính tổng phần tử của list:
total = 0
for x in A:
    total += x
print("Tổng: ", total)

# f) Tính tổng của các phần tử có chỉ số (index) 1, 2, 3, 5 trong list
Tong = A[1] + A[2] + A[3] + A[5]
print("Tong: ", Tong)

# g) Tạo ra một list mới có thứ tự các phần tử đảo ngược với một list đã cho (bằng ít nhất hai cách khác nhau).
E = A.reverse()
print(E)

# Cách 2
D = A.sort(reverse= True)
print(D)

#h) Tách list ban đầu thành hai list, một chỉ chứa các số chẵn, một chỉ chứa các số lẻ.
G = []
H = []
for x in A: 
    if(x % 2 == 0):
        G.append(x)
    else:
        H.append(x)
print(G, H)

#i) Tạo một list B gồm các phần tử của list A được sắp xếp theo thứ tự giảm dần từ trái qua phải.
B = sorted(A, reverse=True)
print(B)

# j) So sánh độ dài của hai list A và list B để thấy rằng sau khi sắp xếp, số phần tử của một list không thay đổi.
print(len(A) == len(B))

# k) Ghép hai list A và list B lại với nhau thành list C.
C = A + B
print(C)
