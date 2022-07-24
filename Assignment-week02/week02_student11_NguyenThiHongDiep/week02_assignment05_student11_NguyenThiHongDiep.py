# a. Thay giá trị tại vị trí thứ 3 của list A bởi bình phương của chính giá trị đó.
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
temp1 = A[2] 
temp1 = temp1 * temp1
A[2] = temp1
print(A) # [70, 43, 49, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]

# b. Xóa phần tử thứ 3 của list A bằng ít nhất hai cách khác nhau (gợi ý: sử dụng hàm pop hoặc hàm delete).
# Cách 1
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
del A[2] 
print(A) # [70, 43, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]

# Cách 2
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
A.pop(2)
print(A) # [70, 43, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]

# c. Thêm vào phía cuối list A một phần tử có giá trị bằng với bình phương của phần tử cuối cùng của list A.
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
x = len(A)
temp2 = A[x-1]
temp2 = temp2 * temp2
A.append(temp2)
print(A) # [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53, 2809]
 
# d. Tính số phần tử trong list.
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
print(len(A)) # 15

# e. Tính tổng các phần tử trong list.
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
sum = 0

for i in A:
    sum = sum + i

print(sum) # 559

# f. Tính tổng của các phần tử có chỉ số (index) 1, 2, 3, 5 trong list.
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
sum = A[1] + A[2] + A[3] + A[5]
print(sum) # 173

# g. Tạo ra một list mới có thứ tự các phần tử đảo ngược với một list đã cho (bằng ít nhất hai cách khác nhau).
# Cách 1
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
A.reverse()
print(A) # [53, 3, 53, 5, 1, 3, 49, 35, 80, 77, 34, 46, 7, 43, 70]

# Cách 2
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
print(A[::-1]) # [53, 3, 53, 5, 1, 3, 49, 35, 80, 77, 34, 46, 7, 43, 70]

# h. Tách list ban đầu thành hai list, một chỉ chứa các số chẵn, một chỉ chứa các số lẻ.
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
even = []
odd = []

for i in range(0,15):
    if A[i] % 2 == 0:
        even.append(A[i]) 
    else:
        odd.append(A[i])

print(even) # [70, 46, 34, 80]
print(odd) # [43, 7, 77, 35, 49, 3, 1, 5, 53, 3, 53]

# i. Tạo một list B gồm các phần tử của list A được sắp xếp theo thứ tự giảm dần từ trái qua phải.
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
B = sorted(A, reverse = True)
print(B)

# j. So sánh độ dài của hai list A và list B để thấy rằng sau khi sắp xếp, số phần tử của một list không thay đổi.
a = len(A)
b = len(B)
print(a == b) # True

# k. Ghép hai list A và list B lại với nhau thành list C.
C = A + B
print(C) # [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53, 80, 77, 70, 53, 53, 49, 46, 43, 35, 34, 7, 5, 3, 3, 1]


