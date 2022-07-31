#Bai5
from xml.dom.minidom import Element


A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
#a
print("(a) Thay giá trị tại vị trí thứ 3 của list A bởi bình phương của chính giá trị đó")
A[2]*=A[2]
print(A)
#b
print("(b) Xóa phần tử thứ 3 của list A bằng ít nhất hai cách khác nhau (gợi ý: sử dụng hàm pop hoặc hàm delete)")
#Cách1
print("Cách 1")
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
del A[2]
print(A)
#Cách2
print("Cách 2")
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
A.pop(2)
print(A)
#c
print("(c) Thêm vào phía cuối list A một phần tử có giá trị bằng với bình phương của phần tử cuối cùng của list A")
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
elem = A[len(A) -1]
A.append(elem*elem)
print(A)
#d
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
print("(d) Số phần tử trong list là", len(A))
#e
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
sum = 0
for i in range(len(A)):
    sum += A[i]
print("(e) Tổng số phần tử trong list là", sum)
#f
sum1 = A[0] + A[1] + A[2] + A[4]
print("(f) Tổng của các phần tử có chỉ số (index) 1, 2, 3, 5 trong list là", sum1)
#g
#Cách1
print("(g)Tạo ra một list mới có thứ tự các phần tử đảo ngược với một list đã cho (bằng ít nhất hai cách khác nhau)")
print("Cách 1")
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
A.reverse()
print(A)
#Cách2
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
print("Cách 2")
C = []
for i in range(1,len(A)+1):
    C.append(A[-i])
print(C)
#h
print("(h) Tách list ban đầu thành hai list, một chỉ chứa các số chẵn, một chỉ chứa các số lẻ")
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
list1 = []
list2 = []
for element in A:
    if element % 2 == 0: 
        list1.append(element)
    else:
        list2.append(element)

print("Tập chỉ chứa các số chẵn là: ", list1)
print("Tập chỉ chứa các số lẻ là: ", list2)
#i
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
A.sort()
B = []
for element in A:
    B.append(element)
B.reverse()
print("(i) list B gồm các phần tử của list A được sắp xếp theo thứ tự giảm dần từ trái qua phải B = ", B)
#j
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
print("(j) So sánh độ dài của hai list A và list B để thấy rằng sau khi sắp xếp, số phần tử của một list không thay đổi")
print(len(A) == len(B))
#k
C = A + B
print(C)