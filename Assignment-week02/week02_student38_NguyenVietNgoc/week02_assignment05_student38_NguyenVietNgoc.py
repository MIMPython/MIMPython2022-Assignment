A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]


# a) Thay giá trị tại vị trí thứ 3 của list A bởi bình phương của chính giá trị đó
A[2] = A[2]**2
print (f"A = {A}")    # A = [70, 43, 49, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]

# b) Xóa phần tử thứ 3 của list A 
del A[2]
print (f"A = {A}")    # A = [70, 43, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]

A.pop(2)
print (f"A = {A}")   # A = [70, 43, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]

# c) Thêm vào phía cuối list A một phần tử có giá trị bằng với bình phương của phần tử cuối cùng của list A
A.append(A[-1]**2)
print (f"A = {A}")    # A = [70, 43, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53, 2809]

# d) Tính số phần tử trong list.
print (f"element number = {len(A)}") # element number = 14

# e) Tính tổng các phần tử trong list.
print (sum(A)) # 3315

# f) Tính tổng của các phần tử có chỉ số (index) 1, 2, 3, 5 trong list.
sum2 = 0
index = (1, 2, 3, 5)
for i in index:
    sum2 += A[i-1]
print (sum2) # 227

# g) Tạo ra một list mới có thứ tự các phần tử đảo ngược với một list đã cho.
# cách 1:
A1 = A
A1.reverse()
print (f"A1 = {A1}")   # A1 = [2809, 53, 3, 53, 5, 1, 3, 49, 35, 80, 77, 34, 43, 70]

#cách 2:
A = [70, 43, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53, 2809]
A2 = []
for i in range(len(A)):
    A2.insert(0, A[i])   
print (f"A2 = {A2}")   # A2 = [2809, 53, 3, 53, 5, 1, 3, 49, 35, 80, 77, 34, 43, 70]

# h) Tách list ban đầu thành hai list, một chỉ chứa các số chẵn, một chỉ chứa các số lẻ.
A2 = []
A3 = []

for i in range(len(A)):
    if A[i] % 2 == 0:
        A2.append(A[i])
    else:
        A3.append(A[i])

print (f"Even list:  {A2}")  # Even list:  [70, 34, 80]
print (f"Odd list:   {A3}")  # Odd list:   [43, 77, 35, 49, 3, 1, 5, 53, 3, 53, 2809]

# i) Tạo một list B gồm các phần tử của list A được sắp xếp theo thứ tự giảm dần từ trái qua phải.
# A = [70, 43, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53, 2809]
B = A
B.sort(reverse = True)
print (f"B = {B}")     # [2809, 80, 77, 70, 53, 53, 49, 43, 35, 34, 5, 3, 3, 1]

# j) So sánh độ dài của hai list A và list B để thấy rằng sau khi sắp xếp.
A = [70, 43, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53, 2809]
print (len(A) == len(B))   # True

# k) Ghép hai list A và list B lại với nhau thành list C.
C = A + B
print (f"C = {C}")  # C = [70, 43, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53, 2809, 
                    #      2809, 80, 77, 70, 53, 53, 49, 43, 35, 34, 5, 3, 3, 1]

