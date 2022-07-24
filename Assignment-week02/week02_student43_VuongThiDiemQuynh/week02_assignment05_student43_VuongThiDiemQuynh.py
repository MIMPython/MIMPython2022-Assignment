"""
    A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
"""
# (a) Thay giá trị tại vị trí thứ 3 của list A bởi bình phương của chính giá trị đó.
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
A[2] = A[2]**2
print(A)
#(b) Xóa phần tử thứ 3 của list A bằng ít nhất hai cách khác nhau (gợi ý: sử dụng hàm pop hoặc hàm delete).
    #1 - Use the del statement
del A[2]
print(A)
    #2 - removing an Item Using the pop() Method
Q = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
new_A = Q.pop(2)
print(Q)

#(c) Thêm vào phía cuối list A một phần tử có giá trị bằng với bình phương của phần tử cuối cùng của list A.
size = len(A)
index = size-1
A.append(A[index])
print(A)

#(d) Tính số phần tử trong list.
    #1 - using len() method
print(len(A))
    #2
count = 0
for item in A:
    count = count + 1
print(count)

#(e) Tính tổng các phần tử trong list.
sum_1 = 0
for item in A:
    sum_1 = sum_1 + item
print(sum_1)

#(f) Tính tổng của các phần tử có chỉ số (index) 1, 2, 3, 5 trong list.
sum_2 = A[1] + A[2] + A[3] +A[5]
print(sum_2)

#(g) Tạo ra một list mới có thứ tự các phần tử đảo ngược với một list đã cho (bằng ít nhất hai cách khác nhau).
    #1 - using reverse() method
A.reverse()
print(A)
    #2 - using insert() method
result = []
for i in A:
    result.insert(0,i)
print(result)
    #3 
def reverse_list(A):
    for i in range(1,len(A)+1):
        return A[len(A) - i]
print(A)

#(h) Tách list ban đầu thành hai list, một chỉ chứa các số chẵn, một chỉ chứa các số lẻ.
even_list = []
odd_list = []
for i in A:
    if i%2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)
print(even_list)
print(odd_list)


#(i) Tạo một list B gồm các phần tử của list A được sắp xếp theo thứ tự giảm dần từ trái qua phải.
B = []
A.sort()
A.reverse()
B = A[:]
print(B)

#(j) So sánh độ dài của hai list A và list B để thấy rằng sau khi sắp xếp, số phần tử của một list không thay đổi.
if len(A) == len(B):
    print('length of A = length of B')
else:
    print('length of A is not equal length of B')

#(k) Ghép hai list A và list B lại với nhau thành list C.
A.extend(B)
print(A)