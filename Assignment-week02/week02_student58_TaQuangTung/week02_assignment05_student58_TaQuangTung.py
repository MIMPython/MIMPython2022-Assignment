print("Bài 5: Cho List A với các giá trị dưới đây")
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]

print("a) Thay tại vị trí thứ 3 của A bởi bình phương giá trị đó")
A[2] = A[2]**2
print(A)
print()

print("b) Xóa phần tử thứ 3 của list A bằng hai cách khác nhau")
#Cách 1: Sử dụng hàm pop --> xóa theo index
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
A.pop(2)
print(A)
#Cách 2: Sử dụng hàm remove --> xóa theo giá trị
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
d = 0
for i in A:
    d += 1
    if d == 3:
        A.remove(i)
        break
print(A)

print()

print("c) Thêm vào cuối listA phần tử có giá trị bằng bình phương phần tử cuối")
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
k = len(A)
ptA = A[k-1]**2
A.append(ptA)
print("List sau khi thêm là:",A)
print()

A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
print("d) Số phần tử trong list là:", len(A))
print()

A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
print("e) Tổng các phần tử trong list là:", sum(A))
print()

print("f) Tính tổng các phần tử có chỉ số cho sẵn")
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
A1 = A[1]
A2 = A[2]
A3 = A[3]
A5 = A[5]
print("Tổng các phần tử theo chỉ số 1,2,3,5 là:", A1 + A2 + A3 + A5)
print()

print("g) Tạo 1 list đảo ngược với list đã cho bằng hai cách")
#Cách 1: Sử dụng hàm reverse 
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
A.reverse()
B1 = A.copy()
print(B1)
#Cách 2: Sử dụng thuật toán đếm ngược
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
B2 = []
for t in A:
    B2.insert(0, t)
print(B2)

print()

print("h) Tách list ban đầu thành 2 list với 1 chẵn và 1 lẻ")
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
C = []      #List chẵn
L = []      #List lẻ
for u in A:
    if u % 2 == 0:
        C.append(u)
    else:
        L.append(u)
print("List chẵn là:", C)
print("List lẻ là:", L)
print()

print("i) Tạo listB gồm các phần tử của listA được sắp xếp giảm dần trái qua phải")
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
A.sort(reverse = True)
B = A.copy()
print("List B giảm dần là:", B)
print()

print("j) So sánh độ dài listA và listB")
k1 = len(A)
k2 = len(B)
if k1 == k2:
    print("Số phần tử không đổi sau khi sắp xếp")
else:
    print("Số phần tử đã đổi sau khi sắp xếp")
print()

print("k) Ghép hai listA và listB thành listC")
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
C = A + B
print("List C là:", C)
