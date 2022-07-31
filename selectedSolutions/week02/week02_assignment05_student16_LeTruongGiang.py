
#a) Thay giá trị tại vị trí thứ 3 của list A bởi bình phương của chính giá trị đó.
import re


A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
A[2] = A[2]**2
print(A)

#b) Xóa phần tử thứ 3 của list A bằng ít nhất hai cách khác nhau (gợi ý: sử dụng hàm pop hoặc hàm delete).
'''pop'''
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
A.pop(2)
print(A)

'''delete'''
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
del A[2]
print(A)

'''remove'''
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
A.remove(A[2])
print(A)

#c) Thêm vào phía cuối list A một phần tử có giá trị bằng với bình phương của phần tử cuối cùng của list A.
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
A.append(A[len(A) - 1]**2)
print(A)

#d) Tính số phần tử trong list.
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
print(f"Số phần tử trong list: {len(A)}")

#e) Tính tổng các phần tử trong list.
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
def sum_of_arr(arr):
    sum=0
    for i in arr:
        sum += i
    return sum
print(f"Tổng các phần tử trong list: {sum_of_arr(A)}")

#f) Tính tổng của các phần tử có chỉ số (index) 1, 2, 3, 5 trong list.
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
sum = A[1] + A[2] + A[3] + A[5]
print(f"Tổng của các phần tử có chỉ số (index) 1, 2, 3, 5 trong list: {sum}")

#g) Tạo ra một list mới có thứ tự các phần tử đảo ngược với một list đã cho (bằng ít nhất hai cách khác nhau).
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]

#slicing methods
B = A[::-1]
print(B)

#reverse methods
C = A
C.reverse()
print(C)
    
#h) Tách list ban đầu thành hai list, một chỉ chứa các số chẵn, một chỉ chứa các số lẻ.
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
B = []
C = []
for i in A:
    if i%2 == 0:
        B.append(i)
    else:
        C.append(i)
print(B)
print(C)

#i) Tạo một list B gồm các phần tử của list A được sắp xếp theo thứ tự giảm dần từ trái qua phải.
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
B = A
B.sort(reverse=True)
print(B)

#j) So sánh độ dài của hai list A và list B để thấy rằng sau khi sắp xếp, số phần tử của một list không thay đổi.
_lenA = len(A)
print(f"Độ dài của list A là {_lenA}")

_lenB = len(B)
print(f"Độ dài của list B là {_lenB}")

if _lenA == _lenB:
    print("Thấy rằng sau khi sắp xếp, số phần tử của một list không thay đổi.")
    
#k) Ghép hai list A và list B lại với nhau thành list C.
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
C = A
C.extend(B)
print(C)
