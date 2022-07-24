A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
# (a) Thay giá trị tại vị trí thứ 3 của list A bởi bình phương của chính giá trị đó.
temp = A[3]**2
A[3] = temp
print(A[3])  # 2116
# (b) Xóa phần tử thứ 3 của list A bằng ít nhất hai cách khác nhau(gợi ý: sử dụng hàm pop hoặc hàm delete).
# Cach 1
A.pop(3)
print(A)  # [70, 43, 7, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
# Cach 2
A.remove(A[3])
print(A)  # [70, 43, 7, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]

# (c) Thêm vào phía cuối list A một phần tử có giá trị bằng với bình phương của phần tử cuối cùng của list A.
A.append(A[-1]**2)
print(A)  # [70, 43, 7, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53, 2809]

# (d) Tính số phần tử trong list.
print(len(A))  # 14

# (e) Tính tổng các phần tử trong list.
print(sum(A))  # 3288

# (f) Tính tổng của các phần tử có chỉ số(index) 1, 2, 3, 5 trong list.
index = [1, 2, 3, 5]
sum = 0
for i in index:
    sum += sum + A[i]
print(sum)  # 561

# (g) Tạo ra một list mới có thứ tự các phần tử đảo ngược với một list đã cho(bằng ít nhất hai cách khác nhau).
A1 = A
A1.reverse()
print('A1', A1)  # A1 [2809, 53, 3, 53, 5, 1, 3, 49, 35, 80, 77, 7, 43, 70]

A2 = []
for i in range(len(A)):
    A2.append(A[i])
print('A2', A2)  # A2 [2809, 53, 3, 53, 5, 1, 3, 49, 35, 80, 77, 7, 43, 70]

# (h) Tách list ban đầu thành hai list, một chỉ chứa các số chẵn, một chỉ chứa các số lẻ.
even = []
odd = []
for i in A:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print(odd)  # [2809, 53, 3, 53, 5, 1, 3, 49, 35, 77, 7, 43]
print(even)  # [80, 70]

# (i) Tạo một list B gồm các phần tử của list A được sắp xếp theo thứ tự giảm dần từ trái qua phải.
B = A.copy()
B.sort(reverse=True)
print(B)  # [2809, 80, 77, 70, 53, 53, 49, 43, 35, 7, 5, 3, 3, 1]

# (j) So sánh độ dài của hai list A và list B để thấy rằng sau khi sắp xếp, số phần tử của một list không thay đổi.
print(len(A) == len(B))  # True

# (k) Ghép hai list A và list B lại với nhau thành list C.
C = A + B
print(C)  # [2809, 53, 3, 53, 5, 1, 3, 49, 35, 80, 77, 7, 43, 70, 2809, 80, 77, 70, 53, 53, 49, 43, 35, 7, 5, 3, 3, 1]
