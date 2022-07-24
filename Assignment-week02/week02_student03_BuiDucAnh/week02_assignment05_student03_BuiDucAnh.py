A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]

#a. Thay giá trị thứ 3
A[2] = A[2]*A[2]
print(A)

#B. Xóa phần tử thứ 3
A.pop(2)
del A[2]
print(A)

#c. Thêm phần tử
x = len(A) #Số phần tử của A
y = x-1
A.insert(x, A[y]*A[y])
print(A)

#d. Số phần tử trong mảng
z = soPhanTu = len(A)
print(soPhanTu)

#e. Tổng các phần tử trong mảng
sum1 = sum(A)
print(sum1)

#f. Tổng 1 số phần tử
sum2 = A[1] + A[2] + A[3] + A[5]
print(sum2)

#g. Đảo chuỗi
#Cách 1
A.reverse()
print(A)
#Cách 2
newA = []
for i in range(0, z):
    newA.insert(i, A[z-i-1])
print(newA)

#h. Tách mảng
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53] #mảng Ban đầu
a = len(A) #Số phần tử mảng A

A1 = [] #Khởi tạo mảng chẵn
A2 = [] #Khởi tạo mảng lẻ

a1 = 0
a2 = 0
for i in range(0, a):
    if A[i]%2 == 0: #tìm phần tử chẵn
        A1.insert(a1, A[i])
        a1 +=1
    else:
        A2.insert(a2, A[i])
        a2 +=1
print(A1)
print(A2)

#i. Sắp xếp
B = A
for i in range(0, a):
    for j in range(0, a-1):
        if B[j] < B[j+1]:
            temp = B[j]
            B[j] = B[j+1]
            B[j+1] = temp

print(B)

#j. So sánh độ dài chuỗi
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53] #mảng A ban đầu
print(len(A) == len(B))

#k. Ghép
C = A + B
print(C)
