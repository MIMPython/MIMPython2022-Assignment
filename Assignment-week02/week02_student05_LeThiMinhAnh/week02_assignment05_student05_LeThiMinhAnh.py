A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]

# a) Thay giá trị tại vị trí thứ 3 của list A bởi bình phương của chính giá trị đó.
A[2] = A[2]**2

# b) Xóa phần tử thứ 3 của list A bằng ít nhất hai cách khác nhau
#   Cách 1:
A.pop(2)
#   Cách 2:
# del A[2]

# c) Thêm vào phía cuối list A một phần tử có giá trị bằng với bình phương của phần tử cuối cùng của list A.
A.append(A[len(A)-1]**2)

# d) Tính số phần tử trong list
print("So phan tu:", len(A))

# e) Tính tổng các phần tử trong list.
print("Tong phan tu:", sum(A))

# f) Tính tổng của các phần tử có chỉ số (index) 1, 2, 3, 5 trong list.
print("Tong cac phan tu co chi so 1, 2, 3, 5:", A[1]+A[2]+A[3]+A[5])

# g) Tạo ra một list mới có thứ tự các phần tử đảo ngược với một list đã cho (bằng ít nhất hai cách khác nhau).
#   Cách 1:
newList = A.copy()
newList.reverse()
#   Cách 2:
newList = A[::-1]

# h) Tách list ban đầu thành hai list, một chỉ chứa các số chẵn, một chỉ chứa các số lẻ.
evenList = []
oddList = []
for i in A:
    if i % 2 == 0:
        evenList.append(i)
    else:
        oddList.append(i)

# i) Tạo một list B gồm các phần tử của list A được sắp xếp theo thứ tự giảm dần từ trái qua phải.
B = A.copy()
B.sort(reverse=True)

# j) So sánh độ dài của hai list A và list B để thấy rằng sau khi sắp xếp, số phần tử của một list không thay đổi.
if len(A) == len(B):
    print("Do dai hai list A va B bang nhau")
elif len(A) > len(B):
    print("Do dai list A lon hon list B")
else:
    print("Do dai list A nho hon list B")

# k) Ghép hai list A và list B lại với nhau thành list C.
C = A + B
