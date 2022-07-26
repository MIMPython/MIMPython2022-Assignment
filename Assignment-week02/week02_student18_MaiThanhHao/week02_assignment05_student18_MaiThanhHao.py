A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]

#(a) Thay giá trị tại vị trí thứ 3 của list A bởi bình phương của chính giá trị đó
A[2] = A[2] **2
print(A)

#(b) Xóa phần tử thứ 3 của list A bằng ít nhất hai cách khác nhau (gợi ý: sử dụng hàm pop hoặc hàm delete).
 #Cách 1:
removed_value = A.pop(2)
print("Phần tử thứ 3 bị xóa là: ")
print(removed_value)
print(A)
 #Cách 2:
'''
del A[2]
print(A)
'''


#(c) Thêm vào phía cuối list A một phần tử có giá trị bằng với bình phương của phần tử cuối cùng của list A.

A.append(A[len(A) - 1] **2)
print(A)

#(d) Tính số phần tử trong list.
print("Số phần tử trong list là: ")
print(len(A))

#(e) Tính tổng các phần tử trong list.
def sumOfList(A):
    sum = 0
    for i in range(len(A)):
        sum += A[i]
    return sum
print("Tổng các phần tử trong A : ")
print(sumOfList(A))

#(f) Tính tổng của các phần tử có chỉ số (index) 1, 2, 3, 5 trong list.
def sumOfListIndex(A):
    sum=0
    for i in (1,2,3,5):
        sum += A[i]
    return sum
print("Tong của chúng là:")
print(sumOfListIndex(A))

#(g) Tạo ra một list mới có thứ tự các phần tử đảo ngược với một list đã cho (bằng ít nhất hai cách khác nhau).
A1 = A[:: -1]
print(A1)

#Cách 2: 
'''
  A1 = reversed(A)
  print(A1)    
'''
#(h) Tách list ban đầu thành hai list, một chỉ chứa các số chẵn, một chỉ chứa các số lẻ.
even_list = []
odd_list = []
for i in range(len(A)):
    if (A[i] % 2 == 0):
        even_list.append(A[i])
    else:
        odd_list.append(A[i])
print("List số chắn: ")
print(even_list)
print("List số lẻ: ")
print(odd_list)

#(i) Tạo một list B gồm các phần tử của list A được sắp xếp theo thứ tự giảm dần từ trái qua phải.
B = []
A.sort()
B = A[:]
print(B)
A.reverse()

#(j) So sánh độ dài của hai list A và list B để thấy rằng sau khi sắp xếp, số phần tử của một list không thay đổi.
if (len(A) == len(B)):
    print("Bằng nhau")
else:
    print("Không bằng nhau")

#(k) Ghép hai list A và list B lại với nhau thành list C.
C = []
C = A[:]
for i in B:
    C.append(i)
print(C)
 

